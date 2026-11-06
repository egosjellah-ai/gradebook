from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
            else:
                messages.error(request, 'Role not recognized.')
                return redirect('login')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def admin_dashboard(request):
    users = User.objects.exclude(id=request.user.id).order_by('full_name')

    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(full_name__icontains=search_query) | users.filter(email__icontains=search_query)

    role_filter = request.GET.get('role', 'all')
    if role_filter == 'teacher':
        users = users.filter(role='teacher')
    elif role_filter == 'student':
        users = users.filter(role='student')

    context = {
        'users': users,
        'search_query': search_query,
        'current_role': role_filter,
    }
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='login')
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


@login_required(login_url='login')
def student_dashboard(request):
    return render(request, 'student_dashboard.html')


@login_required(login_url='login')
def teacher_grades(request):
    return render(request, 'teacher_grades.html')


@login_required(login_url='login')
def teacher_grade_card(request):
    return render(request, 'teacher_grade_card.html')


# ==========================================
# MGA BAG-ONG VIEWS PARA SA PAG-CREATE OG USER
# ==========================================

@login_required(login_url='login')
def create_teacher(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            User.objects.create_user(
                email=email,
                full_name=full_name,
                password=password,
                role='teacher'
            )
            messages.success(request, 'Teacher account created successfully!')
            return redirect('admin_dashboard')

    return render(request, 'create_teacher.html')


@login_required(login_url='login')
def create_student(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            User.objects.create_user(
                email=email,
                full_name=full_name,
                password=password,
                role='student'
            )
            messages.success(request, 'Student account created successfully!')
            return redirect('admin_dashboard')

    return render(request, 'create_student.html')
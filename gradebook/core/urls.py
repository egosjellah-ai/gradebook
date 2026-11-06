from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    # Teacher Flow
    path('teacher-grades/', views.teacher_grades, name='teacher_grades'),
    path('teacher-grade-card/', views.teacher_grade_card, name='teacher_grade_card'),

    # User Creation Flow (BAG-O)
    path('create-teacher/', views.create_teacher, name='create_teacher'),
    path('create-student/', views.create_student, name='create_student'),
]
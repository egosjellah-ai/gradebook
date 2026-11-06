from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Create default admin user'

    def handle(self, *args, **kwargs):
        email = 'admin@school.edu'
        password = 'admin123'

        if not User.objects.filter(email=email).exists():
            User.objects.create_user(
                email=email,
                full_name='System Administrator',
                password=password,
                role='admin',
                is_staff=True,
                is_superuser=True
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created admin: {email}'))
        else:
            self.stdout.write(self.style.WARNING('Admin already exists.'))
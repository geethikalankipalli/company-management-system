import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create a superuser for the Render deployment"

    def handle(self, *args, **kwargs):
        username = os.environ.get("RENDER_ADMIN_USERNAME")
        password = os.environ.get("RENDER_ADMIN_PASSWORD")

        if not username or not password:
            self.stdout.write(
                self.style.ERROR("Render admin credentials are not configured.")
            )
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("User already exists.")
            )
        else:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=""
            )
            self.stdout.write(
                self.style.SUCCESS("Render admin user created successfully.")
            )
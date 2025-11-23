#!/usr/bin/env python
"""
Script to create a superuser for the Skills Development Platform
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skilldevplatform.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User


def create_superuser():
    """Create a superuser if it doesn't exist"""
    username = 'admin'
    email = 'admin@skillsdev.com'
    password = 'admin123'
    
    if User.objects.filter(username=username).exists():
        print(f"Superuser '{username}' already exists!")
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Password updated for superuser '{username}'")
    else:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser '{username}' created successfully!")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print("\n⚠️  IMPORTANT: Change the password in production!")
    
    print("\nYou can now login at: http://127.0.0.1:8000/admin/")


if __name__ == '__main__':
    create_superuser()


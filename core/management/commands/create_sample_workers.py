"""
Management command to create sample workers with profiles
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from workers.models import Worker, WorkerSkill
from skills.models import Skill
from datetime import timedelta
import random


class Command(BaseCommand):
    help = 'Creates sample workers with profiles and skills'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating sample workers...'))

        # Get available skills
        skills = list(Skill.objects.filter(is_active=True))
        if not skills:
            self.stdout.write(self.style.ERROR('No skills found. Please create skills first using: python manage.py create_sample_skills'))
            return

        # Departments
        departments = ['Engineering', 'Design', 'Marketing', 'Sales', 'Operations', 'HR', 'Finance', 'Product Management']
        positions = {
            'Engineering': ['Software Engineer', 'Senior Developer', 'DevOps Engineer', 'Full Stack Developer'],
            'Design': ['UI/UX Designer', 'Graphic Designer', 'Product Designer'],
            'Marketing': ['Marketing Manager', 'Digital Marketing Specialist', 'Content Writer'],
            'Sales': ['Sales Representative', 'Sales Manager', 'Account Executive'],
            'Operations': ['Operations Manager', 'Project Coordinator'],
            'HR': ['HR Manager', 'Recruiter', 'HR Specialist'],
            'Finance': ['Financial Analyst', 'Accountant'],
            'Product Management': ['Product Manager', 'Product Owner'],
        }

        # Random profile picture URLs (using Unsplash and other sources for diverse people images)
        profile_pictures = [
            'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1527980965255-d3b416303d12?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1552374196-c4e7ffc6e126?w=400&h=400&fit=crop&crop=faces',
            'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=400&fit=crop&crop=faces',
        ]

        # Workers data
        workers_data = [
            {'first_name': 'John', 'last_name': 'Smith', 'email': 'john.smith@company.com', 'username': 'johnsmith', 'employee_id': 'EMP001'},
            {'first_name': 'Sarah', 'last_name': 'Johnson', 'email': 'sarah.johnson@company.com', 'username': 'sarahjohnson', 'employee_id': 'EMP002'},
            {'first_name': 'Michael', 'last_name': 'Chen', 'email': 'michael.chen@company.com', 'username': 'michaelchen', 'employee_id': 'EMP003'},
            {'first_name': 'Emily', 'last_name': 'Davis', 'email': 'emily.davis@company.com', 'username': 'emilydavis', 'employee_id': 'EMP004'},
            {'first_name': 'David', 'last_name': 'Wilson', 'email': 'david.wilson@company.com', 'username': 'davidwilson', 'employee_id': 'EMP005'},
            {'first_name': 'Jessica', 'last_name': 'Brown', 'email': 'jessica.brown@company.com', 'username': 'jessicabrown', 'employee_id': 'EMP006'},
            {'first_name': 'Daniel', 'last_name': 'Miller', 'email': 'daniel.miller@company.com', 'username': 'danielmiller', 'employee_id': 'EMP007'},
            {'first_name': 'Amanda', 'last_name': 'Taylor', 'email': 'amanda.taylor@company.com', 'username': 'amandataylor', 'employee_id': 'EMP008'},
            {'first_name': 'Robert', 'last_name': 'Anderson', 'email': 'robert.anderson@company.com', 'username': 'robertanderson', 'employee_id': 'EMP009'},
            {'first_name': 'Lisa', 'last_name': 'Martinez', 'email': 'lisa.martinez@company.com', 'username': 'lisamartinez', 'employee_id': 'EMP010'},
            {'first_name': 'James', 'last_name': 'Thomas', 'email': 'james.thomas@company.com', 'username': 'jamesthomas', 'employee_id': 'EMP011'},
            {'first_name': 'Patricia', 'last_name': 'Jackson', 'email': 'patricia.jackson@company.com', 'username': 'patriciajackson', 'employee_id': 'EMP012'},
            {'first_name': 'Christopher', 'last_name': 'White', 'email': 'christopher.white@company.com', 'username': 'christopherwhite', 'employee_id': 'EMP013'},
            {'first_name': 'Linda', 'last_name': 'Harris', 'email': 'linda.harris@company.com', 'username': 'lindaharris', 'employee_id': 'EMP014'},
            {'first_name': 'Matthew', 'last_name': 'Martin', 'email': 'matthew.martin@company.com', 'username': 'matthewmartin', 'employee_id': 'EMP015'},
        ]

        created_count = 0
        for worker_data in workers_data:
            # Check if user already exists
            if User.objects.filter(username=worker_data['username']).exists():
                user = User.objects.get(username=worker_data['username'])
                self.stdout.write(self.style.WARNING(f'User "{worker_data["username"]}" already exists, checking worker profile...'))
            else:
                # Create user
                user = User.objects.create_user(
                    username=worker_data['username'],
                    email=worker_data['email'],
                    password='password123',  # Default password
                    first_name=worker_data['first_name'],
                    last_name=worker_data['last_name'],
                )

            # Check if worker profile exists
            if hasattr(user, 'worker_profile'):
                self.stdout.write(self.style.WARNING(f'Worker profile for "{worker_data["username"]}" already exists, skipping...'))
                continue

            # Select random department and position
            department = random.choice(departments)
            position = random.choice(positions.get(department, ['Employee']))
            
            # Select random profile picture
            profile_pic_url = random.choice(profile_pictures)
            
            # Create worker profile
            worker = Worker.objects.create(
                user=user,
                employee_id=worker_data['employee_id'],
                department=department,
                position=position,
                phone=f'+1-555-{random.randint(100,999)}-{random.randint(1000,9999)}',
                profile_picture_url=profile_pic_url,
                bio=f'Experienced {position} with expertise in {department}. Passionate about professional development and continuous learning.',
                date_of_joining=timezone.now() - timedelta(days=random.randint(30, 1000)),
                is_active=True,
            )

            # Assign random skills to worker (2-4 skills)
            num_skills = random.randint(2, 4)
            worker_skills = random.sample(skills, min(num_skills, len(skills)))
            proficiency_levels = ['beginner', 'intermediate', 'advanced', 'expert']

            for skill in worker_skills:
                proficiency = random.choice(proficiency_levels)
                certification_date = timezone.now() - timedelta(days=random.randint(0, 365)) if random.choice([True, False]) else None
                
                WorkerSkill.objects.create(
                    worker=worker,
                    skill=skill,
                    proficiency_level=proficiency,
                    certification_date=certification_date,
                    notes=f'Certified in {skill.name}',
                    is_active=True,
                )

            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'Created worker: {worker.full_name} ({worker.employee_id}) - {worker.position}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} workers!'))
        self.stdout.write(self.style.WARNING('\nDefault password for all workers: password123'))
        self.stdout.write(self.style.WARNING('Please change passwords in production!'))


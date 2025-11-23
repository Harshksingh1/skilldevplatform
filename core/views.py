from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from skills.models import Skill
from training.models import Course
from workers.models import Worker


def home(request):
    """Home page view"""
    skills = Skill.objects.filter(is_active=True)[:6]
    courses = Course.objects.filter(is_active=True).order_by('-created_at')[:12]
    workers_count = Worker.objects.filter(is_active=True).count()
    
    context = {
        'skills': skills,
        'courses': courses,
        'workers_count': workers_count,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'core/about.html')


@login_required
def dashboard(request):
    """Dashboard view for logged in users"""
    from django.utils import timezone
    import random
    from workers.models import Worker
    
    user = request.user
    context = {}
    
    # Auto-create worker profile if it doesn't exist
    if not hasattr(user, 'worker_profile'):
        # Generate unique employee ID
        max_attempts = 100
        for _ in range(max_attempts):
            employee_id = f'EMP{random.randint(10000, 99999)}'
            if not Worker.objects.filter(employee_id=employee_id).exists():
                break
        else:
            employee_id = f'EMP{int(timezone.now().timestamp())}'
        
        worker = Worker.objects.create(
            user=user,
            employee_id=employee_id,
            department='General',
            position='Employee',
            date_of_joining=timezone.now().date(),
            is_active=True,
        )
    else:
        worker = user.worker_profile
    
    context['worker'] = worker
    context['enrollments'] = worker.enrollments.all()[:5]
    context['completed_courses'] = worker.enrollments.filter(status='completed').count()
        
    return render(request, 'core/dashboard.html', context)

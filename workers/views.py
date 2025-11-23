from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Worker


def worker_list(request):
    """List all workers"""
    workers = Worker.objects.filter(is_active=True)
    
    # Search
    query = request.GET.get('q')
    if query:
        workers = workers.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(employee_id__icontains=query) |
            Q(department__icontains=query) |
            Q(position__icontains=query)
        )
    
    # Filter by department
    department = request.GET.get('department')
    if department:
        workers = workers.filter(department=department)
    
    # Get unique departments for filter
    departments = Worker.objects.filter(is_active=True).values_list('department', flat=True).distinct()
    
    context = {
        'workers': workers,
        'departments': departments,
        'current_department': department,
        'search_query': query,
    }
    return render(request, 'workers/worker_list.html', context)


def worker_detail(request, pk):
    """Detail view for a worker"""
    worker = get_object_or_404(Worker, pk=pk, is_active=True)
    worker_skills = worker.worker_skills.filter(is_active=True)
    enrollments = worker.enrollments.filter(is_active=True)[:5]
    
    context = {
        'worker': worker,
        'worker_skills': worker_skills,
        'enrollments': enrollments,
    }
    return render(request, 'workers/worker_detail.html', context)


@login_required
def my_profile(request):
    """User's own profile"""
    from django.utils import timezone
    import random
    
    # Auto-create worker profile if it doesn't exist
    if not hasattr(request.user, 'worker_profile'):
        # Generate unique employee ID
        max_attempts = 100
        for _ in range(max_attempts):
            employee_id = f'EMP{random.randint(10000, 99999)}'
            if not Worker.objects.filter(employee_id=employee_id).exists():
                break
        else:
            employee_id = f'EMP{int(timezone.now().timestamp())}'
        
        worker = Worker.objects.create(
            user=request.user,
            employee_id=employee_id,
            department='General',
            position='Employee',
            date_of_joining=timezone.now().date(),
            is_active=True,
        )
    else:
        worker = request.user.worker_profile
    
    worker_skills = worker.worker_skills.filter(is_active=True)
    enrollments = worker.enrollments.filter(is_active=True)
    
    context = {
        'worker': worker,
        'worker_skills': worker_skills,
        'enrollments': enrollments,
    }
    return render(request, 'workers/my_profile.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from skills.models import Skill
from .models import Course, Enrollment
from workers.models import Worker
import random


def course_list(request):
    """List all courses"""
    courses = Course.objects.filter(is_active=True).distinct()
    available_skills = Skill.objects.filter(is_active=True).order_by('name')
    
    # Search
    query = request.GET.get('q')
    if query:
        courses = courses.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    # Filter by difficulty
    difficulty = request.GET.get('difficulty')
    if difficulty:
        courses = courses.filter(difficulty_level=difficulty)
    
    # Filter by skill
    skill_query = (request.GET.get('skill') or '').strip()
    normalized_skill_query = skill_query.lower()
    if normalized_skill_query == 'none':
        skill_query = ''
    if skill_query:
        if skill_query.isdigit():
            courses = courses.filter(skills__id=int(skill_query))
        else:
            courses = courses.filter(skills__name__icontains=skill_query)
    
    context = {
        'courses': courses,
        'current_difficulty': difficulty,
        'current_skill': skill_query,
        'search_query': query,
        'available_skills': available_skills,
    }
    return render(request, 'training/course_list.html', context)


def course_detail(request, pk):
    """Detail view for a course"""
    course = get_object_or_404(Course, pk=pk, is_active=True)
    modules = course.modules.filter(is_active=True)
    related_courses = Course.objects.filter(skills__in=course.skills.all(), is_active=True).distinct().exclude(pk=pk)[:4]
    
    # Check if user is enrolled
    is_enrolled = False
    enrollment = None
    if request.user.is_authenticated:
        # Auto-create worker profile if it doesn't exist (for display purposes)
        if not hasattr(request.user, 'worker_profile'):
            # Don't create here, just allow viewing - profile will be created on enrollment
            pass
        else:
            try:
                enrollment = Enrollment.objects.get(worker=request.user.worker_profile, course=course, is_active=True)
                is_enrolled = True
            except Enrollment.DoesNotExist:
                pass
    
    context = {
        'course': course,
        'modules': modules,
        'related_courses': related_courses,
        'is_enrolled': is_enrolled,
        'enrollment': enrollment,
    }
    return render(request, 'training/course_detail.html', context)


@login_required
def enroll_course(request, pk):
    """Enroll worker in a course"""
    course = get_object_or_404(Course, pk=pk, is_active=True)
    
    # Auto-create worker profile if it doesn't exist
    if not hasattr(request.user, 'worker_profile'):
        # Generate unique employee ID
        max_attempts = 100
        for _ in range(max_attempts):
            employee_id = f'EMP{random.randint(10000, 99999)}'
            if not Worker.objects.filter(employee_id=employee_id).exists():
                break
        else:
            # If we couldn't generate a unique ID, use timestamp-based
            employee_id = f'EMP{int(timezone.now().timestamp())}'
        
        # Create worker profile with default values
        worker = Worker.objects.create(
            user=request.user,
            employee_id=employee_id,
            department='General',
            position='Employee',
            date_of_joining=timezone.now().date(),
            is_active=True,
        )
        messages.info(request, f'Worker profile created automatically! Employee ID: {employee_id}. You can update your profile details later.')
    else:
        worker = request.user.worker_profile
    
    # Check if already enrolled
    if Enrollment.objects.filter(worker=worker, course=course, is_active=True).exists():
        messages.warning(request, 'You are already enrolled in this course.')
        return redirect('course_detail', pk=pk)
    
    # Check if course is full
    if course.is_full:
        messages.error(request, 'This course is full.')
        return redirect('course_detail', pk=pk)
    
    # Create enrollment
    Enrollment.objects.create(
        worker=worker,
        course=course,
        status='enrolled'
    )
    
    messages.success(request, f'Successfully enrolled in {course.title}!')
    return redirect('course_detail', pk=pk)


@login_required
def my_courses(request):
    """List courses enrolled by the current user"""
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
        messages.info(request, f'Worker profile created automatically! Employee ID: {employee_id}.')
    else:
        worker = request.user.worker_profile
    
    enrollments = Enrollment.objects.filter(worker=worker, is_active=True).order_by('-enrolled_date')
    
    context = {
        'enrollments': enrollments,
    }
    return render(request, 'training/my_courses.html', context)

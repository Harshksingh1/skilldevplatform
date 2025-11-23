from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import BaseModel
from skills.models import Skill
from workers.models import Worker


class Course(BaseModel):
    """Training course model"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='taught_courses')
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="External image URL as fallback")
    skills = models.ManyToManyField(Skill, related_name='courses', blank=True)
    duration_hours = models.PositiveIntegerField(help_text="Course duration in hours")
    capacity = models.PositiveIntegerField(default=30, help_text="Maximum number of participants")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='beginner'
    )
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})
    
    @property
    def enrolled_count(self):
        return self.enrollments.filter(is_active=True).count()
    
    @property
    def available_spots(self):
        return max(0, self.capacity - self.enrolled_count)
    
    @property
    def is_full(self):
        return self.enrolled_count >= self.capacity


class CourseModule(BaseModel):
    """Course module/lesson"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    duration_minutes = models.PositiveIntegerField(default=60)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, help_text="HTML content or instructions")
    
    class Meta:
        ordering = ['order', 'title']
        unique_together = ['course', 'order']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(BaseModel):
    """Worker enrollment in a course"""
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('enrolled', 'Enrolled'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('dropped', 'Dropped'),
        ],
        default='enrolled'
    )
    progress_percentage = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    certificate_issued = models.BooleanField(default=False)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    rating = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5"
    )
    review = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['worker', 'course']
        ordering = ['-enrolled_date']
    
    def __str__(self):
        return f"{self.worker} - {self.course}"


class CourseProgress(BaseModel):
    """Individual module progress tracking"""
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='module_progress')
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, related_name='progress_records')
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    time_spent_minutes = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ['enrollment', 'module']
        ordering = ['module__order']
    
    def __str__(self):
        return f"{self.enrollment} - {self.module.title}"

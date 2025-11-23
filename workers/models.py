from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import BaseModel
from skills.models import Skill


class Worker(BaseModel):
    """Worker profile extending User model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker_profile')
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='workers/', blank=True, null=True)
    profile_picture_url = models.URLField(blank=True, null=True, help_text="External profile picture URL as fallback")
    bio = models.TextField(blank=True)
    date_of_joining = models.DateField()
    skills = models.ManyToManyField(Skill, through='WorkerSkill', related_name='workers', blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.employee_id}"
    
    def get_absolute_url(self):
        return reverse('worker_detail', kwargs={'pk': self.pk})
    
    @property
    def full_name(self):
        return self.user.get_full_name() or self.user.username
    
    @property
    def email(self):
        return self.user.email


class WorkerSkill(BaseModel):
    """Intermediate model for Worker-Skill relationship with proficiency level"""
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='worker_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='worker_skills')
    proficiency_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='beginner'
    )
    certification_date = models.DateField(blank=True, null=True)
    certificate_document = models.FileField(upload_to='certificates/', blank=True, null=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['worker', 'skill']
        ordering = ['-proficiency_level', 'skill__name']
    
    def __str__(self):
        return f"{self.worker} - {self.skill} ({self.proficiency_level})"

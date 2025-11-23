from django.db import models
from django.urls import reverse
from core.models import BaseModel


class SkillCategory(BaseModel):
    """Category for organizing skills"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='fas fa-tag', help_text="Font Awesome icon class")
    
    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Skill(BaseModel):
    """Skill model for tracking worker skills"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
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
    estimated_duration_hours = models.PositiveIntegerField(default=40, help_text="Estimated hours to master")
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='required_for')
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('skill_detail', kwargs={'pk': self.pk})
    
    def get_difficulty_color(self):
        colors = {
            'beginner': 'success',
            'intermediate': 'info',
            'advanced': 'warning',
            'expert': 'danger',
        }
        return colors.get(self.difficulty_level, 'secondary')

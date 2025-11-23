from django.contrib import admin
from .models import SkillCategory, Skill


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'difficulty_level', 'estimated_duration_hours', 'is_active', 'created_at']
    list_filter = ['category', 'difficulty_level', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
    filter_horizontal = ['prerequisites']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category', 'image')
        }),
        ('Details', {
            'fields': ('difficulty_level', 'estimated_duration_hours', 'prerequisites')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )

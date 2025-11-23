from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Worker, WorkerSkill


class WorkerSkillInline(admin.TabularInline):
    model = WorkerSkill
    extra = 1
    fields = ['skill', 'proficiency_level', 'certification_date', 'certificate_document']


class WorkerInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = 'Worker Profile'
    fields = ['employee_id', 'department', 'position', 'phone', 'profile_picture', 'bio', 'date_of_joining']


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'full_name', 'department', 'position', 'date_of_joining', 'is_active']
    list_filter = ['department', 'position', 'is_active', 'date_of_joining']
    search_fields = ['employee_id', 'user__username', 'user__first_name', 'user__last_name', 'department', 'position']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at', 'full_name', 'email']
    inlines = [WorkerSkillInline]
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'full_name', 'email')
        }),
        ('Employee Information', {
            'fields': ('employee_id', 'department', 'position', 'phone', 'date_of_joining')
        }),
        ('Profile', {
            'fields': ('profile_picture', 'profile_picture_url', 'bio')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(WorkerSkill)
class WorkerSkillAdmin(admin.ModelAdmin):
    list_display = ['worker', 'skill', 'proficiency_level', 'certification_date', 'is_active']
    list_filter = ['proficiency_level', 'certification_date', 'is_active']
    search_fields = ['worker__employee_id', 'worker__user__username', 'skill__name']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']

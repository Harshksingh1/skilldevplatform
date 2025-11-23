from django.contrib import admin
from .models import Course, CourseModule, Enrollment, CourseProgress


class CourseModuleInline(admin.TabularInline):
    model = CourseModule
    extra = 1
    fields = ['title', 'order', 'duration_minutes', 'video_url']


class CourseProgressInline(admin.TabularInline):
    model = CourseProgress
    extra = 0
    readonly_fields = ['completed_date']
    fields = ['module', 'completed', 'completed_date', 'time_spent_minutes']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'difficulty_level', 'duration_hours', 'capacity', 'enrolled_count', 'is_full', 'is_active']
    list_filter = ['difficulty_level', 'is_active', 'start_date', 'instructor']
    search_fields = ['title', 'description', 'instructor__username']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at', 'enrolled_count', 'available_spots']
    filter_horizontal = ['skills']
    inlines = [CourseModuleInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'instructor', 'image', 'image_url')
        }),
        ('Course Details', {
            'fields': ('skills', 'duration_hours', 'difficulty_level', 'capacity', 'price')
        }),
        ('Schedule', {
            'fields': ('start_date', 'end_date')
        }),
        ('Statistics', {
            'fields': ('enrolled_count', 'available_spots')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'duration_minutes', 'is_active']
    list_filter = ['course', 'is_active']
    search_fields = ['title', 'description', 'course__title']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['worker', 'course', 'status', 'progress_percentage', 'rating', 'enrolled_date', 'is_active']
    list_filter = ['status', 'certificate_issued', 'rating', 'enrolled_date', 'is_active']
    search_fields = ['worker__employee_id', 'worker__user__username', 'course__title']
    list_editable = ['status', 'is_active']
    readonly_fields = ['enrolled_date', 'created_at', 'updated_at']
    inlines = [CourseProgressInline]
    
    fieldsets = (
        ('Enrollment Information', {
            'fields': ('worker', 'course', 'enrolled_date')
        }),
        ('Progress', {
            'fields': ('status', 'progress_percentage', 'completed_date')
        }),
        ('Certification', {
            'fields': ('certificate_issued', 'certificate_file')
        }),
        ('Feedback', {
            'fields': ('rating', 'review')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(CourseProgress)
class CourseProgressAdmin(admin.ModelAdmin):
    list_display = ['enrollment', 'module', 'completed', 'time_spent_minutes', 'completed_date']
    list_filter = ['completed', 'completed_date']
    search_fields = ['enrollment__worker__employee_id', 'module__title']
    readonly_fields = ['created_at', 'updated_at']

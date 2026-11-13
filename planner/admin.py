from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User, Course, StudyMaterial, BusySlot, Task,
    ScheduledBlock, PomodoroSession, AIInsight, Notification
)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Cấu hình học tập & Pomodoro', {
            'fields': (
                'role',
                'study_start_hour',
                'study_end_hour',
                'pomodoro_work_minutes',
                'pomodoro_break_minutes',
                'pomodoro_long_break_minutes'
            )
        }),
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'semester', 'user', 'color_code', 'created_at')
    list_filter = ('semester', 'user')
    search_fields = ('name', 'code')

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'task', 'material_type', 'created_at')
    list_filter = ('material_type', 'course')
    search_fields = ('title', 'content')

@admin.register(BusySlot)
class BusySlotAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'is_recurring', 'day_of_week', 'start_time', 'end_time', 'specific_date')
    list_filter = ('category', 'is_recurring', 'day_of_week', 'user')
    search_fields = ('title', 'location')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'user', 'priority', 'status', 'estimated_minutes', 'completed_minutes', 'deadline')
    list_filter = ('priority', 'status', 'course', 'user')
    search_fields = ('title', 'description')

@admin.register(ScheduledBlock)
class ScheduledBlockAdmin(admin.ModelAdmin):
    list_display = ('task', 'start_datetime', 'end_datetime', 'status', 'is_locked')
    list_filter = ('status', 'is_locked')
    search_fields = ('task__title',)

@admin.register(PomodoroSession)
class PomodoroSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'task', 'duration_minutes', 'efficiency_score', 'start_datetime', 'end_datetime')
    list_filter = ('efficiency_score', 'user')
    search_fields = ('task__title', 'notes')

@admin.register(AIInsight)
class AIInsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'insight_type', 'severity', 'created_at')
    list_filter = ('insight_type', 'severity', 'user')
    search_fields = ('title', 'summary')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'user')
    search_fields = ('title', 'message')

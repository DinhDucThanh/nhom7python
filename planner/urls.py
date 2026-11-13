from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

    # Core
    path('', views.dashboard_view, name='dashboard'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/optimize/', views.trigger_optimizer_view, name='trigger_optimizer'),

    # Tasks
    path('tasks/', views.tasks_view, name='tasks'),
    path('tasks/create/', views.task_create_view, name='task_create'),
    path('tasks/<int:task_id>/toggle/', views.task_toggle_status_view, name='task_toggle'),
    path('tasks/<int:task_id>/delete/', views.task_delete_view, name='task_delete'),

    # Courses & Materials & BusySlots
    path('courses/', views.courses_view, name='courses'),
    path('courses/create/', views.course_create_view, name='course_create'),
    path('materials/create/', views.material_create_view, name='material_create'),
    path('busyslots/create/', views.busyslot_create_view, name='busyslot_create'),
    path('busyslots/<int:slot_id>/delete/', views.busyslot_delete_view, name='busyslot_delete'),

    # Pomodoro
    path('pomodoro/', views.pomodoro_view, name='pomodoro'),

    # Notifications
    path('notifications/read-all/', views.mark_all_notifications_read_view, name='mark_notifications_read'),

    # Admin Portal
    path('admin-portal/', views.admin_portal_view, name='admin_portal'),
    path('admin-portal/users/<int:user_id>/toggle-active/', views.admin_user_toggle_active_view, name='admin_user_toggle_active'),
    path('admin-portal/users/<int:user_id>/toggle-role/', views.admin_user_toggle_role_view, name='admin_user_toggle_role'),
]

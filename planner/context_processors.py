from .models import Notification

def global_context(request):
    unread_notifications_count = 0
    recent_notifications = []
    if request.user.is_authenticated:
        unread_notifications_count = Notification.objects.filter(user=request.user, is_read=False).count()
        recent_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')[:5]
    return {
        'unread_notifications_count': unread_notifications_count,
        'recent_notifications': recent_notifications,
        'app_name': 'Smart Study Planner & Optimizer',
    }

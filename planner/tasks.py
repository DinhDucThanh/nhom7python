from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from .models import Task, Notification, AIInsight, User

@shared_task
def scan_deadlines_and_notify():
    """
    Quét tất cả các task chưa hoàn thành của tất cả sinh viên.
    Nếu task có deadline trong vòng 24h hoặc 48h, tạo thông báo và AI insight cảnh báo.
    """
    now = timezone.now()
    cutoff_48h = now + timedelta(hours=48)
    cutoff_24h = now + timedelta(hours=24)

    tasks_at_risk = Task.objects.filter(
        status__in=[Task.STATUS_TODO, Task.STATUS_IN_PROGRESS],
        deadline__lte=cutoff_48h,
    ).select_related('user', 'course')

    alerts_created = 0
    for task in tasks_at_risk:
        hours_left = (task.deadline - now).total_seconds() / 3600
        user = task.user

        if hours_left < 0:
            # Overdue task
            task.status = Task.STATUS_OVERDUE
            task.save(update_fields=['status'])
            
            # Check if notification already sent in last 12 hours
            recent_notif = Notification.objects.filter(
                user=user,
                notification_type=Notification.TYPE_DEADLINE_REMINDER,
                created_at__gte=now - timedelta(hours=12),
                message__icontains=task.title
            ).first()

            if not recent_notif:
                Notification.objects.create(
                    user=user,
                    title=f"⚠️ Task quá hạn: {task.title}",
                    message=f"Công việc '{task.title}' thuộc môn {task.course.name} đã quá hạn chót ({task.deadline.strftime('%d/%m/%Y %H:%M')}). Hãy hoàn thành hoặc dời lịch sớm!",
                    notification_type=Notification.TYPE_DEADLINE_REMINDER,
                )
                alerts_created += 1

        elif hours_left <= 24:
            # Critical deadline
            recent_notif = Notification.objects.filter(
                user=user,
                notification_type=Notification.TYPE_DEADLINE_REMINDER,
                created_at__gte=now - timedelta(hours=12),
                message__icontains=task.title
            ).first()

            if not recent_notif:
                Notification.objects.create(
                    user=user,
                    title=f"🔥 Gấp: Còn {int(hours_left)} giờ tới deadline '{task.title}'",
                    message=f"Môn {task.course.name} cần nộp lúc {task.deadline.strftime('%H:%M %d/%m/%Y')}. Thời gian còn thiếu: {task.remaining_minutes} phút.",
                    notification_type=Notification.TYPE_DEADLINE_REMINDER,
                )
                alerts_created += 1

    return f"Đã quét và tạo {alerts_created} cảnh báo deadline."

import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.db.models import Count, Sum, Q

from .models import (
    User, Course, StudyMaterial, BusySlot, Task,
    ScheduledBlock, PomodoroSession, AIInsight, Notification
)
from .optimizer import ScheduleOptimizer
from .ai_service import AIService


# =============================================================================
# Auth Views
# =============================================================================
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        u = request.POST.get('username', '').strip()
        p = request.POST.get('password', '').strip()
        user = authenticate(request, username=u, password=p)
        if user is not None:
            if not user.is_active:
                messages.error(request, "Tài khoản của bạn đã bị khóa. Vui lòng liên hệ Admin.")
                return render(request, 'auth/login.html')
            login(request, user)
            messages.success(request, f"Chào mừng {user.first_name or user.username} quay trở lại!")
            return redirect('dashboard')
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không chính xác.")
    return render(request, 'auth/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        u = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        p1 = request.POST.get('password', '')
        p2 = request.POST.get('password_confirm', '')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()

        if p1 != p2:
            messages.error(request, "Hai mật khẩu nhập không khớp.")
            return render(request, 'auth/register.html')
        if len(p1) < 6:
            messages.error(request, "Mật khẩu phải từ 6 ký tự trở lên.")
            return render(request, 'auth/register.html')
        if User.objects.filter(username=u).exists():
            messages.error(request, f"Tên đăng nhập '{u}' đã tồn tại.")
            return render(request, 'auth/register.html')

        user = User.objects.create_user(
            username=u,
            email=email,
            password=p1,
            first_name=first_name,
            last_name=last_name,
            role=User.ROLE_STUDENT,
        )
        login(request, user)
        messages.success(request, "Đăng ký thành công! Hãy bắt đầu thiết lập kế hoạch học tập.")
        return redirect('dashboard')
    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Bạn đã đăng xuất an toàn.")
    return redirect('login')


@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.openai_api_key = request.POST.get('openai_api_key', '').strip()

        # Cấu hình giờ học
        start_hour_str = request.POST.get('study_start_hour')
        end_hour_str = request.POST.get('study_end_hour')
        if start_hour_str:
            try:
                user.study_start_hour = datetime.datetime.strptime(start_hour_str, "%H:%M").time()
            except ValueError:
                pass
        if end_hour_str:
            try:
                user.study_end_hour = datetime.datetime.strptime(end_hour_str, "%H:%M").time()
            except ValueError:
                pass

        # Cấu hình Pomodoro
        try:
            user.pomodoro_work_minutes = int(request.POST.get('pomodoro_work_minutes', 25))
            user.pomodoro_break_minutes = int(request.POST.get('pomodoro_break_minutes', 5))
            user.pomodoro_long_break_minutes = int(request.POST.get('pomodoro_long_break_minutes', 15))
        except ValueError:
            pass

        user.save()
        messages.success(request, "Cập nhật hồ sơ và cấu hình học tập thành công!")
        return redirect('profile')

    return render(request, 'auth/profile.html', {'user': user})


# =============================================================================
# Dashboard & Core Views (Unified Planner Cockpit)
# =============================================================================
@login_required
def dashboard_view(request):
    user = request.user
    now = timezone.now()
    today = now.date()

    # Thống kê tổng quan
    tasks = Task.objects.filter(user=user)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status=Task.STATUS_COMPLETED).count()
    pending_tasks = tasks.exclude(status=Task.STATUS_COMPLETED).order_by('deadline', '-priority')

    # Danh sách môn học và lịch bận cho Calendar & Task Dock
    courses = Course.objects.filter(user=user)
    busy_slots = BusySlot.objects.filter(user=user)

    # Tổng số giờ Pomodoro trong tuần
    seven_days_ago = now - datetime.timedelta(days=7)
    recent_sessions = PomodoroSession.objects.filter(user=user, start_datetime__gte=seven_days_ago)
    total_pomodoro_minutes = sum(s.duration_minutes for s in recent_sessions)
    total_pomodoro_hours = round(total_pomodoro_minutes / 60.0, 1)

    # Tỷ lệ hoàn thành công việc
    completion_rate = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0

    # Lấy phân tích AI
    ai_service = AIService(user)
    daily_briefing = ai_service.get_daily_briefing()
    deadline_risks = ai_service.get_deadline_risks()
    study_habits = ai_service.get_study_habits()
    time_allocation = ai_service.get_time_allocation_advice()

    context = {
        'courses': courses,
        'busy_slots': busy_slots,
        'pending_tasks': pending_tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'total_pomodoro_hours': total_pomodoro_hours,
        'completion_rate': completion_rate,
        'daily_briefing': daily_briefing,
        'deadline_risks': deadline_risks,
        'study_habits': study_habits,
        'time_allocation': time_allocation,
        'now': now,
        'today': today,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def calendar_view(request):
    return redirect('dashboard')


# =============================================================================
# Tasks & Materials Views
# =============================================================================
@login_required
def tasks_view(request):
    user = request.user
    status_filter = request.GET.get('status', 'ALL')
    priority_filter = request.GET.get('priority', 'ALL')
    course_filter = request.GET.get('course', 'ALL')

    tasks = Task.objects.filter(user=user).select_related('course').prefetch_related('materials')

    if status_filter != 'ALL':
        tasks = tasks.filter(status=status_filter)
    if priority_filter != 'ALL':
        tasks = tasks.filter(priority=priority_filter)
    if course_filter != 'ALL':
        tasks = tasks.filter(course_id=course_filter)

    courses = Course.objects.filter(user=user)

    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'courses': courses,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'course_filter': course_filter,
    })


@login_required
def task_create_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        priority = request.POST.get('priority', Task.PRIORITY_MEDIUM)
        estimated_minutes = int(request.POST.get('estimated_minutes', 120))
        deadline_str = request.POST.get('deadline')

        course = get_object_or_404(Course, id=course_id, user=request.user)

        try:
            deadline = datetime.datetime.fromisoformat(deadline_str)
        except Exception:
            deadline = timezone.now() + datetime.timedelta(days=2)

        task = Task.objects.create(
            user=request.user,
            course=course,
            title=title,
            description=description,
            priority=priority,
            estimated_minutes=estimated_minutes,
            deadline=deadline,
        )
        messages.success(request, f"Đã thêm công việc '{task.title}' thành công!")
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


@login_required
def task_toggle_status_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if task.status == Task.STATUS_COMPLETED:
        task.status = Task.STATUS_TODO
    else:
        task.status = Task.STATUS_COMPLETED
        task.completed_minutes = task.estimated_minutes
    task.save(update_fields=['status', 'completed_minutes'])
    messages.success(request, f"Cập nhật trạng thái công việc '{task.title}'.")
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


@login_required
def task_delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    title = task.title
    task.delete()
    messages.info(request, f"Đã xóa công việc '{title}'.")
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


# =============================================================================
# Courses & Study Materials & BusySlots Views
# =============================================================================
@login_required
def courses_view(request):
    user = request.user
    courses = Course.objects.filter(user=user).annotate(
        task_count=Count('tasks'),
        material_count=Count('materials')
    )
    materials = StudyMaterial.objects.filter(course__user=user).select_related('course', 'task')
    busy_slots = BusySlot.objects.filter(user=user)

    return render(request, 'courses/index.html', {
        'courses': courses,
        'materials': materials,
        'busy_slots': busy_slots,
    })


@login_required
def course_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        code = request.POST.get('code', '').strip()
        color_code = request.POST.get('color_code', '#3B82F6')
        semester = request.POST.get('semester', 'Học kỳ 1 - 2026-2027')
        description = request.POST.get('description', '').strip()

        Course.objects.create(
            user=request.user,
            name=name,
            code=code,
            color_code=color_code,
            semester=semester,
            description=description,
        )
        messages.success(request, f"Đã tạo môn học '{name}'!")
    return redirect('courses')


@login_required
def material_create_view(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        title = request.POST.get('title', '').strip()
        material_type = request.POST.get('material_type', StudyMaterial.TYPE_NOTE)
        url = request.POST.get('url', '').strip()
        content = request.POST.get('content', '').strip()

        course = get_object_or_404(Course, id=course_id, user=request.user) if course_id else None

        StudyMaterial.objects.create(
            course=course,
            title=title,
            material_type=material_type,
            url=url if url else None,
            content=content,
        )
        messages.success(request, f"Đã thêm tài liệu '{title}'!")
    return redirect('courses')


@login_required
def busyslot_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        category = request.POST.get('category', BusySlot.CATEGORY_CLASS)
        is_recurring = request.POST.get('is_recurring') == '1'
        day_of_week = int(request.POST.get('day_of_week', 0)) if is_recurring else None
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        location = request.POST.get('location', '').strip()
        color_code = request.POST.get('color_code', '#64748B')
        specific_date_str = request.POST.get('specific_date')

        try:
            start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
            end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
        except Exception:
            messages.error(request, "Giờ bắt đầu hoặc kết thúc không hợp lệ.")
            return redirect('courses')

        specific_date = None
        if not is_recurring and specific_date_str:
            try:
                specific_date = datetime.datetime.strptime(specific_date_str, "%Y-%m-%d").date()
            except Exception:
                pass

        BusySlot.objects.create(
            user=request.user,
            title=title,
            category=category,
            is_recurring=is_recurring,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
            location=location,
            color_code=color_code,
            specific_date=specific_date,
        )
        messages.success(request, f"Đã thêm lịch bận '{title}'!")
    return redirect('courses')


@login_required
def busyslot_delete_view(request, slot_id):
    slot = get_object_or_404(BusySlot, id=slot_id, user=request.user)
    title = slot.title
    slot.delete()
    messages.info(request, f"Đã xóa lịch bận '{title}'.")
    return redirect('courses')


# =============================================================================
# Pomodoro Room View
# =============================================================================
@login_required
def pomodoro_view(request):
    user = request.user
    selected_task_id = request.GET.get('task_id')
    selected_task = None
    if selected_task_id:
        selected_task = Task.objects.filter(id=selected_task_id, user=user).first()

    pending_tasks = Task.objects.filter(user=user).exclude(status=Task.STATUS_COMPLETED).order_by('deadline')
    recent_sessions = PomodoroSession.objects.filter(user=user).select_related('task', 'task__course').order_by('-start_datetime')[:10]

    return render(request, 'pomodoro/index.html', {
        'user': user,
        'selected_task': selected_task,
        'pending_tasks': pending_tasks,
        'recent_sessions': recent_sessions,
    })


# =============================================================================
# Admin Portal (/admin-portal/)
# =============================================================================
def is_admin_check(user):
    return user.is_authenticated and (user.role == User.ROLE_ADMIN or user.is_superuser)


@user_passes_test(is_admin_check, login_url='dashboard')
def admin_portal_view(request):
    query = request.GET.get('q', '').strip()
    role_filter = request.GET.get('role', 'ALL')

    users_qs = User.objects.all().order_by('-date_joined')
    if query:
        users_qs = users_qs.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
    if role_filter != 'ALL':
        users_qs = users_qs.filter(role=role_filter)

    # Hệ thống số liệu thống kê tổng thể
    total_users_count = User.objects.count()
    total_students_count = User.objects.filter(role=User.ROLE_STUDENT).count()
    total_tasks_count = Task.objects.count()
    total_pomodoro_minutes = PomodoroSession.objects.aggregate(total=Sum('duration_minutes'))['total'] or 0
    total_pomodoro_hours = round(total_pomodoro_minutes / 60.0, 1)

    completed_tasks_count = Task.objects.filter(status=Task.STATUS_COMPLETED).count()
    system_completion_rate = int((completed_tasks_count / total_tasks_count * 100)) if total_tasks_count > 0 else 0

    return render(request, 'admin_portal/index.html', {
        'users': users_qs,
        'total_users_count': total_users_count,
        'total_students_count': total_students_count,
        'total_tasks_count': total_tasks_count,
        'total_pomodoro_hours': total_pomodoro_hours,
        'system_completion_rate': system_completion_rate,
        'query': query,
        'role_filter': role_filter,
    })


@user_passes_test(is_admin_check, login_url='dashboard')
def admin_user_toggle_active_view(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if target_user == request.user:
        messages.error(request, "Không thể tự khóa tài khoản của chính mình!")
        return redirect('admin_portal')

    target_user.is_active = not target_user.is_active
    target_user.save(update_fields=['is_active'])
    status_str = "kích hoạt" if target_user.is_active else "khóa"
    messages.success(request, f"Đã {status_str} tài khoản '{target_user.username}'.")
    return redirect('admin_portal')


@user_passes_test(is_admin_check, login_url='dashboard')
def admin_user_toggle_role_view(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if target_user == request.user:
        messages.error(request, "Không thể tự thay đổi vai trò của chính mình!")
        return redirect('admin_portal')

    if target_user.role == User.ROLE_STUDENT:
        target_user.role = User.ROLE_ADMIN
        target_user.is_staff = True
    else:
        target_user.role = User.ROLE_STUDENT
        target_user.is_staff = False
    target_user.save(update_fields=['role', 'is_staff'])
    messages.success(request, f"Đã chuyển quyền tài khoản '{target_user.username}' sang {target_user.get_role_display()}.")
    return redirect('admin_portal')


# =============================================================================
# Notifications & Quick Optimization Actions
# =============================================================================
@login_required
def mark_all_notifications_read_view(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    messages.info(request, "Đã đánh dấu đã đọc tất cả thông báo.")
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))


@login_required
def trigger_optimizer_view(request):
    """
    Nút bấm tiện lợi trên giao diện để tự sinh lịch tuần thông minh
    """
    optimizer = ScheduleOptimizer(request.user, days_ahead=7)
    res = optimizer.optimize()
    if res.get('overloaded_tasks_count', 0) > 0:
        messages.warning(
            request,
            f"Đã tối ưu lịch ({res['created_blocks_count']} phiên). Lưu ý: Có {res['overloaded_tasks_count']} task có nguy cơ quá tải!"
        )
    else:
        messages.success(request, f"Đã tự động xếp thành công {res['created_blocks_count']} phiên học vào thời khóa biểu tuần!")
    return redirect('calendar')

import os
import datetime
from typing import Optional
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study_planner.settings')
try:
    django.setup()
except RuntimeError:
    pass

from fastapi import FastAPI, Depends, HTTPException, Query, Request, Response
from pydantic import BaseModel
from django.utils import timezone
from django.contrib.sessions.models import Session
from .models import User, Course, Task, ScheduledBlock, BusySlot, PomodoroSession, AIInsight, Notification
from .optimizer import ScheduleOptimizer
from .ai_service import AIService
import icalendar


app = FastAPI(
    title="Smart Study Planner API",
    description="FastAPI auxiliary backend for schedule optimization, calendar synchronization, and AI suggestions",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)


# =============================================================================
# Helper: Get Current Authenticated User from Django Session or Query
# =============================================================================
def get_current_user(request: Request, user_id: Optional[int] = Query(None)) -> User:
    # 1. Thử lấy từ Django Session cookie
    session_key = request.cookies.get('sessionid')
    if session_key:
        try:
            session = Session.objects.filter(session_key=session_key, expire_date__gte=timezone.now()).first()
            if session:
                session_data = session.get_decoded()
                uid = session_data.get('_auth_user_id')
                if uid:
                    user = User.objects.filter(id=uid).first()
                    if user:
                        return user
        except Exception:
            pass

    # 2. Thử lấy từ query param nếu gọi API trực tiếp
    if user_id:
        user = User.objects.filter(id=user_id).first()
        if user:
            return user

    # 3. Fallback lấy user sinh viên đầu tiên (phục vụ demo / API testing)
    user = User.objects.filter(role=User.ROLE_STUDENT).first()
    if not user:
        user = User.objects.first()

    if not user:
        raise HTTPException(status_code=401, detail="Chưa có người dùng trong hệ thống")
    return user


# =============================================================================
# Pydantic Schemas
# =============================================================================
class BlockMoveRequest(BaseModel):
    start_datetime: str
    end_datetime: str
    is_locked: Optional[bool] = True


class PomodoroCompleteRequest(BaseModel):
    duration_minutes: int
    efficiency_score: Optional[int] = 5
    notes: Optional[str] = ""
    scheduled_block_id: Optional[int] = None


# =============================================================================
# Endpoints
# =============================================================================
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Smart Study Planner FastAPI Auxiliary Engine",
        "timestamp": timezone.now().isoformat()
    }


@app.get("/calendar/events")
def get_calendar_events(
    start: Optional[str] = None,
    end: Optional[str] = None,
    current_user: User = Depends(get_current_user)
):
    """
    Trả về danh sách sự kiện chuẩn cho FullCalendar.js:
    - BusySlot (Lịch bận cố định: màu xám, không kéo thả)
    - ScheduledBlock (Phiên học: theo màu môn học, cho phép kéo thả và resize)
    """
    tz = timezone.get_current_timezone()
    now = timezone.now().astimezone(tz)
    events = []

    # 1. Thêm ScheduledBlocks (trong khoảng +/- 30 ngày)
    range_start = now - datetime.timedelta(days=30)
    range_end = now + datetime.timedelta(days=30)

    blocks = ScheduledBlock.objects.filter(
        task__user=current_user,
        start_datetime__gte=range_start,
        end_datetime__lte=range_end
    ).select_related('task', 'task__course')

    for b in blocks:
        course = b.task.course
        color = course.color_code if course else "#3B82F6"
        events.append({
            "id": f"block_{b.id}",
            "block_id": b.id,
            "title": f"📚 {b.task.title}",
            "start": b.start_datetime.isoformat(),
            "end": b.end_datetime.isoformat(),
            "backgroundColor": color,
            "borderColor": "#1E293B" if b.is_locked else color,
            "textColor": "#FFFFFF",
            "editable": True,
            "durationEditable": True,
            "extendedProps": {
                "type": "study_block",
                "course_name": course.name if course else "",
                "priority": b.task.get_priority_display(),
                "status": b.get_status_display(),
                "is_locked": b.is_locked,
                "notes": b.notes,
                "task_id": b.task.id,
                "task_title": b.task.title,
            }
        })

    # 2. Thêm BusySlots
    busy_slots = BusySlot.objects.filter(user=current_user)
    # Tạo sự kiện trong vòng 14 ngày tới
    for d in range(-7, 21):
        cur_date = (now + datetime.timedelta(days=d)).date()
        weekday = cur_date.weekday()

        for bs in busy_slots:
            is_match = False
            if bs.is_recurring and bs.day_of_week == weekday:
                is_match = True
            elif not bs.is_recurring and bs.specific_date == cur_date:
                is_match = True

            if is_match:
                start_dt = datetime.datetime.combine(cur_date, bs.start_time, tzinfo=tz)
                end_dt = datetime.datetime.combine(cur_date, bs.end_time, tzinfo=tz)

                # Icon theo danh mục
                cat_icons = {
                    BusySlot.CATEGORY_CLASS: "🏫",
                    BusySlot.CATEGORY_JOB: "💼",
                    BusySlot.CATEGORY_PERSONAL: "🏃",
                }
                icon = cat_icons.get(bs.category, "🔒")

                events.append({
                    "id": f"busy_{bs.id}_{cur_date}",
                    "title": f"{icon} {bs.title}",
                    "start": start_dt.isoformat(),
                    "end": end_dt.isoformat(),
                    "backgroundColor": bs.color_code or "#64748B",
                    "borderColor": bs.color_code or "#475569",
                    "textColor": "#FFFFFF",
                    "editable": False,
                    "durationEditable": False,
                    "classNames": ["fc-busy-slot"],
                    "extendedProps": {
                        "type": "busy_slot",
                        "category": bs.get_category_display(),
                        "location": bs.location,
                    }
                })

    return events


@app.post("/optimize-schedule")
def optimize_schedule(
    days_ahead: int = Query(7, ge=1, le=14),
    current_user: User = Depends(get_current_user)
):
    """
    Kích hoạt thuật toán tự sinh và tối ưu lịch học tuần.
    """
    optimizer = ScheduleOptimizer(current_user, days_ahead=days_ahead)
    result = optimizer.optimize()
    return result


@app.patch("/blocks/{block_id}/move")
@app.post("/blocks/{block_id}/move")
def move_or_resize_block(
    block_id: int,
    payload: BlockMoveRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Cập nhật thời gian khi kéo-thả hoặc kéo giãn (resize) phiên học trên FullCalendar.
    Tự động đặt cờ is_locked = True để thuật toán không ghi đè.
    """
    block = ScheduledBlock.objects.filter(id=block_id, task__user=current_user).first()
    if not block:
        raise HTTPException(status_code=404, detail="Không tìm thấy phiên học")

    try:
        new_start = datetime.datetime.fromisoformat(payload.start_datetime.replace('Z', '+00:00'))
        new_end = datetime.datetime.fromisoformat(payload.end_datetime.replace('Z', '+00:00'))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Thời gian không hợp lệ: {str(e)}")

    if new_start >= new_end:
        raise HTTPException(status_code=400, detail="Thời gian bắt đầu phải nhỏ hơn thời gian kết thúc")

    block.start_datetime = new_start
    block.end_datetime = new_end
    block.is_locked = True # Khóa lại để bảo vệ chỉnh sửa của người dùng
    block.save(update_fields=['start_datetime', 'end_datetime', 'is_locked'])

    return {
        "status": "success",
        "message": f"Đã cập nhật phiên học '{block.task.title}' và khóa lịch cố định.",
        "block": {
            "id": block.id,
            "start": block.start_datetime.isoformat(),
            "end": block.end_datetime.isoformat(),
            "is_locked": block.is_locked
        }
    }


@app.post("/tasks/{task_id}/pomodoro-complete")
def complete_pomodoro_session(
    task_id: int,
    payload: PomodoroCompleteRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Ghi nhận một phiên Pomodoro đã hoàn thành:
    - Lưu PomodoroSession
    - Tăng Task.completed_minutes
    - Tự động chuyển Task sang COMPLETED nếu completed_minutes >= estimated_minutes
    """
    task = Task.objects.filter(id=task_id, user=current_user).first()
    if not task:
        raise HTTPException(status_code=404, detail="Không tìm thấy công việc")

    now = timezone.now()
    start_time = now - datetime.timedelta(minutes=payload.duration_minutes)

    # 1. Lưu PomodoroSession
    session = PomodoroSession.objects.create(
        user=current_user,
        task=task,
        scheduled_block_id=payload.scheduled_block_id,
        start_datetime=start_time,
        end_datetime=now,
        duration_minutes=payload.duration_minutes,
        efficiency_score=payload.efficiency_score or 5,
        notes=payload.notes or "",
    )

    # 2. Cập nhật Task
    task.completed_minutes += payload.duration_minutes
    if task.status == Task.STATUS_TODO:
        task.status = Task.STATUS_IN_PROGRESS

    if task.completed_minutes >= task.estimated_minutes:
        task.status = Task.STATUS_COMPLETED

    task.save(update_fields=['completed_minutes', 'status', 'updated_at'])

    # 3. Tạo thông báo động viên
    Notification.objects.create(
        user=current_user,
        title=f"🍅 Đã hoàn thành phiên Pomodoro ({payload.duration_minutes} phút)",
        message=f"Đã cộng dồn {payload.duration_minutes} phút vào môn {task.course.name}. Tiến độ: {task.progress_percent}%.",
        notification_type=Notification.TYPE_POMODORO_MILESTONE,
    )

    return {
        "status": "success",
        "session_id": session.id,
        "task_id": task.id,
        "completed_minutes": task.completed_minutes,
        "progress_percent": task.progress_percent,
        "task_status": task.status,
    }


# =============================================================================
# AI Assistant Panel Endpoints (4 core features)
# =============================================================================
@app.get("/ai/daily-briefing")
def get_ai_daily_briefing(current_user: User = Depends(get_current_user)):
    service = AIService(current_user)
    return service.get_daily_briefing()


@app.get("/ai/deadline-risks")
def get_ai_deadline_risks(current_user: User = Depends(get_current_user)):
    service = AIService(current_user)
    return service.get_deadline_risks()


@app.get("/ai/study-habits")
def get_ai_study_habits(current_user: User = Depends(get_current_user)):
    service = AIService(current_user)
    return service.get_study_habits()


@app.get("/ai/time-allocation")
def get_ai_time_allocation(current_user: User = Depends(get_current_user)):
    service = AIService(current_user)
    return service.get_time_allocation_advice()


@app.get("/ai/tasks/{task_id}/decompose")
def get_ai_task_decomposition(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Tính năng AI Nhận thức: Đọc hiểu bản chất chuyên môn của bài tập
    và tự động bóc tách thành các giai đoạn nhận thức kèm lời khuyên kỹ thuật.
    """
    service = AIService(current_user)
    return service.decompose_task(task_id)


# =============================================================================
# iCalendar (.ics) Export Endpoint
# =============================================================================
@app.get("/calendar/export-ics")
def export_icalendar(current_user: User = Depends(get_current_user)):
    """
    Xuất file chuẩn .ics đồng bộ trực tiếp sang Google Calendar hoặc Apple Calendar.
    """
    cal = icalendar.Calendar()
    cal.add('prodid', '-//Smart Study Planner//AI Optimizer//VI')
    cal.add('version', '2.0')
    cal.add('x-wr-calname', f"Lịch Học - {current_user.username}")

    # Thêm ScheduledBlocks
    blocks = ScheduledBlock.objects.filter(
        task__user=current_user
    ).select_related('task', 'task__course')

    for b in blocks:
        event = icalendar.Event()
        event.add('summary', f"📚 {b.task.title} ({b.task.course.name})")
        event.add('dtstart', b.start_datetime)
        event.add('dtend', b.end_datetime)
        event.add('description', f"Môn: {b.task.course.name}\nƯu tiên: {b.task.get_priority_display()}\nGhi chú: {b.notes}")
        event.add('status', 'CONFIRMED')
        cal.add_component(event)

    response = Response(
        content=cal.to_ical(),
        media_type="text/calendar",
        headers={
            "Content-Disposition": f"attachment; filename=study_schedule_{current_user.username}.ics"
        }
    )
    return response

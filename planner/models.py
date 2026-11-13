import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    ROLE_STUDENT = 'STUDENT'
    ROLE_ADMIN = 'ADMIN'
    ROLE_CHOICES = [
        (ROLE_STUDENT, 'Sinh viên'),
        (ROLE_ADMIN, 'Quản trị viên'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_STUDENT)
    study_start_hour = models.TimeField(default=datetime.time(7, 0), help_text="Giờ bắt đầu học trong ngày")
    study_end_hour = models.TimeField(default=datetime.time(22, 0), help_text="Giờ kết thúc học trong ngày")
    pomodoro_work_minutes = models.PositiveIntegerField(default=25, help_text="Độ dài phiên Pomodoro (phút)")
    pomodoro_break_minutes = models.PositiveIntegerField(default=5, help_text="Độ dài nghỉ ngắn (phút)")
    pomodoro_long_break_minutes = models.PositiveIntegerField(default=15, help_text="Độ dài nghỉ dài (phút)")
    openai_api_key = models.CharField(max_length=255, blank=True, verbose_name="OpenAI API Key (Tùy chọn)")

    @property
    def is_student(self):
        return self.role == self.ROLE_STUDENT

    @property
    def is_admin_role(self):
        return self.role == self.ROLE_ADMIN or self.is_superuser


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200, verbose_name="Tên môn học")
    code = models.CharField(max_length=50, blank=True, verbose_name="Mã học phần")
    color_code = models.CharField(max_length=20, default="#3B82F6", verbose_name="Mã màu")
    semester = models.CharField(max_length=100, default="Học kỳ 1 - 2026-2027", verbose_name="Học kỳ")
    description = models.TextField(blank=True, verbose_name="Mô tả môn học")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})" if self.code else self.name


class StudyMaterial(models.Model):
    TYPE_LINK = 'LINK'
    TYPE_FILE = 'FILE'
    TYPE_NOTE = 'NOTE'
    TYPE_CHOICES = [
        (TYPE_LINK, 'Đường dẫn (Link)'),
        (TYPE_FILE, 'Tài liệu / Tệp'),
        (TYPE_NOTE, 'Ghi chú / Tóm tắt'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials', null=True, blank=True)
    task = models.ForeignKey('Task', on_delete=models.SET_NULL, related_name='materials', null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Tiêu đề tài liệu")
    material_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_NOTE)
    url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Đường dẫn")
    content = models.TextField(blank=True, verbose_name="Nội dung ghi chú / Tóm tắt")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class BusySlot(models.Model):
    CATEGORY_CLASS = 'CLASS'
    CATEGORY_JOB = 'JOB'
    CATEGORY_PERSONAL = 'PERSONAL'
    CATEGORY_CHOICES = [
        (CATEGORY_CLASS, 'Lịch học trường'),
        (CATEGORY_JOB, 'Ca làm thêm'),
        (CATEGORY_PERSONAL, 'Hoạt động cá nhân'),
    ]

    DAY_CHOICES = [
        (0, 'Thứ Hai'),
        (1, 'Thứ Ba'),
        (2, 'Thứ Tư'),
        (3, 'Thứ Năm'),
        (4, 'Thứ Sáu'),
        (5, 'Thứ Bảy'),
        (6, 'Chủ Nhật'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='busy_slots')
    title = models.CharField(max_length=200, verbose_name="Tên lịch bận")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_CLASS)
    is_recurring = models.BooleanField(default=True, verbose_name="Lặp lại hàng tuần")
    day_of_week = models.IntegerField(choices=DAY_CHOICES, null=True, blank=True, verbose_name="Thứ trong tuần")
    start_time = models.TimeField(verbose_name="Giờ bắt đầu")
    end_time = models.TimeField(verbose_name="Giờ kết thúc")
    specific_date = models.DateField(null=True, blank=True, verbose_name="Ngày cụ thể (nếu không lặp lại)")
    color_code = models.CharField(max_length=20, default="#64748B", verbose_name="Màu hiển thị")
    location = models.CharField(max_length=200, blank=True, verbose_name="Địa điểm")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        day_str = dict(self.DAY_CHOICES).get(self.day_of_week, "") if self.is_recurring else str(self.specific_date)
        return f"[{self.get_category_display()}] {self.title} ({day_str} {self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')})"


class Task(models.Model):
    PRIORITY_LOW = 'LOW'
    PRIORITY_MEDIUM = 'MEDIUM'
    PRIORITY_HIGH = 'HIGH'
    PRIORITY_CRITICAL = 'CRITICAL'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Thấp'),
        (PRIORITY_MEDIUM, 'Trung bình'),
        (PRIORITY_HIGH, 'Cao'),
        (PRIORITY_CRITICAL, 'Khẩn cấp / Deadline'),
    ]

    STATUS_TODO = 'TODO'
    STATUS_IN_PROGRESS = 'IN_PROGRESS'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_OVERDUE = 'OVERDUE'
    STATUS_CHOICES = [
        (STATUS_TODO, 'Chưa bắt đầu'),
        (STATUS_IN_PROGRESS, 'Đang thực hiện'),
        (STATUS_COMPLETED, 'Đã hoàn thành'),
        (STATUS_OVERDUE, 'Quá hạn'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks', verbose_name="Môn học")
    title = models.CharField(max_length=255, verbose_name="Tiêu đề công việc")
    description = models.TextField(blank=True, verbose_name="Mô tả chi tiết")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default=PRIORITY_MEDIUM, verbose_name="Mức ưu tiên")
    estimated_minutes = models.PositiveIntegerField(default=120, verbose_name="Thời lượng ước tính (phút)")
    completed_minutes = models.PositiveIntegerField(default=0, verbose_name="Thời lượng đã học (phút)")
    deadline = models.DateTimeField(verbose_name="Hạn chót (Deadline)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_TODO, verbose_name="Trạng thái")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['deadline', '-priority']

    def __str__(self):
        return f"{self.title} - {self.course.name}"

    @property
    def remaining_minutes(self):
        rem = self.estimated_minutes - self.completed_minutes
        return max(rem, 0)

    @property
    def progress_percent(self):
        if self.estimated_minutes <= 0:
            return 100 if self.status == self.STATUS_COMPLETED else 0
        pct = int((self.completed_minutes / self.estimated_minutes) * 100)
        return min(pct, 100)

    @property
    def is_past_deadline(self):
        return timezone.now() > self.deadline and self.status != self.STATUS_COMPLETED

    @property
    def priority_weight(self):
        weights = {
            self.PRIORITY_LOW: 1.0,
            self.PRIORITY_MEDIUM: 2.0,
            self.PRIORITY_HIGH: 3.5,
            self.PRIORITY_CRITICAL: 5.0,
        }
        return weights.get(self.priority, 2.0)


class ScheduledBlock(models.Model):
    STATUS_SCHEDULED = 'SCHEDULED'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_SKIPPED = 'SKIPPED'
    STATUS_CHOICES = [
        (STATUS_SCHEDULED, 'Đã lên lịch'),
        (STATUS_COMPLETED, 'Đã hoàn thành'),
        (STATUS_SKIPPED, 'Bỏ qua'),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='scheduled_blocks')
    start_datetime = models.DateTimeField(verbose_name="Bắt đầu")
    end_datetime = models.DateTimeField(verbose_name="Kết thúc")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_SCHEDULED)
    is_locked = models.BooleanField(default=False, verbose_name="Khóa (Không tự động ghi đè)")
    notes = models.TextField(blank=True, verbose_name="Ghi chú phiên")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start_datetime']

    def __str__(self):
        return f"[{self.task.title}] {self.start_datetime.strftime('%d/%m %H:%M')} - {self.end_datetime.strftime('%H:%M')}"

    @property
    def duration_minutes(self):
        diff = self.end_datetime - self.start_datetime
        return int(diff.total_seconds() / 60)


class PomodoroSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pomodoro_sessions')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, related_name='pomodoro_sessions')
    scheduled_block = models.ForeignKey(ScheduledBlock, on_delete=models.SET_NULL, null=True, blank=True, related_name='pomodoro_sessions')
    start_datetime = models.DateTimeField(verbose_name="Bắt đầu")
    end_datetime = models.DateTimeField(verbose_name="Kết thúc")
    duration_minutes = models.PositiveIntegerField(default=25, verbose_name="Thời gian tập trung (phút)")
    efficiency_score = models.IntegerField(default=5, verbose_name="Độ hiệu quả (1-5)")
    notes = models.TextField(blank=True, verbose_name="Ghi chú sau buổi học")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_datetime']

    def __str__(self):
        task_title = self.task.title if self.task else "Tự do"
        return f"Pomodoro: {task_title} ({self.duration_minutes}m) - {self.start_datetime.strftime('%d/%m/%Y %H:%M')}"


class AIInsight(models.Model):
    TYPE_DAILY_BRIEFING = 'DAILY_BRIEFING'
    TYPE_DEADLINE_RISK = 'DEADLINE_RISK'
    TYPE_STUDY_HABIT = 'STUDY_HABIT'
    TYPE_TIME_ALLOCATION = 'TIME_ALLOCATION'
    TYPE_GENERAL = 'GENERAL'
    TYPE_CHOICES = [
        (TYPE_DAILY_BRIEFING, 'Tóm tắt việc cần làm trong ngày'),
        (TYPE_DEADLINE_RISK, 'Cảnh báo rủi ro trễ Deadline'),
        (TYPE_STUDY_HABIT, 'Phân tích thói quen học tập'),
        (TYPE_TIME_ALLOCATION, 'Gợi ý phân bổ thời gian'),
        (TYPE_GENERAL, 'Gợi ý chung'),
    ]

    SEVERITY_INFO = 'INFO'
    SEVERITY_WARNING = 'WARNING'
    SEVERITY_CRITICAL = 'CRITICAL'
    SEVERITY_CHOICES = [
        (SEVERITY_INFO, 'Thông tin'),
        (SEVERITY_WARNING, 'Cảnh báo'),
        (SEVERITY_CRITICAL, 'Rất nguy cấp'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ai_insights')
    insight_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    structured_data = models.JSONField(default=dict, blank=True)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default=SEVERITY_INFO)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_insight_type_display()}] {self.title}"


class Notification(models.Model):
    TYPE_DEADLINE_REMINDER = 'DEADLINE_REMINDER'
    TYPE_SCHEDULE_GENERATED = 'SCHEDULE_GENERATED'
    TYPE_OVERLOAD_WARNING = 'OVERLOAD_WARNING'
    TYPE_POMODORO_MILESTONE = 'POMODORO_MILESTONE'
    TYPE_CHOICES = [
        (TYPE_DEADLINE_REMINDER, 'Nhắc nhở Deadline'),
        (TYPE_SCHEDULE_GENERATED, 'Đã tối ưu thời khóa biểu'),
        (TYPE_OVERLOAD_WARNING, 'Cảnh báo quá tải lịch'),
        (TYPE_POMODORO_MILESTONE, 'Cột mốc Pomodoro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=30, choices=TYPE_CHOICES, default=TYPE_DEADLINE_REMINDER)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({'Đã đọc' if self.is_read else 'Chưa đọc'})"

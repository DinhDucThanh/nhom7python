import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from planner.models import (
    User, Course, StudyMaterial, BusySlot, Task,
    ScheduledBlock, PomodoroSession, Notification, AIInsight
)
from planner.optimizer import ScheduleOptimizer


class Command(BaseCommand):
    help = "Khởi tạo dữ liệu mẫu tinh gọn, thoáng đãng, không gây rối mắt cho Smart Study Planner & Optimizer"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Đang khởi tạo dữ liệu mẫu tinh gọn..."))

        # 1. Tạo tài khoản Admin & Sinh viên
        admin_user, _ = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@studyplanner.vn",
                "first_name": "Quản Trị",
                "last_name": "Hệ Thống",
                "role": User.ROLE_ADMIN,
                "is_staff": True,
                "is_superuser": True,
            }
        )
        admin_user.set_password("admin123")
        admin_user.role = User.ROLE_ADMIN
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        student_user, _ = User.objects.get_or_create(
            username="student",
            defaults={
                "email": "student@university.edu.vn",
                "first_name": "Minh",
                "last_name": "Nguyễn",
                "role": User.ROLE_STUDENT,
                "study_start_hour": datetime.time(8, 0),
                "study_end_hour": datetime.time(22, 0),
                "pomodoro_work_minutes": 25,
                "pomodoro_break_minutes": 5,
            }
        )
        student_user.set_password("student123")
        student_user.role = User.ROLE_STUDENT
        student_user.save()

        # Dọn dẹp dữ liệu cũ của student để tạo dữ liệu thoáng đãng
        ScheduledBlock.objects.filter(task__user=student_user).delete()
        Course.objects.filter(user=student_user).delete()
        BusySlot.objects.filter(user=student_user).delete()
        Task.objects.filter(user=student_user).delete()
        PomodoroSession.objects.filter(user=student_user).delete()
        Notification.objects.filter(user=student_user).delete()
        AIInsight.objects.filter(user=student_user).delete()

        now = timezone.now()

        # 2. Tạo 3 môn học chính (màu sắc hiện đại, dịu mắt)
        c1 = Course.objects.create(
            user=student_user,
            name="Lập trình Python Nâng cao",
            code="CS301",
            color_code="#4F46E5", # Indigo
            semester="Học kỳ 1 - 2026-2027",
            description="Lập trình hướng đối tượng nâng cao, Concurrency, Django và FastAPI."
        )
        c2 = Course.objects.create(
            user=student_user,
            name="Cấu trúc Dữ liệu & Giải thuật",
            code="CS202",
            color_code="#0D9488", # Teal
            semester="Học kỳ 1 - 2026-2027",
            description="Đồ thị, Cây nhị phân, Quy hoạch động và giải thuật tối ưu."
        )
        c3 = Course.objects.create(
            user=student_user,
            name="Cơ sở Dữ liệu & Quản trị SQL",
            code="CS204",
            color_code="#D97706", # Amber
            semester="Học kỳ 1 - 2026-2027",
            description="Chuẩn hóa dữ liệu 3NF, B-Tree Index và tối ưu câu truy vấn."
        )

        # 3. Tạo 3 tài liệu ôn tập tiêu biểu
        StudyMaterial.objects.create(
            course=c1,
            title="Tài liệu FastAPI ASGI & Concurrency Guide",
            material_type=StudyMaterial.TYPE_LINK,
            url="https://fastapi.tiangolo.com/tutorial/",
            content="Hướng dẫn xử lý bất đồng bộ async/await và dependency injection."
        )
        StudyMaterial.objects.create(
            course=c2,
            title="Sổ tay Giải thuật: Thuật toán Dijkstra & DP",
            material_type=StudyMaterial.TYPE_NOTE,
            content="Ghi chú quan trọng về cấu trúc Priority Queue trong thuật toán tìm đường ngắn nhất."
        )
        StudyMaterial.objects.create(
            course=c3,
            title="Cheatsheet Tối ưu hóa SQL & EXPLAIN ANALYZE",
            material_type=StudyMaterial.TYPE_NOTE,
            content="Bí kíp đánh Index và tránh Full Table Scan trong PostgreSQL."
        )

        # 4. Lịch cố định: CHỈ 2 BUỔI HỌC TRƯỜNG + 1 CA LÀM THÊM (Cực kỳ thoáng đãng!)
        # Buổi học 1: Thứ 3 (08:30 - 11:00)
        BusySlot.objects.create(
            user=student_user,
            title="Lớp CS301: Python Nâng cao",
            category=BusySlot.CATEGORY_CLASS,
            is_recurring=True,
            day_of_week=1, # Thứ 3
            start_time=datetime.time(8, 30),
            end_time=datetime.time(11, 0),
            location="Phòng C3-201",
            color_code="#64748B"
        )

        # Buổi học 2: Thứ 5 (13:30 - 16:00)
        BusySlot.objects.create(
            user=student_user,
            title="Lớp CS202: DSA & Giải thuật",
            category=BusySlot.CATEGORY_CLASS,
            is_recurring=True,
            day_of_week=3, # Thứ 5
            start_time=datetime.time(13, 30),
            end_time=datetime.time(16, 0),
            location="Hội trường D9-301",
            color_code="#64748B"
        )

        # Ca làm thêm: Chỉ 1 ca duy nhất vào sáng Thứ 7 (09:00 - 11:30)
        BusySlot.objects.create(
            user=student_user,
            title="Ca làm thêm: Part-time Web Dev",
            category=BusySlot.CATEGORY_JOB,
            is_recurring=True,
            day_of_week=5, # Thứ 7
            start_time=datetime.time(9, 0),
            end_time=datetime.time(11, 30),
            location="TechHub Office",
            color_code="#991B1B"
        )

        # 5. Tạo 4 Tasks trọng tâm (gọn gàng, dễ quản lý)
        t1 = Task.objects.create(
            user=student_user,
            course=c1,
            title="Hoàn thiện Đồ án: Xây dựng REST API bằng FastAPI",
            description="Viết API endpoints, authentication JWT và validation Pydantic.",
            priority=Task.PRIORITY_HIGH,
            estimated_minutes=90,
            completed_minutes=30,
            deadline=now + datetime.timedelta(hours=28), # Sát hạn để kích hoạt cảnh báo AI
            status=Task.STATUS_IN_PROGRESS
        )

        t2 = Task.objects.create(
            user=student_user,
            course=c2,
            title="Luyện 5 bài tập Giải thuật Đồ thị (Dijkstra / BFS)",
            description="Thực hành trên LeetCode dạng bài tìm đường đi ngắn nhất.",
            priority=Task.PRIORITY_MEDIUM,
            estimated_minutes=60,
            completed_minutes=0,
            deadline=now + datetime.timedelta(days=3),
            status=Task.STATUS_TODO
        )

        t3 = Task.objects.create(
            user=student_user,
            course=c3,
            title="Thiết kế CSDL E-Commerce & viết truy vấn doanh thu",
            description="Tạo bảng, khóa ngoại và câu truy vấn GROUP BY tính doanh số theo tháng.",
            priority=Task.PRIORITY_MEDIUM,
            estimated_minutes=60,
            completed_minutes=0,
            deadline=now + datetime.timedelta(days=5),
            status=Task.STATUS_TODO
        )

        t4 = Task.objects.create(
            user=student_user,
            course=c1,
            title="Đọc tài liệu Clean Architecture & Design Patterns",
            description="Nắm vững nguyên lý Dependency Inversion và Repository Pattern.",
            priority=Task.PRIORITY_LOW,
            estimated_minutes=45,
            completed_minutes=45,
            deadline=now + datetime.timedelta(days=7),
            status=Task.STATUS_COMPLETED
        )

        # 6. Tạo 6 bản ghi PomodoroSession trong 5 ngày qua (đủ số liệu biểu đồ cho AI)
        pomo_samples = [
            (4, 9, 0, 25, 5, "Tập trung giải bài tập BFS"),
            (3, 14, 30, 30, 4, "Viết router FastAPI"),
            (2, 9, 30, 25, 5, "Debug cấu hình JWT"),
            (1, 10, 0, 25, 5, "Thiết kế bảng Database"),
            (1, 15, 0, 30, 4, "Tối ưu query SQL"),
            (0, 9, 0, 25, 5, "Bắt đầu ngày mới tập trung"),
        ]

        for days_ago, hour, minute, dur, score, note in pomo_samples:
            sess_time = now - datetime.timedelta(days=days_ago)
            sess_start = sess_time.replace(hour=hour, minute=minute, second=0)
            sess_end = sess_start + datetime.timedelta(minutes=dur)
            PomodoroSession.objects.create(
                user=student_user,
                task=t1 if days_ago % 2 == 0 else t2,
                start_datetime=sess_start,
                end_datetime=sess_end,
                duration_minutes=dur,
                efficiency_score=score,
                notes=note
            )

        # 7. Xếp lịch mẫu CHỈ 3 PHIÊN HỌC THOÁNG ĐÃNG TRONG TUẦN (Không nhét kín!)
        # Xác định các ngày trong tuần này (tính từ hôm nay)
        today = now.date()
        
        # Phiên 1: Ngày mai hoặc hôm nay (Buổi chiều 14:00 - 15:30) - 90 phút cho t1
        day1 = now + datetime.timedelta(days=0 if now.hour < 14 else 1)
        b1_start = timezone.make_aware(datetime.datetime.combine(day1.date(), datetime.time(14, 0)))
        b1_end = timezone.make_aware(datetime.datetime.combine(day1.date(), datetime.time(15, 30)))
        ScheduledBlock.objects.create(
            task=t1,
            start_datetime=b1_start,
            end_datetime=b1_end,
            status=ScheduledBlock.STATUS_SCHEDULED,
            is_locked=False
        )

        # Phiên 2: Sau 2 ngày (Buổi sáng 09:00 - 10:00) - 60 phút cho t2
        day2 = now + datetime.timedelta(days=2)
        b2_start = timezone.make_aware(datetime.datetime.combine(day2.date(), datetime.time(9, 0)))
        b2_end = timezone.make_aware(datetime.datetime.combine(day2.date(), datetime.time(10, 0)))
        ScheduledBlock.objects.create(
            task=t2,
            start_datetime=b2_start,
            end_datetime=b2_end,
            status=ScheduledBlock.STATUS_SCHEDULED,
            is_locked=False
        )

        # Phiên 3: Sau 4 ngày (Buổi chiều 15:00 - 16:00) - 60 phút cho t3
        day3 = now + datetime.timedelta(days=4)
        b3_start = timezone.make_aware(datetime.datetime.combine(day3.date(), datetime.time(15, 0)))
        b3_end = timezone.make_aware(datetime.datetime.combine(day3.date(), datetime.time(16, 0)))
        ScheduledBlock.objects.create(
            task=t3,
            start_datetime=b3_start,
            end_datetime=b3_end,
            status=ScheduledBlock.STATUS_SCHEDULED,
            is_locked=False
        )

        # 8. Tạo 2 thông báo nhắc nhở nhẹ nhàng
        Notification.objects.create(
            user=student_user,
            title="Lịch học thoáng đãng đã sẵn sàng",
            message="Thời khóa biểu của bạn đã được tối ưu tinh gọn với chỉ 3 phiên học trọng tâm trong tuần.",
            is_read=False
        )
        Notification.objects.create(
            user=student_user,
            title="Đến hạn: Đồ án FastAPI",
            message="Bạn có phiên học đồ án lúc 14:00. Hãy duy trì tập trung để hoàn thành đúng hạn nhé!",
            is_read=False
        )

        self.stdout.write(self.style.SUCCESS(
            f"Đã khởi tạo dữ liệu mẫu TINH GỌN thành công!\n"
            f"- Admin: admin / admin123\n"
            f"- Student: student / student123\n"
            f"- Môn học: 3 môn\n"
            f"- Lịch bận: 2 buổi học + 1 ca làm thêm\n"
            f"- Tasks: 4 tasks (rõ ràng, không quá tải)\n"
            f"- Phiên học trên lịch: CHỈ 3 phiên học phân bổ đều, cực kỳ thoáng đãng!"
        ))

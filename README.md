# Ứng Dụng Lập Kế Hoạch Học Tập Cá Nhân Có AI Gợi Ý Lịch
### Smart Study Planner & Optimizer — Calendar, Optimization Engine & AI Productivity Platform

> **Đề tài:** Ứng Dụng Lập Kế Hoạch Học Tập Cá Nhân Có AI Gợi Ý Lịch  
> **Lĩnh vực:** Web / Productivity  
> **Hướng tiếp cận:** Calendar + Optimization Algorithm + AI Support (Dạng Dashboard Cards — Tuyệt đối không làm khung chat)  
> **Kiến trúc:** Thuần Python Full-Stack (Django 5.x ASGI + FastAPI phụ trợ mount trực tiếp tại `/api/v1/`)

---

## 🌟 Điểm Nổi Bật Của Hệ Thống

1. **Giao diện Web Hiện đại & Trải nghiệm SPA mượt mà:**
   - Xây dựng bằng công nghệ Python thuần: **Django 5.x + Django Templates + HTMX + Tailwind CSS + Alpine.js**.
   - Tương tác kéo-thả, cập nhật trạng thái tức thời không cần tải lại trang.

2. **Kiến trúc Lai Cao Cấp (Django + FastAPI ASGI Mount):**
   - FastAPI được mount trực tiếp vào `asgi.py` của Django tại đường dẫn `/api/v1/`.
   - Django chịu trách nhiệm Web UI, Auth, Session, ORM Models và Admin Portal.
   - FastAPI đảm nhận xử lý thuật toán tối ưu xếp lịch, đồng bộ sự kiện kéo-thả và cung cấp AI Analytics JSON endpoints.

3. **Thuật toán Tự sinh Kế hoạch Tuần (Optimization Engine):**
   - Quét khung giờ học của sinh viên trong 7 ngày tới (mặc định 07:00 – 22:30).
   - Tự động trừ đi các lịch bận cố định `BusySlot` (lịch học trên trường, ca làm thêm, việc cá nhân) và các phiên học đã bị khóa `is_locked=True`.
   - Tính điểm ưu tiên cho từng task:
     $$\text{Score} = \frac{\text{Priority\_Weight} \times 100}{\max(\text{Hours\_Until\_Deadline}, 1)} + \frac{\text{Remaining\_Minutes}}{60}$$
   - Chia nhỏ các task lớn thành các phiên học 45–90 phút (có 15 phút nghỉ giữa các phiên) và tự động lấp vào các khoảng trống rảnh.
   - Tự động cảnh báo quá tải (Overload/Deadline Risk) nếu thời gian cần học vượt quá quỹ thời gian rảnh trước hạn chót.

4. **Thời Khóa Biểu Kéo-Thả (FullCalendar.js & Đồng bộ .ics):**
   - Hiển thị song song lịch bận trường / ca làm thêm (màu xám / đỏ đô) và các phiên học (màu sắc theo từng môn học).
   - Hỗ trợ xem dạng Tuần (Week), Ngày (Day), Tháng (Month).
   - Hỗ trợ kéo-thả (Drag & Drop) và co giãn thời lượng (Resize) các phiên học; API FastAPI tự động lưu và khóa vị trí (`is_locked=True`).
   - Nút **Xuất file .ics (iCalendar)** chuẩn quốc tế để nhập vào Google Calendar, Apple Calendar, Outlook.

5. **AI Assistant Panel (4 Cards Trực Quan — KHÔNG dùng Khung Chat):**
   - **Tóm tắt ngày học (Daily Briefing):** Lịch trình hôm nay, tổng số giờ học, mục tiêu ưu tiên số 1 và lời khuyên năng lượng.
   - **Cảnh báo rủi ro trễ Deadline (Deadline Risk Detector):** So sánh giữa thời gian cần học và số giờ rảnh thực tế trước hạn chót, phát hiện nguy cơ trễ hạn.
   - **Phân tích thói quen học tập (Study Habit Analysis):** Thống kê từ dữ liệu `PomodoroSession` thật để chỉ ra khung giờ vàng tập trung, điểm đánh giá hiệu quả trung bình và tỷ lệ bám sát kế hoạch tuần.
   - **Gợi ý phân bổ thời gian (Smart Time Allocation):** Phát hiện ngày bị dồn tải (> 7h học + làm) và gợi ý dời lịch sang ngày thảnh thơi.
   - **Cơ chế Heuristic Fallback thông minh:** Luôn hoạt động mượt mà, phân tích số liệu thực tế trong DB ngay cả khi không có `OPENAI_API_KEY` hay `ANTHROPIC_API_KEY`.

6. **Phòng Pomodoro Tập Trung (Web Audio API & Web Notification API):**
   - Đếm ngược Pomodoro (25m học / 5m nghỉ ngắn / 15m nghỉ dài) kèm vòng tròn SVG trực quan.
   - Chọn công việc đang học để tự động cộng dồn số phút tập trung vào task và tự đánh dấu hoàn thành khi đạt đủ thời lượng.
   - Âm thanh chuông báo tinh thể tổng hợp bằng **Web Audio API** (không phụ thuộc file MP3 ngoài, hoạt động 100% trên mọi trình duyệt).
   - Tích hợp thông báo đẩy trình duyệt (Web Notification) và hiệu ứng pháo hoa ăn mừng (Confetti).

7. **Trang Quản Trị Người Dùng Web UI (`/admin-portal/`):**
   - Dành riêng cho tài khoản Quản trị viên (`role=ADMIN`).
   - Tìm kiếm người dùng, lọc theo vai trò, khóa/mở khóa tài khoản, phân quyền Sinh viên/Admin, xem thống kê toàn hệ thống.

---

## 🛠️ Cấu Trúc Thư Mục Dự Án

```
├── study_planner/
│   ├── __init__.py
│   ├── asgi.py            # Mount FastAPI tại /api/v1/ và Django ASGI tại /
│   ├── wsgi.py
│   ├── settings.py        # Cấu hình Django 5.x, Celery, DB fallback (PostgreSQL/SQLite)
│   ├── urls.py            # URL gốc định tuyến
│   └── celery.py          # Khởi tạo Celery Application
├── planner/
│   ├── models.py          # 8 Models: User, Course, BusySlot, Task, ScheduledBlock, PomodoroSession, AIInsight, Notification
│   ├── api.py             # FastAPI phụ trợ (/calendar/events, /optimize-schedule, /blocks/{id}/move, /ai/...)
│   ├── optimizer.py       # Thuật toán xếp lịch tự động & phát hiện quá tải
│   ├── ai_service.py      # Module AI với 4 tính năng & Heuristic Fallback
│   ├── tasks.py           # Celery background tasks quét deadline
│   ├── views.py           # Django Views (Auth, Dashboard, Calendar, Tasks, Courses, Pomodoro, Admin Portal)
│   ├── urls.py            # Planner app routes
│   ├── admin.py           # Django Admin model registration
│   └── management/
│       └── commands/
│           └── seed_data.py # Lệnh tạo dữ liệu mẫu đầy đủ cho bài toán thực tế
├── templates/
│   ├── base.html          # Layout chuẩn, Tailwind CSS CDN, Alpine.js, Web Audio synthesizer
│   ├── auth/              # login.html, register.html, profile.html
│   ├── dashboard/         # index.html (4 AI Cards + Key Metrics)
│   ├── calendar/          # index.html (FullCalendar.js kéo thả, tối ưu lịch, xuất .ics)
│   ├── tasks/             # index.html (Quản lý Task, lọc trạng thái/ưu tiên, tạo modal)
│   ├── courses/           # index.html (Quản lý Môn học, Lịch bận cố định, Tài liệu ôn tập)
│   ├── pomodoro/          # index.html (Bộ đếm Pomodoro + đánh giá sao hiệu quả)
│   └── admin_portal/      # index.html (Quản lý User & thống kê hệ thống)
├── Dockerfile             # Docker image đa giai đoạn tối ưu
├── docker-compose.yml     # Web + PostgreSQL 16 + Redis 7 + Celery Worker + Celery Beat
├── Procfile               # Khởi chạy trên nền tảng PaaS
├── railway.json           # Cấu hình deploy Railway
├── render.yaml            # Cấu hình deploy Render
├── requirements.txt       # Danh sách thư viện Python
└── .env.example           # Mẫu biến môi trường
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Nhanh

### Cách 1: Chạy trực tiếp trên máy cục bộ (Local)

1. **Cài đặt thư viện:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Chạy Migration & Nạp dữ liệu mẫu:**
   ```bash
   python manage.py migrate
   python manage.py seed_data
   ```

3. **Khởi chạy máy chủ ASGI (Django + FastAPI):**
   ```bash
   python -m uvicorn study_planner.asgi:application --host 127.0.0.1 --port 8000 --reload
   ```

4. **Truy cập ứng dụng:**
   - **Giao diện Web:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **FastAPI Swagger Docs:** [http://127.0.0.1:8000/api/v1/docs](http://127.0.0.1:8000/api/v1/docs)
   - **Django Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

### Cách 2: Chạy toàn bộ hệ thống bằng Docker Compose

Bao gồm Web app + PostgreSQL + Redis + Celery Worker + Celery Beat:

```bash
docker-compose up --build
```
Mở trình duyệt tại [http://localhost:8000](http://localhost:8000).

---

## 🔑 Tài Khoản Demo Sẵn Sàng (Seed Data)

Hệ thống đã chuẩn bị sẵn nút đăng nhập 1-click hoặc nhập thủ công:

| Vai trò | Tên đăng nhập | Mật khẩu | Mô tả quyền hạn |
| :--- | :--- | :--- | :--- |
| **Sinh viên** | `student` | `student123` | Toàn quyền sử dụng Lập lịch, Lịch kéo thả, Task, Môn học, Pomodoro, AI Dashboard. Có sẵn 4 môn học, 7 lịch bận/ca làm thêm, 8 tasks và 15 phiên Pomodoro. |
| **Quản trị viên** | `admin` | `admin123` | Quản trị hệ thống, truy cập `/admin-portal/` để quản lý người dùng, khóa/mở tài khoản, đổi vai trò, và truy cập Django Admin. |

---

## 📡 Danh Mục FastAPI Endpoints (`/api/v1/`)

| Method | Endpoint | Mô tả |
| :--- | :--- | :--- |
| `GET` | `/api/v1/health` | Kiểm tra tình trạng hoạt động của API phụ trợ |
| `GET` | `/api/v1/calendar/events` | Lấy danh sách sự kiện chuẩn cho FullCalendar (BusySlot + ScheduledBlock) |
| `POST` | `/api/v1/optimize-schedule` | Kích hoạt thuật toán tự sinh và tối ưu lịch học tuần |
| `PATCH` | `/api/v1/blocks/{id}/move` | Cập nhật thời gian khi kéo-thả hoặc resize phiên học và tự động khóa (`is_locked=True`) |
| `POST` | `/api/v1/tasks/{id}/pomodoro-complete` | Ghi nhận phiên Pomodoro, cộng dồn phút học và cập nhật tiến độ task |
| `GET` | `/api/v1/ai/daily-briefing` | Dữ liệu tóm tắt ngày học hôm nay |
| `GET` | `/api/v1/ai/deadline-risks` | Dữ liệu phân tích và cảnh báo rủi ro trễ deadline |
| `GET` | `/api/v1/ai/study-habits` | Dữ liệu thống kê thói quen và khung giờ tập trung |
| `GET` | `/api/v1/ai/time-allocation` | Dữ liệu phân tích cân bằng tải và gợi ý phân bổ thời gian |
| `GET` | `/api/v1/calendar/export-ics` | Tải xuống file `.ics` đồng bộ sang Google/Apple Calendar |

---

## 🌐 Sẵn Sàng Deploy Lên Render / Railway / Fly.io

- **Railway:** Đã có file `railway.json` và `Procfile`. Chỉ cần kết nối GitHub repo với Railway, hệ thống sẽ tự động build qua Dockerfile và provision PostgreSQL + Redis.
- **Render:** Đã có file `render.yaml`. Tạo New Blueprint Instance trên Render và chọn repo.
- **Fly.io:** Chạy `fly launch` (sử dụng Dockerfile có sẵn).

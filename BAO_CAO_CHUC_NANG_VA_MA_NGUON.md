# BÁO CÁO TOÀN DIỆN KIẾN TRÚC & ĐỐI CHIẾU MÃ NGUỒN
**Đề tài 4: Ứng Dụng Lập Kế Hoạch Học Tập Cá Nhân Có AI Gợi Ý Lịch (Smart Study Planner & Optimizer)**

---

## 1. BẢN ĐỒ CẤU TRÚC DỰ ÁN (BẤM VÀO ĐÂU ĐỂ XEM CÁI GÌ)

Cấu trúc dự án được phân cấp rõ ràng, dễ hiểu tuyệt đối:

```
├── study_planner/                  # CẤU HÌNH GỐC CỦA TOÀN BỘ HỆ THỐNG
│   ├── asgi.py                     # [QUAN TRỌNG] Nơi gắn kết FastAPI (/api/v1/) và Django (/)
│   ├── settings.py                 # Cấu hình CSDL (PostgreSQL / SQLite), Celery, Auth
│   ├── urls.py                     # Định tuyến URL gốc
│   └── celery.py                   # Cấu hình tiến trình chạy ngầm Celery & Celery Beat
│
├── planner/                        # MODULE CHỨC NĂNG CỐT LÕI
│   ├── models.py                   # 8 Bảng dữ liệu ORM (User, Course, Task, Lịch bận...)
│   ├── optimizer.py                # Thuật toán xếp lịch tuần tự động & công thức tính điểm
│   ├── ai_service.py               # Động cơ AI (OpenAI GPT-4o-mini + Heuristic Fallback)
│   ├── api.py                      # Toàn bộ API FastAPI (kéo-thả lịch, xuất file .ics)
│   ├── views.py                    # Views xử lý logic web, Đăng nhập, Admin Portal
│   ├── urls.py                     # Danh sách URL chi tiết của app
│   ├── tasks.py                    # Tác vụ chạy ngầm Celery quét deadline định kỳ
│   └── management/commands/
│       └── seed_data.py            # Lệnh nạp sẵn dữ liệu mẫu demo 1 chạm
│
├── templates/                      # GIAO DIỆN NGƯỜI DÙNG (HTML + TAILWIND + ALPINE.JS)
│   ├── base.html                   # Khung giao diện dùng chung, Navbar, nút đổi Sáng/Tối
│   ├── dashboard/index.html        # Buồng lái chính: Lịch tuần kéo thả + Hộp việc cần làm
│   ├── pomodoro/index.html         # Không gian tập trung Pomodoro, đồng hồ SVG & chuông
│   ├── courses/index.html          # Quản lý Môn học, Lịch bận trường/làm thêm & Tài liệu
│   ├── auth/
│   │   ├── login.html              # Trang đăng nhập (có 2 nút 1 chạm demo)
│   │   ├── register.html           # Trang đăng ký sinh viên
│   │   └── profile.html            # Trang cài đặt giờ sinh học & API Key
│   └── admin_portal/
│       └── index.html              # Trang Quản trị viên (Khóa/mở user, đổi quyền, thống kê)
│
├── BAO_CAO_CHUC_NANG_VA_MA_NGUON.docx # TỆP WORD BÁO CÁO NỘP THẦY
├── Dockerfile                      # Đóng gói ứng dụng chạy Container Docker
├── docker-compose.yml              # Khởi chạy toàn bộ Web + DB + Redis + Celery
├── Procfile                        # Cấu hình khởi chạy trên PaaS (Heroku / Render)
├── railway.json & render.yaml      # Cấu hình triển khai tự động lên Cloud
└── requirements.txt                # Danh sách thư viện Python cần thiết
```

---

## 2. BẢNG ĐỐI CHIẾU 100% YÊU CẦU CỦA GIẢNG VIÊN VỚI DÒNG CODE CỤ THỂ

| STT | Yêu cầu của Giảng viên | Tệp nguồn (File Path) | Dòng code | Giải thích cơ chế kỹ thuật |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **Mount FastAPI vào Django ASGI** | [`study_planner/asgi.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/study_planner/asgi.py) | **16 - 26** | Dùng `Starlette Mount` định tuyến: `/api/v1` chuyển tới FastAPI, các đường dẫn còn lại chuyển tới Django ASGI. Chạy chung 1 cổng 8000 duy nhất. |
| **2** | **PostgreSQL kết nối qua URL, tự fallback SQLite** | [`study_planner/settings.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/study_planner/settings.py) | **79 - 95** | Sử dụng `dj-database-url`: Nếu phát hiện biến `DATABASE_URL` sẽ kết nối PostgreSQL; nếu không, tự động fallback về SQLite nội bộ. |
| **3** | **Quản lý User, Giờ sinh học & Pomodoro** | [`planner/models.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/models.py)<br>[`planner/views.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/views.py) | **7 - 31**<br><br>**81 - 117** | Custom `AbstractUser` mở rộng: phân quyền (`STUDENT`, `ADMIN`), khung giờ học (`study_start_hour`, `study_end_hour`), độ dài Pomodoro và `openai_api_key`. |
| **4** | **Quản lý Môn học & Mã màu lịch** | [`planner/models.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/models.py)<br>[`planner/views.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/views.py) | **32 - 47**<br><br>**263 - 299** | Model `Course` liên kết người dùng, lưu mã học phần, học kỳ và trường `color_code` mã màu HEX. Mã màu này đồng bộ lên FullCalendar. |
| **5** | **Quản lý Tài liệu ôn tập (Link/File/Note)** | [`planner/models.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/models.py)<br>[`planner/views.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/views.py) | **48 - 72**<br><br>**301 - 321** | Model `StudyMaterial` liên kết Course hoặc Task. Hỗ trợ 3 phân loại: `LINK` (URL ngoài), `NOTE` (ghi chú tóm tắt), `FILE` (tài liệu đính kèm). |
| **6** | **Quản lý Lịch bận (Lịch trường & Làm thêm)** | [`planner/models.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/models.py)<br>[`planner/views.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/views.py) | **73 - 112**<br><br>**323 - 373** | Model `BusySlot` hỗ trợ lặp lại hàng tuần (`day_of_week`) hoặc ngày cụ thể (`specific_date`), phân loại `CLASS` (học trường), `JOB` (làm thêm). |
| **7** | **Quản lý Công việc & Deadline (Task)** | [`planner/models.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/models.py)<br>[`planner/views.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/views.py) | **113 - 180**<br><br>**207 - 258** | Model `Task` quản lý mức ưu tiên (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`), thời lượng ước tính/thực tế, hạn chót deadline, trạng thái và tỷ lệ hoàn thành. |
| **8** | **Thuật toán Tự sinh Kế hoạch Tuần** | [`planner/optimizer.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/optimizer.py) | **18 - 175** | Lấy quỹ thời gian rảnh 7 ngày, trừ `BusySlot` và các khối đã khóa `is_locked=True`. Chia task thành các block 60-90p, chèn 15p nghỉ giải lao. |
| **9** | **Công thức tính Điểm Ưu Tiên Task** | [`planner/optimizer.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/optimizer.py) | **41 - 44** | `Score = (Priority_Weight * 100) / max(Hours_Until_Deadline, 1) + (Remaining_Minutes / 60)`. Task sát hạn và điểm ưu tiên cao sẽ được xếp trước. |
| **10** | **Cảnh báo Quá Tải Lịch (Overload Risk)** | [`planner/optimizer.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/optimizer.py) | **133 - 158** | Nếu tổng thời gian cần làm vượt quá quỹ thời gian trống trước deadline, hệ thống tự động sinh `Notification` và `AIInsight` cảnh báo nguy cơ trễ hạn. |
| **11** | **Lịch FullCalendar.js (Tuần/Tháng/Ngày)** | [`templates/dashboard/index.html`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/templates/dashboard/index.html)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **75 - 95**<br><br>**94 - 190** | Tích hợp FullCalendar 6.x hiển thị đồng thời `BusySlot` (màu xám cố định) và `ScheduledBlock` (theo màu môn học), hỗ trợ view Tuần và Ngày. |
| **12** | **Kéo-thả & Thay đổi thời lượng (Drag/Drop & Resize)** | [`templates/dashboard/index.html`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/templates/dashboard/index.html)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **260 - 290**<br><br>**205 - 243** | Khi thả chuột hoặc co giãn sự kiện, gọi API `PATCH /api/v1/blocks/{id}/move`, cập nhật giờ mới vào DB và tự động bật cờ `is_locked = True`. |
| **13** | **Xuất lịch cá nhân (.ics) chuẩn iCalendar** | [`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **345 - 376** | Endpoint `/api/v1/calendar/export-ics` dùng thư viện `icalendar` sinh file `.ics` chuẩn RFC 5545, cho phép đồng bộ vào Google / Apple Calendar. |
| **14** | **Đồng hồ Pomodoro Focus & Tích lũy phút học** | [`templates/pomodoro/index.html`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/templates/pomodoro/index.html)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **20 - 150**<br><br>**246 - 303** | Đếm ngược 25/5/15p, vòng tròn SVG, chuông Web Audio API, cộng dồn phút học vào `Task.completed_minutes` và lưu lịch sử `PomodoroSession`. |
| **15** | **AI Tính năng 1: Tóm tắt ngày học (Daily Briefing)** | [`planner/ai_service.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/ai_service.py)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **31 - 144**<br><br>**308 - 312** | Tổng hợp các phiên học hôm nay, ca làm thêm, số giờ học dự kiến và mục tiêu ưu tiên số 1. Trả về cấu trúc JSON chuẩn Dashboard Card. |
| **16** | **AI Tính năng 2: Cảnh báo rủi ro trễ Deadline** | [`planner/ai_service.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/ai_service.py)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **148 - 211**<br><br>**314 - 318** | So sánh số giờ rảnh thực tế trước hạn với thời lượng học còn thiếu. Phân cấp cảnh báo: `CRITICAL` (chắc chắn trễ), `HIGH`, `MEDIUM`, `SAFE`. |
| **17** | **AI Tính năng 3: Phân tích thói quen học tập** | [`planner/ai_service.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/ai_service.py)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **215 - 277**<br><br>**320 - 324** | Quét dữ liệu 7 ngày từ `PomodoroSession`, tìm ra khung giờ vàng sinh viên đạt hiệu suất cao nhất (Sáng/Chiều/Tối) và tỷ lệ hoàn thành tuần. |
| **18** | **AI Tính năng 4: Gợi ý phân bổ thời gian** | [`planner/ai_service.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/ai_service.py)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **281 - 347**<br><br>**326 - 330** | Kiểm tra phân bổ tải của từng ngày trong tuần. Nếu ngày nào có tổng tải > 7 giờ (học + làm + tự học), AI sẽ đề xuất dời bớt sang các ngày rảnh hơn. |
| **19** | **AI Đột phá: Bóc tách nhận thức bài tập lớn** | [`planner/ai_service.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/ai_service.py)<br>[`planner/api.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/api.py) | **352 - 500**<br><br>**332 - 340** | Đọc hiểu ngữ nghĩa chuyên ngành của bài tập lớn (Dijkstra, RAG AI, Database 3NF) và tự phân rã thành 3-4 giai đoạn (Milestones) kèm mẹo kỹ thuật. |
| **20** | **Cơ chế Fallback Heuristic tự động (Không cần Key)** | [`planner/ai_service.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/ai_service.py) | **120 - 144**<br>**154 - 210**<br>**404 - 500** | Nếu người dùng chưa nhập `OPENAI_API_KEY` hoặc lỗi mạng, hệ thống tự động kích hoạt Expert Heuristic Engine dựa trên dữ liệu thật, không bao giờ lỗi. |
| **21** | **Tác vụ ngầm Celery & Celery Beat quét nhắc việc** | [`study_planner/celery.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/study_planner/celery.py)<br>[`planner/tasks.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/tasks.py) | **1 - 25**<br><br>**6 - 66** | Hàm `scan_deadlines_and_notify` chạy định kỳ qua Celery Beat, quét các task sắp đến hạn trong vòng 24h - 48h và tạo thông báo nhắc nhở tự động. |
| **22** | **Quản trị phân quyền Admin Portal (/admin-portal/)** | [`planner/views.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/views.py)<br>[`templates/admin_portal/index.html`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/templates/admin_portal/index.html) | **398 - 472** | Trang quản trị riêng trên web: Thống kê số lượng sinh viên, tổng giờ học, tìm kiếm tài khoản, nút khóa/mở khóa tài khoản và chuyển đổi vai trò. |
| **23** | **Dữ liệu mẫu khởi tạo Demo 1 chạm (Seed Data)** | [`planner/management/commands/seed_data.py`](file:///c:/Users/dinhd/OneDrive/Tài%20liệu/Đề%20tài%204%20phần%201%20Nhóm%207%20python/planner/management/commands/seed_data.py) | **1 - 170** | Lệnh `python manage.py seed_data` tạo sẵn tài khoản `admin`/`admin123`, `student`/`student123`, 3 môn học, 2 buổi học, 1 ca làm và lịch học thoáng đãng. |
| **24** | **Cấu hình Đóng gói Deploy Cloud (Production Ready)** | `Dockerfile`<br>`docker-compose.yml`<br>`Procfile`<br>`railway.json`<br>`render.yaml` | **Toàn bộ** | Sẵn sàng triển khai 1-click lên Render, Railway, Fly.io với cấu hình Uvicorn ASGI, PostgreSQL, Redis và Celery Worker/Beat. |

---

## 3. HƯỚNG DẪN BẬT DỰ ÁN VÀ TRÌNH BÀY CHO THẦY NGHIỆM THU

### Bước 1: Khởi động máy chủ ứng dụng
Mở terminal tại thư mục dự án và chạy lệnh:
```bash
python -m uvicorn study_planner.asgi:application --host 127.0.0.1 --port 8000
```
Truy cập vào ứng dụng tại trình duyệt: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Bước 2: Nạp dữ liệu mẫu sạch sẽ (Seed Data)
Mở một cửa sổ terminal mới và chạy:
```bash
python manage.py seed_data
```
Lệnh này sẽ khởi tạo sẵn tài khoản sinh viên với lịch học đã được tinh giản, cực kỳ thoáng đãng và dễ nhìn.

### Bước 3: Đăng nhập 1 chạm
Vào trang đăng nhập [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/), bấm trực tiếp vào nút:
- **Sinh viên:** `student` / `student123`
- Hoặc **Quản trị viên:** `admin` / `admin123`

### Bước 4: Trình diễn các chức năng cốt lõi cho Thầy
1. **Buồng lái Lịch tuần (FullCalendar):**
   - Chỉ cho Thầy xem lịch tuần thoáng đãng, các khối sự kiện có vạch màu nhận diện môn học và thời gian bắt đầu.
   - Dùng chuột kéo một phiên học sang khung giờ khác -> Thả chuột, thông báo toast xuất hiện báo đã khóa lịch và lưu trực tiếp vào cơ sở dữ liệu.
2. **Nút "Tự động xếp lịch":**
   - Bấm nút "Tự động xếp lịch" trên thanh công cụ -> Thuật toán tính toán khoảng trống, chia nhỏ task và xếp vào lịch kèm hiệu ứng pháo giấy chúc mừng.
3. **Đồng hồ Pomodoro:**
   - Bấm vào tab "Đồng hồ Pomodoro" -> Chọn một môn học, bấm Bắt đầu -> Vòng tròn SVG đếm ngược. Khi hoàn thành hoặc bấm "Ghi nhận hoàn thành", chuông ngân vang và số phút học được cộng dồn vào môn học.
4. **Bảng phân tích AI (AI Insights):**
   - Bấm vào icon Biểu đồ trên thanh công cụ để mở Modal 4 tính năng AI: Tóm tắt ngày học, Cảnh báo rủi ro deadline, Thói quen tập trung và Cân bằng tải tuần.
   - Thử bấm nút "Gợi ý chia nhỏ (AI)" bên cạnh một bài tập lớn để xem AI đọc hiểu đề bài và bóc tách giai đoạn học tập.
5. **Chuyển đổi giao diện Sáng / Tối (☀️ / 🌙):**
   - Bấm vào icon mặt trời/mặt trăng trên thanh Header để trình diễn khả năng chuyển đổi giao diện mượt mà theo phong cách Modern Minimalist (chuẩn quy chuẩn `frontend-design`).
6. **Cổng Quản trị người dùng (Admin Portal):**
   - Đăng nhập bằng tài khoản `admin` -> Vào mục "Quản trị người dùng" (`/admin-portal/`) -> Cho Thầy xem bảng danh sách user, thử bấm nút Khóa/Mở khóa hoặc Đổi quyền tài khoản sinh viên.

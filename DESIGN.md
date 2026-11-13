# Design System Specification (Modern SaaS & Productivity Studio)

## 1. Triết lý Thiết kế (Design Philosophy)
- **Thoáng đãng & Tinh gọn (Clean & Breathable):** Không nhồi nhét sự kiện kín mít. Mỗi ngày chỉ có 1-2 khối học tập trọng tâm, nhiều khoảng trống tự do để sinh viên chủ động bố trí cuộc sống.
- **Linh hoạt Theme Sáng / Tối (Dual-Mode Theme):**
  - **Sáng Tinh Tế (Clean Minimalist Light - Mặc định):** Lấy cảm hứng từ *Notion, Cron / Notion Calendar, Craft Docs* và *Apple*. Nền Slate-50 thanh thoát (`#F8FAFC`), card trắng tinh (`#FFFFFF`), viền siêu mỏng (`#E2E8F0`), bóng đổ mờ sương (`shadow-sm`).
  - **Tối Công Nghệ (Dark Studio Mode):** Lấy cảm hứng từ *Raycast* và *Linear*. Nền Slate-950 (`#0B0F17`), card Slate-900 (`#131926`), viền `#232B3E`, chữ `#F8FAFC`.
  - **Chuyển đổi 1 chạm (☀️ / 🌙):** Nút toggle trên thanh Navbar cho phép chuyển đổi ngay lập tức, lưu trạng thái vào `localStorage`.
- **Hệ thống FullCalendar Tinh giản (Calendar Craft):**
  - Thanh công cụ điều hướng tuần/ngày dạng **Segmented Pill Controls**.
  - Các khối học tập (Event Cards) bo góc `rounded-xl`, đổ bóng mềm mại, có vạch màu nhận diện môn học bên trái và chip hiển thị thời gian rõ ràng.
  - Các khe thời gian (Slot Lines) có đường kẻ mờ nhạt, dịu mắt, không còn lưới bảng thô ráp.
- **Typography & Visual Hierarchy:**
  - Font chữ hiện đại: `Plus Jakarta Sans` kết hợp `Inter`.
  - Tiêu đề đậm sắc sảo (`font-black` / `font-extrabold`), khoảng cách âm nhẹ (`tracking-tight`).
  - Điểm nhấn màu: **Indigo / Violet Gradient** (`#4F46E5` -> `#6366F1`) kết hợp với **Emerald** (Tiến độ an toàn) và **Rose** (Deep work / Cảnh báo deadline).

## 2. Bảng Màu Hệ Thống (Color Tokens)
- `Canvas Light`: `#F8FAFC` (Slate-50)
- `Surface Light`: `#FFFFFF` (Pure White)
- `Border Light`: `#E2E8F0` (Slate-200)
- `Canvas Dark`: `#0B0F17` (Slate-950)
- `Surface Dark`: `#131926` (Slate-900)
- `Border Dark`: `#232B3E` (Slate-800)
- `Brand Primary`: `#4F46E5` (Indigo-600) & `#6366F1` (Indigo-500)
- `Success`: `#10B981` (Emerald-500)
- `Warning`: `#F59E0B` (Amber-500)
- `Danger`: `#EF4444` (Rose-500)

## 3. Cấu hình Dữ liệu Mẫu Sinh viên (`student123`)
- **Lịch học trên trường:** Chỉ 2 buổi/tuần (Thứ 3: 08:30 - 11:00 và Thứ 5: 13:30 - 16:00).
- **Lịch làm thêm:** Chỉ 1 ca duy nhất sáng Thứ 7 (09:00 - 11:30).
- **Tasks trọng tâm:** 4 công việc rõ ràng, không dồn ứ.
- **Phiên học tự sinh:** Chỉ 3 phiên phân bổ đều các ngày Thứ 2, Thứ 4, Thứ 6.
- **Độ thoáng:** Giảm hơn 70% số khối hộp thừa, lịch tuần cực kỳ thoáng đãng, dễ nhìn và dễ thao tác kéo-thả!

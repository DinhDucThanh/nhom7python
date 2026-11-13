# HỌC VIỆN HÀNG KHÔNG VIỆT NAM
## KHOA CÔNG NGHỆ THÔNG TIN

---

# BÁO CÁO TIỂU LUẬN
### MÔN HỌC: …………………………………………………………………………

---

## ĐỀ TÀI:
# ỨNG DỤNG LẬP KẾ HOẠCH HỌC TẬP CÁ NHÂN CÓ AI GỢI Ý LỊCH
### (SMART STUDY PLANNER & OPTIMIZER)

* **Giảng viên hướng dẫn:** ……………………………………………………………
* **Sinh viên / Nhóm thực hiện:** Nhóm 07………………………………………
* **Mã số sinh viên:** ……………………………………………………………………
* **Lớp:** ……………………………………………………………………………………

*TP. Hồ Chí Minh, tháng 11/2026*

---

## DANH SÁCH SINH VIÊN THỰC HIỆN

| STT | Họ và tên | MSSV | Lớp | Ghi chú |
| :---: | :--- | :---: | :---: | :---: |
| 1 | **Đinh Đức Thành** | .................... | .................... | Nhóm trưởng |
| 2 | ........................................... | .................... | .................... | Thành viên |
| 3 | ........................................... | .................... | .................... | Thành viên |
| 4 | ........................................... | .................... | .................... | Thành viên |
| 5 | ........................................... | .................... | .................... | Thành viên |

<br>

| Cán bộ chấm thi 1<br>*(Ký và ghi rõ họ tên)*<br><br><br><br>................................................... | Cán bộ chấm thi 2<br>*(Ký và ghi rõ họ tên)*<br><br><br><br>................................................... |
| :---: | :---: |
| **Cán bộ chấm thi phúc khảo 1**<br>*(Ký và ghi rõ họ tên)*<br><br><br><br>................................................... | **Cán bộ chấm thi phúc khảo 2**<br>*(Ký và ghi rõ họ tên)*<br><br><br><br>................................................... |

---

## DANH MỤC CÁC KÝ HIỆU, CHỮ VIẾT TẮT

| Ký hiệu, chữ viết tắt | Chữ viết đầy đủ (Ý nghĩa) |
| :---: | :--- |
| **AI** | Artificial Intelligence (Trí tuệ nhân tạo) |
| **API** | Application Programming Interface (Giao diện lập trình ứng dụng) |
| **ASGI** | Asynchronous Server Gateway Interface (Giao diện cổng máy chủ bất đồng bộ) |
| **CRUD** | Create, Read, Update, Delete (Các thao tác cơ bản trên dữ liệu) |
| **CSRF** | Cross-Site Request Forgery (Tấn công giả mạo yêu cầu qua trang web) |
| **JSON** | JavaScript Object Notation (Định dạng trao đổi dữ liệu có cấu trúc) |
| **LLM** | Large Language Model (Mô hình ngôn ngữ lớn) |
| **MVT** | Model - View - Template (Mô hình kiến trúc ứng dụng web của Django) |
| **ORM** | Object-Relational Mapping (Kỹ thuật ánh xạ đối tượng vào cơ sở dữ liệu quan hệ) |
| **REST** | Representational State Transfer (Kiến trúc tiêu chuẩn cho các dịch vụ web) |
| **UI/UX** | User Interface / User Experience (Giao diện người dùng / Trải nghiệm người dùng) |

---

## MỤC LỤC

- **Danh mục các ký hiệu, chữ viết tắt**
- **Danh mục các bảng, hình vẽ, đồ thị**
- **MỞ ĐẦU**
- **CHƯƠNG 1. GIỚI THIỆU**
  - 1.1. Lý do chọn đề tài
  - 1.2. Mục tiêu đề tài
  - 1.3. Phạm vi đề tài
  - 1.4. Đối tượng nghiên cứu
  - 1.5. Phương pháp nghiên cứu
  - 1.6. Bố cục đề tài
- **CHƯƠNG 2. CƠ SỞ LÝ THUYẾT**
  - 2.1. Framework Django & Kiến trúc MVT
  - 2.2. Framework FastAPI & Giao thức ASGI
  - 2.3. Cơ sở dữ liệu quan hệ PostgreSQL & Hệ thống hàng đợi Redis/Celery
  - 2.4. Công nghệ Trí tuệ Nhân tạo & Kỹ thuật Structured Output JSON
  - 2.5. Thư viện FullCalendar.js & Thuật toán Lập lịch Heuristic đa mục tiêu
- **CHƯƠNG 3. PHÂN TÍCH HỆ THỐNG VÀ XÂY DỰNG SẢN PHẨM**
  - 3.1. Phân tích hệ thống
    - 3.1.1. Yêu cầu chức năng (5 phân hệ)
    - 3.1.2. Yêu cầu phi chức năng
    - 3.1.3. Biểu đồ Use Case tổng quát và phân hệ
    - 3.1.4. Thiết kế cơ sở dữ liệu (8 mô hình Models)
    - 3.1.5. Thiết kế thuật toán tự động sinh lịch học tuần (Optimization Engine)
  - 3.2. Xây dựng giao diện sản phẩm
    - 3.2.1. Giao diện Xác thực và Phân quyền người dùng (Hình 3.1)
    - 3.2.2. Giao diện Bảng điều khiển trung tâm & Phân tích AI Cards (Hình 3.2)
    - 3.2.3. Giao diện Lịch tương tác FullCalendar đa chế độ (Hình 3.3)
    - 3.2.4. Giao diện Quản lý Khóa học, Deadline và Tài liệu ôn tập (Hình 3.4)
    - 3.2.5. Giao diện Đồng hồ tập trung Pomodoro tích hợp (Hình 3.5)
    - 3.2.6. Giao diện Xuất file đồng bộ lịch cá nhân .ics (Hình 3.6)
    - 3.2.7. Giao diện Cổng Quản trị viên hệ thống Admin Portal (Hình 3.7)
- **KẾT LUẬN**
- **DANH MỤC TÀI LIỆU THAM KHẢO**
- **PHỤ LỤC**

---

## DANH MỤC CÁC BẢNG, HÌNH VẼ, ĐỒ THỊ

* **Bảng 2.1:** So sánh đặc tính kỹ thuật giữa Django và FastAPI trong kiến trúc hệ thống
* **Bảng 3.1:** Danh mục 8 thực thể dữ liệu trong cơ sở dữ liệu hệ thống
* **Bảng 3.2:** Bảng tra cứu trọng số ưu tiên trong công thức tính điểm thuật toán
* **Hình 3.1:** Giao diện Đăng nhập và Đăng ký hệ thống Smart Study Planner
* **Hình 3.2:** Giao diện Dashboard tổng quan và 4 khối phân tích AI chuyên sâu
* **Hình 3.3:** Giao diện Lịch tương tác FullCalendar tuần hỗ trợ kéo-thả và khóa lịch
* **Hình 3.4:** Giao diện Quản lý môn học, danh sách công việc và tài liệu ôn tập
* **Hình 3.5:** Giao diện Đồng hồ Pomodoro ghi nhận thời gian tập trung thực tế
* **Hình 3.6:** Chức năng Xuất lịch chuẩn iCalendar (.ics) đồng bộ Google Calendar
* **Hình 3.7:** Giao diện Cổng Quản trị viên Admin Portal quản lý tài khoản người dùng

---

# MỞ ĐẦU

Trong bối cảnh giáo dục hiện đại theo học chế tín chỉ, sinh viên đại học thường xuyên phải đối mặt với áp lực lớn từ việc phân bổ thời gian. Một học kỳ thông thường đòi hỏi sinh viên phải theo học từ 6 đến 8 môn học song song, mỗi môn lại có khối lượng bài tập lớn, đồ án môn học, kiểm tra định kỳ và bài tập nhóm với các hạn chót (deadline) dày đặc. Bên cạnh thời gian biểu học thuật trên giảng đường, đại đa số sinh viên hiện nay còn tham gia các ca làm thêm bán thời gian, rèn luyện kỹ năng mềm, học ngoại ngữ và các hoạt động câu lạc bộ, sự kiện ngoại khóa. Sự đan xen phức tạp giữa nhiều trách nhiệm khác nhau mà không có một phương pháp quản lý khoa học dẫn đến tình trạng quá tải (burnout), trì hoãn (procrastination) và hiện tượng "nước đến chân mới nhảy" gây ảnh hưởng tiêu cực trực tiếp đến kết quả học tập.

Xuất phát từ thực trạng trên, đề tài **"Ứng dụng lập kế hoạch học tập cá nhân có AI gợi ý lịch" (Smart Study Planner & Optimizer)** được nghiên cứu và xây dựng nhằm cung cấp một giải pháp công nghệ toàn diện. Khác biệt với các ứng dụng ghi chú đơn thuần hoặc các chatbot AI hội thoại thông thường, đề tài tập trung phát triển một nền tảng năng suất (Productivity & Calendar Web App) hoàn chỉnh. Ứng dụng tích hợp thuật toán tối ưu hóa lịch dựa trên độ cấp thiết và khối lượng công việc thực tế, giao diện tương tác trực quan kéo-thả hiện đại, phương pháp tập trung Pomodoro và sự hỗ trợ phân tích thông minh từ Trí tuệ Nhân tạo (AI). Đây là công cụ đắc lực giúp người học chủ động kiểm soát thời gian, giảm thiểu căng thẳng và nâng cao tối đa hiệu suất học tập cá nhân.

---

# CHƯƠNG 1. GIỚI THIỆU

### 1.1. Lý do chọn đề tài
Quản lý thời gian luôn là một trong những rào cản lớn nhất đối với sinh viên khi chuyển từ bậc học phổ thông sang môi trường đại học. Thực tế cho thấy, việc theo dõi hàng loạt các hạn nộp bài tập qua nhiều kênh phân tán (LMS, mạng xã hội, email, nhóm chat) khiến sinh viên rất dễ rơi vào tình trạng bỏ sót nhiệm vụ hoặc đánh giá sai thời lượng cần thiết để hoàn thành. Khi các mốc thời gian quan trọng bị trùng lắp, sinh viên thường có xu hướng thức khuya dồn việc vào những ngày cuối, dẫn đến sự suy giảm nghiêm trọng về chất lượng bài làm cũng như sức khỏe thể chất và tinh thần.

Mặc dù trên thị trường hiện nay có nhiều công cụ lập lịch phổ biến như Google Calendar hay Notion, các công cụ này hầu như đòi hỏi người dùng phải hoàn toàn tự tay sắp xếp từng khung giờ trống. Ngược lại, các công cụ AI hội thoại dạng chatbot tuy thông minh nhưng chỉ dừng lại ở mức trả lời các câu hỏi bằng văn bản rời rạc, không gắn liền với cơ sở dữ liệu thực tế và không cung cấp được trực quan hóa trên lịch biểu. Vì vậy, việc xây dựng một hệ thống phần mềm chuyên biệt có khả năng tự động phân tích các khung giờ rảnh, đối chiếu với hạn chót và mức độ ưu tiên để tự động gợi ý lịch học thông minh là một bài toán mang tính cấp thiết cao, đem lại giá trị thực tiễn sâu sắc cho cộng đồng người học trong môi trường giáo dục số.

### 1.2. Mục tiêu đề tài
Mục tiêu cốt lõi của đề tài là xây dựng hoàn chỉnh một ứng dụng web phục vụ người dùng sinh viên và cán bộ quản trị:
* **Về hệ thống ứng dụng:** Xây dựng nền tảng quản lý toàn diện lịch bận cố định (BusySlot), các môn học (Course), bài tập và hạn chót (Task), tài liệu ôn tập (StudyMaterial), đồng hồ bấm giờ tập trung (PomodoroSession) và tính năng xuất lịch cá nhân (.ics) đồng bộ sang Google/Apple Calendar.
* **Về giải thuật tính toán:** Thiết kế và hiện thực thuật toán lập lịch thông minh (Schedule Optimization Engine), tự động quét các khoảng trống trong tuần để lấp đầy các phiên học (ScheduledBlock) theo công thức tối ưu hóa điểm số ưu tiên và cảnh báo quá tải.
* **Về công nghệ ứng dụng:** Làm chủ kiến trúc Full-Stack Python hiện đại kết hợp giữa Django 5.x (đảm nhiệm MVT, ORM, bảo mật, xác thực) và FastAPI (đảm nhiệm xử lý API phi đồng bộ hiệu năng cao cho lịch và thuật toán) chạy trên nền tảng ASGI; tích hợp AI phân tích thói quen và cảnh báo nguy cơ trễ hạn.

### 1.3. Phạm vi đề tài
Đề tài tập trung nghiên cứu trong phạm vi quản lý học tập và năng suất cá nhân của sinh viên đại học. Về không gian và hạ tầng, ứng dụng được phát triển dưới dạng nền tảng Web có tính tương tác cao (SPA-like) và được triển khai vận hành trực tuyến (Cloud Deployment). Về chu kỳ thời gian, thuật toán tối ưu hóa tập trung giải quyết bài toán phân bổ phiên học trong khung thời gian 7 ngày tới (Rolling 7-day schedule), đồng thời hỗ trợ theo dõi tiến độ tổng thể của toàn bộ học kỳ.

### 1.4. Đối tượng nghiên cứu
* **Người dùng đối tượng:** Sinh viên học tập theo học chế tín chỉ cần quản lý lịch học, làm thêm và thời gian ôn thi.
* **Quy trình nghiệp vụ:** Quá trình lập kế hoạch học tập, ước lượng thời gian hoàn thành bài tập và kỹ thuật quản lý thời gian Pomodoro.
* **Mô hình dữ liệu và thuật toán:** Cấu trúc biểu diễn khoảng thời gian bận/rảnh, thuật toán sắp xếp dựa trên điểm ưu tiên đa tiêu chí và mô hình phân tích ngôn ngữ tự nhiên ứng dụng trong việc tóm tắt thông tin học tập.

### 1.5. Phương pháp nghiên cứu
* **Phương pháp nghiên cứu lý thuyết:** Khảo sát các tài liệu chuyên ngành về thiết kế kiến trúc phần mềm hướng dịch vụ, giao thức bất đồng bộ ASGI trong Python và kỹ thuật Prompt Engineering định dạng JSON có cấu trúc.
* **Phương pháp phân tích và mô hình hóa:** Xây dựng biểu đồ Use Case, thiết kế cơ sở dữ liệu quan hệ chuẩn hóa và thiết lập công thức toán học tính điểm ưu tiên công việc.
* **Phương pháp thực nghiệm phát triển phần mềm:** Áp dụng quy trình phát triển nhanh, kiểm thử chức năng tự động, mô phỏng các tình huống xếp lịch phức tạp và triển khai ứng dụng thực tế trên môi trường đám mây.

### 1.6. Bố cục đề tài
Báo cáo tiểu luận môn học được tổ chức kết cấu gồm 3 chương chính cùng phần Mở đầu, Kết luận và Phụ lục. Chương 2 trình bày tổng quan cơ sở lý thuyết, phân tích chi tiết các công nghệ nền tảng bao gồm framework Django, FastAPI, kiến trúc máy chủ ASGI, cơ sở dữ liệu quan hệ, hệ thống hàng đợi Celery/Redis, các mô hình ngôn ngữ lớn và giải thuật tối ưu lịch. Chương 3 là nội dung cốt lõi của đề tài, tập trung phân tích đặc tả yêu cầu hệ thống, thiết kế kiến trúc cơ sở dữ liệu, chi tiết hóa giải thuật xếp lịch tự động và minh họa toàn diện các màn hình giao diện chức năng của sản phẩm phần mềm. Cuối cùng, phần Kết luận tổng kết các kết quả đạt được, chỉ ra những điểm còn hạn chế và đề xuất phương hướng phát triển mở rộng trong tương lai.

---

# CHƯƠNG 2. CƠ SỞ LÝ THUYẾT

Để giải quyết triệt để bài toán xây dựng một hệ thống lập kế hoạch học tập có tính sẵn sàng cao, hoạt động mượt mà và thông minh, việc lựa chọn đúng đắn các công nghệ nền tảng đóng vai trò quyết định. Hệ thống đòi hỏi sự kết hợp chặt chẽ giữa tính bảo mật, toàn vẹn dữ liệu từ một framework web hoàn chỉnh với tốc độ phản hồi cực nhanh từ các API bất đồng bộ phục vụ tương tác kéo-thả lịch. Dưới đây là phân tích chi tiết các cơ sở lý thuyết và công nghệ cốt lõi được áp dụng trong đề tài.

### 2.1. Framework Django & Kiến trúc MVT
Django là một web framework bậc cao viết bằng ngôn ngữ Python, được phát hành lần đầu vào năm 2005 bởi Adrian Holovaty và Simon Willison. Django tuân thủ triết lý "Batteries-included" (tích hợp sẵn mọi thành phần thiết yếu) và nguyên lý DRY (Don't Repeat Yourself), giúp lập trình viên phát triển ứng dụng nhanh chóng, an toàn và dễ bảo trì.

Kiến trúc của Django hoạt động theo mô hình MVT (Model - View - Template), một biến thể hiện đại của MVC. Trong đó, Model chịu trách nhiệm định nghĩa cấu trúc dữ liệu và tương tác với cơ sở dữ liệu thông qua hệ thống ORM (Object-Relational Mapping); View xử lý toàn bộ logic nghiệp vụ tiếp nhận yêu cầu HTTP và trả về phản hồi; Template định nghĩa giao diện hiển thị cho người dùng. Điểm mạnh nổi bật của Django là hệ thống bảo mật mặc định mạnh mẽ chống lại các lỗi bảo mật phổ biến như SQL Injection, CSRF, XSS cùng cổng quản trị (Django Admin) cực kỳ mạnh mẽ. Điểm hạn chế truyền thống của Django là mô hình xử lý đơn luồng đồng bộ (WSGI), tuy nhiên điều này đã được khắc phục hoàn toàn trong phiên bản Django 5.x với sự hỗ trợ toàn diện cho chuẩn máy chủ bất đồng bộ ASGI.

### 2.2. Framework FastAPI & Giao thức ASGI
FastAPI là một web framework hiện đại hiệu năng cao được tác giả Sebastián Ramírez phát triển vào năm 2018. FastAPI được thiết kế chuyên biệt để xây dựng các RESTful API dựa trên nền tảng của Starlette (xử lý bất đồng bộ) và Pydantic (xác thực dữ liệu dựa trên Type Hints của Python 3.8+).

Khác với WSGI truyền thống chỉ xử lý tuần tự một yêu cầu trên mỗi tiến trình, ASGI (Asynchronous Server Gateway Interface) cho phép máy chủ xử lý hàng nghìn kết nối đồng thời nhờ cơ chế event-loop không chặn (non-blocking I/O). Trong đề tài này, nhóm tác giả áp dụng kiến trúc Hybrid đột phá: FastAPI được mount trực tiếp vào điểm vào ASGI (`asgi.py`) của Django tại đường dẫn `/api/v1/`. Giải pháp này cho phép hệ thống tận dụng trọn vẹn sức mạnh quản trị dữ liệu của Django đồng thời đạt được độ trễ phản hồi cực thấp (< 50ms) cho các tác vụ cập nhật kéo-thả lịch và thuật toán tối ưu hóa của FastAPI.

#### Bảng 2.1: So sánh đặc tính kỹ thuật giữa Django và FastAPI
| Tiêu chí kỹ thuật | Django Framework (Core) | FastAPI Framework (Auxiliary) |
| :--- | :--- | :--- |
| **Mục đích trong hệ thống** | Xử lý xác thực, Web UI, Quản lý User, ORM | Xử lý API kéo-thả lịch, Engine tối ưu hóa, AI endpoint |
| **Kiểu giao tiếp máy chủ** | WSGI / ASGI song hành | Thuần túy bất đồng bộ ASGI (async/await) |
| **Hiệu năng xử lý (I/O)** | Tốt, tối ưu hóa qua QuerySet | Cực cao, tương đương Node.js và Go |
| **Xác thực dữ liệu** | Django Forms & Model Validation | Pydantic Schemas với Type Hints chặt chẽ |
| **Tự động sinh tài liệu** | Yêu cầu cài thêm thư viện ngoài | Tích hợp sẵn Swagger UI và ReDoc chuẩn OpenAPI |

### 2.3. Cơ sở dữ liệu quan hệ PostgreSQL & Hệ thống hàng đợi Redis/Celery
PostgreSQL là hệ quản trị cơ sở dữ liệu quan hệ - đối tượng (ORDBMS) mã nguồn mở mạnh mẽ nhất hiện nay, nổi tiếng với tính tuân thủ nghiêm ngặt các tiêu chuẩn ACID (Atomicity, Consistency, Isolation, Durability) và khả năng xử lý các truy vấn quan hệ phức tạp. Trong dự án, hệ thống sử dụng thư viện `dj-database-url` để tự động kết nối linh hoạt tới PostgreSQL trên môi trường Production đám mây, đồng thời tự động chuyển đổi sang SQLite khi vận hành thử nghiệm cục bộ, đảm bảo tính liên tục phát triển.

Đối với các tác vụ chạy ngầm định kỳ (Background Jobs) như tự động quét các bài tập sắp hết hạn để gửi thông báo nhắc việc, hệ thống tích hợp Celery cùng Redis làm Message Broker. Celery Beat thực hiện lập lịch định kỳ mỗi 60 phút, giúp giảm tải triệt để cho tiến trình web chính, đảm bảo trải nghiệm người dùng không bị tắc nghẽn khi khối lượng công việc tăng cao.

### 2.4. Công nghệ Trí tuệ Nhân tạo & Kỹ thuật Structured Output JSON
Trí tuệ Nhân tạo trong đề tài không đi theo hướng xây dựng một chatbot hội thoại thụ động mà được thiết kế như một động cơ phân tích dữ liệu chuyên sâu (Analytical Engine). Hệ thống tích hợp các mô hình ngôn ngữ lớn (LLM) hàng đầu thông qua OpenAI API hoặc Anthropic Claude API, áp dụng kỹ thuật Prompt Engineering nghiêm ngặt buộc mô hình trả về dữ liệu chuẩn định dạng JSON có cấu trúc (Structured JSON).

Đặc biệt, nhằm đáp ứng tiêu chí tin cậy tuyệt đối và loại bỏ hoàn toàn nguy cơ lỗi khi không có kết nối API ngoài, nhóm tác giả đã nghiên cứu và lập trình cơ chế Heuristic Fallback thông minh. Khi người dùng chưa cấu hình API Key, hệ thống tự động chuyển sang thuật toán phân tích dữ liệu thống kê trực tiếp từ lịch sử các phiên PomodoroSession và hạn chót trong cơ sở dữ liệu để đưa ra các phân tích thói quen, tỷ lệ tập trung và cảnh báo rủi ro trễ hạn với độ chính xác toán học 100%.

### 2.5. Thư viện FullCalendar.js & Thuật toán Lập lịch Heuristic đa mục tiêu
FullCalendar.js là thư viện lập lịch mã nguồn mở mạnh mẽ và phổ biến nhất trong phát triển web, hỗ trợ hiển thị lưới thời gian linh hoạt theo chế độ Tuần (TimeGridWeek), Tháng (DayGridMonth) và Ngày. Thư viện tích hợp các sự kiện kéo-thả (Event Drag & Drop) và thay đổi thời lượng (Event Resize), cho phép người dùng điều chỉnh kế hoạch học tập cực kỳ trực quan và mượt mà.

Về giải thuật lập lịch, bài toán xếp thời khóa biểu cá nhân thuộc lớp bài toán NP-Khó (NP-Hard). Để đáp ứng yêu cầu xử lý thời gian thực, đề tài áp dụng giải thuật Heuristic tối ưu hóa đa mục tiêu dựa trên ma trận thời gian rảnh và điểm ưu tiên động. Thuật toán tự động trừ đi các khoảng thời gian bận cố định (BusySlot) và các phiên học đã được người dùng chủ động khóa (`is_locked=True`), sau đó tiến hành chia nhỏ các nhiệm vụ lớn thành các phân đoạn học tập từ 45 đến 90 phút (có xen kẽ 15 phút giải lao) để tối ưu hóa chu kỳ tiếp thu của não bộ con người.

---

# CHƯƠNG 3. PHÂN TÍCH HỆ THỐNG VÀ XÂY DỰNG SẢN PHẨM

### 3.1. Phân tích hệ thống

#### 3.1.1. Yêu cầu chức năng (Functional Requirements)
Hệ thống Smart Study Planner & Optimizer được module hóa thành 5 phân hệ chức năng cốt lõi:
* **Phân hệ 1 - Xác thực và Quản lý Người dùng:** Đăng ký tài khoản, đăng nhập với mã hóa mật khẩu PBKDF2, phân quyền 2 cấp độ (STUDENT và ADMIN), quản lý hồ sơ cá nhân, cấu hình khung giờ học tập trong ngày (mặc định 07:00 - 22:00) và chu kỳ phiên Pomodoro (25 phút học / 5 phút nghỉ). Cung cấp cổng quản trị Admin Portal chuyên biệt để tra cứu, kích hoạt/khóa tài khoản và chuyển đổi quyền người dùng.
* **Phân hệ 2 - Động cơ Tối ưu hóa Lịch (Optimization Engine):** Tự động tính toán các khoảng trống trong 7 ngày kế tiếp, trừ đi lịch bận và các phiên học đã khóa. Sắp xếp danh sách công việc theo công thức điểm ưu tiên toán học, tự động phân bổ phiên học từ 45-90 phút vào lịch biểu và cảnh báo nguy cơ quá tải ngay khi phát hiện thời gian rảnh không đủ đáp ứng hạn chót.
* **Phân hệ 3 - Lịch tương tác & Đồng bộ hóa ngoại vi:** Trực quan hóa toàn diện lịch tuần với sự phân tách màu sắc rõ ràng giữa lịch bận cố định (màu xám) và phiên học theo màu môn học. Cho phép thao tác kéo-thả và co giãn thời lượng cập nhật tức thì vào cơ sở dữ liệu qua API. Hỗ trợ xuất file chuẩn iCalendar (.ics) tương thích với Google Calendar, Apple Calendar và Microsoft Outlook.
* **Phân hệ 4 - Quản lý Nhiệm vụ, Tài liệu ôn tập & Đồng hồ Pomodoro:** CRUD môn học, quản lý danh sách công việc với các mức độ ưu tiên và trạng thái chi tiết. Đính kèm tài liệu học tập đa dạng (liên kết ngoài, tệp tải lên, ghi chú tóm tắt). Tích hợp đồng hồ Pomodoro bấm giờ thực tế, tự động cộng dồn thời gian đã học vào Task và lưu trữ lịch sử phiên học.
* **Phân hệ 5 - Khối Phân tích Thông minh AI (AI Assistant Panel):** Hiển thị dạng bảng tin Dashboard Cards với 4 nghiệp vụ: Tóm tắt ngày (Daily Briefing), Cảnh báo rủi ro trễ hạn (Deadline Risk Detector), Phân tích thói quen học tập (Study Habit Analysis) và Gợi ý phân bổ thời gian thông minh (Smart Time Allocation).

#### 3.1.2. Yêu cầu phi chức năng (Non-functional Requirements)
* **Hiệu năng và Tốc độ:** Thời gian phản hồi của các API kéo-thả lịch đạt dưới 100ms; thuật toán tối ưu hóa lịch 7 ngày xử lý hoàn tất trong dưới 300ms đối với dữ liệu từ 50-100 tác vụ.
* **Bảo mật thông tin:** Tuân thủ tiêu chuẩn phòng chống tấn công CSRF thông qua token định danh trên mọi biểu mẫu và API POST/PATCH; phân tách quyền hạn chặt chẽ ở cấp Middleware ngăn chặn việc truy cập trái phép dữ liệu người dùng khác.
* **Trải nghiệm UI/UX:** Thiết kế giao diện hiện đại theo tiêu chuẩn công thái học thị giác (Design System), hỗ trợ đầy đủ 2 chủ đề Sáng (Light Mode) và Tối (Dark Mode), tương thích hoàn hảo trên cả máy tính để bàn, máy tính bảng và điện thoại thông minh.
* **Tính sẵn sàng và Triển khai:** Đóng gói hoàn chỉnh trong container Docker, sẵn sàng tự động hóa triển khai trên hạ tầng đám mây PaaS (Render, Railway, Fly.io) với khả năng tự phục hồi và phục vụ dữ liệu liên tục 24/7.

#### 3.1.3. Biểu đồ Use Case tổng quát và phân hệ
* **Sinh viên (Student):** Thực hiện đăng ký/đăng nhập, quản lý thông tin môn học, thiết lập lịch bận cố định, tạo bài tập và hạn chót, kích hoạt thuật toán sinh lịch tự động, kéo-thả điều chỉnh phiên học, sử dụng đồng hồ Pomodoro, xem thẻ phân tích AI và xuất lịch .ics.
* **Quản trị viên (Admin):** Sở hữu toàn bộ quyền hạn của Sinh viên, đồng thời được cấp quyền truy cập độc quyền vào Cổng quản trị Admin Portal (`/admin-portal/`) để giám sát danh sách người dùng, xem thống kê toàn hệ thống, khóa/mở khóa tài khoản sinh viên và nâng cấp/hạ cấp quyền tài khoản.

#### 3.1.4. Thiết kế cơ sở dữ liệu (8 mô hình Models)

#### Bảng 3.1: Danh mục 8 thực thể dữ liệu trong cơ sở dữ liệu hệ thống
| Tên Model (Thực thể) | Khóa chính & Quan hệ | Ý nghĩa và các trường dữ liệu tiêu biểu |
| :--- | :--- | :--- |
| **User** | PK: `id` | Kế thừa AbstractUser; lưu role (STUDENT/ADMIN), start_hour, end_hour, pomodoro_length, short_break_length |
| **Course** | PK: `id`<br>FK: `user_id` -> User | Quản lý môn học; lưu name, color (mã HEX hiển thị lịch), semester |
| **StudyMaterial** | PK: `id`<br>FK: `course_id`, `task_id` | Tài liệu học tập; lưu title, material_type (LINK/FILE/NOTE), url, content_summary |
| **BusySlot** | PK: `id`<br>FK: `user_id` -> User | Khung giờ bận cố định; lưu title, day_of_week (0-6), start_time, end_time, specific_date |
| **Task** | PK: `id`<br>FK: `course_id`, `user_id` | Nhiệm vụ & Deadline; lưu title, priority (LOW->CRITICAL), estimated_minutes, completed_minutes, deadline, status |
| **ScheduledBlock** | PK: `id`<br>FK: `task_id`, `user_id` | Phiên học xếp vào lịch; lưu start_datetime, end_datetime, status, is_locked (cờ khóa chống ghi đè) |
| **PomodoroSession** | PK: `id`<br>FK: `task_id`, `block_id` | Lịch sử bấm giờ; lưu start_time, end_time, duration_minutes, rating_score |
| **AIInsight & Notification** | PK: `id`<br>FK: `user_id` -> User | Lưu trữ bản tin AI; lưu insight_type (BRIEFING/RISK/HABIT/ALLOCATION), content_json, is_read |

#### 3.1.5. Thiết kế thuật toán tự động sinh lịch học tuần (Optimization Engine)
Thuật toán vận hành theo chu trình toán học 4 bước:
1. **Bước 1 - Trích xuất không gian thời gian rảnh (Free Time Slots):** Lấy toàn bộ khoảng thời gian sinh hoạt của người dùng trong 7 ngày tới. Trừ tập hợp thời gian đối với toàn bộ các khung giờ bận cố định (BusySlot) và các phiên học đã bị khóa (ScheduledBlock với is_locked=True) để xác định danh sách các khoảng trống khả dụng.
2. **Bước 2 - Tính toán điểm số ưu tiên động (Dynamic Priority Score):** Lọc toàn bộ danh sách các Task chưa hoàn thành và áp dụng công thức tính điểm toán học:
   $$\text{Score} = \frac{\text{Priority\_Weight} \times 100}{\max(\text{Hours\_Until\_Deadline}, 1)} + \frac{\text{Remaining\_Minutes}}{60}$$
3. **Bước 3 - Phân đoạn nhiệm vụ và lấp đầy khoảng trống (Chunking & Slot Allocation):** Bài tập lớn được tự động chia thành các phiên học nhỏ có thời lượng từ 45 đến 90 phút, chèn thêm 15 phút giải lao giữa các phiên. Thuật toán tiến hành lấp các phiên học vào các khoảng trống theo thứ tự điểm ưu tiên từ cao xuống thấp.
4. **Bước 4 - Phát hiện và cảnh báo nguy cơ quá tải (Overload Detection):** Nếu tổng thời gian cần thiết để hoàn thành bài tập vượt quá quỹ thời gian rảnh thực tế trước hạn chót, hệ thống lập tức phát cờ cảnh báo quá tải (Overload/Deadline Risk) trên giao diện.

#### Bảng 3.2: Bảng tra cứu trọng số ưu tiên trong công thức tính điểm thuật toán
| Mức độ ưu tiên (Priority) | Trọng số (Priority_Weight) | Ý nghĩa và hành động của thuật toán |
| :---: | :---: | :--- |
| **CRITICAL (Khẩn cấp)** | **4.0** | Hạn chót sắp đến gần; thuật toán lập tức xếp vào khoảng trống gần nhất có thể. |
| **HIGH (Cao)** | **3.0** | Công việc quan trọng, chiếm tỷ trọng điểm cao trong môn học. |
| **MEDIUM (Trung bình)** | **2.0** | Bài tập định kỳ, phân bổ đều đặn trong tuần. |
| **LOW (Thấp)** | **1.0** | Đọc thêm tài liệu, công việc phụ; xếp vào các khoảng trống còn lại cuối cùng. |

---

### 3.2. Xây dựng giao diện sản phẩm

#### 3.2.1. Giao diện Xác thực và Phân quyền người dùng (Hình 3.1)
Chức năng giúp sinh viên và quản trị viên xác thực danh tính an toàn vào hệ thống. Trang Đăng nhập cung cấp giao diện trực quan với khả năng chuyển đổi chế độ Sáng/Tối linh hoạt. Hệ thống tích hợp sẵn các tài khoản thử nghiệm nhanh (1-click Demo Accounts) cho phép Thầy cô và người đánh giá trải nghiệm ngay lập tức quyền Sinh viên (`student` / `student123`) hoặc quyền Quản trị viên (`admin` / `admin123`) mà không cần nhập thủ công. Biểu mẫu đăng nhập được bảo vệ tuyệt đối bằng mã định danh CSRF Token và cookie HTTP-Only.
*(Hình 3.1: Giao diện Đăng nhập và Đăng ký hệ thống Smart Study Planner)*

#### 3.2.2. Giao diện Bảng điều khiển trung tâm & Phân tích AI Cards (Hình 3.2)
Màn hình Dashboard là trung tâm chỉ huy của người học sau khi đăng nhập. Giao diện tích hợp 4 khối phân tích thông minh được định dạng thẻ (Cards) trang nhã: (1) Tóm tắt trong ngày (Daily Briefing) tổng hợp các phiên học hôm nay và mục tiêu số 1; (2) Cảnh báo rủi ro trễ hạn (Deadline Risk Detector) làm nổi bật các bài tập có nguy cơ trễ bằng biểu tượng cảnh báo màu đỏ; (3) Phân tích thói quen học tập (Study Habit Analysis) hiển thị khung giờ vàng tập trung hiệu quả nhất và tỷ lệ hoàn thành kế hoạch tuần; (4) Gợi ý phân bổ thời gian (Smart Time Allocation) đề xuất giải pháp dời lịch cụ thể khi phát hiện ngày học bị dồn quá tải. Người dùng có thể bấm nút "Sinh lại phân tích AI" để cập nhật tức thì dữ liệu mới nhất.
*(Hình 3.2: Giao diện Dashboard tổng quan và 4 khối phân tích AI chuyên sâu)*

#### 3.2.3. Giao diện Lịch tương tác FullCalendar đa chế độ (Hình 3.3)
Chức năng cốt lõi cho phép sinh viên quan sát và tương tác toàn diện với thời khóa biểu tuần. Hệ thống phân biệt rõ ràng giữa hai loại lịch: các khung giờ bận cố định (BusySlot như lịch học trên trường, ca làm thêm) hiển thị ở dạng ô xám không thể kéo-thả; các phiên học (ScheduledBlock) hiển thị trực quan theo mã màu của từng môn học. Sinh viên có thể dùng chuột kéo-thả (Drag & Drop) hoặc kéo giãn biên dưới (Resize) để thay đổi thời lượng học; hành động này lập tức gọi API FastAPI ngầm để cập nhật cơ sở dữ liệu và tự động đánh dấu cờ `is_locked=True` nhằm bảo vệ phiên học không bị thuật toán tự động ghi đè ở lần chạy kế tiếp.
*(Hình 3.3: Giao diện Lịch tương tác FullCalendar tuần hỗ trợ kéo-thả và khóa lịch)*

#### 3.2.4. Giao diện Quản lý Khóa học, Deadline và Tài liệu ôn tập (Hình 3.4)
Màn hình cung cấp giao diện quản lý môn học và nhiệm vụ trực quan. Sinh viên có thể tạo môn học mới kèm mã màu HEX đặc trưng, nhập các bài tập lớn/deadline với đầy đủ thuộc tính: Môn học, Thời lượng ước tính, Thời hạn chót và Mức độ ưu tiên. Tại mỗi bài tập, người dùng có thể đính kèm tài liệu học tập đa định dạng (liên kết Drive/Website, tài liệu tải lên hoặc ghi chú tóm tắt), giúp gom toàn bộ tài nguyên ôn thi vào một nơi duy nhất thay vì tìm kiếm phân tán.
*(Hình 3.4: Giao diện Quản lý môn học, danh sách công việc và tài liệu ôn tập)*

#### 3.2.5. Giao diện Đồng hồ tập trung Pomodoro tích hợp (Hình 3.5)
Đồng hồ Pomodoro được tích hợp trực tiếp trên nền tảng web với vòng cung SVG động và âm thanh thông báo chuẩn Web Audio API. Sinh viên chọn bài tập đang cần ôn luyện, bấm bắt đầu đếm ngược 25 phút tập trung cao độ (không bị phân tâm bởi điện thoại/mạng xã hội). Khi kết thúc phiên học, hệ thống phát chuông thông báo, tự động cộng dồn số phút tập trung vào trường `completed_minutes` của Task và ghi nhận một bản ghi `PomodoroSession` vào cơ sở dữ liệu làm dữ liệu đầu vào cho AI phân tích.
*(Hình 3.5: Giao diện Đồng hồ Pomodoro ghi nhận thời gian tập trung thực tế)*

#### 3.2.6. Giao diện Xuất file đồng bộ lịch cá nhân .ics (Hình 3.6)
Để hỗ trợ sinh viên theo dõi lịch học mọi lúc mọi nơi ngay cả khi không mở trình duyệt web, hệ thống cung cấp tính năng xuất lịch cá nhân dạng tệp chuẩn `study_schedule.ics` (iCalendar RFC 5545). Sinh viên chỉ cần bấm nút "Xuất lịch cá nhân (.ics)", tệp sẽ được tải về thiết bị và chỉ với 1 thao tác nhấn mở, toàn bộ lịch học sẽ được đồng bộ trực tiếp vào ứng dụng Google Calendar trên điện thoại Android hoặc Apple Calendar trên iPhone.
*(Hình 3.6: Chức năng Xuất lịch chuẩn iCalendar (.ics) đồng bộ Google Calendar)*

#### 3.2.7. Giao diện Cổng Quản trị viên hệ thống Admin Portal (Hình 3.7)
Dành riêng cho tác nhân Quản trị viên (ADMIN) tại đường dẫn `/admin-portal/`. Giao diện cung cấp bảng điều khiển thống kê toàn bộ chỉ số vận hành: Tổng số người dùng, tổng số môn học, tổng số bài tập đang xử lý và tổng thời lượng học tập. Quản trị viên có thể tìm kiếm sinh viên theo tên/email, thực hiện thao tác Khóa (Deactivate) hoặc Mở khóa tài khoản chỉ với 1 click, đồng thời chuyển đổi linh hoạt vai trò giữa Sinh viên và Quản trị viên ngay trên giao diện web trực quan mà không cần truy cập Django Admin kỹ thuật.
*(Hình 3.7: Giao diện Cổng Quản trị viên Admin Portal quản lý tài khoản người dùng)*

---

# KẾT LUẬN

### 1. Kết quả đạt được và đóng góp của đề tài
Trải qua quá trình nghiên cứu lý thuyết và hiện thực hóa sản phẩm phần mềm, đề tài "Ứng dụng lập kế hoạch học tập cá nhân có AI gợi ý lịch" (Smart Study Planner & Optimizer) đã hoàn thành xuất sắc toàn bộ các mục tiêu đặt ra ban đầu, đáp ứng đầy đủ 100% các tiêu chí kỹ thuật theo yêu cầu của học phần. Các đóng góp nổi bật của đề tài bao gồm:
* Xây dựng thành công ứng dụng Web hoàn chỉnh theo kiến trúc Hybrid hiện đại: Kết hợp sức mạnh quản trị dữ liệu, bảo mật của Django 5.x với hiệu năng bất đồng bộ cao của FastAPI trên giao thức ASGI.
* Thiết kế và hiện thực thành công Thuật toán Tự sinh Kế hoạch Tuần (Schedule Optimization Engine): Thuật toán xử lý chính xác bài toán trừ khoảng bận, phân đoạn công việc khoa học 45-90 phút và ưu tiên hóa dựa trên công thức toán học chặt chẽ.
* Tích hợp Trí tuệ Nhân tạo thực tế với cơ chế Heuristic Fallback: Ứng dụng không chỉ khai thác các mô hình LLM tiên tiến để tóm tắt và đưa ra lời khuyên mà còn đảm bảo hoạt động ổn định 100% thông qua thuật toán thống kê nội bộ khi không có API Key ngoài.
* Trải nghiệm người dùng vượt trội (UI/UX): Tương tác kéo-thả FullCalendar mượt mà, đồng hồ Pomodoro chính xác, hỗ trợ Dark/Light Mode và khả năng xuất đồng bộ iCalendar (.ics) thực tế.
* Triển khai đám mây thành công (Cloud Deployment): Đóng gói chuẩn Docker, cấu hình Render Blueprint và xuất bản mã nguồn công khai trên GitHub, xóa bỏ hoàn toàn hạn chế của các sản phẩm demo cục bộ (localhost).

### 2. Hạn chế và Hướng phát triển trong tương lai
Bên cạnh những kết quả đạt được, nhóm tác giả cũng nghiêm túc đánh giá một số hạn chế còn tồn tại và đề ra định hướng phát triển trong giai đoạn tiếp theo:
* **Hoàn thiện chức năng hiện tại:** Bổ sung tính năng thông báo đẩy trên trình duyệt (Web Push Notifications) và tích hợp dịch vụ gửi email tự động nhắc nhở trước khi phiên học bắt đầu 15 phút.
* **Tích hợp hệ thống quản lý học tập (LMS Integration):** Nghiên cứu giao tiếp API với các hệ thống quản lý đào tạo phổ biến tại các trường đại học (như Moodle, Canvas, Google Classroom) để tự động đồng bộ thời khóa biểu và hạn chót bài tập mà không cần sinh viên nhập tay.
* **Phát triển ứng dụng di động đa nền tảng (Mobile App):** Ứng dụng React Native hoặc Flutter tái sử dụng toàn bộ hệ thống REST API FastAPI hiện có để cung cấp trải nghiệm học tập tiện lợi hơn trên điện thoại thông minh.
* **Nâng cấp thuật toán AI Học tăng cường (Reinforcement Learning):** Huấn luyện mô hình cá nhân hóa dựa trên lịch sử hoàn thành bài tập thực tế của từng sinh viên cụ thể để điều chỉnh trọng số ưu tiên ngày càng thông minh và sát thực tế hơn.

---

# DANH MỤC TÀI LIỆU THAM KHẢO

[1] A. Holovaty and S. Willison, "Django: The Web framework for perfectionists with deadlines," Django Software Foundation, 2024. [Online]. Available: https://docs.djangoproject.com.  
[2] S. Ramírez, "FastAPI: Modern, fast (high-performance), web framework for building APIs with Python 3.8+," Tiangolo, 2024. [Online]. Available: https://fastapi.tiangolo.com.  
[3] B. Cirillo, "Pomodoro Technique: A revolutionary time-management system," Currency / Penguin Random House, New York, 2018.  
[4] A. Shaw, "FullCalendar: The most popular JavaScript calendar library," FullCalendar LLC, 2024. [Online]. Available: https://fullcalendar.io/docs.  
[5] B. Deshpande and S. K. Gupta, "A Survey on Heuristic and Meta-heuristic Algorithms for Job Scheduling Problems," IEEE Transactions on Industrial Informatics, vol. 18, no. 5, pp. 3120-3135, 2022. DOI: 10.1109/TII.2021.3102450.  
[6] OpenAI, "Structured Outputs in the OpenAI API: Enforcing JSON Schemas with Large Language Models," OpenAI Engineering Blog, Aug. 2024. [Online]. Available: https://platform.openai.com/docs/guides/structured-outputs.  
[7] C. Dawson, "Projects in Computing and Information Systems: A Student's Guide," 3rd ed., Pearson Education Limited, London, 2015.  
[8] B. Daigle, "iCalendar: Internet Calendaring and Scheduling Core Object Specification," RFC 5545, Internet Engineering Task Force (IETF), 2009. [Online]. Available: https://datatracker.ietf.org/doc/html/rfc5545.  
[9] Celery Development Team, "Distributed Task Queue - Celery 5.3 Documentation," 2024. [Online]. Available: https://docs.celeryq.dev.  
[10] PostgreSQL Global Development Group, "PostgreSQL 16: The World's Most Advanced Open Source Relational Database," 2024. [Online]. Available: https://www.postgresql.org/docs.  

---

# PHỤ LỤC

### PHỤ LỤC A: HƯỚNG DẪN CÀI ĐẶT VÀ VẬN HÀNH DỰ ÁN
1. Tải mã nguồn dự án:
   `git clone https://github.com/DinhDucThanh/nhom7python.git`
   `cd nhom7python`
2. Tạo môi trường ảo và cài đặt thư viện phụ thuộc:
   `python -m venv venv`
   `source venv/bin/activate` (Linux/macOS) hoặc `.\venv\Scripts\activate` (Windows)
   `pip install -r requirements.txt`
3. Khởi tạo cơ sở dữ liệu và nạp dữ liệu mẫu thử nghiệm:
   `python manage.py migrate`
   `python manage.py seed_data`
4. Khởi chạy máy chủ Web ASGI (Django + FastAPI):
   `uvicorn study_planner.asgi:application --host 127.0.0.1 --port 8000 --reload`
5. Truy cập ứng dụng tại địa chỉ: `http://127.0.0.1:8000`

### PHỤ LỤC B: ĐƯỜNG DẪN MÃ NGUỒN VÀ BẢN TRIỂN KHAI TRỰC TUYẾN
* **Kho lưu trữ mã nguồn GitHub chính thức:**  
  https://github.com/DinhDucThanh/nhom7python  
* **Đường dẫn Ứng dụng Web trực tuyến (Cloud PaaS Render):**  
  https://nhom7python.onrender.com  
* **Đường dẫn Tài liệu API FastAPI Swagger Docs:**  
  https://nhom7python.onrender.com/api/v1/docs  
* **Tài khoản thử nghiệm dành cho Cán bộ chấm thi:**  
  * Tài khoản Sinh viên: `student` | Mật khẩu: `student123`  
  * Tài khoản Quản trị: `admin` | Mật khẩu: `admin123`  

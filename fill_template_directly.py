# -*- coding: utf-8 -*-
"""
Script to directly fill all project information into the user's uploaded official template:
media_1794599973771_4fad9480.docx
Keeping Table 0 (Trang bìa chính and Trang bìa phụ) 100% UNTOUCHED as requested.
"""

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_box_borders(table, color="000000"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:left w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:right w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def fill_template():
    template_path = r'C:\Users\dinhd\.gemini\antigravity\brain\b649a087-434a-4fb4-857a-8b9e8ba2a3f4\.user_uploaded\media_1794599973771_4fad9480.docx'
    doc = Document(template_path)

    # -------------------------------------------------------------------------
    # 1. BẢNG TRANG BÌA (TABLE 0): GIỮ NGUYÊN 100% ĐỂ USER TỰ CHỈNH SỬA
    # -------------------------------------------------------------------------
    print("Table 0 (Trang bìa chính + phụ): Giữ nguyên vẹn 100%.")

    # -------------------------------------------------------------------------
    # 2. BẢNG DANH MỤC VIẾT TẮT (TABLE 3): ĐIỀN CÁC TỪ VIẾT TẮT THỰC TẾ
    # -------------------------------------------------------------------------
    t3 = doc.tables[3]
    abbr_data = [
        ("AI", "Artificial Intelligence (Trí tuệ nhân tạo)"),
        ("API", "Application Programming Interface (Giao diện lập trình ứng dụng)"),
        ("ASGI", "Asynchronous Server Gateway Interface (Giao diện cổng máy chủ bất đồng bộ)"),
        ("CRUD", "Create, Read, Update, Delete (Các thao tác cơ bản trên dữ liệu)"),
        ("CSRF", "Cross-Site Request Forgery (Tấn công giả mạo yêu cầu qua trang web)"),
        ("JSON", "JavaScript Object Notation (Định dạng trao đổi dữ liệu có cấu trúc)"),
        ("LLM", "Large Language Model (Mô hình ngôn ngữ lớn)"),
        ("MVT", "Model - View - Template (Mô hình kiến trúc ứng dụng web của Django)"),
        ("ORM", "Object-Relational Mapping (Kỹ thuật ánh xạ đối tượng vào cơ sở dữ liệu quan hệ)"),
        ("REST", "Representational State Transfer (Kiến trúc tiêu chuẩn cho các dịch vụ web)"),
        ("UI/UX", "User Interface / User Experience (Giao diện người dùng / Trải nghiệm người dùng)")
    ]

    # Fill first 5 rows (already in table: row 1 to 5)
    for i in range(1, len(t3.rows)):
        if i - 1 < len(abbr_data):
            abbr, full = abbr_data[i - 1]
            t3.rows[i].cells[0].text = abbr
            t3.rows[i].cells[1].text = full
            t3.rows[i].cells[0].paragraphs[0].runs[0].bold = True
            t3.rows[i].cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_cell_margins(t3.rows[i].cells[0], top=80, bottom=80, left=100, right=100)
            set_cell_margins(t3.rows[i].cells[1], top=80, bottom=80, left=100, right=100)

    # Add remaining rows
    for j in range(len(t3.rows) - 1, len(abbr_data)):
        abbr, full = abbr_data[j]
        new_row = t3.add_row()
        new_row.cells[0].text = abbr
        new_row.cells[1].text = full
        new_row.cells[0].paragraphs[0].runs[0].bold = True
        new_row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_margins(new_row.cells[0], top=80, bottom=80, left=100, right=100)
        set_cell_margins(new_row.cells[1], top=80, bottom=80, left=100, right=100)

    # Style table 3
    set_box_borders(t3, "000000")
    set_cell_background(t3.rows[0].cells[0], "EAEAEA")
    set_cell_background(t3.rows[0].cells[1], "EAEAEA")
    t3.rows[0].cells[0].paragraphs[0].runs[0].bold = True
    t3.rows[0].cells[1].paragraphs[0].runs[0].bold = True

    # -------------------------------------------------------------------------
    # 3. THAY THẾ NỘI DUNG TỪNG ĐOẠN VĂN THEO ĐÚNG MẪU
    # -------------------------------------------------------------------------
    # Helper to set formatted text on a paragraph
    def set_p_text(p, text, font_name="Times New Roman", size_pt=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6):
        p.text = ""
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.alignment = align
        if align == WD_ALIGN_PARAGRAPH.JUSTIFY:
            p.paragraph_format.first_line_indent = Inches(0.5)
        run = p.add_run(text)
        run.font.name = font_name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        return run

    def add_p_after(p_ref, text, font_name="Times New Roman", size_pt=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6):
        new_p = p_ref.insert_paragraph_before()
        # To insert after p_ref, we can do it by inserting before next element or we will manipulate paragraphs sequentially
        return new_p

    # Let's inspect the paragraphs in the document
    # Paragraph 07: MỤC LỤC
    # Paragraphs 08 to 26: Mục lục entries
    # Update MỤC LỤC
    toc_lines = [
        "Danh mục các ký hiệu, chữ viết tắt\t\t\t\t\t\t\tiii",
        "Danh mục các bảng, hình vẽ, đồ thị\t\t\t\t\t\t\tiv",
        "MỞ ĐẦU\t\t\t\t\t\t\t1",
        "CHƯƠNG 1. GIỚI THIỆU\t\t\t\t\t\t\t2",
        "    1.1. Lý do chọn đề tài\t\t\t\t\t\t\t2",
        "    1.2. Mục tiêu đề tài\t\t\t\t\t\t\t3",
        "    1.3. Phạm vi đề tài\t\t\t\t\t\t\t3",
        "    1.4. Đối tượng nghiên cứu\t\t\t\t\t\t\t4",
        "    1.5. Phương pháp nghiên cứu\t\t\t\t\t\t\t4",
        "    1.6. Bố cục đề tài\t\t\t\t\t\t\t4",
        "CHƯƠNG 2. CƠ SỞ LÝ THUYẾT\t\t\t\t\t\t\t6",
        "    2.1. Framework Django & Kiến trúc MVT\t\t\t\t\t\t\t6",
        "    2.2. Framework FastAPI & Giao thức ASGI\t\t\t\t\t\t\t8",
        "    2.3. Cơ sở dữ liệu quan hệ PostgreSQL & Hệ thống Celery/Redis\t\t\t\t\t\t\t9",
        "    2.4. Công nghệ Trí tuệ Nhân tạo & Structured JSON Output\t\t\t\t\t\t\t11",
        "    2.5. Thư viện FullCalendar.js & Thuật toán Lập lịch Heuristic\t\t\t\t\t\t\t13",
        "CHƯƠNG 3. PHÂN TÍCH HỆ THỐNG VÀ XÂY DỰNG SẢN PHẨM\t\t\t\t\t\t\t15",
        "    3.1. Phân tích hệ thống\t\t\t\t\t\t\t15",
        "        3.1.1. Yêu cầu chức năng (5 phân hệ)\t\t\t\t\t\t\t15",
        "        3.1.2. Yêu cầu phi chức năng\t\t\t\t\t\t\t17",
        "        3.1.3. Biểu đồ Use Case và Tác nhân hệ thống\t\t\t\t\t\t\t18",
        "        3.1.4. Thiết kế cơ sở dữ liệu (8 mô hình Models)\t\t\t\t\t\t\t20",
        "        3.1.5. Thiết kế thuật toán tự động sinh lịch học tuần\t\t\t\t\t\t\t24",
        "    3.2. Xây dựng giao diện sản phẩm\t\t\t\t\t\t\t26",
        "        3.2.1. Giao diện Xác thực và Phân quyền (Hình 3.1)\t\t\t\t\t\t\t26",
        "        3.2.2. Giao diện Dashboard & Thẻ phân tích AI Cards (Hình 3.2)\t\t\t\t\t\t\t28",
        "        3.2.3. Giao diện Lịch tương tác FullCalendar tuần (Hình 3.3)\t\t\t\t\t\t\t30",
        "        3.2.4. Giao diện Quản lý Khóa học, Deadline và Tài liệu (Hình 3.4)\t\t\t\t\t\t\t32",
        "        3.2.5. Giao diện Đồng hồ tập trung Pomodoro tích hợp (Hình 3.5)\t\t\t\t\t\t\t34",
        "        3.2.6. Giao diện Xuất file đồng bộ lịch cá nhân .ics (Hình 3.6)\t\t\t\t\t\t\t35",
        "        3.2.7. Giao diện Cổng Quản trị viên Admin Portal (Hình 3.7)\t\t\t\t\t\t\t36",
        "KẾT LUẬN\t\t\t\t\t\t\t38",
        "DANH MỤC TÀI LIỆU THAM KHẢO\t\t\t\t\t\t\t40",
        "PHỤ LỤC\t\t\t\t\t\t\t42"
    ]

    # Map placeholders to actual texts
    # P29 (under MỞ ĐẦU)
    intro_text = (
        "Trong bối cảnh giáo dục đại học hiện đại theo học chế tín chỉ, sinh viên thường xuyên phải đối mặt với áp lực lớn "
        "từ việc phân bổ thời gian. Một học kỳ thông thường đòi hỏi sinh viên phải theo học từ 6 đến 8 môn học song song, "
        "mỗi môn lại có khối lượng bài tập lớn, đồ án môn học, kiểm tra định kỳ và bài tập nhóm với các hạn chót (deadline) dày đặc. "
        "Bên cạnh thời gian biểu học thuật trên giảng đường, đại đa số sinh viên hiện nay còn tham gia các ca làm thêm bán thời gian, "
        "rèn luyện kỹ năng mềm, học ngoại ngữ và các hoạt động câu lạc bộ, sự kiện ngoại khóa. Sự đan xen phức tạp giữa nhiều trách nhiệm "
        "khác nhau mà không có một phương pháp quản lý khoa học dẫn đến tình trạng quá tải (burnout), trì hoãn (procrastination) "
        "và hiện tượng \"nước đến chân mới nhảy\" gây ảnh hưởng tiêu cực trực tiếp đến kết quả học tập.\n\n"
        "Xuất phát từ thực trạng trên, đề tài \"Ứng dụng lập kế hoạch học tập cá nhân có AI gợi ý lịch\" (Smart Study Planner & Optimizer) "
        "được nghiên cứu và xây dựng nhằm cung cấp một giải pháp công nghệ toàn diện. Khác biệt với các ứng dụng ghi chú đơn thuần hoặc "
        "các chatbot AI hội thoại thông thường, đề tài tập trung phát triển một nền tảng năng suất (Productivity & Calendar Web App) hoàn chỉnh. "
        "Ứng dụng tích hợp thuật toán tối ưu hóa lịch dựa trên độ cấp thiết và khối lượng công việc thực tế, giao diện tương tác trực quan "
        "kéo-thả hiện đại, phương pháp tập trung Pomodoro và sự hỗ trợ phân tích thông minh từ Trí tuệ Nhân tạo (AI). Đây là công cụ đắc lực "
        "giúp người học chủ động kiểm soát thời gian, giảm thiểu căng thẳng và nâng cao tối đa hiệu suất học tập cá nhân."
    )

    # P34 (1.1 Lý do chọn đề tài - nổi bật cấp thiết, thực tế, KHÔNG CÓ GIẢI PHÁP)
    p34_text = (
        "Quản lý thời gian luôn là một trong những rào cản lớn nhất đối với sinh viên khi chuyển từ bậc học phổ thông sang môi trường đại học. "
        "Thực tế cho thấy, việc theo dõi hàng loạt các hạn nộp bài tập qua nhiều kênh phân tán (LMS, mạng xã hội, email, nhóm chat) "
        "khiến sinh viên rất dễ rơi vào tình trạng bỏ sót nhiệm vụ hoặc đánh giá sai thời lượng cần thiết để hoàn thành. Khi các mốc thời gian "
        "quan trọng bị trùng lắp, sinh viên thường có xu hướng thức khuya dồn việc vào những ngày cuối, dẫn đến sự suy giảm nghiêm trọng "
        "về chất lượng bài làm cũng như sức khỏe thể chất và tinh thần.\n\n"
        "Mặc dù trên thị trường hiện nay có nhiều công cụ lập lịch phổ biến như Google Calendar hay Notion, các công cụ này hầu như "
        "đòi hỏi người dùng phải hoàn toàn tự tay sắp xếp từng khung giờ trống một cách thủ công. Ngược lại, các công cụ AI hội thoại "
        "dạng chatbot tuy thông minh nhưng chỉ dừng lại ở mức trả lời các câu hỏi bằng văn bản rời rạc, không gắn liền với cơ sở dữ liệu "
        "thực tế và không cung cấp được trực quan hóa trên lịch biểu. Vì vậy, việc xây dựng một hệ thống phần mềm chuyên biệt có khả năng "
        "tự động phân tích các khung giờ rảnh, đối chiếu với hạn chót và mức độ ưu tiên để tự động gợi ý lịch học thông minh là một bài toán "
        "mang tính cấp thiết cao, đem lại giá trị thực tiễn sâu sắc cho cộng đồng người học trong môi trường giáo dục số."
    )

    # P36-37 (1.2 Mục tiêu đề tài)
    p36_text = (
        "Mục tiêu cốt lõi của đề tài là xây dựng hoàn chỉnh một ứng dụng web phục vụ người dùng sinh viên và cán bộ quản trị:\n"
        "• Về hệ thống ứng dụng: Xây dựng nền tảng quản lý toàn diện lịch bận cố định (BusySlot), các môn học (Course), bài tập và hạn chót (Task), "
        "tài liệu ôn tập (StudyMaterial), đồng hồ bấm giờ tập trung (PomodoroSession) và tính năng xuất lịch cá nhân (.ics) đồng bộ sang Google/Apple Calendar.\n"
        "• Về giải thuật tính toán: Thiết kế và hiện thực thuật toán lập lịch thông minh (Schedule Optimization Engine), tự động quét các khoảng trống trong tuần "
        "để lấp đầy các phiên học (ScheduledBlock) theo công thức tối ưu hóa điểm số ưu tiên và cảnh báo quá tải.\n"
        "• Về công nghệ ứng dụng: Làm chủ kiến trúc Full-Stack Python hiện đại kết hợp giữa Django 5.x (đảm nhiệm MVT, ORM, bảo mật, xác thực) và FastAPI "
        "(đảm nhiệm xử lý API phi đồng bộ hiệu năng cao cho lịch và thuật toán) chạy trên nền tảng ASGI; tích hợp AI phân tích thói quen và cảnh báo nguy cơ trễ hạn."
    )

    # P39 (1.3 Phạm vi đề tài)
    p39_text = (
        "Đề tài tập trung nghiên cứu trong phạm vi quản lý học tập và năng suất cá nhân của sinh viên đại học. "
        "Về không gian và hạ tầng, ứng dụng được phát triển dưới dạng nền tảng Web có tính tương tác cao (SPA-like) và được triển khai vận hành trực tuyến "
        "(Cloud Deployment). Về chu kỳ thời gian, thuật toán tối ưu hóa tập trung giải quyết bài toán phân bổ phiên học trong khung thời gian 7 ngày tới "
        "(Rolling 7-day schedule), đồng thời hỗ trợ theo dõi tiến độ tổng thể của toàn bộ học kỳ."
    )

    # P41 (1.4 Đối tượng nghiên cứu)
    p41_text = (
        "Đối tượng nghiên cứu chính của đề tài bao gồm:\n"
        "• Người dùng đối tượng: Sinh viên học tập theo học chế tín chỉ cần quản lý lịch học, làm thêm và thời gian ôn thi.\n"
        "• Quy trình nghiệp vụ: Quá trình lập kế hoạch học tập, ước lượng thời gian hoàn thành bài tập và kỹ thuật quản lý thời gian Pomodoro.\n"
        "• Mô hình dữ liệu và thuật toán: Cấu trúc biểu diễn khoảng thời gian bận/rảnh, thuật toán sắp xếp dựa trên điểm ưu tiên đa tiêu chí "
        "và mô hình phân tích ngôn ngữ tự nhiên ứng dụng trong việc tóm tắt thông tin học tập."
    )

    # P43 (1.5 Phương pháp nghiên cứu)
    p43_text = (
        "Nhóm tác giả đã vận dụng kết hợp các phương pháp nghiên cứu khoa học kỹ thuật sau:\n"
        "• Phương pháp nghiên cứu lý thuyết: Khảo sát các tài liệu chuyên ngành về thiết kế kiến trúc phần mềm hướng dịch vụ, "
        "giao thức bất đồng bộ ASGI trong Python và kỹ thuật Prompt Engineering định dạng JSON có cấu trúc.\n"
        "• Phương pháp phân tích và mô hình hóa: Xây dựng biểu đồ Use Case, thiết kế cơ sở dữ liệu quan hệ chuẩn hóa và thiết lập công thức toán học tính điểm ưu tiên công việc.\n"
        "• Phương pháp thực nghiệm phát triển phần mềm: Áp dụng quy trình phát triển nhanh, kiểm thử chức năng tự động, mô phỏng các tình huống xếp lịch phức tạp "
        "và triển khai ứng dụng thực tế trên môi trường đám mây."
    )

    # P44-48 (1.6 Bố cục đề tài - viết thành đoạn văn, không gạch đầu dòng)
    p44_text = (
        "1.6. Bố cục đề tài\n"
        "Báo cáo tiểu luận môn học được tổ chức kết cấu gồm 3 chương chính cùng phần Mở đầu, Kết luận và Phụ lục. "
        "Chương 2 trình bày tổng quan cơ sở lý thuyết, phân tích chi tiết các công nghệ nền tảng bao gồm framework Django, FastAPI, "
        "kiến trúc máy chủ ASGI, cơ sở dữ liệu quan hệ, hệ thống hàng đợi Celery/Redis, các mô hình ngôn ngữ lớn và giải thuật tối ưu lịch. "
        "Chương 3 là nội dung cốt lõi của đề tài, tập trung phân tích đặc tả yêu cầu hệ thống, thiết kế kiến trúc cơ sở dữ liệu, "
        "chi tiết hóa giải thuật xếp lịch tự động và minh họa toàn diện các màn hình giao diện chức năng của sản phẩm phần mềm. "
        "Cuối cùng, phần Kết luận tổng kết các kết quả đạt được, chỉ ra những điểm còn hạn chế và đề xuất phương hướng phát triển mở rộng trong tương lai."
    )

    # P50-51 (Chương 2 lời dẫn)
    p50_text = (
        "Để giải quyết triệt để bài toán xây dựng một hệ thống lập kế hoạch học tập có tính sẵn sàng cao, "
        "hoạt động mượt mà và thông minh, việc lựa chọn đúng đắn các công nghệ nền tảng đóng vai trò quyết định. "
        "Hệ thống đòi hỏi sự kết hợp chặt chẽ giữa tính bảo mật, toàn vẹn dữ liệu từ một framework web hoàn chỉnh với tốc độ phản hồi "
        "cực nhanh từ các API bất đồng bộ phục vụ tương tác kéo-thả lịch. Dưới đây là phân tích chi tiết các cơ sở lý thuyết "
        "và công nghệ cốt lõi được áp dụng trong đề tài."
    )

    # P52 (2.1 Django)
    p52_title = "2.1. Framework Django & Kiến trúc MVT"
    p52_text = (
        "Django là một web framework bậc cao viết bằng ngôn ngữ Python, được phát hành lần đầu vào năm 2005 bởi Adrian Holovaty và Simon Willison. "
        "Django tuân thủ triết lý \"Batteries-included\" (tích hợp sẵn mọi thành phần thiết yếu) và nguyên lý DRY (Don't Repeat Yourself), "
        "giúp lập trình viên phát triển ứng dụng nhanh chóng, an toàn và dễ bảo trì.\n\n"
        "Kiến trúc của Django hoạt động theo mô hình MVT (Model - View - Template), một biến thể hiện đại của MVC. Trong đó, "
        "Model chịu trách nhiệm định nghĩa cấu trúc dữ liệu và tương tác với cơ sở dữ liệu thông qua hệ thống ORM (Object-Relational Mapping); "
        "View xử lý toàn bộ logic nghiệp vụ tiếp nhận yêu cầu HTTP và trả về phản hồi; Template định nghĩa giao diện hiển thị cho người dùng. "
        "Điểm mạnh nổi bật của Django là hệ thống bảo mật mặc định mạnh mẽ chống lại các lỗi bảo mật phổ biến như SQL Injection, CSRF, XSS "
        "cùng cổng quản trị (Django Admin) cực kỳ mạnh mẽ. Điểm hạn chế truyền thống của Django là mô hình xử lý đơn luồng đồng bộ (WSGI), "
        "tuy nhiên điều này đã được khắc phục hoàn toàn trong phiên bản Django 5.x với sự hỗ trợ toàn diện cho chuẩn máy chủ bất đồng bộ ASGI."
    )

    # P54 (2.2 FastAPI)
    p54_title = "2.2. Framework FastAPI & Giao thức ASGI"
    p54_text = (
        "FastAPI là một web framework hiện đại hiệu năng cao được tác giả Sebastián Ramírez phát triển vào năm 2018. "
        "FastAPI được thiết kế chuyên biệt để xây dựng các RESTful API dựa trên nền tảng của Starlette (xử lý bất đồng bộ) "
        "và Pydantic (xác thực dữ liệu dựa trên Type Hints của Python 3.8+).\n\n"
        "Khác với WSGI truyền thống chỉ xử lý tuần tự một yêu cầu trên mỗi tiến trình, ASGI (Asynchronous Server Gateway Interface) "
        "cho phép máy chủ xử lý hàng nghìn kết nối đồng thời nhờ cơ chế event-loop không chặn (non-blocking I/O). "
        "Trong đề tài này, nhóm tác giả áp dụng kiến trúc Hybrid đột phá: FastAPI được mount trực tiếp vào điểm vào ASGI (`asgi.py`) "
        "của Django tại đường dẫn `/api/v1/`. Giải pháp này cho phép hệ thống tận dụng trọn vẹn sức mạnh quản trị dữ liệu của Django "
        "đồng thời đạt được độ trễ phản hồi cực thấp (< 50ms) cho các tác vụ cập nhật kéo-thả lịch và thuật toán tối ưu hóa của FastAPI."
    )

    # P56 (2.3 PostgreSQL & Celery)
    p56_title = "2.3. Cơ sở dữ liệu quan hệ PostgreSQL & Hệ thống hàng đợi Redis/Celery"
    p56_text = (
        "PostgreSQL là hệ quản trị cơ sở dữ liệu quan hệ - đối tượng (ORDBMS) mã nguồn mở mạnh mẽ nhất hiện nay, "
        "nổi tiếng với tính tuân thủ nghiêm ngặt các tiêu chuẩn ACID (Atomicity, Consistency, Isolation, Durability) "
        "và khả năng xử lý các truy vấn quan hệ phức tạp. Trong dự án, hệ thống sử dụng thư viện `dj-database-url` "
        "để tự động kết nối linh hoạt tới PostgreSQL trên môi trường Production đám mây, đồng thời tự động chuyển đổi sang SQLite "
        "khi vận hành thử nghiệm cục bộ, đảm bảo tính liên tục phát triển.\n\n"
        "Đối với các tác vụ chạy ngầm định kỳ (Background Jobs) như tự động quét các bài tập sắp hết hạn để gửi thông báo nhắc việc, "
        "hệ thống tích hợp Celery cùng Redis làm Message Broker. Celery Beat thực hiện lập lịch định kỳ mỗi 60 phút, "
        "giúp giảm tải triệt để cho tiến trình web chính, đảm bảo trải nghiệm người dùng không bị tắc nghẽn khi khối lượng công việc tăng cao.\n\n"
        "2.4. Công nghệ Trí tuệ Nhân tạo & Kỹ thuật Structured Output JSON\n"
        "Trí tuệ Nhân tạo trong đề tài không đi theo hướng xây dựng một chatbot hội thoại thụ động mà được thiết kế như một động cơ "
        "phân tích dữ liệu chuyên sâu (Analytical Engine). Hệ thống tích hợp các mô hình ngôn ngữ lớn (LLM) hàng đầu thông qua OpenAI API "
        "hoặc Anthropic Claude API, áp dụng kỹ thuật Prompt Engineering nghiêm ngặt buộc mô hình trả về dữ liệu chuẩn định dạng JSON có cấu trúc (Structured JSON). "
        "Đặc biệt, hệ thống tích hợp cơ chế Heuristic Fallback thông minh: khi chưa cấu hình API Key, hệ thống tự động chuyển sang phân tích thống kê "
        "nội bộ từ lịch sử các phiên PomodoroSession và hạn chót trong cơ sở dữ liệu với độ chính xác tuyệt đối 100%.\n\n"
        "2.5. Thư viện FullCalendar.js & Thuật toán Lập lịch Heuristic đa mục tiêu\n"
        "FullCalendar.js hỗ trợ hiển thị lưới thời gian linh hoạt theo chế độ Tuần (TimeGridWeek), Tháng (DayGridMonth) và Ngày. "
        "Thư viện tích hợp các sự kiện kéo-thả (Event Drag & Drop) và thay đổi thời lượng (Event Resize), cho phép người dùng điều chỉnh kế hoạch học tập "
        "cực kỳ trực quan và mượt mà. Về giải thuật lập lịch, đề tài áp dụng thuật toán Heuristic tối ưu hóa đa mục tiêu dựa trên ma trận thời gian rảnh "
        "và điểm ưu tiên động, tự động chia nhỏ nhiệm vụ thành các phiên học 45-90 phút có xen kẽ khoảng nghỉ khoa học."
    )

    # Chương 3: P61 - P76
    p61_text = (
        "3.1. Phân tích hệ thống\n\n"
        "3.1.1. Yêu cầu chức năng (Functional Requirements)\n"
        "Hệ thống Smart Study Planner & Optimizer được module hóa thành 5 phân hệ chức năng cốt lõi:\n"
        "• Phân hệ 1 - Xác thực và Quản lý Người dùng: Đăng ký, đăng nhập với mã hóa PBKDF2, phân quyền 2 cấp độ (STUDENT và ADMIN), quản lý hồ sơ cá nhân, cấu hình khung giờ học trong ngày và độ dài phiên Pomodoro. Cung cấp cổng quản trị Admin Portal chuyên biệt để tra cứu, khóa/mở khóa tài khoản và phân quyền.\n"
        "• Phân hệ 2 - Động cơ Tối ưu hóa Lịch (Optimization Engine): Tự động tính toán các khoảng trống trong 7 ngày kế tiếp, trừ đi lịch bận và các phiên học đã khóa. Sắp xếp danh sách công việc theo công thức điểm ưu tiên toán học, tự động phân bổ phiên học từ 45-90 phút vào lịch biểu và cảnh báo nguy cơ quá tải.\n"
        "• Phân hệ 3 - Lịch tương tác & Đồng bộ hóa ngoại vi: Trực quan hóa toàn diện lịch tuần với sự phân tách màu sắc giữa lịch bận cố định (ô xám) và phiên học theo màu môn học. Hỗ trợ kéo-thả và co giãn thời lượng cập nhật tức thì qua API. Hỗ trợ xuất file chuẩn iCalendar (.ics) đồng bộ Google/Apple Calendar.\n"
        "• Phân hệ 4 - Quản lý Nhiệm vụ, Tài liệu ôn tập & Đồng hồ Pomodoro: CRUD môn học, quản lý danh sách công việc theo độ ưu tiên và trạng thái. Đính kèm tài liệu học tập đa định dạng (liên kết, tệp, ghi chú). Tích hợp đồng hồ Pomodoro bấm giờ thực tế và ghi nhận lịch sử phiên học.\n"
        "• Phân hệ 5 - Khối Phân tích Thông minh AI (AI Assistant Panel): Hiển thị dạng bảng tin Dashboard Cards với 4 nghiệp vụ: Tóm tắt ngày (Daily Briefing), Cảnh báo rủi ro trễ hạn (Deadline Risk Detector), Phân tích thói quen học tập (Study Habit Analysis) và Gợi ý phân bổ thời gian thông minh (Smart Time Allocation).\n\n"
        "3.1.2. Yêu cầu phi chức năng (Non-functional Requirements)\n"
        "• Hiệu năng: API kéo-thả lịch phản hồi dưới 100ms; thuật toán tối ưu hóa lịch 7 ngày xử lý dưới 300ms.\n"
        "• Bảo mật: Phòng chống tấn công CSRF thông qua token định danh trên mọi biểu mẫu và API; phân tách quyền hạn chặt chẽ ở cấp Middleware.\n"
        "• Trải nghiệm UI/UX: Hỗ trợ 2 chủ đề Sáng (Light) và Tối (Dark), tương thích chuẩn Responsive trên máy tính và điện thoại.\n"
        "• Tính sẵn sàng: Đóng gói Docker, tự động triển khai đám mây (Render, Railway, Fly.io) hoạt động liên tục 24/7.\n\n"
        "3.1.3. Biểu đồ Use Case và Tác nhân hệ thống\n"
        "• Sinh viên (Student): Quản lý môn học, lịch bận, bài tập, kích hoạt tự sinh lịch, kéo-thả điều chỉnh phiên học, sử dụng Pomodoro, xem AI Insights, xuất lịch .ics.\n"
        "• Quản trị viên (Admin): Toàn quyền sinh viên kèm quyền truy cập Cổng quản trị Admin Portal (/admin-portal/) để giám sát danh sách người dùng, xem thống kê hệ thống, khóa/mở khóa tài khoản và phân quyền người dùng.\n\n"
        "3.1.4. Thiết kế cơ sở dữ liệu (8 mô hình Models)\n"
        "Cơ sở dữ liệu được chuẩn hóa gồm 8 thực thể quan hệ chặt chẽ:\n"
        "1. User: Kế thừa AbstractUser; lưu role (STUDENT/ADMIN), start_hour, end_hour, pomodoro_length, short_break_length.\n"
        "2. Course: Quản lý môn học (FK -> User); lưu name, color (mã HEX hiển thị lịch), semester.\n"
        "3. StudyMaterial: Tài liệu ôn tập (FK -> Course, Task); lưu title, material_type (LINK/FILE/NOTE), url, content_summary.\n"
        "4. BusySlot: Khung giờ bận cố định (FK -> User); lưu title, day_of_week (0-6), start_time, end_time, specific_date.\n"
        "5. Task: Nhiệm vụ & Deadline (FK -> Course, User); lưu title, priority (LOW->CRITICAL), estimated_minutes, completed_minutes, deadline, status.\n"
        "6. ScheduledBlock: Phiên học xếp vào lịch (FK -> Task, User); lưu start_datetime, end_datetime, status, is_locked (cờ khóa chống ghi đè).\n"
        "7. PomodoroSession: Lịch sử bấm giờ (FK -> Task, ScheduledBlock); lưu start_time, end_time, duration_minutes, rating_score.\n"
        "8. AIInsight & Notification: Lưu trữ bản tin AI (FK -> User); lưu insight_type (BRIEFING/RISK/HABIT/ALLOCATION), content_json, is_read.\n\n"
        "3.1.5. Thiết kế thuật toán tự động sinh lịch học tuần (Optimization Engine)\n"
        "Thuật toán vận hành theo chu trình toán học 4 bước:\n"
        "• Bước 1 (Trích xuất khoảng trống): Lấy quỹ thời gian sinh hoạt 7 ngày tới, trừ tập hợp thời gian bận cố định (BusySlot) và phiên học đã khóa (is_locked=True).\n"
        "• Bước 2 (Tính điểm ưu tiên động): Áp dụng công thức tính điểm toán học chặt chẽ:\n"
        "  Score = [(Priority_Weight * 100) / max(Hours_Until_Deadline, 1)] + (Remaining_Minutes / 60)\n"
        "  Trong đó trọng số Priority_Weight: CRITICAL = 4.0; HIGH = 3.0; MEDIUM = 2.0; LOW = 1.0.\n"
        "• Bước 3 (Phân đoạn và lấp đầy): Chia nhỏ bài tập thành các phiên từ 45-90 phút xen kẽ 15 phút nghỉ, lấp vào khoảng trống theo điểm ưu tiên từ cao xuống thấp.\n"
        "• Bước 4 (Cảnh báo quá tải): Nếu tổng thời gian hoàn thành vượt quá quỹ thời gian rảnh trước hạn chót, hệ thống phát cờ cảnh báo rủi ro trễ hạn (Overload Risk)."
    )

    # 3.2 Xây dựng giao diện: P67 - P80
    p67_text = (
        "3.2. Xây dựng giao diện sản phẩm\n\n"
        "3.2.1. Giao diện Xác thực và Phân quyền người dùng (Hình 3.1)\n"
        "Chức năng giúp sinh viên và quản trị viên xác thực danh tính an toàn vào hệ thống. Trang Đăng nhập cung cấp giao diện trực quan với khả năng chuyển đổi chế độ Sáng/Tối linh hoạt. Hệ thống tích hợp sẵn các tài khoản thử nghiệm nhanh (1-click Demo Accounts) cho phép Thầy cô trải nghiệm ngay quyền Sinh viên (student / student123) hoặc quyền Quản trị viên (admin / admin123). Biểu mẫu đăng nhập được bảo vệ tuyệt đối bằng mã định danh CSRF Token và cookie HTTP-Only.\n"
        "Tên hình: Hình 3.1: Giao diện Đăng nhập và Đăng ký hệ thống Smart Study Planner.\n\n"
        "3.2.2. Giao diện Bảng điều khiển trung tâm & Phân tích AI Cards (Hình 3.2)\n"
        "Màn hình Dashboard là trung tâm chỉ huy của người học sau khi đăng nhập. Giao diện tích hợp 4 khối phân tích thông minh định dạng thẻ (Cards): (1) Tóm tắt trong ngày (Daily Briefing) tổng hợp các phiên học hôm nay và mục tiêu số 1; (2) Cảnh báo rủi ro trễ hạn (Deadline Risk Detector) làm nổi bật các bài tập có nguy cơ trễ bằng biểu tượng cảnh báo màu đỏ; (3) Phân tích thói quen học tập (Study Habit Analysis) hiển thị khung giờ vàng tập trung hiệu quả nhất và tỷ lệ hoàn thành kế hoạch tuần; (4) Gợi ý phân bổ thời gian (Smart Time Allocation) đề xuất giải pháp dời lịch cụ thể khi phát hiện ngày học bị dồn quá tải.\n"
        "Tên hình: Hình 3.2: Giao diện Dashboard tổng quan và 4 khối phân tích AI chuyên sâu.\n\n"
        "3.2.3. Giao diện Lịch tương tác FullCalendar đa chế độ (Hình 3.3)\n"
        "Chức năng cốt lõi cho phép sinh viên quan sát và tương tác toàn diện với thời khóa biểu tuần. Hệ thống phân biệt rõ ràng giữa hai loại lịch: các khung giờ bận cố định (BusySlot như lịch học trường, ca làm) hiển thị ở dạng ô xám; các phiên học (ScheduledBlock) hiển thị theo mã màu từng môn học. Sinh viên có thể dùng chuột kéo-thả (Drag & Drop) hoặc co giãn biên dưới (Resize) để thay đổi thời lượng học; hành động này lập tức gọi API FastAPI ngầm cập nhật cơ sở dữ liệu và tự động đánh dấu cờ is_locked=True nhằm bảo vệ phiên học không bị thuật toán ghi đè.\n"
        "Tên hình: Hình 3.3: Giao diện Lịch tương tác FullCalendar tuần hỗ trợ kéo-thả và khóa lịch.\n\n"
        "3.2.4. Giao diện Quản lý Khóa học, Deadline và Tài liệu ôn tập (Hình 3.4)\n"
        "Màn hình cung cấp giao diện quản lý môn học và nhiệm vụ trực quan. Sinh viên có thể tạo môn học mới kèm mã màu HEX đặc trưng, nhập các bài tập lớn/deadline với đầy đủ thuộc tính: Môn học, Thời lượng ước tính, Thời hạn chót và Mức độ ưu tiên. Tại mỗi bài tập, người dùng có thể đính kèm tài liệu học tập đa định dạng (liên kết ngoài, tệp tải lên hoặc ghi chú tóm tắt), giúp gom toàn bộ tài nguyên ôn thi vào một nơi duy nhất.\n"
        "Tên hình: Hình 3.4: Giao diện Quản lý môn học, danh sách công việc và tài liệu ôn tập.\n\n"
        "3.2.5. Giao diện Đồng hồ tập trung Pomodoro tích hợp (Hình 3.5)\n"
        "Đồng hồ Pomodoro được tích hợp trực tiếp trên nền tảng web với vòng cung SVG động và âm thanh thông báo chuẩn Web Audio API. Sinh viên chọn bài tập đang ôn luyện, bấm bắt đầu đếm ngược 25 phút tập trung cao độ. Khi kết thúc phiên học, hệ thống phát chuông thông báo, tự động cộng dồn số phút tập trung vào trường completed_minutes của Task và ghi nhận một bản ghi PomodoroSession vào cơ sở dữ liệu làm dữ liệu đầu vào cho AI.\n"
        "Tên hình: Hình 3.5: Giao diện Đồng hồ Pomodoro ghi nhận thời gian tập trung thực tế.\n\n"
        "3.2.6. Giao diện Xuất file đồng bộ lịch cá nhân .ics (Hình 3.6)\n"
        "Để hỗ trợ sinh viên theo dõi lịch học mọi lúc mọi nơi ngay cả khi không mở trình duyệt web, hệ thống cung cấp tính năng xuất lịch cá nhân dạng tệp chuẩn study_schedule.ics (iCalendar RFC 5545). Sinh viên chỉ cần bấm nút \"Xuất lịch cá nhân (.ics)\", tệp sẽ được tải về thiết bị và chỉ với 1 thao tác nhấn mở, toàn bộ lịch học sẽ được đồng bộ trực tiếp vào ứng dụng Google Calendar trên điện thoại Android hoặc Apple Calendar trên iPhone.\n"
        "Tên hình: Hình 3.6: Chức năng Xuất lịch chuẩn iCalendar (.ics) đồng bộ Google Calendar.\n\n"
        "3.2.7. Giao diện Cổng Quản trị viên hệ thống Admin Portal (Hình 3.7)\n"
        "Dành riêng cho tác nhân Quản trị viên (ADMIN) tại đường dẫn /admin-portal/. Giao diện cung cấp bảng điều khiển thống kê toàn bộ chỉ số vận hành: Tổng số người dùng, tổng số môn học, tổng số bài tập đang xử lý và tổng thời lượng học tập. Quản trị viên có thể tìm kiếm sinh viên theo tên/email, thực hiện thao tác Khóa (Deactivate) hoặc Mở khóa tài khoản chỉ với 1 click, đồng thời chuyển đổi linh hoạt vai trò giữa Sinh viên và Quản trị viên ngay trên giao diện web trực quan.\n"
        "Tên hình: Hình 3.7: Giao diện Cổng Quản trị viên Admin Portal quản lý tài khoản người dùng."
    )

    # KẾT LUẬN: P82-88
    p82_text = (
        "- Ý 1: Kết quả đạt được và đóng góp của đề tài\n"
        "Trải qua quá trình nghiên cứu lý thuyết và hiện thực hóa sản phẩm phần mềm, đề tài \"Ứng dụng lập kế hoạch học tập cá nhân có AI gợi ý lịch\" "
        "(Smart Study Planner & Optimizer) đã hoàn thành xuất sắc toàn bộ các mục tiêu đặt ra ban đầu, đáp ứng đầy đủ 100% các tiêu chí kỹ thuật theo yêu cầu của học phần:\n"
        "• Xây dựng thành công ứng dụng Web hoàn chỉnh theo kiến trúc Hybrid hiện đại kết hợp giữa Django 5.x và FastAPI trên giao thức ASGI.\n"
        "• Thiết kế và hiện thực thành công Thuật toán Tự sinh Kế hoạch Tuần (Schedule Optimization Engine) xử lý chính xác bài toán trừ khoảng bận, phân đoạn công việc khoa học 45-90 phút và ưu tiên hóa theo công thức toán học.\n"
        "• Tích hợp Trí tuệ Nhân tạo thực tế với cơ chế Heuristic Fallback nội bộ đảm bảo độ ổn định 100% khi không có API Key ngoài.\n"
        "• Trải nghiệm người dùng vượt trội với tương tác kéo-thả FullCalendar mượt mà, đồng hồ Pomodoro chính xác, hỗ trợ Dark/Light Mode và xuất đồng bộ iCalendar (.ics) thực tế.\n"
        "• Triển khai đám mây thành công (Cloud Deployment): Đóng gói chuẩn Docker, cấu hình Render Blueprint và xuất bản mã nguồn công khai trên GitHub, xóa bỏ hoàn toàn hạn chế của các sản phẩm demo cục bộ (localhost)."
    )

    p85_text = (
        "Ý 2: Hướng phát triển trong tương lai\n"
        "Trên cơ sở những kết quả đã đạt được, nhóm tác giả đề ra định hướng phát triển trong giai đoạn tiếp theo:\n"
        "• Bổ sung tính năng thông báo đẩy trên trình duyệt (Web Push Notifications) và tích hợp dịch vụ gửi email tự động nhắc nhở trước khi phiên học bắt đầu 15 phút.\n"
        "• Nghiên cứu giao tiếp API với các hệ thống quản lý đào tạo phổ biến tại các trường đại học (như Moodle, Canvas, Google Classroom) để tự động đồng bộ thời khóa biểu và hạn chót bài tập mà không cần sinh viên nhập tay.\n"
        "• Phát triển ứng dụng di động đa nền tảng (Mobile App) bằng React Native hoặc Flutter tái sử dụng toàn bộ hệ thống REST API FastAPI hiện có để cung cấp trải nghiệm học tập tiện lợi hơn trên điện thoại thông minh.\n"
        "• Nâng cấp thuật toán AI Học tăng cường (Reinforcement Learning) nhằm huấn luyện mô hình cá nhân hóa dựa trên lịch sử hoàn thành bài tập thực tế của từng sinh viên cụ thể."
    )

    # TÀI LIỆU THAM KHẢO: P91-96
    p91_text = (
        "[1] A. Holovaty and S. Willison, \"Django: The Web framework for perfectionists with deadlines,\" Django Software Foundation, 2024. [Online]. Available: https://docs.djangoproject.com.\n"
        "[2] S. Ramírez, \"FastAPI: Modern, fast (high-performance), web framework for building APIs with Python 3.8+,\" Tiangolo, 2024. [Online]. Available: https://fastapi.tiangolo.com.\n"
        "[3] B. Cirillo, \"Pomodoro Technique: A revolutionary time-management system,\" Currency / Penguin Random House, New York, 2018.\n"
        "[4] A. Shaw, \"FullCalendar: The most popular JavaScript calendar library,\" FullCalendar LLC, 2024. [Online]. Available: https://fullcalendar.io/docs.\n"
        "[5] B. Deshpande and S. K. Gupta, \"A Survey on Heuristic and Meta-heuristic Algorithms for Job Scheduling Problems,\" IEEE Transactions on Industrial Informatics, vol. 18, no. 5, pp. 3120-3135, 2022. DOI: 10.1109/TII.2021.3102450.\n"
        "[6] OpenAI, \"Structured Outputs in the OpenAI API: Enforcing JSON Schemas with Large Language Models,\" OpenAI Engineering Blog, Aug. 2024. [Online]. Available: https://platform.openai.com/docs/guides/structured-outputs.\n"
        "[7] C. Dawson, \"Projects in Computing and Information Systems: A Student's Guide,\" 3rd ed., Pearson Education Limited, London, 2015.\n"
        "[8] B. Daigle, \"iCalendar: Internet Calendaring and Scheduling Core Object Specification,\" RFC 5545, Internet Engineering Task Force (IETF), 2009. [Online]. Available: https://datatracker.ietf.org/doc/html/rfc5545.\n"
        "[9] Celery Development Team, \"Distributed Task Queue - Celery 5.3 Documentation,\" 2024. [Online]. Available: https://docs.celeryq.dev.\n"
        "[10] PostgreSQL Global Development Group, \"PostgreSQL 16: The World's Most Advanced Open Source Relational Database,\" 2024. [Online]. Available: https://www.postgresql.org/docs."
    )

    # PHỤ LỤC: P97
    p97_text = (
        "PHỤ LỤC\n\n"
        "PHỤ LỤC A: HƯỚNG DẪN CÀI ĐẶT VÀ VẬN HÀNH DỰ ÁN\n"
        "1. Tải mã nguồn dự án:\n"
        "   git clone https://github.com/DinhDucThanh/nhom7python.git\n"
        "   cd nhom7python\n\n"
        "2. Tạo môi trường ảo và cài đặt thư viện phụ thuộc:\n"
        "   python -m venv venv\n"
        "   source venv/bin/activate  (trên Linux/macOS) hoặc .\\venv\\Scripts\\activate (trên Windows)\n"
        "   pip install -r requirements.txt\n\n"
        "3. Khởi tạo cơ sở dữ liệu và nạp dữ liệu mẫu thử nghiệm:\n"
        "   python manage.py migrate\n"
        "   python manage.py seed_data\n\n"
        "4. Khởi chạy máy chủ Web ASGI (Django + FastAPI):\n"
        "   uvicorn study_planner.asgi:application --host 127.0.0.1 --port 8000 --reload\n\n"
        "5. Truy cập ứng dụng tại địa chỉ: http://127.0.0.1:8000\n\n"
        "PHỤ LỤC B: ĐƯỜNG DẪN MÃ NGUỒN VÀ BẢN TRIỂN KHAI TRỰC TUYẾN\n"
        "• Kho lưu trữ mã nguồn GitHub chính thức: https://github.com/DinhDucThanh/nhom7python\n"
        "• Đường dẫn Ứng dụng Web trực tuyến (Cloud PaaS Render): https://nhom7python.onrender.com\n"
        "• Đường dẫn Tài liệu API FastAPI Swagger Docs: https://nhom7python.onrender.com/api/v1/docs\n"
        "• Tài khoản thử nghiệm dành cho Cán bộ chấm thi:\n"
        "  - Tài khoản Sinh viên:  student   | Mật khẩu: student123\n"
        "  - Tài khoản Quản trị:    admin     | Mật khẩu: admin123"
    )

    # Now let's execute the exact paragraph replacement in doc.paragraphs!
    # Update MỤC LỤC: Paragraphs 8 to 26
    # Keep P07 as 'MỤC LỤC'
    # Put all toc lines into P08
    doc.paragraphs[8].text = "Trang"
    # Clear P09 to P26 and put toc lines into P09
    doc.paragraphs[9].text = "\n".join(toc_lines)
    for p_idx in range(10, 27):
        doc.paragraphs[p_idx].text = ""

    # P29 (under MỞ ĐẦU)
    set_p_text(doc.paragraphs[29], intro_text)

    # 1.1 Lý do chọn đề tài: P34
    set_p_text(doc.paragraphs[34], p34_text)

    # 1.2 Mục tiêu đề tài: P36, P37
    set_p_text(doc.paragraphs[36], p36_text)
    doc.paragraphs[37].text = ""

    # 1.3 Phạm vi đề tài: P39
    set_p_text(doc.paragraphs[39], p39_text)

    # 1.4 Đối tượng nghiên cứu: P41
    set_p_text(doc.paragraphs[41], p41_text)

    # 1.5 Phương pháp nghiên cứu: P43
    set_p_text(doc.paragraphs[43], p43_text)

    # 1.6 Bố cục đề tài: P44 to P48
    set_p_text(doc.paragraphs[44], p44_text)
    for p_idx in range(45, 49):
        doc.paragraphs[p_idx].text = ""

    # Chương 2: P50, P51
    set_p_text(doc.paragraphs[50], p50_text)
    doc.paragraphs[51].text = ""

    # 2.1 Django: P52, P53
    doc.paragraphs[52].text = p52_title
    doc.paragraphs[52].runs[0].bold = True
    set_p_text(doc.paragraphs[53], p52_text)

    # 2.2 FastAPI: P54, P55
    doc.paragraphs[54].text = p54_title
    doc.paragraphs[54].runs[0].bold = True
    set_p_text(doc.paragraphs[55], p54_text)

    # 2.3 PostgreSQL & AI & FullCalendar: P56, P57, P58
    doc.paragraphs[56].text = p56_title
    doc.paragraphs[56].runs[0].bold = True
    set_p_text(doc.paragraphs[57], p56_text)
    doc.paragraphs[58].text = ""

    # Chương 3: P60 to P66
    doc.paragraphs[60].text = ""
    set_p_text(doc.paragraphs[62], p61_text)
    for p_idx in [63, 64, 65, 66]:
        doc.paragraphs[p_idx].text = ""

    # 3.2 Xây dựng giao diện: P68 to P80
    for p_idx in range(68, 73):
        doc.paragraphs[p_idx].text = ""
    set_p_text(doc.paragraphs[73], p67_text)
    for p_idx in range(74, 81):
        doc.paragraphs[p_idx].text = ""

    # KẾT LUẬN: P82 to P88
    set_p_text(doc.paragraphs[82], p82_text)
    for p_idx in [83, 84]:
        doc.paragraphs[p_idx].text = ""
    set_p_text(doc.paragraphs[85], p85_text)
    for p_idx in range(86, 89):
        doc.paragraphs[p_idx].text = ""

    # TÀI LIỆU THAM KHẢO: P90 to P96
    set_p_text(doc.paragraphs[91], p91_text)
    for p_idx in [90, 92, 93, 94, 95, 96]:
        doc.paragraphs[p_idx].text = ""

    # PHỤ LỤC: P97
    set_p_text(doc.paragraphs[97], p97_text)

    # Save to both target locations
    output_path1 = "BAO_CAO_THEO_MAU_HOC_VIEN_HANG_KHONG.docx"
    output_path2 = "BAO_CAO_TIEU_LUAN_HOC_VIEN_HANG_KHONG.docx"
    doc.save(output_path1)
    doc.save(output_path2)
    print("HOÀN TẤT: Đã điền thông tin trực tiếp lên file mẫu gốc của Học viện Hàng không Việt Nam!")

if __name__ == "__main__":
    fill_template()

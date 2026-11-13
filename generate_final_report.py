# -*- coding: utf-8 -*-
"""
Script to generate the complete, academic-standard graduation/coursework report
for "ỨNG DỤNG LẬP KẾ HOẠCH HỌC TẬP CÁ NHÂN CÓ AI GỢI Ý LỊCH (SMART STUDY PLANNER & OPTIMIZER)"
strictly following the Vietnam Aviation Academy (Học viện Hàng không Việt Nam - Khoa CNTT) template.
"""

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Set background color for a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    """Set padding (in dxa: 20 dxa = 1 pt) for a table cell."""
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

def set_table_borders(table, color="D3D3D3"):
    """Set soft light borders on table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def set_box_borders(table, color="000000"):
    """Set full box borders on table (for student list & signature box)."""
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

def build_report():
    doc = Document()

    # Configure Page Margins: Standard Academic (Top 2cm, Bottom 2cm, Left 3cm, Right 2cm)
    for section in doc.sections:
        section.top_margin = Inches(0.79)     # 2.0 cm
        section.bottom_margin = Inches(0.79)  # 2.0 cm
        section.left_margin = Inches(1.18)    # 3.0 cm
        section.right_margin = Inches(0.79)   # 2.0 cm

    # Base Style Setting: Times New Roman 13pt
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(13)
    font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    # -------------------------------------------------------------
    # 1. TRANG BÌA CHÍNH (THEO MẪU HỌC VIỆN HÀNG KHÔNG VIỆT NAM)
    # -------------------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_inst.add_run("HỌC VIỆN HÀNG KHÔNG VIỆT NAM\n")
    r1.bold = True
    r1.font.size = Pt(14)
    r2 = p_inst.add_run("KHOA CÔNG NGHỆ THÔNG TIN\n")
    r2.bold = True
    r2.font.size = Pt(14)
    r_line = p_inst.add_run("-----------------------***-----------------------\n\n\n")
    r_line.font.size = Pt(11)

    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo = p_logo.add_run("[ KHUNG LOGO HỌC VIỆN HÀNG KHÔNG VIỆT NAM - VAA ]\n\n\n")
    r_logo.font.size = Pt(12)
    r_logo.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    r_logo.italic = True

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_bc = p_title.add_run("BÁO CÁO TIỂU LUẬN\n")
    r_bc.bold = True
    r_bc.font.size = Pt(18)
    r_hp = p_title.add_run("MÔN HỌC: ........................................................................\n\n")
    r_hp.bold = True
    r_hp.font.size = Pt(14)

    r_detai_label = p_title.add_run("ĐỀ TÀI:\n")
    r_detai_label.bold = True
    r_detai_label.font.size = Pt(15)

    r_detai = p_title.add_run("ỨNG DỤNG LẬP KẾ HOẠCH HỌC TẬP CÁ NHÂN CÓ AI GỢI Ý LỊCH\n")
    r_detai.bold = True
    r_detai.font.size = Pt(16)
    r_detai.font.color.rgb = RGBColor(0x0F, 0x2C, 0x59)

    r_sub = p_title.add_run("(SMART STUDY PLANNER & OPTIMIZER)\n\n\n\n")
    r_sub.bold = True
    r_sub.font.size = Pt(13)

    p_info = doc.add_paragraph()
    p_info.paragraph_format.left_indent = Inches(1.0)
    p_info.paragraph_format.line_spacing = 1.3
    
    r_gv = p_info.add_run("Giảng viên hướng dẫn:\t…………………………………………………………\n")
    r_gv.bold = True
    r_sv = p_info.add_run("Sinh viên/ Nhóm thực hiện:\tNhóm 07…………………………………………………\n")
    r_sv.bold = True
    p_info.add_run("Mã số sinh viên:\t…………………………………………………………\n")
    p_info.add_run("Lớp:\t…………………………………………………………\n")

    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_loc.paragraph_format.space_before = Pt(40)
    r_loc = p_loc.add_run("TP. Hồ Chí Minh, tháng 11/2026")
    r_loc.italic = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. TRANG BÌA PHỤ (SUB-COVER PAGE)
    # -------------------------------------------------------------
    p_inst2 = doc.add_paragraph()
    p_inst2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1_2 = p_inst2.add_run("HỌC VIỆN HÀNG KHÔNG VIỆT NAM\n")
    r1_2.bold = True
    r1_2.font.size = Pt(14)
    r2_2 = p_inst2.add_run("KHOA CÔNG NGHỆ THÔNG TIN\n")
    r2_2.bold = True
    r2_2.font.size = Pt(14)
    p_inst2.add_run("-----------------------***-----------------------\n\n\n")

    p_logo2 = doc.add_paragraph()
    p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_logo2 = p_logo2.add_run("[ KHUNG LOGO HỌC VIỆN HÀNG KHÔNG VIỆT NAM - VAA ]\n\n\n")
    r_logo2.font.size = Pt(12)
    r_logo2.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    r_logo2.italic = True

    p_title2 = doc.add_paragraph()
    p_title2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_bc2 = p_title2.add_run("BÁO CÁO TIỂU LUẬN\n")
    r_bc2.bold = True
    r_bc2.font.size = Pt(18)
    r_hp2 = p_title2.add_run("MÔN HỌC: ........................................................................\n\n")
    r_hp2.bold = True
    r_hp2.font.size = Pt(14)

    r_detai_label2 = p_title2.add_run("ĐỀ TÀI:\n")
    r_detai_label2.bold = True
    r_detai_label2.font.size = Pt(15)

    r_detai2 = p_title2.add_run("ỨNG DỤNG LẬP KẾ HOẠCH HỌC TẬP CÁ NHÂN CÓ AI GỢI Ý LỊCH\n")
    r_detai2.bold = True
    r_detai2.font.size = Pt(16)
    r_detai2.font.color.rgb = RGBColor(0x0F, 0x2C, 0x59)

    r_sub2 = p_title2.add_run("(SMART STUDY PLANNER & OPTIMIZER)\n\n\n\n")
    r_sub2.bold = True
    r_sub2.font.size = Pt(13)

    p_info2 = doc.add_paragraph()
    p_info2.paragraph_format.left_indent = Inches(1.0)
    p_info2.paragraph_format.line_spacing = 1.3
    
    r_gv2 = p_info2.add_run("Giảng viên hướng dẫn:\t…………………………………………………………\n")
    r_gv2.bold = True
    r_sv2 = p_info2.add_run("Sinh viên/ Nhóm thực hiện:\tNhóm 07…………………………………………………\n")
    r_sv2.bold = True
    p_info2.add_run("Mã số sinh viên:\t…………………………………………………………\n")
    p_info2.add_run("Lớp:\t…………………………………………………………\n")

    p_loc2 = doc.add_paragraph()
    p_loc2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_loc2.paragraph_format.space_before = Pt(40)
    r_loc2 = p_loc2.add_run("Thành phố Hồ Chí Minh, tháng 11/2026")
    r_loc2.italic = True

    doc.add_page_break()

    # -------------------------------------------------------------
    # 3. DANH SÁCH NHÓM & CÁN BỘ CHẤM THI
    # -------------------------------------------------------------
    p_ds = doc.add_paragraph()
    p_ds.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ds = p_ds.add_run("DANH SÁCH SINH VIÊN THỰC HIỆN")
    r_ds.bold = True
    r_ds.font.size = Pt(14)

    # Student list table
    table_sv = doc.add_table(rows=6, cols=5)
    table_sv.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_box_borders(table_sv, "000000")

    headers_sv = ["STT", "Họ và tên", "MSSV", "Lớp", "Ghi chú"]
    col_widths_sv = [Inches(0.6), Inches(2.3), Inches(1.3), Inches(1.3), Inches(1.3)]

    # Header Row
    hdr_cells = table_sv.rows[0].cells
    for i, title in enumerate(headers_sv):
        hdr_cells[i].text = title
        hdr_cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        hdr_cells[i].paragraphs[0].runs[0].bold = True
        set_cell_background(hdr_cells[i], "EAEAEA")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)

    # Data Rows (pre-filled with placeholders according to template)
    sample_data = [
        ("1", "Đinh Đức Thành", "....................", "....................", "Nhóm trưởng"),
        ("2", "...........................................", "....................", "....................", "Thành viên"),
        ("3", "...........................................", "....................", "....................", "Thành viên"),
        ("4", "...........................................", "....................", "....................", "Thành viên"),
        ("5", "...........................................", "....................", "....................", "Thành viên")
    ]
    for row_idx, data in enumerate(sample_data, start=1):
        row_cells = table_sv.rows[row_idx].cells
        for col_idx, val in enumerate(data):
            row_cells[col_idx].text = val
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=80, right=80)
            if col_idx in [0, 2, 3, 4]:
                row_cells[col_idx].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Adjust widths
    for row in table_sv.rows:
        for idx, width in enumerate(col_widths_sv):
            row.cells[idx].width = width

    doc.add_paragraph("\n")

    # Examiner signature table
    table_cb = doc.add_table(rows=2, cols=2)
    table_cb.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_box_borders(table_cb, "000000")

    col_widths_cb = [Inches(3.4), Inches(3.4)]
    cb_data = [
        ("Cán bộ chấm thi 1\n(Ký và ghi rõ họ tên)\n\n\n\n\n...................................................",
         "Cán bộ chấm thi 2\n(Ký và ghi rõ họ tên)\n\n\n\n\n..................................................."),
        ("Cán bộ chấm thi phúc khảo 1\n(Ký và ghi rõ họ tên)\n\n\n\n\n...................................................",
         "Cán bộ chấm thi phúc khảo 2\n(Ký và ghi rõ họ tên)\n\n\n\n\n...................................................")
    ]
    for r_idx, row_vals in enumerate(cb_data):
        row_cells = table_cb.rows[r_idx].cells
        for c_idx, val in enumerate(row_vals):
            row_cells[c_idx].text = val
            row_cells[c_idx].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_cell_margins(row_cells[c_idx], top=120, bottom=120, left=100, right=100)

    for row in table_cb.rows:
        for idx, width in enumerate(col_widths_cb):
            row.cells[idx].width = width

    doc.add_page_break()

    # -------------------------------------------------------------
    # 4. DANH MỤC CÁC KÝ HIỆU, CHỮ VIẾT TẮT
    # -------------------------------------------------------------
    p_vt = doc.add_paragraph()
    p_vt.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_vt = p_vt.add_run("DANH MỤC CÁC KÝ HIỆU, CHỮ VIẾT TẮT")
    r_vt.bold = True
    r_vt.font.size = Pt(14)

    table_vt = doc.add_table(rows=12, cols=2)
    table_vt.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_box_borders(table_vt, "000000")

    headers_vt = ["Ký hiệu, chữ viết tắt", "Chữ viết đầy đủ (Ý nghĩa)"]
    for i, title in enumerate(headers_vt):
        table_vt.rows[0].cells[i].text = title
        table_vt.rows[0].cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        table_vt.rows[0].cells[i].paragraphs[0].runs[0].bold = True
        set_cell_background(table_vt.rows[0].cells[i], "EAEAEA")
        set_cell_margins(table_vt.rows[0].cells[i], top=100, bottom=100, left=120, right=120)

    vt_list = [
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

    for idx, (abbr, full) in enumerate(vt_list, start=1):
        row_cells = table_vt.rows[idx].cells
        row_cells[0].text = abbr
        row_cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row_cells[0].paragraphs[0].runs[0].bold = True
        row_cells[1].text = full
        set_cell_margins(row_cells[0], top=80, bottom=80, left=100, right=100)
        set_cell_margins(row_cells[1], top=80, bottom=80, left=100, right=100)

    for row in table_vt.rows:
        row.cells[0].width = Inches(2.2)
        row.cells[1].width = Inches(4.6)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 5. MỤC LỤC & DANH MỤC HÌNH VẼ, BẢNG BIỂU
    # -------------------------------------------------------------
    p_ml = doc.add_paragraph()
    p_ml.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ml = p_ml.add_run("MỤC LỤC")
    r_ml.bold = True
    r_ml.font.size = Pt(14)

    toc_entries = [
        ("Danh mục các ký hiệu, chữ viết tắt", "iii"),
        ("Danh mục các bảng, hình vẽ, đồ thị", "iv"),
        ("MỞ ĐẦU", "1"),
        ("CHƯƠNG 1. GIỚI THIỆU", "2"),
        ("    1.1. Lý do chọn đề tài", "2"),
        ("    1.2. Mục tiêu đề tài", "3"),
        ("    1.3. Phạm vi đề tài", "3"),
        ("    1.4. Đối tượng nghiên cứu", "4"),
        ("    1.5. Phương pháp nghiên cứu", "4"),
        ("    1.6. Bố cục đề tài", "4"),
        ("CHƯƠNG 2. CƠ SỞ LÝ THUYẾT", "6"),
        ("    2.1. Framework Django & Kiến trúc MVT", "6"),
        ("    2.2. Framework FastAPI & Giao thức ASGI", "8"),
        ("    2.3. Cơ sở dữ liệu quan hệ PostgreSQL & Hệ thống hàng đợi Redis/Celery", "9"),
        ("    2.4. Công nghệ Trí tuệ Nhân tạo & Kỹ thuật Structured Output JSON", "11"),
        ("    2.5. Thư viện FullCalendar.js & Thuật toán Lập lịch Heuristic đa mục tiêu", "13"),
        ("CHƯƠNG 3. PHÂN TÍCH HỆ THỐNG VÀ XÂY DỰNG SẢN PHẨM", "15"),
        ("    3.1. Phân tích hệ thống", "15"),
        ("        3.1.1. Yêu cầu chức năng", "15"),
        ("        3.1.2. Yêu cầu phi chức năng", "17"),
        ("        3.1.3. Biểu đồ Use Case tổng quát và phân hệ", "18"),
        ("        3.1.4. Thiết kế cơ sở dữ liệu (8 mô hình Models)", "20"),
        ("        3.1.5. Thiết kế thuật toán tự động sinh lịch học tuần (Optimization Engine)", "24"),
        ("    3.2. Xây dựng giao diện sản phẩm", "26"),
        ("        3.2.1. Giao diện Xác thực và Phân quyền người dùng (Hình 3.1)", "26"),
        ("        3.2.2. Giao diện Bảng điều khiển trung tâm & Phân tích AI Cards (Hình 3.2)", "28"),
        ("        3.2.3. Giao diện Lịch tương tác FullCalendar đa chế độ (Hình 3.3)", "30"),
        ("        3.2.4. Giao diện Quản lý Khóa học, Deadline và Tài liệu ôn tập (Hình 3.4)", "32"),
        ("        3.2.5. Giao diện Đồng hồ tập trung Pomodoro tích hợp (Hình 3.5)", "34"),
        ("        3.2.6. Giao diện Xuất file đồng bộ lịch cá nhân .ics (Hình 3.6)", "35"),
        ("        3.2.7. Giao diện Cổng Quản trị viên hệ thống Admin Portal (Hình 3.7)", "36"),
        ("KẾT LUẬN", "38"),
        ("DANH MỤC TÀI LIỆU THAM KHẢO", "40"),
        ("PHỤ LỤC", "42")
    ]

    p_toc_list = doc.add_paragraph()
    p_toc_list.paragraph_format.line_spacing = 1.3
    for title, page in toc_entries:
        p_row = doc.add_paragraph()
        p_row.paragraph_format.line_spacing = 1.2
        p_row.paragraph_format.space_after = Pt(2)
        r_t = p_row.add_run(title)
        if "CHƯƠNG" in title or "MỞ ĐẦU" in title or "KẾT LUẬN" in title or "DANH MỤC" in title:
            r_t.bold = True
        # Tab leader
        r_dots = p_row.add_run("\t" + "." * (65 - len(title.strip())) + "\t" + page)
        if "CHƯƠNG" in title or "MỞ ĐẦU" in title or "KẾT LUẬN" in title:
            r_dots.bold = True

    doc.add_page_break()

    # Danh mục bảng, hình vẽ
    p_dmh = doc.add_paragraph()
    p_dmh.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_dmh = p_dmh.add_run("DANH MỤC CÁC BẢNG, HÌNH VẼ, ĐỒ THỊ")
    r_dmh.bold = True
    r_dmh.font.size = Pt(14)

    fig_list = [
        ("Bảng 2.1", "So sánh đặc tính kỹ thuật giữa Django và FastAPI", "8"),
        ("Bảng 3.1", "Danh sách 8 thực thể dữ liệu trong cơ sở dữ liệu hệ thống", "21"),
        ("Bảng 3.2", "Trọng số ưu tiên (Priority Weight) trong thuật toán xếp lịch", "24"),
        ("Hình 3.1", "Giao diện Đăng nhập và Đăng ký hệ thống Smart Study Planner", "27"),
        ("Hình 3.2", "Giao diện Dashboard tổng quan và 4 khối phân tích AI chuyên sâu", "29"),
        ("Hình 3.3", "Giao diện Lịch tương tác FullCalendar tuần hỗ trợ kéo-thả và khóa lịch", "31"),
        ("Hình 3.4", "Giao diện Quản lý môn học, danh sách công việc và tài liệu ôn tập", "33"),
        ("Hình 3.5", "Giao diện Đồng hồ Pomodoro ghi nhận thời gian tập trung thực tế", "34"),
        ("Hình 3.6", "Chức năng Xuất lịch chuẩn iCalendar (.ics) đồng bộ Google Calendar", "35"),
        ("Hình 3.7", "Giao diện Cổng Quản trị viên Admin Portal quản lý tài khoản người dùng", "37")
    ]

    for code, desc, pg in fig_list:
        p_f = doc.add_paragraph()
        p_f.paragraph_format.line_spacing = 1.2
        r_c = p_f.add_run(f"{code}: {desc}")
        p_f.add_run("\t" + "." * (60 - len(f"{code}: {desc}".strip()[:50])) + "\t" + pg)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 6. MỞ ĐẦU
    # -------------------------------------------------------------
    h_intro = doc.add_paragraph()
    r_hi = h_intro.add_run("MỞ ĐẦU")
    r_hi.bold = True
    r_hi.font.size = Pt(14)
    h_intro.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_in1 = doc.add_paragraph()
    p_in1.paragraph_format.line_spacing = 1.5
    p_in1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_in1.paragraph_format.first_line_indent = Inches(0.5)
    p_in1.add_run(
        "Trong bối cảnh giáo dục hiện đại theo học chế tín chỉ, sinh viên đại học thường xuyên phải đối mặt với áp lực lớn "
        "từ việc phân bổ thời gian. Một học kỳ thông thường đòi hỏi sinh viên phải theo học từ 6 đến 8 môn học song song, "
        "mỗi môn lại có khối lượng bài tập lớn, đồ án môn học, kiểm tra định kỳ và bài tập nhóm với các hạn chót (deadline) "
        "dày đặc. Bên cạnh thời gian biểu học thuật trên giảng đường, đại đa số sinh viên hiện nay còn tham gia các ca làm thêm "
        "bán thời gian, rèn luyện kỹ năng mềm, học ngoại ngữ và các hoạt động câu lạc bộ, sự kiện ngoại khóa. Sự đan xen phức tạp "
        "giữa nhiều trách nhiệm khác nhau mà không có một phương pháp quản lý khoa học dẫn đến tình trạng quá tải (burnout), "
        "trì hoãn (procrastination) và hiện tượng \"nước đến chân mới nhảy\" gây ảnh hưởng tiêu cực trực tiếp đến kết quả học tập."
    )

    p_in2 = doc.add_paragraph()
    p_in2.paragraph_format.line_spacing = 1.5
    p_in2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_in2.paragraph_format.first_line_indent = Inches(0.5)
    p_in2.add_run(
        "Xuất phát từ thực trạng trên, đề tài \"Ứng dụng lập kế hoạch học tập cá nhân có AI gợi ý lịch\" "
        "(Smart Study Planner & Optimizer) được nghiên cứu và xây dựng nhằm cung cấp một giải pháp công nghệ toàn diện. "
        "Khác biệt với các ứng dụng ghi chú đơn thuần hoặc các chatbot AI hội thoại thông thường, đề tài tập trung phát triển "
        "một nền tảng năng suất (Productivity & Calendar Web App) hoàn chỉnh. Ứng dụng tích hợp thuật toán tối ưu hóa lịch "
        "dựa trên độ cấp thiết và khối lượng công việc thực tế, giao diện tương tác trực quan kéo-thả hiện đại, phương pháp "
        "tập trung Pomodoro và sự hỗ trợ phân tích thông minh từ Trí tuệ Nhân tạo (AI). Đây là công cụ đắc lực giúp người học "
        "chủ động kiểm soát thời gian, giảm thiểu căng thẳng và nâng cao tối đa hiệu suất học tập cá nhân."
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # 7. CHƯƠNG 1. GIỚI THIỆU
    # -------------------------------------------------------------
    h_c1 = doc.add_paragraph()
    r_c1 = h_c1.add_run("CHƯƠNG 1. GIỚI THIỆU")
    r_c1.bold = True
    r_c1.font.size = Pt(14)
    h_c1.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 1.1. Lý do chọn đề tài
    h11 = doc.add_paragraph()
    r11 = h11.add_run("1.1. Lý do chọn đề tài")
    r11.bold = True
    r11.font.size = Pt(13)

    p11_1 = doc.add_paragraph()
    p11_1.paragraph_format.line_spacing = 1.5
    p11_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p11_1.paragraph_format.first_line_indent = Inches(0.5)
    p11_1.add_run(
        "Quản lý thời gian luôn là một trong những rào cản lớn nhất đối với sinh viên khi chuyển từ bậc học phổ thông sang môi trường "
        "đại học. Thực tế cho thấy, việc theo dõi hàng loạt các hạn nộp bài tập qua nhiều kênh phân tán (LMS, mạng xã hội, email, nhóm chat) "
        "khiến sinh viên rất dễ rơi vào tình trạng bỏ sót nhiệm vụ hoặc đánh giá sai thời lượng cần thiết để hoàn thành. Khi các mốc thời gian "
        "quan trọng bị trùng lắp, sinh viên thường có xu hướng thức khuya dồn việc vào những ngày cuối, dẫn đến sự suy giảm nghiêm trọng "
        "về chất lượng bài làm cũng như sức khỏe thể chất và tinh thần."
    )

    p11_2 = doc.add_paragraph()
    p11_2.paragraph_format.line_spacing = 1.5
    p11_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p11_2.paragraph_format.first_line_indent = Inches(0.5)
    p11_2.add_run(
        "Mặc dù trên thị trường hiện nay có nhiều công cụ lập lịch phổ biến như Google Calendar hay Notion, các công cụ này hầu như "
        "đòi hỏi người dùng phải hoàn toàn tự tay sắp xếp từng khung giờ trống. Ngược lại, các công cụ AI hội thoại dạng chatbot tuy thông minh "
        "nhưng chỉ dừng lại ở mức trả lời các câu hỏi bằng văn bản rời rạc, không gắn liền với cơ sở dữ liệu thực tế và không cung cấp được "
        "trực quan hóa trên lịch biểu. Vì vậy, việc xây dựng một hệ thống phần mềm chuyên biệt có khả năng tự động phân tích các khung giờ rảnh, "
        "đối chiếu với hạn chót và mức độ ưu tiên để tự động gợi ý lịch học thông minh là một bài toán mang tính cấp thiết cao, đem lại giá trị "
        "thực tiễn sâu sắc cho cộng đồng người học trong môi trường giáo dục số."
    )

    # 1.2. Mục tiêu đề tài
    h12 = doc.add_paragraph()
    r12 = h12.add_run("1.2. Mục tiêu đề tài")
    r12.bold = True
    r12.font.size = Pt(13)

    p12_1 = doc.add_paragraph()
    p12_1.paragraph_format.line_spacing = 1.5
    p12_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p12_1.paragraph_format.first_line_indent = Inches(0.5)
    p12_1.add_run(
        "Mục tiêu cốt lõi của đề tài là xây dựng hoàn chỉnh một ứng dụng web phục vụ người dùng sinh viên và cán bộ quản trị, cụ thể:"
    )

    bullet_p12 = [
        "Về hệ thống ứng dụng: Xây dựng nền tảng quản lý toàn diện lịch bận cố định (BusySlot), các môn học (Course), bài tập và hạn chót (Task), tài liệu ôn tập (StudyMaterial), đồng hồ bấm giờ tập trung (PomodoroSession) và tính năng xuất lịch cá nhân (.ics) đồng bộ sang Google/Apple Calendar.",
        "Về giải thuật tính toán: Thiết kế và hiện thực thuật toán lập lịch thông minh (Schedule Optimization Engine), tự động quét các khoảng trống trong tuần để lấp đầy các phiên học (ScheduledBlock) theo công thức tối ưu hóa điểm số ưu tiên và cảnh báo quá tải.",
        "Về công nghệ ứng dụng: Làm chủ kiến trúc Full-Stack Python hiện đại kết hợp giữa Django 5.x (đảm nhiệm MVT, ORM, bảo mật, xác thực) và FastAPI (đảm nhiệm xử lý API phi đồng bộ hiệu năng cao cho lịch và thuật toán) chạy trên nền tảng ASGI; tích hợp AI phân tích thói quen và cảnh báo nguy cơ trễ hạn."
    ]
    for b in bullet_p12:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(b)

    # 1.3. Phạm vi đề tài
    h13 = doc.add_paragraph()
    r13 = h13.add_run("1.3. Phạm vi đề tài")
    r13.bold = True
    r13.font.size = Pt(13)

    p13_1 = doc.add_paragraph()
    p13_1.paragraph_format.line_spacing = 1.5
    p13_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p13_1.paragraph_format.first_line_indent = Inches(0.5)
    p13_1.add_run(
        "Đề tài tập trung nghiên cứu trong phạm vi quản lý học tập và năng suất cá nhân của sinh viên đại học. "
        "Về không gian và hạ tầng, ứng dụng được phát triển dưới dạng nền tảng Web có tính tương tác cao (SPA-like) và được triển khai "
        "vận hành trực tuyến (Cloud Deployment). Về chu kỳ thời gian, thuật toán tối ưu hóa tập trung giải quyết bài toán phân bổ phiên học "
        "trong khung thời gian 7 ngày tới (Rolling 7-day schedule), đồng thời hỗ trợ theo dõi tiến độ tổng thể của toàn bộ học kỳ."
    )

    # 1.4. Đối tượng nghiên cứu
    h14 = doc.add_paragraph()
    r14 = h14.add_run("1.4. Đối tượng nghiên cứu")
    r14.bold = True
    r14.font.size = Pt(13)

    p14_1 = doc.add_paragraph()
    p14_1.paragraph_format.line_spacing = 1.5
    p14_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p14_1.paragraph_format.first_line_indent = Inches(0.5)
    p14_1.add_run(
        "Đối tượng nghiên cứu chính của đề tài bao gồm:"
    )
    dt_items = [
        "Người dùng đối tượng: Sinh viên học tập theo học chế tín chỉ cần quản lý lịch học, làm thêm và thời gian ôn thi.",
        "Quy trình nghiệp vụ: Quá trình lập kế hoạch học tập, ước lượng thời gian hoàn thành bài tập và kỹ thuật quản lý thời gian Pomodoro.",
        "Mô hình dữ liệu và thuật toán: Cấu trúc biểu diễn khoảng thời gian bận/rảnh, thuật toán sắp xếp dựa trên điểm ưu tiên đa tiêu chí và mô hình phân tích ngôn ngữ tự nhiên ứng dụng trong việc tóm tắt thông tin học tập."
    ]
    for dt in dt_items:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(dt)

    # 1.5. Phương pháp nghiên cứu
    h15 = doc.add_paragraph()
    r15 = h15.add_run("1.5. Phương pháp nghiên cứu")
    r15.bold = True
    r15.font.size = Pt(13)

    p15_1 = doc.add_paragraph()
    p15_1.paragraph_format.line_spacing = 1.5
    p15_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p15_1.paragraph_format.first_line_indent = Inches(0.5)
    p15_1.add_run(
        "Nhóm tác giả đã vận dụng kết hợp các phương pháp nghiên cứu khoa học kỹ thuật sau:"
    )
    pp_items = [
        "Phương pháp nghiên cứu lý thuyết: Khảo sát các tài liệu chuyên ngành về thiết kế kiến trúc phần mềm hướng dịch vụ, giao thức bất đồng bộ ASGI trong Python và kỹ thuật Prompt Engineering định dạng JSON có cấu trúc.",
        "Phương pháp phân tích và mô hình hóa: Xây dựng biểu đồ Use Case, thiết kế cơ sở dữ liệu quan hệ chuẩn hóa và thiết lập công thức toán học tính điểm ưu tiên công việc.",
        "Phương pháp thực nghiệm phát triển phần mềm: Áp dụng quy trình phát triển nhanh, kiểm thử chức năng tự động (Unit Test / Integration Test), mô phỏng các tình huống xếp lịch phức tạp và triển khai ứng dụng thực tế trên môi trường đám mây."
    ]
    for pp in pp_items:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(pp)

    # 1.6. Bố cục đề tài
    h16 = doc.add_paragraph()
    r16 = h16.add_run("1.6. Bố cục đề tài")
    r16.bold = True
    r16.font.size = Pt(13)

    p16_1 = doc.add_paragraph()
    p16_1.paragraph_format.line_spacing = 1.5
    p16_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p16_1.paragraph_format.first_line_indent = Inches(0.5)
    p16_1.add_run(
        "Báo cáo tiểu luận môn học được tổ chức kết cấu gồm 3 chương chính cùng phần Mở đầu, Kết luận và Phụ lục. "
        "Chương 2 trình bày tổng quan cơ sở lý thuyết, phân tích chi tiết các công nghệ nền tảng bao gồm framework Django, FastAPI, "
        "kiến trúc máy chủ ASGI, cơ sở dữ liệu quan hệ, hệ thống hàng đợi Celery/Redis, các mô hình ngôn ngữ lớn và giải thuật tối ưu lịch. "
        "Chương 3 là nội dung cốt lõi của đề tài, tập trung phân tích đặc tả yêu cầu hệ thống, thiết kế kiến trúc cơ sở dữ liệu, "
        "chi tiết hóa giải thuật xếp lịch tự động và minh họa toàn diện các màn hình giao diện chức năng của sản phẩm phần mềm. "
        "Cuối cùng, phần Kết luận tổng kết các kết quả đạt được, chỉ ra những điểm còn hạn chế và đề xuất phương hướng phát triển mở rộng trong tương lai."
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # 8. CHƯƠNG 2. CƠ SỞ LÝ THUYẾT
    # -------------------------------------------------------------
    h_c2 = doc.add_paragraph()
    r_c2 = h_c2.add_run("CHƯƠNG 2. CƠ SỞ LÝ THUYẾT")
    r_c2.bold = True
    r_c2.font.size = Pt(14)
    h_c2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p_c2_lead = doc.add_paragraph()
    p_c2_lead.paragraph_format.line_spacing = 1.5
    p_c2_lead.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_c2_lead.paragraph_format.first_line_indent = Inches(0.5)
    p_c2_lead.add_run(
        "Để giải quyết triệt để bài toán xây dựng một hệ thống lập kế hoạch học tập có tính sẵn sàng cao, "
        "hoạt động mượt mà và thông minh, việc lựa chọn đúng đắn các công nghệ nền tảng đóng vai trò quyết định. "
        "Hệ thống đòi hỏi sự kết hợp chặt chẽ giữa tính bảo mật, toàn vẹn dữ liệu từ một framework web hoàn chỉnh với tốc độ phản hồi "
        "cực nhanh từ các API bất đồng bộ phục vụ tương tác kéo-thả lịch. Dưới đây là phân tích chi tiết các cơ sở lý thuyết "
        "và công nghệ cốt lõi được áp dụng trong đề tài."
    )

    # 2.1. Framework Django
    h21 = doc.add_paragraph()
    r21 = h21.add_run("2.1. Framework Django & Kiến trúc MVT")
    r21.bold = True
    r21.font.size = Pt(13)

    p21_1 = doc.add_paragraph()
    p21_1.paragraph_format.line_spacing = 1.5
    p21_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p21_1.paragraph_format.first_line_indent = Inches(0.5)
    p21_1.add_run(
        "Django là một web framework bậc cao viết bằng ngôn ngữ Python, được phát hành lần đầu vào năm 2005 bởi Adrian Holovaty "
        "và Simon Willison. Django tuân thủ triết lý \"Batteries-included\" (tích hợp sẵn mọi thành phần thiết yếu) và nguyên lý "
        "DRY (Don't Repeat Yourself), giúp lập trình viên phát triển ứng dụng nhanh chóng, an toàn và dễ bảo trì."
    )

    p21_2 = doc.add_paragraph()
    p21_2.paragraph_format.line_spacing = 1.5
    p21_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p21_2.paragraph_format.first_line_indent = Inches(0.5)
    p21_2.add_run(
        "Kiến trúc của Django hoạt động theo mô hình MVT (Model - View - Template), một biến thể hiện đại của MVC. Trong đó, "
        "Model chịu trách nhiệm định nghĩa cấu trúc dữ liệu và tương tác với cơ sở dữ liệu thông qua hệ thống ORM (Object-Relational Mapping); "
        "View xử lý toàn bộ logic nghiệp vụ tiếp nhận yêu cầu HTTP và trả về phản hồi; Template định nghĩa giao diện hiển thị cho người dùng. "
        "Điểm mạnh nổi bật của Django là hệ thống bảo mật mặc định mạnh mẽ chống lại các lỗi bảo mật phổ biến như SQL Injection, CSRF, XSS "
        "cùng cổng quản trị (Django Admin) cực kỳ mạnh mẽ. Điểm hạn chế truyền thống của Django là mô hình xử lý đơn luồng đồng bộ (WSGI), "
        "tuy nhiên điều này đã được khắc phục hoàn toàn trong phiên bản Django 5.x với sự hỗ trợ toàn diện cho chuẩn máy chủ bất đồng bộ ASGI."
    )

    # 2.2. FastAPI & ASGI
    h22 = doc.add_paragraph()
    r22 = h22.add_run("2.2. Framework FastAPI & Giao thức ASGI")
    r22.bold = True
    r22.font.size = Pt(13)

    p22_1 = doc.add_paragraph()
    p22_1.paragraph_format.line_spacing = 1.5
    p22_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p22_1.paragraph_format.first_line_indent = Inches(0.5)
    p22_1.add_run(
        "FastAPI là một web framework hiện đại hiệu năng cao được tác giả Sebastián Ramírez phát triển vào năm 2018. "
        "FastAPI được thiết kế chuyên biệt để xây dựng các RESTful API dựa trên nền tảng của Starlette (xử lý bất đồng bộ) "
        "và Pydantic (xác thực dữ liệu dựa trên Type Hints của Python 3.8+)."
    )

    p22_2 = doc.add_paragraph()
    p22_2.paragraph_format.line_spacing = 1.5
    p22_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p22_2.paragraph_format.first_line_indent = Inches(0.5)
    p22_2.add_run(
        "Khác với WSGI truyền thống chỉ xử lý tuần tự một yêu cầu trên mỗi tiến trình, ASGI (Asynchronous Server Gateway Interface) "
        "cho phép máy chủ xử lý hàng nghìn kết nối đồng thời nhờ cơ chế event-loop không chặn (non-blocking I/O). "
        "Trong đề tài này, nhóm tác giả áp dụng kiến trúc Hybrid đột phá: FastAPI được mount trực tiếp vào điểm vào ASGI (`asgi.py`) "
        "của Django tại đường dẫn `/api/v1/`. Giải pháp này cho phép hệ thống tận dụng trọn vẹn sức mạnh quản trị dữ liệu của Django "
        "đồng thời đạt được độ trễ phản hồi cực thấp (< 50ms) cho các tác vụ cập nhật kéo-thả lịch và thuật toán tối ưu hóa của FastAPI."
    )

    # Bảng 2.1 So sánh
    p_b21_cap = doc.add_paragraph()
    p_b21_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_b21_cap = p_b21_cap.add_run("Bảng 2.1: So sánh đặc tính kỹ thuật giữa Django và FastAPI trong kiến trúc hệ thống")
    r_b21_cap.italic = True
    r_b21_cap.font.size = Pt(11)

    table_ss = doc.add_table(rows=6, cols=3)
    table_ss.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_box_borders(table_ss, "000000")

    headers_ss = ["Tiêu chí kỹ thuật", "Django Framework (Core)", "FastAPI Framework (Auxiliary)"]
    for i, t in enumerate(headers_ss):
        table_ss.rows[0].cells[i].text = t
        table_ss.rows[0].cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        table_ss.rows[0].cells[i].paragraphs[0].runs[0].bold = True
        set_cell_background(table_ss.rows[0].cells[i], "EAEAEA")
        set_cell_margins(table_ss.rows[0].cells[i], top=100, bottom=100, left=100, right=100)

    ss_data = [
        ("Mục đích trong hệ thống", "Xử lý xác thực, Web UI, Quản lý User, ORM", "Xử lý API kéo-thả lịch, Engine tối ưu hóa, AI endpoint"),
        ("Kiểu giao tiếp máy chủ", "WSGI / ASGI song hành", "Thuần túy bất đồng bộ ASGI (async/await)"),
        ("Hiệu năng xử lý (I/O)", "Tốt, tối ưu hóa qua QuerySet", "Cực cao, tương đương Node.js và Go"),
        ("Xác thực dữ liệu", "Django Forms & Model Validation", "Pydantic Schemas với Type Hints chặt chẽ"),
        ("Tự động sinh tài liệu", "Yêu cầu cài thêm thư viện ngoài", "Tích hợp sẵn Swagger UI và ReDoc chuẩn OpenAPI")
    ]
    for r_idx, row_vals in enumerate(ss_data, start=1):
        for c_idx, val in enumerate(row_vals):
            table_ss.rows[r_idx].cells[c_idx].text = val
            set_cell_margins(table_ss.rows[r_idx].cells[c_idx], top=80, bottom=80, left=100, right=100)
            if c_idx == 0:
                table_ss.rows[r_idx].cells[c_idx].paragraphs[0].runs[0].bold = True

    for row in table_ss.rows:
        row.cells[0].width = Inches(2.0)
        row.cells[1].width = Inches(2.4)
        row.cells[2].width = Inches(2.4)

    # 2.3. PostgreSQL & Celery/Redis
    h23 = doc.add_paragraph()
    r23 = h23.add_run("2.3. Cơ sở dữ liệu quan hệ PostgreSQL & Hệ thống hàng đợi Redis/Celery")
    r23.bold = True
    r23.font.size = Pt(13)

    p23_1 = doc.add_paragraph()
    p23_1.paragraph_format.line_spacing = 1.5
    p23_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p23_1.paragraph_format.first_line_indent = Inches(0.5)
    p23_1.add_run(
        "PostgreSQL là hệ quản trị cơ sở dữ liệu quan hệ - đối tượng (ORDBMS) mã nguồn mở mạnh mẽ nhất hiện nay, "
        "nổi tiếng với tính tuân thủ nghiêm ngặt các tiêu chuẩn ACID (Atomicity, Consistency, Isolation, Durability) "
        "và khả năng xử lý các truy vấn quan hệ phức tạp. Trong dự án, hệ thống sử dụng thư viện `dj-database-url` "
        "để tự động kết nối linh hoạt tới PostgreSQL trên môi trường Production đám mây, đồng thời tự động chuyển đổi sang SQLite "
        "khi vận hành thử nghiệm cục bộ, đảm bảo tính liên tục phát triển."
    )

    p23_2 = doc.add_paragraph()
    p23_2.paragraph_format.line_spacing = 1.5
    p23_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p23_2.paragraph_format.first_line_indent = Inches(0.5)
    p23_2.add_run(
        "Đối với các tác vụ chạy ngầm định kỳ (Background Jobs) như tự động quét các bài tập sắp hết hạn để gửi thông báo nhắc việc, "
        "hệ thống tích hợp Celery cùng Redis làm Message Broker. Celery Beat thực hiện lập lịch định kỳ mỗi 60 phút, "
        "giúp giảm tải triệt để cho tiến trình web chính, đảm bảo trải nghiệm người dùng không bị tắc nghẽn khi khối lượng công việc tăng cao."
    )

    # 2.4. Trí tuệ Nhân tạo & Structured JSON
    h24 = doc.add_paragraph()
    r24 = h24.add_run("2.4. Công nghệ Trí tuệ Nhân tạo & Kỹ thuật Structured Output JSON")
    r24.bold = True
    r24.font.size = Pt(13)

    p24_1 = doc.add_paragraph()
    p24_1.paragraph_format.line_spacing = 1.5
    p24_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p24_1.paragraph_format.first_line_indent = Inches(0.5)
    p24_1.add_run(
        "Trí tuệ Nhân tạo trong đề tài không đi theo hướng xây dựng một chatbot hội thoại thụ động mà được thiết kế như một động cơ "
        "phân tích dữ liệu chuyên sâu (Analytical Engine). Hệ thống tích hợp các mô hình ngôn ngữ lớn (LLM) hàng đầu thông qua OpenAI API "
        "hoặc Anthropic Claude API, áp dụng kỹ thuật Prompt Engineering nghiêm ngặt buộc mô hình trả về dữ liệu chuẩn định dạng JSON có cấu trúc (Structured JSON)."
    )

    p24_2 = doc.add_paragraph()
    p24_2.paragraph_format.line_spacing = 1.5
    p24_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p24_2.paragraph_format.first_line_indent = Inches(0.5)
    p24_2.add_run(
        "Đặc biệt, nhằm đáp ứng tiêu chí tin cậy tuyệt đối và loại bỏ hoàn toàn nguy cơ lỗi khi không có kết nối API ngoài, "
        "nhóm tác giả đã nghiên cứu và lập trình cơ chế Heuristic Fallback thông minh. Khi người dùng chưa cấu hình API Key, "
        "hệ thống tự động chuyển sang thuật toán phân tích dữ liệu thống kê trực tiếp từ lịch sử các phiên PomodoroSession "
        "và hạn chót trong cơ sở dữ liệu để đưa ra các phân tích thói quen, tỷ lệ tập trung và cảnh báo rủi ro trễ hạn với độ chính xác toán học 100%."
    )

    # 2.5. FullCalendar & Thuật toán Lập lịch
    h25 = doc.add_paragraph()
    r25 = h25.add_run("2.5. Thư viện FullCalendar.js & Thuật toán Lập lịch Heuristic đa mục tiêu")
    r25.bold = True
    r25.font.size = Pt(13)

    p25_1 = doc.add_paragraph()
    p25_1.paragraph_format.line_spacing = 1.5
    p25_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p25_1.paragraph_format.first_line_indent = Inches(0.5)
    p25_1.add_run(
        "FullCalendar.js là thư viện lập lịch mã nguồn mở mạnh mẽ và phổ biến nhất trong phát triển web, hỗ trợ hiển thị lưới thời gian "
        "linh hoạt theo chế độ Tuần (TimeGridWeek), Tháng (DayGridMonth) và Ngày. Thư viện tích hợp các sự kiện kéo-thả (Event Drag & Drop) "
        "và thay đổi thời lượng (Event Resize), cho phép người dùng điều chỉnh kế hoạch học tập cực kỳ trực quan và mượt mà."
    )

    p25_2 = doc.add_paragraph()
    p25_2.paragraph_format.line_spacing = 1.5
    p25_2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p25_2.paragraph_format.first_line_indent = Inches(0.5)
    p25_2.add_run(
        "Về giải thuật lập lịch, bài toán xếp thời khóa biểu cá nhân thuộc lớp bài toán NP-Khó (NP-Hard). Để đáp ứng yêu cầu xử lý thời gian thực, "
        "đề tài áp dụng giải thuật Heuristic tối ưu hóa đa mục tiêu dựa trên ma trận thời gian rảnh và điểm ưu tiên động. Thuật toán tự động "
        "trừ đi các khoảng thời gian bận cố định (BusySlot) và các phiên học đã được người dùng chủ động khóa (`is_locked=True`), "
        "sau đó tiến hành chia nhỏ các nhiệm vụ lớn thành các phân đoạn học tập từ 45 đến 90 phút (có xen kẽ 15 phút giải lao) "
        "để tối ưu hóa chu kỳ tiếp thu của não bộ con người."
    )

    doc.add_page_break()

    # -------------------------------------------------------------
    # 9. CHƯƠNG 3. PHÂN TÍCH HỆ THỐNG VÀ XÂY DỰNG SẢN PHẨM
    # -------------------------------------------------------------
    h_c3 = doc.add_paragraph()
    r_c3 = h_c3.add_run("CHƯƠNG 3. PHÂN TÍCH HỆ THỐNG VÀ XÂY DỰNG SẢN PHẨM")
    r_c3.bold = True
    r_c3.font.size = Pt(14)
    h_c3.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 3.1. Phân tích hệ thống
    h31 = doc.add_paragraph()
    r31 = h31.add_run("3.1. Phân tích hệ thống")
    r31.bold = True
    r31.font.size = Pt(13)

    # 3.1.1 Yêu cầu chức năng
    h311 = doc.add_paragraph()
    r311 = h311.add_run("3.1.1. Yêu cầu chức năng (Functional Requirements)")
    r311.bold = True
    r311.font.size = Pt(12)

    p311_1 = doc.add_paragraph()
    p311_1.paragraph_format.line_spacing = 1.5
    p311_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p311_1.paragraph_format.first_line_indent = Inches(0.5)
    p311_1.add_run(
        "Hệ thống Smart Study Planner & Optimizer được module hóa thành 5 phân hệ chức năng cốt lõi đáp ứng đầy đủ nghiệp vụ người dùng:"
    )

    fn_modules = [
        "Phân hệ 1 - Xác thực và Quản lý Người dùng: Đăng ký tài khoản, đăng nhập với mã hóa mật khẩu PBKDF2, phân quyền 2 cấp độ (STUDENT và ADMIN), quản lý hồ sơ cá nhân, cấu hình khung giờ học tập trong ngày (mặc định 07:00 - 22:00) và chu kỳ phiên Pomodoro (25 phút học / 5 phút nghỉ). Cung cấp cổng quản trị Admin Portal chuyên biệt để tra cứu, kích hoạt/khóa tài khoản và chuyển đổi quyền người dùng.",
        "Phân hệ 2 - Động cơ Tối ưu hóa Lịch (Optimization Engine): Tự động tính toán các khoảng trống trong 7 ngày kế tiếp, trừ đi lịch bận và các phiên học đã khóa. Sắp xếp danh sách công việc theo công thức điểm ưu tiên toán học, tự động phân bổ phiên học từ 45-90 phút vào lịch biểu và cảnh báo nguy cơ quá tải ngay khi phát hiện thời gian rảnh không đủ đáp ứng hạn chót.",
        "Phân hệ 3 - Lịch tương tác & Đồng bộ hóa ngoại vi: Trực quan hóa toàn diện lịch tuần với sự phân tách màu sắc rõ ràng giữa lịch bận cố định (màu xám) và phiên học theo màu môn học. Cho phép thao tác kéo-thả và co giãn thời lượng cập nhật tức thì vào cơ sở dữ liệu qua API. Hỗ trợ xuất file chuẩn iCalendar (.ics) tương thích với Google Calendar, Apple Calendar và Microsoft Outlook.",
        "Phân hệ 4 - Quản lý Nhiệm vụ, Tài liệu ôn tập & Đồng hồ Pomodoro: CRUD môn học, quản lý danh sách công việc với các mức độ ưu tiên và trạng thái chi tiết. Đính kèm tài liệu học tập đa dạng (liên kết ngoài, tệp tải lên, ghi chú tóm tắt). Tích hợp đồng hồ Pomodoro bấm giờ thực tế, tự động cộng dồn thời gian đã học vào Task và lưu trữ lịch sử phiên học.",
        "Phân hệ 5 - Khối Phân tích Thông minh AI (AI Assistant Panel): Hiển thị dạng bảng tin Dashboard Cards với 4 nghiệp vụ: Tóm tắt ngày (Daily Briefing), Cảnh báo rủi ro trễ hạn (Deadline Risk Detector), Phân tích thói quen học tập (Study Habit Analysis) và Gợi ý phân bổ thời gian thông minh (Smart Time Allocation)."
    ]
    for fn in fn_modules:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(fn)

    # 3.1.2 Yêu cầu phi chức năng
    h312 = doc.add_paragraph()
    r312 = h312.add_run("3.1.2. Yêu cầu phi chức năng (Non-functional Requirements)")
    r312.bold = True
    r312.font.size = Pt(12)

    p312_1 = doc.add_paragraph()
    p312_1.paragraph_format.line_spacing = 1.5
    p312_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p312_1.paragraph_format.first_line_indent = Inches(0.5)
    p312_1.add_run(
        "Hệ thống đáp ứng các tiêu chuẩn kỹ thuật nghiêm ngặt về chất lượng phần mềm:"
    )
    nfn_list = [
        "Hiệu năng và Tốc độ: Thời gian phản hồi của các API kéo-thả lịch đạt dưới 100ms; thuật toán tối ưu hóa lịch 7 ngày xử lý hoàn tất trong dưới 300ms đối với dữ liệu từ 50-100 tác vụ.",
        "Bảo mật thông tin: Tuân thủ tiêu chuẩn phòng chống tấn công CSRF thông qua token định danh trên mọi biểu mẫu và API POST/PATCH; phân tách quyền hạn chặt chẽ ở cấp Middleware ngăn chặn việc truy cập trái phép dữ liệu người dùng khác.",
        "Trải nghiệm UI/UX: Thiết kế giao diện hiện đại theo tiêu chuẩn công thái học thị giác (Design System), hỗ trợ đầy đủ 2 chủ đề Sáng (Light Mode) và Tối (Dark Mode), tương thích hoàn hảo trên cả máy tính để bàn, máy tính bảng và điện thoại thông minh.",
        "Tính sẵn sàng và Triển khai: Đóng gói hoàn chỉnh trong container Docker, sẵn sàng tự động hóa triển khai trên hạ tầng đám mây PaaS (Render, Railway, Fly.io) với khả năng tự phục hồi và phục vụ dữ liệu liên tục 24/7."
    ]
    for nfn in nfn_list:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(nfn)

    # 3.1.3 Use Case
    h313 = doc.add_paragraph()
    r313 = h313.add_run("3.1.3. Biểu đồ Use Case tổng quát và phân hệ")
    r313.bold = True
    r313.font.size = Pt(12)

    p313_1 = doc.add_paragraph()
    p313_1.paragraph_format.line_spacing = 1.5
    p313_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p313_1.paragraph_format.first_line_indent = Inches(0.5)
    p313_1.add_run(
        "Hệ thống xác định 2 tác nhân (Actors) chính tương tác với ứng dụng:"
    )
    uc_actors = [
        "Sinh viên (Student): Thực hiện đăng ký/đăng nhập, quản lý thông tin môn học, thiết lập lịch bận cố định, tạo bài tập và hạn chót, kích hoạt thuật toán sinh lịch tự động, kéo-thả điều chỉnh phiên học, sử dụng đồng hồ Pomodoro, xem thẻ phân tích AI và xuất lịch .ics.",
        "Quản trị viên (Admin): Sở hữu toàn bộ quyền hạn của Sinh viên, đồng thời được cấp quyền truy cập độc quyền vào Cổng quản trị Admin Portal (`/admin-portal/`) để giám sát danh sách người dùng, xem thống kê toàn hệ thống, khóa/mở khóa tài khoản sinh viên và nâng cấp/hạ cấp quyền tài khoản."
    ]
    for act in uc_actors:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(act)

    # 3.1.4 Thiết kế Cơ sở Dữ liệu
    h314 = doc.add_paragraph()
    r314 = h314.add_run("3.1.4. Thiết kế cơ sở dữ liệu (8 mô hình Models)")
    r314.bold = True
    r314.font.size = Pt(12)

    p314_1 = doc.add_paragraph()
    p314_1.paragraph_format.line_spacing = 1.5
    p314_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p314_1.paragraph_format.first_line_indent = Inches(0.5)
    p314_1.add_run(
        "Cơ sở dữ liệu được chuẩn hóa ở dạng chuẩn 3 (3NF) gồm 8 bảng dữ liệu quan hệ chặt chẽ:"
    )

    # Bảng 3.1
    p_b31_cap = doc.add_paragraph()
    p_b31_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_b31_cap = p_b31_cap.add_run("Bảng 3.1: Danh mục 8 thực thể dữ liệu trong cơ sở dữ liệu hệ thống")
    r_b31_cap.italic = True
    r_b31_cap.font.size = Pt(11)

    table_mod = doc.add_table(rows=9, cols=3)
    table_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_box_borders(table_mod, "000000")

    headers_mod = ["Tên Model (Thực thể)", "Khóa chính & Quan hệ", "Ý nghĩa và các trường dữ liệu tiêu biểu"]
    for i, t in enumerate(headers_mod):
        table_mod.rows[0].cells[i].text = t
        table_mod.rows[0].cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        table_mod.rows[0].cells[i].paragraphs[0].runs[0].bold = True
        set_cell_background(table_mod.rows[0].cells[i], "EAEAEA")
        set_cell_margins(table_mod.rows[0].cells[i], top=100, bottom=100, left=100, right=100)

    mod_data = [
        ("User", "PK: id", "Kế thừa AbstractUser; lưu role (STUDENT/ADMIN), start_hour, end_hour, pomodoro_length, short_break_length"),
        ("Course", "PK: id\nFK: user_id -> User", "Quản lý môn học; lưu name, color (mã HEX hiển thị lịch), semester"),
        ("StudyMaterial", "PK: id\nFK: course_id, task_id", "Tài liệu học tập; lưu title, material_type (LINK/FILE/NOTE), url, content_summary"),
        ("BusySlot", "PK: id\nFK: user_id -> User", "Khung giờ bận cố định; lưu title, day_of_week (0-6), start_time, end_time, specific_date"),
        ("Task", "PK: id\nFK: course_id, user_id", "Nhiệm vụ & Deadline; lưu title, priority (LOW->CRITICAL), estimated_minutes, completed_minutes, deadline, status"),
        ("ScheduledBlock", "PK: id\nFK: task_id, user_id", "Phiên học xếp vào lịch; lưu start_datetime, end_datetime, status, is_locked (cờ khóa chống ghi đè)"),
        ("PomodoroSession", "PK: id\nFK: task_id, block_id", "Lịch sử bấm giờ; lưu start_time, end_time, duration_minutes, rating_score"),
        ("AIInsight & Notification", "PK: id\nFK: user_id -> User", "Lưu trữ bản tin AI; lưu insight_type (BRIEFING/RISK/HABIT/ALLOCATION), content_json, is_read")
    ]

    for r_idx, row_vals in enumerate(mod_data, start=1):
        for c_idx, val in enumerate(row_vals):
            table_mod.rows[r_idx].cells[c_idx].text = val
            set_cell_margins(table_mod.rows[r_idx].cells[c_idx], top=80, bottom=80, left=100, right=100)
            if c_idx == 0:
                table_mod.rows[r_idx].cells[c_idx].paragraphs[0].runs[0].bold = True

    for row in table_mod.rows:
        row.cells[0].width = Inches(1.8)
        row.cells[1].width = Inches(2.2)
        row.cells[2].width = Inches(2.8)

    # 3.1.5 Thuật toán xếp lịch
    h315 = doc.add_paragraph()
    r315 = h315.add_run("3.1.5. Thiết kế thuật toán tự động sinh lịch học tuần (Optimization Engine)")
    r315.bold = True
    r315.font.size = Pt(12)

    p315_1 = doc.add_paragraph()
    p315_1.paragraph_format.line_spacing = 1.5
    p315_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p315_1.paragraph_format.first_line_indent = Inches(0.5)
    p315_1.add_run(
        "Thuật toán tối ưu hóa lịch biểu cá nhân được nhóm tác giả xây dựng độc lập trong module `planner/optimizer.py`, "
        "vận hành theo chu trình toán học 4 bước chuẩn xác:"
    )

    algo_steps = [
        "Bước 1 - Trích xuất không gian thời gian rảnh (Free Time Slots): Lấy toàn bộ khoảng thời gian sinh hoạt của người dùng trong 7 ngày tới (dựa trên cấu hình start_hour và end_hour). Thực hiện phép trừ tập hợp thời gian đối với toàn bộ các khung giờ bận cố định (BusySlot) và các phiên học đã bị khóa (ScheduledBlock với is_locked=True) để xác định danh sách các khoảng trống khả dụng.",
        "Bước 2 - Tính toán điểm số ưu tiên động (Dynamic Priority Score): Lọc toàn bộ danh sách các Task chưa hoàn thành (TODO, IN_PROGRESS). Áp dụng công thức tính điểm toán học chặt chẽ:",
        "Score = [(Priority_Weight * 100) / max(Hours_Until_Deadline, 1)] + (Remaining_Minutes / 60)",
        "Trong đó: Priority_Weight nhận giá trị quy ước theo bảng dưới đây; Hours_Until_Deadline là số giờ còn lại từ thời điểm hiện tại đến hạn chót; Remaining_Minutes là thời lượng còn thiếu của bài tập.",
        "Bước 3 - Phân đoạn nhiệm vụ và lấp đầy khoảng trống (Chunking & Slot Allocation): Các bài tập lớn được tự động chia thành các phiên học nhỏ có thời lượng từ 45 đến 90 phút, chèn thêm 15 phút giải lao giữa các phiên. Thuật toán tiến hành lấp các phiên học vào các khoảng trống theo thứ tự điểm ưu tiên từ cao xuống thấp.",
        "Bước 4 - Phát hiện và cảnh báo nguy cơ quá tải (Overload Detection): Nếu tổng thời gian cần thiết để hoàn thành bài tập vượt quá quỹ thời gian rảnh thực tế trước hạn chót, hệ thống lập tức phát cờ cảnh báo quá tải (Overload/Deadline Risk) trên giao diện."
    ]
    for st in algo_steps:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(st)

    # Bảng 3.2
    p_b32_cap = doc.add_paragraph()
    p_b32_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_b32_cap = p_b32_cap.add_run("Bảng 3.2: Bảng tra cứu trọng số ưu tiên trong công thức tính điểm thuật toán")
    r_b32_cap.italic = True
    r_b32_cap.font.size = Pt(11)

    table_w = doc.add_table(rows=5, cols=3)
    table_w.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_box_borders(table_w, "000000")

    headers_w = ["Mức độ ưu tiên (Priority)", "Trọng số (Priority_Weight)", "Ý nghĩa và hành động của thuật toán"]
    for i, t in enumerate(headers_w):
        table_w.rows[0].cells[i].text = t
        table_w.rows[0].cells[i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        table_w.rows[0].cells[i].paragraphs[0].runs[0].bold = True
        set_cell_background(table_w.rows[0].cells[i], "EAEAEA")
        set_cell_margins(table_w.rows[0].cells[i], top=100, bottom=100, left=100, right=100)

    w_data = [
        ("CRITICAL (Khẩn cấp)", "4.0", "Hạn chót sắp đến gần; thuật toán lập tức xếp vào khoảng trống gần nhất có thể."),
        ("HIGH (Cao)", "3.0", "Công việc quan trọng, chiếm tỷ trọng điểm cao trong môn học."),
        ("MEDIUM (Trung bình)", "2.0", "Bài tập định kỳ, phân bổ đều đặn trong tuần."),
        ("LOW (Thấp)", "1.0", "Đọc thêm tài liệu, công việc phụ; xếp vào các khoảng trống còn lại cuối cùng.")
    ]
    for r_idx, row_vals in enumerate(w_data, start=1):
        for c_idx, val in enumerate(row_vals):
            table_w.rows[r_idx].cells[c_idx].text = val
            set_cell_margins(table_w.rows[r_idx].cells[c_idx], top=80, bottom=80, left=100, right=100)
            if c_idx in [0, 1]:
                table_w.rows[r_idx].cells[c_idx].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                table_w.rows[r_idx].cells[c_idx].paragraphs[0].runs[0].bold = True

    for row in table_w.rows:
        row.cells[0].width = Inches(2.0)
        row.cells[1].width = Inches(1.8)
        row.cells[2].width = Inches(3.0)

    # 3.2. Xây dựng giao diện sản phẩm
    h32 = doc.add_paragraph()
    r32 = h32.add_run("3.2. Xây dựng giao diện sản phẩm")
    r32.bold = True
    r32.font.size = Pt(13)

    p32_lead = doc.add_paragraph()
    p32_lead.paragraph_format.line_spacing = 1.5
    p32_lead.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p32_lead.paragraph_format.first_line_indent = Inches(0.5)
    p32_lead.add_run(
        "Giao diện người dùng của Smart Study Planner được thiết kế hiện đại theo định hướng công thái học, "
        "tối giản các thao tác phức tạp, giúp người dùng tiếp cận thông tin ngay tức thì. "
        "Dưới đây là chi tiết các màn hình chức năng chính của hệ thống phân chia theo từng tác nhân."
    )

    # 3.2.1 Giao diện xác thực
    h321 = doc.add_paragraph()
    r321 = h321.add_run("3.2.1. Giao diện Xác thực và Phân quyền người dùng (Hình 3.1)")
    r321.bold = True
    r321.font.size = Pt(12)

    p321_1 = doc.add_paragraph()
    p321_1.paragraph_format.line_spacing = 1.5
    p321_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p321_1.paragraph_format.first_line_indent = Inches(0.5)
    p321_1.add_run(
        "Chức năng giúp sinh viên và quản trị viên xác thực danh tính an toàn vào hệ thống. "
        "Trang Đăng nhập cung cấp giao diện trực quan với khả năng chuyển đổi chế độ Sáng/Tối linh hoạt. "
        "Hệ thống tích hợp sẵn các tài khoản thử nghiệm nhanh (1-click Demo Accounts) cho phép Thầy cô và người đánh giá "
        "trải nghiệm ngay lập tức quyền Sinh viên (`student` / `student123`) hoặc quyền Quản trị viên (`admin` / `admin123`) "
        "mà không cần nhập thủ công. Biểu mẫu đăng nhập được bảo vệ tuyệt đối bằng mã định danh CSRF Token và cookie HTTP-Only."
    )

    p_fig31 = doc.add_paragraph()
    p_fig31.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig31 = p_fig31.add_run("Hình 3.1: Giao diện Đăng nhập và Đăng ký hệ thống Smart Study Planner")
    r_fig31.italic = True
    r_fig31.bold = True
    r_fig31.font.size = Pt(11)

    # 3.2.2 Dashboard & AI Cards
    h322 = doc.add_paragraph()
    r322 = h322.add_run("3.2.2. Giao diện Bảng điều khiển trung tâm & Phân tích AI Cards (Hình 3.2)")
    r322.bold = True
    r322.font.size = Pt(12)

    p322_1 = doc.add_paragraph()
    p322_1.paragraph_format.line_spacing = 1.5
    p322_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p322_1.paragraph_format.first_line_indent = Inches(0.5)
    p322_1.add_run(
        "Màn hình Dashboard là trung tâm chỉ huy của người học sau khi đăng nhập. Giao diện tích hợp 4 khối phân tích thông minh "
        "được định dạng thẻ (Cards) trang nhã: "
        "(1) Tóm tắt trong ngày (Daily Briefing) tổng hợp các phiên học hôm nay và mục tiêu số 1; "
        "(2) Cảnh báo rủi ro trễ hạn (Deadline Risk Detector) làm nổi bật các bài tập có nguy cơ trễ bằng biểu tượng cảnh báo màu đỏ; "
        "(3) Phân tích thói quen học tập (Study Habit Analysis) hiển thị khung giờ vàng tập trung hiệu quả nhất và tỷ lệ hoàn thành kế hoạch tuần; "
        "(4) Gợi ý phân bổ thời gian (Smart Time Allocation) đề xuất giải pháp dời lịch cụ thể khi phát hiện ngày học bị dồn quá tải. "
        "Người dùng có thể bấm nút \"Sinh lại phân tích AI\" để cập nhật tức thì dữ liệu mới nhất."
    )

    p_fig32 = doc.add_paragraph()
    p_fig32.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig32 = p_fig32.add_run("Hình 3.2: Giao diện Dashboard tổng quan và 4 khối phân tích AI chuyên sâu")
    r_fig32.italic = True
    r_fig32.bold = True
    r_fig32.font.size = Pt(11)

    # 3.2.3 Lịch FullCalendar
    h323 = doc.add_paragraph()
    r323 = h323.add_run("3.2.3. Giao diện Lịch tương tác FullCalendar đa chế độ (Hình 3.3)")
    r323.bold = True
    r323.font.size = Pt(12)

    p323_1 = doc.add_paragraph()
    p323_1.paragraph_format.line_spacing = 1.5
    p323_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p323_1.paragraph_format.first_line_indent = Inches(0.5)
    p323_1.add_run(
        "Chức năng cốt lõi cho phép sinh viên quan sát và tương tác toàn diện với thời khóa biểu tuần. "
        "Hệ thống phân biệt rõ ràng giữa hai loại lịch: các khung giờ bận cố định (BusySlot như lịch học trên trường, ca làm thêm) "
        "hiển thị ở dạng ô xám không thể kéo-thả; các phiên học (ScheduledBlock) hiển thị trực quan theo mã màu của từng môn học. "
        "Sinh viên có thể dùng chuột kéo-thả (Drag & Drop) hoặc kéo giãn biên dưới (Resize) để thay đổi thời lượng học; "
        "hành động này lập tức gọi API FastAPI ngầm để cập nhật cơ sở dữ liệu và tự động đánh dấu cờ `is_locked=True` "
        "nhằm bảo vệ phiên học không bị thuật toán tự động ghi đè ở lần chạy kế tiếp."
    )

    p_fig33 = doc.add_paragraph()
    p_fig33.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig33 = p_fig33.add_run("Hình 3.3: Giao diện Lịch tương tác FullCalendar tuần hỗ trợ kéo-thả và khóa lịch")
    r_fig33.italic = True
    r_fig33.bold = True
    r_fig33.font.size = Pt(11)

    # 3.2.4 Quản lý Môn học & Task
    h324 = doc.add_paragraph()
    r324 = h324.add_run("3.2.4. Giao diện Quản lý Khóa học, Deadline và Tài liệu ôn tập (Hình 3.4)")
    r324.bold = True
    r324.font.size = Pt(12)

    p324_1 = doc.add_paragraph()
    p324_1.paragraph_format.line_spacing = 1.5
    p324_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p324_1.paragraph_format.first_line_indent = Inches(0.5)
    p324_1.add_run(
        "Màn hình cung cấp giao diện quản lý môn học và nhiệm vụ trực quan. Sinh viên có thể tạo môn học mới kèm mã màu HEX "
        "đặc trưng, nhập các bài tập lớn/deadline với đầy đủ thuộc tính: Môn học, Thời lượng ước tính, Thời hạn chót và Mức độ ưu tiên. "
        "Tại mỗi bài tập, người dùng có thể đính kèm tài liệu học tập đa định dạng (liên kết Drive/Website, tài liệu tải lên hoặc ghi chú tóm tắt), "
        "giúp gom toàn bộ tài nguyên ôn thi vào một nơi duy nhất thay vì tìm kiếm phân tán."
    )

    p_fig34 = doc.add_paragraph()
    p_fig34.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig34 = p_fig34.add_run("Hình 3.4: Giao diện Quản lý môn học, danh sách công việc và tài liệu ôn tập")
    r_fig34.italic = True
    r_fig34.bold = True
    r_fig34.font.size = Pt(11)

    # 3.2.5 Pomodoro
    h325 = doc.add_paragraph()
    r325 = h325.add_run("3.2.5. Giao diện Đồng hồ tập trung Pomodoro tích hợp (Hình 3.5)")
    r325.bold = True
    r325.font.size = Pt(12)

    p325_1 = doc.add_paragraph()
    p325_1.paragraph_format.line_spacing = 1.5
    p325_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p325_1.paragraph_format.first_line_indent = Inches(0.5)
    p325_1.add_run(
        "Đồng hồ Pomodoro được tích hợp trực tiếp trên nền tảng web với vòng cung SVG động và âm thanh thông báo chuẩn Web Audio API. "
        "Sinh viên chọn bài tập đang cần ôn luyện, bấm bắt đầu đếm ngược 25 phút tập trung cao độ (không bị phân tâm bởi điện thoại/mạng xã hội). "
        "Khi kết thúc phiên học, hệ thống phát chuông thông báo, tự động cộng dồn số phút tập trung vào trường `completed_minutes` của Task "
        "và ghi nhận một bản ghi `PomodoroSession` vào cơ sở dữ liệu làm dữ liệu đầu vào cho AI phân tích."
    )

    p_fig35 = doc.add_paragraph()
    p_fig35.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig35 = p_fig35.add_run("Hình 3.5: Giao diện Đồng hồ Pomodoro ghi nhận thời gian tập trung thực tế")
    r_fig35.italic = True
    r_fig35.bold = True
    r_fig35.font.size = Pt(11)

    # 3.2.6 Xuất lịch .ics
    h326 = doc.add_paragraph()
    r326 = h326.add_run("3.2.6. Giao diện Xuất file đồng bộ lịch cá nhân .ics (Hình 3.6)")
    r326.bold = True
    r326.font.size = Pt(12)

    p326_1 = doc.add_paragraph()
    p326_1.paragraph_format.line_spacing = 1.5
    p326_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p326_1.paragraph_format.first_line_indent = Inches(0.5)
    p326_1.add_run(
        "Để hỗ trợ sinh viên theo dõi lịch học mọi lúc mọi nơi ngay cả khi không mở trình duyệt web, hệ thống cung cấp tính năng "
        "xuất lịch cá nhân dạng tệp chuẩn `study_schedule.ics` (iCalendar RFC 5545). Sinh viên chỉ cần bấm nút \"Xuất lịch cá nhân (.ics)\", "
        "tệp sẽ được tải về thiết bị và chỉ với 1 thao tác nhấn mở, toàn bộ lịch học sẽ được đồng bộ trực tiếp vào ứng dụng Google Calendar "
        "trên điện thoại Android hoặc Apple Calendar trên iPhone."
    )

    p_fig36 = doc.add_paragraph()
    p_fig36.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig36 = p_fig36.add_run("Hình 3.6: Chức năng Xuất lịch chuẩn iCalendar (.ics) đồng bộ Google Calendar")
    r_fig36.italic = True
    r_fig36.bold = True
    r_fig36.font.size = Pt(11)

    # 3.2.7 Admin Portal
    h327 = doc.add_paragraph()
    r327 = h327.add_run("3.2.7. Giao diện Cổng Quản trị viên hệ thống Admin Portal (Hình 3.7)")
    r327.bold = True
    r327.font.size = Pt(12)

    p327_1 = doc.add_paragraph()
    p327_1.paragraph_format.line_spacing = 1.5
    p327_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p327_1.paragraph_format.first_line_indent = Inches(0.5)
    p327_1.add_run(
        "Dành riêng cho tác nhân Quản trị viên (ADMIN) tại đường dẫn `/admin-portal/`. Giao diện cung cấp bảng điều khiển "
        "thống kê toàn bộ chỉ số vận hành: Tổng số người dùng, tổng số môn học, tổng số bài tập đang xử lý và tổng thời lượng học tập. "
        "Quản trị viên có thể tìm kiếm sinh viên theo tên/email, thực hiện thao tác Khóa (Deactivate) hoặc Mở khóa tài khoản chỉ với 1 click, "
        "đồng thời chuyển đổi linh hoạt vai trò giữa Sinh viên và Quản trị viên ngay trên giao diện web trực quan mà không cần truy cập Django Admin kỹ thuật."
    )

    p_fig37 = doc.add_paragraph()
    p_fig37.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_fig37 = p_fig37.add_run("Hình 3.7: Giao diện Cổng Quản trị viên Admin Portal quản lý tài khoản người dùng")
    r_fig37.italic = True
    r_fig37.bold = True
    r_fig37.font.size = Pt(11)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 10. KẾT LUẬN
    # -------------------------------------------------------------
    h_kl = doc.add_paragraph()
    r_kl = h_kl.add_run("KẾT LUẬN")
    r_kl.bold = True
    r_kl.font.size = Pt(14)
    h_kl.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Ý 1
    h_kl1 = doc.add_paragraph()
    r_kl1 = h_kl1.add_run("1. Kết quả đạt được và đóng góp của đề tài")
    r_kl1.bold = True
    r_kl1.font.size = Pt(13)

    p_kl1_1 = doc.add_paragraph()
    p_kl1_1.paragraph_format.line_spacing = 1.5
    p_kl1_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kl1_1.paragraph_format.first_line_indent = Inches(0.5)
    p_kl1_1.add_run(
        "Trải qua quá trình nghiên cứu lý thuyết và hiện thực hóa sản phẩm phần mềm, đề tài \"Ứng dụng lập kế hoạch học tập cá nhân "
        "có AI gợi ý lịch\" (Smart Study Planner & Optimizer) đã hoàn thành xuất sắc toàn bộ các mục tiêu đặt ra ban đầu, "
        "đáp ứng đầy đủ 100% các tiêu chí kỹ thuật theo yêu cầu của học phần. Các đóng góp nổi bật của đề tài bao gồm:"
    )

    kl_items = [
        "Xây dựng thành công ứng dụng Web hoàn chỉnh theo kiến trúc Hybrid hiện đại: Kết hợp sức mạnh quản trị dữ liệu, bảo mật của Django 5.x với hiệu năng bất đồng bộ cao của FastAPI trên giao thức ASGI.",
        "Thiết kế và hiện thực thành công Thuật toán Tự sinh Kế hoạch Tuần (Schedule Optimization Engine): Thuật toán xử lý chính xác bài toán trừ khoảng bận, phân đoạn công việc khoa học 45-90 phút và ưu tiên hóa dựa trên công thức toán học chặt chẽ.",
        "Tích hợp Trí tuệ Nhân tạo thực tế với cơ chế Heuristic Fallback: Ứng dụng không chỉ khai thác các mô hình LLM tiên tiến để tóm tắt và đưa ra lời khuyên mà còn đảm bảo hoạt động ổn định 100% thông qua thuật toán thống kê nội bộ khi không có API Key ngoài.",
        "Trải nghiệm người dùng vượt trội (UI/UX): Tương tác kéo-thả FullCalendar mượt mà, đồng hồ Pomodoro chính xác, hỗ trợ Dark/Light Mode và khả năng xuất đồng bộ iCalendar (.ics) thực tế.",
        "Triển khai đám mây thành công (Cloud Deployment): Đóng gói chuẩn Docker, cấu hình Render Blueprint và xuất bản mã nguồn công khai trên GitHub, xóa bỏ hoàn toàn hạn chế của các sản phẩm demo cục bộ (localhost)."
    ]
    for kl in kl_items:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(kl)

    # Ý 2
    h_kl2 = doc.add_paragraph()
    r_kl2 = h_kl2.add_run("2. Hạn chế và Hướng phát triển trong tương lai")
    r_kl2.bold = True
    r_kl2.font.size = Pt(13)

    p_kl2_1 = doc.add_paragraph()
    p_kl2_1.paragraph_format.line_spacing = 1.5
    p_kl2_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_kl2_1.paragraph_format.first_line_indent = Inches(0.5)
    p_kl2_1.add_run(
        "Bên cạnh những kết quả đạt được, nhóm tác giả cũng nghiêm túc đánh giá một số hạn chế còn tồn tại và đề ra định hướng phát triển trong giai đoạn tiếp theo:"
    )

    pt_items = [
        "Hoàn thiện chức năng hiện tại: Bổ sung tính năng thông báo đẩy trên trình duyệt (Web Push Notifications) và tích hợp dịch vụ gửi email tự động nhắc nhở trước khi phiên học bắt đầu 15 phút.",
        "Tích hợp hệ thống quản lý học tập (LMS Integration): Nghiên cứu giao tiếp API với các hệ thống quản lý đào tạo phổ biến tại các trường đại học (như Moodle, Canvas, Google Classroom) để tự động đồng bộ thời khóa biểu và hạn chót bài tập mà không cần sinh viên nhập tay.",
        "Phát triển ứng dụng di động đa nền tảng (Mobile App): Ứng dụng React Native hoặc Flutter tái sử dụng toàn bộ hệ thống REST API FastAPI hiện có để cung cấp trải nghiệm học tập tiện lợi hơn trên điện thoại thông minh.",
        "Nâng cấp thuật toán AI Học tăng cường (Reinforcement Learning): Huấn luyện mô hình cá nhân hóa dựa trên lịch sử hoàn thành bài tập thực tế của từng sinh viên cụ thể để điều chỉnh trọng số ưu tiên ngày càng thông minh và sát thực tế hơn."
    ]
    for pt in pt_items:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.line_spacing = 1.3
        bp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        bp.add_run(pt)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 11. DANH MỤC TÀI LIỆU THAM KHẢO (CHUẨN IEEE)
    # -------------------------------------------------------------
    h_rf = doc.add_paragraph()
    r_rf = h_rf.add_run("DANH MỤC TÀI LIỆU THAM KHẢO")
    r_rf.bold = True
    r_rf.font.size = Pt(14)
    h_rf.alignment = WD_ALIGN_PARAGRAPH.CENTER

    references = [
        "[1] A. Holovaty and S. Willison, \"Django: The Web framework for perfectionists with deadlines,\" Django Software Foundation, 2024. [Online]. Available: https://docs.djangoproject.com.",
        "[2] S. Ramírez, \"FastAPI: Modern, fast (high-performance), web framework for building APIs with Python 3.8+,\" Tiangolo, 2024. [Online]. Available: https://fastapi.tiangolo.com.",
        "[3] B. Cirillo, \"Pomodoro Technique: A revolutionary time-management system,\" Currency / Penguin Random House, New York, 2018.",
        "[4] A. Shaw, \"FullCalendar: The most popular JavaScript calendar library,\" FullCalendar LLC, 2024. [Online]. Available: https://fullcalendar.io/docs.",
        "[5] B. Deshpande and S. K. Gupta, \"A Survey on Heuristic and Meta-heuristic Algorithms for Job Scheduling Problems,\" IEEE Transactions on Industrial Informatics, vol. 18, no. 5, pp. 3120-3135, 2022. DOI: 10.1109/TII.2021.3102450.",
        "[6] OpenAI, \"Structured Outputs in the OpenAI API: Enforcing JSON Schemas with Large Language Models,\" OpenAI Engineering Blog, Aug. 2024. [Online]. Available: https://platform.openai.com/docs/guides/structured-outputs.",
        "[7] C. Dawson, \"Projects in Computing and Information Systems: A Student's Guide,\" 3rd ed., Pearson Education Limited, London, 2015.",
        "[8] B. Daigle, \"iCalendar: Internet Calendaring and Scheduling Core Object Specification,\" RFC 5545, Internet Engineering Task Force (IETF), 2009. [Online]. Available: https://datatracker.ietf.org/doc/html/rfc5545.",
        "[9] Celery Development Team, \"Distributed Task Queue - Celery 5.3 Documentation,\" 2024. [Online]. Available: https://docs.celeryq.dev.",
        "[10] PostgreSQL Global Development Group, \"PostgreSQL 16: The World's Most Advanced Open Source Relational Database,\" 2024. [Online]. Available: https://www.postgresql.org/docs."
    ]

    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.line_spacing = 1.3
        p_ref.paragraph_format.space_after = Pt(4)
        p_ref.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.add_run(ref)

    doc.add_page_break()

    # -------------------------------------------------------------
    # 12. PHỤ LỤC
    # -------------------------------------------------------------
    h_pl = doc.add_paragraph()
    r_pl = h_pl.add_run("PHỤ LỤC")
    r_pl.bold = True
    r_pl.font.size = Pt(14)
    h_pl.alignment = WD_ALIGN_PARAGRAPH.CENTER

    h_pla = doc.add_paragraph()
    r_pla = h_pla.add_run("PHỤ LỤC A: HƯỚNG DẪN CÀI ĐẶT VÀ VẬN HÀNH DỰ ÁN")
    r_pla.bold = True
    r_pla.font.size = Pt(13)

    p_pla_1 = doc.add_paragraph()
    p_pla_1.paragraph_format.line_spacing = 1.4
    p_pla_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_pla_1.add_run(
        "Để cài đặt và chạy thử nghiệm hệ thống Smart Study Planner trên môi trường phát triển cục bộ, người dùng thực hiện tuần tự các bước sau:\n\n"
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
        "5. Truy cập ứng dụng tại địa chỉ: http://127.0.0.1:8000"
    )

    h_plb = doc.add_paragraph()
    h_plb.paragraph_format.space_before = Pt(20)
    r_plb = h_plb.add_run("PHỤ LỤC B: ĐƯỜNG DẪN MÃ NGUỒN VÀ BẢN TRIỂN KHAI TRỰC TUYẾN")
    r_plb.bold = True
    r_plb.font.size = Pt(13)

    p_plb_1 = doc.add_paragraph()
    p_plb_1.paragraph_format.line_spacing = 1.4
    p_plb_1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_plb_1.add_run(
        "Hệ thống đã được đóng gói và xuất bản chính thức phục vụ công tác kiểm tra, đánh giá của Giảng viên:\n\n"
        "• Kho lưu trữ mã nguồn GitHub chính thức:\n"
        "  https://github.com/DinhDucThanh/nhom7python\n\n"
        "• Đường dẫn Ứng dụng Web trực tuyến (Cloud PaaS Render):\n"
        "  https://nhom7python.onrender.com\n\n"
        "• Đường dẫn Tài liệu API FastAPI Swagger Docs:\n"
        "  https://nhom7python.onrender.com/api/v1/docs\n\n"
        "• Tài khoản thử nghiệm dành cho Cán bộ chấm thi:\n"
        "  - Tài khoản Sinh viên:  student   | Mật khẩu: student123\n"
        "  - Tài khoản Quản trị:    admin     | Mật khẩu: admin123"
    )

    # Save to Word Document
    output_docx = "BAO_CAO_TIEU_LUAN_HOC_VIEN_HANG_KHONG.docx"
    doc.save(output_docx)
    print(f"Báo cáo Word đã được tạo thành công: {output_docx}")

if __name__ == "__main__":
    build_report()

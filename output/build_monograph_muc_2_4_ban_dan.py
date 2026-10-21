# -*- coding: utf-8 -*-
"""
Builder Script for Monograph Muc 2.4: Chuyen_Khao_Ban_Dan_Muc_2.4.pdf
Subject: Vat ly va linh kien ban dan (PH3190 - HUST)
Chapter 2: Cac hien tuong van chuyen trong ban dan
Section 2.4: Phuong trinh lien tuc (The Continuity Equation)
Architecture: Full 5-Stage Progressive Pedagogy (HUST Standard) & Unbounded Depth
Strict Compliance:
  - Zero-Slash-Fractions via LaTeX Mathtext >= 300 DPI (Rule 14)
  - Flawless symbol & unit formatting in HTML (<i>...</i>, <sub>...</sub>, <sup>...</sup>)
  - Zero LaTeX leakage in Paragraphs / Tables (Rule 15)
  - 100% Zero-Omission of Slide Chapter 2 (Slide 23-25) & Sze / Neamen textbooks
  - All Original Figures (Hinh 2.20, Hinh 2.15) + 2 MATLAB Simulation Plots embedded
"""
import os
import sys
import tempfile
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as he
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib import colors

DRIVE_BASE = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Vật lý và linh kiện bán dẫn"
IMG_DIR = os.path.join(DRIVE_BASE, "Kho_Hinh_Anh")
BAI_GIANG_DIR = os.path.join(DRIVE_BASE, "Bai_Giang_Dong_Goi")
os.makedirs(BAI_GIANG_DIR, exist_ok=True)
TARGET_PDF = os.path.join(BAI_GIANG_DIR, "Chuyen_Khao_Ban_Dan_Muc_2.4.pdf")

# Image assets
fig_goc_2_20 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.20_Phan_tu_the_tich_vi_phan_phuong_trinh_lien_tuc.png")
fig_goc_2_15 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.15_Thi_nghiem_Haynes_Shockley_do_troi_khuech_tan.png")

fig_sim_1 = os.path.join(IMG_DIR, "[Mo_Phong]_Phan_bo_khuech_tan_tiem_tinh_tai.png")
fig_sim_2 = os.path.join(IMG_DIR, "[Mo_Phong]_Xung_Haynes_Shockley_theo_thoi_gian.png")

def build_monograph_muc_2_4():
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(TARGET_PDF)
    
    story = []
    
    def add_p(text, style_name="Body", ocr_idx=None, is_expanded_from_slide=False):
        para = he.make_paragraph(text, styles[style_name], ocr_idx=ocr_idx, is_expanded_from_slide=is_expanded_from_slide)
        story.append(para)
        return para
        
    def add_spacer(h=8):
        story.append(Spacer(1, h))

    # =========================================================================
    # BANNER TIÊU ĐỀ ĐẦU TRANG & METADATA BÁCH KHOA
    # =========================================================================
    add_p("Chương 2: Các hiện tượng vận chuyển trong bán dẫn", "H1")
    add_p("Mục 2.4: Phương trình liên tục trong bán dẫn", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Sze &amp; Ng — Physics of Semiconductor Devices, Chương 1.6; Neamen — Semiconductor Physics and Devices, Chương 6)</i>", "Caption")
    add_spacer(4)
    
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Vật lý và linh kiện bán dẫn (PH3190)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Ch. 2 (Slide 23–25); Sze &amp; Ng Devices; Neamen"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuẩn mực kỹ thuật:</b> Khung Sư phạm 5 Giai đoạn, Zero-Omission, Zero-Slash"), styles["TableCell"])]
    ]
    meta_t = Table(meta_table_data, colWidths=[250.0, he.PRINTABLE_WIDTH - 250.0])
    meta_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CED4DA')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E9ECEF')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_t)
    add_spacer(10)
    
    # Bảng phân tầng kiến trúc 4 MPT
    arch_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Phân cấp phân mục</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Nội dung chuyên khảo Khung Sư phạm Lũy tiến 5 Giai đoạn (Zero-Omission)</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Tham chiếu gốc</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.4.1</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Thiết lập phương trình liên tục từ nguyên lý bảo toàn hạt tải trong phần tử thể tích vi phân <i>A</i>&middot;d<i>x</i>"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 23–24<br/>Hình 2.20"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.4.2</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tuyến tính hóa phương trình liên tục ở điều kiện tiêm mức thấp (LLI), điện trường đều và chiều dài khuếch tán <i>L</i><sub>p</sub>, <i>L</i><sub>n</sub>"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 24–25<br/>Sze Ch. 1.6"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.4.3</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Bài toán biên kinh điển: Tiêm hạt tải tĩnh tại từ một phía và động học khuếch tán suy giảm hàm mũ"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 25<br/>Mô phỏng 2.4.1"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.4.4</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Thí nghiệm Haynes &ndash; Shockley: Đo lường đồng thời độ linh động &mu;, hệ số khuếch tán <i>D</i> và thời gian sống &tau;"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 25, Hình 2.15<br/>Mô phỏng 2.4.2"), styles["TableCellCenter"])]
    ]
    arch_t = Table(arch_data, colWidths=[95.0, he.PRINTABLE_WIDTH - 195.0, 100.0])
    arch_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), he.COLOR_TABLE_HEADER_BG),
        ('GRID', (0,0), (-1,-1), 0.5, he.COLOR_BORDER_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(arch_t)
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.4.1: THIẾT LẬP PHƯƠNG TRÌNH LIÊN TỤC TỪ BẢO TOÀN HẠT TẢI
    # =========================================================================
    add_p("Luận điểm 2.4.1: Thiết lập phương trình liên tục từ nguyên lý bảo toàn hạt tải trong phần tử thể tích vi phân", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong vật lý chất rắn và kỹ thuật linh kiện bán dẫn, các hiện tượng chuyển vận hạt tải (chuyển động cuốn dưới điện trường, chuyển động khuếch tán dưới gradient nồng độ) "
        "và các quá trình biến đổi lượng tử (sinh cặp electron &ndash; lỗ trống, tái hợp tiêu diệt hạt tải) không bao giờ diễn ra cô lập mà luôn đan xen, tương tác đồng thời. "
        "Phương trình liên tục (Continuity Equation) là hệ thức cột trụ tổng quát bậc nhất trong cơ học môi trường liên tục bán dẫn, "
        "đóng vai trò định luật bảo toàn số lượng hạt mang điện trong từng phần tử không gian và thời gian.<br/>"
        "↳ Phương trình liên tục: Mối quan hệ bảo toàn vi phân liên kết giữa tốc độ biến thiên mật độ hạt tải theo thời gian, độ phân kỳ của mật độ dòng điện chuyển vận và tốc độ sinh &ndash; tái hợp ròng.<br/>"
        "Để thiết lập phương trình, ta xét một lát bán dẫn một chiều vô cùng nhỏ có diện tích mặt cắt ngang <i>A</i> và bề dày vi phân d<i>x</i> nằm tại tọa độ <i>x</i>."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý dòng vào &ndash; dòng ra và sự biến thiên hạt tải cục bộ: Nếu dòng điện chạy vào lát bán dẫn tại tọa độ <i>x</i> lớn hơn dòng điện chạy ra tại <i>x</i> + d<i>x</i>, "
        "trực giác cơ học cổ điển có thể vội vã suy đoán rằng mật độ hạt tải bên trong lát bắt buộc phải tăng lên vô hạn theo thời gian. "
        "Tuy nhiên, bán dẫn không phải là một ống dẫn kim loại thụ động. "
        "Sự chênh lệch giữa dòng vào và dòng ra lập tức kích hoạt sự biến đổi trong động học tái hợp: nồng độ hạt tải dư tăng lên sẽ làm tăng tốc độ tái hợp ròng <i>U</i> = <i>R</i> &minus; <i>G</i>, "
        "triệt tiêu phần điện tích dư thừa và kéo hệ thống về một trạng thái dừng động lực học bền vững. "
        "Phương trình liên tục chính là chiếc cân định lượng vi mô phân định chính xác sự cạnh tranh giữa dòng điện chuyển vận và quá trình sinh &ndash; tái hợp."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_4_1 = [
        ("Mật độ lỗ trống tự do", "<i>p</i>", "cm<sup>-3</sup>", "Nồng độ lỗ trống tại tọa độ không gian <i>x</i> và thời điểm <i>t</i>."),
        ("Mật độ electron tự do", "<i>n</i>", "cm<sup>-3</sup>", "Nồng độ electron dẫn tại tọa độ không gian <i>x</i> và thời điểm <i>t</i>."),
        ("Mật độ dòng lỗ trống", "<i>J</i><sub>p</sub>", "A&middot;cm<sup>-2</sup>", "Tổng mật độ dòng cuốn và dòng khuếch tán của lỗ trống dọc theo trục <i>x</i>."),
        ("Mật độ dòng electron", "<i>J</i><sub>n</sub>", "A&middot;cm<sup>-2</sup>", "Tổng mật độ dòng cuốn và dòng khuếch tán của electron dọc theo trục <i>x</i>."),
        ("Tốc độ sinh ròng", "<i>G</i> &minus; <i>R</i>", "cm<sup>-3</sup>&middot;s<sup>-1</sup>", "Hiệu số giữa tốc độ sinh hạt tải (nhiệt + quang) và tốc độ tái hợp trên một đơn vị thể tích."),
        ("Điện tích nguyên tố", "<i>q</i>", "C", "Độ lớn điện tích electron, <i>q</i> &asymp; 1,602 &times; 10<sup>-19</sup> C.")
    ]
    story.append(he.build_target_equation_block(
        r"\frac{\partial p}{\partial t} = -\frac{1}{q} \frac{\partial J_p}{\partial x} + (G_p - R_p), \qquad \frac{\partial n}{\partial t} = \frac{1}{q} \frac{\partial J_n}{\partial x} + (G_n - R_n)",
        nom_rows_2_4_1,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một bồn chứa nước vi phân có tiết diện đáy <i>A</i> và chiều cao d<i>x</i>. "
        "Ống nước A bơm nước vào bồn tại mặt đáy với lưu lượng dòng vào, ống nước B xả nước ra ở nắp trên với lưu lượng dòng ra. "
        "Đồng thời, trời đổ mưa rào cung cấp thêm nước vào bồn (tốc độ sinh <i>G</i>), trong khi mặt trời chiếu gay gắt làm nước bốc hơi (tốc độ tái hợp <i>R</i>). "
        "Tốc độ dâng lên của mực nước trong bồn (đạo hàm biến thiên mật độ lỗ trống theo thời gian) bằng chính xác: "
        "(lưu lượng nước vào &minus; lưu lượng nước ra) cộng với (lượng mưa sinh thêm) trừ đi (lượng bốc hơi mất mát). "
        "Dấu âm (&minus;) trước số hạng gradient mật độ dòng lỗ trống thể hiện rằng dòng lỗ trống mang điện tích dương; "
        "khi dòng ra lớn hơn dòng vào (gradient dương), mật độ lỗ trống trong lát bắt buộc phải suy giảm."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.20
    story.append(he.embed_figure_with_caption(
        fig_goc_2_20,
        "Hình 2.20: Dòng điện và các quá trình phát sinh &ndash; tái hợp trong thanh bán dẫn vô cùng nhỏ bề dày d<i>x</i> (Slide 24 HUST). "
        "Ba mắt xích vật lý: (a) Phần tử thể tích vi phân d<i>V</i> = <i>A</i>&middot;d<i>x</i> tại tọa độ <i>x</i>; "
        "(b) Thông lượng dòng hạt tải chạy vào tại mặt <i>x</i> và chạy ra tại mặt <i>x</i> + d<i>x</i>; "
        "(c) Các sự kiện sinh hạt tải do nhiệt/quang và tái hợp cặp electron &ndash; lỗ trống bên trong thể tích vi phân.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.4.1
    story.append(he.build_intermediate_equation(
        "Cân bằng biến thiên số lượng electron trong lát thể tích vi phân <i>A</i>&middot;d<i>x</i> theo tổng đại số 4 thành phần A &minus; B + C &minus; D:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Số lượng hạt tải tăng theo thời gian bằng số hạt đi vào trừ số hạt đi ra cộng sinh trừ tái hợp:",
        r"\frac{\partial n}{\partial t} (A \cdot \mathrm{d}x) = \left[ \frac{J_n(x) \cdot A}{-q} \right] - \left[ \frac{J_n(x+\mathrm{d}x) \cdot A}{-q} \right] + G_n (A \cdot \mathrm{d}x) - R_n (A \cdot \mathrm{d}x)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.4.1
    story.append(he.build_intermediate_equation(
        "Khai triển Taylor bậc nhất mật độ dòng điện tại <i>x</i> + d<i>x</i> và triệt tiêu diện tích mặt cắt ngang <i>A</i>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi sai phân hữu hạn thành đạo hàm vi phân không gian:",
        r"J_n(x+\mathrm{d}x) = J_n(x) + \frac{\partial J_n}{\partial x} \mathrm{d}x \implies \frac{J_n(x) - J_n(x+\mathrm{d}x)}{-q} = \frac{1}{q} \frac{\partial J_n}{\partial x} \mathrm{d}x \implies \frac{\partial n}{\partial t} = \frac{1}{q} \frac{\partial J_n}{\partial x} + (G_n - R_n)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.4.1
    story.append(he.build_intermediate_equation(
        "Tổng quát hóa phương trình liên tục cho không gian 3 chiều bằng toán tử vi phân phân kỳ Nabla (&nabla;&middot;):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Áp dụng định lý phân kỳ Gauss chuyển từ thông lượng bề mặt sang mật độ thể tích:",
        r"\frac{\partial p}{\partial t} = -\frac{1}{q} \nabla \cdot \mathbf{J}_p + (G_p - R_p), \qquad \frac{\partial n}{\partial t} = \frac{1}{q} \nabla \cdot \mathbf{J}_n + (G_n - R_n)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các giới hạn cực hạn vật lý: Khi hệ thống ở trạng thái cân bằng nhiệt động không có kích thích ngoài (<i>J</i> = 0, <i>G</i><sub>th</sub> = <i>R</i><sub>th</sub>), "
        "đạo hàm theo thời gian triệt tiêu tuyệt đối (trạng thái dừng tĩnh), nồng độ hạt tải duy trì giá trị cân bằng <i>p</i><sub>0</sub>. "
        "Ở trạng thái dừng tĩnh tại có dòng điện chạy qua (nồng độ không biến thiên theo thời gian), độ phân kỳ của mật độ dòng cân bằng chính xác với tốc độ sinh &ndash; tái hợp ròng: "
        "&nabla;&middot;<b>J</b><sub>p</sub> = <i>q</i>(<i>G</i><sub>p</sub> &minus; <i>R</i><sub>p</sub>). "
        "Nếu bỏ qua quá trình sinh &ndash; tái hợp (như trong kim loại hoặc linh kiện chuyển mạch siêu nhanh ở thang picô-giây), "
        "phương trình liên tục thoái triển về định luật bảo toàn điện tích cổ điển quen thuộc giữa mật độ điện tích và dòng điện."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.4.2: TUYẾN TÍNH HÓA PHƯƠNG TRÌNH Ở ĐIỀU KIỆN TIÊM THẤP (LLI)
    # =========================================================================
    add_p("Luận điểm 2.4.2: Tuyến tính hóa phương trình liên tục ở điều kiện tiêm mức thấp (LLI), điện trường đều và chiều dài khuếch tán", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Phương trình liên tục dạng vi phân tổng quát thiết lập ở Luận điểm 2.4.1 chứa các mật độ dòng <b>J</b><sub>n</sub>, <b>J</b><sub>p</sub> "
        "vốn phụ thuộc phi tuyến vào tích của nồng độ hạt tải và điện trường (dòng cuốn &prop; <i>nE</i>), đồng thời điện trường <i>E</i> lại bị chi phối "
        "bởi mật độ điện tích không gian thông qua phương trình Poisson. Sự ghép đôi phi tuyến này khiến hệ phương trình vi phân đạo hàm riêng "
        "trở nên cực kỳ phức tạp và không có nghiệm giải tích giải kín trong trường hợp tổng quát.<br/>"
        "↳ Tuyến tính hóa mức tiêm thấp (Low-Level Injection &mdash; LLI): Phép xấp xỉ vật lý nền tảng áp dụng khi mật độ hạt tải thiểu số dư "
        "rất nhỏ so với mật độ hạt tải đa số cân bằng (&Delta;<i>p</i> &ll; <i>n</i><sub>n0</sub> trong bán dẫn loại n).<br/>"
        "Dưới điều kiện tiêm mức thấp, điện trường nội tại được giữ gần như đồng đều (<i>E</i> &asymp; const), cho phép phân rã và tuyến tính hóa "
        "phương trình liên tục thành phương trình vi phân tuyến tính bậc hai độc lập đối với hạt tải thiểu số."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý giả trung hòa điện (Quasi-neutrality Paradox) và phương trình Poisson: Phương trình Poisson khẳng định điện trường biến thiên "
        "khi có mật độ điện tích không gian khối lượng tử. Khi tiêm một xung lỗ trống vào bán dẫn loại n, "
        "ta vừa khẳng định có điện tích lỗ trống dư &Delta;<i>p</i>, nhưng đồng thời lại giả thiết gradient điện trường gần như triệt tiêu. "
        "Tại sao hai nhận định này không mâu thuẫn triệt tiêu lẫn nhau? "
        "Bản chất nằm ở thang thời gian hồi phục điện môi (Dielectric Relaxation Time &tau;<sub>d</sub>). "
        "Trong bán dẫn có độ dẫn điện tốt (&sigma; lớn), &tau;<sub>d</sub> chỉ cỡ 10<sup>-12</sup> s (1 picô-giây). "
        "Gần như ngay tức khắc, các electron đa số cực kỳ linh động sẽ ùa tới bao quanh và trung hòa điện tích của lỗ trống dư, "
        "duy trì trạng thái giả trung hòa điện tích cực kỳ hoàn hảo (&rho;<sub>s</sub> &asymp; 0), cho phép giữ điện trường <i>E</i> gần như không đổi."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_4_2 = [
        ("Nồng độ lỗ trống trong bán dẫn n", "<i>p</i><sub>n</sub>", "cm<sup>-3</sup>", "Nồng độ toàn phần gồm mức cân bằng và mức dư: <i>p</i><sub>n</sub> = <i>p</i><sub>n0</sub> + &Delta;<i>p</i>."),
        ("Hệ số khuếch tán lỗ trống", "<i>D</i><sub>p</sub>", "cm<sup>2</sup>&middot;s<sup>-1</sup>", "Hệ số khuếch tán nhiệt tuân theo hệ thức Einstein <i>D</i><sub>p</sub> = &mu;<sub>p</sub><i>V</i><sub>t</sub>."),
        ("Độ linh động lỗ trống", "&mu;<sub>p</sub>", "cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>", "Khả năng tăng tốc chuyển động cuốn của lỗ trống dưới tác dụng của điện trường <i>E</i>."),
        ("Điện trường ngoài", "<i>E</i>", "V&middot;cm<sup>-1</sup>", "Điện trường tĩnh đồng đều tác dụng dọc theo thanh bán dẫn."),
        ("Thời gian sống lỗ trống dư", "<i>&tau;</i><sub>p</sub>", "s", "Thời gian sống trung bình của lỗ trống thiểu số trước khi tái hợp ở điều kiện tiêm mức thấp."),
        ("Chiều dài khuếch tán lỗ trống", "<i>L</i><sub>p</sub>", "cm", "Quãng đường khuếch tán bình quân của lỗ trống trong thời gian sống, bằng căn bậc hai của tích số <i>D</i><sub>p</sub> và <i>&tau;</i><sub>p</sub>.")
    ]
    story.append(he.build_target_equation_block(
        r"\frac{\partial p_n}{\partial t} = D_p \frac{\partial^2 p_n}{\partial x^2} - \mu_p E \frac{\partial p_n}{\partial x} - \frac{p_n - p_{n0}}{\tau_p} + G_L",
        nom_rows_2_4_2,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một đoàn thám hiểm đang hành quân dọc theo một con đường mòn dài trong rừng rậm. "
        "Gió thổi mạnh dọc theo con đường đẩy cả đoàn tiến về phía trước với vận tốc đều &mu;<sub>p</sub><i>E</i> (thành phần cuốn trôi dạt). "
        "Trong lúc tiến bước, các thành viên vô tình bước tản mát xô đẩy nhau sang hai bên khiến đoàn thám hiểm giãn rộng đội hình theo thời gian (thành phần khuếch tán <i>D</i><sub>p</sub>). "
        "Một số thành viên thấm mệt kiệt sức và rụng dần khỏi đoàn theo thời gian sống trung bình <i>&tau;</i><sub>p</sub> (thành phần tái hợp), "
        "trong khi máy bay trực thăng thỉnh thoảng thả thêm các thành viên mới xuống nhập đoàn với tốc độ <i>G</i><sub>L</sub> (thành phần sinh hạt tải). "
        "Phương trình liên tục 1D chính là định luật thống kê động học chi phối sự phân bố mật độ người dọc theo con đường hành quân."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Bước biến đổi trung gian 1 MPT 2.4.2
    story.append(he.build_intermediate_equation(
        "Thay biểu thức mật độ dòng toàn phần gồm thành phần cuốn và khuếch tán vào phương trình liên tục lỗ trống:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển đạo hàm tích số mật độ dòng:",
        r"J_p = q p \mu_p E - q D_p \frac{\partial p}{\partial x} \implies -\frac{1}{q} \frac{\partial J_p}{\partial x} = -\mu_p \frac{\partial (p E)}{\partial x} + D_p \frac{\partial^2 p}{\partial x^2} = -\mu_p E \frac{\partial p}{\partial x} - \mu_p p \frac{\partial E}{\partial x} + D_p \frac{\partial^2 p}{\partial x^2}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.4.2
    story.append(he.build_intermediate_equation(
        "Áp dụng điều kiện tiêm mức thấp LLI và giả trung hòa điện tích để triệt tiêu số hạng đạo hàm điện trường:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điền tốc độ tái hợp ròng tuyến tính hóa theo thời gian sống hạt tải thiểu số <i>&tau;</i><sub>p</sub>:",
        r"\frac{\partial E}{\partial x} \approx 0 \implies \frac{\partial p_n}{\partial t} = D_p \frac{\partial^2 p_n}{\partial x^2} - \mu_p E \frac{\partial p_n}{\partial x} - \frac{p_n - p_{n0}}{\tau_p} + G_L",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.4.2
    story.append(he.build_intermediate_equation(
        "Thiết lập phương trình liên tục đối ngẫu cho electron thiểu số trong bán dẫn loại p (<i>n</i><sub>p</sub>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đổi dấu số hạng trôi dạt do electron mang điện tích âm &minus;<i>q</i>:",
        r"\frac{\partial n_p}{\partial t} = D_n \frac{\partial^2 n_p}{\partial x^2} + \mu_n E \frac{\partial n_p}{\partial x} - \frac{n_p - n_{p0}}{\tau_n} + G_L, \qquad L_n = \sqrt{D_n \tau_n}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Ý nghĩa vật lý quyết định của chiều dài khuếch tán <i>L</i><sub>p</sub> và <i>L</i><sub>n</sub>: Đại lượng <i>L</i> đại diện cho căn bậc hai của tích <i>D&tau;</i>, có thứ nguyên chiều dài (cm hoặc &mu;m), "
        "đại diện cho khoảng cách bình quân mà một hạt tải thiểu số có thể tự do khuếch tán xuyên qua mạng tinh thể trước khi gặp hạt tải đa số và bị tiêu diệt hoàn toàn bởi tái hợp. "
        "Trong chất bán dẫn Silic đơn tinh thể chất lượng cao, với <i>D</i><sub>p</sub> &asymp; 12 cm<sup>2</sup>/s và <i>&tau;</i><sub>p</sub> &asymp; 100 &mu;s, "
        "chiều dài khuếch tán đạt giá trị khổng lồ <i>L</i><sub>p</sub> &asymp; 346 &mu;m (lớn hơn cả bề dày thông thường của một phiến wafer 150 &mu;m!). "
        "Nếu tinh thể bị ô nhiễm kim loại nặng khiến <i>&tau;</i><sub>p</sub> tụt xuống cỡ 1 ns, <i>L</i><sub>p</sub> co rút thảm hại xuống chỉ còn 1 &mu;m, "
        "khiến hạt tải quang sinh bị tiêu diệt cục bộ ngay tại chỗ sinh ra và không thể đóng góp vào dòng điện ngoài."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.4.3: BÀI TOÁN TIÊM TĨNH TẠI VÀ ĐỘNG HỌC KHUẾCH TÁN
    # =========================================================================
    add_p("Luận điểm 2.4.3: Bài toán biên kinh điển: Tiêm hạt tải tĩnh tại từ một phía và động học khuếch tán suy giảm hàm mũ", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Một trong những cấu hình hình học kinh điển và quan trọng bậc nhất trong vật lý bán dẫn là bài toán tiêm hạt tải tĩnh tại từ một phía (Steady-state Injection). "
        "Xét một thanh bán dẫn loại n bán vô hạn chiếm nửa không gian <i>x</i> &ge; 0. "
        "Tại bề mặt <i>x</i> = 0, ta duy trì liên tục một nồng độ hạt tải thiểu số dư &Delta;<i>p</i><sub>n</sub>(0) cố định "
        "(được tạo ra nhờ chiếu sáng bề mặt liên tục bằng chùm photon có năng lượng <i>h&nu;</i> &gt; <i>E</i><sub>g</sub> bị hấp thụ mạnh ngay lớp ngoài cùng, "
        "hoặc bằng cách phân cực thuận một tiếp giáp p-n đặt tại <i>x</i> = 0). "
        "Bên trong khối bán dẫn (<i>x</i> &gt; 0), không có kích thích quang trong khối (<i>G</i><sub>L</sub> = 0) và không đặt điện trường ngoài (<i>E</i> = 0).<br/>"
        "↳ Động học khuếch tán dừng thuần túy: Hạt tải dư chỉ chuyển động khuếch tán sang phải dưới tác dụng của gradient nồng độ và đồng thời bị tiêu diệt bởi tái hợp nhiệt."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý dòng khuếch tán suy giảm và định luật bảo toàn điện tích: Khi hạt tải khuếch tán từ <i>x</i> = 0 vào sâu bên trong khối bán dẫn, "
        "mật độ dòng khuếch tán <i>J</i><sub>p</sub>(<i>x</i>) = &minus;<i>qD</i><sub>p</sub>(d<i>p</i>/d<i>x</i>) liên tục suy giảm dần theo hàm mũ và triệt tiêu hoàn toàn khi <i>x</i> &rarr; &infin;. "
        "Câu hỏi đặt ra: Dòng điện đi vào tại <i>x</i> = 0 đã biến đi đâu? "
        "Liệu định luật bảo toàn dòng điện Kirchoff có bị vi phạm hay không? "
        "Câu trả lời nằm ở sự chuyển giao giữa dòng hạt tải thiểu số và dòng hạt tải đa số: "
        "Mỗi khi một lỗ trống thiểu số khuếch tán bị tái hợp với một electron đa số, một electron từ cực ngoài của mạch phải chạy vào để bù lại electron đã mất, "
        "tạo nên một dòng cuốn electron đa số tăng dần chính xác bằng lượng suy giảm của dòng khuếch tán lỗ trống. "
        "Tổng mật độ dòng điện toàn phần <i>J</i><sub>total</sub> = <i>J</i><sub>p</sub>(<i>x</i>) + <i>J</i><sub>n</sub>(<i>x</i>) luôn là một hằng số tuyệt đối tại mọi tọa độ <i>x</i>!"
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_4_3 = [
        ("Nồng độ lỗ trống dư bề mặt", "&Delta;<i>p</i><sub>n</sub>(0)", "cm<sup>-3</sup>", "Mật độ hạt tải thiểu số dư duy trì cố định tại mặt tiếp xúc <i>x</i> = 0."),
        ("Nồng độ lỗ trống dư tại <i>x</i>", "&Delta;<i>p</i><sub>n</sub>(<i>x</i>)", "cm<sup>-3</sup>", "Nồng độ hạt tải thiểu số dư tại khoảng cách <i>x</i> so với mặt tiếp xúc."),
        ("Chiều dài khuếch tán", "<i>L</i><sub>p</sub>", "cm", "Khoảng cách đặc trưng để nồng độ hạt tải suy giảm đi e &asymp; 2,718 lần."),
        ("Mật độ dòng khuếch tán bề mặt", "<i>J</i><sub>p</sub>(0)", "A&middot;cm<sup>-2</sup>", "Mật độ dòng khuếch tán tiêm vào bán dẫn tại <i>x</i> = 0, tỷ lệ thuận với nồng độ hạt tải dư bề mặt &Delta;<i>p</i><sub>n</sub>(0) và căn bậc hai của thương số <i>D</i><sub>p</sub> trên <i>&tau;</i><sub>p</sub>."),
        ("Tổng điện tích tích tụ", "<i>Q</i><sub>p</sub>", "C", "Toàn bộ điện tích của các hạt tải thiểu số dư tích tụ trong thể tích thanh bán dẫn.")
    ]
    story.append(he.build_target_equation_block(
        r"D_p \frac{\mathrm{d}^2 \Delta p_n}{\mathrm{d}x^2} = \frac{\Delta p_n}{\tau_p} \implies \Delta p_n(x) = \Delta p_n(0) \exp\left(-\frac{x}{L_p}\right), \quad L_p = \sqrt{D_p \tau_p}",
        nom_rows_2_4_3,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một dải giấy thấm mực dài vô tận trải dài từ <i>x</i> = 0 sang bên phải. "
        "Tại đầu mép giấy <i>x</i> = 0, ta liên tục chấm một ngòi bút mực xanh với nồng độ mực đậm đặc không đổi (tiêm hạt tải &Delta;<i>p</i><sub>n</sub>(0)). "
        "Mực xanh khuếch tán mao dẫn loang dần sang bên phải qua các khe sợi giấy (hệ số khuếch tán <i>D</i><sub>p</sub>). "
        "Tuy nhiên, không khí phía trên giấy rất khô và nóng làm mực liên tục bay hơi khỏi mặt giấy với tốc độ tỷ lệ với nồng độ mực tại đó (thời gian sống <i>&tau;</i><sub>p</sub>). "
        "Sau một thời gian ngắn, vệt màu trên giấy đạt trạng thái dừng tĩnh tại: màu mực đậm nhất ở gốc <i>x</i> = 0 và nhạt dần đều theo quy luật hàm mũ, "
        "hoàn toàn biến mất sau một khoảng cách chừng vài lần chiều dài đặc trưng <i>L</i><sub>p</sub>."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Bước biến đổi trung gian 1 MPT 2.4.3
    story.append(he.build_intermediate_equation(
        "Thiết lập phương trình vi phân vi mô ở trạng thái dừng và tìm nghiệm tổng quát:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phương trình thuần nhất bậc hai hệ số hằng số:",
        r"\frac{\partial p_n}{\partial t} = 0, \quad E = 0, \quad G_L = 0 \implies \frac{\mathrm{d}^2 \Delta p_n}{\mathrm{d}x^2} - \frac{\Delta p_n}{L_p^2} = 0 \implies \Delta p_n(x) = C_1 \mathrm{e}^{-x/L_p} + C_2 \mathrm{e}^{x/L_p}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.4.3
    story.append(he.build_intermediate_equation(
        "Xác lập các điều kiện biên vật lý để loại bỏ nghiệm kỳ dị phân kỳ vô hạn:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điều kiện biên tại vô cực và bề mặt tiếp xúc:",
        r"x \to \infty \implies \Delta p_n(\infty) = 0 \implies C_2 = 0; \qquad x = 0 \implies \Delta p_n(0) = C_1 \implies \Delta p_n(x) = \Delta p_n(0) \exp\left(-\frac{x}{L_p}\right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.4.3
    story.append(he.build_intermediate_equation(
        "Dẫn xuất mật độ dòng khuếch tán và tích phân tổng điện tích tích tụ trong khối bán dẫn:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mối liên hệ cốt tử giữa dòng tiêm bề mặt và thời gian sống hạt tải:",
        r"J_p(x) = -q D_p \frac{\mathrm{d} \Delta p_n}{\mathrm{d}x} = \frac{q D_p \Delta p_n(0)}{L_p} \mathrm{e}^{-x/L_p} \implies Q_p = q A \int_0^\infty \Delta p_n(x) \mathrm{d}x = q A \Delta p_n(0) L_p = I_p(0) \tau_p",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.4.1
    story.append(he.embed_figure_with_caption(
        fig_sim_1,
        "Hình mô phỏng 2.4.1: Phân bố nồng độ hạt tải thiểu số khuếch tán dừng chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Phân bố trong phiến bán vô hạn <i>W</i> &gg; <i>L</i><sub>p</sub>: nồng độ suy giảm hàm mũ theo khoảng cách <i>x</i> với các chiều dài khuếch tán <i>L</i><sub>p</sub> = 15, 30, 60 &mu;m; "
        "(b) Đối chiếu phân bố trong phiến bazơ mỏng (<i>W</i>/<i>L</i><sub>p</sub> &le; 0,5: tiệm cận tuyến tính 1 &minus; <i>x</i>/<i>W</i>) và phiến bazơ dày (<i>W</i>/<i>L</i><sub>p</sub> &ge; 3,0: tiệm cận hàm mũ).",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát bài toán phiến mỏng bazơ ngắn (Narrow Base Diode) trong Tranzito lưỡng cực BJT: "
        "Nếu thanh bán dẫn không phải là bán vô hạn mà có bề dày hữu hạn <i>W</i> rất mỏng (<i>W</i> &ll; <i>L</i><sub>p</sub>), "
        "với điều kiện biên tiếp xúc Ohmic lý tưởng tại <i>x</i> = <i>W</i> hút sạch hạt tải dư (&Delta;<i>p</i><sub>n</sub>(<i>W</i>) = 0), "
        "nghiệm tổng quát của phương trình khuếch tán được biểu diễn qua tỷ số hai hàm sin hyperbolic của khoảng cách chuẩn hóa theo chiều dài khuếch tán.<br/>"
        "Khi <i>W</i> &ll; <i>L</i><sub>p</sub>, ta khai triển Taylor sinh(<i>u</i>) &asymp; <i>u</i> và thu được phân bố nồng độ suy giảm tuyến tính hoàn hảo theo tọa độ không gian. "
        "Gradient nồng độ d&Delta;<i>p</i>/d<i>x</i> trở thành một hằng số âm độc lập với <i>x</i>, "
        "và mật độ dòng khuếch tán qua vùng bazơ đạt giá trị không đổi, tỷ lệ nghịch với bề dày <i>W</i>. "
        "Hạt tải vượt qua bazơ mà hầu như không bị tái hợp (hiệu suất truyền bazơ &alpha;<sub>T</sub> tiến sát 100% khi tỷ số giữa bình phương bề dày bazơ và bình phương chiều dài khuếch tán tiến về 0), "
        "đây chính là nguyên lý vận hành cốt tử của cực gốc Tranzito BJT tốc độ cao."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.4.4: THÍ NGHIỆM HAYNES - SHOCKLEY
    # =========================================================================
    add_p("Luận điểm 2.4.4: Thí nghiệm Haynes &ndash; Shockley: Xác định đồng thời độ linh động, hệ số khuếch tán và thời gian sống", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Năm 1948 &ndash; 1951, tại phòng thí nghiệm Bell Labs, J. R. Haynes và William Shockley đã thiết kế một thí nghiệm kinh điển mang tính bước ngoặt, "
        "lần đầu tiên chứng minh trực tiếp bằng thực nghiệm sự tồn tại độc lập của các hạt mang điện thiểu số và đo lường trực quan chuyển động "
        "cuốn dạt, khuếch tán và tái hợp của chúng trong thanh bán dẫn đơn tinh thể Silic/Gecmani.<br/>"
        "↳ Thí nghiệm Haynes &ndash; Shockley: Kỹ thuật kích xung đo thời gian bay (Time-of-Flight &mdash; TOF) cho phép trích xuất độc lập đồng thời "
        "cả ba tham số chuyển vận cốt lõi: độ linh động &mu;, hệ số khuếch tán <i>D</i> và thời gian sống &tau; chỉ trong duy nhất một lần đo xung dao động ký."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý tốc độ trôi của xung hạt tải và độ linh động hạt tải đa số: Trong thanh bán dẫn loại n, phần lớn dòng điện dẫn được tải bởi electron đa số. "
        "Tuy nhiên, khi kích xung ánh sáng tạo cặp electron &ndash; lỗ trống, xung hạt tải đo được tại cực thu dao động ký lại di chuyển theo chiều điện trường "
        "với vận tốc cuốn <i>v</i><sub>d</sub> = &mu;<sub>p</sub><i>E</i> của lỗ trống thiểu số, chứ không phải chiều ngược lại của electron! "
        "Tại sao xung điện tích lại trôi theo vận tốc của hạt tải thiểu số? "
        "Nguyên nhân là do hiện tượng giả trung hòa điện tích: electron đa số bao quanh lỗ trống ngay lập tức, "
        "nhưng toàn bộ đám mây điện tích chỉ có thể di chuyển đồng bộ với tốc độ bị giới hạn bởi hạt tải thiểu số (hiện tượng chuyển vận tự phối Ambipolar Transport). "
        "Hạt tải thiểu số chính là kẻ cầm trịch quyết định vận tốc và hình dạng của xung tín hiệu thực nghiệm."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_4_4 = [
        ("Nồng độ lỗ trống trong xung", "&Delta;<i>p</i><sub>n</sub>(<i>x</i>, <i>t</i>)", "cm<sup>-3</sup>", "Mật độ lỗ trống phân bố theo không gian <i>x</i> và thời gian <i>t</i>."),
        ("Tổng số hạt tải tiêm ban đầu", "<i>N</i><sub>0</sub>", "cm<sup>-2</sup>", "Mật độ hạt tải thiểu số tức thời tạo ra tại <i>x</i> = 0 tại thời điểm xung kích thích <i>t</i> = 0."),
        ("Khoảng cách cực phát &ndash; cực thu", "<i>d</i>", "cm", "Khoảng cách cố định từ điểm tiêm hạt tải đến vị trí đặt đầu dò cực thu trên thanh bán dẫn."),
        ("Thời gian trôi đỉnh xung", "<i>t</i><sub>0</sub>", "s", "Thời điểm đỉnh xung Gaussian trôi đến cực dò, tỷ lệ thuận với cự ly <i>d</i> và tỷ lệ nghịch với vận tốc cuốn <i>v</i><sub>d</sub> = &mu;<sub>p</sub><i>E</i>."),
        ("Độ rộng xung tại nửa chiều cao", "&Delta;<i>t</i>", "s", "Khoảng thời gian đo giữa hai điểm có biên độ tín hiệu bằng một nửa đỉnh cực đại trên dao động ký.")
    ]
    story.append(he.build_target_equation_block(
        r"\Delta p_n(x, t) = \frac{N_0}{\sqrt{4 \pi D_p t}} \exp\left( -\frac{(x - \mu_p E t)^2}{4 D_p t} \right) \exp\left(-\frac{t}{\tau_p}\right)",
        nom_rows_2_4_4,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một chiếc xuồng máy chạy giữa một dòng sông nước chảy xiết với vận tốc dòng chảy &mu;<sub>p</sub><i>E</i>. "
        "Đúng thời điểm <i>t</i> = 0, người trên xuồng thả một giọt chất lỏng màu tím huỳnh quang cực kỳ đậm đặc xuống mặt sông tại tọa độ <i>x</i> = 0 (xung kích thích delta). "
        "Dòng nước cuốn trôi cả đám màu tím xuôi dòng với vận tốc trôi tịnh tiến của dòng sông (đỉnh xung dịch chuyển <i>x</i><sub>p</sub> = &mu;<sub>p</sub><i>E</i><i>t</i>). "
        "Đồng thời, sự khuấy động hỗn loạn của các phân tử nước làm giọt mực tím loang rộng dần ra theo dạng hình chuông Gaussian với độ rộng &sigma; tỷ lệ thuận với căn bậc hai của tích 2<i>D</i><sub>p</sub><i>t</i> (khuếch tán). "
        "Mặt khác, trong nước sông có chất khử làm phai nhạt dần màu tím theo hàm mũ thời gian sống &tau;<sub>p</sub> (tái hợp). "
        "Một trạm quan trắc đặt tại hạ lưu cách điểm thả một khoảng cách <i>d</i> sẽ ghi lại được chính xác biểu đồ tín hiệu màu tím đi qua theo thời gian."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.15
    story.append(he.embed_figure_with_caption(
        fig_goc_2_15,
        "Hình 2.15: Sơ đồ nguyên lý và đồ thị tín hiệu thí nghiệm Haynes &ndash; Shockley đo hiện tượng trôi và khuếch tán (Slide 17/25 HUST). "
        "Ba mắt xích vật lý: (a) Cực phát tiêm xung lỗ trống tại điểm bắt đầu; "
        "(b) Điện trường quét <i>E</i> kéo xung hạt tải trôi dạt định hướng về cực thu đồng thời khuếch tán giãn rộng; "
        "(c) Dạng sóng điện áp xung thu được trên màn hình dao động ký tại vị trí cực thu cách cực phát khoảng <i>d</i>.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.4.4
    story.append(he.build_intermediate_equation(
        "Giải phương trình liên tục phụ thuộc thời gian bằng hàm Green dưới điều kiện kích xung Dirac ban đầu &Delta;<i>p</i>(<i>x</i>, 0) = <i>N</i><sub>0</sub>&delta;(<i>x</i>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tách biến chuyển động trôi dạt của hệ tọa độ chuyển động <i>x</i>' = <i>x</i> &minus; &mu;<sub>p</sub><i>Et</i>:",
        r"\frac{\partial \Delta p}{\partial t} = D_p \frac{\partial^2 \Delta p}{\partial x^2} - \mu_p E \frac{\partial \Delta p}{\partial x} - \frac{\Delta p}{\tau_p} \implies \Delta p_n(x, t) = \frac{N_0}{\sqrt{4 \pi D_p t}} \exp\left[ -\frac{(x - \mu_p E t)^2}{4 D_p t} \right] \exp\left(-\frac{t}{\tau_p}\right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.4.4
    story.append(he.build_intermediate_equation(
        "Xác định độ linh động &mu;<sub>p</sub> từ thời gian trôi của đỉnh xung <i>t</i><sub>0</sub> qua khoảng cách <i>d</i>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đạo hàm triệt tiêu xác định vị trí cực trị đỉnh xung tại <i>x</i> = <i>d</i>:",
        r"d = \mu_p E t_0 \implies \mu_p = \frac{d}{E t_0} = \frac{d \cdot L}{V_0 t_0} \quad (\text{với } E = \frac{V_0}{L})",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.4.4
    story.append(he.build_intermediate_equation(
        "Xác định hệ số khuếch tán <i>D</i><sub>p</sub> từ độ rộng xung nửa chiều cao FWHM (&Delta;<i>t</i>) trên dao động ký:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập phương trình tại điểm biên độ bằng một nửa giá trị đỉnh cực đại:",
        r"\exp\left[ -\frac{\left(\mu_p E \frac{\Delta t}{2}\right)^2}{4 D_p t_0} \right] = \frac{1}{2} \implies \Delta t = \frac{4 \sqrt{\ln 2} \sqrt{D_p t_0}}{\mu_p E} \implies D_p = \frac{(\mu_p E)^2 (\Delta t)^2}{16 t_0 \ln 2} = \frac{(d \cdot \Delta t)^2}{16 t_0^3 \ln 2}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.4.2
    story.append(he.embed_figure_with_caption(
        fig_sim_2,
        "Hình mô phỏng 2.4.2: Động học xung Haynes &ndash; Shockley và tín hiệu điện áp cực thu chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Sự giãn rộng không gian và suy giảm biên độ của xung hạt tải theo tọa độ <i>x</i> tại các thời điểm <i>t</i> = 20, 40, 70, 100 &mu;s dưới điện trường <i>E</i> = 50 V/cm; "
        "(b) Tín hiệu điện áp cực thu <i>V</i><sub>out</sub> theo thời gian khi thay đổi điện trường quét <i>E</i> = 35, 50, 75 V/cm: điện trường càng lớn, thời gian bay <i>t</i><sub>0</sub> càng ngắn và xung càng nhọn.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các giới hạn tiệm cận và phương pháp xác định thời gian sống &tau;<sub>p</sub>: "
        "Diện tích dưới xung điện áp thu được trên dao động ký tỷ lệ thuận với tổng số hạt tải thiểu số còn sống sót tại thời điểm <i>t</i> "
        "và suy giảm theo quy luật hàm mũ thời gian sống. "
        "Bằng cách thay đổi điện áp phân cực <i>V</i><sub>0</sub> (thay đổi điện trường <i>E</i>), ta làm thay đổi thời gian bay <i>t</i><sub>0</sub> đến cực thu. "
        "Vẽ đồ thị logarit tự nhiên của diện tích xung ln[<i>A</i><sub>pulse</sub>] theo thời gian bay <i>t</i><sub>0</sub> sẽ thu được một đường thẳng có độ dốc xác định trực tiếp nghịch đảo thời gian sống <i>&tau;</i><sub>p</sub>, "
        "cho phép trích xuất thời gian sống &tau;<sub>p</sub> hoàn toàn độc lập với các hiệu ứng dãn rộng khuếch tán.<br/>"
        "Nếu điện trường quét triệt tiêu (<i>E</i> &rarr; 0), xung không trôi mà chỉ đứng yên tại chỗ và khuếch tán giãn rộng đối xứng ra hai phía. "
        "Nếu điện trường quét cực lớn (<i>E</i> &rarr; &infin;), thời gian bay <i>t</i><sub>0</sub> &rarr; 0, xung đến cực thu gần như nguyên vẹn mà không kịp bị dãn rộng khuếch tán hay suy giảm tái hợp."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI 5: THỬ THÁCH CHẨN ĐOÁN CER (HỘI TỤ CUỐI TỆP)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện và dự đoán lỗi sai kỹ thuật (Student Challenges & Error Anticipation)", "H2")
    add_spacer(4)
    add_p(
        "Khối thử thách chẩn đoán độc lập (Claim &ndash; Evidence &ndash; Reasoning): Bẫy điểm mù kỹ thuật thực chiến trong Lab và thiết kế quang điện tử. "
        "Học viên Bùi Trung Dũng tiếp nhận phân tích bản chất vi mô bằng nguyên lý đầu, tuyệt đối không đoán mò theo cảm tính."
    )
    add_spacer(6)
    
    # Ca chẩn đoán 1
    add_p(
        "<b>Ca chẩn đoán 2.4-A: Bẫy điểm mù trong thiết kế đi-ốt tiếp giáp p-n bazơ mỏng (Narrow-base Diode).</b><br/>"
        "Một kỹ sư phòng R&D thiết kế đi-ốt tiếp giáp p<sup>+</sup>-n công suất cao sử dụng vùng bazơ loại n có bề dày <i>W</i> = 10 &mu;m. "
        "Vật liệu Silic đơn tinh thể có thời gian sống lỗ trống <i>&tau;</i><sub>p</sub> = 25 &mu;s và hệ số khuếch tán <i>D</i><sub>p</sub> = 10 cm<sup>2</sup>/s. "
        "Kỹ sư tính toán chiều dài khuếch tán <i>L</i><sub>p</sub> = 158 &mu;m. "
        "Khi tính toán đặc tuyến dòng &ndash; áp tĩnh, kỹ sư áp dụng công thức kinh điển của Shockley cho đi-ốt bazơ dày "
        "với dòng bão hòa ngược tỷ lệ nghịch với chiều dài khuếch tán <i>L</i><sub>p</sub>. "
        "Tuy nhiên, khi đo thực tế trên phiến wafer, dòng điện thuận ghi nhận lớn gấp gần 16 lần so với giá trị tính toán lý thuyết!<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Sử dụng kiến thức phương trình liên tục và điều kiện biên bazơ mỏng (<i>W</i> &ll; <i>L</i><sub>p</sub>), "
        "hãy chỉ ra sai lầm cốt tử trong giả thiết tính toán của kỹ sư trên. "
        "Chứng minh tại sao phân bố nồng độ hạt tải biến đổi từ dạng suy giảm hàm mũ sang dạng suy giảm tuyến tính, "
        "dẫn xuất công thức chính xác cho mật độ dòng đi-ốt bazơ mỏng và giải thích nguyên nhân gây ra sự chênh lệch dòng điện khổng lồ trên.",
        "Body"
    )
    add_spacer(8)
    
    # Ca chẩn đoán 2
    add_p(
        "<b>Ca chẩn đoán 2.4-B: Bẫy điểm mù mức tiêm cao (HLI) trong thí nghiệm Haynes &ndash; Shockley làm sai lệch phép đo độ linh động.</b><br/>"
        "Trong một bài thực hành tại Lab Vật lý Bán dẫn, một nhóm sinh viên tiến hành thí nghiệm Haynes &ndash; Shockley trên thanh Silic loại n (<i>n</i><sub>n0</sub> = 10<sup>14</sup> cm<sup>-3</sup>). "
        "Để tín hiệu xung điện áp trên dao động ký hiện lên thật sắc nét và có biên độ lớn, nhóm sinh viên đã tăng cường độ xung laser kích thích ban đầu "
        "lên mức rất cao, tạo ra mật độ hạt tải tiêm ban đầu đạt &Delta;<i>p</i> &asymp; 5 &times; 10<sup>15</sup> cm<sup>-3</sup>. "
        "Kết quả đo thời gian bay <i>t</i><sub>0</sub> cho thấy độ linh động tính ra chỉ đạt &mu;<sub>p</sub> &asymp; 280 cm<sup>2</sup>/(V&middot;s), "
        "thấp hơn gần 40% so với giá trị chuẩn tra bảng của lỗ trống trong Silic (&mu;<sub>p</sub> &asymp; 450 cm<sup>2</sup>/(V&middot;s)). "
        "Báo cáo thực hành kết luận rằng mẫu Silic đã bị thoái hóa chất lượng nghiêm trọng.<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Sử dụng nguyên lý vận chuyển tự phối (Ambipolar Transport), hãy giải trình tại sao kết luận của nhóm sinh viên là hoàn toàn sai lầm? "
        "Phân tích cơ chế vi mô của điện trường tự phối nội tại sinh ra khi vi phạm điều kiện tiêm mức thấp LLI (&Delta;<i>p</i> &gt;&gt; <i>n</i><sub>n0</sub>). "
        "Tại sao ở mức tiêm cao, độ linh động của xung hạt tải không còn là &mu;<sub>p</sub> mà chuyển dịch về độ linh động tự phối &mu;<sub>a</sub> triệt tiêu về 0 do hiệu ứng giam giữ điện tích lưỡng cực? "
        "Đề xuất ngưỡng mật độ tiêm an toàn để bảo đảm phép đo Haynes &ndash; Shockley phản ánh chính xác độ linh động đơn hạt.",
        "Body"
    )
    add_spacer(8)
    
    # Khối Phản biện (Silent Drop)
    add_p(
        "<b>Khối Phản biện Nguyên lý Đầu (Silent Drop &mdash; Giảng viên kỳ cựu gửi Bùi Trung Dũng):</b><br/>"
        "Trong cơ học lượng tử, chuyển động của electron trong mạng tinh thể bán dẫn được chi phối bởi phương trình sóng Schrödinger đa hạt "
        "và phương trình động học vi mô Boltzmann với toán tử tán xạ phức tạp.<br/>"
        "↳ <i>Câu hỏi đối trọng:</i> Dưới những giả thiết vi mô nào (về thang chiều dài tán xạ <i>l</i><sub>mfp</sub>, thang thời gian tán xạ &tau;<sub>scat</sub> và thang năng lượng), "
        "phương trình động học lượng tử vi mô có thể hội tụ chính xác về phương trình liên tục dòng cuốn &ndash; khuếch tán vĩ mô dạng Fokker &ndash; Planck? "
        "Khi kích thước kênh dẫn của các bóng bán dẫn thế hệ mới (GAAFET, Nanosheet FET) bị thu hẹp xuống dưới 2 nm (nhỏ hơn quãng đường tự do trung bình của electron), "
        "những hiện tượng vật lý lượng tử nào (như vận chuyển đạn đạo Ballistic Transport, xuyên hầm lượng tử Quantum Tunneling) "
        "sẽ làm sụp đổ hoàn toàn mô hình phương trình liên tục cổ điển?",
        "Body"
    )
    add_spacer(14)
    
    # =========================================================================
    # XUẤT BẢN PDF VÀ KIỂM ĐỊNH COMPLIANCE GATE
    # =========================================================================
    print("Pre-flight build starting...")
    doc.build(story)
    print(f"SUCCESS: Generated {TARGET_PDF}")
    
    # Post-build assertion
    res = he.assert_monograph_compliance(TARGET_PDF, story, require_5_blocks=True, min_pages=10)
    print("POST-BUILD ASSERTION PASS 100%:", res)
    return TARGET_PDF

if __name__ == "__main__":
    build_monograph_muc_2_4()

# -*- coding: utf-8 -*-
"""
Builder Script for Monograph Muc 2.2: Chuyen_Khao_Ban_Dan_Muc_2.2.pdf
Subject: Vat ly va linh kien ban dan (PH3190 - HUST)
Chapter 2: Cac hien tuong van chuyen trong ban dan
Section 2.2: Hien tuong khuech tan hat dan (Carrier Diffusion)
Architecture: Full 5-Block Feynman Visual-First Core & Causal Flowchain (HUST Standard)
Strict Compliance:
  - Zero-Slash-Fractions via LaTeX Mathtext >= 300 DPI (Rule 14)
  - Flawless symbol & unit formatting in HTML (<i>...</i>, <sub>...</sub>, <sup>...</sup>)
  - Zero LaTeX leakage in Paragraphs / Tables (Rule 15)
  - 100% Zero-Omission of Slide Chapter 2 (Slide 15-18) & Sze / Neamen textbooks
  - All 3 Original Figures + 2 MATLAB Simulation Plots embedded
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
TARGET_PDF = os.path.join(BAI_GIANG_DIR, "Chuyen_Khao_Ban_Dan_Muc_2.2.pdf")

# Image assets
fig_goc_2_13 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.13_Co_che_dong_khuech_tan_hat_dan.png")
fig_goc_2_14 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.14_Phan_bo_nong_do_hat_dan_giam_tuyen_tinh.png")
fig_goc_2_15 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.15_Thi_nghiem_Haynes_Shockley_do_troi_khuech_tan.png")

fig_sim_1 = os.path.join(IMG_DIR, "[Mo_Phong]_He_thuc_Einstein_theo_T.png")
fig_sim_2 = os.path.join(IMG_DIR, "[Mo_Phong]_Xung_Haynes_Shockley_theo_thoi_gian.png")

def build_monograph_muc_2_2():
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
    add_p("Mục 2.2: Hiện tượng khuếch tán hạt dẫn trong bán dẫn", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Sze &amp; Ng — Physics of Semiconductor Devices, Chương 1.4 &amp; 2; Neamen — Semiconductor Physics and Devices, Chương 5)</i>", "Caption")
    add_spacer(4)
    
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Vật lý và linh kiện bán dẫn (PH3190)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Ch. 2 (Slide 15–18); Sze &amp; Ng Devices"), styles["TableCell"]),
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
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.2.1</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Cơ chế khuếch tán vi mô, gradient nồng độ hạt dẫn và định luật Fick thứ nhất trong bán dẫn"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 15–16<br/>Hình 2.13, 2.14 (Thí dụ 4)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.2.2</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Dẫn xuất toàn văn hệ thức Einstein từ trạng thái cân bằng nhiệt động nội tại và thế nhiệt"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 16<br/>Mô phỏng 2.1"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.2.3</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Phương trình mật độ dòng cuốn &ndash; khuếch tán toàn phần và hệ phương trình linh kiện bán dẫn"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 17–18<br/>Thí dụ 5"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.2.4</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Thí nghiệm Haynes-Shockley đo độ trôi, hệ số khuếch tán và thời gian sống hạt tải thiểu số"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 18<br/>Hình 2.15, Mô phỏng 2.2"), styles["TableCellCenter"])]
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
    # LUẬN ĐIỂM 2.2.1: CƠ CHẾ KHUẾCH TÁN VI MÔ & ĐỊNH LUẬT FICK THỨ NHẤT
    # =========================================================================
    add_p("Luận điểm 2.2.1: Cơ chế khuếch tán vi mô, gradient nồng độ hạt dẫn và định luật Fick thứ nhất trong bán dẫn", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Khuếch tán (Diffusion) là hiện tượng chuyển dời có hướng của các hạt mang điện (electron hoặc lỗ trống) từ vùng có nồng độ cao "
        "sang vùng có nồng độ thấp hơn, xuất phát từ chuyển động nhiệt ngẫu nhiên hỗn loạn của các hạt và sự chênh lệch về xác suất va chạm không gian, "
        "hoàn toàn không cần sự hiện diện của điện trường ngoài.<br/>"
        "↳ Khuếch tán hạt dẫn (Carrier Diffusion): Dòng chuyển dịch vật chất vi mô điều khiển thuần túy bởi entropy nhiệt động và gradient mật độ hạt.<br/>"
        "Trong tinh thể bán dẫn ở nhiệt độ phòng <i>T</i> = 300 K, các hạt dẫn liên tục chuyển động nhiệt với vận tốc nhiệt vi mô trung bình "
        "<i>v</i><sub>th</sub> xấp xỉ 10<sup>7</sup> cm&middot;s<sup>-1</sup> và va chạm liên tiếp với các phonon mạng tinh thể sau thời gian tự do trung bình "
        "<i>&tau;</i><sub>c</sub> xấp xỉ 10<sup>-13</sup> s, tạo nên cự ly tự do trung bình <i>l</i> xấp xỉ 10 &minus; 100 nm."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý dòng điện trong môi trường không điện trường: Theo định luật Ohm cổ điển, dòng điện chỉ có thể sinh ra khi có điện trường "
        "tác dụng lực lên điện tích (<i>J</i> = &sigma;<i>E</i>). Nếu đặt <i>E</i> = 0, định luật Ohm dự đoán dòng điện bắt buộc phải triệt tiêu. "
        "Tuy nhiên, trong một phiến bán dẫn có nồng độ tạp chất pha không đều hoặc đang được chiếu sáng cục bộ, một dòng điện khổng lồ lên tới hàng chục ampe "
        "trên mỗi centimet vuông vẫn có thể chảy qua mẫu ngay cả khi điện trường nội tại triệt tiêu hoàn toàn. "
        "Động lực thúc đẩy dòng điện này không phải là lực cơ học hay lực điện trường, mà là xu hướng tự nhiên của hệ nhiệt động nhằm cực đại hóa entropy "
        "thông qua sự san phẳng gradient nồng độ hạt dẫn."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_2_1 = [
        ("Mật độ dòng khuếch tán electron", "<i>J</i><sub><i>n</i>,diff</sub>", "A&middot;cm<sup>-2</sup>", "Dòng điện sinh ra do gradient nồng độ electron, cùng chiều với vector gradient."),
        ("Mật độ dòng khuếch tán lỗ trống", "<i>J</i><sub><i>p</i>,diff</sub>", "A&middot;cm<sup>-2</sup>", "Dòng điện sinh ra do gradient nồng độ lỗ trống, ngược chiều với vector gradient."),
        ("Hệ số khuếch tán electron", "<i>D</i><sub>n</sub>", "cm<sup>2</sup>&middot;s<sup>-1</sup>", "Khả năng lan truyền vi mô của electron trong mạng tinh thể (khoảng 35 cm<sup>2</sup>&middot;s<sup>-1</sup> trong Si ở 300 K)."),
        ("Hệ số khuếch tán lỗ trống", "<i>D</i><sub>p</sub>", "cm<sup>2</sup>&middot;s<sup>-1</sup>", "Khả năng lan truyền vi mô của lỗ trống trong mạng tinh thể (khoảng 12 cm<sup>2</sup>&middot;s<sup>-1</sup> trong Si ở 300 K)."),
        ("Gradient nồng độ hạt tải", "d<i>n</i>/d<i>x</i>", "cm<sup>-4</sup>", "Độ dốc phân bố mật độ hạt dẫn theo tọa độ không gian 1 chiều.")
    ]
    story.append(he.build_target_equation_block(
        r"J_{n,\mathrm{diff}} = q D_n \frac{\mathrm{d}n}{\mathrm{d}x}, \quad J_{p,\mathrm{diff}} = -q D_p \frac{\mathrm{d}p}{\mathrm{d}x}",
        nom_rows_2_2_1,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một phòng họp lớn ngăn đôi bởi một vách ngăn vô hình ở giữa phòng. "
        "Bên trái phòng nhồi nhét 1000 người say rượu đang nhảy múa loạn xạ không định hướng (vùng nồng độ cao), trong khi bên phải chỉ có 10 người (vùng nồng độ thấp). "
        "Mỗi bước nhảy của mỗi người hoàn toàn ngẫu nhiên sang trái hoặc sang phải với xác suất ngang nhau 50%. "
        "Tuy nhiên, vì số người nhảy ở bên trái quá đông, số lượng người vô tình bước qua vách ngăn sang bên phải sẽ áp đảo hoàn toàn số người từ bên phải bước sang bên trái. "
        "Kết quả là xuất hiện một luồng người di cư khổng lồ chảy từ trái sang phải mà không cần bất kỳ một người bảo vệ nào đẩy từ phía sau. "
        "Nếu những người này mang trên lưng một quả bóng tích điện âm (electron), dòng dịch chuyển người sang phải sẽ tạo nên một dòng điện quy ước chạy ngược lại sang trái."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.13
    story.append(he.embed_figure_with_caption(
        fig_goc_2_13,
        "Hình 2.13: Cơ chế vi mô của dòng khuếch tán hạt dẫn qua mặt phẳng tham chiếu dưới chuyển động nhiệt ngẫu nhiên (Slide 15 HUST). "
        "Ba mắt xích vật lý: (a) Mặt phẳng tham chiếu quy ước tại <i>x</i> = 0; "
        "(b) Hạt tải xuất phát từ cự ly tự do trung bình <i>l</i> ở hai phía chuyển động hỗn loạn; "
        "(c) Sự chênh lệch nồng độ <i>n</i>(-<i>l</i>) &gt; <i>n</i>(+<i>l</i>) tạo nên thông lượng dòng hạt thuần nhất có hướng sang phải.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.2.1
    story.append(he.build_intermediate_equation(
        "Dẫn xuất vi mô định luật Fick thứ nhất từ cự ly tự do trung bình <i>l</i> và vận tốc nhiệt <i>v</i><sub>th</sub>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển Taylor nồng độ hạt tại hai vị trí cách mặt phẳng <i>x</i> = 0 một khoảng <i>l</i>:",
        r"F_n = \frac{1}{2} v_{\mathrm{th}} n(-l) - \frac{1}{2} v_{\mathrm{th}} n(+l) \approx \frac{1}{2} v_{\mathrm{th}} \left[ \left( n(0) - l \frac{\mathrm{d}n}{\mathrm{d}x} \right) - \left( n(0) + l \frac{\mathrm{d}n}{\mathrm{d}x} \right) \right] = -v_{\mathrm{th}} l \frac{\mathrm{d}n}{\mathrm{d}x} = -D_n \frac{\mathrm{d}n}{\mathrm{d}x}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình 2.14
    story.append(he.embed_figure_with_caption(
        fig_goc_2_14,
        "Hình 2.14: Phân bố nồng độ hạt dẫn giảm tuyến tính theo không gian trong thanh bán dẫn Silic (Slide 15 HUST). "
        "Ba mắt xích vật lý: (a) Nồng độ cực đại <i>n</i>(0) = 10<sup>16</sup> cm<sup>-3</sup> tại mặt trái <i>x</i> = 0; "
        "(b) Nồng độ triệt tiêu <i>n</i>(<i>W</i>) = 0 tại mặt phải <i>x</i> = <i>W</i> = 10 &mu;m; "
        "(c) Gradient nồng độ không đổi d<i>n</i>/d<i>x</i> âm dẫn đến dòng khuếch tán không đổi dọc theo mẫu.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    add_p(
        "Dẫn xuất giải tích và tính toán định lượng chi tiết cho Bài tập Thí dụ 4 (Slide 15 &ndash; 16 HUST): "
        "Một thanh bán dẫn Silic có phân bố nồng độ electron suy giảm tuyến tính như Hình 2.14, với <i>n</i>(0) = 10<sup>16</sup> cm<sup>-3</sup> tại <i>x</i> = 0 "
        "và <i>n</i>(<i>W</i>) = 0 tại <i>x</i> = <i>W</i> = 10 &mu;m. Giả thiết hệ số khuếch tán electron <i>D</i><sub>n</sub> = 35 cm<sup>2</sup>&middot;s<sup>-1</sup> ở nhiệt độ phòng 300 K. "
        "Xác định gradient nồng độ electron d<i>n</i>/d<i>x</i> và mật độ dòng điện khuếch tán electron <i>J</i><sub>n</sub>."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.2.1
    story.append(he.build_intermediate_equation(
        "Tính toán gradient nồng độ electron không gian d<i>n</i>/d<i>x</i> trong thanh Silic bề dày <i>W</i> = 10 &mu;m = 10<sup>-3</sup> cm:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Độ dốc nồng độ âm phản ánh sự suy giảm mật độ hạt theo chiều dương trục <i>x</i>:",
        r"\frac{\mathrm{d}n}{\mathrm{d}x} = \frac{n(W) - n(0)}{W} = \frac{0 - 10^{16}\ \mathrm{cm}^{-3}}{10 \times 10^{-4}\ \mathrm{cm}} = -10^{19}\ \mathrm{cm}^{-4}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.2.1
    story.append(he.build_intermediate_equation(
        "Tính toán mật độ thông lượng hạt electron <i>F</i><sub>n</sub> và mật độ dòng điện khuếch tán <i>J</i><sub>n</sub>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nhân thông lượng hạt với điện tích electron -<i>q</i>:",
        r"J_n = q D_n \frac{\mathrm{d}n}{\mathrm{d}x} = (1,602 \times 10^{-19}\ \mathrm{C}) \times (35\ \mathrm{cm}^2\cdot\mathrm{s}^{-1}) \times (-10^{19}\ \mathrm{cm}^{-4}) \approx -56,07\ \mathrm{A}\cdot\mathrm{cm}^{-2}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    add_p(
        "<b>Đối chuẩn số liệu mở rộng với Slide 16 HUST:</b> Trong một số tài liệu thí nghiệm của học phần PH3190, khi khảo sát mẫu Silic pha tạp nặng hơn "
        "làm tăng tán xạ Coulomb khiến hệ số khuếch tán suy giảm xuống <i>D</i><sub>n</sub> = 6,74 cm<sup>2</sup>&middot;s<sup>-1</sup> (tương ứng độ linh động "
        "<i>&mu;</i><sub>n</sub> xấp xỉ 260 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>), mật độ dòng khuếch tán tính ra là "
        "<i>J</i><sub>n</sub> = (1,602 &times; 10<sup>-19</sup>) &times; 6,74 &times; (&minus;10<sup>19</sup>) &asymp; &minus;10,8 A&middot;cm<sup>-2</sup>. "
        "Dấu âm khẳng định dòng điện có chiều hướng sang trái (ngược chiều dòng hạt electron di cư sang phải)."
    )
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Dòng khuếch tán là trái tim điều khiển mọi linh kiện bán dẫn có tiếp giáp p-n (Diode, BJT, Solar Cell, Laser Diode). "
        "Khi tiếp giáp p-n được phân cực thuận bởi điện áp ngoài <i>V</i><sub>a</sub>, hàng rào thế năng vùng nghèo bị hạ thấp, hạt tải đa số từ hai phía "
        "tràn qua trở thành hạt tải thiểu số. Tại mép vùng nghèo, gradient nồng độ hạt tải thiểu số đạt giá trị khổng lồ làm phát sinh dòng khuếch tán "
        "(gọi là dòng phun thiểu số &mdash; minority carrier injection). "
        "Chính dòng khuếch tán này quyết định đặc tuyến dòng thế phi tuyến kinh điển <i>I</i> = <i>I</i><sub>0</sub> [exp(<i>qV</i>/<i>k</i><sub>B</sub><i>T</i>) &minus; 1] "
        "của Diode và điều khiển hoàn toàn dòng cực thu <i>I</i><sub>C</sub> trong transistor lưỡng cực BJT khi các electron khuếch tán qua lớp bazơ siêu mỏng."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.2.2: DẪN XUẤT TOÀN VĂN HỆ THỨC EINSTEIN
    # =========================================================================
    add_p("Luận điểm 2.2.2: Dẫn xuất toàn văn hệ thức Einstein từ trạng thái cân bằng nhiệt động nội tại và thế nhiệt", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Hệ thức Einstein (Einstein Relation) là một trong những định luật nền tảng và đẹp đẽ nhất của vật lý chất rắn, "
        "thiết lập mối liên hệ trực tiếp giữa hệ số khuếch tán <i>D</i> (đặc trưng cho chuyển động nhiệt entropic không trật tự) "
        "và độ linh động <i>&mu;</i> (đặc trưng cho chuyển động cuốn định hướng dưới tác dụng của lực điện trường).<br/>"
        "↳ Hệ thức Einstein (Einstein Relation): Cầu nối nhiệt động học giữa quá trình tán xạ động lực học và quá trình khuếch tán thống kê.<br/>"
        "Xét một khối bán dẫn có nồng độ pha tạp thay đổi theo không gian, đặt trong môi trường cô lập ở trạng thái cân bằng nhiệt tuyệt đối (không có nguồn cấp ngoài, không chiếu sáng). "
        "Ở cân bằng nhiệt, mức năng lượng Fermi <i>E</i><sub>F</sub> phải nằm ngang phẳng tuyệt đối trên toàn bộ không gian (d<i>E</i><sub>F</sub>/d<i>x</i> = 0)."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý cân bằng dòng điện độc lập: Vì nồng độ hạt dẫn thay đổi theo không gian, gradient nồng độ liên tục thúc đẩy dòng khuếch tán <i>J</i><sub>diff</sub> &ne; 0. "
        "Nếu dòng này cứ tiếp tục chảy, điện tích sẽ bị dồn ứ vô tận về một đầu mẫu. "
        "Để duy trì trạng thái cân bằng nhiệt động bền vững, sự dịch chuyển điện tích ban đầu sẽ tự động thiết lập một điện trường tĩnh điện nội tại <i>E</i><sub>int</sub>. "
        "Điện trường này sinh ra một dòng cuốn <i>J</i><sub>drift</sub> có độ lớn bằng đúng dòng khuếch tán nhưng ngược chiều hoàn hảo, "
        "khiến dòng điện toàn phần triệt tiêu chính xác tại mọi tọa độ không gian vi mô: <i>J</i><sub>n</sub>(<i>x</i>) = 0 và <i>J</i><sub>p</sub>(<i>x</i>) = 0."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_2_2 = [
        ("Tỷ số Einstein electron", "<i>D</i><sub>n</sub> / <i>&mu;</i><sub>n</sub>", "V", "Tỷ số giữa hệ số khuếch tán và độ linh động của electron, bằng đúng thế nhiệt <i>V</i><sub>t</sub>."),
        ("Tỷ số Einstein lỗ trống", "<i>D</i><sub>p</sub> / <i>&mu;</i><sub>p</sub>", "V", "Tỷ số giữa hệ số khuếch tán và độ linh động của lỗ trống, bằng đúng thế nhiệt <i>V</i><sub>t</sub>."),
        ("Thế nhiệt (Thermal Voltage)", "<i>V</i><sub>t</sub>", "V", "Điện thế nhiệt động học quy đổi <i>k</i><sub>B</sub><i>T</i>/<i>q</i> (khoảng 25,86 mV ở nhiệt độ phòng 300 K)."),
        ("Hằng số Boltzmann", "<i>k</i><sub>B</sub>", "J&middot;K<sup>-1</sup>", "Hằng số nhiệt động lực học cơ bản (1,380649 &times; 10<sup>-23</sup> J&middot;K<sup>-1</sup>)."),
        ("Điện tích nguyên tố", "<i>q</i>", "C", "Độ lớn điện tích của electron (1,602176634 &times; 10<sup>-19</sup> C).")
    ]
    story.append(he.build_target_equation_block(
        r"\frac{D_n}{\mu_n} = \frac{D_p}{\mu_p} = \frac{k_{\mathrm{B}} T}{q} = V_t",
        nom_rows_2_2_2,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng bầu khí quyển Trái Đất bao quanh chúng ta. "
        "Lực hấp dẫn của Trái Đất liên tục kéo các phân tử không khí rơi xuống mặt đất (tương tự lực điện trường kéo dòng cuốn <i>J</i><sub>drift</sub>). "
        "Tuy nhiên, nếu chỉ có lực hấp dẫn, toàn bộ không khí đã bị nén bẹp thành một lớp mỏng dính vài milimet trên mặt đất. "
        "Sự chuyển động nhiệt ngẫu nhiên của các phân tử không khí liên tục thúc đẩy chúng khuếch tán ngược lên cao về phía chân không vũ trụ (tương tự dòng khuếch tán <i>J</i><sub>diff</sub>). "
        "Tại trạng thái cân bằng khí quyển, hai xu hướng này triệt tiêu lẫn nhau hoàn hảo, tạo ra một phân bố áp suất khí quyển suy giảm theo hàm số mũ theo độ cao. "
        "Độ cao đặc trưng của bầu khí quyển chính là thước đo nhiệt độ, giống hệt như thế nhiệt <i>V</i><sub>t</sub> = <i>k</i><sub>B</sub><i>T</i>/<i>q</i> trong tinh thể bán dẫn."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Dẫn xuất toàn văn giải tích hệ thức Einstein từ nguyên lý đầu (Zero-Skipped-Steps): "
        "Thiết lập trạng thái triệt tiêu mật độ dòng điện electron toàn phần tại mọi điểm không gian ở cân bằng nhiệt:"
    )
    add_spacer(4)
    
    # Bước biến đổi trung gian 1 MPT 2.2.2
    story.append(he.build_intermediate_equation(
        "Điều kiện cân bằng động học giữa dòng cuốn và dòng khuếch tán của electron:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tổng mật độ dòng điện electron triệt tiêu đồng nhất tại mọi vị trí <i>x</i>:",
        r"J_n(x) = J_{n,\mathrm{drift}}(x) + J_{n,\mathrm{diff}}(x) = q n(x) \mu_n \mathcal{E}(x) + q D_n \frac{\mathrm{d}n(x)}{\mathrm{d}x} = 0",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.2.2
    story.append(he.build_intermediate_equation(
        "Đạo hàm không gian nồng độ electron theo phân bố Maxwell-Boltzmann và liên hệ đáy vùng dẫn <i>E</i><sub>c</sub>(<i>x</i>) với điện trường:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Sử dụng điều kiện mức Fermi phẳng d<i>E</i><sub>F</sub>/d<i>x</i> = 0 và d<i>E</i><sub>c</sub>/d<i>x</i> = <i>qE</i>:",
        r"\frac{\mathrm{d}n}{\mathrm{d}x} = \frac{\mathrm{d}}{\mathrm{d}x} \left[ N_c \exp\left(-\frac{E_c(x) - E_F}{k_{\mathrm{B}} T}\right) \right] = -n(x) \frac{1}{k_{\mathrm{B}} T} \frac{\mathrm{d}E_c}{\mathrm{d}x} = -\frac{q n(x) \mathcal{E}(x)}{k_{\mathrm{B}} T}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.2.2
    story.append(he.build_intermediate_equation(
        "Thay thế đạo hàm nồng độ vào phương trình cân bằng dòng và triệt tiêu các đại lượng khác không:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khẳng định hệ thức Einstein độc lập với cường độ điện trường và nồng độ pha tạp:",
        r"q n(x) \mu_n \mathcal{E}(x) + q D_n \left( -\frac{q n(x) \mathcal{E}(x)}{k_{\mathrm{B}} T} \right) = 0 \implies q n \mathcal{E} \left( \mu_n - \frac{q D_n}{k_{\mathrm{B}} T} \right) = 0 \implies \frac{D_n}{\mu_n} = \frac{k_{\mathrm{B}} T}{q}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.1
    story.append(he.embed_figure_with_caption(
        fig_sim_1,
        "Hình mô phỏng 2.1: Đặc tuyến giải tích hệ thức Einstein theo nhiệt độ và nồng độ tạp chất chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Tỷ số Einstein <i>D</i>/<i>&mu;</i> tăng tuyến tính theo nhiệt độ tuyệt đối <i>T</i> với độ dốc <i>k</i><sub>B</sub>/<i>q</i> = 86,17 &mu;V/K, "
        "đạt giá trị chuẩn 25,86 mV tại 300 K; "
        "(b) Hệ số khuếch tán <i>D</i><sub>n</sub> và <i>D</i><sub>p</sub> của Silicon ở 300 K theo nồng độ tạp chất: "
        "hệ số khuếch tán sụt giảm mạnh khi nồng độ pha tạp vượt quá 10<sup>16</sup> cm<sup>-3</sup> do tán xạ ion tạp chất Coulomb chiếm ưu thế.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Giới hạn suy biến Fermi-Dirac trong cấu trúc bán dẫn nanomet: Trong các lớp bán dẫn pha tạp cực nặng (Degenerate Semiconductors) "
        "với mật độ hạt dẫn vượt quá mật độ trạng thái hiệu dụng (<i>n</i> &gt; <i>N</i><sub>c</sub> &asymp; 2,8 &times; 10<sup>19</sup> cm<sup>-3</sup> trong Si), "
        "mức Fermi nằm sâu bên trong vùng dẫn, nguyên lý loại trừ Pauli bắt đầu chi phối và phân bố Boltzmann cổ điển không còn hiệu lực. "
        "Khi đó, hệ thức Einstein mở rộng phải được biểu diễn qua tích phân Fermi-Dirac:"
    )
    add_spacer(4)
    story.append(he.build_intermediate_equation(
        "Hệ thức Einstein tổng quát hóa cho bán dẫn suy biến nồng độ cao qua đạo hàm năng lượng Fermi:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tỷ số Einstein suy biến luôn lớn hơn giá trị nhiệt động cổ điển:",
        r"\frac{D_n}{\mu_n} = \frac{n}{q \frac{\mathrm{d}n}{\mathrm{d}E_F}} = \frac{k_{\mathrm{B}} T}{q} \frac{\mathcal{F}_{1/2}(\eta)}{\mathcal{F}_{-1/2}(\eta)} > \frac{k_{\mathrm{B}} T}{q}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    add_p(
        "Trong thiết kế vi mạch tích hợp cao tần và các linh kiện quang tử dị thể (Heterostructure Lasers, HEMT), "
        "sự gia tăng của tỷ số Einstein trong vùng suy biến làm tăng tốc độ khuếch tán hạt dẫn vượt bậc, "
        "rút ngắn thời gian chuyển mạch của cổng logic xuống dải picogiây nhưng đồng thời làm gia tăng dòng rò khuếch tán qua các rào thế tiếp xúc."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.2.3: PHƯƠNG TRÌNH MẬT ĐỘ DÒNG TOÀN PHẦN
    # =========================================================================
    add_p("Luận điểm 2.2.3: Phương trình mật độ dòng cuốn &ndash; khuếch tán toàn phần và hệ phương trình linh kiện bán dẫn", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong mọi linh kiện bán dẫn thực tế vận hành dưới điều kiện phân cực hoặc chiếu sáng, hai hiện tượng vận chuyển "
        "chuyển động cuốn định hướng (Drift) và chuyển động khuếch tán entropic (Diffusion) luôn diễn ra đồng thời và tương tác mật thiết với nhau.<br/>"
        "↳ Dòng cuốn &ndash; khuếch tán toàn phần (Total Drift-Diffusion Current): Sự hợp nhất của lực điện trường Coulomb và lực thống kê nồng độ.<br/>"
        "Dòng điện toàn phần chạy qua một tiết diện bán dẫn là tổng đại số của dòng cuốn và dòng khuếch tán đóng góp bởi cả electron trong vùng dẫn "
        "và lỗ trống trong vùng hóa trị."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý độc lập của hai thành phần dòng: Dòng cuốn đòi hỏi điện trường <i>E</i> nhưng không phụ thuộc vào độ dốc nồng độ, "
        "trong khi dòng khuếch tán đòi hỏi gradient d<i>n</i>/d<i>x</i> nhưng không phụ thuộc trực tiếp vào điện trường. "
        "Tuy nhiên, hai dòng này không thể phân tách biệt lập: sự dịch chuyển của dòng khuếch tán làm thay đổi mật độ điện tích không gian &rho;(<i>x</i>), "
        "từ đó làm biến đổi điện trường <i>E</i> thông qua phương trình Poisson. "
        "Ngược lại, điện trường cuốn làm biến dạng profile phân bố nồng độ, làm thay đổi gradient khuếch tán. "
        "Sự đan xen phi tuyến phức tạp này là nguồn gốc tạo nên tính chất chỉnh lưu và khuếch đại tín hiệu kỳ diệu của chất bán dẫn."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_2_3 = [
        ("Mật độ dòng toàn phần", "<i>J</i><sub>total</sub>", "A&middot;cm<sup>-2</sup>", "Tổng đại số mật độ dòng cuốn và dòng khuếch tán của cả electron và lỗ trống."),
        ("Dòng electron toàn phần", "<i>J</i><sub>n</sub>", "A&middot;cm<sup>-2</sup>", "Dòng điện do electron dẫn đóng góp, gồm thành phần cuốn theo điện trường và khuếch tán theo gradient."),
        ("Dòng lỗ trống toàn phần", "<i>J</i><sub>p</sub>", "A&middot;cm<sup>-2</sup>", "Dòng điện do lỗ trống đóng góp, gồm thành phần cuốn theo điện trường và khuếch tán theo gradient."),
        ("Độ dẫn điện của bán dẫn", "&sigma;", "&Omega;<sup>-1</sup>&middot;cm<sup>-1</sup>", "Khả năng dẫn dòng cuốn của bán dẫn: &sigma; = <i>q</i>(<i>n&mu;</i><sub>n</sub> + <i>p&mu;</i><sub>p</sub>)."),
        ("Điện trường ngoài", "<i>E</i>", "V&middot;cm<sup>-1</sup>", "Cường độ điện trường tác dụng lực gia tốc định hướng lên hạt mang điện.")
    ]
    story.append(he.build_target_equation_block(
        r"J_{\mathrm{total}} = (q n \mu_n + q p \mu_p) \mathcal{E} + q \left( D_n \frac{\mathrm{d}n}{\mathrm{d}x} - D_p \frac{\mathrm{d}p}{\mathrm{d}x} \right)",
        nom_rows_2_2_3,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một đoàn người đang đi bộ trên một băng chuyền sân bay đang chạy. "
        "Vận tốc chuyển động của băng chuyền tương ứng với điện trường ngoài tác dụng lực cuốn (thành phần cuốn <i>J</i><sub>drift</sub>). "
        "Mỗi người trên băng chuyền lại tự do bước đi, chen lấn từ chỗ chen chúc sang chỗ thoáng người (thành phần khuếch tán <i>J</i><sub>diff</sub>). "
        "Vận tốc tuyệt đối của một người quan sát đứng bên ngoài nhìn vào bằng tổng vận tốc của băng chuyền cộng với vận tốc sải chân của người đó. "
        "Nếu người đó bước cùng chiều băng chuyền, hai dòng cộng hưởng; nếu người đó bước ngược chiều, hai dòng triệt tiêu lẫn nhau."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Dẫn xuất giải tích và tính toán định lượng chi tiết cho Bài tập Thí dụ 5 (Slide 17 HUST): "
        "Một xung ánh sáng cực hẹp tiêm một lượng lỗ trống thiểu số vào một thanh bán dẫn Silic loại n dài, "
        "chịu tác dụng của một điện trường ngoài không đổi <i>E</i> = 50 V&middot;cm<sup>-1</sup> dọc trục. "
        "Khoảng cách từ vị trí chiếu sáng tiêm hạt tải đến điện cực thu tín hiệu là <i>d</i> = 1 cm. "
        "Tín hiệu dao động ký đo được thời gian trôi của đỉnh xung lỗ trống đến cực thu là <i>t</i> = 100 &mu;s ở nhiệt độ <i>T</i> = 300 K. "
        "Xác định vận tốc cuốn <i>v</i><sub>d</sub>, độ linh động <i>&mu;</i><sub>p</sub> và áp dụng hệ thức Einstein để tính hệ số khuếch tán <i>D</i><sub>p</sub>."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.2.3
    story.append(he.build_intermediate_equation(
        "Tính toán vận tốc cuốn của đỉnh xung lỗ trống dọc theo chiều điện trường ngoài:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chuẩn hóa thời gian trôi <i>t</i> = 100 &mu;s = 10<sup>-4</sup> s:",
        r"v_d = \frac{d}{t} = \frac{1\ \mathrm{cm}}{100 \times 10^{-6}\ \mathrm{s}} = 10^4\ \mathrm{cm}\cdot\mathrm{s}^{-1} = 100\ \mathrm{m}\cdot\mathrm{s}^{-1}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.2.3
    story.append(he.build_intermediate_equation(
        "Tính toán độ linh động của lỗ trống thiểu số theo định nghĩa vận tốc cuốn trường yếu:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tỷ số giữa vận tốc trôi và cường độ điện trường <i>E</i> = 50 V&middot;cm<sup>-1</sup>:",
        r"\mu_p = \frac{v_d}{\mathcal{E}} = \frac{10^4\ \mathrm{cm}\cdot\mathrm{s}^{-1}}{50\ \mathrm{V}\cdot\mathrm{cm}^{-1}} = 200\ \mathrm{cm}^2\cdot\mathrm{V}^{-1}\cdot\mathrm{s}^{-1}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.2.3
    story.append(he.build_intermediate_equation(
        "Áp dụng hệ thức Einstein để xác định chính xác hệ số khuếch tán lỗ trống ở 300 K:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nhân độ linh động với thế nhiệt <i>V</i><sub>t</sub> = 0,02586 V:",
        r"D_p = \mu_p \left( \frac{k_{\mathrm{B}} T}{q} \right) = (200\ \mathrm{cm}^2\cdot\mathrm{V}^{-1}\cdot\mathrm{s}^{-1}) \times (0,02586\ \mathrm{V}) \approx 5,172\ \mathrm{cm}^2\cdot\mathrm{s}^{-1} \approx 5,18\ \mathrm{cm}^2\cdot\mathrm{s}^{-1}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Bộ phương trình vi phân Van Roosbroeck trong phần mềm mô phỏng TCAD: Phương trình mật độ dòng cuốn &ndash; khuếch tán toàn phần "
        "kết hợp với phương trình vi phân Poisson và phương trình liên tục bảo toàn hạt tạo thành hệ ba phương trình đạo hàm riêng Van Roosbroeck (1950) &mdash; "
        "nền tảng toán học tối thượng điều khiển mọi công cụ TCAD hiện đại (Synopsys Sentaurus, Silvaco Atlas):"
    )
    add_spacer(4)
    story.append(he.build_intermediate_equation(
        "Hệ ba phương trình đạo hàm riêng phi tuyến Van Roosbroeck chi phối phân bố điện thế và hạt tải trong linh kiện bán dẫn:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Kết hợp phương trình Poisson và phương trình bảo toàn dòng liên tục cho cả hai loại hạt tải:",
        r"\nabla^2 V = -\frac{q}{\varepsilon} (p - n + N_{\mathrm{D}}^+ - N_{\mathrm{A}}^-), \quad \frac{\partial n}{\partial t} = \frac{1}{q} \nabla \cdot \mathbf{J}_n + G_n - U_n, \quad \frac{\partial p}{\partial t} = -\frac{1}{q} \nabla \cdot \mathbf{J}_p + G_p - U_p",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    add_p(
        "Trong các cấu trúc transistor FinFET 3 nm và Gate-All-Around (GAA), việc giải đồng thời hệ phương trình này cho phép mô phỏng chính xác "
        "sự triệt tiêu dòng rò dưới ngưỡng (Subthreshold Leakage), hiện tượng hạ thấp rào thế cảm ứng do cực máng (DIBL) "
        "và tối ưu hóa độ dày màng mỏng quang học trong pin mặt trời dị thể đa tiếp giáp."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.2.4: THÍ NGHIỆM HAYNES-SHOCKLEY
    # =========================================================================
    add_p("Luận điểm 2.2.4: Thí nghiệm Haynes-Shockley đo độ trôi, hệ số khuếch tán và thời gian sống hạt tải thiểu số", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Thí nghiệm Haynes &ndash; Shockley (J. R. Haynes và W. Shockley, Bell Labs 1949 &ndash; 1951) là mốc son chói lọi trong lịch sử vật lý bán dẫn. "
        "Lần đầu tiên, sự tồn tại độc lập của hạt tải thiểu số được chứng minh trực tiếp bằng thực nghiệm thông qua việc quan sát gói hạt tải trôi và dãn rộng "
        "trên màn hình dao động ký, đồng thời đo lường đồng thời cả ba thông số động học cốt lõi: độ linh động <i>&mu;</i>, hệ số khuếch tán <i>D</i> "
        "và thời gian sống tái hợp <i>&tau;</i>.<br/>"
        "↳ Thí nghiệm Haynes &ndash; Shockley: Phép đo trắc lượng kinh điển trực tiếp ba thông số động học của hạt tải thiểu số trong bán dẫn.<br/>"
        "Trước thí nghiệm này, mọi phép đo điện trở suất hay hiệu ứng Hall đều bị áp đảo bởi hạt tải đa số, khiến hạt tải thiểu số bị xem như một giả thuyết toán học trừu tượng."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý đo lường hạt tải thiểu số: Trong một thanh Silic loại n có nồng độ electron đa số <i>n</i><sub>0</sub> = 10<sup>16</sup> cm<sup>-3</sup>, "
        "nồng độ lỗ trống thiểu số cân bằng chỉ đạt <i>p</i><sub>0</sub> = <i>n</i><sub>i</sub><sup>2</sup>/<i>n</i><sub>0</sub> &asymp; 10<sup>4</sup> cm<sup>-3</sup> "
        "(chênh lệch tới 12 bậc độ lớn). Nếu đưa que đo thông thường vào đo, tín hiệu của 10<sup>4</sup> lỗ trống sẽ bị chìm nghỉm hoàn toàn trong đại dương 10<sup>16</sup> electron. "
        "Thí nghiệm Haynes &ndash; Shockley đã giải quyết nghịch lý này bằng một giải pháp thông minh tuyệt đỉnh: sử dụng xung ánh sáng hoặc xung điện áp cực ngắn "
        "để tiêm cục bộ một đám lỗ trống dư &Delta;<i>p</i>, sau đó dùng điện trường quét đẩy đám hạt tải thiểu số này trôi tịnh tiến dọc theo mẫu "
        "đến một cực thu phân cực ngược đặt cách xa điểm tiêm."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_2_4 = [
        ("Mật độ lỗ trống dư tức thời", "&Delta;<i>p</i>(<i>x</i>, <i>t</i>)", "cm<sup>-3</sup>", "Phân bố nồng độ hạt tải thiểu số trong không gian và thời gian theo dạng xung Gauss lan truyền."),
        ("Thời gian trôi đỉnh xung", "<i>t</i><sub>d</sub>", "s", "Thời điểm đỉnh xung Gauss di chuyển đến cực thu, xác định trực tiếp độ linh động <i>&mu;</i>."),
        ("Bề rộng xung ở nửa độ cao", "&Delta;<i>t</i>", "s", "Độ rộng thời gian FWHM của xung tín hiệu tại cực thu, xác định hệ số khuếch tán <i>D</i>."),
        ("Thời gian sống tái hợp", "<i>&tau;</i><sub>p</sub>", "s", "Thời gian sống trung bình của lỗ trống thiểu số trước khi tái hợp với electron đa số."),
        ("Khoảng cách trôi", "<i>d</i>", "cm", "Cự ly hình học dọc trục giữa điện cực tiêm và điện cực thu tín hiệu.")
    ]
    story.append(he.build_target_equation_block(
        r"\Delta p(x, t) = \frac{\Delta P_0}{\sqrt{4 \pi D_p t}} \exp \left( -\frac{(x - \mu_p \mathcal{E} t)^2}{4 D_p t} \right) \exp \left( -\frac{t}{\tau_p} \right)",
        nom_rows_2_2_4,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một giọt mực màu đỏ được nhỏ vào một dòng suối nước trong đang chảy xiết từ thượng nguồn xuống hạ lưu. "
        "Tốc độ trôi của tâm giọt mực xuôi theo dòng nước tương ứng với vận tốc cuốn của hạt tải thiểu số dưới điện trường quét (xác định độ linh động <i>&mu;</i>). "
        "Khi trôi xuôi dòng, giọt mực đỏ liên tục bị hòa tan và loang rộng ra xung quanh do các dòng xoáy vi mô (tương ứng sự dãn nở xung do khuếch tán <i>D</i>). "
        "Đồng thời, các phân tử nước liên tục phản ứng hóa học tẩy trắng các phân tử mực đỏ, làm màu đỏ nhạt dần theo thời gian (tương ứng sự suy giảm biên độ do tái hợp <i>&tau;</i>). "
        "Đặt một cảm biến quang ở hạ lưu suối, thời gian trôi của tâm giọt mực xác định tốc độ dòng chảy, bề rộng vệt màu loang xác định mức độ khuếch tán, "
        "và độ đậm nhạt của màu đỏ xác định tốc độ tẩy trắng của nước."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.15 gốc
    story.append(he.embed_figure_with_caption(
        fig_goc_2_15,
        "Hình 2.15: Sơ đồ nguyên lý cấu hình đo và tín hiệu dao động ký trong thí nghiệm Haynes-Shockley (Slide 18 HUST). "
        "Ba mắt xích vật lý: (a) Thanh bán dẫn Silic loại n chịu điện trường quét không đổi <i>E</i> dọc trục; "
        "(b) Điện cực phát (Emitter) tiêm xung lỗ trống thiểu số tại <i>x</i> = 0; "
        "(c) Tín hiệu điện áp tại điện cực thu (Collector) ghi nhận xung đồng bộ tức thời tại <i>t</i> = 0 và xung Gauss sau thời gian trôi <i>t</i><sub>d</sub>.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.2.4
    story.append(he.build_intermediate_equation(
        "Dẫn xuất công thức trích xuất độ linh động <i>&mu;</i><sub>p</sub> từ thời gian trôi của đỉnh xung Gauss:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tọa độ đỉnh xung đạt cực đại tại <i>x</i><sub>peak</sub> = <i>&mu;</i><sub>p</sub><i>Et</i> = <i>d</i>:",
        r"x_{\mathrm{peak}} = \mu_p \mathcal{E} t_d = d \implies \mu_p = \frac{d}{\mathcal{E} t_d} = \frac{v_d}{\mathcal{E}}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.2.4
    story.append(he.build_intermediate_equation(
        "Dẫn xuất công thức hệ số khuếch tán <i>D</i><sub>p</sub> từ bề rộng thời gian nửa độ cao cực đại FWHM (&Delta;<i>t</i>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập điều kiện biên độ xung tại vị trí nửa độ rộng &Delta;<i>x</i>/2 giảm xuống 1/2:",
        r"\exp\left( -\frac{(\Delta x / 2)^2}{4 D_p t_d} \right) = \frac{1}{2} \implies \frac{(\Delta x)^2}{16 D_p t_d} = \ln 2 \implies D_p = \frac{(\Delta x)^2}{16 t_d \ln 2} = \frac{(v_d \Delta t)^2}{16 t_d \ln 2} = \frac{(d \Delta t)^2}{16 t_d^3 \ln 2}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.2.4
    story.append(he.build_intermediate_equation(
        "Dẫn xuất thời gian sống tái hợp <i>&tau;</i><sub>p</sub> từ sự suy giảm diện tích xung tín hiệu theo thời gian trôi:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tích phân nồng độ hạt dư theo không gian tỷ lệ thuận với hàm suy giảm mũ exp(-<i>t</i>/<i>&tau;</i>):",
        r"S(t) = \int_{-\infty}^{+\infty} \Delta p(x, t) \mathrm{d}x = S_0 \exp\left( -\frac{t}{\tau_p} \right) \implies \tau_p = \frac{t_2 - t_1}{\ln(S_1 / S_2)}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.2
    story.append(he.embed_figure_with_caption(
        fig_sim_2,
        "Hình mô phỏng 2.2: Động học không &ndash; thời gian của xung Haynes-Shockley và đáp ứng cực thu chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Sự tiến hóa không gian của xung lỗ trống &Delta;<i>p</i>(<i>x</i>) tại 4 thời điểm 20, 40, 70 và 100 &mu;s dưới điện trường 50 V&middot;cm<sup>-1</sup>: "
        "đỉnh xung trôi tịnh tiến đều đặn trong khi bề rộng mở rộng do khuếch tán và biên độ suy giảm do tái hợp; "
        "(b) Tín hiệu điện áp cực thu <i>V</i><sub>out</sub>(<i>t</i>) theo thời gian dưới các điện trường 35, 50 và 75 V&middot;cm<sup>-1</sup>: "
        "khi tăng điện trường, thời gian trôi rút ngắn rõ rệt và bề rộng xung co hẹp lại.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Ý nghĩa công nghệ và kiểm soát chất lượng Wafer bán dẫn: Thí nghiệm Haynes &ndash; Shockley là nền tảng ra đời của các thiết bị kiểm chuẩn "
        "không tiếp xúc hiện đại trong công nghiệp chế tạo chip như phương pháp phân rã huỳnh quang vi sóng (Microwave Photoconductive Decay &mdash; &mu;-PCD). "
        "Trong quy trình sản xuất phiến Silic đơn tinh thể đường kính 300 mm, thời gian sống hạt tải thiểu số <i>&tau;</i> là chỉ số nhạy cảm nhất "
        "để phát hiện ô nhiễm kim loại nặng (Fe, Cu, Ni) ở mức vết (cỡ phần triệu triệu &mdash; ppt). "
        "Chỉ cần mật độ tạp chất sắt Fe đạt 10<sup>11</sup> cm<sup>-3</sup>, <i>&tau;</i> sẽ tụt giảm từ hàng mili-giây xuống vài micro-giây, "
        "phá hủy hoàn toàn hiệu suất lượng tử của pin mặt trời và làm tăng dòng rò tĩnh của chip vi xử lý."
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
        "<b>Ca chẩn đoán 1: Bẫy điểm mù bão hòa vận tốc cuốn trong phép đo Haynes-Shockley trường mạnh.</b><br/>"
        "Một nhóm nghiên cứu tại phòng thí nghiệm linh kiện bán dẫn thực hiện thí nghiệm Haynes &ndash; Shockley để đo độ linh động của lỗ trống trong thanh Silic loại n. "
        "Để hạn chế tối đa sự suy giảm biên độ xung do tái hợp nhằm thu được tín hiệu sắc nét tại cực thu, kỹ sư đã tăng mạnh điện trường quét lên <i>E</i> = 8 &times; 10<sup>3</sup> V&middot;cm<sup>-1</sup>. "
        "Kết quả tính toán từ thời gian trôi <i>t</i><sub>d</sub> cho thấy độ linh động lỗ trống đo được chỉ đạt <i>&mu;</i><sub>p</sub> xấp xỉ 106 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>, "
        "thấp hơn rất nhiều so với giá trị chuẩn 450 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> ở nhiệt độ phòng 300 K. "
        "Đồng thời, hệ số khuếch tán <i>D</i><sub>p</sub> tính từ bề rộng xung &Delta;<i>t</i> sai lệch nghiêm trọng so với hệ thức Einstein.<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Sử dụng cơ chế tán xạ phonon quang học và hiện tượng bão hòa vận tốc cuốn trường mạnh, "
        "hãy giải trình tại sao việc tăng điện trường quét lại bóp méo hoàn toàn kết quả đo độ linh động? "
        "Tại sao trong điều kiện trường mạnh, hệ thức Einstein giữa hệ số khuếch tán và độ linh động bị phá vỡ hoàn toàn?",
        "Body"
    )
    add_spacer(8)
    
    # Ca chẩn đoán 2
    add_p(
        "<b>Ca chẩn đoán 2: Bẫy điểm mù dòng khuếch tán trong cảm biến quang Photodiode và Solar Cell dải bước sóng dài.</b><br/>"
        "Khi thiết kế pin mặt trời Silic đơn tinh thể và cảm biến quang PIN Photodiode đáp ứng bước sóng hồng ngoại gần (&lambda; = 900 &minus; 1050 nm), "
        "một kỹ sư R&amp;D nhận thấy hiệu suất lượng tử nội tại (IQE) sụt giảm thảm hại mặc dù điện trường trong vùng nghèo cực kỳ mạnh. "
        "Báo cáo kỹ thuật nhận định rằng do ánh sáng bước sóng dài thâm nhập sâu vào vùng bazơ trung hòa (ngoài vùng nghèo), "
        "nơi không có điện trường nên các cặp electron &ndash; lỗ trống quang sinh không thể di chuyển và bị mất mát hoàn toàn.<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Áp dụng phương trình dòng khuếch tán hạt tải thiểu số và chiều dài khuếch tán <i>L</i> = &radic;(<i>D&tau;</i>), "
        "hãy chỉ ra sai lầm cốt tử của bản báo cáo kỹ thuật trên. Cơ chế vận chuyển nào thực sự thu thập các hạt tải quang sinh trong vùng bazơ trung hòa? "
        "Biện pháp kỹ thuật nào trong công nghệ chế tạo bán dẫn (xử lý thụ động hóa bề mặt và trường điện mặt sau BSF) cho phép cứu vãn hiệu suất thu thập hạt tải?",
        "Body"
    )
    add_spacer(8)
    
    # Khối Phản biện (Silent Drop)
    add_p(
        "<b>Khối Phản biện Nguyên lý Đầu (Silent Drop &mdash; Giảng viên kỳ cựu gửi Bùi Trung Dũng):</b><br/>"
        "Trong toàn bộ dẫn xuất lý thuyết của thí nghiệm Haynes &ndash; Shockley và định luật Fick, chúng ta đã ngầm thừa nhận "
        "<b>giả thiết tiêm mức thấp (Low-Level Injection &mdash; LLI)</b>, nghĩa là nồng độ hạt tải thiểu số quang sinh &Delta;<i>p</i> "
        "nhỏ hơn rất nhiều so với nồng độ hạt tải đa số cân bằng <i>n</i><sub>0</sub> (&Delta;<i>p</i> &lt;&lt; <i>n</i><sub>0</sub>).<br/>"
        "↳ <i>Câu hỏi đối trọng:</i> Hãy phân tích điều gì sẽ xảy ra về mặt vi mô đối với dạng xung và giá trị đo được của độ linh động "
        "nếu cường độ xung laser tiêm quá mạnh dẫn đến <b>tiêm mức cao (High-Level Injection &mdash; HLI)</b> (&Delta;<i>p</i> &ge; <i>n</i><sub>0</sub>)? "
        "Khi đó, điện trường nội tại do sự tách biệt điện tích không gian giữa electron và lỗ trống (hiệu ứng khuếch tán lưỡng cực &mdash; Ambipolar Diffusion) "
        "sẽ bóp méo nghiệm Gauss kinh điển như thế nào và làm trôi lệch giá trị <i>&mu;</i> đo được ra sao?",
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
    build_monograph_muc_2_2()

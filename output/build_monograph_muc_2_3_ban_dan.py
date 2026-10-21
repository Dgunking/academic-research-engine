# -*- coding: utf-8 -*-
"""
Builder Script for Monograph Muc 2.3: Chuyen_Khao_Ban_Dan_Muc_2.3.pdf
Subject: Vat ly va linh kien ban dan (PH3190 - HUST)
Chapter 2: Cac hien tuong van chuyen trong ban dan
Section 2.3: Cac qua trinh sinh va tai hop trong ban dan (Generation & Recombination)
Architecture: Full 5-Block Feynman Visual-First Core & Causal Flowchain (HUST Standard)
Strict Compliance:
  - Zero-Slash-Fractions via LaTeX Mathtext >= 300 DPI (Rule 14)
  - Flawless symbol & unit formatting in HTML (<i>...</i>, <sub>...</sub>, <sup>...</sup>)
  - Zero LaTeX leakage in Paragraphs / Tables (Rule 15)
  - 100% Zero-Omission of Slide Chapter 2 (Slide 19-23) & Sze / Neamen textbooks
  - All 4 Original Figures + 2 MATLAB Simulation Plots embedded
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
TARGET_PDF = os.path.join(BAI_GIANG_DIR, "Chuyen_Khao_Ban_Dan_Muc_2.3.pdf")

# Image assets
fig_goc_2_16 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.16_Gian_do_tai_hop_va_sinh_truc_tiep_e_h.png")
fig_goc_2_17 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.17_Gian_do_tai_hop_gian_tiep_qua_bay_SRH.png")
fig_goc_2_18 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.18_Co_che_tai_hop_be_mat_Surface_Recombination.png")
fig_goc_2_19 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.19_Co_che_tai_hop_Auger_truyen_nang_luong_hat_thu_3.png")

fig_sim_1 = os.path.join(IMG_DIR, "[Mo_Phong]_Toc_do_tai_hop_SRH_theo_Et.png")
fig_sim_2 = os.path.join(IMG_DIR, "[Mo_Phong]_So_sanh_4_co_che_tai_hop.png")

def build_monograph_muc_2_3():
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
    add_p("Mục 2.3: Các quá trình sinh và tái hợp trong bán dẫn", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Sze &amp; Ng — Physics of Semiconductor Devices, Chương 1.5; Neamen — Semiconductor Physics and Devices, Chương 6)</i>", "Caption")
    add_spacer(4)
    
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Vật lý và linh kiện bán dẫn (PH3190)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Ch. 2 (Slide 19–23); Sze &amp; Ng Devices"), styles["TableCell"]),
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
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.3.1</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Quá trình sinh &ndash; tái hợp trực tiếp giữa các vùng năng lượng và động học thời gian sống hạt tải thiểu số"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 19–20<br/>Hình 2.16"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.3.2</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Cơ chế tái hợp gián tiếp qua bẫy sâu Shockley &ndash; Read &ndash; Hall (SRH) trong bán dẫn vùng cấm xiên"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 21<br/>Hình 2.17, Mô phỏng 2.1"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.3.3</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tái hợp bề mặt, mật độ liên kết treo và vận tốc tái hợp bề mặt trong cấu trúc bán dẫn màng mỏng"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 22<br/>Hình 2.18"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.3.4</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tái hợp Auger ba hạt mang điện ở mật độ kích thích cao và hiện tượng suy giảm hiệu suất lượng tử"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 23<br/>Hình 2.19, Mô phỏng 2.2"), styles["TableCellCenter"])]
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
    # LUẬN ĐIỂM 2.3.1: TÁI HỢP TRỰC TIẾP GIỮA CÁC VÙNG NĂNG LƯỢNG
    # =========================================================================
    add_p("Luận điểm 2.3.1: Quá trình sinh &ndash; tái hợp trực tiếp giữa các vùng năng lượng và thời gian sống hạt tải thiểu số", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong vật lý bán dẫn, quá trình sinh (Generation) và tái hợp (Recombination) là hai cơ chế vi mô đối ngẫu chi phối số lượng tuyệt đối "
        "của các hạt mang điện tự do trong mạng tinh thể. Quá trình sinh là sự chuyển dời của electron từ vùng hóa trị lên vùng dẫn dưới tác dụng "
        "của kích thích nhiệt hoặc kích thích quang học, tạo ra đồng thời một electron tự do và một lỗ trống tự do. "
        "Ngược lại, quá trình tái hợp là sự rơi của một electron từ vùng dẫn xuống lấp đầy một trạng thái trống trong vùng hóa trị, "
        "tiêu diệt đồng thời cặp electron &ndash; lỗ trống và giải phóng năng lượng dưới dạng photon hoặc phonon.<br/>"
        "↳ Tái hợp trực tiếp (Direct Band-to-Band Recombination): Quá trình chuyển dời điện tử thẳng đứng trong không gian xung lượng <b>k</b> mà không cần sự trợ giúp của phonon.<br/>"
        "Cơ chế này chiếm ưu thế tuyệt đối trong các bán dẫn vùng cấm thẳng (Direct Bandgap) như Gallium Arsenide (GaAs), Indium Phosphide (InP), "
        "nơi cực tiểu vùng dẫn và cực đại vùng hóa trị nằm tại cùng một vector sóng <b>k</b> = 0."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý cân bằng nhiệt động và sự phá vỡ cân bằng do chiếu sáng: Ở trạng thái cân bằng nhiệt, định luật tác dụng khối khẳng định "
        "tích số nồng độ hạt tải luôn là một hằng số <i>n</i><sub>0</sub><i>p</i><sub>0</sub> = <i>n</i><sub>i</sub><sup>2</sup>. "
        "Tốc độ sinh nhiệt <i>G</i><sub>th</sub> cân bằng chính xác với tốc độ tái hợp nhiệt <i>R</i><sub>th</sub> = &beta;<i>n</i><sub>0</sub><i>p</i><sub>0</sub>, "
        "khiến số lượng hạt tải không đổi theo thời gian. "
        "Tuy nhiên, khi chiếu sáng mẫu bán dẫn bằng chùm photon có năng lượng lớn hơn độ rộng vùng cấm (<i>h&nu;</i> &gt; <i>E</i><sub>g</sub>), "
        "tốc độ sinh tăng thêm một lượng <i>G</i><sub>L</sub> do kích thích quang. "
        "Hệ thống bị đẩy ra khỏi trạng thái cân bằng nhiệt động. "
        "Tốc độ tái hợp thực tế thuần <i>U</i> = <i>R</i> &minus; <i>G</i><sub>th</sub> xuất hiện nhằm kéo hệ thống trở về trạng thái cân bằng. "
        "Thời gian cần thiết để nồng độ hạt tải dư phân rã sau khi tắt nguồn kích thích chính là thời gian sống của hạt tải thiểu số."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_3_1 = [
        ("Tốc độ tái hợp thực tế", "<i>U</i>", "cm<sup>-3</sup>&middot;s<sup>-1</sup>", "Tốc độ tái hợp thuần vượt quá mức cân bằng nhiệt động: <i>U</i> = <i>R</i> &minus; <i>G</i><sub>th</sub>."),
        ("Hệ số tái hợp bức xạ", "&beta;", "cm<sup>3</sup>&middot;s<sup>-1</sup>", "Xác suất tái hợp trực tiếp trên một đơn vị thể tích (khoảng 10<sup>-10</sup> cm<sup>3</sup>&middot;s<sup>-1</sup> trong GaAs)."),
        ("Nồng độ electron cân bằng", "<i>n</i><sub>n0</sub>", "cm<sup>-3</sup>", "Mật độ electron đa số trong bán dẫn loại n ở trạng thái cân bằng nhiệt."),
        ("Nồng độ lỗ trống cân bằng", "<i>p</i><sub>n0</sub>", "cm<sup>-3</sup>", "Mật độ lỗ trống thiểu số trong bán dẫn loại n ở trạng thái cân bằng nhiệt."),
        ("Thời gian sống lỗ trống thiểu số", "<i>&tau;</i><sub>p</sub>", "s", "Thời gian sống trung bình của lỗ trống dư ở điều kiện tiêm mức thấp, xác định bởi nghịch đảo của tích số giữa hệ số &beta; và nồng độ electron <i>n</i><sub>n0</sub>.")
    ]
    story.append(he.build_target_equation_block(
        r"U = \beta (n p - n_i^2) \approx \beta n_{n0} \Delta p = \frac{\Delta p}{\tau_p}",
        nom_rows_2_3_1,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một vũ hội khiêu vũ trong một khán phòng lớn. "
        "Số lượng nam thanh niên độc thân tương ứng với nồng độ electron <i>n</i>, và số lượng nữ thanh niên độc thân tương ứng với nồng độ lỗ trống <i>p</i>. "
        "Mỗi khi một nam và một nữ gặp nhau và ghép đôi khiêu vũ, một cặp electron &ndash; lỗ trống biến mất (quá trình tái hợp). "
        "Xác suất để một đôi gặp nhau tỷ lệ thuận với tích số của số lượng nam và số lượng nữ (tốc độ tái hợp <i>R</i> = &beta;<i>n</i>&middot;<i>p</i>). "
        "Trong một bán dẫn loại n pha tạp rất nặng (ví dụ 1000 nam và chỉ có 1 nữ), cơ hội để một cô gái tìm thấy một chàng trai là gần như tức thì "
        "vì bất kỳ bước chân nào của cô cũng va phải một chàng trai. "
        "Do đó, thời gian sống của cô gái (hạt tải thiểu số) cực kỳ ngắn ngủi và tỷ lệ nghịch với số lượng nam thanh niên có mặt trong phòng."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.16
    story.append(he.embed_figure_with_caption(
        fig_goc_2_16,
        "Hình 2.16: Quá trình sinh &ndash; tái hợp trực tiếp giữa các vùng năng lượng và động học suy giảm nồng độ lỗ trống theo thời gian (Slide 19 &ndash; 20 HUST). "
        "Ba mắt xích vật lý: (a) Quá trình hấp thụ photon sinh cặp e-h và tái hợp bức xạ trực tiếp phát ra photon; "
        "(b) Trạng thái dừng tĩnh tại khi chiếu sáng liên tục đạt nồng độ <i>p</i><sub>n</sub>(0) = <i>p</i><sub>n0</sub> + <i>&tau;</i><sub>p</sub><i>G</i><sub>L</sub>; "
        "(c) Quy luật phân rã hàm mũ theo thời gian sau khi tắt nguồn sáng tại <i>t</i> = 0.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.3.1
    story.append(he.build_intermediate_equation(
        "Thiết lập phương trình vi phân tốc độ biến thiên nồng độ hạt tải thiểu số dưới kích thích quang học:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tốc độ biến thiên nồng độ lỗ trống bằng hiệu số giữa tốc độ sinh và tốc độ tái hợp:",
        r"\frac{\mathrm{d}p_n}{\mathrm{d}t} = G_L + G_{\mathrm{th}} - R = G_L - U = G_L - \beta (n p - n_i^2)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.3.1
    story.append(he.build_intermediate_equation(
        "Xác lập điều kiện trạng thái dừng khi chiếu sáng liên tục và tuyến tính hóa ở mức tiêm thấp LLI:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi đạo hàm triệt tiêu d<i>p</i><sub>n</sub>/d<i>t</i> = 0, nồng độ lỗ trống dư tỷ lệ thuận với tốc độ sinh:",
        r"\frac{\mathrm{d}p_n}{\mathrm{d}t} = 0 \implies G_L = U = \frac{\Delta p}{\tau_p} \implies \Delta p = \tau_p G_L \implies p_n(0) = p_{n0} + \tau_p G_L",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.3.1
    story.append(he.build_intermediate_equation(
        "Giải nghiệm phương trình vi phân phân rã nồng độ sau khi tắt nguồn kích thích quang học tại <i>t</i> = 0:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm hàm mũ thỏa mãn điều kiện biên <i>p</i><sub>n</sub>(0) và <i>p</i><sub>n</sub>(&infin;) = <i>p</i><sub>n0</sub>:",
        r"\frac{\mathrm{d} \Delta p}{\mathrm{d}t} = -\frac{\Delta p}{\tau_p} \implies \Delta p(t) = \Delta p(0) \exp\left(-\frac{t}{\tau_p}\right) \implies p_n(t) = p_{n0} + \tau_p G_L \exp\left(-\frac{t}{\tau_p}\right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Ý nghĩa quyết định của tái hợp trực tiếp trong Quang điện tử và Laser Diode: Trong các chất bán dẫn vùng cấm thẳng (GaAs, InP, GaN), "
        "quá trình tái hợp trực tiếp diễn ra cực kỳ nhanh chóng với thời gian sống chỉ cỡ vài nano-giây (<i>&tau;</i> &asymp; 1 &minus; 10 ns). "
        "Năng lượng giải phóng hầu như 100% chuyển hóa thành photon ánh sáng đơn sắc, cho phép chế tạo các nguồn phát quang hiệu suất cao "
        "như LED phát quang và Diode Laser bán dẫn trong thông tin sợi quang. "
        "Ngược lại, trong Silicon (vùng cấm xiên), sự lệch pha vector sóng &Delta;<b>k</b> khiến xác suất tái hợp bức xạ trực tiếp cực kỳ bé "
        "(thời gian sống bức xạ lý thuyết lên tới hàng giây). "
        "Do đó, Silicon hoàn toàn bất lực trong việc đóng vai trò nguồn phát quang tích hợp, buộc nền công nghiệp quang tử vi mạch (Silicon Photonics) "
        "phải sử dụng công nghệ lai ghép dị thể (Heterogeneous Integration) bằng cách dán phiến màng mỏng InP/GaAs lên đế bán dẫn Silicon."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.3.2: TÁI HỢP GIÁN TIẾP SHOCKLEY-READ-HALL (SRH)
    # =========================================================================
    add_p("Luận điểm 2.3.2: Cơ chế tái hợp gián tiếp qua bẫy sâu Shockley &ndash; Read &ndash; Hall (SRH) trong bán dẫn vùng cấm xiên", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong các chất bán dẫn có cấu trúc vùng cấm xiên (Indirect Bandgap) như Silicon (Si) và Germanium (Ge), cực tiểu vùng dẫn "
        "nằm lệch khỏi gốc tọa độ không gian xung lượng so với cực đại vùng hóa trị. Một electron muốn nhảy xuống tái hợp với một lỗ trống "
        "bắt buộc phải giải phóng đồng thời năng lượng (cho photon) và xung lượng khổng lồ &Delta;<b>p</b> = &hbar;&Delta;<b>k</b> cho một phonon mạng tinh thể. "
        "Xác suất của một biến cố lượng tử đòi hỏi ba thực thể tương tác đồng thời là cực kỳ nhỏ.<br/>"
        "↳ Tái hợp gián tiếp SRH (Shockley-Read-Hall Recombination): Cơ chế tái hợp hai bước thông qua các trạng thái năng lượng trung gian định xứ trong vùng cấm.<br/>"
        "Các trạng thái này được tạo ra bởi các sai hỏng cấu trúc mạng tinh thể (nút khuyết vacancy, nguyên tử xen kẽ) hoặc các nguyên tử tạp chất kim loại nặng (Vàng Au, Sắt Fe, Đồng Cu)."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý bẫy sâu và bẫy nông: Không phải mọi mức tạp chất trong vùng cấm đều là tâm tái hợp hiệu quả. "
        "Các tạp chất pha nồng độ donor (như Phosphor) hoặc acceptor (như Boron) có mức năng lượng nằm rất sát mép vùng dẫn hoặc vùng hóa trị "
        "(gọi là bẫy nông &mdash; Shallow Traps, cách mép dải chỉ khoảng 0,04 eV). "
        "Khi một electron rơi vào bẫy nông, năng lượng nhiệt của mạng tinh thể <i>k</i><sub>B</sub><i>T</i> &asymp; 0,026 eV thừa sức kích thích electron "
        "nhảy ngược trở lại vùng dẫn trước khi một lỗ trống kịp đến tái hợp. "
        "Chỉ những tạp chất tạo ra mức năng lượng nằm sâu ở chính giữa vùng cấm (gọi là bẫy sâu &mdash; Deep Traps, như Au trong Si có <i>E</i><sub>t</sub> &asymp; <i>E</i><sub>i</sub>) "
        "mới có thể giữ chân electron đủ lâu để lỗ trống đến hoàn tất quá trình tái hợp, biến bẫy sâu thành tâm tái hợp sát thủ tiêu diệt hạt tải."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_3_2 = [
        ("Tốc độ tái hợp SRH", "<i>U</i><sub>SRH</sub>", "cm<sup>-3</sup>&middot;s<sup>-1</sup>", "Tốc độ tái hợp ròng qua bẫy sâu theo mô hình Shockley &ndash; Read &ndash; Hall."),
        ("Mật độ tâm tái hợp", "<i>N</i><sub>t</sub>", "cm<sup>-3</sup>", "Nồng độ thể tích của các nguyên tử tạp chất hoặc sai hỏng mạng đóng vai trò bẫy năng lượng."),
        ("Tiết diện bắt electron", "&sigma;<sub>n</sub>", "cm<sup>2</sup>", "Diện tích hiệu dụng mà tâm bẫy có thể bắt giữ một electron dẫn (cỡ 10<sup>-15</sup> cm<sup>2</sup>)."),
        ("Tiết diện bắt lỗ trống", "&sigma;<sub>p</sub>", "cm<sup>2</sup>", "Diện tích hiệu dụng mà tâm bẫy có thể bắt giữ một lỗ trống (cỡ 10<sup>-15</sup> cm<sup>2</sup>)."),
        ("Mức năng lượng bẫy", "<i>E</i><sub>t</sub>", "eV", "Vị trí năng lượng của trạng thái định xứ so với mức Fermi nội tại <i>E</i><sub>i</sub>.")
    ]
    story.append(he.build_target_equation_block(
        r"U_{\mathrm{SRH}} = \frac{v_{\mathrm{th}} \sigma_n \sigma_p N_t (n p - n_i^2)}{\sigma_n \left[ n + n_i \exp\left(\frac{E_t - E_i}{k_{\mathrm{B}} T}\right) \right] + \sigma_p \left[ p + n_i \exp\left(-\frac{E_t - E_i}{k_{\mathrm{B}} T}\right) \right]}",
        nom_rows_2_3_2,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một vách đá thẳng đứng cao vút ngăn cách hai bờ vực (độ rộng vùng cấm <i>E</i><sub>g</sub> = 1,12 eV trong Si). "
        "Một người muốn nhảy từ đỉnh vách đá xuống đáy vực sẽ rất sợ hãi và hiếm khi dám nhảy thẳng xuống (tái hợp trực tiếp bị cấm). "
        "Tuy nhiên, nếu người ta gắn một bệ đỡ bậc thang trung gian vào giữa vách đá (mức bẫy sâu <i>E</i><sub>t</sub>), "
        "người đó có thể dễ dàng nhảy bước một xuống bệ đỡ bậc thang (bắt electron), sau đó từ bệ đỡ nhảy tiếp bước hai xuống đáy vực an toàn (bắt lỗ trống). "
        "Nếu bệ đỡ được gắn quá sát đỉnh vách đá hoặc quá sát đáy vực (bẫy nông), người đó nhảy vào bệ đỡ rồi sẽ trèo ngược trở lại ngay. "
        "Chỉ khi bệ đỡ được đặt chính xác ở điểm lưng chừng một nửa độ cao vách đá (<i>E</i><sub>t</sub> &asymp; <i>E</i><sub>i</sub>), "
        "lưu lượng người nhảy qua hai chặng mới đạt tốc độ tối đa."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.17
    story.append(he.embed_figure_with_caption(
        fig_goc_2_17,
        "Hình 2.17: Giản đồ bốn quá trình dịch chuyển năng lượng qua mức bẫy trung gian SRH trong vùng cấm (Slide 21 HUST). "
        "Bốn mắt xích vi mô: (a) Quá trình bắt electron từ vùng dẫn vào bẫy; "
        "(b) Quá trình phát xạ nhiệt electron từ bẫy ngược lên vùng dẫn; "
        "(c) Quá trình bắt lỗ trống từ vùng hóa trị vào bẫy (hoặc electron từ bẫy rơi xuống vùng hóa trị); "
        "(d) Quá trình phát xạ nhiệt lỗ trống từ bẫy xuống vùng hóa trị.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.3.2
    story.append(he.build_intermediate_equation(
        "Cân bằng động học xác suất lấp đầy tâm bẫy <i>f</i><sub>t</sub> ở trạng thái dừng vi mô:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tốc độ bắt electron bằng tốc độ bắt lỗ trống để bảo toàn mật độ điện tích trên bẫy:",
        r"r_a - r_b = r_c - r_d \implies C_n N_t [n (1 - f_t) - n_1 f_t] = C_p N_t [p f_t - p_1 (1 - f_t)]",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.3.2
    story.append(he.build_intermediate_equation(
        "Giải nghiệm đại số xác suất lấp đầy <i>f</i><sub>t</sub> và thay vào biểu thức tốc độ tái hợp ròng <i>U</i> = <i>r</i><sub>a</sub> &minus; <i>r</i><sub>b</sub>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu diễn tốc độ tái hợp qua hai thời gian sống đặc trưng &tau;<sub>n0</sub> và &tau;<sub>p0</sub>:",
        r"U_{\mathrm{SRH}} = \frac{n p - n_i^2}{\tau_{p0} (n + n_1) + \tau_{n0} (p + p_1)}, \quad \tau_{n0} = \frac{1}{v_{\mathrm{th}} \sigma_n N_t}, \quad \tau_{p0} = \frac{1}{v_{\mathrm{th}} \sigma_p N_t}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.3.2
    story.append(he.build_intermediate_equation(
        "Xấp xỉ điều kiện tiêm mức thấp LLI trong bán dẫn loại n (<i>n</i><sub>n0</sub> &gt;&gt; <i>p</i><sub>n0</sub> và <i>n</i><sub>n0</sub> &gt;&gt; <i>n</i><sub>1</sub>, <i>p</i><sub>1</sub>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thời gian sống hạt tải thiểu số độc lập với nồng độ tiêm và bằng đúng &tau;<sub>p0</sub>:",
        r"U_{\mathrm{SRH}} \approx \frac{n_{n0} \Delta p}{\tau_{p0} n_{n0}} = \frac{\Delta p}{\tau_{p0}} \implies \tau = \tau_{p0} = \frac{1}{v_{\mathrm{th}} \sigma_p N_t}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.1
    story.append(he.embed_figure_with_caption(
        fig_sim_1,
        "Hình mô phỏng 2.1: Đặc tuyến tốc độ tái hợp SRH và thời gian sống hạt tải chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Tốc độ tái hợp <i>U</i><sub>SRH</sub> theo vị trí mức bẫy năng lượng (<i>E</i><sub>t</sub> &minus; <i>E</i><sub>i</sub>): "
        "tốc độ đạt cực đại đối xứng tại chính giữa vùng cấm <i>E</i><sub>t</sub> &asymp; <i>E</i><sub>i</sub> và suy giảm dốc đứng khi tiến về hai mép dải; "
        "(b) Thời gian sống hạt tải thiểu số theo tỷ số tiêm hạt tải &Delta;<i>p</i>/<i>n</i><sub>0</sub>: "
        "thể hiện rõ sự chuyển dịch từ mức tiêm thấp LLI (&tau; = &tau;<sub>p0</sub>) sang mức tiêm cao HLI (&tau; = &tau;<sub>n0</sub> + &tau;<sub>p0</sub>).",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Kỹ thuật điều khiển thời gian sống hạt tải (Lifetime Engineering) trong công nghệ bán dẫn công suất: "
        "Trong các linh kiện khóa chuyển mạch công suất cao như Diode phục hồi nhanh (Fast Recovery Diode &mdash; FRD), IGBT và Thyristor, "
        "thời gian chuyển mạch từ trạng thái dẫn sang trạng thái khóa (Reverse Recovery Time <i>t</i><sub>rr</sub>) bị giới hạn bởi thời gian tiêu tán "
        "các hạt tải thiểu số tích tụ trong vùng trôi. "
        "Để tăng tốc độ ngắt mạch từ hàng chục micro-giây xuống vài chục nano-giây, các kỹ sư công nghệ chủ động cấy các nguyên tử Vàng (Au), "
        "Bạch kim (Pt) hoặc chiếu xạ chùm electron năng lượng cao (Electron Beam Irradiation) vào vùng tích cực. "
        "Các nguyên tử kim loại này tạo ra các tâm bẫy sâu SRH hoàn hảo, làm giảm <i>&tau;</i> xuống mức cực nhỏ, triệt tiêu dòng phục hồi ngược "
        "và bảo vệ mạch biến tần công suất khỏi bị quá nhiệt đánh thủng."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.3.3: TÁI HỢP BỀ MẶT TRONG CẤU TRÚC MÀNG MỎNG
    # =========================================================================
    add_p("Luận điểm 2.3.3: Tái hợp bề mặt, mật độ liên kết treo và vận tốc tái hợp bề mặt trong cấu trúc bán dẫn màng mỏng", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Mặt ngoài của tinh thể bán dẫn là nơi trật tự tuần hoàn không gian ba chiều của mạng tinh thể bị gián đoạn đột ngột. "
        "Các nguyên tử Silic ở lớp ngoài cùng không còn nguyên tử lân cận để tạo liên kết cộng hóa trị, để lại các liên kết chưa ghép đôi gọi là "
        "liên kết treo (Dangling Bonds). Sự đứt gãy liên kết kết hợp với sự hấp phụ của các nguyên tử oxy, hydro và tạp chất môi trường "
        "tạo ra một dải liên tục các trạng thái năng lượng định xứ nằm dày đặc trong vùng cấm tại bề mặt (Surface States).<br/>"
        "↳ Tái hợp bề mặt (Surface Recombination): Quá trình tái hợp qua bẫy diễn ra tập trung tại mặt phân giới tiếp xúc của tinh thể bán dẫn.<br/>"
        "Động thái tái hợp bề mặt hoàn toàn tương tự cơ chế SRH trong thể tích khối, nhưng mật độ tâm bẫy được đo trên một đơn vị diện tích (cm<sup>-2</sup>) "
        "thay vì đơn vị thể tích (cm<sup>-3</sup>)."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý vận tốc tái hợp bề mặt và kích thước linh kiện: Đại lượng đặc trưng cho cường độ tái hợp bề mặt có thứ nguyên của một vận tốc "
        "(cm&middot;s<sup>-1</sup>), được gọi là vận tốc tái hợp bề mặt <i>S</i>. "
        "Đối với một khối bán dẫn thể tích lớn (Bulk), tỷ số diện tích bề mặt trên thể tích <i>A</i>/<i>V</i> rất nhỏ, tái hợp trong thể tích khối "
        "chiếm ưu thế áp đảo. "
        "Tuy nhiên, trong kỷ nguyên công nghệ nano và pin mặt trời màng mỏng, độ dày phiến bán dẫn giảm xuống chỉ còn vài chục micromet hoặc vài nanomet "
        "(như kênh dẫn của FinFET, dây nano nanowire, chấm lượng tử quantum dot). "
        "Tỷ số <i>A</i>/<i>V</i> bùng nổ khổng lồ khiến bề mặt trở thành chiếc 'hố đen' nuốt chửng toàn bộ hạt tải, "
        "làm sụp đổ thời gian sống hiệu dụng nếu không có giải pháp thụ động hóa bảo vệ bề mặt."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_3_3 = [
        ("Tốc độ tái hợp bề mặt", "<i>U</i><sub>s</sub>", "cm<sup>-2</sup>&middot;s<sup>-1</sup>", "Tổng số hạt dẫn tái hợp trên một đơn vị diện tích bề mặt trong một đơn vị thời gian."),
        ("Vận tốc tái hợp bề mặt", "<i>S</i>", "cm&middot;s<sup>-1</sup>", "Đại lượng đo lường hiệu lực hút và nuốt hạt tải của bề mặt: <i>S</i> = <i>v</i><sub>th</sub> &sigma;<sub>s</sub> <i>N</i><sub>st</sub>."),
        ("Mật độ tâm bẫy bề mặt", "<i>N</i><sub>st</sub>", "cm<sup>-2</sup>", "Số lượng trạng thái liên kết treo trên một đơn vị diện tích bề mặt bán dẫn."),
        ("Nồng độ hạt tải dư bề mặt", "&Delta;<i>p</i><sub>s</sub>", "cm<sup>-3</sup>", "Mật độ hạt tải thiểu số dư tại vị trí sát mặt phân giới tiếp xúc."),
        ("Tiết diện bắt bề mặt", "&sigma;<sub>s</sub>", "cm<sup>2</sup>", "Tiết diện hiệu dụng bắt giữ hạt tải của các liên kết treo bề mặt.")
    ]
    story.append(he.build_target_equation_block(
        r"U_s = S \cdot \Delta p_s = (v_{\mathrm{th}} \sigma_s N_{st}) \Delta p_s",
        nom_rows_2_3_3,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một hội trường lớn chứa đầy các khán giả đang đi lại tự do trong phòng. "
        "Bức tường xung quanh hội trường được sơn bằng một loại keo dính chuột siêu dính (liên kết treo bề mặt). "
        "Bất kỳ ai vô tình bước chạm vào tường sẽ bị dính chặt lại và bị loại khỏi cuộc chơi (tái hợp bề mặt). "
        "Vận tốc tái hợp bề mặt <i>S</i> tương ứng với độ dính của bức tường và tốc độ mà bức tường nuốt các khán giả ở sát cạnh nó. "
        "Nếu căn phòng rất rộng (linh kiện khối lớn), phần lớn mọi người ở giữa phòng không bao giờ chạm tới tường. "
        "Nhưng nếu căn phòng bị thu hẹp thành một hành lang hẹp dính vách chỉ rộng nửa mét (kênh dẫn transistor nanomet), "
        "tất cả mọi người đều sẽ chạm vào tường sau vài bước chân, và toàn bộ hội trường sẽ bị loại sạch sẽ trong tích tắc."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.18
    story.append(he.embed_figure_with_caption(
        fig_goc_2_18,
        "Hình 2.18: Giản đồ cấu trúc liên kết treo trên bề mặt sạch của tinh thể bán dẫn Silic (Slide 22 HUST). "
        "Ba mắt xích vật lý: (a) Các nguyên tử trong khối duy trì liên kết tứ diện cộng hóa trị hoàn hảo 4 liên kết; "
        "(b) Các nguyên tử ở lớp bề mặt ngoài cùng bị đứt gãy liên kết tạo thành các liên kết treo (Dangling Bonds); "
        "(c) Các liên kết treo tạo dải mức năng lượng dày đặc trong vùng cấm đóng vai trò tâm tái hợp bề mặt.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.3.3
    story.append(he.build_intermediate_equation(
        "Thiết lập điều kiện biên dòng khuếch tán tại bề mặt bán dẫn <i>x</i> = 0:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thông lượng hạt tải khuếch tán ra bề mặt bằng đúng tốc độ hạt tải bị tái hợp tại bề mặt:",
        r"D_p \left. \frac{\mathrm{d} \Delta p}{\mathrm{d}x} \right|_{x=0} = U_s = S \cdot \Delta p(0)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.3.3
    story.append(he.build_intermediate_equation(
        "Tách biến phương trình liên tục và xác định thời gian sống hiệu dụng trong phiến bán dẫn bề dày <i>W</i> có hai mặt đối xứng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Quy tắc cộng nghịch đảo thời gian sống trong khối và thời gian sống bề mặt:",
        r"\frac{1}{\tau_{\mathrm{eff}}} = \frac{1}{\tau_{\mathrm{bulk}}} + \frac{1}{\tau_{\mathrm{surface}}} \approx \frac{1}{\tau_{\mathrm{bulk}}} + \frac{2 S}{W} \quad \left( \text{khi } \frac{S W}{2 D_p} \ll 1 \right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Công nghệ thụ động hóa bề mặt (Surface Passivation) trong Pin mặt trời Silic hiệu suất siêu cao: "
        "Bề mặt Silic sau khi cắt bằng cưa dây kim cương có mật độ liên kết treo cực cao, dẫn đến vận tốc tái hợp bề mặt vượt quá <i>S</i> &gt; 10<sup>5</sup> cm&middot;s<sup>-1</sup>. "
        "Với giá trị <i>S</i> này, mọi hạt tải quang sinh sinh ra gần mặt trước đều bị tiêu diệt, làm sụp đổ dòng ngắn mạch <i>J</i><sub>sc</sub> và điện áp hở mạch <i>V</i><sub>oc</sub>. "
        "Để khắc phục, ngành công nghiệp pin mặt trời (công nghệ TOPCon và Silicon Heterojunction &mdash; HJT) đã phát minh hai chiến lược thụ động hóa đỉnh cao:<br/>"
        "1. <b>Thụ động hóa hóa học (Chemical Passivation):</b> Lắng đọng lớp màng mỏng vô định hình SiO<sub>2</sub> siêu mỏng (cỡ 1,2 nm) hoặc Al<sub>2</sub>O<sub>3</sub> "
        "để các nguyên tử Oxy và Hydro liên kết bão hòa hoàn toàn các liên kết treo của Silic, giảm mật độ bẫy <i>N</i><sub>st</sub> xuống dưới 10<sup>10</sup> cm<sup>-2</sup>.<br/>"
        "2. <b>Thụ động hóa trường điện (Field-Effect Passivation):</b> Tích hợp điện tích cố định âm khổng lồ trong màng Al<sub>2</sub>O<sub>3</sub> "
        "(mật độ <i>Q</i><sub>f</sub> &asymp; &minus;10<sup>13</sup> cm<sup>-2</sup>) tạo điện trường uốn dải năng lượng đẩy lùi các electron thiểu số khỏi bề mặt, "
        "khiến <i>S</i> giảm xuống mức kỷ lục <i>S</i> &lt; 2 cm&middot;s<sup>-1</sup>, đưa hiệu suất chuyển đổi quang năng của pin mặt trời vượt mốc 25%."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.3.4: TÁI HỢP AUGER BA HẠT VÀ SUY GIẢM HIỆU SUẤT
    # =========================================================================
    add_p("Luận điểm 2.3.4: Tái hợp Auger ba hạt mang điện ở mật độ kích thích cao và hiện tượng suy giảm hiệu suất lượng tử", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Khi mật độ hạt mang điện trong chất bán dẫn tăng lên mức rất cao (<i>n</i>, <i>p</i> &gt; 10<sup>18</sup> cm<sup>-3</sup>, đạt được khi pha tạp cực nặng "
        "hoặc khi tiêm dòng điện mật độ cao trong Laser Diode và LED công suất), xác suất va chạm đồng thời của ba hạt mang điện tăng vọt. "
        "Quá trình tái hợp Auger (Pierre Auger, 1923) là một quá trình va chạm ba hạt phi bức xạ (Non-radiative Three-Particle Process). "
        "Trong quá trình này, một electron tái hợp với một lỗ trống, nhưng thay vì phát ra photon ánh sáng, toàn bộ năng lượng vùng cấm giải phóng "
        "được truyền trực tiếp cho một hạt thứ ba (một electron thứ hai trong vùng dẫn hoặc một lỗ trống thứ hai trong vùng hóa trị).<br/>"
        "↳ Tái hợp Auger (Auger Recombination): Quá trình tiêu tán năng lượng tái hợp thành động năng của hạt tải nóng thứ ba.<br/>"
        "Hạt tải thứ ba sau khi nhận năng lượng khổng lồ sẽ bị kích thích vọt lên trạng thái năng lượng rất cao (hạt nóng), "
        "sau đó nhường dần năng lượng cho mạng tinh thể dưới dạng nhiệt lượng thông qua chuỗi va chạm tán xạ phonon liên tiếp."
    )
    add_spacer(6)
    
    add_p(
        "Nghịch lý suy giảm hiệu suất ở mật độ dòng cao (LED Efficiency Droop): Để chế tạo đèn LED chiếu sáng công suất cao hoặc Laser Diode, "
        "các kỹ sư mong muốn tăng dòng điện phân cực để kích thích phát xạ càng nhiều photon càng tốt. "
        "Tuy nhiên, thực nghiệm luôn ghi nhận một hiện tượng trớ trêu: khi tăng dòng điện qua linh kiện vượt quá một ngưỡng nhất định, "
        "hiệu suất phát quang lượng tử nội tại (Internal Quantum Efficiency &mdash; IQE) không tăng mà lại tụt dốc không phanh. "
        "Nguyên nhân cốt tử của nghịch lý này chính là sự bùng nổ của tái hợp Auger: tốc độ tái hợp phát xạ quang chỉ tăng theo bậc hai của nồng độ hạt tải (<i>U</i><sub>rad</sub> &prop; <i>n</i><sup>2</sup>), "
        "trong khi tốc độ tái hợp Auger tăng theo bậc ba (<i>U</i><sub>Auger</sub> &prop; <i>n</i><sup>3</sup>). "
        "Ở nồng độ cao, tái hợp Auger áp đảo hoàn toàn, biến điện năng thành nhiệt lượng phá hủy linh kiện."
    )
    add_spacer(6)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    nom_rows_2_3_4 = [
        ("Tốc độ tái hợp Auger", "<i>U</i><sub>Auger</sub>", "cm<sup>-3</sup>&middot;s<sup>-1</sup>", "Tổng tốc độ tái hợp ba hạt gồm quá trình electron-electron-lỗ trống (eeh) và electron-lỗ trống-lỗ trống (ehh)."),
        ("Hệ số Auger electron", "<i>C</i><sub>n</sub>", "cm<sup>6</sup>&middot;s<sup>-1</sup>", "Hệ số tỷ lệ quá trình va chạm eeh (khoảng 2,8 &times; 10<sup>-31</sup> cm<sup>6</sup>&middot;s<sup>-1</sup> trong Si ở 300 K)."),
        ("Hệ số Auger lỗ trống", "<i>C</i><sub>p</sub>", "cm<sup>6</sup>&middot;s<sup>-1</sup>", "Hệ số tỷ lệ quá trình va chạm ehh (khoảng 9,9 &times; 10<sup>-32</sup> cm<sup>6</sup>&middot;s<sup>-1</sup> trong Si ở 300 K)."),
        ("Thời gian sống Auger", "<i>&tau;</i><sub>Auger</sub>", "s", "Thời gian sống hạt tải giới hạn bởi cơ chế Auger, xác định bởi nghịch đảo của tích số giữa hệ số <i>C</i><sub>n</sub> và bình phương mật độ electron <i>n</i><sup>2</sup>."),
        ("Nồng độ hạt tải đa số", "<i>n</i>", "cm<sup>-3</sup>", "Mật độ electron trong vùng dẫn bán dẫn loại n pha tạp cao.")
    ]
    story.append(he.build_target_equation_block(
        r"U_{\mathrm{Auger}} = C_n n^2 p + C_p n p^2 \approx C_n n^2 \Delta p = \frac{\Delta p}{\tau_{\mathrm{Auger}}}",
        nom_rows_2_3_4,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một bàn bi-a có ba quả bóng đang chuyển động trên mặt bàn. "
        "Quả bóng trắng (electron) va chạm trực diện với quả bóng đỏ (lỗ trống) để rơi xuống lỗ (tái hợp). "
        "Nếu trên bàn chỉ có hai quả bóng, cú va chạm sẽ phát ra một tiếng kêu 'tách' giòn giã vang khắp phòng (phát xạ photon ánh sáng). "
        "Tuy nhiên, nếu mặt bàn bi-a bị nén chặt hàng trăm quả bóng chen chúc (mật độ hạt tải cao), đúng khoảnh khắc bóng trắng va chạm với bóng đỏ, "
        "nó đồng thời đập văng vào một quả bóng vàng thứ ba đứng ngay sát cạnh. "
        "Toàn bộ động năng của cú va chạm không phát ra tiếng kêu mà truyền nguyên vẹn đẩy quả bóng vàng bắn vọt đi với tốc độ kinh hoàng (tái hợp Auger). "
        "Quá trình này biến bàn bi-a thành một lò nhiệt va đập hỗn loạn mà không tạo ra bất kỳ tiếng nhạc du dương nào."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    
    # Embed Hình 2.19
    story.append(he.embed_figure_with_caption(
        fig_goc_2_19,
        "Hình 2.19: Sơ đồ cơ chế vi mô của quá trình tái hợp Auger truyền năng lượng cho hạt mang điện thứ ba (Slide 23 HUST). "
        "Ba mắt xích vật lý: (a) Electron 1 trong vùng dẫn tái hợp với lỗ trống trong vùng hóa trị giải phóng năng lượng xấp xỉ <i>E</i><sub>g</sub>; "
        "(b) Electron thứ 2 trong vùng dẫn hấp thụ trọn vẹn năng lượng này nhảy vọt lên trạng thái năng lượng cao; "
        "(c) Electron nóng nhường năng lượng cho mạng tinh thể qua chuỗi tán xạ phát xạ phonon liên tiếp.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.3.4
    story.append(he.build_intermediate_equation(
        "Dẫn xuất quy luật phụ thuộc bậc ba của tốc độ tái hợp Auger theo tích nồng độ hạt mang điện:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tốc độ tái hợp ba hạt phân tách thành hai kênh độc lập tương ứng hạt thứ ba là electron hoặc lỗ trống:",
        r"U_{\mathrm{Auger}} = R_{\mathrm{Auger}} - G_{\mathrm{Auger}} = (C_n n + C_p p) (n p - n_i^2) \approx C_n n^2 \Delta p \quad (\text{trong bán dẫn loại n pha nặng } n \gg p)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.3.4
    story.append(he.build_intermediate_equation(
        "Tổng hợp thời gian sống hiệu dụng toàn phần của hạt tải theo quy tắc cộng nghịch đảo Matthiessen:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hợp nhất đồng thời 4 cơ chế tái hợp (Bức xạ trực tiếp, Gián tiếp SRH, Auger và Bề mặt):",
        r"\frac{1}{\tau_{\mathrm{eff}}} = \frac{1}{\tau_{\mathrm{SRH}}} + \frac{1}{\tau_{\mathrm{rad}}} + \frac{1}{\tau_{\mathrm{Auger}}} + \frac{1}{\tau_{\mathrm{surface}}} = \frac{1}{\tau_{\mathrm{SRH}}} + B n + C_n n^2 + \frac{2 S}{W}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.2
    story.append(he.embed_figure_with_caption(
        fig_sim_2,
        "Hình mô phỏng 2.2: So sánh tốc độ tái hợp của 4 cơ chế và đặc tuyến suy giảm thời gian sống hiệu dụng chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Tốc độ tái hợp <i>U</i> của 4 cơ chế theo nồng độ hạt tải đa số: cơ chế SRH và bề mặt thống trị ở nồng độ thấp (<i>n</i> &lt; 10<sup>17</sup> cm<sup>-3</sup>), "
        "trong khi tái hợp Auger tăng vọt theo <i>n</i><sup>2</sup> và áp đảo hoàn toàn ở nồng độ cao (<i>n</i> &gt; 10<sup>18</sup> cm<sup>-3</sup>); "
        "(b) Thời gian sống hiệu dụng &tau;<sub>eff</sub> duy trì cao nguyên ở dải nồng độ thấp và sụp đổ dốc đứng tỷ lệ nghịch với <i>n</i><sup>2</sup> ở nồng độ cao do hiệu ứng Auger.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Thách thức Auger trong Laser Diode công suất cao và Pin mặt trời hội tụ: Trong các diode laser viễn thông dải bước sóng 1,3 &mu;m và 1,55 &mu;m "
        "(sử dụng vật liệu bán dẫn vùng cấm hẹp InGaAsP), độ rộng vùng cấm <i>E</i><sub>g</sub> xấp xỉ khoảng cách tách mức spin-quỹ đạo &Delta;<sub>so</sub>. "
        "Sự cộng hưởng năng lượng này làm hệ số Auger tăng vọt gấp hàng trăm lần so với GaAs, dẫn đến dòng ngưỡng kích hoạt laser <i>I</i><sub>th</sub> "
        "nhạy cảm khủng khiếp với nhiệt độ (hệ số nhiệt độ đặc trưng <i>T</i><sub>0</sub> tụt xuống chỉ còn 50 &minus; 70 K). "
        "Để khống chế tái hợp Auger, các kỹ sư quang tử bắt buộc phải sử dụng cấu trúc giếng lượng tử biến dạng nén (Strained Quantum Wells), "
        "làm biến dạng dải hóa trị để tách dải lỗ trống nặng và lỗ trống nhẹ, triệt tiêu điều kiện bảo toàn năng lượng &ndash; xung lượng của quá trình Auger."
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
        "<b>Ca chẩn đoán 1: Bẫy điểm mù suy giảm hiệu suất lượng tử LED (Efficiency Droop) do xem nhẹ cơ chế Auger.</b><br/>"
        "Một nhóm kỹ sư thiết kế đèn LED công suất cao InGaN/GaN phát xạ ánh sáng xanh lam quan sát thấy hiệu suất lượng tử nội tại (IQE) "
        "đạt đỉnh cực đại 85% tại mật độ dòng điện rất thấp <i>J</i> = 10 A&middot;cm<sup>-2</sup>. "
        "Tuy nhiên, khi tăng dòng bơm lên <i>J</i> = 200 A&middot;cm<sup>-2</sup> để tăng độ rọi chiếu sáng, IQE bị tụt dốc thảm hại xuống dưới 45%. "
        "Báo cáo kỹ thuật ban đầu cho rằng nguyên nhân do chất lượng tinh thể kém làm tăng đột biến mật độ tâm sai hỏng bẫy sâu SRH khi nhiệt độ tăng.<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Sử dụng mô hình tốc độ tái hợp ABC (<i>R</i> = <i>An</i> + <i>Bn</i><sup>2</sup> + <i>Cn</i><sup>3</sup>), "
        "hãy giải trình tại sao kết luận của bản báo cáo kỹ thuật là sai lầm hoàn toàn? "
        "Tại sao cơ chế tái hợp SRH (số hạng <i>An</i>) không thể là thủ phạm gây ra hiện tượng tụt dốc hiệu suất ở mật độ dòng cao? "
        "Phân tích vai trò thống trị của số hạng Auger <i>Cn</i><sup>3</sup> và đề xuất giải pháp kỹ thuật mở rộng thể tích giếng lượng tử để cứu vãn IQE.",
        "Body"
    )
    add_spacer(8)
    
    # Ca chẩn đoán 2
    add_p(
        "<b>Ca chẩn đoán 2: Bẫy điểm mù trong kiểm chuẩn phiến Silic pin mặt trời bằng phương pháp phân rã huỳnh quang vi sóng (&mu;-PCD).</b><br/>"
        "Một kỹ sư phòng sạch sử dụng thiết bị đo huỳnh quang vi sóng &mu;-PCD để kiểm tra phẩm chất một phiến Silic loại p mới sản xuất "
        "có bề dày <i>W</i> = 150 &mu;m. Kết quả đo thời gian sống hạt tải ghi nhận giá trị rất thấp <i>&tau;</i><sub>meas</sub> = 15 &mu;s. "
        "Kỹ sư lập tức kết luận mẻ nấu Silic bị ô nhiễm kim loại nặng Fe/Cu nghiêm trọng và yêu cầu loại bỏ toàn bộ lô phiến bán dẫn.<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Áp dụng quy tắc cộng nghịch đảo Matthiessen giữa thời gian sống thể tích khối <i>&tau;</i><sub>bulk</sub> "
        "và thời gian sống bề mặt <i>&tau;</i><sub>surface</sub> (xác định bởi tỉ số giữa bề dày <i>W</i> và hai lần vận tốc tái hợp bề mặt <i>S</i>), hãy chỉ ra lỗ hổng chết người trong quy trình đo đạc của kỹ sư trên. "
        "Nếu bề mặt phiến Silic chưa được thụ động hóa và có vận tốc tái hợp bề mặt <i>S</i> = 10<sup>4</sup> cm&middot;s<sup>-1</sup>, "
        "thì giá trị <i>&tau;</i><sub>meas</sub> = 15 &mu;s thực chất phản ánh đại lượng nào? "
        "Quy trình xử lý hóa học ngâm dung dịch cồn I-ốt (Iodine/Ethanol) trước khi đo sẽ làm thay đổi kết quả như thế nào?",
        "Body"
    )
    add_spacer(8)
    
    # Khối Phản biện (Silent Drop)
    add_p(
        "<b>Khối Phản biện Nguyên lý Đầu (Silent Drop &mdash; Giảng viên kỳ cựu gửi Bùi Trung Dũng):</b><br/>"
        "Trong các giáo trình vật lý bán dẫn kinh điển, người ta thường phân định rạch ròi: bán dẫn vùng cấm thẳng (GaAs) thì tái hợp trực tiếp bức xạ chiếm ưu thế, "
        "còn bán dẫn vùng cấm xiên (Si) thì tái hợp gián tiếp qua bẫy sâu SRH chiếm ưu thế.<br/>"
        "↳ <i>Câu hỏi đối trọng:</i> Hãy xem xét một phiến Silic siêu tinh khiết (Floating-Zone Silicon) với độ sạch tuyệt đối không có bất kỳ tâm bẫy tạp chất kim loại nào (<i>N</i><sub>t</sub> &rarr; 0), "
        "được thụ động hóa bề mặt hoàn hảo (<i>S</i> &rarr; 0). "
        "Khi chiếu laser công suất cao đưa nồng độ hạt tải lên mức <i>n</i> = 10<sup>19</sup> cm<sup>-3</sup>, "
        "cơ chế tái hợp nào sẽ thiết lập giới hạn vật lý tối hậu (Ultimate Physical Limit) đối với thời gian sống của hạt tải trong phiến Silic này? "
        "Tại sao trong điều kiện đó, việc tiếp tục tinh chế độ sạch tinh thể không còn mang lại bất kỳ tác dụng nào nữa?",
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
    build_monograph_muc_2_3()

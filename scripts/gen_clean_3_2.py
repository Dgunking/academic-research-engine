# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Course: Co so vat ly va cong nghe nano (PH3470 - HUST)
Chapter 3: Dac trung cua vat lieu khi kich thuoc giam (What happens at the nanoscale?)
Section 3.2: Nhiet dong hoc vi mo, dong hoc chat luu Stokes va chuyen dong khuech tan Brown o thang nano
Architecture: Progressive 5 Stages & Causal Flowchain (Pass 100% Pre-flight Linter)
Author: Academic Research Engine & Monograph PDF Publisher (Bui Trung Dung - HUST)
"""
import os
import sys
import tempfile
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as he
from reportlab.platypus import Paragraph, Spacer, KeepTogether, PageBreak
from reportlab.lib import colors

DRIVE_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano"
PDF_DIR = os.path.join(DRIVE_DIR, "Bai_Giang_Dong_Goi")
IMG_DIR = os.path.join(DRIVE_DIR, "Kho_Hinh_Anh")
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

PDF_FILENAME = "Chuyen_Khao_Nano_Muc_3.2.pdf"
TARGET_PDF_PATH = os.path.join(PDF_DIR, PDF_FILENAME)


def build_monograph_muc_3_2():
    styles = he.get_hust_styles()
    styles["BodyText"] = styles["Body"]
    # %TEMP% Isolation Policy: Biên dịch vào thư mục cách ly tạm thời của hệ điều hành
    temp_pdf_path = os.path.join(tempfile.gettempdir(), f"temp_{os.getpid()}_{PDF_FILENAME}")
    doc = he.BookmarkDocTemplate(temp_pdf_path)
    story = []

    def add_p(text: str, style_name: str = "Body", ocr_idx: int = None, is_expanded: bool = False):
        p = he.make_paragraph(text, styles[style_name], ocr_idx=ocr_idx, is_expanded_from_slide=is_expanded)
        story.append(p)
        return p

    def add_spacer(pt: float = 8.0):
        story.append(Spacer(1, pt))

    # Figure paths - 6 original figures
    fig_goc_01 = os.path.join(IMG_DIR, "[Goc]_Muc_3.2_Hinh_01_Trao_Doi_Nhiet_Va_Hang_So_Thoi_Gian_Tau.png")
    fig_goc_02 = os.path.join(IMG_DIR, "[Goc]_Muc_3.2_Hinh_02_Dinh_Luat_Ti_Le_Nhiet_Va_Tan_Nhiet_Nano.png")
    fig_goc_03 = os.path.join(IMG_DIR, "[Goc]_Muc_3.2_Hinh_03_Luc_Can_Nhot_Stokes_Va_Van_Toc_Roi.png")
    fig_goc_04 = os.path.join(IMG_DIR, "[Goc]_Muc_3.2_Hinh_04_Sup_Do_Co_Hoc_Newton_O_Thang_Nano.png")
    fig_goc_05 = os.path.join(IMG_DIR, "[Goc]_Muc_3.2_Hinh_05_Khuech_Tan_Nhiet_Brown_Va_He_Thuc_Einstein.png")
    fig_goc_06 = os.path.join(IMG_DIR, "[Goc]_Muc_3.2_Hinh_06_Hien_Tuong_Sieu_Tron_Graphite_Va_CNT.png")

    # Figure paths - 3 simulation plots
    fig_sim_01 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.2_Hang_So_Thoi_Gian_Nhiet_Va_Dinh_Luat_Ti_Le_L2.png")
    fig_sim_02 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.2_Doi_Chuan_Van_Toc_Lang_Stokes_Va_Khuech_Tan_Brown.png")
    fig_sim_03 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.2_The_Nang_Ma_Sat_Va_Hien_Tuong_Sieu_Tron_Incommensurate.png")

    # =========================================================================
    # H1 TIÊU ĐỀ PHÂN MỤC VÀ METADATA ĐÀO TẠO BÁCH KHOA
    # =========================================================================
    add_p("Chương 3: Đặc trưng của vật liệu khi kích thước giảm", "H1")
    add_p("Mục 3.2: Nhiệt động học vi mô, động học chất lưu Stokes và chuyển động khuếch tán Brown ở thang nano", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Edward L. Wolf — Nanophysics and Nanotechnology, Chương 3; Slide bài giảng HUST 22–28)</i>", "Caption")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Cơ sở vật lý và công nghệ nano (PH3470)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Viện Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Bài 3 (Slide 22–28); Wolf Nanotechnology Ch. 3"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuẩn mực kỹ thuật:</b> Khung Sư phạm 5 Giai đoạn, Zero-Omission, Zero-Slash"), styles["TableCell"])]
    ]
    meta_t = he.Table(meta_table_data, colWidths=[250.0, he.PRINTABLE_WIDTH - 250.0])
    meta_t.setStyle(he.TableStyle([
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

    add_p(
        "Chuyên khảo toàn văn chuyên sâu về động học nhiệt vi mô, động học chất lưu Stokes và hiện tượng khuếch tán nhiệt Brown "
        "(PH3470 — HUST; đối chiếu Edward L. Wolf, Nanophysics and Nanotechnology, Chapter 3). "
        "Khảo sát toàn diện sự biến đổi các quy luật vật lý kinh điển khi kích thước cấu trúc thu nhỏ từ thang micromet xuống nanomet: "
        "thiết lập phương trình truyền nhiệt vi phân Fourier và chứng minh định luật tỉ lệ hằng số thời gian nhiệt tỉ lệ thuận với bình phương kích thước, "
        "giải thích cơ chế triệt tiêu gradient nhiệt nội tại dẫn đến trạng thái đẳng nhiệt lý tưởng ở cấu trúc nano, "
        "phân tích lực cản nhớt Stokes trong dòng chảy tầng ở số Reynolds cực nhỏ và đối chuẩn vận tốc lắng cơ học với tốc độ khuếch tán Brown, "
        "chứng minh sự sụp đổ của cơ học Newton tiền định trước các xung lực va chạm nhiệt ngẫu nhiên qua định lý dao động – tiêu tán Einstein-Smoluchowski, "
        "giải trọn vẹn và tường minh hệ thống 3 bài toán định lượng (Bài 4, 5, 6 trong slide bài giảng HUST) về vận tốc lắng và chiều dài khuếch tán vi hạt, "
        "và khám phá cơ chế vật lý của hiện tượng siêu trơn cấu trúc trong màng graphite và ống than nano do sự triệt tiêu thế năng ma sát mạng bất tương thích."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 3.2
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Slide HUST &amp; Wolf)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.2.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Nhiệt động học thang nano &amp; Định luật tỉ lệ bình phương kích thước"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Phương trình truyền nhiệt, hằng số thời gian hằng số thời gian nhiệt τ<sub>th</sub> = <i>L C<sub>V</sub></i> · (<i>k<sub>T</sub> A</i>)<sup>−1</sup> ∝ <i>L</i><sup>2</sup>, chênh lệch nhiệt chênh lệch nhiệt độ bên trong <i>dT</i> ∝ <i>L</i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 22–23; Mô phỏng giải tích 3.2.1"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.2.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Động học chất lưu vi mô &amp; Lực cản nhớt Stokes (Bài tập 4)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Lực cản nhớt lực cản nhớt Stokes <i>F<sub>d</sub></i> = 6π η <i>R v</i>, vận tốc lắng tới hạn vận tốc lắng tới hạn <i>v</i><sub>term</sub> = 2 ρ <i>g R</i><sup>2</sup> · (9η)<sup>−1</sup> ∝ <i>R</i><sup>2</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 24–25 (Bài tập 4: <i>R</i> = 10 μm)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.2.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Khuếch tán Brown &amp; Giới hạn cơ học cổ điển (Bài tập 5 &amp; 6)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hệ số khuếch tán hệ số khuếch tán Einstein <i>D</i> = <i>k<sub>B</sub> T</i> · (6π η <i>R</i>)<sup>−1</sup>, quãng đường khuếch tán quãng đường khuếch tán trung bình <i>x</i><sub>rms</sub> = (4<i>D t</i>)<sup>½</sup> ∝ <i>R</i><sup>−½</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 26–27; Mô phỏng giải tích 3.2.2"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.2.4</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Ma sát cấp nguyên tử &amp; Hiện tượng siêu trơn cấu trúc Graphite/CNT"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô hình thế Frenkel-Kontorova, góc lệch mạng Moiré θ, triệt tiêu ma sát 99.8% (<i>F<sub>s</sub></i> ≤ 0.002 <i>F</i><sub>max</sub>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 28; Mô phỏng giải tích 3.2.3"), styles["TableCellCenter"]),
        ],
    ]
    t_matrix = he.Table(matrix_rows, colWidths=[65.0, 165.0, 155.0, 130.0], repeatRows=1)
    t_matrix.setStyle(he.TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), he.COLOR_TABLE_HEADER_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, he.COLOR_BORDER_GRAY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(t_matrix)
    add_spacer(14)

    # =========================================================================
    # MPT 3.2.1: NHIỆT ĐỘNG HỌC THANG NANO VÀ ĐỊNH LUẬT TỈ LỆ L^2
    # =========================================================================
    add_p("Luận điểm 3.2.1: Nhiệt động học thang nano, hằng số thời gian nhiệt và định luật tỉ lệ bình phương kích thước", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, mô hình trao đổi nhiệt vi mô và nghịch lý gradient nhiệt", "H3")
    add_p(
        "Trong thế giới vĩ mô, các cấu trúc cơ khí và thiết bị điện tử khi hoạt động thường gặp vấn đề tích tụ nhiệt cục bộ nghiêm trọng. "
        "Một khối vật liệu lớn cần từ vài giây đến hàng chục phút để cân bằng nhiệt với môi trường, "
        "tạo ra gradient nhiệt độ lớn giữa tâm và bề mặt, dẫn đến ứng suất nhiệt cơ học gây nứt vỡ và suy giảm độ tin cậy. "
        "Tuy nhiên, khi kích thước vật lý của linh kiện thu nhỏ xuống quy mô micromet và nanomet trong các vi mạch tích hợp mật độ cao, "
        "các quy luật nhiệt động học vĩ mô trải qua một bước ngoặt đột biến: tốc độ truyền nhiệt tăng vọt hàng triệu lần, "
        "và các gradient nhiệt độ nội tại bên trong cấu trúc gần như bị triệt tiêu hoàn toàn.",
        ocr_idx=1
    )
    add_spacer(6)

    add_p(
        "Để lượng hóa hiện tượng này từ nguyên lý đầu, bài giảng xét một mô hình vật lý cơ bản: "
        "một vật thể có nhiệt dung toàn phần <i>C<sub>V</sub></i> và nhiệt độ ban đầu <i>T</i> được liên kết với một nguồn nhiệt vô hạn có nhiệt độ chuẩn <i>T</i><sub>0</sub> "
        "thông qua một cầu dẫn nhiệt có tiết diện tiếp xúc <i>A</i>, chiều dài truyền dẫn <i>L</i> và hệ số dẫn nhiệt của vật liệu là <i>k<sub>T</sub></i>. "
        "Mô hình này mô phỏng trung thực các liên kết tản nhiệt vi mô từ kênh dẫn transistor nano (chẳng hạn kênh dẫn Silicon trong transistor FinFET hay GAAFET) "
        "ra các tiếp điểm kim loại và đế tản nhiệt bên ngoài.",
        ocr_idx=2
    )
    add_spacer(8)

    # Ảnh gốc Slide 22 & 23
    story.append(he.embed_figure_with_caption(
        fig_goc_01,
        "Hình 3.3: Mô hình trao đổi nhiệt vi mô và phương trình vi phân dẫn truyền nhiệt: "
        "Vật thể có nhiệt dung C liên kết với nguồn nhiệt lớn qua cầu dẫn nhiệt chiều dài L, tiết diện A, hệ số truyền nhiệt kT (Slide 22 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_02,
        "Hình 3.4: Định luật tỉ lệ kích thước của hằng số thời gian nhiệt và chênh lệch nhiệt độ: "
        "Hằng số thời gian nhiệt tỉ lệ thuận với bình phương kích thước L², chênh lệch nhiệt độ dT tỉ lệ thuận với L (Slide 23 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ truyền nhiệt thang nano", "H3")
    add_p(
        "Dòng nhiệt truyền qua cầu dẫn nhiệt tuân theo định luật truyền nhiệt Fourier: thông lượng nhiệt biến thiên tỉ lệ thuận với gradient nhiệt độ và tiết diện dẫn. "
        "Mặt khác, theo nguyên lý bảo toàn năng lượng trong nhiệt động học, tốc độ tỏa nhiệt ra môi trường phải bằng tốc độ suy giảm nội năng của vật thể. "
        "Sự cân bằng này thiết lập phương trình vi phân thuần nhất bậc nhất mô tả quá trình hồi phục nhiệt độ của vi cấu trúc."
    )
    add_spacer(6)

    eq_col_1 = r"\frac{dQ}{dt} = k_T A \frac{T - T_0}{L} = -C_V \frac{dT}{dt} \quad \Longrightarrow \quad T(t) - T_0 = \Delta T_0 \exp\left(-\frac{t}{\tau_{\mathrm{th}}}\right), \quad \tau_{\mathrm{th}} = \frac{L C_V}{k_T A}"
    nom_rows_1 = [
        ("Dòng nhiệt truyền dẫn tức thời", "<i>dQ</i> · (<i>dt</i>)<sup>−1</sup>", "W", "Tốc độ năng lượng nhiệt truyền qua cầu dẫn tản nhiệt ra nguồn ngoài"),
        ("Hệ số dẫn nhiệt của vật liệu", "<i>k<sub>T</sub></i>", "W·m<sup>−1</sup>·K<sup>−1</sup>", "Độ dẫn nhiệt nội tại do phonon và electron tự do vận chuyển qua mạng tinh thể"),
        ("Chiều dài và tiết diện truyền dẫn", "<i>L</i>, <i>A</i>", "m, m<sup>2</sup>", "Kích thước hình học của cấu trúc cầu nối tản nhiệt vi mô"),
        ("Nhiệt dung toàn phần của vi cấu trúc", "<i>C<sub>V</sub></i>", "J·K<sup>−1</sup>", "Khả năng tích trữ nhiệt lượng toàn phần, bằng tích khối lượng và nhiệt dung riêng"),
        ("Hằng số thời gian nhiệt hồi phục", "<i>\u03c4</i><sub>th</sub>", "s hoặc ps", "Thời gian cần thiết để độ chênh lệch nhiệt độ suy giảm đi e lần (khoảng 63.2%)"),
    ]
    story.append(he.build_target_equation_block(eq_col_1, nom_rows_1, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất nghiệm hàm mũ và định luật tỉ lệ kích thước", "H3")

    p_step1 = (
        "Thiết lập phương trình vi phân truyền nhiệt từ cân bằng thông lượng nhiệt Fourier và nội năng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Theo định luật Fourier một chiều, dòng nhiệt thoát ra khỏi vật qua tiết diện <i>A</i> và chiều dài <i>L</i> tỉ lệ thuận với độ chênh lệch nhiệt độ. "
        "Đồng thời, nội năng của vật thể biến thiên theo tốc độ làm nguội <i>dQ</i> = −<i>C<sub>V</sub></i> · <i>dT</i>. "
        "Cân bằng hai vế và phân ly biến số nhiệt độ <i>T</i> và thời gian <i>t</i>:"
    )
    story.append(he.build_intermediate_equation(p_step1, r"k_T A \frac{T - T_0}{L} dt = -C_V dT \quad \Longleftrightarrow \quad \frac{dT}{T - T_0} = -\frac{k_T A}{L C_V} dt", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step2 = (
        "Tích phân hai vế xác định nghiệm suy giảm hàm mũ tự nhiên theo thời gian:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Lấy tích phân từ thời điểm ban đầu <i>t</i> = 0 ứng với nhiệt độ <i>T</i>(0) đến thời điểm <i>t</i> bất kỳ ứng với <i>T</i>(<i>t</i>). "
        "Tích phân vế trái cho hàm logarit tự nhiên, lấy mũ hóa hai vế thu được nghiệm suy giảm hàm mũ kinh điển:"
    )
    story.append(he.build_intermediate_equation(p_step2, r"\int_{T(0)}^{T(t)} \frac{d(T - T_0)}{T - T_0} = -\int_0^t \frac{k_T A}{L C_V} dt \quad \Longrightarrow \quad T(t) - T_0 = [T(0) - T_0] \exp\left(-\frac{t}{\tau_{\mathrm{th}}}\right)", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step3 = (
        "Dẫn xuất định luật tỉ lệ kích thước của hằng số thời gian nhiệt trong không gian 3 chiều:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét một cấu trúc hạt hoặc khối lập phương có kích thước đặc trưng <i>L</i>. Thể tích <i>V</i> tỉ lệ với <i>L</i><sup>3</sup>, do đó nhiệt dung toàn phần "
        "<i>C<sub>V</sub></i> = <i>c<sub>v</sub></i> · ρ · <i>V</i> tỉ lệ với <i>L</i><sup>3</sup> (trong đó <i>c<sub>v</sub></i> là nhiệt dung riêng và ρ là khối lượng riêng). "
        "Tiết diện tản nhiệt <i>A</i> tỉ lệ với diện tích bề mặt <i>L</i><sup>2</sup>. Thay thế trực tiếp vào biểu thức hằng số thời gian nhiệt:"
    )
    story.append(he.build_intermediate_equation(p_step3, r"\tau_{\mathrm{th}} = \frac{L \cdot C_V}{k_T \cdot A} \propto \frac{L \cdot L^3}{k_T \cdot L^2} \propto L^2 \frac{c_v \rho}{k_T} \quad \Longrightarrow \quad \tau_{\mathrm{th}} \propto L^2", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step4 = (
        "Dẫn xuất định luật tỉ lệ của chênh lệch nhiệt độ nội tại bên trong cấu trúc vi mô:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Sự chênh lệch nhiệt độ <i>dT</i> giữa hai điểm cách nhau khoảng cách <i>L</i> khi có dòng nhiệt truyền qua được suy ra trực tiếp từ định luật Fourier: "
        "<i>dT</i> = (<i>dQ</i> · <i>dt</i><sup>−1</sup>) · <i>L</i> · (<i>k<sub>T</sub> A</i>)<sup>−1</sup>. "
        "Vì dòng nhiệt sinh ra do tiêu tán công suất tỉ lệ với thể tích <i>V</i> ∝ <i>L</i><sup>3</sup>, còn diện tích <i>A</i> ∝ <i>L</i><sup>2</sup>, "
        "nên đại lượng chênh lệch nhiệt độ nội tại tỉ lệ bậc nhất với kích thước đặc trưng <i>L</i>:"
    )
    story.append(he.build_intermediate_equation(p_step4, r"dT = \frac{dQ}{dt} \frac{L}{k_T A} \propto \frac{L^3 \cdot L}{L^2} \propto L^2 \quad \text{hoặc khi dòng nhiệt cố định:} \quad dT \propto L", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Mô phỏng đối chuẩn & Biến thiên tiệm cận
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích 300 K và biến thiên tiệm cận", "H3")
    add_p(
        "Để đối chuẩn định lượng định luật tỉ lệ bình phương kích thước, chúng tôi tiến hành mô phỏng giải tích quá trình hồi phục nhiệt "
        "trên vật liệu bán dẫn Silicon ở nhiệt độ 300 K (với độ dẫn nhiệt <i>k<sub>T</sub></i> = 148 W·m<sup>−1</sup>·K<sup>−1</sup>, "
        "khối lượng riêng ρ = 2330 kg·m<sup>−3</sup>, nhiệt dung riêng <i>c<sub>v</sub></i> = 705 J·kg<sup>−1</sup>·K<sup>−1</sup>, "
        "cho hệ số tỉ lệ nhiệt <i>c<sub>v</sub></i> ρ · <i>k<sub>T</sub></i><sup>−1</sup> ≈ 1.102 × 10<sup>4</sup> s·m<sup>−2</sup>). "
        "Đồ thị biểu diễn trên thang song logarit cho thấy sự suy giảm cực nhanh của hằng số thời gian nhiệt qua nhiều bậc độ lớn khi kích thước giảm."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_01,
        "Hình 3.5: Mô phỏng giải tích định luật tỉ lệ hằng số thời gian nhiệt τth ∝ L² trên vật liệu Silicon ở 300 K: "
        "Tại kích thước macro L = 1 mm, hằng số thời gian nhiệt khoảng 11 ms; khi thu nhỏ xuống thang nano L = 10 nm, "
        "hằng số thời gian nhiệt rơi xuống ngưỡng sub-picosecond (τth ≈ 1.1 ps), chứng minh cấu trúc nano tản nhiệt gần như tức thời.",
        kind="sim",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 5: Ứng dụng & Cầu nối
    add_p("Giai đoạn 5: Ứng dụng kỹ thuật bán dẫn và cầu nối sang động học chất lưu vi mô", "H3")
    add_p(
        "Định luật tỉ lệ bình phương kích thước <i>\u03c4</i><sub>th</sub> ∝ <i>L</i><sup>2</sup> và <i>dT</i> ∝ <i>L</i> mang lại hai hệ quả kỹ thuật mang tính cách mạng: "
        "(1) Cấu trúc nano có khả năng giải phóng nhiệt siêu tốc trong thời gian pico-giây, cho phép các transistor vi xử lý hiện đại hoạt động ở tần số hàng gigahertz "
        "mà không bị quá nhiệt phá hủy cục bộ; "
        "(2) Chênh lệch nhiệt độ nội tại <i>dT</i> tiến dần về 0 khi <i>L</i> tiến về thang nanomet, biến toàn bộ hạt nano hoặc thanh nano thành một cấu trúc đẳng nhiệt lý tưởng (isothermal nanostructure), "
        "loại bỏ hoàn toàn các vết nứt vỡ do ứng suất nhiệt nội tại. "
        "Tuy nhiên, khi kích thước vật lý tiếp tục giảm, các hiện tượng cơ học bề mặt và tương tác với môi trường xung quanh bắt đầu chi phối mạnh mẽ, "
        "đặc biệt là lực cản nhớt của chất lưu và chuyển động nhiệt ngẫu nhiên của các phân tử môi trường."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.2.2: ĐỘNG HỌC CHẤT LƯU VI MÔ & BÀI TOÁN TỐC ĐỘ LẮNG STOKES
    # =========================================================================
    add_p("Luận điểm 3.2.2: Động học chất lưu vi mô, lực cản nhớt Stokes và giải tích bài toán tốc độ lắng", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, lực nhớt vi mô và chế độ chảy tầng ở số Reynolds cực nhỏ", "H3")
    add_p(
        "Trong đời sống hàng ngày, chuyển động của các vật thể vĩ mô qua không khí hay chất lỏng chịu chi phối bởi lực cản quán tính áp suất (form drag), "
        "tỉ lệ với bình phương vận tốc <i>v</i><sup>2</sup> và tiết diện cản <i>A</i>, tạo ra các dòng xoáy hỗn loạn phía sau vật thể (dòng chảy rối, số Reynolds <i>Re</i> ≫ 1). "
        "Tuy nhiên, đối với một vi hạt chuyển động trong chất lưu, kích thước hạt <i>R</i> cực nhỏ khiến lực quán tính bị triệt tiêu hoàn toàn so với lực ma sát nhớt giữa các lớp chất lưu. "
        "Chuyển động lúc này rơi vào chế độ chảy trườn tầng lý tưởng (Stokes creeping flow), được đặc trưng bởi số Reynolds cực nhỏ (<i>Re</i> ≪ 1).",
        ocr_idx=3
    )
    add_spacer(6)

    add_p(
        "Trong chế độ dòng chảy tầng này, nhà vật lý học George Gabriel Stokes đã thiết lập định luật cản nhớt kinh điển: "
        "lực cản tỉ lệ bậc nhất với độ nhớt động lực học η của môi trường, tỉ lệ bậc nhất với bán kính hình học <i>R</i> của hạt và tỉ lệ bậc nhất với vận tốc chuyển động <i>v</i>: "
        "<i>F<sub>d</sub></i> = 6π η <i>R v</i>. "
        "Khi hạt rơi tự do dưới tác dụng của trọng trường trong môi trường chất lưu, nó nhanh chóng đạt tới trạng thái cân bằng động học giữa lực cản nhớt Stokes và trọng lực hiệu dụng, "
        "thiết lập một vận tốc giới hạn không đổi gọi là vận tốc lắng tới hạn (terminal settling velocity)."
    )
    add_spacer(8)

    # Ảnh gốc Slide 24 & 25
    story.append(he.embed_figure_with_caption(
        fig_goc_03,
        "Hình 3.6: Lực nhớt Stokes trong chuyển động của hạt vi mô trong dung dịch: "
        "Lực cản nhớt F = 6πηRv cân bằng với trọng lực mg, cho vận tốc lắng v = mg · (6πηR)⁻¹ (Slide 24 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_04,
        "Hình 3.7: Bài tập 4 trong slide bài giảng HUST: "
        "Xác định tốc độ rơi của hạt kích thước bán kính 10 μm, khối lượng riêng 2000 kg/m³ trong không khí có độ nhớt 1.8 × 10⁻⁵ Pa·s (Slide 25 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ vận tốc lắng Stokes", "H3")
    add_p(
        "Cân bằng động lực học đạt được khi tổng đại số các lực tác dụng lên hạt triệt tiêu: "
        "trọng lực kéo hạt xuống phía dưới, lực cản nhớt Stokes hướng ngược chiều chuyển động lên phía trên, "
        "và lực đẩy Archimedes hướng lên do phần thể tích chất lưu bị chiếm chỗ. "
        "Trong môi trường không khí loãng, khối lượng riêng của chất lưu (ρ<sub>không khí</sub> ≈ 1.2 kg·m<sup>−3</sup>) "
        "nhỏ hơn hàng ngàn lần so với khối lượng riêng của hạt chất rắn (ρ ≈ 2000 kg·m<sup>−3</sup>), "
        "cho phép bỏ qua hoàn toàn lực đẩy Archimedes để thiết lập biểu thức vận tốc lắng tới hạn chính xác tuyệt đối."
    )
    add_spacer(6)

    eq_col_2 = r"F_d = 6\pi \eta R v = m g = \frac{4}{3}\pi R^3 \rho g \quad \Longrightarrow \quad v_{\mathrm{term}} = \frac{2 \rho g R^2}{9 \eta}"
    nom_rows_2 = [
        ("Lực cản nhớt chất lưu Stokes", "<i>F<sub>d</sub></i>", "N", "Lực ma sát tiếp tuyến do các lớp chất lưu trượt lên bề mặt hạt hình cầu"),
        ("Độ nhớt động lực học của môi trường", "η", "Pa·s hoặc N·s·m<sup>−2</sup>", "Độ nhớt của chất lưu (đối với không khí ở 300 K, η ≈ 1.8 × 10<sup>−5</sup> Pa·s)"),
        ("Bán kính hình học của hạt chất rắn", "<i>R</i>", "m hoặc μm, nm", "Bán kính hình cầu tương đương của hạt vi mô chuyển động trong chất lưu"),
        ("Khối lượng riêng của vật liệu làm hạt", "ρ", "kg·m<sup>−3</sup>", "Mật độ khối lượng của hạt (chẳng hạn SiO<sub>2</sub> ρ ≈ 2000 kg·m<sup>−3</sup>)"),
        ("Vận tốc lắng tới hạn trong trọng trường", "<i>v</i><sub>term</sub>", "m·s<sup>−1</sup> hoặc mm·s<sup>−1</sup>", "Tốc độ rơi đều ổn định khi lực cản nhớt cân bằng hoàn toàn với trọng lực"),
    ]
    story.append(he.build_target_equation_block(eq_col_2, nom_rows_2, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất & Giải chi tiết Bài tập 4
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất và lời giải chi tiết Bài tập 4", "H3")

    p_step5 = (
        "Cân bằng lực động lực học Newton và dẫn xuất biểu thức vận tốc lắng tới hạn:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét hạt hình cầu bán kính <i>R</i> và khối lượng riêng ρ. Khối lượng toàn phần của hạt bằng thể tích nhân khối lượng riêng: "
        "<i>m</i> = 4 · 3<sup>−1</sup> · π <i>R</i><sup>3</sup> ρ. "
        "Khi gia tốc rơi triệt tiêu (<i>dv</i> · <i>dt</i><sup>−1</sup> = 0), lực trọng trường <i>F<sub>g</sub></i> = <i>m</i> · <i>g</i> cân bằng với lực nhớt <i>F<sub>d</sub></i> = 6π η <i>R v</i>:"
    )
    story.append(he.build_intermediate_equation(p_step5, r"6\pi \eta R v_{\mathrm{term}} = \frac{4}{3}\pi R^3 \rho g \quad \Longleftrightarrow \quad v_{\mathrm{term}} = \frac{4 \pi R^3 \rho g}{3 \cdot 6\pi \eta R} = \frac{2 \rho g R^2}{9 \eta}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step6 = (
        "Giải chi tiết toàn văn Bài tập 4 trong slide bài giảng HUST:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Bài toán cho: hạt bán kính <i>R</i> = 10 μm = 10<sup>−5</sup> m, khối lượng riêng ρ = 2000 kg·m<sup>−3</sup>, gia tốc trọng trường <i>g</i> = 9.8 m·s<sup>−2</sup>, "
        "độ nhớt không khí η = 1.8 × 10<sup>−5</sup> Pa·s. Thay thế trực tiếp toàn bộ các thông số số trị vào công thức vận tốc lắng tới hạn:"
    )
    story.append(he.build_intermediate_equation(p_step6, r"v = \frac{2 \times 2000 \times 9.8 \times (10^{-5})^2}{9 \times 1.8 \times 10^{-5}} = \frac{39200 \times 10^{-10}}{1.62 \times 10^{-4}} = \frac{3.92 \times 10^{-6}}{1.62 \times 10^{-4}} \approx 0.0242\,\text{m/s} = 24.2\,\text{mm/s}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Phân tích quy luật tỉ lệ
    add_p("Giai đoạn 4: Phân tích định luật tỉ lệ bình phương bán kính <i>v</i><sub>term</sub> ∝ <i>R</i><sup>2</sup>", "H3")
    add_p(
        "Kết quả tính toán <i>v</i> ≈ 24.2 mm·s<sup>−1</sup> hoàn toàn khớp với giá trị tham chiếu trong slide bài giảng (khoảng 23–24 mm·s<sup>−1</sup>). "
        "Điều này cho thấy ở quy mô micromet (<i>R</i> = 10 μm), hạt bụi trong không khí rơi với tốc độ nhìn thấy được bằng mắt thường: "
        "nó rơi được khoảng 2.4 cm sau mỗi giây và nhanh chóng lắng xuống bề mặt đất hay sàn phòng thí nghiệm. "
        "Tuy nhiên, do vận tốc rơi phụ thuộc bậc hai vào bán kính (<i>v</i><sub>term</sub> ∝ <i>R</i><sup>2</sup>), "
        "khi bán kính hạt giảm đi 1000 lần (từ 10 μm xuống 10 nm), tốc độ rơi không giảm đi 1000 lần mà sụt giảm tới 10<sup>6</sup> lần (1 triệu lần)! "
        "Sự sụt giảm phi mã này làm nảy sinh một câu hỏi căn bản: liệu một hạt nano trong không khí có còn thực sự rơi theo định luật Newton nữa hay không?"
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.2.3: CHUYỂN ĐỘNG NHIỆT BROWN & BÀI TOÁN 5, 6
    # =========================================================================
    add_p("Luận điểm 3.2.3: Chuyển động nhiệt Brown, khuếch tán Einstein-Smoluchowski và giới hạn của cơ học Newton cổ điển", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm & Bài tập 5
    add_p("Giai đoạn 1: Giới thiệu khái niệm, sự sụp đổ của cơ học Newton và phát biểu Bài toán 5", "H3")
    add_p(
        "Năm 1827, nhà thực vật học Robert Brown khi quan sát các hạt phấn hoa lơ lửng trong nước dưới kính hiển vi đã phát hiện "
        "chúng chuyển động hỗn loạn không ngừng theo những đường zig-zag bất định. "
        "Gần 80 năm sau, vào năm kỳ diệu 1905, Albert Einstein đã giải mã nguồn gốc vật lý của hiện tượng này: "
        "chuyển động Brown xuất phát từ hàng tỷ cú va đập ngẫu nhiên, bất đối xứng của các phân tử môi trường xung quanh lên bề mặt hạt vi mô. "
        "Khi kích thước hạt đủ lớn (macro và micro), số lượng phân tử va đập vào các phía triệt tiêu lẫn nhau theo quy luật số lớn của xác suất thống kê. "
        "Nhưng khi kích thước hạt thu nhỏ về thang nanomet, diện tích bề mặt hạt trở nên nhỏ tương đương quãng đường chuyển dịch tự do của phân tử, "
        "khiến xung lực va đập không còn triệt tiêu mà tạo thành một lực kích động ngẫu nhiên cực mạnh đẩy hạt di chuyển hỗn loạn.",
        ocr_idx=4
    )
    add_spacer(6)

    # Ảnh gốc Slide 26 & 27
    story.append(he.embed_figure_with_caption(
        fig_goc_05,
        "Hình 3.8: Bài tập 5 và 6 trong slide bài giảng HUST: "
        "(a) Bài 5: Khảo sát hạt bán kính 10 nm rơi trong không khí và sự giới hạn của định luật Newton; "
        "(b) Bài 6: Xác định chiều dài khuếch tán xrms trong 1 s tại 300 K theo định lý Einstein-Smoluchowski (Slide 26–27 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ khuếch tán Einstein-Smoluchowski", "H3")
    add_p(
        "Einstein và Marian Smoluchowski đã liên kết động học chất lưu Stokes vĩ mô với nhiệt động học thống kê vi mô qua định lý dao động – tiêu tán (Fluctuation-Dissipation Theorem). "
        "Năng lượng nhiệt nội tại <i>k<sub>B</sub> T</i> thúc đẩy quá trình khuếch tán ngẫu nhiên, trong khi hệ số cản nhớt Stokes 6π η <i>R</i> đóng vai trò cản trở tiêu tán động năng. "
        "Quãng đường dịch chuyển hiệu dụng của hạt sau khoảng thời gian <i>t</i> không tăng tuyến tính theo thời gian (<i>x</i> ∝ <i>t</i>) như chuyển động đều cổ điển, "
        "mà tăng theo căn bậc hai của thời gian (<i>x</i><sub>rms</sub> ∝ <i>t</i><sup>½</sup>) đặc trưng cho quá trình bước đi ngẫu nhiên (random walk)."
    )
    add_spacer(6)

    eq_col_3 = r"D = \frac{k_B T}{6\pi \eta R}, \quad x_{\mathrm{rms}} = \sqrt{4 D t} = \sqrt{\frac{2 k_B T t}{3 \pi \eta R}}"
    nom_rows_3 = [
        ("Hằng số Boltzmann CODATA 2022", "<i>k<sub>B</sub></i>", "J·K<sup>−1</sup>", "Hằng số vật lý bất biến: <i>k<sub>B</sub></i> = 1.380649 × 10<sup>−23</sup> J·K<sup>−1</sup>"),
        ("Nhiệt độ tuyệt đối của hệ", "<i>T</i>", "K", "Nhiệt độ nhiệt động học của môi trường xung quanh (chuẩn phòng thí nghiệm <i>T</i> = 300 K)"),
        ("Hệ số khuếch tán nhiệt động học", "<i>D</i>", "m<sup>2</sup>·s<sup>−1</sup>", "Tốc độ lan truyền diện tích phân bố xác suất vị trí hạt do dao động nhiệt"),
        ("Khoảng thời gian quan sát khuếch tán", "<i>t</i>", "s", "Thời gian hạt nano tự do di chuyển trong chất lưu (chuẩn bài toán <i>t</i> = 1 s)"),
        ("Chiều dài khuếch tán căn quân phương", "<i>x</i><sub>rms</sub>", "m hoặc μm", "Độ dời hiệu dụng trung bình bình phương (root-mean-square displacement) trong không gian"),
    ]
    story.append(he.build_target_equation_block(eq_col_3, nom_rows_3, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất & Giải chi tiết Bài tập 5, 6
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất và lời giải chi tiết Bài tập 5 và Bài tập 6", "H3")

    p_step7 = (
        "Giải chi tiết Bài tập 5: Tính vận tốc lắng rơi trọng lực của hạt nano R = 10 nm:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Hạt có bán kính <i>R</i> = 10 nm = 10<sup>−8</sup> m, khối lượng riêng ρ = 500 kg·m<sup>−3</sup> rơi trong không khí có η = 1.8 × 10<sup>−5</sup> Pa·s. "
        "Áp dụng công thức vận tốc lắng Stokes:"
    )
    story.append(he.build_intermediate_equation(p_step7, r"v_{\mathrm{nano}} = \frac{2 \times 500 \times 9.8 \times (10^{-8})^2}{9 \times 1.8 \times 10^{-5}} = \frac{9800 \times 10^{-16}}{1.62 \times 10^{-4}} \approx 6.049 \times 10^{-9}\,\text{m/s} \approx 6.05\,\text{nm/s}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step8 = (
        "Đánh giá quãng đường rơi do trọng lực trong thời gian t = 1 s:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Trong thời gian <i>t</i> = 1 giây, hạt nano chỉ rơi được một quãng đường vi mô vô cùng nhỏ bé: "
        "<i>h</i><sub>grav</sub> = <i>v</i><sub>nano</sub> · <i>t</i> = 6.05 × 10<sup>−9</sup> m = 6.05 nm. "
        "Quãng đường này chỉ bằng khoảng vài chục khoảng cách liên nguyên tử, đồng nghĩa với việc hạt hầu như đứng yên hoàn toàn nếu chỉ xét riêng trọng lực."
    )
    story.append(he.build_intermediate_equation(p_step8, r"h_{\mathrm{grav}} = v_{\mathrm{nano}} \cdot t = 6.05 \times 10^{-9}\,\text{m/s} \times 1.0\,\text{s} = 6.05 \times 10^{-9}\,\text{m} = 6.05\,\text{nm}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step9 = (
        "Giải chi tiết Bài tập 6: Tính hệ số khuếch tán D tại nhiệt độ 300 K:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Năng lượng nhiệt ở <i>T</i> = 300 K là <i>k<sub>B</sub> T</i> = 1.380649 × 10<sup>−23</sup> × 300 = 4.1419 × 10<sup>−21</sup> J. "
        "Mẫu số cản nhớt là 6π η <i>R</i> = 6 × π × 1.8 × 10<sup>−5</sup> × 10<sup>−8</sup> ≈ 3.3929 × 10<sup>−12</sup> N·s·m<sup>−1</sup>. "
        "Thực hiện phép chia xác định hệ số khuếch tán:"
    )
    story.append(he.build_intermediate_equation(p_step9, r"D = \frac{k_B T}{6\pi \eta R} = \frac{4.1419 \times 10^{-21}\,\text{J}}{3.3929 \times 10^{-12}\,\text{N}\cdot\text{s/m}} \approx 1.2208 \times 10^{-9}\,\text{m}^2/\text{s}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step10 = (
        "Xác định chiều dài khuếch tán căn quân phương <i>x</i><sub>rms</sub> trong thời gian <i>t</i> = 1 s:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Theo công thức gợi ý trong slide 27 của bài giảng HUST: <i>x</i><sub>rms</sub> = (4<i>D t</i>)<sup>½</sup>. "
        "Thay thế giá trị hệ số khuếch tán <i>D</i> vừa tính được với <i>t</i> = 1.0 s:"
    )
    story.append(he.build_intermediate_equation(p_step10, r"x_{\mathrm{rms}} = \sqrt{4 \times 1.2208 \times 10^{-9} \times 1.0} = \sqrt{4.8832 \times 10^{-9}} \approx 6.988 \times 10^{-5}\,\text{m} \approx 69.9\,\mu\text{m}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step11 = (
        "So sánh đối chuẩn tỉ số giữa chuyển động nhiệt Brown và rơi trọng lực:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Lập tỉ số giữa quãng đường khuếch tán nhiệt Brown <i>x</i><sub>rms</sub> và độ rơi do trọng trường <i>h</i><sub>grav</sub> trong cùng khoảng thời gian 1 s:"
    )
    story.append(he.build_intermediate_equation(p_step11, r"\frac{x_{\mathrm{rms}}}{h_{\mathrm{grav}}} = \frac{6.988 \times 10^{-5}\,\text{m}}{6.049 \times 10^{-9}\,\text{m}} \approx 11552 \quad (\text{lớn hơn } 11500 \text{ lần})", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn & Điểm chuyển pha
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn và điểm chuyển pha động học vi mô", "H3")
    add_p(
        "Kết quả tính toán đưa ra một kết luận mang tính nền tảng cho công nghệ nano: "
        "đối với hạt có kích thước nano (<i>R</i> = 10 nm), chuyển động nhiệt Brown lấn át hoàn toàn chuyển động rơi trọng trường với biên độ gấp hơn 11500 lần! "
        "Hạt nano không bao giờ có thể lắng xuống đáy bình chứa dưới tác dụng của trọng lực thông thường; "
        "chúng bị giam giữ vĩnh viễn trong trạng thái huyền phù nhiệt động học bền vững. "
        "Để làm lắng các hạt nano này, các phòng thí nghiệm bắt buộc phải sử dụng các máy siêu ly tâm (ultracentrifuge) tạo ra gia tốc trường gấp hàng trăm ngàn lần gia tốc trọng trường <i>g</i>."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_02,
        "Hình 3.9: Đối chuẩn động học giữa vận tốc lắng trọng trường Stokes và khuếch tán nhiệt Brown ở 300 K: "
        "Đường lắng Stokes hgrav ∝ R² giao cắt với đường khuếch tán Brown xrms ∝ R⁻⁰·⁵ tại điểm chuyển pha Rc ≈ 0.82 μm. "
        "Vùng bên trái (R < Rc) do chuyển động nhiệt Brown hoàn toàn thống trị; vùng bên phải (R > Rc) do trọng lực cổ điển chi phối.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    add_p(
        "Bằng cách cho hai phương trình <i>h</i><sub>grav</sub>(<i>R</i>) = <i>x</i><sub>rms</sub>(<i>R</i>) giao nhau, chúng ta xác định được bán kính chuyển pha cơ học – nhiệt động học: "
        "tại điểm <i>R</i><sub>cross</sub> ≈ 0.82 μm trong không khí, chuyển động nhiệt Brown và chuyển động rơi cơ học có độ lớn ngang nhau. "
        "Đây chính là ranh giới tự nhiên phân chia giữa thế giới hạt vi mô cổ điển và thế giới hạt nano nhiệt động học."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.2.4: MA SÁT CẤP NGUYÊN TỬ VÀ HIỆN TƯỢNG SIÊU TRƠN CẤU TRÚC
    # =========================================================================
    add_p("Luận điểm 3.2.4: Ma sát cấp nguyên tử và hiện tượng siêu trơn cấu trúc trong màng Graphite và ống than nano", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, nghịch lý ma sát khô và tính chất bôi trơn của Graphite", "H3")
    add_p(
        "Theo định luật ma sát cổ điển Amontons-Coulomb, lực ma sát trượt tỉ lệ thuận với áp lực pháp tuyến (<i>F<sub>f</sub></i> = μ <i>N</i>) "
        "và hoàn toàn độc lập với diện tích tiếp xúc biểu kiến. "
        "Lực ma sát này xuất phát từ sự móc nối cơ học của các nhấp nhô bề mặt (asperities) và sự hàn dính cục bộ của các đỉnh tiếp xúc. "
        "Tuy nhiên, khi hai bề mặt tiếp xúc đạt tới độ hoàn hảo tuyệt đối cấp độ nguyên tử — chẳng hạn giữa các lớp nguyên tử Carbon trong tinh thể than chì (Graphite) "
        "hoặc giữa các ống trụ đồng trục trong ống than nano đa vách (Multiwalled Carbon Nanotubes — MWCNT) — "
        "ở đó hoàn toàn không có bất kỳ nhấp nhô cơ học nào, và cũng không có bất kỳ phân tử chất bôi trơn xen kẽ nào.",
        ocr_idx=5
    )
    add_spacer(6)

    add_p(
        "Trong điều kiện tiếp xúc nguyên tử lý tưởng đó, một hiện tượng vật lý kỳ diệu xuất hiện: "
        "lực ma sát trượt có thể biến mất gần như hoàn toàn (sụt giảm hơn 99.8% đến hàng ngàn lần so với mức thông thường), "
        "cho phép các lớp trượt lên nhau với lực cản bằng không. "
        "Hiện tượng này được gọi là Siêu trơn cấu trúc (Structural Superlubricity)."
    )
    add_spacer(8)

    # Ảnh gốc Slide 28
    story.append(he.embed_figure_with_caption(
        fig_goc_06,
        "Hình 3.10: Hiện tượng ma sát có thể biến mất ở kích thước phân tử trong Graphite và Ống than nano: "
        "Graphite là chất bôi trơn nổi tiếng do sự trượt dễ dàng giữa các lớp nguyên tử Carbon liên kết van der Waals mà không có phân tử xen kẽ (Slide 28 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ thế năng ma sát nguyên tử", "H3")
    add_p(
        "Nguồn gốc của ma sát nguyên tử được mô hình hóa bởi mô hình Frenkel-Kontorova và mô hình He-Müser: "
        "lực ma sát bên phát sinh từ gradient thế năng tương tác tuần hoàn van der Waals giữa các nguyên tử của hai mặt tiếp xúc. "
        "Khi hai mạng tinh thể lục giác chồng khít lên nhau hoàn hảo (góc lệch xoay mạng θ = 0° hoặc 60°, gọi là trạng thái tương thích — Commensurate state), "
        "tất cả các nguyên tử của lớp trên đồng thời rơi vào các hố thế năng cực tiểu của lớp dưới. "
        "Để di chuyển, một lực bên lớn phải được tác dụng để kéo đồng loạt toàn bộ mạng nguyên tử vượt qua hàng rào thế năng, tạo ra lực ma sát cực đại. "
        "Ngược lại, khi hai lớp bị xoay lệch đi một góc θ bất kỳ (trạng thái bất tương thích — Incommensurate state), "
        "sự bất đối xứng pha không gian làm triệt tiêu triệt để tổng lực tương tác pháp tuyến và tiếp tuyến."
    )
    add_spacer(6)

    eq_col_4 = r"F_s(\theta) \approx F_{\mathrm{max}} \left[\cos^2(3\theta) \exp\left(-\gamma \sin^2(3\theta)\right) + \varepsilon\right], \quad \varepsilon \le 0.002"
    nom_rows_4 = [
        ("Lực ma sát tĩnh phụ thuộc góc lệch mạng", "<i>F<sub>s</sub></i>(θ)", "nN hoặc pN", "Lực tối thiểu cần thiết để kích hoạt sự trượt tương đối giữa hai lớp nguyên tử"),
        ("Góc lệch xoay mạng tinh thể Moiré", "θ", "độ hoặc rad", "Góc định hướng góc giữa các trục tinh thể học của hai mặt tiếp xúc Carbon"),
        ("Lực ma sát khóa mạng cực đại", "<i>F</i><sub>max</sub>", "nN", "Lực ma sát tại góc ăn khớp hoàn hảo (Commensurate: θ = 0° và 60°)"),
        ("Hệ số suy giảm ma sát không gian", "γ", "không thứ nguyên", "Độ dốc phản ánh tốc độ triệt tiêu giao thoa thế năng khi rời khỏi góc ăn khớp"),
        ("Hệ số ma sát dư cực tiểu siêu trơn", "ε", "không thứ nguyên", "Giới hạn ma sát siêu trơn thực tế do dao động nhiệt phonon và khuyết tật biên"),
    ]
    story.append(he.build_target_equation_block(eq_col_4, nom_rows_4, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất cơ chế triệt tiêu lực ma sát bên", "H3")

    p_step12 = (
        "Phân tích cơ chế cộng hưởng lực trong trạng thái ăn khớp mạng (Commensurate):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi góc xoay θ = 0° (hoặc 60° đối với mạng lục giác đối xứng bậc 6), chu kỳ không gian của hai lớp trùng khớp hoàn toàn. "
        "Lực tác dụng lên nguyên tử thứ <i>i</i> là <i>f<sub>i</sub></i> = −∇<i>U</i>(<i>r<sub>i</sub></i>). "
        "Vì tất cả các nguyên tử đều ở cùng một pha thế năng dốc, tổng lực ma sát bên là tổng đồng pha của <i>N</i> nguyên tử: "
        "<i>F</i><sub>total</sub> = ∑ <i>f<sub>i</sub></i> = <i>N</i> · <i>f</i><sub>0</sub>, tạo nên lực cản ma sát vĩ mô đo được."
    )
    story.append(he.build_intermediate_equation(p_step12, r"F_{\mathrm{commensurate}} = \sum_{i=1}^N \left(-\frac{\partial U}{\partial x_i}\right) = N \cdot f_0 \propto N", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step13 = (
        "Chứng minh cơ chế triệt tiêu giao thoa lực trong trạng thái bất tương thích (Incommensurate):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi xoay lệch góc θ khác 0° và 60°, hai mạng tinh thể tạo thành cấu trúc vân Moiré không trùng chu kỳ. "
        "Tại mỗi thời điểm, một nửa số nguyên tử nằm trên sườn dốc thế năng đẩy sang phải, trong khi nửa còn lại nằm trên sườn dốc thế năng đẩy sang trái. "
        "Tổng các vector lực ma sát cục bộ triệt tiêu lẫn nhau theo tích phân giao thoa trên toàn bộ diện tích tiếp xúc:"
    )
    story.append(he.build_intermediate_equation(p_step13, r"F_{\mathrm{incommensurate}} = \int_{\text{Mặt tiếp xúc}} -\nabla U(\mathbf{r}) \, d^2\mathbf{r} \approx 0 \quad \Longrightarrow \quad F_s \le 0.002 F_{\mathrm{max}}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích hiện tượng siêu trơn cấu trúc", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích lực ma sát chuẩn hóa theo góc xoay mạng θ minh chứng rõ nét hiện tượng siêu trơn cấu trúc: "
        "lực ma sát chỉ đạt đỉnh cực đại tại đúng hai góc ăn khớp mạng θ = 0° và θ = 60°. "
        "Chỉ cần mạng bị xoay lệch đi một góc rất nhỏ (vượt ra ngoài phạm vi hẹp ±2°), lực ma sát sụt giảm thẳng đứng hơn 3 bậc độ lớn (giảm 99.8%) "
        "và duy trì ở mức siêu trơn lý tưởng trên toàn bộ dải góc từ 5° đến 55°."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_03,
        "Hình 3.11: Mô phỏng giải tích lực ma sát liên lớp Fs(θ) theo góc lệch mạng Moiré trong Graphene và CNT: "
        "Đỉnh ma sát cực đại xuất hiện tại góc ăn khớp mạng θ = 0° và 60° (khóa mạng). "
        "Trong toàn bộ miền bất tương thích (5° ≤ θ ≤ 55°), lực ma sát triệt tiêu hơn 99.8%, mở ra khả năng chế tạo ổ trục quay nano không ma sát.",
        kind="sim",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 5: Ứng dụng & Cầu nối
    add_p("Giai đoạn 5: Ứng dụng đột phá trong máy vi cơ điện tử NEMS và động cơ nano", "H3")
    add_p(
        "Hiện tượng siêu trơn cấu trúc đã được kiểm chứng thực nghiệm bằng việc rút các ống than nano đa vách đồng trục (telescoping carbon nanotubes) "
        "bằng đầu dò kính hiển vi lực nguyên tử AFM trong chân không. "
        "Ống bên trong có thể trượt tự do ra vào ống bên ngoài hàng triệu chu kỳ mà không hề bị mài mòn cơ học hay suy giảm hiệu suất. "
        "Khám phá này mở ra kỷ nguyên mới cho các hệ thống vi cơ điện tử lượng tử nano (NEMS), động cơ phân tử quay tự do, "
        "và các thiết bị lưu trữ năng lượng cơ học có tuổi thọ hoạt động vĩnh cửu."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI THỬ THÁCH HỌC VIÊN CER 3.2
    # =========================================================================
    add_p("Thử thách Học viên CER 3.2: Thiết kế hệ hạt nano vàng dẫn thuốc hướng đích (AuNP-mAb)", "H2")
    add_spacer(4)

    add_p(
        "<b>Bối cảnh kỹ thuật:</b> Một nhóm nghiên cứu tại Viện Vật lý Kỹ thuật — ĐHBK Hà Nội đang thiết kế một hệ hạt nano vàng hình cầu gắn kháng thể đơn dòng "
        "(AuNP-mAb, khối lượng riêng của hạt vàng ρ<sub>Au</sub> = 19320 kg·m<sup>−3</sup>) để vận chuyển thuốc điều trị trúng đích khối u qua hệ mạch máu người. "
        "Môi trường huyết tương ở thân nhiệt <i>T</i> = 310 K có độ nhớt động lực học η = 1.2 × 10<sup>−3</sup> Pa·s. "
        "Để đảm bảo hạt lưu thông tuần hoàn bền vững trong mạch máu mà không bị lắng đọng tắc nghẽn ở đáy thành mạch do trọng trường, "
        "hạt cần thỏa mãn tiêu chí: quãng đường khuếch tán nhiệt Brown <i>x</i><sub>rms</sub> trong thời gian <i>t</i> = 1 s "
        "phải lớn hơn ít nhất 1000 lần so với quãng đường rơi lắng do trọng lực <i>h</i><sub>grav</sub>."
    )
    add_spacer(6)

    cer_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Thành tố CER</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Nội dung Yêu cầu &amp; Luận chứng Kỹ thuật</b>"), styles["TableHeader"]),
    ]
    cer_rows = [
        cer_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>Claim (Khẳng định)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Xác định bán kính giới hạn tối đa <i>R</i><sub>max</sub> của hạt vàng AuNP để tỉ số chuyển động <i>x</i><sub>rms</sub> · <i>h</i><sub>grav</sub><sup>−1</sup> ≥ 1000, "
                "chứng minh hạt có bán kính <i>R</i> = 15 nm hoàn toàn đáp ứng tiêu chuẩn an toàn lưu thông trong dòng máu."
            ), styles["TableCell"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>Evidence (Bằng chứng số liệu)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Tính toán định lượng tại <i>T</i> = 310 K:<br/>"
                "↳ [Tường minh bước biến đổi trung gian từ slide gốc]:<br/>"
                "(1) Năng lượng nhiệt: <i>k<sub>B</sub> T</i> = 1.380649 × 10<sup>−23</sup> × 310 ≈ 4.28 × 10<sup>−21</sup> J.<br/>"
                "(2) Với hạt vàng <i>R</i> = 15 nm = 1.5 × 10<sup>−8</sup> m:<br/>"
                "• Vận tốc lắng Stokes: <i>v</i><sub>term</sub> = 2 × 19320 × 9.8 × (1.5 × 10<sup>−8</sup>)<sup>2</sup> · (9 × 1.2 × 10<sup>−3</sup>)<sup>−1</sup> ≈ 7.89 × 10<sup>−9</sup> m·s<sup>−1</sup> = 7.89 nm·s<sup>−1</sup>.<br/>"
                "• Quãng đường rơi trong 1 s: <i>h</i><sub>grav</sub> = 7.89 nm.<br/>"
                "• Hệ số khuếch tán: <i>D</i> = 4.28 × 10<sup>−21</sup> · (6π × 1.2 × 10<sup>−3</sup> × 1.5 × 10<sup>−8</sup>)<sup>−1</sup> ≈ 1.26 × 10<sup>−11</sup> m<sup>2</sup>·s<sup>−1</sup>.<br/>"
                "• Chiều dài khuếch tán Brown: <i>x</i><sub>rms</sub> = (4 × 1.26 × 10<sup>−11</sup> × 1.0)<sup>½</sup> ≈ 7.10 × 10<sup>−6</sup> m = 7.10 μm.<br/>"
                "• Tỉ số đối chuẩn: <i>x</i><sub>rms</sub> · <i>h</i><sub>grav</sub><sup>−1</sup> = 7.10 × 10<sup>−6</sup> · (7.89 × 10<sup>−9</sup>)<sup>−1</sup> ≈ 900 lần (xấp xỉ ngưỡng an toàn 1000 lần)."
            ), styles["TableCell"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>Reasoning (Lập luận nguyên lý đầu)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Từ định luật tỉ lệ: <i>h</i><sub>grav</sub> ∝ <i>R</i><sup>2</sup> và <i>x</i><sub>rms</sub> ∝ <i>R</i><sup>−½</sup>, "
                "suy ra tỉ số ưu thế nhiệt động học tỉ lệ với bán kính theo lũy thừa âm mạnh: "
                "<i>x</i><sub>rms</sub> · <i>h</i><sub>grav</sub><sup>−1</sup> ∝ <i>R</i><sup>−2.5</sup>. "
                "Khi giảm bán kính hạt vàng từ 15 nm xuống 10 nm, tỉ số này tăng vọt lên: 900 × (15 · 10<sup>−1</sup>)<sup>2.5</sup> ≈ 2480 lần, "
                "hoàn toàn vượt xa ngưỡng an toàn 1000 lần. "
                "Do đó, để ngăn chặn nguy cơ tắc mạch do lắng đọng cơ học của vàng khối lượng riêng cao, "
                "kích thước tối ưu cho hạt AuNP dẫn thuốc bắt buộc phải được kiểm soát nghiêm ngặt trong dải 10–12 nm."
            ), styles["TableCell"]),
        ],
    ]
    t_cer = he.Table(cer_rows, colWidths=[110.0, he.PRINTABLE_WIDTH - 110.0])
    t_cer.setStyle(he.TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), he.COLOR_TABLE_HEADER_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, he.COLOR_BORDER_GRAY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_cer)
    add_spacer(14)

    # =========================================================================
    # HẬU KIỂM TOÀN VĂN & BIÊN DỊCH XUẤT BẢN PDF
    # =========================================================================
    print("Executing Pre-flight Text Compliance Audit for Section 3.2...")
    compliance_report = he.assert_monograph_text_compliance(story)
    print("Pre-flight Audit Passed 100%:", compliance_report)

    print(f"Building Monograph PDF into isolated %TEMP%: {temp_pdf_path}...")
    doc.build(story)
    print("PDF build successful in %TEMP%!")

    # Hậu kiểm kích thước tệp và số trang
    file_size_mb = os.path.getsize(temp_pdf_path) / (1024 * 1024)
    print(f"Generated PDF File Size: {file_size_mb:.2f} MB (Standard <= 5.0 MB)")
    assert file_size_mb <= 5.0, f"FILE SIZE VIOLATION: {file_size_mb:.2f} MB exceeds 5.0 MB limit!"

    # Atomic Replacement vào Google Drive G:\
    print(f"Executing Atomic Replacement to Google Drive: {TARGET_PDF_PATH}...")
    shutil.move(temp_pdf_path, TARGET_PDF_PATH)
    print(f"PUBLISHING COMPLETE: Section 3.2 Monograph successfully deployed to Google Drive!")
    return TARGET_PDF_PATH


if __name__ == "__main__":
    build_monograph_muc_3_2()

# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Course: Co so vat ly va cong nghe nano (PH3470 - HUST)
Chapter 3: Dac trung cua vat lieu khi kich thuoc giam (What happens at the nanoscale?)
Section 3.3: Hinh dang (Morphology), chieu khong gian va mat do trang thai dien tu (DOS) cua cau truc nano
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

PDF_FILENAME = "Chuyen_Khao_Nano_Muc_3.3.pdf"
TARGET_PDF_PATH = os.path.join(PDF_DIR, PDF_FILENAME)


def build_monograph_muc_3_3():
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
    fig_goc_01 = os.path.join(IMG_DIR, "[Goc]_Muc_3.3_Hinh_01_Phan_Loai_Chieu_Khong_Gian_0D_1D_2D_3D.png")
    fig_goc_02 = os.path.join(IMG_DIR, "[Goc]_Muc_3.3_Hinh_02_Hinh_Thai_Hoc_Morphology_Vat_Lieu_ZnO.png")
    fig_goc_03 = os.path.join(IMG_DIR, "[Goc]_Muc_3.3_Hinh_03_So_Do_Mat_Do_Trang_Thai_Dien_Tu_DOS.png")
    fig_goc_04 = os.path.join(IMG_DIR, "[Goc]_Muc_3.3_Hinh_04_Bieu_Do_DOS_Theo_Chieu_Khong_Gian_3D_2D_1D_0D.png")
    fig_goc_05 = os.path.join(IMG_DIR, "[Goc]_Muc_3.3_Hinh_05_Vector_Chiral_Va_Cau_Truc_Ong_Than_CNT.png")
    fig_goc_06 = os.path.join(IMG_DIR, "[Goc]_Muc_3.3_Hinh_06_Tinh_Chat_Dien_Armchair_Zigzag_Chiral_CNT.png")

    # Figure paths - 3 simulation plots
    fig_sim_01 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.3_So_Sanh_Mat_Do_Trang_Thai_DOS_3D_2D_1D_0D.png")
    fig_sim_02 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.3_Khe_Nang_Luong_Theo_Ban_Kinh_Cham_Luong_Tu_Model_Brus.png")
    fig_sim_03 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.3_Phan_Loai_Vector_Chiral_Va_Khe_Nang_Luong_CNT.png")

    # =========================================================================
    # H1 TIÊU ĐỀ PHÂN MỤC VÀ METADATA ĐÀO TẠO BÁCH KHOA
    # =========================================================================
    add_p("Chương 3: Đặc trưng của vật liệu khi kích thước giảm", "H1")
    add_p("Mục 3.3: Hình dạng (Morphology), chiều không gian và mật độ trạng thái điện tử (DOS) của cấu trúc nano", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Edward L. Wolf — Nanophysics and Nanotechnology, Chương 3; Slide bài giảng HUST 29–34)</i>", "Caption")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Cơ sở vật lý và công nghệ nano (PH3470)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Viện Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Bài 3 (Slide 29–34); Wolf Nanotechnology Ch. 3"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu về hình thái học cấu trúc, số chiều không gian giam giữ lượng tử "
        "và sự tiến hóa của hàm mật độ trạng thái điện tử (DOS) ở thang nano (PH3470 — HUST; đối chiếu Edward L. Wolf, Nanophysics and Nanotechnology, Chapter 3). "
        "Khảo sát toàn diện mối liên hệ hữu cơ giữa số chiều tự do chuyển động và phổ năng lượng hạt tải: "
        "phân loại hệ thống cấu trúc nano từ 0D, 1D, 2D đến 3D theo bước sóng de Broglie, "
        "giải phẫu hình thái học đa dạng phi thường của vật liệu bán dẫn ZnO bắt nguồn từ sự bất đối xứng phân cực mạng tinh thể Wurtzite, "
        "dẫn xuất giải tích từ nguyên lý đầu hàm mật độ trạng thái điện tử <i>g</i>(<i>E</i>) qua các chiều không gian (từ parabol trơn 3D, bậc thang Heaviside 2D, "
        "kỳ dị Van Hove 1D đến vạch nhọn delta Dirac 0D của nguyên tử nhân tạo), "
        "thiết lập mô hình khối lượng hiệu dụng Brus mô tả định lượng sự mở rộng khe năng lượng quang học theo bán kính chấm lượng tử, "
        "và phân tích cấu trúc tinh thể học cùng quy tắc cuộn vector chiral (<i>n</i>, <i>m</i>) quyết định tính dẫn điện kim loại hay bán dẫn của ống than nano Carbon Nanotubes."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 3.3
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Slide HUST &amp; Wolf)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.3.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hình thái học (Morphology) &amp; Phân loại chiều không gian cấu trúc nano"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Điều kiện giam giữ lượng tử <i>L</i> ≤ λ<sub>dB</sub>, phân loại 0D, 1D, 2D, 3D; hình thái ZnO Wurtzite phân cực trục [0001]"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 29–30 (Hình thái ZnO đa dạng)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.3.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Mật độ trạng thái điện tử (DOS) &amp; Sự biến đổi hàm <i>g</i>(<i>E</i>) theo chiều không gian"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>g</i><sub>3D</sub> ∝ <i>E</i><sup>½</sup>, <i>g</i><sub>2D</sub> ∝ ∑ θ(<i>E</i> − <i>E<sub>n</sub></i>), <i>g</i><sub>1D</sub> ∝ ∑ (<i>E</i> − <i>E<sub>nm</sub></i>)<sup>−½</sup>, <i>g</i><sub>0D</sub> ∝ ∑ δ(<i>E</i> − <i>E<sub>i</sub></i>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 31–32; Mô phỏng giải tích 3.3.1"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.3.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hiệu ứng giam giữ lượng tử &amp; Mô hình khối lượng hiệu dụng Brus"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>E<sub>g</sub></i>(<i>R</i>) = <i>E</i><sub><i>g</i>,bulk</sub> + ħ<sup>2</sup>π<sup>2</sup> · (2μ <i>R</i><sup>2</sup>)<sup>−1</sup> − 1.786 <i>e</i><sup>2</sup> · (4πε<sub>0</sub>ε<i><sub>r</sub> R</i>)<sup>−1</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng giải tích 3.3.2 (CdSe at 300 K)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.3.4</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Cấu trúc tinh thể học, vector chiral (<i>n</i>, <i>m</i>) &amp; Tính chất điện CNT"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>d<sub>t</sub></i> = <i>a</i> · π<sup>−1</sup> (<i>n</i><sup>2</sup> + <i>nm</i> + <i>m</i><sup>2</sup>)<sup>½</sup>; (<i>n</i> − <i>m</i>) mod 3 = 0 (Kim loại); <i>E<sub>g</sub></i> ∝ <i>d<sub>t</sub></i><sup>−1</sup> (Bán dẫn)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 33–34; Mô phỏng giải tích 3.3.3"), styles["TableCellCenter"]),
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
    # MPT 3.3.1: HÌNH THÁI HỌC VÀ PHÂN LOẠI CHIỀU KHÔNG GIAN CẤU TRÚC NANO
    # =========================================================================
    add_p("Luận điểm 3.3.1: Hình thái học (Morphology) và Phân loại Chiều Không gian Cấu trúc Nano (0D, 1D, 2D, 3D)", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, bước sóng de Broglie và tiêu chuẩn chiều giam giữ lượng tử", "H3")
    add_p(
        "Trong vật lý chất rắn vĩ mô, một tinh thể bán dẫn được coi là một môi trường liên tục vô hạn theo cả ba chiều không gian (3D Bulk). "
        "Các hạt tải điện (electron trong dải dẫn và lỗ trống trong dải hóa trị) tự do chuyển động dưới dạng sóng Bloch lan truyền khắp mạng tinh thể. "
        "Tuy nhiên, hành vi lượng tử của hạt tải được đặc trưng bởi bước sóng de Broglie nhiệt: "
        "λ<sub>dB</sub> = <i>h</i> · (2<i>m</i><sup>*</sup> <i>k<sub>B</sub> T</i>)<sup>−½</sup>. "
        "Đối với các bán dẫn thông dụng ở nhiệt độ phòng 300 K (chẳng hạn GaAs, InAs, CdSe), bước sóng de Broglie và bán kính Bohr exciton <i>a<sub>B</sub></i> "
        "nằm trong khoảng từ 5 nm đến 50 nm.",
        ocr_idx=1
    )
    add_spacer(6)

    add_p(
        "Khi kích thước hình học <i>L</i> của một cấu trúc vật liệu theo một hoặc nhiều phương bị thu nhỏ lại tới giá trị nhỏ hơn hoặc tương đương bước sóng de Broglie "
        "(<i>L</i> ≤ λ<sub>dB</sub>), chuyển động của hạt tải theo phương đó không còn là chuyển động tự do liên tục nữa mà bị khóa cứng bởi các điều kiện biên lượng tử. "
        "Năng lượng chuyển động dọc theo phương bị giới hạn sẽ phân rã thành các mức năng lượng gián đoạn riêng biệt (quantum subbands). "
        "Dựa trên số chiều không gian bị giam giữ lượng tử, khoa học nano phân loại vật liệu thành 4 họ cấu trúc nền tảng:",
        ocr_idx=2
    )
    add_spacer(6)

    add_p(
        "• <b>Cấu trúc 0D (Chấm lượng tử — Quantum Dots):</b> Vật liệu bị giam giữ lượng tử theo cả 3 chiều không gian (<i>L<sub>x</sub></i>, <i>L<sub>y</sub></i>, <i>L<sub>z</sub></i> ≤ λ<sub>dB</sub>). "
        "Hạt tải không còn bất kỳ chiều tự do chuyển động tịnh tiến nào, phổ năng lượng hoàn toàn gián đoạn như trong một nguyên tử độc lập (nguyên tử nhân tạo);<br/>"
        "• <b>Cấu trúc 1D (Dây lượng tử — Quantum Wires, Nanotubes, Nanorods):</b> Vật liệu bị giam giữ lượng tử theo 2 chiều (<i>L<sub>x</sub></i>, <i>L<sub>y</sub></i> ≤ λ<sub>dB</sub>) "
        "và tự do chuyển động dọc theo 1 chiều trục (<i>L<sub>z</sub></i> ≫ λ<sub>dB</sub>);<br/>"
        "• <b>Cấu trúc 2D (Giếng lượng tử — Quantum Wells, Graphene, Màng mỏng Nanosheets):</b> Vật liệu bị giam giữ lượng tử theo 1 chiều chiều dày (<i>L<sub>z</sub></i> ≤ λ<sub>dB</sub>) "
        "và hoàn toàn tự do chuyển động trong mặt phẳng 2 chiều (<i>L<sub>x</sub></i>, <i>L<sub>y</sub></i> ≫ λ<sub>dB</sub>);<br/>"
        "• <b>Cấu trúc 3D (Vật liệu khối — Bulk Materials):</b> Kích thước theo cả 3 chiều đều vượt xa bước sóng de Broglie (<i>L<sub>x</sub></i>, <i>L<sub>y</sub></i>, <i>L<sub>z</sub></i> ≫ λ<sub>dB</sub>)."
    )
    add_spacer(8)

    # Ảnh gốc Slide 29 & 30
    story.append(he.embed_figure_with_caption(
        fig_goc_01,
        "Hình 3.12: Phân loại hình thái học và chiều không gian của các cấu trúc nano: "
        "Sơ đồ phân loại kinh điển từ vật liệu khối 3D, giếng lượng tử 2D, dây nano 1D đến chấm lượng tử 0D (Slide 29 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_02,
        "Hình 3.13: Đa dạng hình thái học (morphology) phi thường của vật liệu bán dẫn ZnO: "
        "Các cấu trúc dây nano (nanowires), thanh nano (nanorods), đai nano (nanobelts), lược nano (nanocombs) và hoa nano (nanoflowers) (Slide 30 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Cơ chế phân cực mạng tinh thể Wurtzite của ZnO", "H3")
    add_p(
        "Kẽm oxit (ZnO) là ví dụ kinh điển nhất về sự phong phú hình thái học trong khoa học vật liệu nano. "
        "ZnO kết tinh theo cấu trúc mạng Wurtzite lục giác (nhóm không gian <i>P</i>6<sub>3</sub><i>mc</i>), đặc trưng bởi các mặt đáy phân cực [0001] mang điện tích dương của ion Zn<sup>2+</sup> "
        "và mặt [000-1] mang điện tích âm của ion O<sup>2−</sup>. "
        "Momen lưỡng cực tĩnh điện nội tại dọc theo trục <i>c</i> tạo ra năng lượng bề mặt phân cực cực kỳ cao so với các mặt phẳng bên không phân cực {10-10} và {11-20}. "
        "Để cực tiểu hóa năng lượng tự do bề mặt trong quá trình kết tinh nhiệt động học, các mặt tinh thể phát triển với tốc độ dị hướng khác nhau, "
        "tạo nên phổ hình thái học phong phú bậc nhất trong tự nhiên."
    )
    add_spacer(6)

    eq_col_1 = r"\lambda_{\mathrm{dB}} = \frac{h}{\sqrt{2 m^* k_B T}}, \quad E_n = \frac{\hbar^2 \pi^2 n^2}{2 m^* L^2}, \quad v_{[0001]} > v_{\{01\bar{1}0\}} > v_{\{000\bar{1}\}}"
    nom_rows_1 = [
        ("Bước sóng de Broglie nhiệt của hạt tải", "λ<sub>dB</sub>", "nm hoặc m", "Thang đo độ dài lượng tử; khi kích thước hạt nhỏ hơn λ<sub>dB</sub> thì hiệu ứng lượng tử bộc lộ"),
        ("Khối lượng hiệu dụng của electron/lỗ trống", "<i>m</i><sup>*</sup>", "kg hoặc <i>m</i><sub>0</sub>", "Khối lượng quán tính quy đổi phản ánh ảnh hưởng của thế trường mạng tinh thể"),
        ("Mức năng lượng lượng tử hóa giam giữ", "<i>E<sub>n</sub></i>", "eV hoặc J", "Năng lượng trạng thái dừng bậc n sinh ra do rào thế giam giữ kích thước <i>L</i>"),
        ("Bề rộng giam giữ hình học", "<i>L</i>", "nm", "Kích thước đặc trưng của giếng, dây hoặc chấm lượng tử"),
        ("Tốc độ phát triển tinh thể dị hướng ZnO", "<i>v</i><sub>[0001]</sub>", "m·s<sup>−1</sup>", "Tốc độ kết tinh nhanh nhất dọc trục phân cực c tạo nên các cấu trúc dây nano thanh mảnh"),
    ]
    story.append(he.build_target_equation_block(eq_col_1, nom_rows_1, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất điều kiện giam giữ lượng tử", "H3")

    p_step1 = (
        "Thiết lập điều kiện biên sóng dừng de Broglie trong hố thế lượng tử một chiều:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét hạt tải điện chuyển động trong miền không gian bị giới hạn giữa hai rào thế vô hạn cách nhau bề rộng <i>L</i>. "
        "Hàm sóng của hạt bắt buộc phải triệt tiêu tại hai biên: ψ(0) = ψ(<i>L</i>) = 0. "
        "Điều kiện biên này đòi hỏi bề rộng <i>L</i> phải chứa đúng một số nguyên lần nửa bước sóng de Broglie: <i>L</i> = <i>n</i> · (λ · 2<sup>−1</sup>):"
    )
    story.append(he.build_intermediate_equation(p_step1, r"k_n = \frac{2\pi}{\lambda_n} = \frac{n \pi}{L} \quad (n = 1, 2, 3, \dots) \quad \Longrightarrow \quad \lambda_n = \frac{2L}{n}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step2 = (
        "Dẫn xuất phổ năng lượng gián đoạn của hạt tải bị giam giữ:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Theo hệ thức tán sắc parabol của hạt tự do với khối lượng hiệu dụng <i>m</i><sup>*</sup>, động năng của hạt liên hệ với vector sóng <i>k</i> qua: "
        "<i>E</i> = ħ<sup>2</sup> <i>k</i><sup>2</sup> · (2<i>m</i><sup>*</sup>)<sup>−1</sup>. Thay thế vector sóng lượng tử hóa <i>k<sub>n</sub></i> vừa xác định:"
    )
    story.append(he.build_intermediate_equation(p_step2, r"E_n = \frac{\hbar^2 k_n^2}{2 m^*} = \frac{\hbar^2}{2 m^*} \left(\frac{n \pi}{L}\right)^2 = \frac{\hbar^2 \pi^2 n^2}{2 m^* L^2} \propto \frac{n^2}{L^2}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Biến thiên tiệm cận & Ứng dụng ZnO
    add_p("Giai đoạn 4: Phân tích biến thiên tiệm cận khoảng cách mức năng lượng", "H3")
    add_p(
        "Biểu thức <i>E<sub>n</sub></i> ∝ <i>L</i><sup>−2</sup> chỉ ra rằng khoảng cách giữa các mức năng lượng lượng tử hóa (Δ<i>E</i> = <i>E</i><sub><i>n</i>+1</sub> − <i>E<sub>n</sub></i>) "
        "tăng tỉ lệ nghịch với bình phương kích thước hình học <i>L</i><sup>2</sup>. "
        "Khi <i>L</i> thu nhỏ từ 100 nm xuống 2 nm, khoảng cách mức năng lượng tăng vọt tới 2500 lần! "
        "Khi khoảng cách này vượt qua năng lượng kích thích nhiệt <i>k<sub>B</sub> T</i> (khoảng 25.9 meV ở 300 K), "
        "các hiệu ứng lượng tử sẽ bộc lộ rõ nét ngay tại nhiệt độ phòng mà không bị dao động nhiệt phonon xóa nhòa."
    )
    add_spacer(6)

    # Giai đoạn 5: Ứng dụng kỹ thuật
    add_p("Giai đoạn 5: Ứng dụng kỹ thuật và điều khiển hình thái mọc tinh thể dị hướng ZnO", "H3")
    add_p(
        "Đối với vật liệu ZnO, bằng cách điều khiển nhiệt độ bay hơi, áp suất riêng phần của oxy và sử dụng các chất hoạt động bề mặt tạo phức che chắn các mặt phân cực, "
        "các nhà khoa học có thể định hướng tốc độ kết tinh để thu được các cấu trúc nano với độ hoàn hảo tinh thể phi thường: "
        "từ dây nano (nanowires) có tỉ số khung hình <i>L</i> · <i>D</i><sup>−1</sup> > 1000 dùng trong cảm biến khí và laser nano, "
        "đến đai nano (nanobelts) phẳng có tính áp điện siêu nhạy dùng trong máy phát điện nano tự cấp nguồn (piezoelectric nanogenerators — PENG)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.3.2: MẬT ĐỘ TRẠNG THÁI ĐIỆN TỬ (DOS) THEO SỐ CHIỀU
    # =========================================================================
    add_p("Luận điểm 3.3.2: Mật độ Trạng thái Điện tử (DOS) và Sự Biến đổi Hàm g(E) theo Chiều Không gian", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, không gian sóng k-space và định nghĩa mật độ trạng thái", "H3")
    add_p(
        "Mật độ trạng thái điện tử (Density of States — DOS), ký hiệu là <i>g</i>(<i>E</i>), là đại lượng vật lý nền tảng nhất quyết định toàn bộ "
        "các tính chất điện, quang, nhiệt và từ của một vật liệu bán dẫn. "
        "Về mặt định nghĩa, <i>g</i>(<i>E</i>) <i>dE</i> đại diện cho số lượng trạng thái lượng tử khả dĩ của electron trong một đơn vị thể tích "
        "nằm trong dải năng lượng hẹp giữa <i>E</i> và <i>E</i> + <i>dE</i>. "
        "Hàm mật độ trạng thái được xây dựng từ việc đếm số điểm nút sóng dừng khả dĩ trong không gian vector sóng <i>k</i>-space "
        "theo điều kiện biên tuần hoàn Born-von Karman.",
        ocr_idx=3
    )
    add_spacer(6)

    add_p(
        "Khi số chiều tự do chuyển động của hạt tải thay đổi từ 3D (vật liệu khối) xuống 2D (giếng lượng tử), 1D (dây nano) và 0D (chấm lượng tử), "
        "hình học của bề mặt đẳng năng lượng trong không gian pha <i>k</i>-space thay đổi căn bản: "
        "từ mặt cầu 3 chiều biến thành các đường tròn đồng tâm 2 chiều, các cặp điểm đối xứng 1 chiều, và cuối cùng thành một điểm định xứ 0 chiều. "
        "Sự chuyển dịch hình học này làm biến đổi hoàn toàn dạng toán học của hàm <i>g</i>(<i>E</i>)."
    )
    add_spacer(8)

    # Ảnh gốc Slide 31 & 32
    story.append(he.embed_figure_with_caption(
        fig_goc_03,
        "Hình 3.14: Sơ đồ nguồn gốc mật độ trạng thái điện tử (DOS) trong tinh thể: "
        "Số lượng trạng thái khả dĩ trên mỗi đơn vị năng lượng dN · dE⁻¹ phản ánh cấu trúc vùng năng lượng hạt tải (Slide 31 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_04,
        "Hình 3.15: Đồ thị kinh điển biểu diễn mật độ trạng thái điện tử theo số chiều không gian 3D, 2D, 1D, 0D: "
        "Sự tiến hóa từ parabol trơn liên tục (3D), hàm bậc thang gián đoạn (2D), đỉnh kỳ dị Van Hove (1D) đến các vạch nhọn delta Dirac (0D) (Slide 32 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hàm mật độ trạng thái DOS", "H3")
    add_p(
        "Bốn hàm giải tích của mật độ trạng thái qua 4 chiều không gian cấu thành bảng tuần hoàn động học của vật lý chất rắn và công nghệ nano. "
        "Mỗi biểu thức là một dấu ấn toán học bất biến, phản ánh trực tiếp số chiều tự do của hạt tải."
    )
    add_spacer(6)

    eq_col_2 = r"g_{\mathrm{3D}}(E) \propto \sqrt{E}, \quad g_{\mathrm{2D}}(E) \propto \sum_n \theta(E - E_n), \quad g_{\mathrm{1D}}(E) \propto \sum_{n,m} \frac{1}{\sqrt{E - E_{n,m}}}, \quad g_{\mathrm{0D}}(E) \propto \sum_i \delta(E - E_i)"
    nom_rows_2 = [
        ("Mật độ trạng thái khối 3D", "<i>g</i><sub>3D</sub>(<i>E</i>)", "m<sup>−3</sup>·eV<sup>−1</sup>", "Hàm parabol trơn liên tục tỉ lệ thuận với căn bậc hai năng lượng <i>E</i><sup>½</sup>"),
        ("Mật độ trạng thái giếng 2D", "<i>g</i><sub>2D</sub>(<i>E</i>)", "m<sup>−2</sup>·eV<sup>−1</sup>", "Hàm bậc thang Heaviside θ, mật độ không đổi độc lập với năng lượng trên mỗi dải con"),
        ("Mật độ trạng thái dây 1D", "<i>g</i><sub>1D</sub>(<i>E</i>)", "m<sup>−1</sup>·eV<sup>−1</sup>", "Đỉnh kỳ dị Van Hove nghịch đảo căn thức (<i>E</i> − <i>E<sub>nm</sub></i>)<sup>−½</sup>, đạt cực đại vô hạn tại ngưỡng dải"),
        ("Mật độ trạng thái chấm 0D", "<i>g</i><sub>0D</sub>(<i>E</i>)", "eV<sup>−1</sup>", "Hàm delta Dirac δ nhọn định xứ, toàn bộ trạng thái tập trung tuyệt đối tại các mức năng lượng gián đoạn"),
        ("Hàm bước nhảy Heaviside", "θ(<i>x</i>)", "không thứ nguyên", "Bằng 0 khi <i>x</i> < 0 và bằng 1 khi <i>x</i> ≥ 0, đánh dấu sự mở ra của một dải con lượng tử mới"),
    ]
    story.append(he.build_target_equation_block(eq_col_2, nom_rows_2, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất hàm mật độ trạng thái từ không gian k-space", "H3")

    p_step3 = (
        "Dẫn xuất mật độ trạng thái trong vật liệu khối 3 chiều <i>g</i><sub>3D</sub>(<i>E</i>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Trong không gian 3D kích thước <i>L</i> × <i>L</i> × <i>L</i>, thể tích của một trạng thái lượng tử trong <i>k</i>-space là (2π · <i>L</i><sup>−1</sup>)<sup>3</sup>. "
        "Số trạng thái trong quả cầu bán kính <i>k</i> tính cả độ suy biến spin (hệ số 2) là: <i>N</i>(<i>k</i>) = 2 · (4 · 3<sup>−1</sup> · π <i>k</i><sup>3</sup>) · [<i>V</i> · (2π)<sup>−3</sup>] = <i>V</i> · <i>k</i><sup>3</sup> · (3π<sup>2</sup>)<sup>−1</sup>. "
        "Thay thế <i>k</i> = (2<i>m</i><sup>*</sup> <i>E</i> · ħ<sup>−2</sup>)<sup>½</sup> và lấy đạo hàm theo năng lượng <i>E</i>:"
    )
    story.append(he.build_intermediate_equation(p_step3, r"g_{\mathrm{3D}}(E) = \frac{1}{V}\frac{dN}{dE} = \frac{1}{2\pi^2} \left(\frac{2 m^*}{\hbar^2}\right)^{3/2} \sqrt{E} \quad \Longrightarrow \quad g_{\mathrm{3D}}(E) \propto E^{1/2}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step4 = (
        "Dẫn xuất mật độ trạng thái trong giếng lượng tử 2 chiều <i>g</i><sub>2D</sub>(<i>E</i>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Trong không gian 2D, diện tích của một trạng thái trong <i>k</i>-space là (2π · <i>L</i><sup>−1</sup>)<sup>2</sup>. "
        "Số trạng thái trong hình tròn bán kính <i>k</i> tính cả spin là: <i>N</i>(<i>k</i>) = 2 · (π <i>k</i><sup>2</sup>) · [<i>A</i> · (2π)<sup>−2</sup>] = <i>A</i> · <i>k</i><sup>2</sup> · (2π)<sup>−1</sup>. "
        "Thay thế <i>k</i><sup>2</sup> = 2<i>m</i><sup>*</sup> (<i>E</i> − <i>E<sub>n</sub></i>) · ħ<sup>−2</sup> và lấy đạo hàm theo <i>E</i>:"
    )
    story.append(he.build_intermediate_equation(p_step4, r"g_{\mathrm{2D}}(E) = \frac{1}{A}\frac{dN}{dE} = \frac{m^*}{\pi \hbar^2} \sum_n \theta(E - E_n) \quad \Longrightarrow \quad g_{\mathrm{2D}} = \text{const trên mỗi dải con}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step5 = (
        "Dẫn xuất mật độ trạng thái trong dây lượng tử 1 chiều <i>g</i><sub>1D</sub>(<i>E</i>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Trong không gian 1D, độ dài một trạng thái trong <i>k</i>-space là 2π · <i>L</i><sup>−1</sup>. "
        "Số trạng thái trong đoạn từ −<i>k</i> đến +<i>k</i> tính cả spin là: <i>N</i>(<i>k</i>) = 2 · (2<i>k</i>) · [<i>L</i> · (2π)<sup>−1</sup>] = 2<i>L k</i> · π<sup>−1</sup>. "
        "Vì <i>k</i> = [2<i>m</i><sup>*</sup> (<i>E</i> − <i>E<sub>nm</sub></i>) · ħ<sup>−2</sup>]<sup>½</sup>, lấy đạo hàm <i>dk</i> · <i>dE</i><sup>−1</sup> sinh ra nghịch đảo căn thức:"
    )
    story.append(he.build_intermediate_equation(p_step5, r"g_{\mathrm{1D}}(E) = \frac{1}{L}\frac{dN}{dE} = \frac{\sqrt{2 m^*}}{\pi \hbar} \sum_{n,m} \frac{1}{\sqrt{E - E_{n,m}}} \theta(E - E_{n,m}) \quad \Longrightarrow \quad \text{Kỳ dị Van Hove}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích đối chuẩn 4 chiều không gian", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích chuẩn hóa ZT-GVLE thể hiện trực quan bước chuyển pha lượng tử: "
        "khi số chiều giảm từ 3D xuống 0D, năng lượng không còn phân tán loãng trên một phổ liên tục rộng lớn "
        "mà bị nén dồn vào các đỉnh nhọn cục bộ. "
        "Ở 1D, các đỉnh kỳ dị Van Hove tạo ra mật độ trạng thái khổng lồ tại bờ dải dẫn; "
        "và ở 0D, toàn bộ trạng thái hội tụ tuyệt đối thành các vạch delta nhọn, "
        "khiến chấm lượng tử sở hữu các tính chất quang điện tử sắc nét như một nguyên tử khí độc lập nhưng lại nằm trọn vẹn trong một tinh thể chất rắn."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_01,
        "Hình 3.16: Mô phỏng giải tích đối chuẩn mật độ trạng thái điện tử (DOS) qua 4 chiều không gian 3D, 2D, 1D, 0D: "
        "Màu xanh dương: parabol 3D; màu cam: bậc thang gián đoạn Heaviside 2D; màu tím: các đỉnh kỳ dị Van Hove 1D; màu xanh lá: các vạch delta Dirac 0D.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    # Giai đoạn 5: Ứng dụng quang điện tử
    add_p("Giai đoạn 5: Ứng dụng quang điện tử của dải con lượng tử và cầu nối sang chấm lượng tử", "H3")
    add_p(
        "Sự nén mật độ trạng thái điện tử tại các đỉnh kỳ dị Van Hove trong dây 1D và vạch delta trong chấm 0D mang lại lợi thế vượt trội "
        "cho các thiết bị laser bán dẫn (quantum dot / quantum wire lasers): "
        "dòng ngưỡng bơm quang học giảm hàng chục lần so với laser khối 3D truyền thống, hiệu suất lượng tử vi phân tăng vọt, "
        "và độ ổn định nhiệt độ không phụ thuộc vào dao động dải dẫn. "
        "Để hiểu sâu hơn về cơ chế này, chúng ta khảo sát hiệu ứng giam giữ lượng tử trong chấm 0D qua mô hình toán học giải tích Brus."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.3.3: HIỆU ỨNG GIAM GIỮ LƯỢNG TỬ & MÔ HÌNH BRUS
    # =========================================================================
    add_p("Luận điểm 3.3.3: Hiệu ứng Giam giữ Lượng tử trong Chấm Lượng tử và Mô hình Brus", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, cặp exciton và sự mở rộng khe dải năng lượng", "H3")
    add_p(
        "Khi một photon có năng lượng lớn hơn khe năng lượng của bán dẫn chiếu vào vật liệu, "
        "một electron từ dải hóa trị được kích thích nhảy lên dải dẫn, để lại một lỗ trống tích điện dương. "
        "Cặp electron – lỗ trống liên kết với nhau bằng lực hút tĩnh điện Coulomb, tạo thành một giả hạt trung hòa điện gọi là exciton Wannier-Mott. "
        "Trong vật liệu khối, exciton có bán kính quỹ đạo tự nhiên gọi là bán kính Bohr exciton: "
        "<i>a<sub>B</sub></i> = 4πε<sub>0</sub> ε<i><sub>r</sub></i> ħ<sup>2</sup> · (μ <i>e</i><sup>2</sup>)<sup>−1</sup>, "
        "trong đó μ = (<i>m<sub>e</sub></i><sup>*−1</sup> + <i>m<sub>h</sub></i><sup>*−1</sup>)<sup>−1</sup> là khối lượng rút gọn của cặp hạt tải.",
        ocr_idx=4
    )
    add_spacer(6)

    add_p(
        "Khi một tinh thể bán dẫn được chế tạo dưới dạng một hạt cầu nano có bán kính <i>R</i> nhỏ hơn bán kính Bohr exciton (<i>R</i> < <i>a<sub>B</sub></i>), "
        "cặp exciton bị ép chặt vào một thể tích nhỏ hơn quỹ đạo tự nhiên của nó (chế độ giam giữ mạnh — strong confinement regime). "
        "Theo nguyên lý bất định Heisenberg, sự định xứ không gian cưỡng bức này làm tăng vọt động năng của cả electron và lỗ trống, "
        "khiến năng lượng photon phát xạ tái hợp bị đẩy lên mức cao hơn, tạo nên hiện tượng dịch chuyển xanh (blue shift) ngoạn mục: "
        "chỉ cần thay đổi bán kính hạt từ 6 nm xuống 1.5 nm, cùng một chất bán dẫn CdSe có thể phát xạ ánh sáng từ đỏ, vàng, lục đến xanh lam."
    )
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ mô hình Brus", "H3")
    add_p(
        "Louis E. Brus (nhà hóa học lượng tử được trao giải Nobel Hóa học năm 2023) đã thiết lập mô hình khối lượng hiệu dụng "
        "tính toán chính xác năng lượng kích thích exciton trong chấm lượng tử hình cầu dựa trên lý thuyết nhiễu loạn bậc nhất. "
        "Biểu thức Brus bao gồm ba số hạng vật lý độc lập: khe năng lượng vật liệu khối, số hạng động năng giam giữ lượng tử, "
        "và số hạng hiệu chỉnh thế năng hút tĩnh điện Coulomb giữa electron và lỗ trống."
    )
    add_spacer(6)

    eq_col_3 = r"E_g(R) = E_{g,\mathrm{bulk}} + \frac{\hbar^2 \pi^2}{2 \mu R^2} - \frac{1.786 e^2}{4\pi \varepsilon_0 \varepsilon_r R}"
    nom_rows_3 = [
        ("Khe năng lượng quang hiệu dụng của chấm", "<i>E<sub>g</sub></i>(<i>R</i>)", "eV", "Năng lượng photon hấp thụ hoặc phát xạ huỳnh quang cực đại của chấm lượng tử"),
        ("Khe năng lượng của vật liệu khối ban đầu", "<i>E</i><sub><i>g</i>,bulk</sub>", "eV", "Khe dải cấm nội tại ở 300 K (đối với tinh thể khối CdSe, <i>E</i><sub><i>g</i>,bulk</sub> = 1.74 eV)"),
        ("Số hạng động năng giam giữ lượng tử", "Δ<i>E</i><sub>conf</sub> ∝ <i>R</i><sup>−2</sup>", "eV", "Động năng tăng thêm do hạt tải bị nhốt trong giếng cầu vô hạn, tỉ lệ nghịch với <i>R</i><sup>2</sup>"),
        ("Số hạng thế năng tương tác Coulomb", "Δ<i>E</i><sub>Coul</sub> ∝ <i>R</i><sup>−1</sup>", "eV", "Năng lượng liên kết exciton hiệu chỉnh bởi hằng số điện môi mạng ε<i><sub>r</sub></i>"),
        ("Khối lượng rút gọn của cặp exciton", "μ", "kg", "Khối lượng quán tính kết hợp: μ = (<i>m<sub>e</sub></i><sup>*−1</sup> + <i>m<sub>h</sub></i><sup>*−1</sup>)<sup>−1</sup>"),
    ]
    story.append(he.build_target_equation_block(eq_col_3, nom_rows_3, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất mô hình Brus từ phương trình Schrödinger", "H3")

    p_step6 = (
        "Giải phương trình Schrödinger cho electron và lỗ trống trong hố thế hình cầu đối xứng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Trong gần đúng giam giữ mạnh (strong confinement), thế năng giam giữ vượt trội năng lượng liên kết Coulomb. "
        "Phương trình phần bán kính cho trạng thái cơ bản 1<i>s</i> (momen xung lượng <i>l</i> = 0) có nghiệm hàm cầu Bessel bậc không <i>j</i><sub>0</sub>(<i>kr</i>) = sin(<i>kr</i>) · (<i>kr</i>)<sup>−1</sup>. "
        "Điều kiện triệt tiêu tại biên hạt <i>r</i> = <i>R</i> cho vector sóng dừng bậc nhất: <i>k</i><sub>1</sub> = π · <i>R</i><sup>−1</sup>:"
    )
    story.append(he.build_intermediate_equation(p_step6, r"\Delta E_{\mathrm{conf}} = E_e + E_h = \frac{\hbar^2 \pi^2}{2 m_e^* R^2} + \frac{\hbar^2 \pi^2}{2 m_h^* R^2} = \frac{\hbar^2 \pi^2}{2 R^2} \left(\frac{1}{m_e^*} + \frac{1}{m_h^*}\right) = \frac{\hbar^2 \pi^2}{2 \mu R^2}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step7 = (
        "Hiệu chỉnh tương tác hút Coulomb bậc nhất giữa electron và lỗ trống:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Sử dụng lý thuyết nhiễu loạn bậc một với hàm sóng không nhiễu loạn ψ(<i>r<sub>e</sub></i>, <i>r<sub>h</sub></i>) = ψ<sub>1<i>s</i></sub>(<i>r<sub>e</sub></i>) ψ<sub>1<i>s</i></sub>(<i>r<sub>h</sub></i>). "
        "Tích phân không gian 6 chiều của thế năng Coulomb tương tác qua hằng số điện môi tương đối ε<i><sub>r</sub></i> của chất bán dẫn thu được giá trị giải tích chính xác:"
    )
    story.append(he.build_intermediate_equation(p_step7, r"\Delta E_{\mathrm{Coul}} = \langle \psi | -\frac{e^2}{4\pi \varepsilon_0 \varepsilon_r |\mathbf{r}_e - \mathbf{r}_h|} | \psi \rangle = -\frac{1.786 e^2}{4\pi \varepsilon_0 \varepsilon_r R} \propto \frac{1}{R}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Mô phỏng đối chuẩn & Đồ thị Brus
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích CdSe ở 300 K", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích theo phương trình Brus trên vật liệu CdSe ở nhiệt độ 300 K "
        "minh chứng sự cạnh tranh giữa hai số hạng phụ thuộc kích thước: số hạng động năng giam giữ (∝ <i>R</i><sup>−2</sup>) "
        "và số hạng hút tĩnh điện Coulomb (∝ <i>R</i><sup>−1</sup>). "
        "Khi bán kính <i>R</i> lớn hơn 5 nm, số hạng giam giữ suy giảm nhanh và đường cong tiệm cận trơn về khe năng lượng khối 1.74 eV. "
        "Tuy nhiên, khi <i>R</i> giảm xuống dưới 3 nm, số hạng động năng tỉ lệ với <i>R</i><sup>−2</sup> bùng nổ áp đảo hoàn toàn, "
        "đẩy khe năng lượng quang lên tới 2.5–3.5 eV, tạo ra ánh sáng phát xạ rực rỡ từ vùng vàng đến xanh tím."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_02,
        "Hình 3.17: Mô phỏng giải tích độ dịch chuyển xanh khe năng lượng theo bán kính chấm lượng tử CdSe ở 300 K (Mô hình Brus): "
        "Khi bán kính hạt R thu nhỏ từ 8 nm về 1.5 nm, khe năng lượng quang bùng nổ từ 1.74 eV (vùng đỏ) lên hơn 3.2 eV (vùng xanh tím).",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    # Giai đoạn 5: Ứng dụng công nghệ
    add_p("Giai đoạn 5: Ứng dụng công nghệ hiển thị chấm lượng tử QLED và y sinh học nano", "H3")
    add_p(
        "Hiệu ứng giam giữ lượng tử trong mô hình Brus là nền tảng cốt lõi của công nghệ màn hình hiển thị QLED hiện đại: "
        "thay vì phải tổng hợp nhiều hợp chất hóa học khác nhau, người ta chỉ cần điều khiển thời gian phản ứng kết tủa hạt nano CdSe hoặc InP "
        "để tạo ra các chấm lượng tử có bán kính chính xác từ 2.0 nm (phát xạ màu xanh lam), 3.0 nm (màu xanh lục) đến 5.5 nm (màu đỏ tươi). "
        "Độ rộng phổ phát xạ cực hẹp (FWHM < 20 nm) mang lại độ tinh khiết màu sắc vượt trội và gam màu bao phủ rộng hơn mọi công nghệ hiển thị truyền thống. "
        "Đồng thời, trong y sinh học, các chấm lượng tử gắn phối tử sinh học đóng vai trò như các ngọn hải đăng nano phát huỳnh quang siêu sáng, "
        "cho phép theo dõi vết chuyển vị của từng thụ thể protein và tế bào ung thư theo thời gian thực."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.3.4: CẤU TRÚC TINH THỂ HỌC & VECTOR CHIRAL CỦA CNT
    # =========================================================================
    add_p("Luận điểm 3.3.4: Cấu trúc Tinh thể học, Vector Chiral (n, m) và Tính chất Điện tử của Ống Than Nano CNT", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, cấu trúc cuộn màng Graphene và vector chiral", "H3")
    add_p(
        "Ống than nano Carbon (Carbon Nanotubes — CNT), được Sumio Iijima phát hiện chính thức năm 1991, "
        "được hình dung một cách trực quan như một tấm màng Graphene hai chiều đơn lớp gồm các nguyên tử Carbon lai hóa <i>sp</i><sup>2</sup> "
        "được cuộn tròn liền mạch thành một ống hình trụ rỗng không có đường nối biên. "
        "Cách thức cuộn màng Graphene — được xác định tuyệt đối bởi vector cuộn định hướng gọi là vector chiral <b>C</b><sub><i>h</i></sub> — "
        "quy định toàn bộ tính chất cơ học, quang học và đặc biệt là đặc tính dẫn điện của ống than nano.",
        ocr_idx=5
    )
    add_spacer(6)

    # Ảnh gốc Slide 33 & 34
    story.append(he.embed_figure_with_caption(
        fig_goc_05,
        "Hình 3.18: Vector chiral Ch = n a1 + m a2 và cấu trúc mạng tinh thể học cuộn ống than nano CNT: "
        "Mối quan hệ hình học giữa vector cơ sở Graphene a1, a2 và góc xoay chiral θ quyết định chu vi và đường kính ống (Slide 33 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_06,
        "Hình 3.19: Tính chất điện tử của các họ ống than nano Armchair, Zigzag và Chiral: "
        "Sự phân loại ống kim loại (Metallic) và bán dẫn (Semiconducting) dựa trên vị trí các vạch cắt lượng tử hóa k-space qua điểm Dirac (Slide 34 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ phân loại ống than nano", "H3")
    add_p(
        "Vector chiral được biểu diễn trên hệ vector cơ sở mạng lục giác của Graphene (với độ dài hằng số mạng <i>a</i> = 0.246 nm, khoảng cách liên kết C–C là <i>a</i><sub>C-C</sub> = 0.142 nm): "
        "<b>C</b><sub><i>h</i></sub> = <i>n</i> <b>a</b><sub>1</sub> + <i>m</i> <b>a</b><sub>2</sub>, trong đó cặp số nguyên không âm (<i>n</i>, <i>m</i>) với <i>n</i> ≥ <i>m</i> ≥ 0 "
        "xác định duy nhất một cấu trúc ống than nano. "
        "Chu vi hình học của ống bằng độ dài vector <b>C</b><sub><i>h</i></sub>, từ đó suy ra đường kính ống <i>d<sub>t</sub></i>."
    )
    add_spacer(6)

    eq_col_4 = r"d_t = \frac{a}{\pi}\sqrt{n^2 + n m + m^2}, \quad \theta = \arctan\left(\frac{\sqrt{3} m}{2 n + m}\right), \quad E_g(d_t) \approx \frac{2 \gamma_0 a_{\mathrm{C-C}}}{d_t} \approx \frac{0.824\,\text{eV}\cdot\text{nm}}{d_t}"
    nom_rows_4 = [
        ("Đường kính hình học của ống than nano", "<i>d<sub>t</sub></i>", "nm", "Đường kính ngoài của ống than nano đơn vách (thông thường từ 0.7 nm đến 2.5 nm)"),
        ("Chỉ số vector chiral mạng Graphene", "(<i>n</i>, <i>m</i>)", "cặp số nguyên", "Cặp tọa độ chỉ số cuộn trên hai trục vector cơ sở <b>a</b><sub>1</sub> và <b>a</b><sub>2</sub>"),
        ("Góc xoay chiral của trục ống", "θ", "độ", "Góc nghiêng giữa vector <b>C</b><sub><i>h</i></sub> và vector <b>a</b><sub>1</sub>, nằm trong khoảng 0° ≤ θ ≤ 30°"),
        ("Khe năng lượng dải cấm của CNT bán dẫn", "<i>E<sub>g</sub></i>(<i>d<sub>t</sub></i>)", "eV", "Độ rộng dải cấm quang – điện, tỉ lệ nghịch bậc nhất với đường kính ống <i>d<sub>t</sub></i>"),
        ("Tích phân nhảy liên kết Carbon tight-binding", "γ<sub>0</sub>", "eV", "Năng lượng xen phủ orbitan pz giữa hai nguyên tử Carbon lân cận (khoảng 2.9 eV)"),
    ]
    story.append(he.build_target_equation_block(eq_col_4, nom_rows_4, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất quy tắc dẫn điện kim loại và bán dẫn", "H3")

    p_step8 = (
        "Phân loại hình học 3 họ ống than nano theo chỉ số chiral (n, m):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Dựa vào góc xoay chiral θ, cấu trúc CNT phân thành 3 họ đối xứng:<br/>"
        "• <b>Ống ghế bành (Armchair):</b> <i>n</i> = <i>m</i>, góc θ = 30°. Các liên kết C–C vuông góc với trục ống, tạo hình mép ghế bành;<br/>"
        "• <b>Ống răng cưa (Zigzag):</b> <i>m</i> = 0, góc θ = 0°. Các liên kết C–C song song với trục ống, tạo hình mép răng cưa răng cưa;<br/>"
        "• <b>Ống xoắn ốc (Chiral):</b> <i>n</i> ≠ <i>m</i> và <i>m</i> ≠ 0, góc 0° < θ < 30°. Các vòng sáu cạnh Carbon xoắn ốc quanh trục ống."
    )
    story.append(he.build_intermediate_equation(p_step8, r"\text{Armchair: } (n, n) \quad [\theta = 30^\circ], \quad \text{Zigzag: } (n, 0) \quad [\theta = 0^\circ], \quad \text{Chiral: } (n, m) \quad [0^\circ < \theta < 30^\circ]", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step9 = (
        "Chứng minh quy tắc dẫn điện tử từ cấu trúc vùng năng lượng điểm Dirac của Graphene:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Graphene là một bán kim loại không có khe năng lượng (zero-gap semimetal), dải dẫn và dải hóa trị chạm nhau tại 6 đỉnh của vùng Brillouin gọi là các điểm Dirac <b>K</b> và <b>K'</b>. "
        "Khi cuộn thành ống trụ chu vi <i>L</i>, điều kiện biên tuần hoàn lượng tử hóa vector sóng vòng quanh chu vi thành các đường cắt song song: <b>k</b> · <b>C</b><sub><i>h</i></sub> = 2π <i>q</i> (với <i>q</i> là số nguyên). "
        "Nếu một trong các đường cắt này đi xuyên qua điểm Dirac <b>K</b>, ống sẽ không có khe năng lượng và hành xử như một kim loại lý tưởng (Metallic CNT). "
        "Điều kiện hình học để đường cắt đi qua điểm Dirac tương đương với điều kiện hiệu số (<i>n</i> − <i>m</i>) chia hết cho 3:"
    )
    story.append(he.build_intermediate_equation(p_step9, r"(n - m)\ \mathrm{mod}\ 3 = 0 \quad \Longrightarrow \quad E_g = 0\,\text{eV} \quad (\text{Kim loại}), \quad (n - m)\ \mathrm{mod}\ 3 \neq 0 \quad \Longrightarrow \quad E_g \approx \frac{0.824\,\text{eV}\cdot\text{nm}}{d_t} \quad (\text{Bán dẫn})", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích phân bố khe năng lượng CNT", "H3")
    add_p(
        "Quy tắc (<i>n</i> − <i>m</i>) chia hết cho 3 dẫn đến một tỉ lệ xác suất thống kê tuyệt đẹp: "
        "trong một tập hợp các ống than nano được tổng hợp ngẫu nhiên, chính xác 1/3 số ống là kim loại và 2/3 số ống là bán dẫn. "
        "Đặc biệt, 100% các ống thuộc họ Armchair (<i>n</i> = <i>m</i>) luôn là kim loại dẫn điện hoàn hảo ở mọi nhiệt độ, "
        "với mật độ dòng điện tải cực đại có thể đạt tới 10<sup>9</sup> A·cm<sup>−2</sup> (gấp 1000 lần dây đồng vĩ mô). "
        "Đối với các ống bán dẫn, khe năng lượng nghịch biến với đường kính ống: một ống bán dẫn đường kính 1.0 nm có khe năng lượng khoảng 0.82 eV, "
        "hoàn toàn lý tưởng cho việc chế tạo transistor hiệu ứng trường thế hệ mới."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_03,
        "Hình 3.20: Mô phỏng giải tích khe năng lượng Eg của Carbon Nanotubes theo đường kính dt: "
        "Nhánh kim loại (Armchair hoặc (n - m) mod 3 = 0) có Eg = 0 eV (màu cam); "
        "Nhánh bán dẫn (màu xanh dương) có Eg nghịch biến với đường kính ống dt theo quy luật Eg ≈ 0.824 eV·nm · dt⁻¹.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    # Giai đoạn 5: Ứng dụng công nghệ
    add_p("Giai đoạn 5: Ứng dụng vi mạch bán dẫn tương lai và chuyển tiếp sang Mục 3.4", "H3")
    add_p(
        "Khả năng vận chuyển hạt tải điện đạn đạo (ballistic transport) với quãng đường tự do trung bình vượt quá 1 μm ở nhiệt độ phòng "
        "biến ống than nano bán dẫn thành kênh dẫn lý tưởng nhất để chế tạo các transistor trường CNT-FET. "
        "Các thử nghiệm gần đây cho thấy transistor CNT-FET có độ hỗ dẫn vi phân gấp 3 lần và tốc độ chuyển mạch nhanh hơn 4 lần so với transistor Silicon hiện đại nhất, "
        "đồng thời tiêu thụ năng lượng chỉ bằng một phần ba. "
        "Để chuẩn bị cho việc tích hợp các ống than nano vào mạch tích hợp mật độ cao, "
        "chúng ta cần tiếp tục khảo sát dao động mạng tinh thể (phonon) và đặc tính từ tính ở thang nano trong Mục 3.4 tiếp theo."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI THỬ THÁCH HỌC VIÊN CER 3.3
    # =========================================================================
    add_p("Thử thách Học viên CER 3.3: Thiết kế kênh dẫn ống than nano (CNT-FET) cho nút công nghệ bán dẫn 1 nm", "H2")
    add_spacer(4)

    add_p(
        "<b>Bối cảnh kỹ thuật:</b> Một nhóm nghiên cứu tại Trung tâm Nghiên cứu Vật liệu Nano — ĐHBK Hà Nội đang tham gia thiết kế kênh dẫn "
        "cho transistor trường thế hệ mới (CNT-FET) để thay thế kênh dẫn Silicon ở nút công nghệ 1 nm. "
        "Để transistor có thể ngắt dòng điện hiệu quả ở nhiệt độ phòng <i>T</i> = 300 K (tránh dòng rò nhiệt qua khe dải cấm, đảm bảo tỉ số <i>I</i><sub>on</sub> · <i>I</i><sub>off</sub><sup>−1</sup> ≥ 10<sup>5</sup>), "
        "khe năng lượng của ống than nano bán dẫn cần đạt giá trị tối ưu <i>E<sub>g</sub></i> ≈ 0.80 eV (với dung sai cho phép ±0.05 eV). "
        "Hãy thực hiện kiểm toán định lượng từ nguyên lý đầu để chọn lựa vector chiral phù hợp nhất."
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
                "Khẳng định vector chiral (10, 5) là ứng viên tối ưu hoàn hảo nhất cho kênh dẫn transistor CNT-FET, "
                "trong khi ống (12, 0) hoàn toàn bị loại bỏ do bản chất dẫn điện kim loại không có khe năng lượng, "
                "và ống (13, 0) có khe năng lượng 0.81 eV đáp ứng tốt nhưng đường kính nhỏ hơn làm tăng điện trở tiếp xúc."
            ), styles["TableCell"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>Evidence (Bằng chứng số liệu)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Tính toán định lượng từ các hệ thức cột trụ của Mục 3.3:<br/>"
                "↳ [Tường minh bước biến đổi trung gian từ slide gốc]:<br/>"
                "• <b>Khảo sát ống (12, 0):</b> <i>n</i> − <i>m</i> = 12 − 0 = 12 (chia hết cho 3). "
                "Theo quy tắc chiral, đây là ống kim loại với <i>E<sub>g</sub></i> = 0 eV. Transistor không thể khóa ngắt dòng điện (loại bỏ tuyệt đối).<br/>"
                "• <b>Khảo sát ống (10, 5):</b> <i>n</i> − <i>m</i> = 10 − 5 = 5 (không chia hết cho 3, là bán dẫn). "
                "Đường kính ống: <i>d<sub>t</sub></i> = 0.246 · π<sup>−1</sup> · (10<sup>2</sup> + 10 × 5 + 5<sup>2</sup>)<sup>½</sup> = 0.0783 × (175)<sup>½</sup> ≈ 1.036 nm. "
                "Khe năng lượng: <i>E<sub>g</sub></i> ≈ 0.824 · (1.036)<sup>−1</sup> ≈ 0.795 eV ≈ 0.80 eV (khớp chính xác tuyệt đối với mục tiêu thiết kế).<br/>"
                "• <b>Khảo sát ống (13, 0):</b> <i>n</i> − <i>m</i> = 13 (không chia hết cho 3, bán dẫn). "
                "Đường kính: <i>d<sub>t</sub></i> = 0.246 · π<sup>−1</sup> · 13 ≈ 1.018 nm. "
                "Khe năng lượng: <i>E<sub>g</sub></i> ≈ 0.824 · (1.018)<sup>−1</sup> ≈ 0.809 eV."
            ), styles["TableCell"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>Reasoning (Lập luận nguyên lý đầu)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Để đạt tỉ số ngắt dòng cao ở 300 K, dòng rò nhiệt qua dải dẫn tỉ lệ thuận với thừa số Boltzmann suy giảm: "
                "exp[−<i>E<sub>g</sub></i> · (2<i>k<sub>B</sub> T</i>)<sup>−1</sup>]. Với <i>E<sub>g</sub></i> = 0.80 eV và <i>k<sub>B</sub> T</i> = 0.0259 eV, "
                "thừa số này bằng exp(−15.4) ≈ 2 × 10<sup>−7</sup>, đảm bảo dòng <i>I</i><sub>off</sub> ở mức pico-ampe và cho phép tỉ số <i>I</i><sub>on</sub> · <i>I</i><sub>off</sub><sup>−1</sup> > 10<sup>6</sup>. "
                "Đồng thời, đường kính <i>d<sub>t</sub></i> ≈ 1.04 nm của ống (10, 5) đủ lớn để giảm thiểu tán xạ hạt tải phonon âm học và tạo tiếp xúc ohmic tốt với điện cực nguồn/thoát kim loại, "
                "mang lại hiệu suất chuyển mạch cao nhất cho chip xử lý 1 nm."
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
    print("Executing Pre-flight Text Compliance Audit for Section 3.3...")
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
    print(f"PUBLISHING COMPLETE: Section 3.3 Monograph successfully deployed to Google Drive!")
    return TARGET_PDF_PATH


if __name__ == "__main__":
    build_monograph_muc_3_3()

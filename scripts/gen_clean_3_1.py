# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Course: Co so vat ly va cong nghe nano (PH3470 - HUST)
Chapter 3: Dac trung cua vat lieu khi kich thuoc giam (What happens at the nanoscale?)
Section 3.1: Co hoc thang nano, dao dong tu dieu hoa va dinh luat ti le tan so
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

PDF_FILENAME = "Chuyen_Khao_Nano_Muc_3.1.pdf"
TARGET_PDF_PATH = os.path.join(PDF_DIR, PDF_FILENAME)


def build_monograph_muc_3_1():
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

    # Figure paths - 8 original figures
    fig_goc_01 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_01_Dong_Ho_Antikythera_Va_Dao_Dong_Dieu_Hoa.png")
    fig_goc_02 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_02_Dam_Cantilever_Va_Dao_Dong_Hai_Nguyen_Tu.png")
    fig_goc_03 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_03_The_Nang_Parabol_Dao_Dong_Tu.png")
    fig_goc_04 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_04_Ham_Song_Va_Xac_Suat_Dao_Dong_Tu_Luong_Tu.png")
    fig_goc_05 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_05_So_Sanh_Xac_Suat_Co_Dien_Va_Luong_Tu.png")
    fig_goc_06 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_06_Dao_Dong_Tat_Dan_Va_Cong_Huong_He_So_Q.png")
    fig_goc_07 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_07_The_Tuong_Tac_Lennard_Jones_Lien_Nguyen_Tu.png")
    fig_goc_08 = os.path.join(IMG_DIR, "[Goc]_Muc_3.1_Hinh_08_Do_Vong_Dam_Cantilever_AFM.png")

    # Figure paths - 3 simulation plots
    fig_sim_01 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.1_The_Nang_Lennard_Jones_Va_Xap_Xi_Dieu_Hoa.png")
    fig_sim_02 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.1_Mat_Do_Xac_Suat_Dao_Dong_Tu_Luong_Tu_Va_Co_Dien.png")
    fig_sim_03 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.1_Dinh_Luat_Ti_Le_Tan_So_Theo_Kich_Thuoc.png")

    # =========================================================================
    # H1 TIÊU ĐỀ PHÂN MỤC VÀ METADATA ĐÀO TẠO BÁCH KHOA
    # =========================================================================
    add_p("Chương 3: Đặc trưng của vật liệu khi kích thước giảm", "H1")
    add_p("Mục 3.1: Cơ học thang nano, dao động tử điều hòa và định luật tỉ lệ tần số", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Edward L. Wolf — Nanophysics and Nanotechnology, Chương 3; Slide bài giảng 1–21)</i>", "Caption")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Cơ sở vật lý và công nghệ nano (PH3470)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Viện Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Bài 3 (Slide 1–21); Wolf Nanotechnology Ch. 3"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu về bản chất cơ học ở thang nano và động lực học của các hệ dao động tử vi mô "
        "(PH3470 — HUST; đối chiếu Edward L. Wolf, Nanophysics and Nanotechnology, Chapter 3). "
        "Khảo sát toàn diện sự chuyển giao từ thế giới quan cơ học cổ điển tiền định kiểu Newton sang động lực học lượng tử gián đoạn, "
        "thiết lập phương trình vi phân dao động uốn đàn hồi của dầm cantilever trong kính hiển vi lực nguyên tử AFM và dao động liên kết giữa hai nguyên tử, "
        "đối chuẩn phân bố xác suất cổ điển nghịch biến với vận tốc và nghiệm hàm sóng Hermite của dao động tử điều hòa lượng tử theo nguyên lý tương ứng Bohr, "
        "phân tích ảnh hưởng của lực cản môi trường và hệ số phẩm chất Q, giải phẫu thế năng tương tác liên nguyên tử Lennard-Jones cùng gần đúng điều hòa bậc hai quanh đáy thế, "
        "chứng minh định luật tỉ lệ tần số dao động bùng nổ tỉ lệ nghịch với kích thước (tần số góc ω tỉ lệ với <i>L</i><sup>−1</sup> đạt ngưỡng GHz ở thang 100 nm), "
        "và giải quyết trọn vẹn hệ thống 3 bài toán định lượng kinh điển về dao động phân tử CO, hiệu ứng đồng vị và định luật cắt ngắn chiều dài liên kết đàn hồi."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 3.1
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Slide HUST &amp; Wolf)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.1.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Nghịch lý cỗ máy cổ điển &amp; Động lực học dao động dầm AFM"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Phương trình vi phân dao động, tần số góc tần số góc riêng ω<sub>0</sub> = (<i>k</i> · <i>m</i><sup>−1</sup>)<sup>½</sup>, bảo toàn cơ năng cơ năng toàn phần <i>E</i> = ½ <i>k A</i><sup>2</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Cỗ máy Antikythera, Dầm AFM (Slide 3–7)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.1.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Thế năng parabol &amp; Phân bố xác suất: Cổ điển vs Lượng tử"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Phổ năng lượng phổ năng lượng <i>E<sub>n</sub></i> = (<i>n</i> + ½) ħω, hàm sóng Hermite, bao hình Bohr <i>p</i><sub>cl</sub>(<i>x</i>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 10–12; Mô phỏng giải tích 3.1.2"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.1.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Lực cản nhớt, dao động tắt dần &amp; Thế tương tác Lennard-Jones"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hệ số phẩm chất <i>Q</i>, thế Lennard-Jones <i>U</i>(<i>r</i>) và độ cứng hiệu dụng <i>k</i><sub>eff</sub> quanh <i>r</i><sub>0</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 14–15; Mô phỏng giải tích 3.1.1"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.1.4</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Định luật tỉ lệ kích thước &amp; Tần số dao động siêu cao NEMS"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Độ cứng <i>k</i> ∝ <i>L</i>, khối lượng <i>m</i> ∝ <i>L</i><sup>3</sup> suy ra tần số tần số góc ω tỉ lệ với <i>L</i><sup>−1</sup> (15 GHz ở 100 nm)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 18; Mô phỏng giải tích 3.1.3"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.1.5</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hệ bài toán định lượng: Phân tử CO, hiệu ứng đồng vị &amp; cắt ngắn liên kết"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Khối lượng rút gọn μ, tần số <i>f</i> = 64.34 THz, λ = 4.66 μm, định lý cắt ngắn <i>K'</i> = 2<i>K</i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Dầm AFM Slide 16–17; Thử thách CER 3.1"), styles["TableCellCenter"]),
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
    # MPT 3.1.1: NGHỊCH LÝ CỔ ĐIỂN & ĐỘNG LỰC HỌC DAO ĐỘNG DẦM AFM
    # =========================================================================
    add_p("Luận điểm 3.1.1: Nghịch lý cỗ máy cổ điển &amp; Động lực học dao động điều hòa của dầm cantilever AFM và liên kết nguyên tử", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm & Nghịch lý
    add_p("Giai đoạn 1: Giới thiệu khái niệm, cỗ máy Antikythera và nghịch lý thế giới quan cơ học cổ điển", "H3")
    add_p(
        "Năm 1900, một thợ lặn Hy Lạp đã phát hiện một con tàu đắm cổ đại gần đảo Antikythera. "
        "Trong số các cổ vật trục vớt được, có một khối hợp kim đồng bị ăn mòn chứa hơn 30 bánh răng khớp nhau với độ tinh xảo phi thường, "
        "được chế tạo từ hơn 2000 năm trước để mô phỏng chính xác chuyển động thiên văn của Mặt Trời, Mặt Trăng và các hành tinh. "
        "Cơ chế Antikythera là minh chứng lịch sử cho thế giới quan cơ học cổ điển: vũ trụ được quan niệm như một cỗ máy đồng hồ khổng lồ, "
        "nơi mọi chuyển động của vật chất đều tuân theo các phương trình vi phân động lực học tất định của Isaac Newton.",
        ocr_idx=1
    )
    add_spacer(6)

    add_p(
        "Theo cơ học Newton, nếu biết chính xác vị trí và vận tốc ban đầu của một hạt, toàn bộ quỹ đạo quá khứ và tương lai của nó đều được dự đoán tuyệt đối. "
        "Tuy nhiên, khi thu nhỏ vật chất xuống quy mô nanomet, cơ học cổ điển sụp đổ hoàn toàn trước ba nghịch lý vật lý nền tảng: "
        "(1) Tại sao các nguyên tử như Hydro chỉ nhận các mức năng lượng gián đoạn mà không phát xạ liên tục xoáy ốc vào hạt nhân? "
        "(2) Tại sao electron và photon vừa hành xử như sóng lan truyền giao thoa vừa hành xử như hạt va chạm định xứ? "
        "(3) Tại sao không thể xác định đồng thời cả vị trí và động lượng của một hạt với độ chính xác vô hạn? "
        "Để trả lời những câu hỏi này, chúng ta phải nghiên cứu động lực học của các cấu trúc vi mô cơ bản nhất: dao động đàn hồi của thanh dầm cantilever vi mô "
        "và dao động tương tác giữa các nguyên tử trong mạng tinh thể.",
        ocr_idx=2
    )
    add_spacer(8)

    # Hình ảnh gốc Slide 4
    story.append(he.embed_figure_with_caption(
        fig_goc_01,
        "Hình 3.1: Cơ học cổ điển và phương trình động lực học dao động điều hòa: "
        "Hệ khối lượng m nối lò xo đàn hồi k minh họa chuyển động điều hòa không ma sát, làm mô hình nền tảng cho dao động dầm nano và liên kết nguyên tử (Slide 4 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    # Hình ảnh gốc Slide 7
    story.append(he.embed_figure_with_caption(
        fig_goc_02,
        "Hình 3.2: Cấu trúc dầm cantilever (beam) và dao động xuyên tâm của hai nguyên tử: "
        "(a) Dầm vi mô có một đầu ngàm cố định, đầu kia tự do dao động dùng trong cảm biến AFM; "
        "(b) Dao động của hai nguyên tử dọc trục liên kết dưới tác dụng của lực tĩnh điện Coulomb và lực đẩy lõi nguyên tử (Slide 7 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ dao động điều hòa", "H3")
    add_p(
        "Hệ dao động cơ học đơn giản nhất gồm một vật thể có khối lượng quán tính <i>m</i> liên kết với một cấu trúc đàn hồi có độ cứng <i>k</i>. "
        "Khi vật lệch khỏi vị trí cân bằng một khoảng li độ <i>y</i>, cấu trúc đàn hồi sinh ra lực hồi phục hướng về tâm cân bằng theo định luật Hooke: "
        "<i>F</i> = −<i>k</i> · <i>y</i>. Áp dụng định luật II Newton <i>F</i> = <i>m</i> · <i>a</i> với <i>a</i> là đạo hàm bậc hai của li độ theo thời gian, "
        "ta thu được phương trình vi phân động lực học thuần nhất bậc hai của dao động tử điều hòa tự do."
    )
    add_spacer(6)

    eq_col_1 = r"m \frac{d^2 y}{dt^2} + k y = 0 \quad \Longrightarrow \quad y(t) = A \cos\left(\omega_0 t + \varphi\right), \quad \omega_0 = \sqrt{\frac{k}{m}}, \quad E = \frac{1}{2} k A^2"
    nom_rows_1 = [
        ("Li độ dao động lệch khỏi vị trí cân bằng", "<i>y</i>(<i>t</i>)", "m hoặc nm", "Độ dời tức thời của khối lượng hoặc đỉnh dầm cantilever dọc theo trục dao động"),
        ("Khối lượng quán tính hiệu dụng", "<i>m</i>", "kg", "Khối lượng hiệu dụng của dầm dao động hoặc khối lượng rút gọn của cặp nguyên tử liên kết"),
        ("Hệ số đàn hồi của dầm hoặc liên kết", "<i>k</i>", "N·m<sup>−1</sup>", "Độ cứng cơ học chống lại biến dạng đàn hồi uốn hoặc giãn liên kết nguyên tử"),
        ("Tần số góc dao động riêng tự do", "<i>\u03c9</i><sub>0</sub>", "rad·s<sup>−1</sup>", "Tốc độ biến thiên pha dao động tự nhiên của hệ khi không có lực cản môi trường"),
        ("Năng lượng cơ học toàn phần", "<i>E</i>", "J hoặc eV", "Tổng động năng và thế năng đàn hồi được bảo toàn tuyệt đối trong chân không"),
    ]
    story.append(he.build_target_equation_block(eq_col_1, nom_rows_1, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phương trình vi phân và bảo toàn năng lượng", "H3")

    p_step1 = (
        "Thiết lập phương trình động lực học Newton từ định luật Hooke và định luật II Newton:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét vật khối lượng <i>m</i> chịu lực đàn hồi tuyến tính tỉ lệ với li độ dịch chuyển <i>y</i>. "
        "Lực tác dụng luôn có xu hướng đưa hệ về vị trí cân bằng bền, do đó mang dấu âm đối kháng với hướng chuyển dịch: "
        "<i>F</i> = −<i>k</i> · <i>y</i>. Đặt vào phương trình Newton <i>F</i> = <i>m</i> · <i>a</i> với gia tốc <i>a</i> là đạo hàm bậc hai của li độ theo thời gian:"
    )
    story.append(he.build_intermediate_equation(p_step1, r"m \frac{d^2 y}{dt^2} = -k \cdot y \quad \Longleftrightarrow \quad m \frac{d^2 y}{dt^2} + k \cdot y = 0", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step2 = (
        "Chuẩn hóa phương trình vi phân về dạng dao động điều hòa tự do bằng cách đặt tần số góc riêng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Chia cả hai vế cho khối lượng quán tính <i>m</i> và đặt hằng số thực dương tỉ số <i>k</i> trên <i>m</i>. "
        "Phương trình đặc trưng λ<sup>2</sup> + <i>\u03c9</i><sub>0</sub><sup>2</sup> = 0 có hai nghiệm ảo thuần túy λ = ± <i>i</i> <i>\u03c9</i><sub>0</sub>, "
        "cho phép viết nghiệm thực tổng quát dưới dạng hàm điều hòa cosin với biên độ <i>A</i> và pha ban đầu φ:"
    )
    story.append(he.build_intermediate_equation(p_step2, r"\frac{d^2 y}{dt^2} + \omega_0^2 \cdot y = 0 \quad \Longrightarrow \quad y(t) = A \cos\left(\omega_0 t + \varphi\right), \quad \omega_0 = \sqrt{\frac{k}{m}}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step3 = (
        "Xác định hàm vận tốc và gia tốc tức thời thông qua phép lấy đạo hàm theo thời gian:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Vận tốc tức thời là đạo hàm bậc nhất của li độ theo thời gian, lệch pha vuông góc π/2 so với li độ: vận tốc tức thời trễ pha π/2 so với li độ. "
        "Gia tốc tức thời là đạo hàm bậc hai, ngược pha π so với li độ:"
    )
    story.append(he.build_intermediate_equation(p_step3, r"v(t) = \frac{dy}{dt} = - A \omega_0 \sin\left(\omega_0 t + \varphi\right), \quad a(t) = \frac{d^2 y}{dt^2} = - A \omega_0^2 \cos\left(\omega_0 t + \varphi\right) = - \omega_0^2 \cdot y(t)", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step4 = (
        "Chứng minh sự bảo toàn năng lượng cơ học toàn phần của dao động tử tự do:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Năng lượng toàn phần <i>E</i> là tổng động năng động năng <i>T</i> = ½ <i>m v</i><sup>2</sup> và thế năng đàn hồi <i>U</i> = ½ <i>k y</i><sup>2</sup>. "
        "Thay thế biểu thức <i>y</i>(<i>t</i>) và <i>v</i>(<i>t</i>) cùng đồng nhất thức sin<sup>2</sup> + cos<sup>2</sup> = 1:"
    )
    story.append(he.build_intermediate_equation(p_step4, r"E = T + U = \frac{1}{2} m v(t)^2 + \frac{1}{2} k y(t)^2 = \frac{1}{2} k A^2 \sin^2\left(\omega_0 t + \varphi\right) + \frac{1}{2} k A^2 \cos^2\left(\omega_0 t + \varphi\right) = \frac{1}{2} k A^2 = \text{const}", styles=styles, is_expanded_from_slide=True))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận và thực chiến dầm Cantilever AFM", "H3")
    add_p(
        "Trong kính hiển vi lực nguyên tử (AFM), dầm cantilever đóng vai trò là một dao động tử điều hòa cực nhạy để ghi nhận tương tác bề mặt. "
        "Độ võng tĩnh δ của dầm dưới tác dụng của lực tập trung <i>F</i> tại đỉnh được xác định từ lý thuyết đàn hồi Euler-Bernoulli: "
        "δ = <i>F</i> · <i>L</i><sup>3</sup> · (3<i>E</i> <i>I</i>)<sup>−1</sup>, với <i>E</i> là môđun Young của vật liệu (Silicon hoặc Si<sub>3</sub>N<sub>4</sub>) "
        "và <i>I</i> = <i>w</i> · <i>t</i><sup>3</sup> · 12<sup>−1</sup> là mômen quán tính hình học của mặt cắt ngang dầm (chiều rộng <i>w</i>, độ dày <i>t</i>). "
        "Từ đó, độ cứng đàn hồi của dầm cantilever AFM được tính chính xác bằng: độ cứng dầm <i>k</i> = 3<i>E</i> <i>I</i> · <i>L</i><sup>−3</sup> = <i>E</i> <i>w</i> <i>t</i><sup>3</sup> · (4<i>L</i><sup>3</sup>)<sup>−1</sup>."
    )
    add_spacer(6)

    add_p(
        "Khảo sát các giới hạn tiệm cận hình học:<br/>"
        "• Tiệm cận độ dày dầm mỏng <i>t</i> → 0: Độ cứng <i>k</i> suy giảm theo lũy thừa bậc ba <i>t</i><sup>3</sup>, cho phép chế tạo các dầm siêu mềm có độ cứng <i>k</i> ~ 0.01–0.1 N/m "
        "(nhỏ hơn cả độ cứng liên kết hóa học giữa hai nguyên tử ~ 10 N/m), bảo đảm đầu dò AFM không phá hủy mẫu sinh học mềm như màng lipid hay DNA.<br/>"
        "• Tiệm cận chiều dài dầm ngắn <i>L</i> → 0: Độ cứng tăng vọt theo <i>L</i><sup>−3</sup>, đồng thời khối lượng giảm theo <i>L</i>, "
        "làm tần số dao động riêng tăng vọt phục vụ chế độ đo tapping mode tốc độ cao (High-speed AFM)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.1.2: THẾ NĂNG PARABOL & PHÂN BỐ XÁC SUẤT (CỔ ĐIỂN VS LƯỢNG TỬ)
    # =========================================================================
    add_p("Luận điểm 3.1.2: Thế năng parabol và phân bố xác suất: Đối chuẩn Cổ điển vs Cơ học lượng tử (Bohr Correspondence Principle)", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, thế năng parabol và nghịch lý phân bố xác suất tìm hạt", "H3")
    add_p(
        "Thế năng của dao động tử điều hòa có dạng một đường cong parabol đối xứng qua vị trí cân bằng: "
        "thế năng đàn hồi parabol <i>U</i>(<i>x</i>) = ½ <i>k x</i><sup>2</sup>. "
        "Trong cơ học cổ điển, khi hạt dao động giữa hai điểm đảo chiều tọa độ <i>x</i> = −<i>A</i> và <i>x</i> = +<i>A</i>, "
        "vận tốc của hạt đạt cực đại tại tâm <i>x</i> = 0 và giảm dần về 0 tại các biên đảo chiều. "
        "Do thời gian hạt lưu lại trong một khoảng không gian <i>dx</i> tỉ lệ nghịch với vận tốc <i>v</i>(<i>x</i>), "
        "xác suất tìm thấy hạt trong cơ học cổ điển <i>p</i><sub>cl</sub>(<i>x</i>) đạt giá trị cực tiểu tại tâm và phân kỳ cực đại ở hai biên dao động: "
        "xác suất tìm thấy hạt trong cơ học cổ điển tỉ lệ nghịch với vận tốc tức thời, có biểu thức phụ thuộc vào li độ và đạt cực đại ở hai biên đảo chiều.",
        ocr_idx=10
    )
    add_spacer(6)

    # Hình ảnh gốc Slide 10, 11, 12
    story.append(he.embed_figure_with_caption(
        fig_goc_03,
        "Hình 3.3: Dạng giếng thế năng parabol của dao động tử điều hòa: "
        "Đường cong thế năng parabolic và tần số dao động riêng tự do (Slide 10 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_04,
        "Hình 3.4: Phân bố năng lượng và hàm sóng của dao động tử điều hòa lượng tử: "
        "Các mức năng lượng gián đoạn cách đều nhau và hàm sóng Hermite ứng với các số lượng tử n = 0, 1, 2, 3 (Slide 11 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_05,
        "Hình 3.5: Đối chuẩn xác suất tìm thấy hạt trong cơ học cổ điển và cơ học lượng tử: "
        "Xác suất cổ điển tỉ lệ nghịch với vận tốc <i>v</i> đạt giá trị nhỏ nhất tại vị trí cân bằng và lớn nhất tại hai biên; "
        "hoàn toàn đối lập với trạng thái cơ bản lượng tử n = 0 có xác suất cực đại tại tâm (Slide 12 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ dao động tử điều hòa lượng tử", "H3")
    add_p(
        "Khi giải phương trình Schrödinger dừng cho hạt chuyển động trong giếng thế parabol thế năng đàn hồi parabol bậc hai, "
        "điều kiện biên chuẩn hóa và tính hữu hạn của hàm sóng tại vô cùng đòi hỏi năng lượng của hệ phải bị lượng tử hóa thành các mức rời rạc cách đều nhau một lượng ħ<i>\u03c9</i><sub>0</sub>. "
        "Hàm sóng của mỗi trạng thái dừng được biểu diễn chính xác qua hệ đa thức Hermite trực giao."
    )
    add_spacer(6)

    eq_col_2 = r"E_n = \left( n + \frac{1}{2} \right) \hbar \omega_0, \quad \psi_n(\xi) = \left( \frac{m \omega_0}{\pi \hbar} \right)^{\frac{1}{4}} \frac{1}{\sqrt{2^n n!}} H_n(\xi) \exp\left( - \frac{\xi^2}{2} \right), \quad \xi = \sqrt{\frac{m \omega_0}{\hbar}} x"
    nom_rows_2 = [
        ("Mức năng lượng lượng tử hóa bậc n", "<i>E<sub>n</sub></i>", "J hoặc eV", "Phổ năng lượng gián đoạn cách đều nhau của dao động tử lượng tử"),
        ("Số lượng tử dao động", "<i>n</i>", "không thứ nguyên", "Số nguyên không âm <i>n</i> = 0, 1, 2, ... đánh số các trạng thái dừng kích thích"),
        ("Hằng số Planck rút gọn", "ħ", "J·s", "Lượng tử tác dụng nền tảng của vật lý lượng tử ħ = 1.05457 × 10<sup>−34</sup> J·s"),
        ("Đa thức Hermite bậc n", "<i>H<sub>n</sub></i>(ξ)", "không thứ nguyên", "Hệ đa thức trực giao giải tích xác định số nút không gian của hàm sóng lượng tử"),
        ("Tọa độ không thứ nguyên hóa", "ξ", "không thứ nguyên", "Khoảng cách tọa độ quy chuẩn theo độ rộng đặc trưng dao động tử độ rộng đặc trưng dao động tử <i>x</i><sub>0</sub>"),
    ]
    story.append(he.build_target_equation_block(eq_col_2, nom_rows_2, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phương trình Schrödinger và đa thức Hermite", "H3")

    p2_step1 = (
        "Thiết lập phương trình Schrödinger dừng một chiều trong giếng thế parabol:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Thế năng tương tác đàn hồi là thế năng đàn hồi parabol bậc hai. "
        "Toán tử Hamiltonian toàn phần bao gồm động năng vi phân và thế năng tọa độ: toán tử Hamiltonian toàn phần:"
    )
    story.append(he.build_intermediate_equation(p2_step1, r"- \frac{\hbar^2}{2m} \frac{d^2 \psi}{dx^2} + \frac{1}{2} m \omega_0^2 x^2 \psi = E \psi", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p2_step2 = (
        "Chuyển đổi sang hệ biến số không thứ nguyên để đơn giản hóa phương trình vi phân:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Định nghĩa biến tọa độ không thứ nguyên tọa độ không thứ nguyên ξ và năng lượng quy chuẩn ε. "
        "Khi đó đạo hàm bậc hai biến đổi theo quy tắc dây chuyền: toán tử vi phân chuyển sang biến số không thứ nguyên:"
    )
    story.append(he.build_intermediate_equation(p2_step2, r"\frac{d^2 \psi}{d\xi^2} + \left( \varepsilon - \xi^2 \right) \psi = 0, \quad \varepsilon = \frac{2E}{\hbar \omega_0}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p2_step3 = (
        "Khảo sát hành vi tiệm cận tại vô cùng và thiết lập phương trình vi phân Hermite:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi |ξ| → ∞, số hạng ε trở nên không đáng kể so với ξ<sup>2</sup>, phương trình tiệm cận <i>d</i><sup>2</sup>ψ/<i>d</i>ξ<sup>2</sup> ≈ ξ<sup>2</sup> ψ có nghiệm hội tụ là hàm Gauss. "
        "Tách nghiệm toàn phần ψ(ξ) = <i>H</i>(ξ) hàm Gauss và thay vào phương trình vi phân, ta thu được phương trình Hermite:"
    )
    story.append(he.build_intermediate_equation(p2_step3, r"\frac{d^2 H}{d\xi^2} - 2\xi \frac{dH}{d\xi} + (\varepsilon - 1) H = 0 \quad \Longrightarrow \quad \varepsilon - 1 = 2n \quad (n = 0, 1, 2...)", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p2_step4 = (
        "Dẫn xuất phổ năng lượng lượng tử hóa và năng lượng điểm không:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Từ điều kiện ngắt chuỗi lũy thừa để hàm sóng không phân kỳ tại vô cùng, ta có ε = 2<i>n</i> + 1. "
        "Thay biểu thức năng lượng quy chuẩn vào hệ thức trên, ta trực tiếp suy ra phổ năng lượng cách đều kinh điển:"
    )
    story.append(he.build_intermediate_equation(p2_step4, r"\frac{2E_n}{\hbar \omega_0} = 2n + 1 \quad \Longleftrightarrow \quad E_n = \left( n + \frac{1}{2} \right) \hbar \omega_0, \quad E_0 = \frac{1}{2} \hbar \omega_0", styles=styles, is_expanded_from_slide=True))
    add_spacer(8)

    # Đồ thị mô phỏng 2
    story.append(he.embed_figure_with_caption(
        fig_sim_02,
        "Hình 3.6: Mô phỏng giải tích mật độ xác suất dao động tử điều hòa lượng tử vs bao hình cổ điển: "
        "Mật độ xác suất |ψn(ξ)|^2 ở các mức năng lượng n = 0, 2, 8 đối chuẩn với phân bố xác suất cổ điển pcl(x). "
        "Ở n = 0, hạt có xác suất lớn nhất tại tâm x = 0; khi n tăng lên n = 8, các đỉnh xác suất dày đặc tiệm cận chính xác đường bao cổ điển (Nguyên lý tương ứng Bohr).",
        kind="sim",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận Bohr và hiện tượng xuyên hầm lượng tử", "H3")
    add_p(
        "Phân tích sự khác biệt sâu sắc giữa mô tả lượng tử và cổ điển thông qua hai hiện tượng vật lý then chốt:<br/>"
        "• Hiện tượng xuyên hầm lượng tử ngoài biên cổ điển (|<i>x</i>| > <i>A</i>): "
        "Trong cơ học cổ điển, hạt không bao giờ có thể vượt qua hai điểm đảo chiều biên độ biên độ dao động cổ điển <i>A</i> "
        "vì động năng ngoài vùng này sẽ bị âm <i>T</i> = <i>E</i> − <i>U</i>(<i>x</i>) < 0 (vùng cổ điển cấm). "
        "Tuy nhiên, hàm sóng lượng tử ψ<sub><i>n</i></sub>(<i>x</i>) có phần đuôi hàm mũ suy giảm chậm hàm Gauss lan tỏa ra ngoài vùng cấm, "
        "dẫn đến xác suất tìm thấy hạt tại |<i>x</i>| > <i>A</i> luôn khác không (đạt ~16% ở trạng thái cơ bản <i>n</i> = 0).<br/>"
        "• Nguyên lý tương ứng Bohr (Bohr Correspondence Principle): "
        "Khi số lượng tử kích thích rất lớn (<i>n</i> ≫ 1), khoảng cách giữa các nút sóng liên tiếp thu hẹp cực nhanh theo tỉ lệ nghịch biến với căn bậc hai của <i>n</i>. "
        "Giá trị trung bình trượt trong một khoảng không gian nhỏ của mật độ xác suất lượng tử |ψ<sub><i>n</i></sub>(<i>x</i>)|<sup>2</sup> "
        "hội tụ chính xác về đường bao hàm phân bố xác suất của cơ học cổ điển <i>p</i><sub>cl</sub>(<i>x</i>), "
        "xóa nhòa ranh giới giữa hai lý thuyết ở giới hạn vĩ mô."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.1.3: LỰC CẢN NHỚT & THẾ TƯƠNG TÁC LENNARD-JONES
    # =========================================================================
    add_p("Luận điểm 3.1.3: Lực cản môi trường, dao động tắt dần, cộng hưởng cơ học và thế tương tác Lennard-Jones", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, lực cản môi trường và tương tác liên nguyên tử thực tế", "H3")
    add_p(
        "Trong môi trường thực tế (không khí, dung dịch nước hoặc chất lỏng sinh học), dao động của dầm nano luôn chịu tác dụng của lực cản ma sát nhớt. "
        "Lực cản này tiêu tán cơ năng thành nhiệt năng, làm biên độ dao động suy giảm dần theo thời gian (dao động tắt dần). "
        "Để duy trì dao động điều hòa ổn định, cần cấp năng lượng bù đắp bằng một ngoại lực kích thích tuần hoàn, dẫn đến hiện tượng cộng hưởng cơ học. "
        "Đồng thời, ở cấp độ hai nguyên tử liên kết trong mạng tinh thể, lực hồi phục đàn hồi không phải là lò xo tuyến tính lý tưởng "
        "mà xuất phát từ thế năng tương tác phi điều hòa Lennard-Jones (6-12) giữa các đám mây điện tử.",
        ocr_idx=14
    )
    add_spacer(6)

    # Hình ảnh gốc Slide 14, 15
    story.append(he.embed_figure_with_caption(
        fig_goc_06,
        "Hình 3.7: Dao động tắt dần có lực cản và hiện tượng cộng hưởng cơ học: "
        "Lực cản môi trường <i>F</i><sub>can</sub> = −<i>b</i> <i>v</i> làm suy giảm biên độ dao động theo thời gian; "
        "hệ cần ngoại lực kích thích tuần hoàn để bù đắp năng lượng và duy trì cộng hưởng (Slide 14 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_07,
        "Hình 3.8: Thế năng tương tác Lennard-Jones giữa hai nguyên tử: "
        "Đường cong thế năng tương tác gồm lực hút van der Waals tỉ lệ r^{-6} và lực đẩy Pauli tỉ lệ r^{-12}, "
        "xác định vị trí cân bằng <i>r</i><sub>0</sub> tại đáy giếng thế nơi lực tương tác triệt tiêu bằng không (Slide 15 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ thế năng Lennard-Jones", "H3")
    add_p(
        "Thế năng tương tác Lennard-Jones (6-12) là mô hình giải tích thực nghiệm kinh điển mô tả tương tác giữa hai nguyên tử trung hòa. "
        "Lực tương tác liên nguyên tử <i>F</i>(<i>r</i>) là gradient âm của thế năng. "
        "Tại vị trí đáy giếng thế năng <i>r</i><sub>0</sub> = 1.122 σ, lực tương tác triệt tiêu hoàn toàn. "
        "Khai triển Taylor bậc hai của <i>U</i>(<i>r</i>) quanh <i>r</i><sub>0</sub> cho phép xác định độ cứng đàn hồi hiệu dụng <i>k</i><sub>eff</sub> của liên kết."
    )
    add_spacer(6)

    eq_col_3 = r"U(r) = 4 \varepsilon \left[ \left( \frac{\sigma}{r} \right)^{12} - \left( \frac{\sigma}{r} \right)^6 \right], \quad F(r) = - \frac{dU}{dr}, \quad k_{\mathrm{eff}} = \left. \frac{d^2 U}{dr^2} \right|_{r = r_0} = \frac{72 \varepsilon}{2^{\frac{1}{3}} \sigma^2} \approx 57.15 \frac{\varepsilon}{\sigma^2}"
    nom_rows_3 = [
        ("Thế năng tương tác Lennard-Jones", "<i>U</i>(<i>r</i>)", "J hoặc eV", "Năng lượng tương tác toàn phần giữa hai nguyên tử cách nhau khoảng cách r"),
        ("Độ sâu cực đại của giếng thế năng", "ε", "J hoặc eV", "Năng lượng liên kết cần thiết để phân ly hai nguyên tử từ khoảng cách cân bằng ra vô cùng"),
        ("Khoảng cách va chạm đặc trưng hữu hạn", "σ", "nm hoặc Å", "Khoảng cách liên hạt nơi thế năng tương tác triệt tiêu <i>U</i>(σ) = 0"),
        ("Khoảng cách cân bằng bền liên nguyên tử", "<i>r</i><sub>0</sub>", "nm", "Vị trí đáy giếng thế nơi lực tương tác triệt tiêu: <i>r</i><sub>0</sub> = 1.122 σ ≈ 1.122 σ"),
        ("Độ cứng đàn hồi hiệu dụng bậc hai", "<i>k</i><sub>eff</sub>", "N·m<sup>−1</sup>", "Độ cong của giếng thế năng tại đáy cân bằng, chi phối tần số dao động liên kết"),
    ]
    story.append(he.build_target_equation_block(eq_col_3, nom_rows_3, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất dao động tắt dần và khai triển Taylor thế Lennard-Jones", "H3")

    p3_step1 = (
        "Thiết lập phương trình vi phân dao động tắt dần có lực cản môi trường:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Lực tổng hợp tác dụng lên vật gồm lực đàn hồi hồi phục <i>F</i><sub>dh</sub> = −<i>k</i> <i>y</i> và lực cản nhớt tỉ lệ với vận tốc lực cản tỉ lệ với vận tốc. "
        "Phương trình động lực học Newton trở thành: định luật II Newton cho hệ dao động có lực cản:"
    )
    story.append(he.build_intermediate_equation(p3_step1, r"\frac{d^2 y}{dt^2} + 2\gamma \frac{dy}{dt} + \omega_0^2 y = 0, \quad \gamma = \frac{b}{2m}, \quad \omega_0 = \sqrt{\frac{k}{m}}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p3_step2 = (
        "Xác định nghiệm tắt dần dưới tới hạn và định nghĩa hệ số phẩm chất Q:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi lực cản nhỏ (γ < <i>\u03c9</i><sub>0</sub>), nghiệm vi phân có dạng dao động với biên độ suy giảm theo hàm mũ: <i>y</i>(<i>t</i>) = <i>A</i><sub>0</sub> exp(−γ <i>t</i>) cos(<i>\u03c9</i><sub><i>d</i></sub> <i>t</i> + φ) "
        "với tần số dao động suy giảm <i>\u03c9</i><sub><i>d</i></sub>. "
        "Hệ số phẩm chất <i>Q</i> định lượng số chu kỳ dao động trước khi năng lượng suy giảm đáng kể:"
    )
    story.append(he.build_intermediate_equation(p3_step2, r"Q = \frac{\omega_0}{2\gamma} = \frac{m \omega_0}{b} = \frac{\sqrt{k m}}{b}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p3_step3 = (
        "Lấy đạo hàm bậc nhất của thế Lennard-Jones để xác định lực tương tác liên nguyên tử:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Lực tương tác là gradient âm của thế năng: lực tương tác là gradient âm của thế năng. "
        "Lấy đạo hàm từng số hạng của biểu thức <i>U</i>(<i>r</i>) = 4ε [σ<sup>12</sup> <i>r</i><sup>−12</sup> − σ<sup>6</sup> <i>r</i><sup>−6</sup>]:"
    )
    story.append(he.build_intermediate_equation(p3_step3, r"F(r) = - \frac{dU}{dr} = 24 \frac{\varepsilon}{\sigma} \left[ 2 \left( \frac{\sigma}{r} \right)^{13} - \left( \frac{\sigma}{r} \right)^7 \right]", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p3_step4 = (
        "Xác định khoảng cách cân bằng bền và khai triển Taylor bậc hai quanh đáy giếng thế:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Tại vị trí cân bằng bền <i>r</i><sub>0</sub>, lực tương tác triệt tiêu <i>F</i>(<i>r</i><sub>0</sub>) = 0, suy ra điều kiện cân bằng lực triệt tiêu, dẫn tới <i>r</i><sub>0</sub> = 1.122 σ ≈ 1.12246 σ. "
        "Lấy đạo hàm bậc hai của thế năng tại vị trí cân bằng để tìm độ cứng đàn hồi tương đương:"
    )
    story.append(he.build_intermediate_equation(p3_step4, r"k_{\mathrm{eff}} = \left. \frac{d^2 U}{dr^2} \right|_{r = r_0} = 4\varepsilon \left[ \frac{156 \sigma^{12}}{r_0^{14}} - \frac{42 \sigma^6}{r_0^8} \right] = \frac{72 \varepsilon}{2^{\frac{1}{3}} \sigma^2} \approx 57.146 \frac{\varepsilon}{\sigma^2}", styles=styles, is_expanded_from_slide=True))
    add_spacer(8)

    # Đồ thị mô phỏng 1
    story.append(he.embed_figure_with_caption(
        fig_sim_01,
        "Hình 3.9: Mô phỏng giải tích thế năng Lennard-Jones và xấp xỉ điều hòa bậc hai quanh đáy thế: "
        "So sánh đường cong thế thực tế U(r) (xanh đậm) với đường cong parabol xấp xỉ điều hòa Uharm(r) (cam đứt nét). "
        "Tại lân cận đáy thế r0 = 1.122 sigma, thế năng có độ sâu -epsilon và trùng khít hoàn hảo với dao động tử điều hòa có độ cứng hiệu dụng <i>k</i><sub>eff</sub>.",
        kind="sim",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận và thực chiến cảm biến AFM cộng hưởng", "H3")
    add_p(
        "Ứng dụng hệ số phẩm chất <i>Q</i> và độ dốc lực gradient lực tương tác trong kính hiển vi AFM chế độ không tiếp xúc (Non-contact AFM):<br/>"
        "• Dịch chuyển tần số cộng hưởng do gradient lực: Khi đầu dò AFM dao động ở tần số riêng <i>f</i><sub>0</sub> tiến lại gần bề mặt mẫu, "
        "lực tương tác bề mặt <i>F</i><sub>ts</sub>(<i>z</i>) tác dụng lên mũi dò làm biến đổi độ cứng hiệu dụng của dầm phụ thuộc gradient lực. "
        "Độ dịch chuyển tần số cộng hưởng đo được tỉ lệ thuận với gradient lực: độ dịch tần tỉ đối tỉ lệ thuận với gradient lực theo phương thẳng đứng.<br/>"
        "• Tối ưu hóa hệ số phẩm chất <i>Q</i>: Trong môi trường chất lỏng, lực cản nhớt rất lớn khiến <i>Q</i> ~ 10–50; "
        "trong không khí <i>Q</i> ~ 300–1000; trong khi trong môi trường siêu chân không (UHV), không có phân tử khí cản trở, <i>Q</i> đạt tới 50.000–200.000. "
        "Hệ số <i>Q</i> cực cao làm đỉnh cộng hưởng vô cùng sắc nhọn, cho phép AFM phát hiện lực tương tác yếu đến thang piconewton (10<sup>−12</sup> N) "
        "và phân giải hình ảnh cấu trúc orbital của từng phân tử đơn lẻ."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.1.4: ĐỊNH LUẬT TỈ LỆ KÍCH THƯỚC & TẦN SỐ NANO NEMS
    # =========================================================================
    add_p("Luận điểm 3.1.4: Định luật tỉ lệ kích thước (Scaling Laws) và tần số dao động siêu cao ở thang nano (NEMS GHz)", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm và định luật tỉ lệ hình học khi thu nhỏ vật chất", "H3")
    add_p(
        "Một trong những hệ quả vật lý quan trọng và kỳ thú nhất khi thu nhỏ cấu trúc từ thang vĩ mô xuống thang nano là sự biến đổi phi tuyến của các đại lượng vật lý theo kích thước hình học đặc trưng <i>L</i> (Định luật tỉ lệ — Scaling Laws). "
        "Trong khi diện tích bề mặt tỉ lệ với <i>L</i><sup>2</sup> và thể tích tỉ lệ với <i>L</i><sup>3</sup>, "
        "các thông số cơ học như khối lượng quán tính và độ cứng đàn hồi lại suy giảm với các bậc lũy thừa hoàn toàn khác nhau. "
        "Sự bất đối xứng về bậc tỉ lệ này dẫn tới sự bùng nổ của tần số dao động cộng hưởng cơ học ở quy mô nanomet.",
        ocr_idx=18
    )
    add_spacer(6)

    # Hình ảnh gốc Slide 18
    story.append(he.embed_figure_with_caption(
        fig_goc_08,
        "Hình 3.10: Định luật tỉ lệ kích thước và sự phụ thuộc của tần số riêng vào kích thước hình học L: "
        "k tỉ lệ với L, m tỉ lệ với <i>L</i><sup>3</sup> suy ra tần số dao động ω tỉ lệ nghịch với kích thước <i>L</i><sup>−1</sup>; "
        "vật thể 100 nm đạt tần số dao động siêu cao 15 GHz tương ứng bước sóng sóng điện từ 2 cm (Slide 18 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ định luật tỉ lệ tần số", "H3")
    add_p(
        "Độ cứng đàn hồi <i>k</i> của một thanh dầm chịu biến dạng uốn tỉ lệ tuyến tính với kích thước chiều dài <i>L</i>: <i>k</i> ∝ <i>L</i>. "
        "Trong khi đó, khối lượng quán tính <i>m</i> của cấu trúc đồng nhất tỉ lệ thuận với thể tích ba chiều: <i>m</i> = ρ · <i>V</i> ∝ <i>L</i><sup>3</sup>. "
        "Tần số góc dao động riêng <i>\u03c9</i><sub>0</sub> do đó tỉ lệ nghịch bậc nhất với kích thước hình học <i>L</i>: <i>\u03c9</i><sub>0</sub> ∝ <i>L</i><sup>−1</sup>."
    )
    add_spacer(6)

    eq_col_4 = r"k \propto L, \quad m \propto L^3 \quad \Longrightarrow \quad \omega_0 = \sqrt{\frac{k}{m}} \propto \sqrt{\frac{L}{L^3}} = L^{-1} \quad \Longrightarrow \quad f \propto \frac{1}{L}"
    nom_rows_4 = [
        ("Kích thước hình học đặc trưng của hệ", "<i>L</i>", "m hoặc nm", "Chiều dài hoặc kích thước chuẩn của thanh dầm, dây nano hoặc cấu trúc cơ học"),
        ("Độ cứng cơ học chống biến dạng đàn hồi", "<i>k</i>", "N·m<sup>−1</sup>", "Tỉ lệ tuyến tính với kích thước hình học theo quy tắc: <i>k</i> tỉ lệ tuyến tính với <i>L</i>"),
        ("Khối lượng quán tính của cấu trúc", "<i>m</i>", "kg", "Tỉ lệ với thể tích ba chiều của vật thể theo định luật: <i>m</i> = ρ <i>V</i> ∝ <i>L</i><sup>3</sup>"),
        ("Tần số dao động cộng hưởng cơ học", "<i>f</i>", "Hz hoặc GHz", "Số chu kỳ dao động trên một giây, tỉ lệ nghịch bậc nhất với kích thước <i>L</i>"),
        ("Vận tốc truyền sóng âm đàn hồi", "<i>c<sub>s</sub></i>", "m·s<sup>−1</sup>", "Vận tốc pha của sóng âm dọc trong vật liệu thanh: vận tốc truyền sóng âm"),
    ]
    story.append(he.build_target_equation_block(eq_col_4, nom_rows_4, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất định luật tỉ lệ tần số", "H3")

    p4_step1 = (
        "Chứng minh quy luật tỉ lệ của độ cứng đàn hồi k theo kích thước hình học đặc trưng L:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét một thanh dầm đàn hồi đồng nhất có môđun Young <i>E</i>, chiều dài <i>L</i>, chiều rộng <i>w</i> và độ dày <i>t</i>. "
        "Giả sử khi thu nhỏ đồng dạng hình học, tất cả các kích thước đều co lại theo cùng một tỉ lệ: <i>w</i> ∝ <i>L</i>, <i>t</i> ∝ <i>L</i>. "
        "Độ cứng uốn của dầm ngàm được tính từ công thức Euler-Bernoulli: <i>k</i> = <i>E</i> <i>w</i> <i>t</i><sup>3</sup> · (4<i>L</i><sup>3</sup>)<sup>−1</sup>:"
    )
    story.append(he.build_intermediate_equation(p4_step1, r"k = \frac{E \cdot w \cdot t^3}{4 L^3} \propto \frac{E \cdot L \cdot L^3}{L^3} = E \cdot L \propto L", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p4_step2 = (
        "Chứng minh quy luật tỉ lệ của khối lượng quán tính m theo thể tích ba chiều:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khối lượng quán tính của thanh dầm là tích của khối lượng riêng vật liệu ρ với thể tích hình học <i>V</i> = <i>L</i> · <i>w</i> · <i>t</i>. "
        "Do <i>w</i> ∝ <i>L</i> và <i>t</i> ∝ <i>L</i>, thể tích tỉ lệ với lũy thừa bậc ba của kích thước chiều dài:"
    )
    story.append(he.build_intermediate_equation(p4_step2, r"m = \rho \cdot V = \rho \cdot L \cdot w \cdot t \propto \rho \cdot L^3 \propto L^3", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p4_step3 = (
        "Xác lập định luật tỉ lệ nghịch bậc nhất của tần số dao động theo kích thước:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Thay thế tỉ lệ của độ cứng <i>k</i> ∝ <i>L</i> và khối lượng <i>m</i> ∝ <i>L</i><sup>3</sup> vào công thức tần số góc riêng của hệ dao động tử điều hòa. Rút gọn biểu thức dưới căn bậc hai:"
    )
    story.append(he.build_intermediate_equation(p4_step3, r"\omega_0 = \sqrt{\frac{k}{m}} \propto \sqrt{\frac{L}{L^3}} = \sqrt{\frac{1}{L^2}} = L^{-1} \quad \Longrightarrow \quad \omega_0 \propto \frac{1}{L}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p4_step4 = (
        "Định lượng hóa tần số dao động siêu cao tại thang đo 100 nm và bước sóng điện từ tương ứng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Áp dụng định luật tỉ lệ với mốc chuẩn thực nghiệm: Một vật thể dầm nano silicon kích thước <i>L</i> = 100 nm = 10<sup>−7</sup> m "
        "sẽ sở hữu tần số dao động riêng đạt ngưỡng <i>f</i> ≈ 15 GHz = 1.5 × 10<sup>10</sup> Hz. "
        "Bước sóng bức xạ điện từ tương ứng trong chân không được tính bằng:"
    )
    story.append(he.build_intermediate_equation(p4_step4, r"\lambda = \frac{c}{f} = \frac{3 \cdot 10^8 \text{ [m/s]}}{15 \cdot 10^9 \text{ [Hz]}} = 0.02 \text{ [m]} = 2 \text{ [cm]}", styles=styles, is_expanded_from_slide=True))
    add_spacer(8)

    # Đồ thị mô phỏng 3
    story.append(he.embed_figure_with_caption(
        fig_sim_03,
        "Hình 3.11: Mô phỏng giải tích định luật tỉ lệ tần số dao động riêng theo kích thước <i>f</i>(<i>L</i>) ∝ <i>L</i><sup>−1</sup>: "
        "Đặc tuyến tần số trên thang log-log quét qua 8 bậc độ lớn kích thước từ vĩ mô (1 m, 1.5 Hz), vi cơ điện tử MEMS (100 um, 15 MHz) "
        "đến nano cơ điện tử NEMS (100 nm, 15 GHz). Các vùng công nghệ được phân biệt rõ ràng bằng màu sắc chuẩn mực.",
        kind="sim",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận và thực chiến cảm biến cân phân tử NEMS", "H3")
    add_p(
        "Ý nghĩa thực tiễn mang tính cách mạng của định luật tỉ lệ <i>f</i> ∝ <i>L</i><sup>−1</sup> trong công nghệ cảm biến Nano Cơ Điện Tử (NEMS):<br/>"
        "• Độ nhạy khối lượng bùng nổ (Zeptogram Mass Sensing): "
        "Khi một phân tử lạ có khối lượng cực nhỏ Δ<i>m</i> bám vào bề mặt dầm NEMS đang dao động ở tần số <i>f</i><sub>0</sub>, "
        "tần số cộng hưởng của dầm sẽ bị dịch chuyển giảm một lượng: Δ<i>f</i> / <i>f</i><sub>0</sub> ≈ − (2<i>m</i>)<sup>−1</sup> Δ<i>m</i>. "
        "Vì khối lượng <i>m</i> của dầm nano tỉ lệ với <i>L</i><sup>3</sup> cực nhỏ (chỉ cỡ 10<sup>−18</sup>–10<sup>−15</sup> kg), "
        "đồng thời tần số <i>f</i><sub>0</sub> lại cực lớn (hàng GHz), độ dịch tần Δ<i>f</i> trên một đơn vị khối lượng bám dính đạt giá trị khổng lồ. "
        "Điều này cho phép các thiết bị NEMS cân được khối lượng của từng phân tử protein đơn lẻ, từng chuỗi DNA, thậm chí từng nguyên tử khí trơ (độ phân giải đạt ngưỡng 1 yg = 10<sup>−24</sup> g = 1 dalton).<br/>"
        "• Ứng dụng lọc tần số sóng vô tuyến trong vi mạch 5G/6G: "
        "Thay vì sử dụng các cuộn cảm và tụ điện cồng kềnh, các bộ cộng hưởng NEMS kích thước dưới 100 nm được tích hợp trực tiếp lên chip silicon "
        "để tạo ra các bộ lọc băng thông siêu hẹp hoạt động ở tần số sóng milimet (10–30 GHz) với mức tiêu thụ năng lượng chỉ bằng một phần nghìn so với mạch điện tử truyền thống."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.1.5: HỆ BÀI TOÁN ĐỊNH LƯỢNG KINH ĐIỂN & THỬ THÁCH CER
    # =========================================================================
    add_p("Luận điểm 3.1.5: Hệ bài toán định lượng kinh điển: Dao động phân tử hai nguyên tử CO, hiệu ứng đồng vị và định luật cắt ngắn liên kết", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm và mô hình dao động phân tử hai nguyên tử", "H3")
    add_p(
        "Phân tử hai nguyên tử là hệ vi mô đơn giản nhất mô phỏng trực tiếp dao động tử điều hòa tuyến tính trong tự nhiên. "
        "Khi hai nguyên tử có khối lượng <i>m</i><sub>1</sub> và <i>m</i><sub>2</sub> liên kết với nhau bằng một liên kết hóa học có độ cứng lò xo <i>K</i>, "
        "chuyển động tương đối của chúng dọc theo trục xuyên tâm tương đương với chuyển động của một chất điểm duy nhất "
        "có khối lượng bằng khối lượng rút gọn khối lượng rút gọn μ của hệ hai nguyên tử gắn vào điểm cố định. "
        "Dưới đây là lời giải giải tích chi tiết toàn văn cho 3 bài toán định lượng kinh điển từ Slide 19, 20 và 21 của bài giảng HUST.",
        ocr_idx=19
    )
    add_spacer(6)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ dao động phân tử hai nguyên tử", "H3")
    add_p(
        "Hệ thức cột trụ tính toán khối lượng rút gọn μ, tần số dao động riêng <i>f</i>, bước sóng photon hồng ngoại hấp thụ λ, "
        "và định luật biến thiên độ cứng đàn hồi khi cắt ngắn chiều dài lò xo."
    )
    add_spacer(6)

    eq_col_5 = r"\mu = \frac{m_1 m_2}{m_1 + m_2}, \quad f = \frac{1}{2\pi} \sqrt{\frac{K}{\mu}}, \quad \lambda = \frac{c}{f}, \quad K' = 2K \quad \left( \text{khi } L' = \frac{L}{2} \right)"
    nom_rows_5 = [
        ("Khối lượng rút gọn của phân tử", "μ", "kg hoặc u", "Khối lượng quán tính hiệu dụng của hệ hai nguyên tử chuyển động quanh khối tâm chung"),
        ("Hệ số đàn hồi của liên kết hóa học", "<i>K</i>", "N·m<sup>−1</sup>", "Độ cứng lò xo dọc trục liên kết phân tử (với CO: <i>K</i> = 1860 N/m)"),
        ("Tần số dao động tự nhiên của phân tử", "<i>f</i>", "Hz hoặc THz", "Tần số hấp thụ quang học đặc trưng trong vùng phổ hồng ngoại"),
        ("Bước sóng bức xạ điện từ cộng hưởng", "λ", "m hoặc μm", "Bước sóng photon kích thích quá trình chuyển mức dao động phân tử"),
        ("Độ cứng lò xo sau khi cắt ngắn", "<i>K'</i>", "N·m<sup>−1</sup>", "Độ cứng tăng gấp đôi khi chiều dài dây hoặc lò xo giảm một nửa: <i>K'</i> = 2<i>K</i>"),
    ]
    story.append(he.build_target_equation_block(eq_col_5, nom_rows_5, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Dẫn xuất toàn văn giải tích 3 bài toán định lượng", "H3")

    p5_step1 = (
        "<b>Bài toán 1 (Slide 19):</b> Phân tử CO giả sử có liên kết đàn hồi dao động tuyến tính dạng lò xo theo trục xuyên tâm các nguyên tử. "
        "Cho biết hệ số đàn hồi <i>K</i> = 1860 N/m, nguyên tử lượng của Carbon và Oxy lần lượt là 12 u và 16 u (với 1 u = 1.66054 × 10<sup>−27</sup> kg). "
        "Xác định tần số dao động tuyến tính <i>f</i> và bước sóng bức xạ điện từ λ tương ứng?<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Bước 1: Tính khối lượng rút gọn μ của phân tử Carbon Monoxide (CO):"
    )
    story.append(he.build_intermediate_equation(p5_step1, r"\mu = \frac{m_C \cdot m_O}{m_C + m_O} = \frac{12 \cdot 16}{12 + 16} \text{ [u]} = \frac{192}{28} \text{ [u]} \approx 6.85714 \text{ [u]} = 6.85714 \cdot 1.66054 \cdot 10^{-27} \approx 1.13866 \cdot 10^{-26} \text{ [kg]}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p5_step2 = (
        "Tiếp tục Bài toán 1: Tính tần số góc dao động và tần số dao động tự nhiên:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Bước 2: Thay độ cứng <i>K</i> = 1860 N/m và khối lượng rút gọn μ vào công thức tần số góc: tần số góc <i>\u03c9</i>. "
        "Sau đó tính tần số dao động tần số dao động <i>f</i>:"
    )
    story.append(he.build_intermediate_equation(p5_step2, r"\omega = \sqrt{\frac{1860}{1.13866 \cdot 10^{-26}}} \approx 4.04166 \cdot 10^{14} \text{ [rad/s]} \quad \Longrightarrow \quad f = \frac{\omega}{2\pi} \approx 6.4325 \cdot 10^{13} \text{ [Hz]} = 64.325 \text{ [THz]}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p5_step3 = (
        "Tiếp tục Bài toán 1: Tính bước sóng quang học và số sóng hồng ngoại đặc trưng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Bước 3: Bước sóng bức xạ λ và số sóng ν tương ứng của photon kích thích:"
    )
    story.append(he.build_intermediate_equation(p5_step3, r"\lambda = \frac{c}{f} = \frac{2.99792 \cdot 10^8 \text{ [m/s]}}{6.4325 \cdot 10^{13} \text{ [Hz]}} \approx 4.6606 \cdot 10^{-6} \text{ [m]} = 4.66 \text{ [\mu m]} \quad \Longrightarrow \quad \tilde{\nu} = \frac{1}{\lambda} \approx 2145.6 \text{ [cm}^{-1}\text{]}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p5_step4 = (
        "<b>Bài toán 2 (Slide 20):</b> Dựa trên bài 1, nếu thay thế nguyên tử C (12 u) bằng nguyên tử O (16 u) thì tần số dao động thay đổi thế nào? "
        "Giả sử hệ đồng nhất có khối lượng tỉ lệ với kích thước <i>L</i><sup>3</sup>, khi khối lượng tăng như trên, tần số biến đổi ra sao?<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi thay Carbon bằng Oxy, phân tử trở thành O<sub>2</sub> giả định có cùng độ cứng liên kết <i>K</i> = 1860 N/m. "
        "Khối lượng rút gọn mới là: khối lượng rút gọn mới là 8 u. "
        "Tỉ số tần số dao động mới so với tần số ban đầu tỉ lệ nghịch với căn bậc hai của khối lượng rút gọn:"
    )
    story.append(he.build_intermediate_equation(p5_step4, r"\frac{f'}{f} = \sqrt{\frac{\mu}{\mu'}} = \sqrt{\frac{6.85714}{8.00000}} = \sqrt{0.85714} \approx 0.92582 \quad \Longrightarrow \quad \Delta f \approx -7.42\%", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p5_step5 = (
        "<b>Bài toán 3 (Slide 21):</b> Dựa trên bài 1, nếu cùng tần số dao động nhưng chiều dài lò xo giảm đi một nửa khi chiều dài giảm đi một nửa, "
        "chứng minh rằng khi đó hệ số đàn hồi <i>K'</i> = 2<i>K</i>?<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Theo định luật Hooke dạng ứng suất đàn hồi, lực tác dụng <i>F</i> liên hệ với độ biến dạng Δ<i>L</i> qua môđun Young <i>E</i> và tiết diện ngang <i>A</i>: "
        "lực đàn hồi tỉ lệ với độ dời qua độ cứng đàn hồi <i>K</i> tỉ lệ nghịch với chiều dài <i>L</i>. "
        "Khi chiều dài giảm một nửa <i>L'</i> = 0.5 <i>L</i> trong khi giữ nguyên vật liệu và tiết diện:"
    )
    story.append(he.build_intermediate_equation(p5_step5, r"K' = \frac{E \cdot A}{L'} = \frac{E \cdot A}{L/2} = 2 \cdot \frac{E \cdot A}{L} = 2 K \quad \text{(Điều phải chứng minh)}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p5_step6 = (
        "Hệ quả bài toán 3: Điều kiện để giữ nguyên tần số dao động khi chiều dài giảm một nửa:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Để tần số dao động không đổi (<i>\u03c9'</i> = <i>\u03c9</i>), tỉ số độ cứng trên khối lượng phải được bảo toàn: tỉ số độ cứng trên khối lượng được bảo toàn. "
        "Thay <i>K'</i> = 2<i>K</i> vào hệ thức trên:"
    )
    story.append(he.build_intermediate_equation(p5_step6, r"\frac{2K}{m'} = \frac{K}{m} \quad \Longleftrightarrow \quad m' = 2m", styles=styles, is_expanded_from_slide=True))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát thực chiến quang phổ FTIR và hiệu ứng dịch chuyển đồng vị", "H3")
    add_p(
        "Kết quả tính toán giải tích ở Bài toán 1 hoàn toàn trùng khớp với dữ liệu thực nghiệm quang phổ học hồng ngoại (FTIR): "
        "Vạch hấp thụ dao động cơ bản của khí Carbon Monoxide (CO) nằm ở số sóng thực nghiệm 2143 cm<sup>−1</sup> (sai số lý thuyết dưới 0.12%). "
        "Số sóng này nằm trong dải hồng ngoại giữa (Mid-IR, 4.66 μm), đóng vai trò như một mỏ neo quang học để phát hiện rò rỉ khí độc CO trong môi trường công nghiệp.<br/>"
        "Trong khi đó, hiệu ứng đồng vị ở Bài toán 2 là cơ sở vật lý của phương pháp ghi nhãn đồng vị (Isotope Labeling): "
        "Khi tổng hợp phân tử sử dụng đồng vị nặng <sup>13</sup>C thay thế cho <sup>12</sup>C, tần số hấp thụ giảm dịch chuyển về 2096 cm<sup>−1</sup>, "
        "cho phép các nhà khoa học theo dõi chi tiết từng phản ứng xúc tác trung gian trên bề mặt vật liệu nano mà không làm thay đổi tính chất hóa học của phân tử."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI 5: THỬ THÁCH CHẨN ĐOÁN CER (CLAIM - EVIDENCE - REASONING)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai (CER)", "H2")
    add_spacer(6)

    add_p(
        "Khối Thử thách Chẩn đoán CER (Claim — Evidence — Reasoning) là trạm kiểm định năng lực tư duy nguyên lý đầu độc lập của Bùi Trung Dũng. "
        "Học viên bắt buộc tự giải quyết bài toán chẩn đoán kỹ thuật dưới đây, không có đáp án giải hộ trong tài liệu, "
        "và nộp phần trả lời trực tiếp trên Chat để Giảng viên phản biện và chấm điểm."
    )
    add_spacer(8)

    cer_box_content = [
        Paragraph(he.wrap_math_glyphs("<b>BÀI TOÁN THỬ THÁCH CHẨN ĐOÁN CER 3.1:</b>"), styles["H3"]),
        Spacer(1, 4),
        Paragraph(he.wrap_math_glyphs(
            "Trong một phòng thí nghiệm đo lường kích thước nano tại HUST, một nhóm nghiên cứu sử dụng cảm biến dầm nano silicon NEMS "
            "(kích thước <i>L</i> = 200 nm, <i>w</i> = 30 nm, <i>t</i> = 20 nm) hoạt động ở chế độ cộng hưởng uốn tần số cao trong buồng chân không "
            "để đo khối lượng của các hạt virus sinh học bám dính. "
            "Trước khi bơm virus vào buồng đo, hệ thống ghi nhận tần số cộng hưởng ban đầu <i>f</i><sub>0</sub> = 8.500 GHz ở nhiệt độ 300 K. "
            "Khi nhiệt độ buồng chân không bị trôi nhiệt tăng từ 300 K lên 360 K do bức xạ nhiệt từ nguồn đèn laser hội tụ, "
            "tần số cộng hưởng của dầm NEMS bị dịch chuyển giảm một lượng Δ<i>f</i> = −42.5 MHz ngay cả khi buồng đo hoàn toàn sạch (chưa có virus bám vào).<br/><br/>"
            "<b>Yêu cầu học viên hoàn thành cấu trúc lập luận 3 phần:</b><br/>"
            "• <b>Luận điểm (Claim):</b> Xác định chính xác nguyên nhân vật lý cốt lõi dẫn đến sự suy giảm tần số cộng hưởng của dầm NEMS khi nhiệt độ tăng. "
            "Sự suy giảm này xuất phát chủ yếu từ sự giãn nở nhiệt làm tăng kích thước hình học, hay do sự biến đổi tính chất đàn hồi vi mô của liên kết mạng tinh thể Silicon?<br/>"
            "• <b>Bằng chứng (Evidence):</b> Trích xuất và đối chuẩn các thông số định lượng vật lý của Silicon ở 300 K: "
            "hệ số giãn nở nhiệt tuyến tính α<sub><i>L</i></sub> = đạo hàm dãn nở ≈ 2.6 × 10<sup>−6</sup> K<sup>−1</sup> "
            "và hệ số nhiệt của môđun đàn hồi Young (Temperature Coefficient of Elastic Modulus — TCEM) hệ số nhiệt của môđun đàn hồi α<sub><i>E</i></sub> ≈ −6.4 × 10<sup>−5</sup> K<sup>−1</sup>. "
            "Tính toán tỉ số đóng góp tương đối giữa hai hiệu ứng vào độ dịch tần độ dịch tần tỉ đối.<br/>"
            "• <b>Lập luận (Reasoning):</b> Dẫn xuất biểu thức giải tích vi phân toàn phần của tần số dao động <i>f</i> theo nhiệt độ <i>T</i>: "
            "đạo hàm toàn phần của tần số theo nhiệt độ qua các số hạng liên quan đến <i>E</i> và <i>L</i> "
            "Áp dụng nguyên lý đầu và thế năng Lennard-Jones giải thích tại sao dao động nhiệt phi điều hòa lại làm mềm độ cứng liên kết mạng tinh thể (Thermal softening), "
            "và đề xuất giải pháp kỹ thuật bù nhiệt (Thermal compensation) để triệt tiêu sai số trôi nhiệt trong phép đo khối lượng virus NEMS."
        ), styles["Body"])
    ]
    t_cer = he.Table([[cer_box_content]], colWidths=[he.PRINTABLE_WIDTH])
    t_cer.setStyle(he.TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#FFF8E7")),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor("#D95319")),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(t_cer)
    add_spacer(14)

    # Lời kết mỏ neo điều hướng chuyển tiếp sang Mục 3.2
    add_p("Khâu nối biên độ và Tiền đề chuyển tiếp sang Mục 3.2", "H3")
    add_p(
        "Mục 3.1 đã giải quyết trọn vẹn nền tảng cơ học thang nano và các định luật tỉ lệ tần số dao động từ nguyên lý đầu. "
        "Tuy nhiên, khi một cấu trúc nano dao động hoặc di chuyển trong môi trường chất lưu, hai câu hỏi nhiệt động học và thủy động lực học lớn nảy sinh: "
        "(1) Tốc độ tản nhiệt và hằng số thời gian nhiệt biến đổi thế nào khi diện tích bề mặt tiếp xúc bùng nổ theo tỉ lệ <i>L</i><sup>−1</sup>? "
        "(2) Lực cản nhớt Stokes ảnh hưởng ra sao đến tốc độ lắng đọng trọng trường của hạt nano, và tại sao cơ học Newton hoàn toàn bất lực trước chuyển động nhiệt hỗn loạn Brown? "
        "Tất cả những quy luật nhiệt - động học vi mô then chốt này sẽ được khai mở toàn văn tại <b>Mục 3.2: Nhiệt động học vi mô, động học chất lưu Stokes và chuyển động khuếch tán Brown</b>."
    )

    # Biên dịch PDF bằng BookmarkDocTemplate tại thư mục cách ly %TEMP%
    print(f"Building PDF monograph in isolated temp directory: {temp_pdf_path}...")
    doc.build(story)

    # Thuật toán 9 (%TEMP% Isolation Policy): Thay thế nguyên tử (Atomic Replace / Cross-Drive Safe) vào Google Drive
    try:
        os.replace(temp_pdf_path, TARGET_PDF_PATH)
    except OSError:
        shutil.copy2(temp_pdf_path, TARGET_PDF_PATH)
        try:
            os.remove(temp_pdf_path)
        except Exception:
            pass
    print(f"Successfully published monograph PDF to Drive: {TARGET_PDF_PATH}!")


if __name__ == "__main__":
    build_monograph_muc_3_1()

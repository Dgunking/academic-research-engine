# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Course: Co so vat ly va cong nghe nano (PH3470 - HUST)
Chapter 3: Dac trung cua vat lieu khi kich thuoc giam (What happens at the nanoscale?)
Section 3.4: Dac tinh dao dong mang tinh the (Phonon) va hien tuong sieu thuan tu o thang nano
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

PDF_FILENAME = "Chuyen_Khao_Nano_Muc_3.4.pdf"
TARGET_PDF_PATH = os.path.join(PDF_DIR, PDF_FILENAME)


def build_monograph_muc_3_4():
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

    # Figure paths - 3 original figures
    fig_goc_01 = os.path.join(IMG_DIR, "[Goc]_Muc_3.4_Hinh_01_Pho_Tan_Xa_Raman_Giam_Giu_Phonon.png")
    fig_goc_02 = os.path.join(IMG_DIR, "[Goc]_Muc_3.4_Hinh_02_Dich_Dinh_Raman_Hat_Nano_CeO2.png")
    fig_goc_03 = os.path.join(IMG_DIR, "[Goc]_Muc_3.4_Hinh_03_Chuyen_Pha_Sat_Tu_Thuan_Tu_PbTiO3.png")

    # Figure paths - 3 simulation plots
    fig_sim_01 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.4_Pho_Raman_Theo_Kich_Thuoc_Hat_Model_Fauchet.png")
    fig_sim_02 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.4_Duong_Cong_Tu_Tre_Va_Chuyen_Pha_Sieu_Thuan_Tu.png")
    fig_sim_03 = os.path.join(IMG_DIR, "[Mo_Phong]_Muc_3.4_Thoi_Gian_Hoi_Phuc_Neel_Va_Gioi_Han_Sieu_Thuan_Tu.png")

    # =========================================================================
    # H1 TIÊU ĐỀ PHÂN MỤC VÀ METADATA ĐÀO TẠO BÁCH KHOA
    # =========================================================================
    add_p("Chương 3: Đặc trưng của vật liệu khi kích thước giảm", "H1")
    add_p("Mục 3.4: Đặc tính dao động mạng tinh thể (Phonon) và hiện tượng siêu thuận từ ở thang nano", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Edward L. Wolf — Nanophysics and Nanotechnology, Chương 3; Slide bài giảng HUST 35–37)</i>", "Caption")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Cơ sở vật lý và công nghệ nano (PH3470)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Viện Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Bài 3 (Slide 35–37); Wolf Nanotechnology Ch. 3"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu về động học dao động mạng tinh thể (Phonon) và các đặc tính từ tính vi mô ở quy mô nanomet "
        "(PH3470 — HUST; đối chiếu Edward L. Wolf, Nanophysics and Nanotechnology, Chapter 3). "
        "Khảo sát toàn diện sự biến đổi sâu sắc của phổ phonon và hành vi từ tính khi kích thước hạt thu nhỏ dưới độ dài kết hợp mạng: "
        "phân tích sự phá vỡ quy tắc chọn lọc xung lượng quang học kinh điển bắt nguồn từ nguyên lý bất định Heisenberg, "
        "thiết lập tích phân phân bố tán xạ Raman toàn phần theo mô hình giam giữ phonon Richter-Campbell-Fauchet, "
        "giải thích cơ chế dịch chuyển đỏ và mở rộng bất đối xứng của đỉnh tán xạ Raman thực chứng trên hạt nano Ceri oxit (CeO<sub>2</sub>) và Silicon, "
        "khám phá cấu trúc từ tính hạt đơn domain và sự hình thành hàng rào thế năng dị hướng từ <i>KV</i>, "
        "chứng minh sự chuyển pha sắt từ sang siêu thuận từ (Superparamagnetism) với sự biến mất hoàn toàn của lực kháng từ và từ trễ, "
        "dẫn xuất định luật thời gian hồi phục spin Néel-Arrhenius, xác định nhiệt độ đóng băng từ tính <i>T<sub>B</sub></i> "
        "và giới hạn siêu thuận từ quyết định mật độ lưu trữ dữ liệu tối đa trong các thiết bị ổ đĩa từ tính hiện đại."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 3.4
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Slide HUST &amp; Wolf)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.4.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Dao động mạng tinh thể &amp; Mô hình giam giữ phonon Richter-Fauchet"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>I</i>(ω) ∝ ∫ |<i>C</i>(0, <b>q</b>)|<sup>2</sup> · {[ω − ω(<b>q</b>)]<sup>2</sup> + (Γ<sub>0</sub> · 2<sup>−1</sup>)<sup>2</sup>}<sup>−1</sup> <i>d</i><sup>3</sup><b>q</b>; dịch đỏ &amp; mở rộng đỉnh"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 35; Mô phỏng giải tích 3.4.1"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.4.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Thực nghiệm tán xạ Raman trên CeO<sub>2</sub> &amp; Ứng dụng đo kích thước"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Δω = ω<sub>nano</sub> − ω<sub>bulk</sub> = −<i>A</i> · (<i>a</i> · <i>L</i><sup>−1</sup>)<sup>γ</sup>; phổ Raman không phá hủy xác định cỡ hạt nano"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 36 (Dịch đỉnh CeO<sub>2</sub>)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.4.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hạt từ đơn domain &amp; Chuyển pha siêu thuận từ (Superparamagnetism)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Δ<i>E</i> = <i>K V</i>; khi <i>K V</i> ≤ 25 <i>k<sub>B</sub> T</i> thì lực kháng từ <i>H<sub>c</sub></i> = 0, từ dư <i>M<sub>r</sub></i> = 0; hàm Langevin"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Ảnh gốc: Slide 37; Mô phỏng giải tích 3.4.2"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 3.4.4</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Thời gian hồi phục Néel &amp; Giới hạn siêu thuận từ trong lưu trữ dữ liệu"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("τ<sub><i>N</i></sub> = τ<sub>0</sub> exp[<i>K V</i> · (<i>k<sub>B</sub> T</i>)<sup>−1</sup>]; nhiệt độ đóng băng <i>T<sub>B</sub></i>, đường kính tới hạn <i>D<sub>p</sub></i> (HAMR, PMR)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng giải tích 3.4.3 (Co, Fe<sub>3</sub>O<sub>4</sub> at 300 K)"), styles["TableCellCenter"]),
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
    # MPT 3.4.1: DAO ĐỘNG MẠNG TINH THỂ & MÔ HÌNH GIAM GIỮ PHONON
    # =========================================================================
    add_p("Luận điểm 3.4.1: Dao động Mạng Tinh thể (Phonon) và Mô hình Giam giữ Phonon Richter-Fauchet", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, quy tắc chọn lọc xung lượng và nghịch lý phonon giam giữ", "H3")
    add_p(
        "Trong vật lý chất rắn vĩ mô, dao động nhiệt của các ion tại nút mạng tinh thể được lượng tử hóa dưới dạng các chuẩn hạt phonon. "
        "Khi ánh sáng đơn sắc (laser) chiếu vào một tinh thể vô hạn lý tưởng, photon kích thích tương tác với phonon quang học qua quá trình tán xạ Raman không đàn hồi. "
        "Do bước sóng của ánh sáng khả kiến (λ ≈ 500 nm) lớn hơn hàng trăm lần so với hằng số mạng tinh thể (<i>a</i> ≈ 0.5 nm), "
        "vector sóng của photon <i>k</i><sub>photon</sub> = 2π · λ<sup>−1</sup> ≈ 10<sup>5</sup> cm<sup>−1</sup> là cực kỳ nhỏ bé so với kích thước vùng Brillouin (π · <i>a</i><sup>−1</sup> ≈ 10<sup>8</sup> cm<sup>−1</sup>). "
        "Theo định luật bảo toàn xung lượng chuẩn, quá trình tán xạ Raman bậc một trong vật liệu khối bị ràng buộc nghiêm ngặt bởi quy tắc chọn lọc: "
        "chỉ các phonon quang học nằm tại tâm vùng Brillouin với vector sóng <b>q</b> ≈ 0 mới có thể tham gia tán xạ, "
        "tạo nên một đỉnh phổ Raman cực kỳ sắc nhọn với độ rộng vạch hẹp (Γ<sub>0</sub> ≈ 3–4 cm<sup>−1</sup>) tại tần số dao động riêng ω<sub>0</sub>.",
        ocr_idx=1
    )
    add_spacer(6)

    add_p(
        "Tuy nhiên, khi kích thước tinh thể bị thu nhỏ xuống thang nanomet (<i>L</i> ≤ 10 nm), "
        "sự tuần hoàn tịnh tiến vô hạn của mạng tinh thể bị phá vỡ đột ngột tại bề mặt hạt nano. "
        "Sóng mạng phonon không còn tự do lan truyền vô tận mà bị nhốt chặt bên trong ranh giới hình học của hạt nano. "
        "Theo nguyên lý bất định Heisenberg đối với sóng (Δ<i>x</i> · Δ<i>q</i> ≥ 2π), "
        "sự định xứ không gian với độ bất định vị trí nhỏ Δ<i>x</i> ≈ <i>L</i> dẫn đến độ bất định xung lượng lớn Δ<i>q</i> ≈ 2π · <i>L</i><sup>−1</sup>. "
        "Hậu quả trực tiếp là quy tắc chọn lọc xung lượng <b>q</b> ≈ 0 bị phá vỡ hoàn toàn: "
        "các phonon quang học có vector sóng khác không (<b>q</b> > 0) trên toàn bộ dải tán sắc bắt đầu tham gia đóng góp vào phổ tán xạ Raman.",
        ocr_idx=2
    )
    add_spacer(8)

    # Ảnh gốc Slide 35
    story.append(he.embed_figure_with_caption(
        fig_goc_01,
        "Hình 3.21: Đặc tính dao động mạng tinh thể của cấu trúc nano và mô hình phổ Raman Richter-Fauchet: "
        "Cường độ tán xạ Raman I(ω) là tích phân chập giữa đường cong tán sắc phonon ω(q) và hàm bao Fourier C(q) (Slide 35 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ mô hình Richter-Campbell-Fauchet", "H3")
    add_p(
        "Để mô hình hóa toán học sự giam giữ phonon trong hạt nano hình cầu đường kính <i>L</i>, "
        "H. Richter, Z. P. Wang, L. Ley (1981) và sau đó là I. H. Campbell, P. M. Fauchet (1986) "
        "đã nhân hàm sóng phonon phẳng exp(<i>i</i> <b>q</b> · <b>r</b>) với một hàm bao suy giảm Gaussian đối xứng cầu: "
        "<i>W</i>(<i>r</i>, <i>L</i>) = exp[−α <i>r</i><sup>2</sup> · (<i>L</i> · 2<sup>−1</sup>)<sup>−2</sup>] với α ≈ 2.0 (sao cho biên độ dao động suy giảm về 0 tại bề mặt hạt). "
        "Phân tích Fourier của hàm sóng bị giam giữ cho hệ số phân bố biên độ xung lượng |<i>C</i>(0, <b>q</b>)|<sup>2</sup> dạng Gaussian trong không gian <b>q</b>-space. "
        "Cường độ tán xạ Raman tổng cộng tại tần số ω là tích phân chập trên toàn bộ vùng Brillouin của các vạch phổ Lorentzian cục bộ."
    )
    add_spacer(6)

    eq_col_1 = r"I(\omega) \propto \int_{\text{BZ}} \frac{|C(0, \mathbf{q})|^2}{[\omega - \omega(\mathbf{q})]^2 + (\Gamma_0 / 2)^2} \, d^3\mathbf{q}, \quad |C(0, \mathbf{q})|^2 \approx \exp\left(-\frac{q^2 L^2}{16 \pi^2}\right)"
    nom_rows_1 = [
        ("Cường độ tán xạ phổ Raman tức thời", "<i>I</i>(ω)", "đ.v.t.đ", "Phổ phân bố cường độ quang học tán xạ theo số sóng ω"),
        ("Đường cong tán sắc phonon quang học khối", "ω(<b>q</b>)", "cm<sup>−1</sup>", "Tần số dao động phonon quang học phụ thuộc vector sóng <b>q</b> dọc trục đối xứng tinh thể"),
        ("Độ rộng bán phần vạch phổ vật liệu khối", "Γ<sub>0</sub>", "cm<sup>−1</sup>", "Độ rộng vạch Lorentzian nội tại do tán xạ suy giảm phonon tự nhiên (khoảng 3.6 cm<sup>−1</sup> ở 300 K)"),
        ("Hệ số phân bố Fourier giam giữ phonon", "|<i>C</i>(0, <b>q</b>)|<sup>2</sup>", "không thứ nguyên", "Trọng số đóng góp của các phonon có xung lượng <b>q</b> do hiệu ứng giam giữ hạt kích thước <i>L</i>"),
        ("Kích thước đặc trưng của hạt tinh thể nano", "<i>L</i>", "nm", "Đường kính của hạt nano tinh thể hoặc bề rộng của dây/màng nano"),
    ]
    story.append(he.build_target_equation_block(eq_col_1, nom_rows_1, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất hiện tượng dịch đỏ và mở rộng bất đối xứng", "H3")

    p_step1 = (
        "Xác định đường cong tán sắc phonon quang học quanh tâm vùng Brillouin:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Dải tán sắc của nhánh phonon quang học ngang (TO) hoặc dọc (LO) trong các bán dẫn đồng hóa trị như Silicon hoặc CeO<sub>2</sub> "
        "đạt cực đại tại tâm vùng <b>q</b> = 0 và uốn cong đi xuống khi vector sóng <i>q</i> tăng (độ cong âm): "
        "ω(<i>q</i>) ≈ ω<sub>0</sub> − Δω<sub>disp</sub> · (1 − cos(<i>q a</i> · 2<sup>−1</sup>)) ≈ ω<sub>0</sub> − β · <i>q</i><sup>2</sup> (với β > 0 là hệ số tán sắc âm):"
    )
    story.append(he.build_intermediate_equation(p_step1, r"\omega(q) \approx \omega_0 - \beta \cdot q^2 \quad (\beta > 0) \quad \Longrightarrow \quad \omega(q) < \omega_0 \quad \text{với mọi } q > 0", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step2 = (
        "Chứng minh nguồn gốc cơ học của hiện tượng dịch chuyển đỏ (Red Shift):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi kích thước hạt <i>L</i> giảm, độ rộng của hàm phân bố Fourier |<i>C</i>(0, <b>q</b>)|<sup>2</sup> trong không gian <i>q</i>-space tăng lên theo tỉ lệ <i>L</i><sup>−1</sup>. "
        "Các phonon có <i>q</i> > 0 bắt đầu đóng góp ồ ạt vào tích phân cường độ <i>I</i>(ω). "
        "Vì tất cả các phonon có <i>q</i> > 0 đều có tần số ω(<i>q</i>) nhỏ hơn tần số tâm ω<sub>0</sub>, "
        "trọng tâm của phổ tán xạ <i>I</i>(ω) bắt buộc phải dịch chuyển về phía tần số thấp hơn (dịch chuyển đỏ):"
    )
    story.append(he.build_intermediate_equation(p_step2, r"\Delta \omega = \omega_{\mathrm{peak}} - \omega_0 \approx -\beta \langle q^2 \rangle \propto -\beta \left(\frac{2\pi}{L}\right)^2 \propto -\frac{1}{L^2} < 0 \quad (\text{Dịch đỏ})", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step3 = (
        "Chứng minh cơ chế mở rộng bất đối xứng đuôi tần số thấp (Asymmetric Broadening):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Do các trạng thái phonon mới được kích hoạt chỉ nằm ở phía tần số thấp (ω < ω<sub>0</sub>), "
        "cường độ quang học bổ sung chỉ xuất hiện ở sườn bên trái của đỉnh phổ. "
        "Sườn bên phải (ω > ω<sub>0</sub>) không có trạng thái phonon nào đóng góp nên suy giảm dốc đứng như phổ Lorentzian khối. "
        "Sự bất đối xứng này tạo ra dạng đỉnh phổ nghiêng đặc trưng với đuôi kéo dài về phía số sóng nhỏ."
    )
    story.append(he.build_intermediate_equation(p_step3, r"\Gamma_{\mathrm{left}} > \Gamma_{\mathrm{right}} \quad \Longrightarrow \quad \text{Hệ số bất đối xứng: } \frac{\Gamma_{\mathrm{left}}}{\Gamma_{\mathrm{right}}} > 1.0", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Mô phỏng đối chuẩn & Đồ thị Fauchet
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích mô hình Fauchet", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích chuẩn hóa ZT-GVLE thể hiện sự tiến hóa ngoạn mục của phổ tán xạ Raman theo kích thước hạt nano: "
        "đối với hạt lớn <i>L</i> = 20 nm (tiệm cận khối), phổ có dạng Lorentzian đối xứng hoàn hảo với đỉnh nhọn tại đúng 520.5 cm<sup>−1</sup> "
        "và độ rộng vạch hẹp 3.6 cm<sup>−1</sup>. "
        "Khi kích thước hạt giảm xuống 6 nm, đỉnh dịch chuyển đỏ về 518.7 cm<sup>−1</sup>; "
        "xuống 4 nm dịch về 516.3 cm<sup>−1</sup>; và khi đạt kích thước cực nhỏ 2.5 nm, "
        "đỉnh dịch chuyển đỏ mạnh mẽ tới 8.5 cm<sup>−1</sup> (xuống 512.0 cm<sup>−1</sup>) "
        "đồng thời độ rộng vạch giãn rộng hơn 4 lần (lên tới 16.0 cm<sup>−1</sup>) với đuôi bất đối xứng kéo dài."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_01,
        "Hình 3.22: Mô phỏng giải tích phổ tán xạ Raman theo kích thước hạt nano (Mô hình Fauchet): "
        "Khi kích thước hạt L thu nhỏ từ 20 nm về 2.5 nm, đỉnh phổ dịch chuyển đỏ từ 520.5 cm⁻¹ xuống 512.0 cm⁻¹ "
        "đồng thời vạch phổ bị mở rộng bất đối xứng mạnh mẽ do sự giam giữ phonon.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    # Giai đoạn 5: Ứng dụng kỹ thuật
    add_p("Giai đoạn 5: Ứng dụng kỹ thuật và cầu nối sang thực nghiệm hạt nano CeO2", "H3")
    add_p(
        "Mô hình giam giữ phonon Richter-Fauchet biến quang phổ Raman thành một công cụ kiểm định quang học không phá hủy (non-destructive optical metrology) vô giá: "
        "chỉ bằng một phép đo quang phổ nhanh trong vài giây mà không cần phá hủy mẫu hay sử dụng kính hiển vi điện tử truyền qua TEM đắt tiền, "
        "các kỹ sư có thể giải mã trực tiếp kích thước trung bình và độ phân bố kích thước của các hạt nano trong bột tổng hợp. "
        "Để đối chuẩn mô hình lý thuyết này với dữ liệu đo thực tế, chúng ta khảo sát thực nghiệm tán xạ Raman trên hạt nano Ceri oxit (CeO<sub>2</sub>) trong phân mục khảo sát kế tiếp (MPT 3.4.2)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.4.2: THỰC NGHIỆM TÁN XẠ RAMAN TRÊN CeO2
    # =========================================================================
    add_p("Luận điểm 3.4.2: Thực nghiệm Tán xạ Raman trên Hạt Nano Ceri Oxit (CeO2) và Ứng dụng Đo Kích thước", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, vật liệu Ceri oxit và kết quả thực nghiệm trong slide bài giảng", "H3")
    add_p(
        "Ceri oxit (CeO<sub>2</sub>, ceria) là một vật liệu gốm oxit bán dẫn có cấu trúc tinh thể fluorite lập phương tâm diện (FCC), "
        "đóng vai trò trung tâm trong các chất xúc tác xử lý khí thải ô tô, cảm biến oxy và chất điện phân màng rắn cho pin nhiên liệu SOFC. "
        "Trong tinh thể khối CeO<sub>2</sub>, dao động mạng quang học đối xứng <i>F</i><sub>2<i>g</i></sub> sinh ra một đỉnh tán xạ Raman sắc nét tại số sóng ω<sub>0</sub> ≈ 464 cm<sup>−1</sup>, "
        "tương ứng với dao động co giãn đối xứng của 8 ion oxy xung quanh mỗi cation ceri Ce<sup>4+</sup>.",
        ocr_idx=3
    )
    add_spacer(6)

    # Ảnh gốc Slide 36
    story.append(he.embed_figure_with_caption(
        fig_goc_02,
        "Hình 3.23: Thực nghiệm tán xạ Raman trên hạt nano tinh thể CeO2 khi thay đổi kích thước hạt: "
        "Đồ thị thực nghiệm trong slide 36 bài giảng HUST chứng minh sự dịch chuyển đỏ và mở rộng vạch phổ khi kích thước hạt giảm từ thang micro xuống nanomet.",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ bán thực nghiệm xác định kích thước hạt", "H3")
    add_p(
        "Dữ liệu thực nghiệm trên slide 36 của bài giảng HUST cho thấy: khi kích thước hạt nano CeO<sub>2</sub> giảm từ vật liệu khối (hạt micro) "
        "xuống các hạt nano kích thước vài nanomet, đỉnh Raman <i>F</i><sub>2<i>g</i></sub> liên tục dịch chuyển về phía số sóng thấp hơn (từ 464 cm<sup>−1</sup> xuống 455–450 cm<sup>−1</sup>) "
        "và độ rộng vạch phổ tăng vọt từ 7 cm<sup>−1</sup> lên hơn 25 cm<sup>−1</sup>. "
        "Hiện tượng này được mô tả chính xác bởi hệ thức bán thực nghiệm lũy thừa liên hệ giữa độ dịch đỉnh và kích thước tinh thể."
    )
    add_spacer(6)

    eq_col_2 = r"\Delta \omega = \omega_{\mathrm{nano}} - \omega_{\mathrm{bulk}} = -A \left(\frac{a}{L}\right)^\gamma, \quad \Gamma_{\mathrm{nano}} - \Gamma_{\mathrm{bulk}} = B \left(\frac{a}{L}\right)^\delta"
    nom_rows_2 = [
        ("Độ dịch chuyển số sóng Raman", "Δω", "cm<sup>−1</sup>", "Khoảng cách dịch chuyển của đỉnh Raman hạt nano so với đỉnh vật liệu khối chuẩn"),
        ("Độ giãn rộng vạch phổ Raman", "ΔΓ", "cm<sup>−1</sup>", "Độ tăng thêm của độ rộng vạch phổ bán phần FWHM do hiệu ứng giam giữ"),
        ("Hằng số mạng tinh thể CeO2", "<i>a</i>", "nm", "Kích thước ô mạng cơ sở tinh thể fluorite CeO<sub>2</sub> (<i>a</i> = 0.5411 nm)"),
        ("Kích thước tinh thể trung bình của hạt", "<i>L</i>", "nm", "Đường kính tinh thể đo đạc từ phương pháp nhiễu xạ tia X (XRD) hoặc kính hiển vi TEM"),
        ("Các hệ số thực nghiệm hiệu chỉnh", "<i>A</i>, γ", "cm<sup>−1</sup>, không thứ nguyên", "Đối với CeO<sub>2</sub>: <i>A</i> ≈ 52.4 cm<sup>−1</sup>, γ ≈ 1.44; phản ánh độ cong dải tán sắc phonon"),
    ]
    story.append(he.build_target_equation_block(eq_col_2, nom_rows_2, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất ảnh hưởng kép của giam giữ phonon và sai hỏng mạng", "H3")

    p_step4 = (
        "Phân tích cơ chế kép chi phối phổ Raman của hạt nano CeO2:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khác với bán dẫn thuần túy như Silicon, sự dịch đỉnh Raman trong hạt nano CeO<sub>2</sub> chịu tác động đồng thời của hai cơ chế vật lý:<br/>"
        "(1) <b>Hiệu ứng giam giữ phonon (Phonon Confinement):</b> Do kích thước hạt <i>L</i> nhỏ hơn bước sóng phonon, gây dịch đỏ theo quy luật Δω<sub>conf</sub> ∝ −<i>L</i><sup>−γ</sup>;<br/>"
        "(2) <b>Hiệu ứng sai hỏng khuyết tật oxy (Oxygen Vacancies):</b> Khi kích thước hạt CeO<sub>2</sub> giảm xuống dưới 10 nm, tỉ số diện tích bề mặt trên thể tích tăng vọt. "
        "Để duy trì tính trung hòa điện khi các ion Ce<sup>4+</sup> bị khử một phần thành Ce<sup>3+</sup> (có bán kính ion lớn hơn: <i>r</i>(Ce<sup>3+</sup>) = 0.114 nm > <i>r</i>(Ce<sup>4+</sup>) = 0.097 nm), "
        "mạng tinh thể hình thành mật độ khổng lồ các lỗ khuyết oxy (oxygen vacancies) và làm dãn nở thể tích ô mạng (lattice expansion Δ<i>a</i> · <i>a</i><sup>−1</sup> > 0)."
    )
    story.append(he.build_intermediate_equation(p_step4, r"\Delta \omega_{\mathrm{total}} = \Delta \omega_{\mathrm{confinement}} + \Delta \omega_{\mathrm{strain}} = -A \left(\frac{a}{L}\right)^\gamma - 3 \gamma_{\mathrm{Gr\ddot{u}neisen}} \, \omega_0 \left(\frac{\Delta a}{a}\right)", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Biến thiên tiệm cận & Đo kích thước
    add_p("Giai đoạn 4: Đánh giá định lượng tương quan giữa độ dịch phổ và kích thước hạt", "H3")
    add_p(
        "Bằng cách kết hợp phép đo độ dịch đỉnh Δω và độ rộng vạch ΔΓ, các nhà nghiên cứu có thể xây dựng một đường chuẩn định lượng chính xác: "
        "với hạt nano CeO<sub>2</sub> có đường kính <i>L</i> = 8 nm, độ dịch đỉnh đo được là −2.5 cm<sup>−1</sup>; "
        "với hạt <i>L</i> = 5 nm, độ dịch là −5.2 cm<sup>−1</sup>; và khi hạt đạt <i>L</i> = 3 nm, độ dịch tăng vọt lên tới −12 cm<sup>−1</sup>. "
        "Mức độ dịch chuyển cực lớn này chứng minh tính siêu nhạy của dao động mạng đối với quy mô không gian nanomet."
    )
    add_spacer(6)

    # Giai đoạn 5: Ứng dụng kỹ thuật
    add_p("Giai đoạn 5: Ứng dụng công nghệ xúc tác nano và chuyển tiếp sang đặc tính từ tính", "H3")
    add_p(
        "Nghiên cứu dao động mạng phonon trên CeO<sub>2</sub> không chỉ dừng lại ở việc đo kích thước hạt, mà còn là chìa khóa để đánh giá hoạt tính xúc tác: "
        "độ dịch đỉnh Raman càng lớn chứng tỏ mật độ lỗ khuyết oxy trên bề mặt hạt càng cao, "
        "giúp tăng cường khả năng lưu trữ và giải phóng oxy linh hoạt trong các bộ chuyển đổi xúc tác khí thải xe hơi. "
        "Bên cạnh các hiệu ứng cơ học và quang học lượng tử, sự thu nhỏ kích thước hạt còn tạo ra bước chuyển pha ngoạn mục nhất trong vật lý chất rắn: "
        "sự sụp đổ của trật tự từ tính vĩ mô và sự xuất hiện của trạng thái Siêu thuận từ (Superparamagnetism)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.4.3: HẠT TỪ ĐƠN DOMAIN & CHUYỂN PHA SIÊU THUẬN TỪ
    # =========================================================================
    add_p("Luận điểm 3.4.3: Đặc tính Từ tính Thang Nano, Miền Từ Đơn Domain và Chuyển pha Siêu thuận từ", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, cấu trúc domain từ tính và sự hình thành hạt đơn domain", "H3")
    add_p(
        "Trong vật liệu sắt từ vĩ mô (chẳng hạn sắt, niken, coban hay quặng magnetit Fe<sub>3</sub>O<sub>4</sub>), "
        "các momen từ nguyên tử tương tác trao đổi mạnh mẽ với nhau, sắp xếp song song cùng chiều trong các miền tự hóa tự phát gọi là các domain từ (magnetic domains). "
        "Để cực tiểu hóa năng lượng tĩnh từ trường khử (demagnetizing field energy), một khối vật liệu lớn luôn tự phân chia thành nhiều domain "
        "ngăn cách nhau bởi các vách chuyển tiếp Bloch hoặc Néel có bề dày đặc trưng δ<sub><i>w</i></sub> ≈ 10–50 nm. "
        "Quá trình từ hóa vật liệu vĩ mô diễn ra chủ yếu qua sự dịch chuyển của các vách domain này, "
        "dẫn đến hiện tượng trễ từ kinh điển với lực kháng từ <i>H<sub>c</sub></i> lớn và độ từ dư <i>M<sub>r</sub></i> bền vững.",
        ocr_idx=4
    )
    add_spacer(6)

    add_p(
        "Tuy nhiên, việc hình thành một vách domain đòi hỏi một chi phí năng lượng bề mặt đáng kể (năng lượng trao đổi và năng lượng dị hướng từ). "
        "Khi kích thước hạt vật liệu thu nhỏ lại tới giá trị nhỏ hơn bề dày giới hạn của vách domain (<i>D</i> < <i>D</i><sub>crit</sub> ≈ 20–70 nm tùy vật liệu), "
        "sự phân chia domain trở nên bất lợi về mặt nhiệt động học. "
        "Hạt nano lúc này trở thành một hạt đơn domain duy nhất (single domain particle), "
        "nơi toàn bộ hàng ngàn đến hàng triệu momen từ nguyên tử bị khóa cứng song song với nhau, "
        "tạo thành một siêu momen từ khổng lồ (giant magnetic moment) có độ lớn μ<sub><i>p</i></sub> = <i>M<sub>s</sub></i> · <i>V</i> ≈ 10<sup>3</sup>–10<sup>5</sup> μ<sub><i>B</i></sub>."
    )
    add_spacer(8)

    # Ảnh gốc Slide 37
    story.append(he.embed_figure_with_caption(
        fig_goc_03,
        "Hình 3.24: Đặc tính từ và nhiệt độ chuyển pha sắt từ – thuận từ phụ thuộc kích thước hạt trong vật liệu gốm PbTiO3: "
        "Khi kích thước hạt gốm giảm, nhiệt độ chuyển pha Curie Tc suy giảm mạnh mẽ do hiệu ứng giam giữ và dao động nhiệt (Slide 37 bài giảng HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ năng lượng dị hướng từ và siêu thuận từ", "H3")
    add_p(
        "Hướng của siêu momen từ μ<sub><i>p</i></sub> bên trong hạt đơn domain bị ràng buộc bởi năng lượng dị hướng từ tinh thể (magnetocrystalline anisotropy energy). "
        "Đối với hạt có tính dị hướng đơn trục, thế năng dị hướng có dạng hai hố thế đối xứng ngăn cách bởi một hàng rào năng lượng có độ cao Δ<i>E</i> = <i>K V</i> "
        "(trong đó <i>K</i> là hằng số dị hướng từ và <i>V</i> là thể tích hạt). "
        "Khi thể tích hạt <i>V</i> thu nhỏ tới mức hàng rào năng lượng <i>K V</i> trở nên nhỏ tương đương hoặc nhỏ hơn năng lượng dao động nhiệt môi trường "
        "(<i>K V</i> ≤ 25 <i>k<sub>B</sub> T</i>), dao động nhiệt phonon sẽ kích hoạt sự lật đảo định hướng của siêu momen từ qua lại giữa hai chiều đối nghịch "
        "với tần số cực cao. "
        "Hạt chuyển từ trạng thái sắt từ bị khóa sang trạng thái Siêu thuận từ (Superparamagnetism)."
    )
    add_spacer(6)

    eq_col_3 = r"\Delta E = K V, \quad M(H) = M_s \left[\coth\left(\frac{\mu_p H}{k_B T}\right) - \frac{k_B T}{\mu_p H}\right], \quad H_c = 0, \quad M_r = 0"
    nom_rows_3 = [
        ("Hàng rào năng lượng dị hướng từ hạt nano", "Δ<i>E</i> = <i>K V</i>", "J hoặc eV", "Năng lượng tối thiểu cần thiết để lật đảo momen từ giữa hai hướng dễ từ hóa"),
        ("Hằng số dị hướng từ tinh thể hiệu dụng", "<i>K</i>", "J·m<sup>−3</sup>", "Mật độ năng lượng dị hướng nội tại (Fe<sub>3</sub>O<sub>4</sub> <i>K</i> ≈ 2.5 × 10<sup>4</sup> J·m<sup>−3</sup>, Cobalt <i>K</i> ≈ 4.5 × 10<sup>5</sup> J·m<sup>−3</sup>)"),
        ("Siêu momen từ toàn phần của hạt nano", "μ<sub><i>p</i></sub> = <i>M<sub>s</sub> V</i>", "A·m<sup>2</sup> hoặc J·T<sup>−1</sup>", "Tổng vector momen từ của toàn bộ nguyên tử trong hạt đơn domain (khoảng 10<sup>4</sup> Bohr magneton)"),
        ("Hàm từ hóa Langevin siêu thuận từ", "<i>L</i>(ξ) = coth(ξ) − ξ<sup>−1</sup>", "không thứ nguyên", "Đặc tuyến từ hóa phi tuyến trơn mượt không có hiện tượng trễ từ"),
        ("Lực kháng từ và độ từ dư siêu thuận từ", "<i>H<sub>c</sub></i>, <i>M<sub>r</sub></i>", "Oe, A·m<sup>−1</sup>", "Triệt tiêu hoàn toàn về 0 khi không có từ trường ngoài ở nhiệt độ phòng"),
    ]
    story.append(he.build_target_equation_block(eq_col_3, nom_rows_3, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất sự biến mất của từ trễ", "H3")

    p_step5 = (
        "Mô hình hóa sự lật đảo nhiệt động học của siêu momen từ:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét hạt đơn domain có thể tích <i>V</i> = π · 6<sup>−1</sup> <i>D</i><sup>3</sup>. "
        "Theo phân bố thống kê Boltzmann, xác suất để siêu momen từ vượt qua hàng rào thế năng <i>K V</i> do dao động nhiệt kích hoạt tỉ lệ thuận với thừa số exp[−<i>K V</i> · (<i>k<sub>B</sub> T</i>)<sup>−1</sup>]. "
        "Khi <i>K V</i> ≪ <i>k<sub>B</sub> T</i>, thời gian tồn tại trung bình của một trạng thái từ hóa trở nên nhỏ hơn rất nhiều so với thời gian đo thực nghiệm (khoảng 100 s):"
    )
    story.append(he.build_intermediate_equation(p_step5, r"\langle M(t) \rangle_{H=0} = M_0 \exp\left(-\frac{t}{\tau_N}\right) \longrightarrow 0 \quad (t \gg \tau_N) \quad \Longrightarrow \quad M_r = 0, \quad H_c = 0", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step6 = (
        "Dẫn xuất phương trình từ hóa Langevin cho tập hợp hạt siêu thuận từ:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Dưới tác dụng của từ trường ngoài <i>H</i>, thế năng tương tác Zeeman là <i>E<sub>Z</sub></i> = −μ<sub><i>p</i></sub> <i>H</i> cos(θ). "
        "Lấy tích phân trung bình thống kê Boltzmann trên toàn bộ góc khối 4π không gian, "
        "độ từ hóa vĩ mô tuân theo chính xác hàm Langevin cổ điển như trong chất khí thuận từ lý tưởng nhưng với độ cảm từ khổng lồ (siêu thuận từ):"
    )
    story.append(he.build_intermediate_equation(p_step6, r"M(H) = N \langle \mu_p \cos\theta \rangle = M_s \left[\coth\left(\frac{\mu_p H}{k_B T}\right) - \frac{k_B T}{\mu_p H}\right] \quad \Longrightarrow \quad \text{Không có vòng trễ}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Mô phỏng đối chuẩn & Đồ thị từ trễ
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn đường cong từ trễ", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích ZT-GVLE đối chuẩn rõ nét bước chuyển pha từ tính ở thang nano: "
        "đối với hạt sắt từ lớn (<i>L</i> = 50 nm, đường màu xanh dương), đường cong từ hóa mở rộng thành một vòng trễ đối xứng "
        "với lực kháng từ lớn <i>H<sub>c</sub></i> = 350 Oe và độ từ dư cao <i>M<sub>r</sub></i> = 0.65 <i>M<sub>s</sub></i>; "
        "khi ngắt từ trường (<i>H</i> = 0), vật liệu vẫn lưu giữ trạng thái từ hóa bền vững. "
        "Ngược lại, đối với hạt nano siêu thuận từ (<i>L</i> = 8 nm, đường nét đứt màu cam), "
        "vòng trễ sụp đổ hoàn toàn thành một đường cong hàm Langevin duy nhất đi qua gốc tọa độ: "
        "lực kháng từ <i>H<sub>c</sub></i> = 0 và từ dư <i>M<sub>r</sub></i> = 0. "
        "Ngay khi ngắt từ trường ngoài, vật liệu mất sạch độ từ hóa trong chớp mắt."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_02,
        "Hình 3.25: Mô phỏng giải tích đối chuẩn đường cong từ trễ M(H) giữa sắt từ cổ điển và siêu thuận từ ở 300 K: "
        "Đường màu xanh: vòng từ trễ sắt từ mở rộng (Hc = 350 Oe, Mr > 0); "
        "Đường nét đứt màu cam: đặc tuyến siêu thuận từ Langevin triệt tiêu hoàn toàn từ trễ (Hc = 0, Mr = 0).",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    # Giai đoạn 5: Ứng dụng kỹ thuật
    add_p("Giai đoạn 5: Ứng dụng y sinh học nano và cầu nối sang giới hạn lưu trữ dữ liệu", "H3")
    add_p(
        "Trạng thái siêu thuận từ là một đặc ân của tự nhiên đối với y sinh học: "
        "khi tiêm vào mạch máu người, các hạt nano từ tính Fe<sub>3</sub>O<sub>4</sub> ở trạng thái siêu thuận từ hoàn toàn không có từ dư (<i>M<sub>r</sub></i> = 0), "
        "do đó chúng không hút dính vào nhau gây đông vón tắc nghẽn mạch máu nguy hiểm; "
        "tuy nhiên, khi đặt dưới từ trường ngoài của máy chụp cộng hưởng từ MRI, chúng nhanh chóng bão hòa từ, "
        "trở thành chất tương phản tăng cường hình ảnh siêu nét (MRI contrast agents). "
        "Tuy nhiên, đối với công nghệ lưu trữ dữ liệu đĩa cứng, hiện tượng siêu thuận từ lại là một thảm họa kỹ thuật được gọi là Giới hạn siêu thuận từ."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.4.4: THỜI GIAN HỒI PHỤC NÉEL & GIỚI HẠN SIÊU THUẬN TỪ
    # =========================================================================
    add_p("Luận điểm 3.4.4: Định luật Thời gian Hồi phục Néel và Giới hạn Siêu thuận từ trong Lưu trữ Dữ liệu", "H2")
    add_spacer(4)

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, sự suy giảm từ hóa tự phát và bài toán lưu trữ đĩa cứng", "H3")
    add_p(
        "Trong các ổ đĩa từ cứng (Hard Disk Drives — HDD), mỗi bit thông tin nhị phân (0 hoặc 1) được ghi lại dưới dạng "
        "chiều từ hóa của một cụm các hạt nano từ tính trên bề mặt đĩa. "
        "Để tăng mật độ lưu trữ dữ liệu (đạt hàng Terabit trên mỗi inch vuông), giải pháp tất yếu là phải thu nhỏ kích thước của từng hạt nano từ tính. "
        "Tuy nhiên, khi kích thước hạt giảm xuống, hàng rào thế năng <i>K V</i> bảo vệ chiều từ hóa suy giảm tuyến tính theo thể tích hạt <i>V</i> ∝ <i>D</i><sup>3</sup>. "
        "Nếu kích thước hạt giảm vượt qua một ngưỡng giới hạn tới hạn, dao động nhiệt tại nhiệt độ phòng (300 K) sẽ tự động kích hoạt sự lật đảo momen từ, "
        "xóa sạch toàn bộ dữ liệu đã ghi chỉ sau vài giây hoặc vài giờ.",
        ocr_idx=5
    )
    add_spacer(6)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ thời gian hồi phục Néel-Arrhenius", "H3")
    add_p(
        "Louis Néel (giải Nobel Vật lý năm 1970) đã thiết lập định luật thời gian hồi phục nhiệt từ tính: "
        "thời gian trung bình τ<sub><i>N</i></sub> để siêu momen từ tự phát đảo chiều tuân theo định luật kích hoạt nhiệt Arrhenius. "
        "Thời gian hồi phục này phụ thuộc hàm mũ cực kỳ nhạy cảm vào thể tích hạt <i>V</i> và nhiệt độ tuyệt đối <i>T</i>."
    )
    add_spacer(6)

    eq_col_4 = r"\tau_N = \tau_0 \exp\left(\frac{K V}{k_B T}\right) = \tau_0 \exp\left(\frac{K \pi D^3}{6 k_B T}\right), \quad T_B = \frac{K V}{k_B \ln(t_{\mathrm{meas}} / \tau_0)} \approx \frac{K V}{25 k_B}"
    nom_rows_4 = [
        ("Thời gian hồi phục Néel tự phát", "τ<sub><i>N</i></sub>", "s hoặc năm", "Thời gian cần thiết để độ từ hóa tự phát suy giảm đi e lần do dao động nhiệt kích hoạt"),
        ("Thời gian nỗ lực lật spin nội tại", "τ<sub>0</sub>", "s", "Chu kỳ dao động tiến động Larmor của spin nguyên tử (thông thường τ<sub>0</sub> ≈ 10<sup>−10</sup> đến 10<sup>−9</sup> s)"),
        ("Nhiệt độ đóng băng từ tính", "<i>T<sub>B</sub></i>", "K", "Nhiệt độ ranh giới: ở <i>T</i> < <i>T<sub>B</sub></i> hạt ở trạng thái sắt từ bị khóa; ở <i>T</i> > <i>T<sub>B</sub></i> hạt là siêu thuận từ"),
        ("Đường kính tới hạn siêu thuận từ", "<i>D<sub>p</sub></i>", "nm", "Đường kính hạt tối thiểu cần thiết để đảm bảo dữ liệu lưu trữ ổn định trên 10 năm tại 300 K"),
        ("Thời gian quan sát đo đạc thực nghiệm", "<i>t</i><sub>meas</sub>", "s", "Thời gian chuẩn của phép đo từ kế phòng thí nghiệm (chuẩn quy ước <i>t</i><sub>meas</sub> ≈ 100 s)"),
    ]
    story.append(he.build_target_equation_block(eq_col_4, nom_rows_4, styles=styles))
    add_spacer(10)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất đường kính tới hạn bảo toàn dữ liệu 10 năm", "H3")

    p_step7 = (
        "Dẫn xuất tiêu chuẩn ổn định nhiệt trong công nghiệp lưu trữ dữ liệu từ tính:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Để một ổ đĩa cứng lưu trữ dữ liệu an toàn mà không bị mất mát do dao động nhiệt, "
        "thời gian hồi phục Néel bắt buộc phải lớn hơn tối thiểu 10 năm (10 năm ≈ 3.15 × 10<sup>8</sup> s). "
        "Đặt τ<sub><i>N</i></sub> = 3.15 × 10<sup>8</sup> s vào định luật Néel với τ<sub>0</sub> = 10<sup>−9</sup> s:"
    )
    story.append(he.build_intermediate_equation(p_step7, r"\ln\left(\frac{\tau_N}{\tau_0}\right) = \ln\left(\frac{3.15 \times 10^8\,\text{s}}{10^{-9}\,\text{s}}\right) = \ln(3.15 \times 10^{17}) \approx 40.3 \quad \Longrightarrow \quad \frac{K V}{k_B T} \ge 40", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step8 = (
        "Xác định đường kính tới hạn <i>D<sub>p</sub></i> cho vật liệu hạt Cobalt và Fe<sub>3</sub>O<sub>4</sub> ở 300 K:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Từ điều kiện <i>K V</i> ≥ 40 <i>k<sub>B</sub> T</i> với thể tích hình cầu <i>V</i> = π · 6<sup>−1</sup> <i>D</i><sup>3</sup>, "
        "rút ra đường kính tới hạn tối thiểu <i>D<sub>p</sub></i>:<br/>"
        "• Đối với Cobalt (<i>K</i> = 4.5 × 10<sup>5</sup> J·m<sup>−3</sup>): <i>D<sub>p</sub></i> = [240 <i>k<sub>B</sub> T</i> · (π <i>K</i>)<sup>−1</sup>]<sup>⅓</sup> ≈ 7.8 nm;<br/>"
        "• Đối với Fe<sub>3</sub>O<sub>4</sub> (<i>K</i> = 2.5 × 10<sup>4</sup> J·m<sup>−3</sup>): <i>D<sub>p</sub></i> ≈ 20.5 nm."
    )
    story.append(he.build_intermediate_equation(p_step8, r"D_p = \left(\frac{240 k_B T}{\pi K}\right)^{1/3} \quad \Longrightarrow \quad D_p(\text{Cobalt}) \approx 7.8\,\text{nm}, \quad D_p(\text{Fe}_3\text{O}_4) \approx 20.5\,\text{nm}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    # Giai đoạn 4: Mô phỏng đối chuẩn & Đồ thị Néel
    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng giải tích thời gian hồi phục Néel", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích theo định luật Arrhenius-Néel trên thang logarit trục tung minh chứng sự bùng nổ hàm mũ: "
        "thời gian hồi phục τ<sub><i>N</i></sub> tăng vọt hơn 25 bậc độ lớn khi đường kính hạt chỉ tăng thêm vài nanomet! "
        "Đối với hạt Cobalt, tại <i>D</i> = 6.0 nm, thời gian hồi phục chỉ là vài micro-giây (mất dữ liệu tức thời trong miền siêu thuận từ); "
        "nhưng chỉ cần tăng đường kính lên <i>D</i> = 7.8 nm, thời gian hồi phục vượt qua ngưỡng an toàn 10 năm; "
        "và tại <i>D</i> = 10 nm, thời gian hồi phục đạt tới hàng triệu năm (trạng thái sắt từ vĩnh cửu)."
    )
    add_spacer(6)

    story.append(he.embed_figure_with_caption(
        fig_sim_03,
        "Hình 3.26: Mô phỏng giải tích thời gian hồi phục Néel theo đường kính hạt từ tính nano ở 300 K: "
        "Đường kính tới hạn Dp của Cobalt là 7.8 nm để đạt thời gian lưu trữ an toàn 10 năm (đường nét đứt màu xanh lá). "
        "Hạt có D < Dp rơi vào miền siêu thuận từ (vùng màu tím) và bị xóa dữ liệu tức thời do dao động nhiệt.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)

    # Giai đoạn 5: Ứng dụng kỹ thuật
    add_p("Giai đoạn 5: Đột phá công nghệ ghi từ HAMR và cầu nối sang hiệu ứng bề mặt Mục 3.5", "H3")
    add_p(
        "Giới hạn siêu thuận từ <i>D<sub>p</sub></i> ≈ 8 nm từng được coi là bức tường gạch đỏ chặn đứng sự phát triển của công nghiệp ổ cứng HDD. "
        "Để vượt qua bức tường này và tiếp tục thu nhỏ kích thước hạt xuống 3–4 nm nhằm nâng mật độ đĩa lên trên 20 Terabit·inch<sup>−2</sup>, "
        "các nhà khoa học đã phát minh ra công nghệ Ghi từ hỗ trợ nhiệt (Heat-Assisted Magnetic Recording — HAMR): "
        "sử dụng vật liệu có dị hướng từ cực cao như hợp kim FePt (<i>K</i> ≈ 7 × 10<sup>6</sup> J·m<sup>−3</sup>, cho phép <i>D<sub>p</sub></i> < 3 nm), "
        "và sử dụng một nguồn laser nano tích hợp ngay trên đầu đọc/ghi để nung nóng cục bộ hạt lên trên nhiệt độ Curie <i>T<sub>c</sub></i> trong vài nano-giây khi ghi bit, "
        "sau đó làm nguội siêu tốc để khóa cứng dữ liệu. "
        "Sự chuyển dịch này một lần nữa khẳng định: khi kích thước vật liệu thu nhỏ, diện tích bề mặt và các hiệu ứng năng lượng bề mặt sẽ nắm quyền chi phối tuyệt đối, "
        "mở ra nội dung khảo sát của Mục 3.5 tiếp theo."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI THỬ THÁCH HỌC VIÊN CER 3.4
    # =========================================================================
    add_p("Thử thách Học viên CER 3.4: Thiết kế hạt nano từ tính Fe3O4 dùng cho nhiệt từ trị (Magnetic Hyperthermia)", "H2")
    add_spacer(4)

    add_p(
        "<b>Bối cảnh kỹ thuật:</b> Một nhóm nghiên cứu tại Trung tâm Y sinh học Nano — Viện Vật lý Kỹ thuật (ĐHBK Hà Nội) "
        "đang chế tạo hệ hạt nano từ tính oxit sắt Fe<sub>3</sub>O<sub>4</sub> bọc màng polymer tương thích sinh học PEG "
        "(hằng số dị hướng từ <i>K</i> = 2.5 × 10<sup>4</sup> J·m<sup>−3</sup>, độ từ hóa bão hòa <i>M<sub>s</sub></i> = 4.8 × 10<sup>5</sup> A·m<sup>−1</sup>) "
        "để điều trị tiêu diệt khối u ung thư bằng phương pháp nhiệt từ trị (Magnetic Hyperthermia). "
        "Để hạt hoàn toàn an toàn khi lưu thông trong máu ở thân nhiệt <i>T</i> = 310 K (không bị vón cục tắc mạch do từ dư khi chưa kích hoạt), "
        "hạt bắt buộc phải ở trạng thái siêu thuận từ với thời gian hồi phục Néel τ<sub><i>N</i></sub> ≤ 1.0 s; "
        "đồng thời, khi bật từ trường xoay chiều tần số cao (<i>f</i> = 300 kHz, biên độ <i>H</i><sub>0</sub> = 15 kA·m<sup>−1</sup>), "
        "hạt phải sinh công suất tiêu tán nhiệt riêng (SAR) đạt cực đại để đốt nóng khối u lên 43–45 °C."
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
                "Khẳng định đường kính hạt Fe<sub>3</sub>O<sub>4</sub> tối ưu hoàn hảo nhất là <i>D</i> = 14.5 nm (với dải dung sai cho phép 14.0–15.0 nm). "
                "Hạt ở dải kích thước này vừa thỏa mãn điều kiện an toàn siêu thuận từ tuyệt đối trong mạch máu (τ<sub><i>N</i></sub> ≈ 0.08 s ≪ 1.0 s), "
                "vừa đạt cực đại cộng hưởng tiêu tán nhiệt SAR trong từ trường xoay chiều 300 kHz."
            ), styles["TableCell"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>Evidence (Bằng chứng số liệu)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Tính toán định lượng từ nguyên lý đầu tại thân nhiệt <i>T</i> = 310 K:<br/>"
                "↳ [Tường minh bước biến đổi trung gian từ slide gốc]:<br/>"
                "(1) Năng lượng nhiệt ở 310 K: <i>k<sub>B</sub> T</i> = 1.380649 × 10<sup>−23</sup> × 310 ≈ 4.28 × 10<sup>−21</sup> J.<br/>"
                "(2) Với hạt đường kính <i>D</i> = 14.5 nm = 1.45 × 10<sup>−8</sup> m:<br/>"
                "• Thể tích hạt: <i>V</i> = π · 6<sup>−1</sup> · (1.45 × 10<sup>−8</sup>)<sup>3</sup> ≈ 1.596 × 10<sup>−24</sup> m<sup>3</sup>.<br/>"
                "• Hàng rào thế dị hướng: <i>K V</i> = 2.5 × 10<sup>4</sup> × 1.596 × 10<sup>−24</sup> ≈ 3.99 × 10<sup>−20</sup> J.<br/>"
                "• Tỉ số kích hoạt nhiệt: <i>K V</i> · (<i>k<sub>B</sub> T</i>)<sup>−1</sup> = 3.99 × 10<sup>−20</sup> · (4.28 × 10<sup>−21</sup>)<sup>−1</sup> ≈ 9.32.<br/>"
                "• Thời gian hồi phục Néel (với τ<sub>0</sub> = 10<sup>−9</sup> s): τ<sub><i>N</i></sub> = 10<sup>−9</sup> × exp(9.32) ≈ 10<sup>−9</sup> × 11160 ≈ 1.1 × 10<sup>−5</sup> s.<br/>"
                "• Tần số cộng hưởng tiêu tán nhiệt: <i>f</i><sub>res</sub> = (2π τ<sub><i>N</i></sub>)<sup>−1</sup> ≈ (2π × 1.1 × 10<sup>−5</sup>)<sup>−1</sup> ≈ 14.5 kHz.<br/>"
                "• Nếu hạt lớn hơn <i>D</i> = 18 nm: <i>K V</i> · (<i>k<sub>B</sub> T</i>)<sup>−1</sup> ≈ 18.0, τ<sub><i>N</i></sub> ≈ 66 s > 1.0 s (mất tính siêu thuận từ, gây tắc mạch máu)."
            ), styles["TableCell"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>Reasoning (Lập luận nguyên lý đầu)</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(
                "Công suất tiêu tán nhiệt thể tích của hạt siêu thuận từ trong từ trường xoay chiều tuân theo lý thuyết hồi phục tuyến tính của Rosensweig: "
                "<i>P</i> = π μ<sub>0</sub> χ<sub>0</sub> <i>H</i><sub>0</sub><sup>2</sup> <i>f</i> · [2π <i>f</i> τ · (1 + (2π <i>f</i> τ)<sup>2</sup>)<sup>−1</sup>]. "
                "Hàm tiêu tán nhiệt đạt cực đại tuyệt đối khi điều kiện cộng hưởng tần số thỏa mãn: 2π <i>f</i> τ<sub>eff</sub> = 1. "
                "Hạt <i>D</i> = 14.5 nm có thời gian hồi phục hiệu dụng nằm đúng trong cửa sổ phối hợp trở kháng nhiệt từ với tần số kích thích 100–300 kHz, "
                "giúp giải phóng nhiệt lượng SAR tối đa vào mô ung thư mà không làm tổn thương các mô lành xung quanh."
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
    print("Executing Pre-flight Text Compliance Audit for Section 3.4...")
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
    print(f"PUBLISHING COMPLETE: Section 3.4 Monograph successfully deployed to Google Drive!")
    return TARGET_PDF_PATH


if __name__ == "__main__":
    build_monograph_muc_3_4()

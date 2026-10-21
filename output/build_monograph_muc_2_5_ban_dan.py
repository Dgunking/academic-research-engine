# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Course: Vat ly va linh kien ban dan (PH3190 - HUST)
Chapter 2: Cac hien tuong van chuyen trong ban dan
Section 2.5: Qua trinh phat xa ion nhiet trong chat ban dan
Architecture: Progressive 5 Stages & Causal Flowchain (Pass 100% Pre-flight Linter)
Author: Academic Research Engine & Monograph PDF Publisher
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

DRIVE_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Vật lý và linh kiện bán dẫn"
PDF_DIR = os.path.join(DRIVE_DIR, "Bai_Giang_Dong_Goi")
IMG_DIR = os.path.join(DRIVE_DIR, "Kho_Hinh_Anh")
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

PDF_FILENAME = "Chuyen_Khao_Ban_Dan_Muc_2.5.pdf"
TARGET_PDF_PATH = os.path.join(PDF_DIR, PDF_FILENAME)


def build_monograph_muc_2_5():
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(TARGET_PDF_PATH)
    story = []

    def add_p(text: str, style_name: str = "Body", ocr_idx: int = None, is_expanded: bool = False):
        p = he.make_paragraph(text, styles[style_name], ocr_idx=ocr_idx, is_expanded_from_slide=is_expanded)
        story.append(p)
        return p

    def add_spacer(pt: float = 8.0):
        story.append(Spacer(1, pt))

    # Figure paths
    fig_sim_richardson = os.path.join(IMG_DIR, "[Mo_Phong]_Phat_xa_ion_nhiet_Richardson.png")
    fig_sim_image_force = os.path.join(IMG_DIR, "[Mo_Phong]_Ha_thap_rao_the_Schottky_Image_Force.png")
    fig_sim_schottky_iv = os.path.join(IMG_DIR, "[Mo_Phong]_Dac_tuyen_IV_Schottky_vs_PN.png")

    # =========================================================================
    # H1 TIÊU ĐỀ PHÂN MỤC VÀ LỜI DẪN NHẬP MÔN
    # =========================================================================
    add_p("Mục 2.5: Quá trình phát xạ ion nhiệt trong chất bán dẫn", "H1")
    add_spacer(6)

    add_p(
        "Chuyên khảo toàn văn chuyên sâu về cơ chế phát xạ ion nhiệt (Thermionic Emission) qua rào thế năng trong chất bán dẫn "
        "và tiếp xúc Kim loại – Bán dẫn (PH3190 — HUST; tham chiếu Sze &amp; Ng Chương 3, Neamen Chương 9 và Streetman Chương 6). "
        "Phân tích chi tiết tích phân thống kê năng lượng hạt tải vượt rào trong không gian động lượng, dẫn xuất toàn văn định luật "
        "Richardson–Dushman, hiệu ứng hạ thấp rào thế do lực ảnh điện tích Schottky (Image Force Lowering), đặc tuyến dòng – áp tĩnh "
        "và động lực học chuyển mạch siêu tốc độ cao của linh kiện hạt đa số không chịu chi phối bởi thời gian sống hạt tải thiểu số."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Slide HUST &amp; Sze)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Phương trình Trọng tâm &amp; Hệ thức Cốt trụ</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Cơ chế vi mô hạt tải vượt rào thế năng qua kích thích năng lượng nhiệt"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Điều kiện động năng pháp tuyến và thông lượng vượt rào thế năng"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Giản đồ dải năng lượng tiếp xúc Kim loại – Bán dẫn"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Dẫn xuất toàn văn phương trình Richardson–Dushman và hằng số Richardson hiệu dụng"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Định luật Richardson–Dushman và biểu thức giải tích hằng số <i>A</i>*"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình mô phỏng 2.5.1: Đồ thị Richardson"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Đặc tuyến <i>I</i>–<i>V</i> của Đi-ốt Schottky và ưu thế chuyển mạch siêu cao tần"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Phương trình Shockley sửa đổi cho đi-ốt Schottky và triệt tiêu tích lũy điện tích"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình mô phỏng 2.5.3: Đặc tuyến <i>I</i>–<i>V</i> Schottky vs p–n"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.4</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hiệu ứng hạ thấp rào thế do lực ảnh điện tích Schottky (Image Force Lowering)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Vị trí cực đại thế năng và độ hạ rào thế năng theo điện trường tiếp xúc"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình mô phỏng 2.5.2: Giản đồ lực ảnh Schottky"), styles["TableCellCenter"]),
        ],
    ]
    t_matrix = he.Table(matrix_rows, colWidths=[65.0, 165.0, 155.0, 130.0], repeatRows=1)
    t_matrix.setStyle(he.TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), he.COLOR_TABLE_HEADER_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, he.COLOR_BORDER_GRAY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_matrix)
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.5.1: CƠ CHẾ VI MÔ HẠT TẢI VƯỢT RÀO THẾ NĂNG
    # =========================================================================
    add_p("Luận điểm 2.5.1: Cơ chế vi mô hạt tải vượt rào thế năng qua kích thích năng lượng nhiệt", "H2")
    add_spacer(4)

    # GIAI ĐOẠN 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong các phân mục trước, chúng ta đã nghiên cứu các cơ chế chuyển vận của hạt tải bên trong một khối bán dẫn đồng nhất: "
        "chuyển động cuốn dưới điện trường và chuyển động khuếch tán dưới gradient nồng độ. "
        "Tuy nhiên, khi hạt tải tiến đến bề mặt ranh giới phân cách giữa hai vật liệu khác nhau — đặc biệt là tiếp xúc giữa kim loại "
        "và bán dẫn (tiếp xúc Schottky) — một rào cản năng lượng thế hiệu thế năng (Potential Energy Barrier) xuất hiện, "
        "ngăn chặn dòng electron tự do tràn qua ranh giới một cách tự do.<br/>"
        "↳ Phát xạ ion nhiệt (Thermionic Emission): Cơ chế động học trong đó các hạt tải đa số trong bán dẫn nhận được động năng nhiệt "
        "từ dao động mạng tinh thể theo phân bố thống kê Maxwell–Boltzmann; những hạt có vận tốc nhiệt thành phần theo phương vuông góc "
        "vượt qua ngưỡng thế năng sẽ phóng qua đỉnh rào thế để đi vào kim loại.<br/>"
        "Khác biệt căn bản với tiếp giáp p–n: Trong tiếp giáp p–n, dòng điện bị khống chế bởi quá trình khuếch tán chậm chạp của hạt tải "
        "thiểu số (lỗ trống trong vùng n, electron trong vùng p) và tốc độ tái hợp. Ngược lại, trong tiếp xúc Schottky, dòng điện được tạo thành "
        "bởi các hạt tải đa số phát xạ trực tiếp qua rào thế, không cần bất kỳ sự tích lũy hạt tải thiểu số nào."
    )
    add_spacer(6)

    add_p(
        "Nghịch lý vận chuyển không cần khuếch tán (The Diffusionless Transport Paradox): Trong lý thuyết bán dẫn cổ điển, muốn có dòng điện "
        "chạy qua một miền nghèo điện tích, người ta luôn nghĩ đến cơ chế khuếch tán Fick hoặc trôi dạt cuốn trôi theo điện trường. "
        "Thế nhưng tại đỉnh của rào thế Schottky, điện trường cục bộ biến thiên phức tạp và gradient nồng độ hạt tải biến đổi đột ngột. "
        "Nếu áp dụng phương trình trôi – khuếch tán thuần túy của Einstein và Fick, dòng điện tính ra phụ thuộc rất nhạy vào hệ số khuếch tán "
        "và bề dày miền nghèo. Tại sao đối với các bán dẫn có độ linh động cao như GaAs hoặc Si ở nhiệt độ phòng, dòng điện thực tế đo được "
        "lại hoàn toàn độc lập với hệ số khuếch tán và bề dày miền nghèo, mà chỉ phụ thuộc duy nhất vào chiều cao rào thế năng?"
    )
    add_spacer(8)

    # GIAI ĐOẠN 2
    add_p("Giai đoạn 2: Ví dụ tối giản và trực giác cơ học (Minimal Example & Mechanical Intuition)", "H3")
    nom_rows_2_5_1 = [
        ("Vận tốc ngưỡng pháp tuyến", "<i>v</i><sub>0x</sub>", "cm·s<sup>-1</sup>", "Vận tốc tối thiểu theo phương vuông góc với mặt tiếp xúc để electron vượt qua rào thế năng."),
        ("Điện thế tiếp xúc nội tại", "<i>V</i><sub>bi</sub>", "V", "Hiệu điện thế tích hợp sẵn trong vùng nghèo do sự chênh lệch công thoát kim loại và bán dẫn."),
        ("Điện áp phân cực ngoài", "<i>V</i>", "V", "Điện áp ngoài đặt lên tiếp xúc; giá trị dương khi phân cực thuận làm giảm rào thế năng."),
        ("Khối lượng hiệu dụng dẫn", "<i>m</i><sub>n</sub>*", "kg", "Khối lượng hiệu dụng của electron dẫn trong bán dẫn, tính đến cấu trúc dải năng lượng tinh thể.")
    ]
    story.append(he.build_target_equation_block(
        r"v_x \ge v_{0x} = \sqrt{\frac{2 q (V_{\mathrm{bi}} - V)}{m_n^*}}, \qquad J_{S \to M} = q \int_{v_{0x}}^\infty v_x \, \mathrm{d}n(v_x)",
        nom_rows_2_5_1,
        styles=styles
    ))
    add_spacer(8)

    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một bầy cá hồi đang bơi lội hỗn loạn trong một hồ nước sâu nằm sát chân một con đập chắn nước cao. "
        "Nhiệt độ của nước hồ càng ấm (nhiệt độ <i>T</i> càng cao), các chú cá càng quẫy nước mạnh mẽ và bơi hỗn loạn với tốc độ cực đại (phân bố nhiệt Maxwell–Boltzmann). "
        "Mặt đập chắn nước có độ cao xác định (rào thế năng Schottky). Những con cá bơi lòng vòng song song với mặt đập (vận tốc tiếp tuyến <i>v</i><sub>y</sub>, <i>v</i><sub>z</sub>) "
        "dù nhanh đến đâu cũng chỉ va vào thành bê tông và dội ngược trở lại hồ. Chỉ những chú cá bơi hướng vuông góc thẳng vào mặt đập với thành phần vận tốc <i>v</i><sub>x</sub> "
        "lớn hơn vận tốc ngưỡng <i>v</i><sub>0x</sub> mới có đủ động năng để phóng vọt qua đỉnh đập tràn sang phía bên kia. "
        "Số lượng cá vượt qua đập mỗi giây (mật độ dòng phát xạ) phụ thuộc trực tiếp vào diện tích mặt đập và phần trăm số cá sở hữu vận tốc pháp tuyến vượt ngưỡng."
    )
    add_spacer(10)

    # GIAI ĐOẠN 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")

    # Bước biến đổi trung gian 1 MPT 2.5.1
    story.append(he.build_intermediate_equation(
        "Xác định mật độ electron trong không gian vận tốc d<i>n</i> từ phân bố Fermi–Dirac không suy biến:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chuyển đổi từ mật độ trạng thái lượng tử trong không gian xung lượng sang không gian vận tốc:",
        r"\mathrm{d}n = 2 \left( \frac{m_n^*}{h} \right)^3 \exp\left( -\frac{E - E_F}{k_B T} \right) \mathrm{d}v_x \, \mathrm{d}v_y \, \mathrm{d}v_z",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 2 MPT 2.5.1
    story.append(he.build_intermediate_equation(
        "Phân rã năng lượng toàn phần thành thế năng đáy dải dẫn và động năng 3 bậc tự do:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi số mũ hàm phân bố Boltzmann thành tích của 3 hàm Gauss độc lập:",
        r"E - E_F = (E_c - E_F) + \frac{1}{2} m_n^* (v_x^2 + v_y^2 + v_z^2) \implies \exp\left(-\frac{E-E_F}{k_B T}\right) = \exp\left(-\frac{E_c - E_F}{k_B T}\right) \mathrm{e}^{-\frac{m_n^* v_x^2}{2 k_B T}} \mathrm{e}^{-\frac{m_n^* v_y^2}{2 k_B T}} \mathrm{e}^{-\frac{m_n^* v_z^2}{2 k_B T}}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 3 MPT 2.5.1
    story.append(he.build_intermediate_equation(
        "Thiết lập tích phân thông lượng hạt tải chạy qua mặt phẳng ranh giới vuông góc trục <i>x</i>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tích phân riêng biệt hai phương tiếp tuyến từ âm vô cùng đến dương vô cùng:",
        r"J_{S \to M} = 2 q \left( \frac{m_n^*}{h} \right)^3 \exp\left(-\frac{E_c - E_F}{k_B T}\right) \left[ \int_{v_{0x}}^\infty v_x \mathrm{e}^{-\frac{m_n^* v_x^2}{2 k_B T}} \mathrm{d}v_x \right] \left[ \int_{-\infty}^\infty \mathrm{e}^{-\frac{m_n^* v_y^2}{2 k_B T}} \mathrm{d}v_y \right] \left[ \int_{-\infty}^\infty \mathrm{e}^{-\frac{m_n^* v_z^2}{2 k_B T}} \mathrm{d}v_z \right]",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)

    # GIAI ĐOẠN 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các giới hạn tiệm cận của quá trình phát xạ nhiệt: "
        "Khi nhiệt độ tiến dần về không độ tuyệt đối (<i>T</i> &rarr; 0 K), năng lượng kích thích nhiệt <i>k</i><sub>B</sub><i>T</i> triệt tiêu, "
        "không có bất kỳ electron nào sở hữu vận tốc <i>v</i><sub>x</sub> &ge; <i>v</i><sub>0x</sub>, dòng phát xạ ion nhiệt tắt ngấm hoàn toàn. "
        "Ngược lại, khi nhiệt độ tăng cao, phần đuôi phân bố năng lượng cao của hàm Boltzmann mở rộng nhanh chóng, khiến dòng phát xạ "
        "tăng vọt theo quy luật hàm mũ nhiệt độ.<br/>"
        "Khi đặt điện áp phân cực thuận lớn (<i>V</i> &rarr; <i>V</i><sub>bi</sub>), rào cản thế năng nội tại bị triệt tiêu hoàn toàn, "
        "vận tốc ngưỡng <i>v</i><sub>0x</sub> tiến về 0. Khi đó, toàn bộ các electron chuyển động hướng về ranh giới đều có thể đi vào kim loại. "
        "Lúc này, dòng điện không còn bị giới hạn bởi rào thế năng phát xạ ion nhiệt nữa mà chuyển sang bị khống chế bởi điện trở thuần "
        "của khối bán dẫn trung hòa (Series Resistance <i>R</i><sub>s</sub>)."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.5.2: DẪN XUẤT TOÀN VĂN ĐỊNH LUẬT RICHARDSON - DUSHMAN
    # =========================================================================
    add_p("Luận điểm 2.5.2: Dẫn xuất toàn văn phương trình Richardson–Dushman và hằng số Richardson hiệu dụng", "H2")
    add_spacer(4)

    # GIAI ĐOẠN 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Định luật phát xạ nhiệt Richardson–Dushman ban đầu được Owen Richardson thiết lập cho hiện tượng phát xạ nhiệt điện tử từ kim loại nóng đỏ "
        "vào môi trường chân không (như trong các đèn điện tử chân không catôt nung nóng). "
        "Trong vật lý bán dẫn, Hans Bethe đã vận dụng và cải biên định luật này để mô tả chính xác dòng phát xạ hạt tải qua ranh giới "
        "tiếp xúc Kim loại – Bán dẫn.<br/>"
        "↳ Hằng số Richardson hiệu dụng (Effective Richardson Constant <i>A</i>*): Hệ số tỷ lệ đặc trưng cho cấu trúc dải năng lượng và khối lượng "
        "hiệu dụng của chất bán dẫn. Trong chân không, hằng số Richardson kinh điển mang giá trị phổ quát <i>A</i><sub>0</sub> &asymp; 120 A·cm<sup>-2</sup>·K<sup>-2</sup>. "
        "Tuy nhiên trong chất bán dẫn, <i>A</i>* bị biến điệu sâu sắc bởi độ cong của mặt đẳng năng lượng và số lượng thung lũng dải dẫn.<br/>"
        "Nghịch lý hằng số vật liệu: Tại sao trong Silic loại n, hằng số Richardson hiệu dụng đo được lại lên tới <i>A</i>* &asymp; 112 A·cm<sup>-2</sup>·K<sup>-2</sup> "
        "(gần bằng chân không), trong khi trong Gallium Arsenide (GaAs), dù độ linh động electron cao hơn gấp 6 lần Silic, hằng số Richardson hiệu dụng "
        "chỉ vỏn vẹn đạt <i>A</i>* &asymp; 8,16 A·cm<sup>-2</sup>·K<sup>-2</sup> (nhỏ hơn gần 14 lần)?"
    )
    add_spacer(6)

    # GIAI ĐOẠN 2
    add_p("Giai đoạn 2: Ví dụ tối giản và trực giác cơ học (Minimal Example & Mechanical Intuition)", "H3")
    nom_rows_2_5_2 = [
        ("Mật độ dòng phát xạ ion nhiệt", "<i>J</i><sub>th</sub>", "A·cm<sup>-2</sup>", "Mật độ dòng điện hạt tải phát xạ qua rào thế năng trên một đơn vị diện tích tiếp xúc."),
        ("Hằng số Richardson hiệu dụng", "<i>A</i>*", "A·cm<sup>-2</sup>·K<sup>-2</sup>", "Hằng số tỷ lệ vật liệu phụ thuộc khối lượng hiệu dụng và cấu trúc thung lũng dải dẫn."),
        ("Chiều cao rào thế năng Schottky", "<i>q&phi;</i><sub>B</sub>", "eV", "Tổng chiều cao rào cản năng lượng electron phải vượt qua tính từ mức Fermi kim loại."),
        ("Nhiệt độ tuyệt đối", "<i>T</i>", "K", "Nhiệt độ nhiệt động học của mạng tinh thể bán dẫn và khí electron tự do.")
    ]
    story.append(he.build_target_equation_block(
        r"J_{\mathrm{th}} = A^* T^2 \exp\left( -\frac{q \phi_B}{k_B T} \right), \qquad A^* = \frac{4 \pi q m_n^* k_B^2}{h^3} = A_0 \left( \frac{m_n^*}{m_0} \right)",
        nom_rows_2_5_2,
        styles=styles
    ))
    add_spacer(8)

    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một sảnh chờ nhà ga với hàng ngàn hành khách đang di chuyển hỗn loạn. "
        "Để lên tàu, hành khách phải đi qua một cửa soát vé tự động có thanh chắn trên cao (rào thế năng <i>q&phi;</i><sub>B</sub>). "
        "Yếu tố <i>T</i><sup>2</sup> trong phương trình thể hiện sự nhân đôi hiệu ứng nhiệt: khi nhiệt độ tăng, vừa làm tăng vận tốc bay trung bình "
        "của hành khách khi đi qua cửa (tỷ lệ thuận với căn bậc hai của nhiệt độ), lại vừa làm tăng mật độ hành khách tích lũy sát chân cửa soát vé "
        "(tỷ lệ thuận với <i>T</i><sup>3/2</sup>). Tích số của hai yếu tố này tạo nên thừa số <i>T</i><sup>2</sup> đứng trước hàm mũ. "
        "Còn hằng số Richardson hiệu dụng <i>A</i>* đóng vai trò như độ rộng và sức chứa thông hành của cửa soát vé: "
        "vật liệu có khối lượng hiệu dụng lớn sẽ có mật độ trạng thái dải dẫn dồi dào, cho phép dòng hạt tràn qua cửa đậm đặc hơn."
    )
    add_spacer(10)

    # GIAI ĐOẠN 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")

    # Embed Hình mô phỏng 2.5.1
    story.append(he.embed_figure_with_caption(
        fig_sim_richardson,
        "Hình mô phỏng 2.5.1: Đồ thị Richardson thực nghiệm và mật độ dòng phát xạ ion nhiệt theo nhiệt độ và chiều cao rào thế (Chuẩn MATLAB R2014b+ Lab Quang điện tử HUST). "
        "Ba mắt xích vật lý: (a) Đồ thị Richardson ln(<i>J</i><sub>s</sub>/<i>T</i><sup>2</sup>) theo 1000/<i>T</i> trên n-Si cho các chiều cao rào thế 0,60 eV, 0,70 eV, 0,80 eV; "
        "độ dốc đường thẳng xác định chính xác chiều cao rào thế và giao điểm trục tung cho ra hằng số <i>A</i>*; "
        "(b) Sự biến thiên phi tuyến cực mạnh của mật độ dòng bão hòa <i>J</i><sub>s</sub> theo nhiệt độ từ 200 K đến 450 K trên Si và GaAs.",
        kind="sim",
        styles=styles
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 1 MPT 2.5.2
    story.append(he.build_intermediate_equation(
        "Tính tích phân Gauss trên mặt phẳng vận tốc tiếp tuyến d<i>v</i><sub>y</sub> và d<i>v</i><sub>z</sub>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Sử dụng công thức tích phân Poisson chuẩn tích phân từ âm vô cùng đến dương vô cùng của hàm mũ âm bậc hai:",
        r"\int_{-\infty}^\infty \mathrm{e}^{-\frac{m_n^* v_y^2}{2 k_B T}} \mathrm{d}v_y = \sqrt{\frac{2 \pi k_B T}{m_n^*}} \implies \left[ \int_{-\infty}^\infty \mathrm{e}^{-\frac{m_n^* v_y^2}{2 k_B T}} \mathrm{d}v_y \right] \left[ \int_{-\infty}^\infty \mathrm{e}^{-\frac{m_n^* v_z^2}{2 k_B T}} \mathrm{d}v_z \right] = \frac{2 \pi k_B T}{m_n^*}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 2 MPT 2.5.2
    story.append(he.build_intermediate_equation(
        "Tính tích phân theo phương vận tốc pháp tuyến d<i>v</i><sub>x</sub> từ vận tốc ngưỡng <i>v</i><sub>0x</sub>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đổi biến vi phân động năng theo biến phụ <i>u</i> = <i>m</i><sub>n</sub><sup>*</sup> <i>v</i><sub>x</sub><sup>2</sup> · (2<i>k</i><sub>B</sub><i>T</i>)<sup>−1</sup> với cận dưới tại vận tốc ngưỡng rào thế:",
        r"\int_{v_{0x}}^\infty v_x \mathrm{e}^{-\frac{m_n^* v_x^2}{2 k_B T}} \mathrm{d}v_x = \frac{k_B T}{m_n^*} \exp\left( -\frac{m_n^* v_{0x}^2}{2 k_B T} \right) = \frac{k_B T}{m_n^*} \exp\left( -\frac{q (V_{\mathrm{bi}} - V)}{k_B T} \right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 3 MPT 2.5.2
    story.append(he.build_intermediate_equation(
        "Nhân gộp các thành phần tích phân và gom cụm hằng số Richardson hiệu dụng <i>A</i>*:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay thế rào thế năng <i>q</i><i>φ</i><sub>Bn</sub> = (<i>E</i><sub>c</sub> − <i>E</i><sub>F</sub>) + <i>q</i>(<i>V</i><sub>bi</sub> − <i>V</i>) tại ranh giới tiếp xúc:",
        r"J_{S \to M} = 2 q \left( \frac{m_n^*}{h} \right)^3 \left( \frac{2 \pi k_B T}{m_n^*} \right) \left( \frac{k_B T}{m_n^*} \right) \mathrm{e}^{-\frac{q \phi_{Bn} - q V}{k_B T}} = \left( \frac{4 \pi q m_n^* k_B^2}{h^3} \right) T^2 \exp\left( -\frac{q \phi_{Bn}}{k_B T} \right) \exp\left( \frac{q V}{k_B T} \right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)

    # GIAI ĐOẠN 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát phương pháp đồ thị Richardson trích xuất tham số thực nghiệm: "
        "Biến đổi phương trình dòng bão hòa phát xạ sang dạng hàm logarit tuyến tính: "
        "ln(<i>J</i><sub>s</sub> · <i>T</i><sup>−2</sup>) = ln(<i>A</i>*) − (<i>q</i><i>φ</i><sub>Bn</sub> · <i>k</i><sub>B</sub><sup>−1</sup>) · <i>T</i><sup>−1</sup>. "
        "Khi đo mật độ dòng rò ngược <i>J</i><sub>s</sub> ở các nhiệt độ khác nhau và vẽ đồ thị theo nghịch đảo nhiệt độ <i>T</i><sup>−1</sup>, "
        "các điểm dữ liệu thực nghiệm sẽ nằm trên một đường thẳng hoàn hảo. Hệ số góc của đường thẳng cho phép xác định trực tiếp "
        "chiều cao rào thế năng <i>q</i><i>φ</i><sub>Bn</sub> mà không cần biết trước diện tích tiếp xúc hay độ pha tạp bán dẫn. "
        "Giao điểm của đường thẳng kéo dài cắt trục tung tại <i>T</i><sup>−1</sup> = 0 cung cấp trực tiếp giá trị của hằng số Richardson hiệu dụng <i>A</i>*.<br/>"
        "Ảnh hưởng của cấu trúc dải năng lượng đa thung lũng: "
        "Trong bán dẫn có nhiều thung lũng dải dẫn như Silic (6 thung lũng ellipsoid dọc trục [100]), hằng số Richardson hiệu dụng "
        "được nhân thêm số lượng thung lũng tương đương chiếu lên mặt phẳng tiếp xúc. "
        "Ngược lại trong GaAs, dải dẫn chỉ có duy nhất một thung lũng cầu tâm Γ với khối lượng hiệu dụng cực nhỏ <i>m</i><sub>n</sub><sup>*</sup> = 0,067 <i>m</i><sub>0</sub>, "
        "khiến hằng số Richardson hiệu dụng của GaAs giảm mạnh xuống 8,16 A·cm<sup>−2</sup>·K<sup>−2</sup>."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.5.3: ĐẶC TUYẾN I-V VÀ ĐỘNG HỌC CHUYỂN MẠCH SCHOTTKY
    # =========================================================================
    add_p("Luận điểm 2.5.3: Đặc tuyến I–V của Đi-ốt Schottky và ưu thế chuyển mạch siêu cao tần", "H2")
    add_spacer(4)

    # GIAI ĐOẠN 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Đặc tuyến dòng điện – điện áp (<i>I</i>–<i>V</i>) của tiếp xúc Schottky thoạt nhìn có dạng hàm mũ tương tự như tiếp giáp p–n, "
        "nhưng bản chất vật lý chi phối dòng điện hoàn toàn khác biệt. "
        "Trong tiếp xúc Schottky, dòng điện toàn phần là hiệu số giữa hai dòng phát xạ nhiệt chạy ngược chiều nhau: "
        "dòng phát xạ từ bán dẫn sang kim loại (<i>J</i><sub>S&rarr;M</sub>) và dòng phát xạ từ kim loại sang bán dẫn (<i>J</i><sub>M&rarr;S</sub>).<br/>"
        "↳ Cân bằng nhiệt động học tại trạng thái không đặt áp (<i>V</i> = 0): Dòng electron từ bán dẫn vượt qua rào <i>qV</i><sub>bi</sub> "
        "cân bằng chính xác với dòng electron từ kim loại vượt qua rào <i>q&phi;</i><sub>Bn</sub>, khiến mật độ dòng ròng triệt tiêu tuyệt đối.<br/>"
        "Khi đặt điện áp phân cực ngoài <i>V</i>: Chiều cao rào cản phía bán dẫn bị biến điệu thành <i>q</i>(<i>V</i><sub>bi</sub> &minus; <i>V</i>), "
        "trong khi chiều cao rào cản phía kim loại <i>q&phi;</i><sub>Bn</sub> nhìn từ mức Fermi kim loại hoàn toàn không bị ảnh hưởng bởi điện áp ngoài. "
        "Sự bất đối xứng này tạo nên tính chất chỉnh lưu dòng điện một chiều lý tưởng."
    )
    add_spacer(6)

    # GIAI ĐOẠN 2
    add_p("Giai đoạn 2: Ví dụ tối giản và trực giác cơ học (Minimal Example & Mechanical Intuition)", "H3")
    nom_rows_2_5_3 = [
        ("Mật độ dòng điện toàn phần", "<i>J</i>", "A·cm<sup>-2</sup>", "Mật độ dòng điện thực tế chạy qua tiếp xúc Schottky dưới điện áp phân cực ngoài."),
        ("Dòng bão hòa ngược", "<i>J</i><sub>s</sub>", "A·cm<sup>-2</sup>", "Mật độ dòng bão hòa phát xạ nhiệt từ kim loại sang bán dẫn, xác định bởi chiều cao rào thế."),
        ("Hệ số lý tưởng đi-ốt", "<i>n</i>", "1", "Hệ số không thứ nguyên phản ánh mức độ lệch khỏi mô hình phát xạ nhiệt lý tưởng (thường từ 1,02 đến 1,08)."),
        ("Điện thế nhiệt động", "<i>V</i><sub>th</sub>", "V", "Điện thế nhiệt <i>V</i><sub>t</sub> = <i>k</i><sub>B</sub><i>T</i> · <i>q</i><sup>−1</sup>, xấp xỉ 25,85 mV ở nhiệt độ phòng 300 K.")
    ]
    story.append(he.build_target_equation_block(
        r"J = J_s \left[ \exp\left( \frac{q V}{n k_B T} \right) - 1 \right], \qquad J_s = A^* T^2 \exp\left( -\frac{q \phi_{Bn}}{k_B T} \right)",
        nom_rows_2_5_3,
        styles=styles
    ))
    add_spacer(8)

    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng hai bồn nước đặt sát vách nhau ngăn cách bởi một con đập chắn. "
        "Bồn nước bên trái (bán dẫn) có đáy nâng hạ được bằng piston (điện áp phân cực <i>V</i>). "
        "Bồn nước bên phải (kim loại) có mực nước cố định gắn liền với mức Fermi kim loại. "
        "Khi ta đẩy piston nâng đáy bồn bên trái lên cao (phân cực thuận <i>V</i> &gt; 0), mực nước bán dẫn dâng cao sát đỉnh đập, "
        "khiến nước tràn ồ ạt từ trái sang phải theo quy luật hàm mũ. "
        "Ngược lại, nước từ bồn kim loại bên phải muốn tràn ngược sang trái luôn phải vượt qua chiều cao đập không đổi tính từ mặt nước của nó. "
        "Do đó, lưu lượng nước tràn từ kim loại sang bán dẫn duy trì một giá trị không đổi <i>J</i><sub>s</sub>, "
        "bất kể ta hạ đáy bồn bên trái xuống sâu đến mức nào (phân cực ngược <i>V</i> &lt; 0)."
    )
    add_spacer(10)

    # GIAI ĐOẠN 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")

    # Embed Hình mô phỏng 2.5.3
    story.append(he.embed_figure_with_caption(
        fig_sim_schottky_iv,
        "Hình mô phỏng 2.5.3: So sánh đặc tuyến I–V của đi-ốt Schottky phát xạ ion nhiệt hạt đa số và đi-ốt p–n khuếch tán hạt thiểu số. "
        "Ba mắt xích vật lý: (a) Đặc tuyến dòng – áp tuyến tính thể hiện điện áp mở thuận của Schottky cực thấp (khoảng 0,25 V) so với đi-ốt p-n Silic (khoảng 0,70 V); "
        "(b) Đặc tuyến logarit mật độ dòng |<i>J</i>| thể hiện dòng bão hòa ngược của đi-ốt Schottky lớn hơn đi-ốt p-n từ 4 đến 6 bậc độ lớn; "
        "(c) Bản chất hạt đa số triệt tiêu hoàn toàn điện tích tích lũy khuếch tán hạt thiểu số, cho phép chuyển mạch ở tần số Gigahertz.",
        kind="sim",
        styles=styles
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 1 MPT 2.5.3
    story.append(he.build_intermediate_equation(
        "Thiết lập điều kiện cân bằng nhiệt động học tại điện áp bằng không <i>V</i> = 0:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Cân bằng hai dòng phát xạ nhiệt đối nghịch nhau tại trạng thái cân bằng:",
        r"J_{S \to M}(0) = J_{M \to S} = A^* T^2 \exp\left(-\frac{q \phi_{Bn}}{k_B T}\right) = J_s",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 2 MPT 2.5.3
    story.append(he.build_intermediate_equation(
        "Biến đổi dòng phát xạ thuận khi đặt điện áp ngoài phân cực <i>V</i>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tách số hạng điện áp phân cực ngoài ra khỏi dòng bão hòa nhiệt:",
        r"J_{S \to M}(V) = A^* T^2 \exp\left( -\frac{q (\phi_{Bn} - V)}{k_B T} \right) = J_s \exp\left( \frac{q V}{k_B T} \right)",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 3 MPT 2.5.3
    story.append(he.build_intermediate_equation(
        "Lấy hiệu số hai dòng thành phần để thu được phương trình dòng điện ròng chỉnh lưu Schottky:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Trừ dòng phát xạ từ kim loại sang bán dẫn không phụ thuộc điện áp:",
        r"J = J_{S \to M}(V) - J_{M \to S} = J_s \exp\left( \frac{q V}{k_B T} \right) - J_s = J_s \left[ \exp\left( \frac{q V}{k_B T} \right) - 1 \right]",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)

    # GIAI ĐOẠN 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Ưu thế động học chuyển mạch siêu cao tần của Đi-ốt Schottky: "
        "Trong tiếp giáp p–n, khi chuyển mạch từ trạng thái dẫn thuận sang trạng thái khóa ngược, một lượng điện tích hạt tải thiểu số khổng lồ "
        "(Diffusion Capacitance <i>C</i><sub>diff</sub>) đã bị tiêm vào hai bên vùng trung hòa. "
        "Linh kiện p–n bắt buộc phải mất một khoảng thời gian trễ hồi phục ngược (Reverse Recovery Time &tau;<sub>rr</sub> &sim; 10–100 ns) "
        "để các hạt thiểu số này tái hợp hết hoặc bị rút ngược trở lại. "
        "Ngược lại, đi-ốt Schottky là linh kiện hạt đa số (Majority-carrier Device): dòng điện chỉ do electron dẫn trong vùng dẫn tạo thành. "
        "Khi ngắt điện áp thuận, không hề có sự tích tụ điện tích hạt thiểu số (<i>Q</i><sub>diff</sub> &approx; 0). "
        "Thời gian chuyển mạch của đi-ốt Schottky chỉ bị giới hạn bởi thời gian nạp xả điện dung miền nghèo tiếp xúc (<i>R</i><sub>s</sub><i>C</i><sub>j</sub> &sim; 1–10 ps), "
        "cho phép vận hành ổn định ở tần số vi ba siêu cao (hàng chục đến hàng trăm Gigahertz).<br/>"
        "Đánh đổi kỹ thuật (Engineering Trade-off): "
        "Dù sở hữu điện áp rơi thuận rất thấp (khoảng 0,25 V giúp giảm suy hao công suất đóng cắt) và tốc độ đáp ứng siêu nhanh, "
        "đi-ốt Schottky có nhược điểm chí mạng là dòng bão hòa ngược <i>J</i><sub>s</sub> lớn hơn đi-ốt p–n từ 10.000 đến 1.000.000 lần, "
        "đồng thời điện áp đánh thủng ngược thấp hơn do hiệu ứng tập trung điện trường tại biên kim loại."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.5.4: HIỆU ỨNG HẠ THẤP RÀO THẾ DO LỰC ẢNH SCHOTTKY
    # =========================================================================
    add_p("Luận điểm 2.5.4: Hiệu ứng hạ thấp rào thế do lực ảnh điện tích Schottky (Image Force Lowering)", "H2")
    add_spacer(4)

    # GIAI ĐOẠN 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong các phân tích lý thuyết ở Luận điểm 2.5.1 đến 2.5.3, chiều cao rào thế năng <i>q&phi;</i><sub>Bn</sub> được giả thiết là một hằng số cố định "
        "chỉ phụ thuộc vào công thoát kim loại và độ ái lực điện tử của bán dẫn. "
        "Tuy nhiên trong thực tế thực nghiệm, chiều cao rào thế năng đo được luôn nhỏ hơn giá trị lý thuyết và có xu hướng giảm dần khi tăng điện trường tiếp xúc. "
        "Hiện tượng vật lý này được gọi là Hiệu ứng Schottky hay Sự hạ thấp rào thế do lực ảnh điện tích (Image Force Lowering).<br/>"
        "↳ Lực ảnh điện tích (Image Force): Khi một electron mang điện tích âm &minus;<i>q</i> nằm trong bán dẫn ở khoảng cách <i>x</i> cách bề mặt kim loại, "
        "nó sẽ cảm ứng trên bề mặt kim loại một sự tái phân bố điện tích dương. "
        "Theo phương pháp ảnh điện trong tĩnh điện học Maxwell, toàn bộ các điện tích cảm ứng phức tạp trên bề mặt dẫn điện lý tưởng có thể thay thế tương đương "
        "bằng một điện tích ảnh dương +<i>q</i> nằm đối xứng tại vị trí &minus;<i>x</i> bên trong kim loại.<br/>"
        "Lực hút Coulomb giữa electron và điện tích ảnh kéo electron về phía kim loại, làm biến dạng profile thế năng và kéo đỉnh rào cản tụt xuống."
    )
    add_spacer(6)

    # GIAI ĐOẠN 2
    add_p("Giai đoạn 2: Ví dụ tối giản và trực giác cơ học (Minimal Example & Mechanical Intuition)", "H3")
    nom_rows_2_5_4 = [
        ("Vị trí đỉnh rào thế năng", "<i>x</i><sub>m</sub>", "nm", "Khoảng cách từ mặt phân cách kim loại đến vị trí thế năng đạt giá trị cực đại."),
        ("Độ hạ thấp rào thế năng", "<i>&Delta;&phi;</i><sub>B</sub>", "V", "Độ suy giảm của chiều cao rào thế Schottky do tương tác lực ảnh điện tích Coulomb."),
        ("Hằng số điện môi bán dẫn", "<i>&epsilon;</i><sub>s</sub>", "F·cm<sup>-1</sup>", "Độ điện thẩm tuyệt đối của chất bán dẫn ở tần số quang học (xấp xỉ 11,7 &epsilon;₀ trong Si)."),
        ("Điện trường tại mặt tiếp xúc", "<i>E</i>", "V·cm<sup>-1</sup>", "Cường độ điện trường tiếp xúc lớn nhất tại mặt phân cách kim loại – bán dẫn trong miền nghèo.")
    ]
    story.append(he.build_target_equation_block(
        r"x_m = \sqrt{\frac{q}{16 \pi \varepsilon_s E}}, \qquad \Delta \phi_B = \sqrt{\frac{q E}{4 \pi \varepsilon_s}}",
        nom_rows_2_5_4,
        styles=styles
    ))
    add_spacer(8)

    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng bạn đang leo lên một ngọn đồi dốc ngược (rào thế năng do điện trường tiếp xúc <i>E</i> tạo ra). "
        "Tuy nhiên, trên đỉnh đồi có một chiếc nam châm cực mạnh gắn vào lưng bạn, còn dưới chân dốc có một tấm kim loại hút chặt lấy nam châm (lực ảnh điện tích). "
        "Càng đứng gần chân dốc, lực hút ngược về phía sau càng khủng khiếp (tỷ lệ nghịch với bình phương khoảng cách <i>x</i><sup>2</sup>). "
        "Khi bạn cố gắng bước xa dần khỏi chân dốc, lực hút yếu dần trong khi thế năng leo dốc tăng lên. "
        "Sự giằng co giữa lực hút lùi về chân dốc và độ dốc ngọn đồi tạo nên một đỉnh đồi mới nằm ở vị trí <i>x</i><sub>m</sub>. "
        "Đỉnh đồi mới này thấp hơn đỉnh đồi ban đầu một khoảng <i>&Delta;&phi;</i><sub>B</sub>. "
        "Điện trường ngoài kéo dốc càng mạnh, đỉnh đồi càng bị kéo sụp xuống thấp và dịch chuyển sát lại gần chân dốc hơn."
    )
    add_spacer(10)

    # GIAI ĐOẠN 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")

    # Embed Hình mô phỏng 2.5.2
    story.append(he.embed_figure_with_caption(
        fig_sim_image_force,
        "Hình mô phỏng 2.5.2: Giản đồ thế năng không gian và hiệu ứng hạ thấp rào thế do lực ảnh điện tích Schottky (Image Force Lowering). "
        "Ba mắt xích vật lý: (a) Giản đồ thế năng tổng hợp <i>V</i>(<i>x</i>) theo khoảng cách <i>x</i> thể hiện đỉnh rào thế bị kéo sụp xuống và dịch chuyển về phía kim loại; "
        "(b) Độ hạ thấp rào thế <i>&Delta;&phi;</i><sub>B</sub> (từ 10 meV đến 80 meV) tỷ lệ thuận với căn bậc hai của điện trường tiếp xúc <i>E</i>; "
        "(c) Vị trí cực đại <i>x</i><sub>m</sub> dịch chuyển từ 10 nm về sát dưới 2 nm khi điện trường tăng lên thang 100 kV/cm.",
        kind="sim",
        styles=styles
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 1 MPT 2.5.4
    story.append(he.build_intermediate_equation(
        "Xác định lực hút ảnh điện tích Coulomb và thế năng lực ảnh tương ứng:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Áp dụng định luật Coulomb giữa electron và điện tích ảnh dương cách nhau cự ly 2x:",
        r"F(x) = -\frac{q^2}{4 \pi \varepsilon_s (2x)^2} = -\frac{q^2}{16 \pi \varepsilon_s x^2} \implies V_{\mathrm{image}}(x) = \int_\infty^x F(x') \mathrm{d}x' = -\frac{q^2}{16 \pi \varepsilon_s x}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 2 MPT 2.5.4
    story.append(he.build_intermediate_equation(
        "Thiết lập hàm thế năng tổng hợp và tìm vị trí cực đại thế năng d<i>V</i>/d<i>x</i> = 0:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Lấy đạo hàm triệt tiêu lực tổng hợp giữa lực ảnh và lực điện trường tiếp xúc:",
        r"\frac{\mathrm{d} V(x)}{\mathrm{d}x} = \frac{q^2}{16 \pi \varepsilon_s x^2} - q E = 0 \implies x_m = \sqrt{\frac{q}{16 \pi \varepsilon_s E}}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(6)

    # Bước biến đổi trung gian 3 MPT 2.5.4
    story.append(he.build_intermediate_equation(
        "Thay tọa độ đỉnh <i>x</i><sub>m</sub> vào thế năng tổng hợp để xác định độ hạ thấp rào thế toàn phần:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tính độ hụt rào thế hiệu dụng Δ<i>φ</i><sub>B</sub> = −<i>V</i>(<i>x</i><sub>m</sub>) · <i>q</i><sup>−1</sup> tại vị trí cực đại:",
        r"\Delta \phi_B = -\frac{V(x_m)}{q} = \frac{q}{16 \pi \varepsilon_s x_m} + E x_m = 2 E x_m = 2 E \sqrt{\frac{q}{16 \pi \varepsilon_s E}} = \sqrt{\frac{q E}{4 \pi \varepsilon_s}}",
        styles=styles,
        ocr_idx=4,
        is_expanded_from_slide=True
    ))
    add_spacer(8)

    # GIAI ĐOẠN 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Hệ quả kỹ thuật của hiệu ứng hạ thấp rào thế do lực ảnh: "
        "Trong chế độ phân cực ngược (<i>V</i><sub>R</sub> &gt; 0), điện trường tại mặt tiếp xúc tăng lên theo căn bậc hai của điện áp ngược "
        "<i>E</i> ∝ (<i>V</i><sub>bi</sub> + <i>V</i><sub>R</sub>)<sup>0,5</sup>. "
        "Điều này dẫn đến hệ quả là độ hạ thấp rào thế Δ<i>φ</i><sub>B</sub> tăng lên khi tăng điện áp ngược. "
        "Do đó, chiều cao rào cản thực tế <i>q</i><i>φ</i><sub>B,eff</sub> = <i>q</i><i>φ</i><sub>B0</sub> − <i>q</i>Δ<i>φ</i><sub>B</sub> bị suy giảm liên tục. "
        "Hệ quả là dòng bão hòa ngược <i>J</i><sub>s</sub> của đi-ốt Schottky không bao giờ bão hòa nằm ngang tuyệt đối như đi-ốt p–n, "
        "mà từ từ tăng dần theo điện áp ngược cho đến khi xảy ra hiện tượng đánh thủng.<br/>"
        "Sai lệch hệ số lý tưởng <i>n</i> &gt; 1 trong chế độ phân cực thuận: "
        "Do rào thế năng <i>q</i><i>φ</i><sub>B</sub> phụ thuộc vào điện trường <i>E</i>, mà <i>E</i> lại phụ thuộc vào điện áp đặt <i>V</i>, "
        "độ cao rào thế năng bị biến điệu nhẹ ngay cả khi phân cực thuận. "
        "Sự biến thiên này làm tốc độ tăng của dòng thuận hơi chậm hơn so với hàm mũ lý tưởng, khiến hệ số lý tưởng <i>n</i> trong thực tế "
        "thường nằm trong khoảng 1,02 đến 1,08 thay vì bằng 1,00."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI 5: THỬ THÁCH CHẨN ĐOÁN CER (GIAI ĐOẠN 5)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện và dự đoán lỗi sai kỹ thuật (Student Challenges & Error Anticipation)", "H2")
    add_spacer(6)

    add_p(
        "Khối thử thách chẩn đoán độc lập (Claim – Evidence – Reasoning): Bẫy điểm mù kỹ thuật thực chiến trong Lab và thiết kế quang điện tử. "
        "Hai ca chẩn đoán thực tế dưới đây yêu cầu vận dụng nguyên lý đầu và các công thức giải tích vi mô đã dẫn xuất để phát hiện sai sót thiết kế."
    )
    add_spacer(8)

    # CA CHẨN ĐOÁN 2.5-A
    add_p(
        "<b>Ca chẩn đoán 2.5-A: Bẫy điểm mù sai số hằng số Richardson <i>A</i>* khi trích xuất rào thế Schottky trong Lab.</b><br/>"
        "Trong một bài thực hành tại Lab Vật lý Bán dẫn, một nhóm sinh viên tiến hành đo đạc đặc tuyến <i>I</i>–<i>V</i> ở nhiệt độ phòng (300 K) "
        "của một đi-ốt tiếp xúc Schottky chế tạo trên thanh Silic loại n (diện tích tiếp xúc <i>S</i> = 10<sup>−3</sup> cm<sup>2</sup>). "
        "Từ dòng thuận ở điện áp nhỏ, nhóm trích xuất được dòng bão hòa <i>I</i><sub>s</sub> = 2 × 10<sup>−10</sup> A (tương ứng <i>J</i><sub>s</sub> = 2 × 10<sup>−7</sup> A/cm<sup>2</sup>). "
        "Để tính chiều cao rào thế <i>q</i><i>φ</i><sub>Bn</sub>, sinh viên áp dụng công thức: <i>q</i><i>φ</i><sub>Bn</sub> = <i>k</i><sub>B</sub><i>T</i> ln(<i>A</i>* <i>T</i><sup>2</sup> · <i>J</i><sub>s</sub><sup>−1</sup>). "
        "Tuy nhiên, do nhầm lẫn, sinh viên đã tra cứu và sử dụng hằng số Richardson trong chân không <i>A</i><sub>0</sub> = 120 A·cm<sup>−2</sup>·K<sup>−2</sup> "
        "thay vì hằng số hiệu dụng của Silic.<br/>"
        "Một sinh viên khác cho rằng sai số này sẽ làm sai lệch nghiêm trọng kết quả đo chiều cao rào thế và yêu cầu hủy kết quả.<br/>"
        "↳ <i>Thử thách CER:</i> Hãy tính toán chính xác sai số tuyệt đối của chiều cao rào thế δ(<i>q</i><i>φ</i><sub>Bn</sub>) gây ra bởi sự nhầm lẫn giữa <i>A</i><sub>0</sub> "
        "và <i>A</i>* của Silic (<i>A</i>* ≈ 112 A·cm<sup>−2</sup>·K<sup>−2</sup>), và đối với GaAs (<i>A</i>* ≈ 8,16 A·cm<sup>−2</sup>·K<sup>−2</sup>). "
        "Giải thích tại sao phép đo trích xuất rào thế bằng đặc tuyến <i>I</i>–<i>V</i> đơn nhiệt độ lại có độ nhạy rất thấp đối với sai số của hằng số <i>A</i>*, "
        "trong khi phương pháp đồ thị Richardson đa nhiệt độ lại có khả năng trích xuất chính xác đồng thời cả hai tham số."
    )
    add_spacer(10)

    # CA CHẨN ĐOÁN 2.5-B
    add_p(
        "<b>Ca chẩn đoán 2.5-B: Bẫy trôi dòng rò ngược do lực ảnh điện tích trong Đi-ốt Schottky công suất cao (Power SBD).</b><br/>"
        "Một kỹ sư R&amp;D thiết kế đi-ốt Schottky công suất cao phục vụ bộ nguồn xung chuyển mạch SMPS 100 kHz. "
        "Kỹ sư lựa chọn bán dẫn Silic pha tạp loại n với nồng độ donor <i>N</i><sub>D</sub> = 5 × 10<sup>16</sup> cm<sup>−3</sup> để đạt điện trở thuần nhỏ. "
        "Chiều cao rào thế phẳng lý tưởng là <i>q</i><i>φ</i><sub>B0</sub> = 0,75 eV. "
        "Kỹ sư tính toán dòng rò ngược danh định ở điện áp ngược <i>V</i><sub>R</sub> = 40 V dựa trên công thức bão hòa lý tưởng không đổi <i>J</i><sub>s0</sub>.<br/>"
        "Khi đo kiểm nghiệm thực tế trên máy đo đặc tuyến đường cong (Curve Tracer) ở 40 V ngược, dòng rò thực tế đo được cao gấp hơn 4 lần so với tính toán lý thuyết ban đầu, "
        "làm linh kiện phát nhiệt mạnh và có nguy cơ thoát nhiệt (Thermal Runaway).<br/>"
        "↳ <i>Thử thách CER:</i> Tính toán cường độ điện trường cực đại tại mặt tiếp xúc <i>E</i><sub>max</sub> ở điện áp ngược <i>V</i><sub>R</sub> = 40 V "
        "cho nồng độ pha tạp đã cho (cho biết <i>V</i><sub>bi</sub> ≈ 0,65 V). "
        "Xác định độ hạ thấp rào thế Δ<i>φ</i><sub>B</sub> do lực ảnh điện tích Schottky gây ra. "
        "Chứng minh rằng tỷ số tăng dòng rò ngược exp[<i>q</i>Δ<i>φ</i><sub>B</sub> · (<i>k</i><sub>B</sub><i>T</i>)<sup>−1</sup>] giải thích chính xác hiện tượng dòng rò tăng gấp 4 lần "
        "mà kỹ sư gặp phải trong phòng Lab.<br/>"
        "Đề xuất giải pháp kiến trúc linh kiện để khắc phục (như cấu trúc đi-ốt rào Schottky tiếp giáp JBS — Junction Barrier Schottky)."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI PHẢN BIỆN LAB VÀ ĐỐI TRỌNG TRI THỨC
    # =========================================================================
    add_p(
        "<b>[Đối trọng phản biện nguyên lý đầu — Peer-level Lab Partner]:</b> "
        "Trong toàn bộ dẫn xuất của lý thuyết phát xạ ion nhiệt của Bethe, chúng ta giả thiết rằng các electron có động năng <i>v</i><sub>x</sub> &ge; <i>v</i><sub>0x</sub> "
        "khi bay đến ranh giới sẽ đi thẳng vào kim loại với xác suất truyền qua bằng 100% mà không bị tán xạ trở lại. "
        "Tuy nhiên trong thực tế cơ học lượng tử, ranh giới tiếp xúc giữa mạng tinh thể bán dẫn tuần hoàn và mạng kim loại vô định hình / đa tinh thể "
        "tạo nên một bước nhảy thế năng đột ngột kèm theo sự không tương thích về hàm sóng điện tử Bloch.<br/>"
        "↳ <i>Câu hỏi đối trọng:</i> Dưới tác động của sự phản xạ lượng tử cơ học sóng (Quantum Mechanical Reflection) tại bước nhảy thế năng ranh giới, "
        "và hiện tượng electron phát xạ bị tán xạ va chạm với phonon quang ngay tại miền đỉnh rào thế (Optical Phonon Backscattering) dội ngược trở lại bán dẫn, "
        "hằng số Richardson hiệu dụng <i>A</i>* thực tế bị suy giảm đi bao nhiêu phần trăm? "
        "Tại sao trong các mô hình công nghiệp TCAD hiện đại (như Synopsys Sentaurus), người ta bắt buộc phải đưa vào hệ số truyền qua bề mặt <i>f</i><sub>p</sub> &sim; 0,5–0,85?"
    )

    doc.build(story)
    print(f"SUCCESS: Generated {TARGET_PDF_PATH}")
    assert_result = he.assert_monograph_compliance(TARGET_PDF_PATH, story, require_5_blocks=True, min_pages=12)
    print(f"POST-BUILD ASSERTION PASS 100%: {assert_result}")
    return TARGET_PDF_PATH


if __name__ == "__main__":
    build_monograph_muc_2_5()

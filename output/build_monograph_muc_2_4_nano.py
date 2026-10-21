# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Chương 2: Bản chất lượng tử của thế giới nano
Mục 2.4: Phổ năng lượng của các hệ hạt lượng tử (Nguyên tử & Phân tử)
Sinh viên: Bùi Trung Dũng (ĐHBK Hà Nội - HUST)
"""

import os
import sys
import tempfile
import shutil

# Thêm đường dẫn thư viện hust_pdf_engine
engine_dir = r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts"
if engine_dir not in sys.path:
    sys.path.insert(0, engine_dir)

import hust_pdf_engine as he
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib import colors

sys.stdout.reconfigure(encoding="utf-8")

def build_pdf():
    # 1. Đường dẫn thư mục & tệp đích
    drive_base = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano"
    kho_anh = os.path.join(drive_base, "Kho_Hinh_Anh")
    bai_giang = os.path.join(drive_base, "Bai_Giang_Dong_Goi")
    os.makedirs(bai_giang, exist_ok=True)
    target_pdf = os.path.join(bai_giang, "Chuyen_Khao_Nano_Muc_2.4.pdf")

    print(f"Bắt đầu biên dịch chuyên khảo Mục 2.4: {target_pdf}")

    # 2. Khởi tạo Styles và Document Template
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(target_pdf)
    story = []

    # =========================================================================
    # TIÊU ĐỀ ĐẦU CHUYÊN KHẢO (H1)
    # =========================================================================
    title_main = (
        "CHƯƠNG 2: BẢN CHẤT LƯỢNG TỬ CỦA THẾ GIỚI NANO<br/>"
        "MỤC 2.4: PHỔ NĂNG LƯỢNG CỦA CÁC HỆ HẠT LƯỢNG TỬ (NGUYÊN TỬ &amp; PHÂN TỬ)"
    )
    story.append(he.make_paragraph(title_main, styles["H1"]))
    story.append(Spacer(1, 4))

    meta_info = (
        "<b>Hệ Thống Chuyên Khảo Giảng Dạy &amp; Nghiên Cứu Vật Lý Nano — ĐHBK Hà Nội</b><br/>"
        "<i>Chủ thể nghiên cứu:</i> Bùi Trung Dũng — Khoa Vật lý Kỹ thuật, Trường Đại học Bách khoa Hà Nội (HUST)<br/>"
        "<i>Tài liệu nguồn kép:</i> Bài giảng 'Bài 2-Quantum nature.pdf' (Slide 28–53), Bộ môn Vật liệu Điện tử — HUST; "
        "kết hợp các chuyên khảo quốc tế đỉnh cao: Griffiths (<i>Introduction to Quantum Mechanics</i>), Sze (<i>Physics of Semiconductor Devices</i>), "
        "Saleh &amp; Teich (<i>Fundamentals of Photonics</i>), Herzberg (<i>Molecular Spectra and Molecular Structure</i>)."
    )
    story.append(he.make_paragraph(meta_info, styles["Body"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=he.COLOR_PRIMARY, spaceBefore=4, spaceAfter=10))

    # =========================================================================
    # LỜI NÓI ĐẦU ĐỊNH VỊ HỌC THUẬT & TỔNG QUAN
    # =========================================================================
    overview_text = (
        "<b>Lời nói đầu định vị học thuật:</b> Trong cơ học lượng tử và vật lý nano, phổ năng lượng của các hệ hạt vi mô "
        "chính là chìa khóa then chốt mở ra bản chất cấu trúc của thế giới vật chất. Khác biệt hoàn toàn với cơ học cổ điển "
        "nơi năng lượng của hạt mang tính chất biến thiên liên tục, các hệ vi mô bị giam cầm trong trường thế Coulomb của hạt nhân "
        "(như nguyên tử) hoặc trường thế liên kết hóa học (như phân tử) đều sở hữu phổ năng lượng bị lượng tử hóa thành các mức rời rạc. "
        "Đối với nguyên tử Hydro — hệ lượng tử hai hạt duy nhất giải được giải tích chính xác tuyệt đối — nghiệm của phương trình Schrödinger "
        "trong tọa độ cầu dẫn tới bộ ba số lượng tử không gian (<i>n</i>, <i>l</i>, <i>m<sub>l</sub></i>) phản ánh đối xứng cầu hoàn hảo. "
        "Khi bổ sung thuộc tính spin nội tại của electron (<i>m<sub>s</sub></i>), hệ bốn số lượng tử xác định duy nhất trạng thái một hạt, "
        "đặt nền móng cho Nguyên lý loại trừ Pauli, quy tắc Aufbau và các quy tắc Hund chi phối toàn bộ bảng tuần hoàn các nguyên tố hóa học. "
        "Bước sang hệ phân tử, sự phân tách ba thang bậc thời gian và năng lượng theo Xấp xỉ Born – Oppenheimer dẫn tới cấu trúc phổ dải "
        "bao gồm dải điện tử, dao động và quay, phản ánh hình học và động học liên kết hạt nhân ở quy mô hạ nanomet. "
        "Chuyên khảo Mục 2.4 triển khai trọn vẹn 5 Luận điểm Vi mô (MPT) theo chuẩn mực sư phạm 5 giai đoạn lũy tiến, "
        "dẫn xuất tường minh từng phương trình từ nguyên lý đầu và minh họa bằng đồ thị giải tích kỹ thuật chuẩn MATLAB R2014b+."
    )
    story.append(he.make_paragraph(overview_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # =========================================================================
    # LUẬN ĐIỂM 2.4.1: BÀI TOÁN NGUYÊN TỬ HYDRO & PHƯƠNG PHÁP TÁCH BIẾN CẦU
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.4.1: Bài toán nguyên tử hydro &amp; Phương pháp tách biến trong tọa độ cầu", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g1_p1 = (
        "Nguyên tử Hydro và các ion đồng dạng một electron (He<sup>+</sup>, Li<sup>2+</sup>, Be<sup>3+</sup>) là mô hình chuẩn mực "
        "kinh điển trong vật lý lượng tử. Hệ bao gồm hạt nhân mang điện tích dương +<i>Z·e</i> (với <i>Z</i> = 1 đối với Hydro) "
        "và một electron mang điện tích −<i>e</i> chuyển động trong trường lực tĩnh điện Coulomb. Do khối lượng hạt nhân <i>M</i> "
        "lớn hơn khối lượng electron <i>m</i> xấp xỉ 1836 lần, hạt nhân có thể được coi là đứng yên tại gốc tọa độ, hoặc chính xác hơn, "
        "hệ quy về chuyển động của một giả hạt có khối lượng rút gọn <i>μ</i> xấp xỉ bằng <i>m</i> (với <i>m</i> &lt;&lt; <i>M</i>).<br/>"
        "Thế năng tương tác Coulomb giữa electron và hạt nhân chỉ phụ thuộc duy nhất vào khoảng cách xuyên tâm <i>r</i>:<br/>"
        "thế Coulomb hút <i>U</i>(<i>r</i>) tỉ lệ nghịch với khoảng cách xuyên tâm <i>r</i>.<br/>"
        "Do thế năng có tính đối xứng cầu hoàn hảo, việc giải phương trình Schrödinger trong hệ tọa độ Descartes (<i>x</i>, <i>y</i>, <i>z</i>) "
        "sẽ làm mất đi tính đối xứng tự nhiên của bài toán. Thay vào đó, việc chuyển sang hệ tọa độ cầu (<i>r</i>, <i>θ</i>, <i>φ</i>) "
        "cho phép tách biệt hoàn toàn chuyển động hướng kính (radial) khỏi chuyển động góc (angular), từ đó tìm ra nghiệm giải tích dạng giải tích đóng."
    )
    story.append(he.make_paragraph(g1_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 01: Cấu trúc nguyên tử Hydro & tọa độ cầu
    img_h01 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_01_Cau_Truc_Nguyen_Tu_Hydro.png")
    cap_h01 = "Hình 2.4.1: Mô hình tương tác tĩnh điện Coulomb giữa electron và hạt nhân trong hệ tọa độ cầu (r, θ, φ)."
    story.append(he.embed_figure_with_caption(img_h01, cap_h01, kind="orig", styles=styles))

    # 5 Mắt xích OCR cho Hình 2.4.1
    h01_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Sơ đồ không gian 3 chiều biểu diễn hạt nhân mang điện tích +ze tại gốc tọa độ O và electron −e tại vị trí bán kính r với góc cực θ và góc phương vị φ."
    h01_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Khoảng cách hướng kính r đo bằng mét (hoặc Ångström Å, bán kính Bohr a<sub>0</sub>); góc cực θ ∈ [0, π] rad; góc phương vị φ ∈ [0, 2π] rad."
    h01_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Lực Coulomb hút tĩnh điện lực hút Coulomb F(r) tỉ lệ nghịch với r<sup>2</sup> hướng về gốc tâm, tạo nên hố thế năng Coulomb đối xứng cầu U(r) tỉ lệ nghịch với r."
    h01_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Tính đẳng hướng không gian của thế Coulomb bảo toàn toán tử vectơ momen động lượng toàn phần L, cho phép giao hoán đồng thời [H, L<sup>2</sup>] = 0 và [H, L<sub>z</sub>] = 0."
    h01_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Điểm kỳ dị tại r = 0 của thế Coulomb được cân bằng bởi số hạng thế năng ly tâm lực ly tâm tỉ lệ nghịch với r<sup>2</sup> khi l > 0, ngăn electron rơi thẳng vào hạt nhân."
    story.append(he.make_paragraph(h01_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h01_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h01_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h01_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h01_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh gốc 02: Hàm sóng hướng kính và mật độ xác suất
    img_h02 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_02_Mat_Do_Xac_Suat_Huong_Kinh_Hydro.png")
    cap_h02 = "Hình 2.4.2: Đồ thị hàm sóng hướng kính R(r) và hàm mật độ xác suất hướng kính r<sup>2</sup>R<sup>2</sup>(r) của Hydro (Slide 33)."
    story.append(he.embed_figure_with_caption(img_h02, cap_h02, kind="orig", styles=styles))

    h02_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Đồ thị so sánh giữa biên độ hàm sóng hướng kính R<sub>nl</sub>(r) và hàm mật độ xác suất tìm thấy hạt trong vỏ cầu P(r) = r<sup>2</sup>|R<sub>nl</sub>(r)|<sup>2</sup>."
    h02_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Trục hoành là khoảng cách r theo đơn vị bán kính Bohr a<sub>0</sub>; trục tung là mật độ xác suất P(r) theo đơn vị a<sub>0</sub><sup>−1</sup>."
    h02_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Hàm 1s có biên độ cực đại tại r = 0 nhưng mật độ xác suất P<sub>1s</sub>(r) triệt tiêu tại r = 0 do thừa số diện tích r<sup>2</sup> và đạt đỉnh cực đại tại đúng r = a<sub>0</sub>."
    h02_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Trạng thái 2s có một điểm nút hướng kính tại r = 2a<sub>0</sub> nơi mật độ xác suất bằng 0, chia không gian thành vùng xuyên thấu lõi và vùng mây điện tử vỏ ngoài."
    h02_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Trạng thái 2p không có nút hướng kính, cực đại xác suất xuất hiện tại r = 4a<sub>0</sub>, nằm xa hạt nhân hơn so với đỉnh cực đại phụ của trạng thái 2s."
    story.append(he.make_paragraph(h02_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h02_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h02_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h02_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h02_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 8))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g1_p2 = (
        "<b>Hạt nhân phương trình vi phân tọa độ cầu:</b> Toán tử vi phân Laplace ∇<sup>2</sup> trong tọa độ cầu được phân tách thành các thành phần vi phân hướng kính và thành phần đạo hàm góc cực cùng góc phương vị.<br/>Phương trình Schrödinger dừng tổng quát viết cho thế Coulomb:<br/>"
        "∇<sup>2</sup>Ψ + thành phần động năng kết hợp thế hút Coulomb·Ψ = 0.<br/>"
        "Phương pháp tách ly biến số giả định hàm sóng toàn phần có dạng tích độc lập:<br/>"
        "Ψ(<i>r</i>, <i>θ</i>, <i>φ</i>) = <i>R</i>(<i>r</i>)·<i>Θ</i>(<i>θ</i>)·<i>Φ</i>(<i>φ</i>) = <i>R</i>(<i>r</i>)·<i>Y</i>(<i>θ</i>, <i>φ</i>).<br/>"
        "Thay dạng tích này vào phương trình Schrödinger và chia hai vế cho Ψ, ta tách bài toán thành ba phương trình vi phân thường độc lập, "
        "kết nối với nhau qua hai hằng số tách ly: <i>m<sub>l</sub></i><sup>2</sup> (đặc trưng cho hình chiếu momen quỹ đạo) "
        "và <i>λ</i> = <i>l</i>(<i>l</i> + 1) (đặc trưng cho bình phương độ lớn momen quỹ đạo)."
    )
    story.append(he.make_paragraph(g1_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    # Trình bày phương trình cốt lõi & Bảng danh pháp MPT 2.4.1
    eq_hydro = r"E_n = -\frac{m Z^2 e^4}{32 \pi^2 \varepsilon_0^2 \hbar^2} \frac{1}{n^2} = -\frac{13.6 Z^2}{n^2} \text{ [eV]}"
    nom_hydro = [
        ("Mức năng lượng Bohr", "<i>E<sub>n</sub></i>", "eV", "Năng lượng lượng tử hóa của electron trong nguyên tử Hydro"),
        ("Số lượng tử chính", "<i>n</i>", "1", "Xác định kích thước orbital và mức năng lượng cơ bản (<i>n</i> = 1, 2, 3...)"),
        ("Số điện tích hạt nhân", "<i>Z</i>", "1", "Điện tích hạt nhân tính theo đơn vị điện tích nguyên tố (<i>Z</i> = 1)"),
        ("Khối lượng nghỉ electron", "<i>m</i>", "kg", "Khối lượng quán tính của electron (9.1093837 × 10<sup>−31</sup> kg)"),
        ("Điện tích nguyên tố", "<i>e</i>", "C", "Độ lớn điện tích cơ bản (1.602176634 × 10<sup>−19</sup> C)"),
        ("Hằng số điện môi chân không", "<i>ε</i><sub>0</sub>", "F/m", "Độ thấm điện chân không (8.8541878 × 10<sup>−12</sup> F/m)"),
        ("Hằng số Planck rút gọn", "ħ", "J·s", "Lượng tử tác dụng (1.0545718 × 10<sup>−34</sup> J·s)")
    ]
    story.append(he.build_target_equation_block(eq_hydro, nom_hydro, styles=styles))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step1_text = (
        "<b>Bước 1: Tách phương trình góc phương vị Φ(φ) và điều kiện đơn trị tuần hoàn:</b><br/>"
        "Từ toán tử vi phân góc <i>φ</i>, phương trình thành phần có dạng vi phân điều hòa bậc hai. "
        "Để hàm sóng là một hàm giải tích đơn trị trong toàn bộ không gian, giá trị hàm sóng tại <i>φ</i> và <i>φ</i> + 2<i>π</i> "
        "bắt buộc phải trùng nhau hoàn toàn: Φ(<i>φ</i> + 2<i>π</i>) = Φ(<i>φ</i>). "
        "Điều kiện biên này lượng tử hóa hằng số biến đổi thành một số nguyên <i>m<sub>l</sub></i>."
    )
    step1_eq = r"\frac{d^2\Phi}{d\varphi^2} = -m_l^2 \Phi \quad \Longrightarrow \quad \Phi(\varphi) = \frac{1}{\sqrt{2\pi}} e^{i m_l \varphi}, \quad m_l \in \{0, \pm 1, \pm 2, \dots\}"
    story.append(he.build_intermediate_equation(step1_text, step1_eq, styles=styles, is_expanded_from_slide=True))

    step2_text = (
        "<b>Bước 2: Tách phương trình góc cực Θ(θ) và phương trình Legendre liên kết:</b><br/>"
        "Phương trình góc <i>θ</i> liên hệ với hằng số tách ly <i>λ</i>. "
        "Đổi biến <i>u</i> = cos<i>θ</i> (với −1 ≤ <i>u</i> ≤ 1), phương trình chuyển thành phương trình vi phân Legendre liên kết. "
        "Để nghiệm không bị phân kỳ vô hạn tại hai điểm cực <i>θ</i> = 0 và <i>θ</i> = <i>π</i> (tương ứng <i>u</i> = ±1), "
        "chuỗi nghiệm buộc phải ngắt thành một đa thức hữu hạn. Điều kiện này đòi hỏi <i>λ</i> = <i>l</i>(<i>l</i> + 1) "
        "với <i>l</i> là một số nguyên không âm và |<i>m<sub>l</sub></i>| ≤ <i>l</i>."
    )
    step2_eq = r"\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta \frac{d\Theta}{d\theta}\right) + \left[ l(l+1) - \frac{m_l^2}{\sin^2\theta} \right]\Theta = 0 \quad \Longrightarrow \quad \Theta(\theta) \propto P_l^{|m_l|}(\cos\theta)"
    story.append(he.build_intermediate_equation(step2_text, step2_eq, styles=styles, is_expanded_from_slide=True))

    step3_text = (
        "<b>Bước 3: Giải phương trình hướng kính R(r) và xác định phổ năng lượng rời rạc:</b><br/>"
        "Phương trình hướng kính chứa thế hiệu dụng bao gồm thế Coulomb hút và thế đẩy ly tâm. "
        "Khảo sát hành vi tiệm cận: Khi <i>r</i> → 0, <i>R</i>(<i>r</i>) tỉ lệ với <i>r<sup>l</sup></i>; khi <i>r</i> → ∞, <i>R</i>(<i>r</i>) tắt dần theo hàm mũ exp(−<i>κ·r</i>). "
        "Biểu diễn nghiệm dưới dạng tích của hàm mũ và đa thức Laguerre liên kết. "
        "Để hàm sóng chuẩn hóa được bình phương khả tích (không bùng nổ ra vô cùng), chuỗi Laguerre phải ngắt tại bậc hữu hạn, "
        "dẫn tới sự xuất hiện của số lượng tử chính <i>n</i> = <i>n<sub>r</sub></i> + <i>l</i> + 1 và công thức năng lượng Bohr."
    )
    step3_eq = r"\frac{d}{dr}\left(r^2 \frac{dR}{dr}\right) + \frac{2m r^2}{\hbar^2} \left[ E + \frac{Z e^2}{4\pi\varepsilon_0 r} - \frac{l(l+1)\hbar^2}{2m r^2} \right] R = 0"
    story.append(he.build_intermediate_equation(step3_text, step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g1_p4 = (
        "<b>Khảo sát tiệm cận năng lượng liên tục (<i>E</i> &gt; 0):</b> Khi năng lượng của hệ dương (<i>E</i> &gt; 0), "
        "hạt electron sở hữu động năng vượt qua thế rào Coulomb và hoàn toàn tự do thoát khỏi sự giam cầm của hạt nhân. "
        "Phương trình vi phân hướng kính khi đó có nghiệm giải tích hữu hạn với mọi giá trị <i>E</i>, phổ năng lượng là phổ liên tục, "
        "tương ứng với quá trình tán xạ electron trên trường Coulomb của ion (hiện tượng bức xạ hãm Bremsstrahlung).<br/>"
        "<b>Khảo sát trạng thái liên kết (<i>E</i> &lt; 0):</b> Khi electron bị bẫy trong hố thế (<i>E</i> &lt; 0), "
        "điều kiện biên chuẩn hóa bình phương khả tích ∫|Ψ|<sup>2</sup><i>dV</i> = 1 áp đặt điều kiện ngắt chuỗi nghiêm ngặt. "
        "Phổ năng lượng chuyển thành phổ rời rạc bị lượng tử hóa tỉ lệ nghịch với <i>n</i><sup>2</sup>. "
        "Khoảng cách giữa các mức năng lượng liên tiếp Δ<i>E</i> = <i>E</i><sub><i>n</i>+1</sub> − <i>E<sub>n</sub></i> "
        "thu hẹp rất nhanh theo tỉ lệ tỉ lệ nghịch với <i>n</i><sup>3</sup>, tiệm cận về mức 0 khi <i>n</i> → ∞ (ngưỡng ion hóa).<br/>"
        "<b>Ion giống Hydro (Hydrogen-like ions):</b> Với các ion có điện tích hạt nhân <i>Z</i> &gt; 1 (He<sup>+</sup> có <i>Z</i> = 2, Li<sup>2+</sup> có <i>Z</i> = 3), "
        "lực hút Coulomb tăng mạnh làm bán kính Bohr co lại: <i>a<sub>Z</sub></i> tỉ lệ nghịch với số điện tích <i>Z</i>. "
        "Năng lượng liên kết trạng thái cơ bản tăng vọt theo <i>Z</i><sup>2</sup>: đối với He<sup>+</sup>, năng lượng ion hóa là 13.6 × 4 = 54.4 eV; "
        "đối với Li<sup>2+</sup>, năng lượng ion hóa là 13.6 × 9 = 122.4 eV."
    )
    story.append(he.make_paragraph(g1_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_title_1 = "Thử thách CER 2.4.1: Bản chất suy biến năng lượng trong nguyên tử Hydro thuần túy"
    cer_claim_1 = (
        "Trong bài toán nguyên tử Hydro phi tương đối tính với trường thế Coulomb thuần túy, mức năng lượng <i>E<sub>n</sub></i> "
        "chỉ phụ thuộc duy nhất vào số lượng tử chính <i>n</i> mà hoàn toàn độc lập với số lượng tử quỹ đạo <i>l</i> và số lượng tử từ <i>m<sub>l</sub></i>. "
        "Mức suy biến toàn phần của mức <i>n</i> (chưa xét spin) bằng chính xác <i>g<sub>n</sub></i> = <i>n</i><sup>2</sup>."
    )
    cer_ev_1 = (
        "Phương trình vi phân hướng kính chứa cả <i>E</i> và <i>l</i>. Tuy nhiên, khi giải bằng đa thức Laguerre liên kết, "
        "hệ số ngắt chuỗi dẫn tới biểu thức <i>n</i> = <i>n<sub>r</sub></i> + <i>l</i> + 1, trong đó hằng số năng lượng <i>E</i> "
        "chỉ gắn với tổng <i>n</i> mà không chứa riêng lẻ <i>l</i>. Với mỗi giá trị <i>n</i> cố định, số lượng tử <i>l</i> có thể nhận các giá trị từ 0 đến <i>n</i> − 1. "
        "Với mỗi giá trị <i>l</i>, số lượng tử <i>m<sub>l</sub></i> nhận 2<i>l</i> + 1 giá trị. "
        "Tổng số trạng thái suy biến là: ∑<sub><i>l</i>=0</sub><sup><i>n</i>−1</sup> (2<i>l</i> + 1) = <i>n</i><sup>2</sup>."
    )
    cer_re_1 = (
        "Sự độc lập của <i>E</i> đối với <i>m<sub>l</sub></i> xuất phát từ đối xứng quay không gian 3 chiều SO(3) của thế đối xứng cầu <i>U</i>(<i>r</i>). "
        "Tuy nhiên, sự suy biến theo số lượng tử <i>l</i> (các orbital 2s và 2p có cùng năng lượng) là một hiện tượng đặc biệt gọi là 'suy biến tình cờ' (accidental degeneracy). "
        "Về mặt bản chất đối xứng động lực học, trường thế tỉ lệ nghịch <i>r</i><sup>−1</sup> sở hữu thêm một tích phân chuyển động được bảo toàn là vectơ Runge – Lenz. "
        "Sự bảo toàn đồng thời của momen động lượng L và vectơ Runge – Lenz nâng đối xứng của bài toán Hydro từ nhóm quay không gian SO(3) lên nhóm đối xứng động lực SO(4) trong không gian 4 chiều, "
        "buộc tất cả các trạng thái có cùng số lượng tử chính <i>n</i> phải có mức năng lượng hoàn toàn bằng nhau."
    )
    cer_text_1 = (
        f"<b>{cer_title_1}:</b><br/>"
        f"• <b>[Khẳng định (Claim)]:</b> {cer_claim_1}<br/>"
        f"• <b>[Bằng chứng định lượng (Evidence)]:</b> {cer_ev_1}<br/>"
        f"• <b>[Lập luận vi mô (Reasoning)]:</b> {cer_re_1}<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến của sinh viên là nghĩ rằng sự suy biến mức năng lượng theo số lượng tử quỹ đạo <i>l</i> xảy ra trong mọi nguyên tử. Thực tế, sự suy biến theo <i>l</i> chỉ tồn tại duy nhất ở nguyên tử một electron (Hydro và các ion tương đương) do đối xứng động lực Runge – Lenz trong trường thế tỉ lệ với <i>r</i><sup>−1</sup>; trong nguyên tử nhiều electron, hiệu ứng chắn và lực đẩy Coulomb phá vỡ đối xứng này làm các phân lớp 2s và 2p tách xa nhau."
    )
    story.append(he.make_paragraph(cer_text_1, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.4.2: HỆ 4 SỐ LƯỢNG TỬ VÀ SPIN ELECTRON
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.4.2: Hệ 4 số lượng tử và Spin electron", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g2_p1 = (
        "Giải phương trình Schrödinger không gian xuất hiện bộ ba số lượng tử (<i>n</i>, <i>l</i>, <i>m<sub>l</sub></i>). "
        "Tuy nhiên, bức tranh cơ học lượng tử về electron chỉ thực sự hoàn thiện khi tính đến thuộc tính lượng tử nội tại: <b>Spin của electron</b>.<br/>"
        "Năm 1925, Samuel Goudsmit và George Uhlenbeck đề xuất rằng electron sở hữu một momen động lượng nội tại riêng biệt, "
        "tương tự như một quả cầu điện tích tự quay quanh trục của nó. Năm 1922, thí nghiệm kinh điển của Otto Stern và Walther Gerlach "
        "cho chùm nguyên tử Bạc bay qua từ trường không đồng nhất ∂<i>B<sub>z</sub></i>/∂<i>z</i>. "
        "Nếu electron không có spin, chùm nguyên tử ở trạng thái cơ bản (<i>l</i> = 0) sẽ đi thẳng mà không bị tách. "
        "Thực tế, chùm hạt bị tách thành đúng hai vệt đối xứng trên màn hứng. "
        "Điều này chứng minh không thể chối cãi rằng momen từ nội tại của electron bị lượng tử hóa không gian thành đúng hai thành phần chiếu, "
        "tương ứng với số lượng tử spin <i>s</i> = ½ và số lượng tử hình chiếu spin <i>m<sub>s</sub></i> = ±½.<br/>"
        "Như vậy, trạng thái lượng tử đầy đủ của một electron trong nguyên tử được xác định duy nhất bởi <b>bộ 4 số lượng tử</b>: (<i>n</i>, <i>l</i>, <i>m<sub>l</sub></i>, <i>m<sub>s</sub></i>)."
    )
    story.append(he.make_paragraph(g2_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 03: Hình dạng các orbital s, p, d
    img_h03 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_03_Hinh_Dang_Cac_Orbital_s_p_d.png")
    cap_h03 = "Hình 2.4.3: Hình dạng hình học không gian 3 chiều của các orbital s, p và d (Slide 34)."
    story.append(he.embed_figure_with_caption(img_h03, cap_h03, kind="orig", styles=styles))

    h03_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Biểu diễn bề mặt đồng xác suất của các orbital nguyên tử: orbital s dạng cầu đối xứng; orbital p (p<sub>x</sub>, p<sub>y</sub>, p<sub>z</sub>) dạng hình số 8 nổi hai thùy; orbital d dạng bốn thùy hoa thị hoặc thùy đôi kèm vành xuyến."
    h03_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Hệ trục tọa độ vuông góc Descartes Oxyz trong không gian thực."
    h03_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Mặt phẳng nút (Nodal plane) nơi hàm sóng đổi dấu và xác suất tìm thấy electron bằng 0 tuyệt đối: orbital s có 0 mặt phẳng nút; orbital p có 1 mặt phẳng nút; orbital d có 2 mặt phẳng nút."
    h03_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Định hướng không gian của các orbital p và d quyết định trực tiếp tính có hướng của liên kết cộng hóa trị, giải thích hình học lập thể của phân tử và cấu trúc tinh thể nano."
    h03_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Dấu của hàm sóng (+ và −) trên các thùy thể hiện pha lượng tử, đóng vai trò sống còn trong hiện tượng giao thoa hàm sóng tạo liên kết liên kết (bonding) và phản liên kết (antibonding)."
    story.append(he.make_paragraph(h03_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h03_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h03_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h03_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h03_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng đồ thị mô phỏng 01: Mật độ xác suất hướng kính MATLAB
    img_sim01 = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.4_Mat_Do_Xac_Suat_Huong_Kinh_Hydro.png")
    cap_sim01 = "Hình 2.4.4: Mô phỏng MATLAB giải tích hàm mật độ xác suất hướng kính P<sub>nl</sub>(r) = r<sup>2</sup>|R<sub>nl</sub>(r)|<sup>2</sup> cho các orbital 1s, 2s, 2p, 3s, 3p, 3d theo chuẩn bán kính Bohr a<sub>0</sub>."
    story.append(he.embed_figure_with_caption(img_sim01, cap_sim01, kind="sim", styles=styles))

    h_sim01_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Hai khung đồ thị mô phỏng phân bố hướng kính: khung trái biểu diễn các orbital s (l=0); khung phải so sánh orbital p (l=1) và d (l=2)."
    h_sim01_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Trục hoành r / a<sub>0</sub> từ 0 đến 20; trục tung mật độ xác suất P<sub>nl</sub>(r) theo đơn vị 1/a<sub>0</sub>."
    h_sim01_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Trạng thái 1s đạt cực đại tại r = 1.0 a<sub>0</sub>; trạng thái 2p đạt cực đại tại r = 4.0 a<sub>0</sub>; trạng thái 3d đạt cực đại tại r = 9.0 a<sub>0</sub> (tổng quát r<sub>max</sub> = n<sup>2</sup>a<sub>0</sub> đối với orbital có l = n−1)."
    h_sim01_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Trạng thái 2s có cực đại phụ tại r ≈ 0.76 a<sub>0</sub> nằm sâu bên trong bán kính orbital 2p, thể hiện hiệu ứng xuyên thấu (penetration effect) cực kỳ quan trọng đối với nguyên tử nhiều electron."
    h_sim01_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Số lượng nút hướng kính thỏa mãn đúng công thức N<sub>r</sub> = n − l − 1 (1s có 0 nút, 2s có 1 nút tại r = 2a<sub>0</sub>, 3s có 2 nút)."
    story.append(he.make_paragraph(h_sim01_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h_sim01_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h_sim01_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h_sim01_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h_sim01_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 8))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g2_p2 = (
        "<b>Định nghĩa hàm mật độ xác suất hướng kính <i>P<sub>nl</sub></i>(<i>r</i>):</b><br/>"
        "Xác suất tìm thấy electron trong một phần tử thể tích không gian <i>dV</i> = <i>r</i><sup>2</sup>sin<i>θ·dr·dθ·dφ</i> là:<br/>"
        "<i>dW</i> = |Ψ<sub><i>nl·m<sub>l</sub></i></sub>(<i>r</i>, <i>θ</i>, <i>φ</i>)|<sup>2</sup>·<i>dV</i>.<br/>"
        "Tích phân theo toàn bộ các góc định hướng (0 ≤ <i>θ</i> ≤ <i>π</i> và 0 ≤ <i>φ</i> ≤ 2<i>π</i>) cho ta xác suất tìm thấy hạt "
        "trong lớp vỏ cầu mỏng có bán kính từ <i>r</i> đến <i>r</i> + <i>dr</i> bao quanh hạt nhân:<br/>"
        "<i>dW</i>(<i>r</i>) = |<i>R<sub>nl</sub></i>(<i>r</i>)|<sup>2</sup>·<i>r</i><sup>2</sup>·<i>dr</i> = <i>P<sub>nl</sub></i>(<i>r</i>)·<i>dr</i>.<br/>"
        "Thừa số <i>r</i><sup>2</sup> chính là diện tích mặt cầu 4<i>π·r</i><sup>2</sup> (Jacobian chuyển hệ tọa độ), làm cho xác suất tìm thấy hạt "
        "ngay tại tâm hạt nhân (<i>r</i> = 0) luôn bằng 0 đối với mọi trạng thái, mặc dù đối với các orbital s, biên độ hàm sóng |Ψ(0)| "
        "đạt giá trị cực đại khác 0."
    )
    story.append(he.make_paragraph(g2_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    eq_spin = r"P_{nl}(r) = r^2 |R_{nl}(r)|^2, \quad S^2 = s(s+1)\hbar^2, \quad S_z = m_s \hbar \quad \left(s = \frac{1}{2}, \, m_s = \pm \frac{1}{2}\right)"
    nom_spin = [
        ("Mật độ xác suất hướng kính", "<i>P<sub>nl</sub></i>(<i>r</i>)", "<i>a</i><sub>0</sub><sup>−1</sup>", "Mật độ xác suất tìm thấy electron trong vỏ cầu bán kính r đến r+dr"),
        ("Bình phương momen spin", "<i>S</i><sup>2</sup>", "J<sup>2</sup>·s<sup>2</sup>", "Bình phương độ lớn momen spin nội tại S<sup>2</sup> = s(s+1)ħ<sup>2</sup>"),
        ("Hình chiếu momen spin", "<i>S<sub>z</sub></i>", "J·s", "Hình chiếu của spin lên trục lượng tử hóa S<sub>z</sub> = m<sub>s</sub>ħ"),
        ("Số lượng tử spin", "<i>s</i>", "1", "Đặc trưng lượng tử nội tại của hạt fermion (s = ½ đối với electron)"),
        ("Số lượng tử từ spin", "<i>m<sub>s</sub></i>", "1", "Hai trạng thái định hướng không gian: +½ (Up) và −½ (Down)"),
        ("Độ suy biến mức năng lượng", "<i>g<sub>n</sub></i>", "1", "Tổng số trạng thái lượng tử có cùng năng lượng E<sub>n</sub> kể cả spin (g<sub>n</sub> = 2n<sup>2</sup>)")
    ]
    story.append(he.build_target_equation_block(eq_spin, nom_spin, styles=styles))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step2_1_text = (
        "<b>Bước 1: Tính bán kính có xác suất tìm thấy electron cực đại ở trạng thái cơ bản 1s:</b><br/>"
        "Hàm sóng hướng kính của trạng thái cơ bản Hydro (<i>n</i> = 1, <i>l</i> = 0) có dạng: "
        "hàm sóng hướng kính 1s phụ thuộc bán kính Bohr <i>a</i><sub>0</sub> và suy giảm hàm mũ theo khoảng cách <i>r</i>. "
        "Xây dựng biểu thức mật độ xác suất hướng kính <i>P</i><sub>10</sub>(<i>r</i>) và lấy đạo hàm bậc nhất theo biến <i>r</i> để tìm cực trị."
    )
    step2_1_eq = r"P_{10}(r) = r^2 R_{10}^2(r) = \frac{4}{a_0^3} r^2 e^{-\frac{2r}{a_0}} \quad \Longrightarrow \quad \frac{dP_{10}}{dr} = \frac{4}{a_0^3} \left( 2r - \frac{2r^2}{a_0} \right) e^{-\frac{2r}{a_0}} = 0"
    story.append(he.build_intermediate_equation(step2_1_text, step2_1_eq, styles=styles, is_expanded_from_slide=True))

    step2_2_text = (
        "<b>Bước 2: Xác lập kết quả cực đại và so sánh với mô hình bán cổ điển Bohr:</b><br/>"
        "Nghiệm cực trị cho hai giá trị: <i>r</i> = 0 (cực tiểu xác suất) và <i>r</i> = <i>a</i><sub>0</sub> (cực đại xác suất). "
        "Kết quả này khẳng định một sự trùng hợp vật lý tuyệt đẹp: Bán kính Bohr <i>a</i><sub>0</sub> trong mô hình bán cổ điển "
        "chính là khoảng cách có xác suất tìm thấy electron lớn nhất trong cơ học lượng tử, "
        "mặc dù electron có thể xuất hiện tại bất kỳ vị trí nào từ 0 đến vô cùng với mật độ xác suất liên tục."
    )
    step2_2_eq = r"r_{\max}(1s) = a_0 = \frac{4\pi\varepsilon_0 \hbar^2}{m e^2} \approx 0.529177 \text{ [\AA]} = 0.052918 \text{ [nm]}"
    story.append(he.build_intermediate_equation(step2_2_text, step2_2_eq, styles=styles, is_expanded_from_slide=True))

    step2_3_text = (
        "<b>Bước 3: Thiết lập hàm sóng toàn phần có spin (Spin-Orbital Wavefunction):</b><br/>"
        "Do toán tử spin tác dụng trên không gian trạng thái nội tại hai chiều độc lập với không gian tọa độ thực, "
        "hàm sóng toàn phần của một electron được biểu diễn dưới dạng tích tensor giữa hàm sóng không gian và spinor hai thành phần:"
    )
    step2_3_eq = r"\Psi_{nl m_l m_s}(r, \theta, \varphi) = \psi_{nl m_l}(r, \theta, \varphi) \chi_{m_s}, \quad \chi_{+\frac{1}{2}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \text{ (Spin Up)}, \quad \chi_{-\frac{1}{2}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \text{ (Spin Down)}"
    story.append(he.build_intermediate_equation(step2_3_text, step2_3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g2_p4 = (
        "<b>Ý nghĩa hình học của số lượng tử quỹ đạo <i>l</i>:</b> Độ lớn của vectơ momen động lượng quỹ đạo được lượng tử hóa theo công thức:<br/>"
        "|<b>L</b>| = √[<i>l</i>(<i>l</i> + 1)]·ħ.<br/>"
        "Hình chiếu của momen động lượng lên trục lượng tử hóa <i>Oz</i> nhận các giá trị: <i>L<sub>z</sub></i> = <i>m<sub>l</sub></i>·ħ.<br/>"
        "Do |<i>m<sub>l</sub></i>| ≤ <i>l</i> &lt; √[<i>l</i>(<i>l</i> + 1)], vectơ momen động lượng <b>L</b> không bao giờ có thể trùng hoàn toàn với trục <i>Oz</i>. "
        "Nó luôn nghiêng một góc <i>θ</i> sao cho cos<i>θ</i> là tỉ số giữa <i>m<sub>l</sub></i> và căn bậc hai của <i>l</i>(<i>l</i> + 1). "
        "Đây là biểu hiện trực quan của Nguyên lý bất định Heisenberg đối với các thành phần momen động lượng: [<i>L<sub>x</sub></i>, <i>L<sub>y</sub></i>] = <i>i</i>ħ<i>L<sub>z</sub></i>, "
        "khiến vectơ <b>L</b> phải thực hiện chuyển động tiến động (precession) xung quanh trục <i>Oz</i>.<br/>"
        "<b>Hiệu ứng xuyên thấu và tách mức phân lớp:</b> Đối với nguyên tử một electron, mức 2s và 2p có cùng năng lượng. "
        "Tuy nhiên, khi có nhiều electron, orbital 2s có cực đại phụ xuyên thấu sâu vào gần hạt nhân (<i>r</i> &lt; <i>a</i><sub>0</sub>), "
        "cảm nhận điện tích hạt nhân ít bị chắn hơn so với orbital 2p. Kết quả là orbital 2s bị kéo xuống mức năng lượng thấp hơn orbital 2p, "
        "phá vỡ suy biến theo <i>l</i>."
    )
    story.append(he.make_paragraph(g2_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_title_2 = "Thử thách CER 2.4.2: Phản biện quan niệm bán kính quỹ đạo cổ điển Rutherford – Bohr"
    cer_claim_2 = (
        "Quan niệm cho rằng electron trong nguyên tử Hydro quay quanh hạt nhân theo một quỹ đạo hình tròn cố định có bán kính <i>a</i><sub>0</sub> "
        "như mô hình hành tinh nguyên tử Bohr là hoàn toàn sai lệch về mặt cơ học lượng tử. "
        "Bán kính Bohr <i>a</i><sub>0</sub> chỉ mang ý nghĩa thống kê là khoảng cách xuyên tâm có mật độ xác suất xuất hiện electron cực đại."
    )
    cer_ev_2 = (
        "Theo hàm mật độ xác suất <i>P</i><sub>10</sub>(<i>r</i>) = hàm mật độ xác suất hướng kính <i>P</i><sub>10</sub>(<i>r</i>), "
        "tích phân xác suất tìm thấy electron trong khoảng từ 0 đến <i>a</i><sub>0</sub> chỉ bằng xấp xỉ 32.3%, trong khi xác suất tìm thấy electron "
        "ở khoảng cách lớn hơn <i>a</i><sub>0</sub> lên tới 67.7%. Giá trị kỳ vọng trung bình khoảng cách của electron là: "
        "⟨<i>r</i>⟩ = ∫ <i>r·P</i><sub>10</sub>(<i>r</i>)·<i>dr</i> = 1.5·<i>a</i><sub>0</sub> ≈ 0.794 Å, lớn hơn 1.5 lần bán kính Bohr."
    )
    cer_re_2 = (
        "Theo Nguyên lý bất định Heisenberg Δ<i>x</i>·Δ<i>p<sub>x</sub></i> ≥ 0.5·ħ, một vi hạt lượng tử không thể đồng thời sở hữu tọa độ xác định "
        "và quỹ đạo chuyển động xác định. Nếu electron chuyển động trên một quỹ đạo tròn phẳng cố định, độ bất định vị trí theo phương vuông góc "
        "với mặt phẳng quỹ đạo sẽ bằng 0 (Δ<i>z</i> = 0), dẫn tới độ bất định động lượng theo phương đó bùng nổ ra vô cùng (Δ<i>p<sub>z</sub></i> → ∞), "
        "phá vỡ hoàn toàn trạng thái liên kết bền vững. Cơ học lượng tử thay thế quỹ đạo chuyển động bằng khái niệm đám mây điện tử (Orbital), "
        "nơi electron tồn tại dưới dạng phân bố xác suất ba chiều không gian."
    )
    cer_text_2 = (
        f"<b>{cer_title_2}:</b><br/>"
        f"• <b>[Khẳng định (Claim)]:</b> {cer_claim_2}<br/>"
        f"• <b>[Bằng chứng định lượng (Evidence)]:</b> {cer_ev_2}<br/>"
        f"• <b>[Lập luận vi mô (Reasoning)]:</b> {cer_re_2}<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù là nhầm lẫn giữa xác suất cực đại hướng kính <i>P</i>(<i>r</i>) và bình phương biên độ hàm sóng |Ψ(<i>r</i>)|<sup>2</sup>. Trong khi |Ψ(<i>r</i>)|<sup>2</sup> đạt cực đại tại <i>r</i> = 0 đối với orbital s, thì thể tích vỏ cầu 4<i>π·r</i><sup>2</sup><i>dr</i> triệt tiêu tại tâm khiến <i>P</i>(0) = 0 và đẩy cực đại xác suất thực tế ra vị trí <i>r</i> = <i>a</i><sub>0</sub>."
    )
    story.append(he.make_paragraph(cer_text_2, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.4.3: NGUYÊN TỬ NHIỀU ELECTRON, NGUYÊN LÝ PAULI & QUY TẮC AUFBAU/HUND
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.4.3: Nguyên tử nhiều electron, Nguyên lý Pauli &amp; Quy tắc Aufbau / Hund", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g3_p1 = (
        "Khi chuyển từ nguyên tử Hydro sang nguyên tử có nhiều hơn một electron (<i>N</i> ≥ 2), "
        "bài toán cơ học lượng tử đối mặt với thách thức to lớn: <b>Tương tác đẩy tĩnh điện Coulomb giữa các electron</b>.<br/>"
        "Hamiltonian toàn phần của hệ chứa số hạng tương tác hạt đôi tương tác đẩy Coulomb giữa các cặp electron. "
        "Do số hạng này phụ thuộc vào khoảng cách tương đối <i>r<sub>ij</sub></i> = |<b>r</b><sub><i>i</i></sub> − <b>r</b><sub><i>j</i></sub>|, "
        "phương trình Schrödinger không thể tách ly biến số chính xác tuyệt đối. "
        "Để giải quyết hệ nhiều hạt, các nhà vật lý xây dựng xấp xỉ trường tự hợp (Hartree – Fock), trong đó mỗi electron chuyển động "
        "trong một trường thế trung tâm hiệu dụng tạo bởi hạt nhân và đám mây tích điện âm của các electron còn lại.<br/>"
        "Năm 1925, nhà vật lý người Áo Wolfgang Pauli đề xuất <b>Nguyên lý loại trừ Pauli</b>: Trong một hệ lượng tử gồm các hạt fermion đồng nhất, "
        "không bao giờ có thể tồn tại hai hạt có cùng một trạng thái lượng tử (nghĩa là có cùng bộ 4 số lượng tử). "
        "Nguyên lý Pauli cùng với quy tắc Aufbau (Madelung) và các quy tắc Hund chính là kim chỉ nam quy định trật tự lấp đầy "
        "các lớp vỏ electron, tạo nên tính tuần hoàn kỳ diệu của bảng hệ thống hóa học Mendeleev."
    )
    story.append(he.make_paragraph(g3_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 04: Chân dung Pauli
    img_h04 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_04_Nguyen_Ly_Pauli_Wolfgang.png")
    cap_h04 = "Hình 2.4.5: Chân dung Wolfgang Pauli (1900–1958) — Giải Nobel Vật lý năm 1945 cho việc phát minh Nguyên lý loại trừ (Slide 41)."
    story.append(he.embed_figure_with_caption(img_h04, cap_h04, kind="orig", styles=styles))

    h04_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Chân dung nhà vật lý lý thuyết Wolfgang Pauli thời kỳ đề xuất nguyên lý loại trừ hạt fermion."
    h04_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Niên đại lịch sử: 1900–1958; năm công bố nguyên lý: 1925."
    h04_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Nguyên lý loại trừ giải thích tại sao vật chất vĩ mô không bị sụp đổ dưới tác dụng của lực hút tĩnh điện và lực hấp dẫn."
    h04_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Áp suất thoái hóa Pauli (Degeneracy pressure) tạo ra lực đẩy lượng tử vĩ mô duy trì sự cân bằng của các sao lùn trắng và sao neutron."
    h04_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Tính phản đối xứng của hàm sóng hai fermion Ψ(1,2) = −Ψ(2,1) dẫn tới xác suất hai electron có cùng spin xuất hiện tại cùng một điểm trong không gian bằng 0 tuyệt đối."
    story.append(he.make_paragraph(h04_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h04_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h04_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h04_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h04_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh gốc 05: Sơ đồ Aufbau Madelung
    img_h05 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_05_Quy_Tac_Aufbau_Madelung.png")
    cap_h05 = "Hình 2.4.6: Quy tắc cấu hình phân lớp điện tử Aufbau / Madelung và thang năng lượng phân lớp (Slide 43)."
    story.append(he.embed_figure_with_caption(img_h05, cap_h05, kind="orig", styles=styles))

    h05_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Sơ đồ mũi tên đường chéo thể hiện thứ tự lấp đầy electron qua các phân lớp 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s... kèm thang năng lượng tương đối."
    h05_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Số lượng tử chính n = 1..7; số lượng tử quỹ đạo l = 0(s), 1(p), 2(d), 3(f)."
    h05_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Phân lớp 4s có tổng (n+l) = 4 + 0 = 4 được điền trước phân lớp 3d có tổng (n+l) = 3 + 2 = 5."
    h05_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Hiệu ứng chắn electron làm giảm điện tích hạt nhân hiệu dụng Z<sub>eff</sub> của phân lớp 3d nhiều hơn so với phân lớp 4s có mật độ xác suất xuyên thấu mạnh vào tâm."
    h05_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Số electron tối đa trong một phân lớp bằng 2(2l+1): phân lớp s chứa 2 electron, p chứa 6, d chứa 10, f chứa 14."
    story.append(he.make_paragraph(h05_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h05_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h05_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h05_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h05_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 8))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g3_p2 = (
        "<b>Định thức Slater và tính phản đối xứng:</b><br/>"
        "Theo định lý thống kê spin lượng tử, hệ gồm <i>N</i> fermion đồng nhất phải có hàm sóng toàn phần phản đối xứng đối với phép hoán vị "
        "tọa độ không gian và spin của bất kỳ cặp hạt nào. Dạng toán học tổng quát thỏa mãn yêu cầu này là <b>Định thức Slater</b>:<br/>"
        "Nếu có hai electron ở cùng một trạng thái spin-orbital (nghĩa là có hai hàng trong định thức giống hệt nhau), "
        "định thức sẽ triệt tiêu bằng 0. Điều này chứng minh toán học trực tiếp cho Nguyên lý loại trừ Pauli.<br/>"
        "<b>Ba quy tắc Hund xác định trạng thái cơ bản bền vững nhất:</b><br/>"
        "1. <i>Quy tắc 1 (Cực đại độ bội spin):</i> Trạng thái cơ bản của nguyên tử có momen spin toàn phần <i>S</i> lớn nhất có thể (độ bội <i>χ</i> = 2<i>S</i> + 1 cực đại). "
        "Các electron ưu tiên chiếm các orbital độc lập với spin song song để cực tiểu hóa lực đẩy Coulomb nhờ hố thế trao đổi.<br/>"
        "2. <i>Quy tắc 2 (Cực đại momen quỹ đạo):</i> Khi có cùng độ bội spin cực đại, trạng thái có momen động lượng quỹ đạo toàn phần <i>L</i> lớn nhất sẽ bền vững nhất.<br/>"
        "3. <i>Quy tắc 3 (Tương tác spin – quỹ đạo):</i> Đối với phân lớp chưa điền đầy quá một nửa số electron tối đa, trạng thái bền nhất có momen toàn phần <i>J</i> = |<i>L</i> − <i>S</i>|; "
        "đối với phân lớp đã điền đầy quá một nửa, trạng thái bền nhất có <i>J</i> = <i>L</i> + <i>S</i>."
    )
    story.append(he.make_paragraph(g3_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    eq_aufbau = r"\hat{H} = \sum_{i=1}^N \left( -\frac{\hbar^2}{2m} \nabla_i^2 - \frac{Z e^2}{4\pi\varepsilon_0 r_i} \right) + \sum_{i < j}^N \frac{e^2}{4\pi\varepsilon_0 r_{ij}}, \quad \Psi = \frac{1}{\sqrt{N!}} \det [\psi_k(j)]"
    nom_aufbau = [
        ("Hamiltonian nhiều electron", "<i>\u0125</i>", "eV", "Toán tử năng lượng gồm động năng, thế hút hạt nhân và thế đẩy Coulomb e-e"),
        ("Khoảng cách tương đối hạt đôi", "<i>r<sub>ij</sub></i>", "m", "Khoảng cách không gian giữa electron thứ i và electron thứ j"),
        ("Hàm sóng định thức Slater", "Ψ", "m<sup>−1.5 N</sup>", "Hàm sóng toàn phần phản đối xứng đối với phép hoán vị hai electron bất kỳ"),
        ("Momen spin toàn phần", "<i>S</i>", "1", "Tổng vectơ momen spin của tất cả các electron hóa trị (S = ∑ s<sub>i</sub>)"),
        ("Momen quỹ đạo toàn phần", "<i>L</i>", "1", "Tổng vectơ momen quỹ đạo của các electron hóa trị (L = ∑ l<sub>i</sub>)"),
        ("Momen động lượng toàn phần", "<i>J</i>", "1", "Momen toàn phần ghép Russell – Saunders (<b>J</b> = <b>L</b> + <b>S</b>)"),
        ("Số hạng quang phổ", "<sup>2<i>S</i>+1</sup><i>L<sub>J</sub></i>", "1", "Ký hiệu trạng thái nguyên tử với độ bội spin χ = 2S+1")
    ]
    story.append(he.build_target_equation_block(eq_aufbau, nom_aufbau, styles=styles))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step3_1_text = (
        "<b>Bước 1: Áp dụng quy tắc Aufbau xác định cấu hình electron nguyên tử Cacbon (Z = 6):</b><br/>"
        "Nguyên tử Cacbon có 6 electron. Thứ tự lấp đầy các phân lớp theo quy tắc Madelung (<i>n</i> + <i>l</i>): "
        "Phân lớp 1s (<i>n</i>+<i>l</i> = 1) nhận tối đa 2 electron → 1s<sup>2</sup>. "
        "Phân lớp 2s (<i>n</i>+<i>l</i> = 2) nhận tối đa 2 electron → 2s<sup>2</sup>. "
        "Còn lại 2 electron đi vào phân lớp 2p (<i>n</i>+<i>l</i> = 3) → 2p<sup>2</sup>. "
        "Cấu hình electron đầy đủ là: 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>2</sup>."
    )
    step3_1_eq = r"\text{C } (Z=6): \quad 1s^2 \, 2s^2 \, 2p^2 \quad \left( [ \text{He} ] \, 2s^2 \, 2p^2 \right)"
    story.append(he.build_intermediate_equation(step3_1_text, step3_1_eq, styles=styles, is_expanded_from_slide=True))

    step3_2_text = (
        "<b>Bước 2: Áp dụng quy tắc Hund tìm trạng thái cơ bản và số hạng quang phổ của Cacbon:</b><br/>"
        "Phân lớp 1s<sup>2</sup> và 2s<sup>2</sup> đã điền đầy nên có <i>L</i> = 0, <i>S</i> = 0. "
        "Chỉ cần xét 2 electron hóa trị ở phân lớp 2p (<i>l</i> = 1). "
        "Theo Quy tắc 1 của Hund, 2 electron này chiếm 2 orbital p khác nhau (ví dụ <i>p<sub>x</sub></i> và <i>p<sub>y</sub></i>) "
        "với spin song song để cực đại hóa momen spin toàn phần: <i>S</i> = ½ + ½ = 1 (độ bội <i>χ</i> = 2<i>S</i> + 1 = 3, trạng thái Triplet). "
        "Để thỏa mãn nguyên lý Pauli, hai electron có <i>m<sub>l</sub></i> = +1 và <i>m<sub>l</sub></i> = 0, suy ra <i>L</i> = 1 + 0 = 1 (ký hiệu chữ cái P). "
        "Do phân lớp 2p chứa 2 electron (ít hơn một nửa dung lượng cực đại 6 electron), theo Quy tắc 3 của Hund: "
        "<i>J</i> = |<i>L</i> − <i>S</i>| = |1 − 1| = 0. Số hạng quang phổ trạng thái cơ bản của Cacbon là <sup>3</sup>P<sub>0</sub>."
    )
    step3_2_eq = r"S = 1, \quad L = 1, \quad J = |L - S| = 0 \quad \Longrightarrow \quad \text{Số hạng quang phổ: } {^3P_0}"
    story.append(he.build_intermediate_equation(step3_2_text, step3_2_eq, styles=styles, is_expanded_from_slide=True))

    step3_3_text = (
        "<b>Bước 3: Quy tắc ghép momen Russell – Saunders (Ghép L – S):</b><br/>"
        "Đối với các nguyên tử nhẹ và trung bình (<i>Z</i> &lt; 30), tương tác tĩnh điện Coulomb giữa các electron "
        "mạnh hơn nhiều so với tương tác spin – quỹ đạo của từng electron riêng lẻ. "
        "Do đó, các momen quỹ đạo <b>l</b><sub><i>i</i></sub> ghép lại thành <b>L</b> = ∑ <b>l</b><sub><i>i</i></sub>, "
        "và các momen spin <b>s</b><sub><i>i</i></sub> ghép lại thành <b>S</b> = ∑ <b>s</b><sub><i>i</i></sub>. "
        "Sau đó, <b>L</b> và <b>S</b> ghép lại tạo thành momen động lượng toàn phần <b>J</b> = <b>L</b> + <b>S</b>, "
        "với số lượng tử <i>J</i> nhận các giá trị từ |<i>L</i> − <i>S</i>| đến <i>L</i> + <i>S</i> theo bước nhảy 1."
    )
    step3_3_eq = r"J \in \{ L + S, \, L + S - 1, \, \dots, \, |L - S| \}, \quad \text{Độ bội } \chi = 2S + 1 \text{ (Số giá trị cho phép của } J \text{ khi } L \ge S \text{)}"
    story.append(he.build_intermediate_equation(step3_3_text, step3_3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g3_p4 = (
        "<b>Ngoại lệ cấu hình nửa bão hòa và bão hòa:</b> Trong dãy kim loại chuyển tiếp 3d, xuất hiện các trường hợp ngoại lệ "
        "vượt ra ngoài quy tắc Aufbau thông thường. Điển hình là Crom (<i>Z</i> = 24) có cấu hình [Ar] 3d<sup>5</sup> 4s<sup>1</sup> "
        "(thay vì 3d<sup>4</sup> 4s<sup>2</sup>) và Đồng (<i>Z</i> = 29) có cấu hình [Ar] 3d<sup>10</sup> 4s<sup>1</sup> (thay vì 3d<sup>9</sup> 4s<sup>2</sup>).<br/>"
        "Bản chất vật lý xuất phát từ <b>Năng lượng trao đổi lượng tử (Exchange Energy)</b>. "
        "Khi phân lớp d đạt trạng thái bán bão hòa (5 electron có spin song song), số lượng cặp electron có spin cùng chiều "
        "là <i>C</i><sub>5</sub><sup>2</sup> = 10 cặp, cực đại hóa năng lượng trao đổi âm làm giảm thế năng toàn phần của nguyên tử. "
        "Độ lợi năng lượng trao đổi này lớn hơn năng lượng cần thiết để kích thích một electron từ 4s lên 3d.<br/>"
        "<b>Chuyển đổi từ ghép L – S sang ghép j – j:</b> Khi điện tích hạt nhân <i>Z</i> tăng cao (các nguyên tố nặng cuối bảng tuần hoàn), "
        "tương tác spin – quỹ đạo tỉ lệ với <i>Z</i><sup>4</sup> tăng vọt và áp đảo tương tác Coulomb hạt đôi. "
        "Khi đó, momen spin và quỹ đạo của từng electron ghép trước với nhau: <b>j</b><sub><i>i</i></sub> = <b>l</b><sub><i>i</i></sub> + <b>s</b><sub><i>i</i></sub>, "
        "rồi các <b>j</b><sub><i>i</i></sub> mới ghép lại thành <b>J</b> = ∑ <b>j</b><sub><i>i</i></sub> (Cơ chế ghép j – j)."
    )
    story.append(he.make_paragraph(g3_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_title_3 = "Thử thách CER 2.4.3: Nguồn gốc độ bền vượt trội của cấu hình electron bán bão hòa 3d<sup>5</sup>"
    cer_claim_3 = (
        "Cấu hình electron của Crom (<i>Z</i> = 24) ở trạng thái cơ bản là [Ar] 3d<sup>5</sup> 4s<sup>1</sup> thay vì [Ar] 3d<sup>4</sup> 4s<sup>2</sup>. "
        "Sự chuyển một electron từ orbital 4s sang 3d làm cho nguyên tử đạt trạng thái năng lượng thấp hơn và bền vững hơn."
    )
    cer_ev_3 = (
        "Năng lượng toàn phần của hệ electron được mô hình hóa gồm: động năng, thế hút hạt nhân, thế đẩy Coulomb tĩnh điện <i>J</i><sub>Coulomb</sub> "
        "và năng lượng trao đổi lượng tử mang dấu âm −<i>K</i> giữa các electron có cùng spin song song. "
        "Với cấu hình 3d<sup>4</sup> 4s<sup>2</sup>, số cặp spin song song trong phân lớp 3d là <i>C</i><sub>4</sub><sup>2</sup> = 6 cặp. "
        "Với cấu hình 3d<sup>5</sup> 4s<sup>1</sup>, cả 5 electron trong 3d đều có spin song song, số cặp spin cùng chiều tăng vọt lên <i>C</i><sub>5</sub><sup>2</sup> = 10 cặp. "
        "Độ sụt giảm năng lượng trao đổi là Δ<i>E</i><sub>ex</sub> = −4<i>K</i> (với <i>K</i> ≈ 0.8 eV), vượt qua phần chênh lệch năng lượng orbital giữa 3d và 4s (khoảng 1.2 eV)."
    )
    cer_re_3 = (
        "Theo định lý Hartree – Fock, năng lượng trao đổi lượng tử xuất hiện do tính phản đối xứng của định thức Slater. "
        "Hai electron có cùng spin không bao giờ có thể ở cùng một vị trí không gian (hiệu ứng hố thế Fermi), "
        "khiến khoảng cách trung bình giữa chúng tăng lên và lực đẩy Coulomb giữa chúng giảm đi rõ rệt. "
        "Cấu hình bán bão hòa 3d<sup>5</sup> tối đa hóa số cặp electron tương tác trao đổi, "
        "giải thích tại sao các phân lớp nửa bão hòa và bão hòa luôn sở hữu độ bền nhiệt động học vượt bậc."
    )
    cer_text_3 = (
        f"<b>{cer_title_3}:</b><br/>"
        f"• <b>[Khẳng định (Claim)]:</b> {cer_claim_3}<br/>"
        f"• <b>[Bằng chứng định lượng (Evidence)]:</b> {cer_ev_3}<br/>"
        f"• <b>[Lập luận vi mô (Reasoning)]:</b> {cer_re_3}<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù của sinh viên là máy móc áp dụng quy tắc Aufbau cho mọi nguyên tố mà bỏ quên vai trò của năng lượng tương tác trao đổi lượng tử giữa các electron cùng spin trong các orbital thoái hóa suy biến."
    )
    story.append(he.make_paragraph(cer_text_3, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.4.4: PHỔ PHÁT XẠ CỦA HYDRO & QUY TẮC LỰA CHỌN QUANG HỌC
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.4.4: Phổ phát xạ của Hydro &amp; Quy tắc lựa chọn quang học", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g4_p1 = (
        "Quang phổ phát xạ và hấp thụ nguyên tử chính là bằng chứng thực nghiệm quan trọng nhất "
        "dẫn tới sự khai sinh của thuyết lượng tử. Khi nguyên tử bị kích thích bởi nhiệt, va chạm electron hoặc chiếu xạ ánh sáng, "
        "electron hấp thụ năng lượng và chuyển dời lên các mức năng lượng cao hơn. "
        "Khi electron chuyển từ mức năng lượng cao <i>E<sub>m</sub></i> về mức năng lượng thấp hơn <i>E<sub>n</sub></i>, "
        "năng lượng dư thừa được giải phóng dưới dạng một photon bức xạ điện từ đơn sắc có tần số <i>ω</i> thỏa mãn hệ thức Einstein:<br/>"
        "ħ<i>ω</i> = |<i>E<sub>m</sub></i> − <i>E<sub>n</sub></i>|.<br/>"
        "Đối với nguyên tử Hydro, các bước chuyển về các mức cơ bản khác nhau tạo thành các <b>dãy phổ vạch đặc trưng</b>: "
        "Dãy Lyman (về <i>n</i> = 1, vùng tử ngoại UV); Dãy Balmer (về <i>n</i> = 2, vùng ánh sáng khả kiến); "
        "Dãy Paschen (về <i>n</i> = 3, vùng hồng ngoại gần IR); Dãy Brackett (về <i>n</i> = 4) và Dãy Pfund (về <i>n</i> = 5).<br/>"
        "Tuy nhiên, không phải mọi bước chuyển giữa hai mức bất kỳ đều được phép xảy ra. "
        "Quá trình tương tác bức xạ lưỡng cực điện bị chi phối nghiêm ngặt bởi <b>các quy tắc lựa chọn quang học (Selection Rules)</b>, "
        "bảo đảm sự bảo toàn toàn vẹn của năng lượng, xung lượng và momen động lượng của hệ hạt và trường bức xạ."
    )
    story.append(he.make_paragraph(g4_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 06: Sơ đồ mức năng lượng Hydro
    img_h06 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_06_So_Do_Muc_Nang_Luong_Hydro.png")
    cap_h06 = "Hình 2.4.7: Sơ đồ chuyển dời mức năng lượng Hydro tạo nên các dãy phổ Lyman, Balmer, Paschen (Slide 48)."
    story.append(he.embed_figure_with_caption(img_h06, cap_h06, kind="orig", styles=styles))

    h06_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Thang mức năng lượng Bohr tỉ lệ −13.6/n<sup>2</sup> eV và các mũi tên thẳng đứng chỉ hướng chuyển mức phát xạ từ các mức n > 1 về các mức cơ bản."
    h06_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Trục năng lượng thẳng đứng tính bằng eV từ −13.6 eV đến 0.0 eV; vạch n = ∞ là mức ion hóa."
    h06_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Độ chênh năng lượng lớn nhất thuộc về dãy Lyman (bước nhảy về n=1), tạo nên các photon tử ngoại có năng lượng lớn hơn 10.2 eV."
    h06_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Mật độ các mức năng lượng dày đặc lại khi n tiến dần ra vô cùng, dẫn tới hiện tượng giới hạn dãy phổ (Series limit)."
    h06_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Bước sóng ngắn nhất của dãy Lyman tương ứng chuyển dời từ n = ∞ về n = 1 có bước sóng λ<sub>limit</sub> = 91.2 nm."
    story.append(he.make_paragraph(h06_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h06_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h06_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h06_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h06_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh gốc 07: Quang phổ vạch Hydro
    img_h07 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_07_Cac_Day_Pho_Lyman_Balmer.png")
    cap_h07 = "Hình 2.4.8: Quang phổ vạch phát xạ thực nghiệm của Hydro trong vùng ánh sáng khả kiến (Dãy Balmer) (Slide 48)."
    story.append(he.embed_figure_with_caption(img_h07, cap_h07, kind="orig", styles=styles))

    h07_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Dải quang phổ vạch màu sắc rực rỡ trên nền tối: vạch H<sub>α</sub> màu đỏ rực rỡ, vạch H<sub>β</sub> màu xanh lơ (cyan), vạch H<sub>γ</sub> màu lam và vạch H<sub>δ</sub> màu tím."
    h07_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Trục bước sóng ánh sáng khả kiến từ 400 nm đến 700 nm."
    h07_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Vạch H<sub>α</sub> xuất hiện tại 656.3 nm; H<sub>β</sub> tại 486.1 nm; H<sub>γ</sub> tại 434.0 nm; H<sub>δ</sub> tại 410.2 nm."
    h07_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Độ sáng và cường độ vạch giảm dần từ H<sub>α</sub> về phía tím do xác suất kích thích và xác suất chuyển mức Einstein A giảm."
    h07_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Phổ vạch rời rạc là bằng chứng thực nghiệm thép phủ nhận mô hình điện động lực học cổ điển Maxwell (vốn dự báo bức xạ liên tục và electron rơi vào tâm sau 10<sup>−11</sup> s)."
    story.append(he.make_paragraph(h07_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h07_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h07_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h07_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h07_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng đồ thị mô phỏng 02: MATLAB Sơ đồ chuyển mức
    img_sim02 = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.4_Cac_Day_Chuyen_Doi_Quang_Hoc_Hydro.png")
    cap_sim02 = "Hình 2.4.9: Mô phỏng MATLAB giải tích sơ đồ thang mức năng lượng Hydro E<sub>n</sub> = −13.6·n<sup>−2</sup> eV và các dãy chuyển dời quang học Lyman, Balmer, Paschen, Brackett."
    story.append(he.embed_figure_with_caption(img_sim02, cap_sim02, kind="sim", styles=styles))

    h_sim02_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Biểu đồ thang mức năng lượng chuẩn với các mũi tên màu vector thể hiện các dãy bước chuyển: Lyman (tím), Balmer (nhiều màu khả kiến), Paschen (cam), Brackett (xanh lá)."
    h_sim02_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Trục tung năng lượng E tính bằng eV từ −14.0 eV đến +0.5 eV; các mức n = 1, 2, 3, 4, 5, 6 và n = ∞."
    h_sim02_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Vạch n=1 (−13.60 eV); n=2 (−3.40 eV); n=3 (−1.51 eV); n=4 (−0.85 eV); n=5 (−0.54 eV); n=6 (−0.38 eV)."
    h_sim02_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Năng lượng photon phát xạ bằng đúng khoảng cách giữa hai vạch mức năng lượng, minh họa trực quan công thức Rydberg."
    h_sim02_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Mức n = ∞ là mức năng lượng ion hóa 0.00 eV; nếu electron hấp thụ photon có năng lượng lớn hơn 13.6 eV, nguyên tử bị ion hóa và electron nhận động năng liên tục."
    story.append(he.make_paragraph(h_sim02_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h_sim02_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h_sim02_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h_sim02_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h_sim02_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 8))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g4_p2 = (
        "<b>Công thức Rydberg – Ritz và các quy tắc chọn lọc lưỡng cực điện:</b><br/>"
        "Bước sóng <i>λ</i> của vạch quang phổ phát xạ khi chuyển từ mức <i>n</i><sub>2</sub> về <i>n</i><sub>1</sub> (với <i>n</i><sub>2</sub> &gt; <i>n</i><sub>1</sub>) "
        "được mô tả chính xác bởi công thức Rydberg – Ritz:<br/>"
        "nghịch đảo bước sóng <i>λ</i><sup>−1</sup> tỉ lệ với hiệu các nghịch đảo bình phương số lượng tử chính,<br/>"
        "trong đó hằng số Rydberg đối với Hydro <i>R<sub>H</sub></i> ≈ 1.097373 × 10<sup>7</sup> m<sup>−1</sup>.<br/>"
        "<b>Các quy tắc lựa chọn quang học (Selection Rules):</b><br/>"
        "1. <i>Quy tắc số lượng tử quỹ đạo:</i> Δ<i>l</i> = <i>l<sub>m</sub></i> − <i>l<sub>n</sub></i> = ±1.<br/>"
        "2. <i>Quy tắc bảo toàn spin:</i> Δ<i>S</i> = <i>S<sub>m</sub></i> − <i>S<sub>n</sub></i> = 0 (Quy tắc cấm tổ hợp giữa các trạng thái khác độ bội, cấm chuyển dời Singulet ↔ Triplet).<br/>"
        "3. <i>Quy tắc momen toàn phần:</i> Δ<i>J</i> = <i>J<sub>m</sub></i> − <i>J<sub>n</sub></i> = 0, ±1 (ngoại lệ cấm chuyển dời <i>J</i> = 0 → <i>J</i> = 0)."
    )
    story.append(he.make_paragraph(g4_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    eq_rydberg = r"\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right), \quad \Delta l = \pm 1, \quad \Delta S = 0, \quad \Delta J = 0, \pm 1 \; (0 \not\to 0)"
    nom_rydberg = [
        ("Bước sóng vạch quang phổ", "<i>λ</i>", "nm", "Bước sóng bức xạ photon phát xạ hoặc hấp thụ giữa hai mức năng lượng"),
        ("Hằng số Rydberg Hydro", "<i>R<sub>H</sub></i>", "m<sup>−1</sup>", "Hằng số quang phổ thực nghiệm (1.0973731568 × 10<sup>7</sup> m<sup>−1</sup>)"),
        ("Số lượng tử mức thấp", "<i>n</i><sub>1</sub>", "1", "Mức năng lượng đích (n<sub>1</sub> = 1: Lyman, 2: Balmer, 3: Paschen)"),
        ("Số lượng tử mức cao", "<i>n</i><sub>2</sub>", "1", "Mức năng lượng kích thích ban đầu của electron (n<sub>2</sub> > n<sub>1</sub>)"),
        ("Quy tắc chọn lọc quỹ đạo", "Δ<i>l</i>", "1", "Độ biến thiên số lượng tử quỹ đạo trong chuyển dời lưỡng cực điện (±1)"),
        ("Quy tắc chọn lọc spin", "Δ<i>S</i>", "1", "Bảo toàn spin toàn phần trong chuyển dời lưỡng cực điện (ΔS = 0)"),
        ("Quy tắc chọn lọc momen toàn phần", "Δ<i>J</i>", "1", "Độ biến thiên momen động lượng toàn phần (0, ±1; cấm 0 → 0)")
    ]
    story.append(he.build_target_equation_block(eq_rydberg, nom_rydberg, styles=styles))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step4_1_text = (
        "<b>Bước 1: Tính bước sóng vạch đỏ H<sub>α</sub> trong dãy Balmer của Hydro:</b><br/>"
        "Vạch H<sub>α</sub> tương ứng với bước chuyển từ mức <i>n</i><sub>2</sub> = 3 về mức <i>n</i><sub>1</sub> = 2. "
        "Thay số vào công thức Rydberg: nghịch đảo bước sóng <i>λ</i><sup>−1</sup> qua hiệu hai mức năng lượng."
    )
    step4_1_eq = r"\frac{1}{\lambda_{H_\alpha}} = 1.097373 \times 10^7 \times \left( \frac{1}{4} - \frac{1}{9} \right) = 1.097373 \times 10^7 \times \frac{5}{36} \approx 1.52413 \times 10^6 \text{ [m}^{-1}\text{]}"
    story.append(he.build_intermediate_equation(step4_1_text, step4_1_eq, styles=styles, is_expanded_from_slide=True))

    step4_2_text = (
        "<b>Bước 2: Nghịch đảo tìm bước sóng chính xác và đối chiếu thực nghiệm:</b><br/>"
        "Nghịch đảo giá trị <i>λ</i><sup>−1</sup> ta tìm được bước sóng vạch H<sub>α</sub> bằng 656.1 nm, "
        "hoàn toàn trùng khớp với vạch đỏ rực rỡ quan sát được trên quang phổ kế thiên văn và phòng thí nghiệm (656.28 nm)."
    )
    step4_2_eq = r"\lambda_{H_\alpha} = \frac{1}{1.52413 \times 10^6} \text{ m} \approx 6.5611 \times 10^{-7} \text{ m} = 656.11 \text{ [nm]}"
    story.append(he.build_intermediate_equation(step4_2_text, step4_2_eq, styles=styles, is_expanded_from_slide=True))

    step4_3_text = (
        "<b>Bước 3: Dẫn xuất nguồn gốc vật lý của quy tắc chọn lọc Δl = ±1:</b><br/>"
        "Theo lý thuyết nhiễu loạn lượng tử phụ thuộc thời gian (Quy tắc vàng Fermi), xác suất chuyển dời giữa trạng thái đầu |<i>i</i>⟩ "
        "và trạng thái cuối |<i>f</i>⟩ dưới tác dụng của sóng điện từ tỉ lệ với bình phương phần tử ma trận lưỡng cực điện <b>D</b><sub><i>fi</i></sub> = ⟨<i>f</i>|<i>e</i>·<b>r</b>|<i>i</i>⟩. "
        "Toán tử vị trí <b>r</b> có tính chẵn lẻ lẻ (odd parity) dưới phép nghịch đảo không gian (<b>r</b> → −<b>r</b>). "
        "Để tích phân không gian ∫ Ψ<sub><i>f</i></sub><sup>*</sup> <b>r</b> Ψ<sub><i>i</i></sub> <i>dV</i> khác 0, hàm dưới dấu tích phân "
        "bắt buộc phải là hàm chẵn, đòi hỏi Ψ<sub><i>f</i></sub> và Ψ<sub><i>i</i></sub> phải có tính chẵn lẻ trái ngược nhau. "
        "Vì tính chẵn lẻ của hàm cầu <i>Y<sub>lm</sub></i> là (−1)<sup><i>l</i></sup>, tích phân chỉ khác 0 khi <i>l<sub>f</sub></i> và <i>l<sub>i</sub></i> "
        "khác nhau một số lẻ, kết hợp với định luật bảo toàn momen photon (photon mang spin 1) dẫn tới điều kiện chặt chẽ Δ<i>l</i> = ±1."
    )
    step4_3_eq = r"\langle f | e \mathbf{r} | i \rangle = \int \Psi_f^*(\mathbf{r}) \, (e\mathbf{r}) \, \Psi_i(\mathbf{r}) \, dV \ne 0 \quad \Longleftrightarrow \quad \Delta l = \pm 1, \quad \Delta m_l \in \{0, \pm 1\}"
    story.append(he.build_intermediate_equation(step4_3_text, step4_3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g4_p4 = (
        "<b>Chuyển dời cấm và trạng thái giả bền (Metastable state):</b> Bước chuyển từ trạng thái 2s về 1s có Δ<i>l</i> = 0, "
        "vi phạm quy tắc chọn lọc lưỡng cực điện nên không thể phát xạ một photon đơn lẻ. "
        "Tuy nhiên, cơ học lượng tử bậc cao cho phép bước chuyển này xảy ra thông qua quá trình phát xạ đồng thời 2 photon "
        "(Two-photon emission) hoặc qua tương tác lưỡng cực từ (Magnetic dipole M1). "
        "Thời gian sống lượng tử của trạng thái kích thích 2p chỉ khoảng 1.6 ns (1.6 × 10<sup>−9</sup> s), "
        "trong khi trạng thái 2s có thời gian sống giả bền kéo dài tới xấp xỉ 0.12 s (lâu hơn gần 100 triệu lần!). "
        "Các trạng thái giả bền này đóng vai trò quyết định trong cơ chế tích lũy hạt tải để tạo nghịch đảo độ tích lũy trong laser.<br/>"
        "<b>Cấu trúc tinh tế (Fine structure) và dịch chuyển Lamb:</b> Khi xét hiệu ứng tương đối tính Dirac và tương tác spin – quỹ đạo <b>L·S</b>, "
        "mức năng lượng <i>E<sub>n</sub></i> bị tách thành các mức nhỏ hơn phụ thuộc vào <i>j</i> = <i>l</i> ± ½. "
        "Năm 1947, Willis Lamb phát hiện mức 2s<sub>½</sub> và 2p<sub>½</sub> chênh nhau một tần số cực nhỏ ~1057 MHz (Dịch chuyển Lamb), "
        "mở ra kỷ nguyên của Điện động lực học lượng tử (QED)."
    )
    story.append(he.make_paragraph(g4_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_title_4 = "Thử thách CER 2.4.4: Tại sao không thể có bước chuyển phát xạ 1 photon giữa 2s và 1s trong nguyên tử Hydro?"
    cer_claim_4 = (
        "Bước chuyển dời trực tiếp từ trạng thái kích thích 2s về trạng thái cơ bản 1s thông qua phát xạ một photon đơn sắc "
        "là một chuyển dời bị cấm hoàn toàn theo cơ chế bức xạ lưỡng cực điện (E1). Trạng thái 2s là một trạng thái giả bền."
    )
    cer_ev_4 = (
        "Trạng thái 2s có <i>l</i> = 0, trạng thái 1s có <i>l</i> = 0, dẫn tới độ biến thiên số lượng tử quỹ đạo là Δ<i>l</i> = 0 − 0 = 0. "
        "Quy tắc chọn lọc lưỡng cực điện bắt buộc Δ<i>l</i> = ±1. "
        "Tính toán phần tử ma trận lưỡng cực cho thấy: ⟨1s|<i>e·z</i>|2s⟩ = ∫ <i>R</i><sub>10</sub>(<i>r</i>)·<i>r</i>·<i>R</i><sub>20</sub>(<i>r</i>)·<i>r</i><sup>2</sup><i>dr</i> × ∫ <i>Y</i><sub>00</sub><sup>*</sup> cos<i>θ Y</i><sub>00</sub> <i>dΩ</i>. "
        "Tích phân phần góc ∫<sub>0</sub><sup><i>π</i></sup> cos<i>θ</i>·sin<i>θ·dθ</i> = tích phân góc triệt tiêu bằng 0, "
        "khiến phần tử ma trận triệt tiêu bằng 0 tuyệt đối."
    )
    cer_re_4 = (
        "Về mặt bản chất định luật bảo toàn, một photon ánh sáng luôn mang momen động lượng spin nội tại bằng chính xác 1ħ. "
        "Trước khi phát xạ, trạng thái 2s có momen quỹ đạo bằng 0. "
        "Nếu nó phát xạ 1 photon mang momen 1ħ và chuyển về trạng thái 1s cũng có momen quỹ đạo bằng 0, "
        "hệ thống sẽ vi phạm định luật bảo toàn momen động lượng (0 ≠ 0 + 1). "
        "Do đó, để bảo toàn momen động lượng, chuyển dời 2s → 1s buộc phải phát xạ đồng thời 2 photon có spin ngược chiều, "
        "giải thích tại sao xác suất chuyển dời cực kỳ nhỏ và thời gian sống của trạng thái 2s kéo dài phi thường."
    )
    cer_text_4 = (
        f"<b>{cer_title_4}:</b><br/>"
        f"• <b>[Khẳng định (Claim)]:</b> {cer_claim_4}<br/>"
        f"• <b>[Bằng chứng định lượng (Evidence)]:</b> {cer_ev_4}<br/>"
        f"• <b>[Lập luận vi mô (Reasoning)]:</b> {cer_re_4}<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến là coi các chuyển dời cấm là hoàn toàn không thể xảy ra trong tự nhiên. Thực chất chuyển dời chỉ bị cấm đối với cơ chế bức xạ lưỡng cực điện bậc nhất (E1); các kênh bậc cao hơn như phát xạ 2 photon hay lưỡng cực từ (M1) vẫn diễn ra với xác suất rất thấp."
    )
    story.append(he.make_paragraph(cer_text_4, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.4.5: PHỔ NĂNG LƯỢNG PHÂN TỬ: XẤP XỈ BORN – OPPENHEIMER, DAO ĐỘNG & QUAY
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.4.5: Phổ năng lượng phân tử: Xấp xỉ Born – Oppenheimer, Dao động &amp; Quay", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g5_p1 = (
        "Phân tử được cấu tạo từ nhiều nguyên tử liên kết với nhau thông qua các liên kết hóa học cộng hóa trị, ion hoặc kim loại. "
        "Khác với nguyên tử cô lập chỉ có chuyển động của electron quanh hạt nhân, trong phân tử luôn đồng thời tồn tại <b>ba dạng chuyển động</b> "
        "với các thang bậc không gian, thời gian và năng lượng phân tách rõ rệt:<br/>"
        "1. <i>Chuyển động của các electron</i> quanh hệ các hạt nhân → Trạng thái năng lượng điện tử (<i>E<sub>e</sub></i> ~ 1–10 eV, vùng UV – Khả kiến);<br/>"
        "2. <i>Chuyển động dao động của các hạt nhân</i> quanh vị trí cân bằng bền → Trạng thái năng lượng dao động (<i>E<sub>v</sub></i> ~ 0.05–0.5 eV, vùng Hồng ngoại IR);<br/>"
        "3. <i>Chuyển động quay của toàn bộ khung phân tử</i> như một khối thống nhất trong không gian → Trạng thái năng lượng quay (<i>E<sub>J</sub></i> ~ 10<sup>−4</sup>–10<sup>−2</sup> eV, vùng Vi ba / Hồng ngoại xa).<br/>"
        "Sự phân tách này được bảo đảm bởi <b>Xấp xỉ Born – Oppenheimer (1927)</b>: Do hạt nhân nguyên tử nặng hơn electron hàng nghìn lần (<i>M</i> ≫ <i>m</i>), "
        "electron chuyển động cực nhanh và tức thời tự điều chỉnh thích ứng với mọi vị trí tức thời của hạt nhân. "
        "Do đó, ta có thể giải riêng chuyển động electron trên nền khung hạt nhân cố định để tạo ra đường cong thế năng hiệu dụng <i>U</i>(<i>R</i>), "
        "sau đó mới giải bài toán dao động và quay của hạt nhân trên đường cong thế năng này."
    )
    story.append(he.make_paragraph(g5_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 08: Phổ dao động phân tử
    img_h08 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_08_Pho_Dao_Dong_Phan_Tu.png")
    cap_h08 = "Hình 2.4.10: Đường cong thế năng dao động phân tử hai nguyên tử và các mức năng lượng dao động điều hòa (Slide 52)."
    story.append(he.embed_figure_with_caption(img_h08, cap_h08, kind="orig", styles=styles))

    h08_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Đường cong thế năng liên kết U(R) dạng thế Morse hoặc thế parabol điều hòa thế năng điều hòa parabol bậc hai với các bậc thang năng lượng ngang cách đều."
    h08_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Trục hoành là khoảng cách liên kết hạt nhân R [Å]; trục tung là thế năng U(R) [eV]."
    h08_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Vị trí cực tiểu thế năng tại R = R<sub>e</sub> là khoảng cách liên kết cân bằng bền; độ sâu hố thế D<sub>e</sub> là năng lượng liên kết phân ly phân tử."
    h08_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Năng lượng điểm không (Zero-point energy) E<sub>0</sub> = 0.5·ħω > 0 bảo đảm phân tử luôn dao động ngay cả ở độ không tuyệt đối T = 0 K."
    h08_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Khi năng lượng kích thích tăng cao, đường cong thế năng lệch khỏi parabol điều hòa (hiệu ứng phi điều hòa anharmonicity), khoảng cách giữa các mức dao động co hẹp dần cho tới ngưỡng phân ly liên kết."
    story.append(he.make_paragraph(h08_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h08_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h08_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h08_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h08_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh gốc 09: Phổ quay phân tử
    img_h09 = os.path.join(kho_anh, "[Goc]_Muc_2.4_Hinh_09_Pho_Quay_Phan_Tu.png")
    cap_h09 = "Hình 2.4.11: Thang mức năng lượng quay phân tử E<sub>J</sub> = B<sub>0</sub>J(J+1) và phổ dải phân tử (Slide 53)."
    story.append(he.embed_figure_with_caption(img_h09, cap_h09, kind="orig", styles=styles))

    h09_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Thang mức năng lượng quay với khoảng cách giữa các mức dãn rộng dần theo tỉ lệ J(J+1); sơ đồ chuyển dời dải phổ."
    h09_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Số lượng tử quay J = 0, 1, 2, 3, 4, 5...; năng lượng tính theo cm<sup>−1</sup> hoặc meV."
    h09_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Chênh lệch năng lượng giữa hai mức quay liên tiếp ΔE = E<sub>J</sub> − E<sub>J−1</sub> = 2B<sub>0</sub>J tăng tuyến tính theo J."
    h09_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Hiệu ứng biến dạng ly tâm (Centrifugal distortion) −DJ<sup>2</sup>(J+1)<sup>2</sup> do lực ly tâm kéo dãn liên kết khi quay ở vận tốc góc cao."
    h09_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Phổ phân tử là quang phổ dải (Band spectra) gồm hàng nghìn vạch quay chen chúc trên mỗi bước chuyển dao động, khác biệt hoàn toàn với quang phổ vạch sắc nét của nguyên tử cô lập."
    story.append(he.make_paragraph(h09_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h09_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h09_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h09_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h09_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng đồ thị mô phỏng 03: MATLAB Dao động quay phân tử
    img_sim03 = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.4_Pho_Dao_Dong_Quay_Phan_Tu.png")
    cap_sim03 = "Hình 2.4.12: Mô phỏng MATLAB cấu trúc mức dao động – quay và phổ vạch hấp thụ phân tử hai nguyên tử với các nhánh P (ΔJ = −1) và nhánh R (ΔJ = +1)."
    story.append(he.embed_figure_with_caption(img_sim03, cap_sim03, kind="sim", styles=styles))

    h_sim03_ocr_1 = "<b>[Mắt xích OCR 1 — Thực thể thị giác]:</b> Biểu đồ kép: đồ thị trên biểu diễn các bước chuyển mức giữa hai trạng thái dao động v=0 và v=1; đồ thị dưới là phổ vạch hấp thụ phân tử thực tế."
    h_sim03_ocr_2 = "<b>[Mắt xích OCR 2 — Tọa độ &amp; Đơn vị]:</b> Số sóng / tần số chuyển dời theo cm<sup>−1</sup>; cường độ tương đối theo phân bố Boltzmann."
    h_sim03_ocr_3 = "<b>[Mắt xích OCR 3 — Hiện tượng &amp; Điểm uốn]:</b> Vạch gốc dải ν<sub>0</sub> (nhánh Q, ΔJ = 0) bị khuyết hoàn toàn; hai nhánh P (bên trái, tần số thấp hơn) và nhánh R (bên phải, tần số cao hơn) nằm đối xứng."
    h_sim03_ocr_4 = "<b>[Mắt xích OCR 4 — Cơ chế vi mô &amp; Tương tác]:</b> Khoảng cách giữa các vạch phổ kế tiếp nhau xấp xỉ bằng hằng số 2B<sub>0</sub>, cho phép xác định trực tiếp mômen quán tính phân tử."
    h_sim03_ocr_5 = "<b>[Mắt xích OCR 5 — Chẩn đoán kỹ thuật]:</b> Bao hình cường độ của các vạch có cực đại ở J ≈ 2–3 do sự cạnh tranh giữa độ suy biến tăng (2·J+1) và hàm suy giảm nhiệt Boltzmann hàm suy giảm nhiệt Boltzmann."
    story.append(he.make_paragraph(h_sim03_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(h_sim03_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(h_sim03_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(h_sim03_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(h_sim03_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 8))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g5_p2 = (
        "<b>Phương trình Schrödinger toàn phần của hệ phân tử:</b><br/>"
        "Hệ phân tử gồm <i>n</i> electron và <i>N</i> hạt nhân có phương trình:<br/>"
        "[ −∑<sub><i>i</i></sub> (ħ<sup>2</sup>/2<i>m</i>)·∇<sub><i>i</i></sub><sup>2</sup> − ∑<sub><i>j</i></sub> (ħ<sup>2</sup>/2<i>M<sub>j</sub></i>)·∇<sub><i>j</i></sub><sup>2</sup> + <i>U</i>(<b>r</b>, <b>R</b>) ] Ψ = <i>E·</i>Ψ.<br/>"
        "Theo Xấp xỉ Born – Oppenheimer, năng lượng toàn phần của phân tử tách thành tổng ba thành phần độc lập:<br/>"
        "<i>E</i><sub>total</sub> = <i>E<sub>e</sub></i> + <i>E<sub>v</sub></i> + <i>E<sub>J</sub></i>.<br/>"
        "Đối với phân tử hai nguyên tử có khối lượng hạt nhân <i>M</i><sub>1</sub> và <i>M</i><sub>2</sub> (khối lượng rút gọn khối lượng rút gọn <i>μ</i> của hai hạt nhân), "
        "năng lượng dao động trong gần đúng dao động điều hòa là:<br/>"
        "<i>E<sub>v</sub></i> = ħ<i>ω</i>·(<i>v</i> + 0.5), với <i>v</i> = 0, 1, 2... và tần số góc <i>ω</i> = căn bậc hai của tỉ số giữa độ cứng <i>K</i> và <i>μ</i>.<br/>"
        "Năng lượng quay trong mô hình rôto cứng (Rigid Rotor) với mômen quán tính <i>I</i><sub>0</sub> = <i>μ·R<sub>e</sub></i><sup>2</sup> là:<br/>"
        "<i>E<sub>J</sub></i> = <i>B</i><sub>0</sub>·<i>J</i>(<i>J</i> + 1), với <i>J</i> = 0, 1, 2... và hằng số quay hằng số quay <i>B</i><sub>0</sub> tỉ lệ nghịch với 2·<i>I</i><sub>0</sub>."
    )
    story.append(he.make_paragraph(g5_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    eq_mol = r"E_{\text{total}} = E_e + \hbar\omega \left( v + \frac{1}{2} \right) + B_0 J (J + 1), \quad B_0 = \frac{\hbar^2}{2 I_0}, \quad I_0 = \mu R_e^2"
    nom_mol = [
        ("Năng lượng toàn phần phân tử", "<i>E</i><sub>total</sub>", "eV", "Tổng năng lượng trạng thái điện tử, dao động hạt nhân và quay phân tử"),
        ("Năng lượng trạng thái điện tử", "<i>E<sub>e</sub></i>", "eV", "Năng lượng chuyển động của các electron trên khung hạt nhân cố định"),
        ("Lượng tử năng lượng dao động", "ħ<i>ω</i>", "eV", "Khoảng cách giữa các mức năng lượng dao động điều hòa phân tử"),
        ("Số lượng tử dao động", "<i>v</i>", "1", "Bậc năng lượng dao động hạt nhân quanh vị trí cân bằng (v = 0, 1, 2...)"),
        ("Hằng số quay phân tử", "<i>B</i><sub>0</sub>", "cm<sup>−1</sup>", "Hằng số quay tỉ lệ nghịch với mômen quán tính (B<sub>0</sub> tỉ lệ nghịch với 2·I<sub>0</sub>)"),
        ("Số lượng tử quay", "<i>J</i>", "1", "Bậc năng lượng quay của khối phân tử trong không gian (J = 0, 1, 2...)"),
        ("Mômen quán tính phân tử", "<i>I</i><sub>0</sub>", "kg·m<sup>2</sup>", "Mômen quán tính quanh trục vuông góc đường nối hai hạt nhân (I<sub>0</sub> = μ·R<sub>e</sub><sup>2</sup>)")
    ]
    story.append(he.build_target_equation_block(eq_mol, nom_mol, styles=styles))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step5_1_text = (
        "<b>Bước 1: Thiết lập quy tắc lựa chọn cho bước chuyển dao động – quay:</b><br/>"
        "Đối với phân tử hai nguyên tử có mômen lưỡng cực điện vĩnh cửu (ví dụ HCl, CO, NO), "
        "bước chuyển dời hấp thụ bức xạ hồng ngoại từ trạng thái dao động <i>v</i>'' = 0 lên <i>v</i>' = 1 tuân theo quy tắc chọn lọc: "
        "Δ<i>v</i> = +1 và Δ<i>J</i> = <i>J</i>' − <i>J</i>'' = ±1. "
        "Sự thay đổi số lượng tử quay phân tách phổ hấp thụ thành hai nhánh riêng biệt."
    )
    step5_1_eq = r"\Delta v = \pm 1, \quad \Delta J = J' - J'' = \pm 1 \quad \Longrightarrow \quad \begin{cases} \Delta J = -1: & \text{Nhánh P (P-branch)} \\ \Delta J = +1: & \text{Nhánh R (R-branch)} \end{cases}"
    story.append(he.build_intermediate_equation(step5_1_text, step5_1_eq, styles=styles, is_expanded_from_slide=True))

    step5_2_text = (
        "<b>Bước 2: Thiết lập phương trình tần số chuyển dời của nhánh P và nhánh R:</b><br/>"
        "Với nhánh R (Δ<i>J</i> = +1, <i>J</i>' = <i>J</i>'' + 1): Năng lượng photon hấp thụ là: "
        "ħ<i>ω<sub>R</sub></i> = ħ<i>ω</i><sub>0</sub> + <i>B</i><sub>0</sub>(<i>J</i>'' + 1)(<i>J</i>'' + 2) − <i>B</i><sub>0</sub><i>J</i>''(<i>J</i>'' + 1) = ħ<i>ω</i><sub>0</sub> + 2<i>B</i><sub>0</sub>(<i>J</i>'' + 1). "
        "Với nhánh P (Δ<i>J</i> = −1, <i>J</i>' = <i>J</i>'' − 1): Năng lượng photon hấp thụ là: "
        "ħ<i>ω<sub>P</sub></i> = ħ<i>ω</i><sub>0</sub> + <i>B</i><sub>0</sub>(<i>J</i>'' − 1)<i>J</i>'' − <i>B</i><sub>0</sub><i>J</i>''(<i>J</i>'' + 1) = ħ<i>ω</i><sub>0</sub> − 2<i>B</i><sub>0</sub><i>J</i>''."
    )
    step5_2_eq = r"\nu_R(J'') = \nu_0 + 2 B_0 (J'' + 1) \quad (J'' = 0, 1, 2, \dots), \quad \nu_P(J'') = \nu_0 - 2 B_0 J'' \quad (J'' = 1, 2, 3, \dots)"
    story.append(he.build_intermediate_equation(step5_2_text, step5_2_eq, styles=styles, is_expanded_from_slide=True))

    step5_3_text = (
        "<b>Bước 3: Xác định cấu trúc hình học phân tử từ khoảng cách vạch quang phổ:</b><br/>"
        "Hiệu tần số giữa hai vạch hấp thụ liên tiếp trong cùng một nhánh R hoặc nhánh P là: "
        "Δ<i>ν</i> = <i>ν<sub>R</sub></i>(<i>J</i>'' + 1) − <i>ν<sub>R</sub></i>(<i>J</i>'') = 2<i>B</i><sub>0</sub>. "
        "Bằng cách đo trực tiếp khoảng cách giữa các vạch trên phổ hấp thụ hồng ngoại thực nghiệm, "
        "ta suy ra chính xác hằng số quay <i>B</i><sub>0</sub>, từ đó tính được mômen quán tính mômen quán tính <i>I</i><sub>0</sub> tỉ lệ nghịch với 2·<i>B</i><sub>0</sub> "
        "và khoảng cách liên kết cân bằng hạt nhân <i>R<sub>e</sub></i> = căn bậc hai của tỉ số giữa <i>I</i><sub>0</sub> và <i>μ</i> với độ chính xác dưới 0.001 Å."
    )
    step5_3_eq = r"\Delta \nu = 2 B_0 \quad \Longrightarrow \quad I_0 = \frac{\hbar^2}{2 B_0} = \mu R_e^2 \quad \Longrightarrow \quad R_e = \sqrt{\frac{\hbar^2}{2 B_0 \mu}}"
    story.append(he.build_intermediate_equation(step5_3_text, step5_3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g5_p4 = (
        "<b>Ảnh hưởng của sự bất đối xứng nhiệt độ lên phân bố cường độ vạch quay:</b><br/>"
        "Cường độ tương đối của một vạch hấp thụ dao động – quay tỉ lệ với tích của hai yếu tố đối nghịch nhau: "
        "(1) Độ suy biến của mức quay ban đầu <i>g<sub>J</sub></i> = 2<i>J</i>'' + 1; và "
        "(2) Xác suất chiếm cứ trạng thái nhiệt động học theo phân bố Boltzmann hàm phân bố nhiệt Boltzmann:<br/>"
        "<i>I</i>(<i>J</i>'') ∝ (2<i>J</i>'' + 1)·hàm phân bố Boltzmann của các mức quay.<br/>"
        "Khi <i>J</i>'' nhỏ, thừa số suy biến (2<i>J</i>'' + 1) tăng tuyến tính chiếm ưu thế, làm cường độ vạch tăng dần. "
        "Khi <i>J</i>'' lớn, hàm mũ Boltzmann suy giảm cực nhanh kéo cường độ vạch triệt tiêu. "
        "Cực đại của bao hình cường độ xuất hiện tại giá trị <i>J</i><sub>max</sub> phụ thuộc căn bậc hai của nhiệt độ T. "
        "Đặc tính này cho phép các nhà quang phổ học đo đạc chính xác nhiệt độ khí quy mô vi mô từ phổ hấp thụ phân tử.<br/>"
        "<b>Phân tử đồng nhân và quy tắc cấm nhánh Q:</b> Đối với phân tử hai nguyên tử đồng nhân (như H<sub>2</sub>, N<sub>2</sub>, O<sub>2</sub>), "
        "do tính đối xứng tâm hoàn hảo, phân tử không có mômen lưỡng cực điện vĩnh cửu (<i>μ</i><sub>0</sub> = 0), "
        "dẫn tới các bước chuyển dao động và quay thuần túy bị cấm hoàn toàn trong phổ hồng ngoại (chúng chỉ quan sát được qua phổ tán xạ Raman). "
        "Đối với phân tử dị nhân trạng thái <sup>1</sup>Σ (như HCl, CO), do momen động lượng orbital của electron bằng 0 dọc trục phân tử, "
        "bước chuyển Δ<i>J</i> = 0 (nhánh Q) bị cấm ngặt nghèo, tạo thành một khe trống đặc trưng tại đúng tần số dao động gốc <i>ν</i><sub>0</sub>."
    )
    story.append(he.make_paragraph(g5_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_title_5 = "Thử thách CER 2.4.5: Giải mã sự vắng mặt của nhánh Q trong phổ hấp thụ dao động – quay của khí HCl"
    cer_claim_5 = (
        "Trong phổ hấp thụ hồng ngoại dao động – quay của phân tử khí HCl, vạch phổ tại đúng tần số dao động trung tâm <i>ν</i><sub>0</sub> "
        "(tương ứng bước chuyển nhánh Q với Δ<i>J</i> = 0) hoàn toàn biến mất, để lại một khoảng trống có độ rộng xấp xỉ 4<i>B</i><sub>0</sub> "
        "giữa vạch đầu tiên của nhánh P và nhánh R."
    )
    cer_ev_5 = (
        "Trạng thái điện tử cơ bản của phân tử HCl là trạng thái <sup>1</sup>Σ<sup>+</sup> (momen động lượng electron chiếu lên trục phân tử bằng 0: Λ = 0). "
        "Toán tử mômen lưỡng cực điện chuyển dời dọc trục liên kết phân tử <b>D</b> có hình chiếu momen động lượng lên trục bằng 0. "
        "Khi tính toán phần tử ma trận lưỡng cực cho chuyển dời quay giữa hai trạng thái |<i>J</i>'', <i>M</i>''⟩ và |<i>J</i>', <i>M</i>'⟩: "
        "Phần tích phân góc phụ thuộc vào hệ số Clebsch – Gordan ⟨<i>J</i>'', 1, 0, 0 | <i>J</i>', 0⟩. "
        "Với <i>J</i>' = <i>J</i>'', hệ số Clebsch – Gordan này triệt tiêu bằng 0 tuyệt đối đối với mọi trạng thái có Λ = 0."
    )
    cer_re_5 = (
        "Về mặt vật lý bảo toàn, khi một photon ánh sáng bị hấp thụ bởi phân tử, photon mang theo một đơn vị lượng tử momen động lượng (spin 1ħ). "
        "Vì phân tử HCl ở trạng thái <sup>1</sup>Σ không có momen động lượng electron tự do nào để bù trừ cho spin của photon, "
        "toàn bộ momen 1ħ của photon bắt buộc phải được chuyển giao trực tiếp cho chuyển động quay của khung hạt nhân phân tử. "
        "Do đó, trạng thái quay của phân tử bắt buộc phải thay đổi đúng một đơn vị lượng tử: <i>J</i>' = <i>J</i>'' + 1 (nhánh R) "
        "hoặc <i>J</i>' = <i>J</i>'' − 1 (nhánh P). Bước chuyển giữ nguyên số lượng tử quay <i>J</i>' = <i>J</i>'' (Δ<i>J</i> = 0) "
        "sẽ vi phạm định luật bảo toàn momen động lượng toàn phần của hệ, giải thích tại sao nhánh Q hoàn toàn biến mất."
    )
    cer_text_5 = (
        f"<b>{cer_title_5}:</b><br/>"
        f"• <b>[Khẳng định (Claim)]:</b> {cer_claim_5}<br/>"
        f"• <b>[Bằng chứng định lượng (Evidence)]:</b> {cer_ev_5}<br/>"
        f"• <b>[Lập luận vi mô (Reasoning)]:</b> {cer_re_5}<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù là cho rằng mọi phân tử đều không có nhánh Q. Đối với các phân tử có momen động lượng electron khác 0 quanh trục liên kết (trạng thái Π như NO), nhánh Q vẫn xuất hiện mạnh mẽ do momen photon được bù trừ bởi trạng thái electron."
    )
    story.append(he.make_paragraph(cer_text_5, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # BẢNG TỔNG KẾT SO SÁNH QUANG PHỔ NGUYÊN TỬ VÀ PHÂN TỬ
    # =========================================================================
    story.append(he.make_paragraph("Tổng kết đối sánh: Phổ năng lượng Nguyên tử và Phân tử", styles["H2"]))
    story.append(Spacer(1, 4))

    summary_intro = (
        "Bảng tổng hợp dưới đây hệ thống hóa các đặc trưng vật lý cốt lõi, cơ chế giam cầm, bậc năng lượng "
        "và quy tắc lựa chọn quang học giữa hai hệ lượng tử nguyên tử và phân tử trong vật lý nano:"
    )
    story.append(he.make_paragraph(summary_intro, styles["Body"]))
    story.append(Spacer(1, 6))

    table_data = [
        [
            Paragraph("<b>Tiêu chí đối sánh</b>", styles["TableHeader"]),
            Paragraph("<b>Hệ Nguyên tử (Hydro &amp; Kim loại kiềm)</b>", styles["TableHeader"]),
            Paragraph("<b>Hệ Phân tử (Hai nguyên tử dị nhân)</b>", styles["TableHeader"])
        ],
        [
            Paragraph("<b>Trường thế giam cầm</b>", styles["TableCell"]),
            Paragraph("Thế Coulomb đối xứng cầu tâm thế Coulomb đối xứng cầu tỉ lệ với −<i>r</i><sup>−1</sup>", styles["TableCell"]),
            Paragraph("Đường cong thế liên kết hóa học hiệu dụng Born – Oppenheimer <i>U</i>(<i>R</i>)", styles["TableCell"])
        ],
        [
            Paragraph("<b>Hệ số lượng tử đặc trưng</b>", styles["TableCell"]),
            Paragraph("Bộ bốn số lượng tử: <i>n</i>, <i>l</i>, <i>m<sub>l</sub></i>, <i>m<sub>s</sub></i>", styles["TableCell"]),
            Paragraph("Số lượng tử điện tử, dao động <i>v</i>, và quay <i>J</i> (kèm hình chiếu <i>M</i>)", styles["TableCell"])
        ],
        [
            Paragraph("<b>Dạng hình học quang phổ</b>", styles["TableCell"]),
            Paragraph("Quang phổ vạch rời rạc sắc nét (Line spectrum)", styles["TableCell"]),
            Paragraph("Quang phổ dải (Band spectrum: điện tử – dao động – quay)", styles["TableCell"])
        ],
        [
            Paragraph("<b>Thang bậc chênh lệch năng lượng</b>", styles["TableCell"]),
            Paragraph("Δ<i>E</i> ~ 1–10 eV (Vùng tử ngoại UV và khả kiến)", styles["TableCell"]),
            Paragraph("Điện tử: 1–10 eV; Dao động: 0.1–0.5 eV; Quay: 10<sup>−4</sup>–10<sup>−2</sup> eV", styles["TableCell"])
        ],
        [
            Paragraph("<b>Quy tắc lựa chọn quang học cốt lõi</b>", styles["TableCell"]),
            Paragraph("Δ<i>l</i> = ±1; Δ<i>S</i> = 0; Δ<i>J</i> = 0, ±1 (0 ↛ 0)", styles["TableCell"]),
            Paragraph("Δ<i>v</i> = ±1; Δ<i>J</i> = ±1 (Nhánh P và R; cấm nhánh Q nếu Λ = 0)", styles["TableCell"])
        ],
        [
            Paragraph("<b>Ứng dụng mũi nhọn trong công nghệ nano</b>", styles["TableCell"]),
            Paragraph("Chấm lượng tử bán dẫn (Quantum Dots) mô phỏng nguyên tử nhân tạo", styles["TableCell"]),
            Paragraph("Cảm biến quang học phân tử nano, quang phổ hấp thụ hồng ngoại FTIR", styles["TableCell"])
        ]
    ]

    col_widths = [110, 205, 205]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), he.COLOR_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, he.COLOR_BORDER_GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8F9FA")])
    ]))
    story.append(t)
    story.append(Spacer(1, 14))

    # =========================================================================
    # LỜI KẾT KHOA HỌC & ĐỊNH HƯỚNG BÀI TIẾP THEO
    # =========================================================================
    conclusion_text = (
        "<b>Lời kết khoa học:</b> Chuyên khảo Mục 2.4 đã hoàn thành việc dẫn xuất và thiết lập hệ thống tri thức "
        "toàn diện về phổ năng lượng của các hệ hạt lượng tử từ nguyên tử đơn lẻ đến hệ phân tử hai nguyên tử. "
        "Quy luật lượng tử hóa mức năng lượng, các điều kiện đối xứng không gian chi phối hình dạng orbital, "
        "Nguyên lý Pauli bảo đảm cấu trúc vỏ electron và các quy tắc lựa chọn quang học chính là những cột trụ vật lý bất biến "
        "chuẩn bị trực tiếp cho việc nghiên cứu Mục 2.5: <i>Mô hình hạt trong giếng thế lượng tử 1D, 2D, 3D</i> "
        "và Mục 2.6: <i>Hiệu ứng xuyên hầm lượng tử qua rào thế hữu hạn</i> — những hiện tượng nền tảng "
        "trực tiếp chế tạo các linh kiện nano bán dẫn đỉnh cao như Dây nano (Nanowires), Chấm lượng tử (Quantum Dots) "
        "và Đi-ốt xuyên hầm cộng hưởng (RTD)."
    )
    story.append(he.make_paragraph(conclusion_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # Build tài liệu sử dụng phương thức an toàn của hust_pdf_engine
    print("Đang tiến hành build PDF với BookmarkDocTemplate (2 passes)...")
    doc.build(story)
    print(f"Hoàn thành xuất bản tài liệu chuyên khảo: {target_pdf}")

if __name__ == "__main__":
    build_pdf()

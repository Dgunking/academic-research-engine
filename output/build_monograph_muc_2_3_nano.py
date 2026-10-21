# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Chương 2: Bản chất lượng tử của thế giới nano
Mục 2.3: Hàm sóng, bó sóng và nguyên lý bất định Heisenberg (Slide 20–27)
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

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding="utf-8")

def build_pdf():
    # 1. Đường dẫn thư mục & tệp đích
    drive_base = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano"
    kho_anh = os.path.join(drive_base, "Kho_Hinh_Anh")
    bai_giang = os.path.join(drive_base, "Bai_Giang_Dong_Goi")
    os.makedirs(bai_giang, exist_ok=True)
    target_pdf = os.path.join(bai_giang, "Chuyen_Khao_Nano_Muc_2.3.pdf")

    print(f"Bắt đầu biên dịch chuyên khảo Mục 2.3: {target_pdf}")

    # 2. Khởi tạo Styles và Document Template
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(target_pdf)
    story = []

    # =========================================================================
    # TIÊU ĐỀ ĐẦU CHUYÊN KHẢO (H1)
    # =========================================================================
    title_main = (
        "CHƯƠNG 2: BẢN CHẤT LƯỢNG TỬ CỦA THẾ GIỚI NANO<br/>"
        "MỤC 2.3: HÀM SÓNG, BÓ SÓNG VÀ NGUYÊN LÝ BẤT ĐỊNH HEISENBERG"
    )
    story.append(he.make_paragraph(title_main, styles["H1"]))
    story.append(Spacer(1, 4))

    meta_info = (
        "<b>Hệ Thống Chuyên Khảo Giảng Dạy &amp; Nghiên Cứu Vật Lý Nano — ĐHBK Hà Nội</b><br/>"
        "<i>Chủ thể nghiên cứu:</i> Bùi Trung Dũng — Khoa Vật lý Kỹ thuật, Trường Đại học Bách khoa Hà Nội (HUST)<br/>"
        "<i>Tài liệu nguồn kép:</i> Bài giảng 'Bài 2-Quantum nature.pdf' (Slide 20–27), Bộ môn Vật liệu Điện tử — Viện Vật lý Kỹ thuật HUST; "
        "kết hợp các chuyên khảo quốc tế đỉnh cao: Griffiths &amp; Schroeter (<i>Introduction to Quantum Mechanics</i>), "
        "Poole &amp; Owens (<i>Introduction to Nanotechnology</i>), Wolf (<i>Nanophysics</i>)."
    )
    story.append(he.make_paragraph(meta_info, styles["Body"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=he.COLOR_PRIMARY, spaceBefore=4, spaceAfter=10))

    # =========================================================================
    # LỜI NÓI ĐẦU ĐỊNH VỊ HỌC THUẬT & TỔNG QUAN
    # =========================================================================
    overview_text = (
        "<b>Lời nói đầu định vị học thuật:</b> Sau khi bản chất sóng của vật chất được khẳng định không thể tranh cãi qua các thí nghiệm "
        "nhiễu xạ của Davisson, Germer và Thomson, câu hỏi trung tâm mang tính cách mạng của vật lý hiện đại trỗi dậy: "
        "<i>Bản chất toán học và ý nghĩa vật lý thực sự của sóng vật chất là gì?</i> "
        "Sóng de Broglie không phải là sóng cơ học (như sóng âm hay sóng nước đòi hỏi môi trường đàn hồi), cũng không phải là sóng điện từ "
        "(vì electron không bức xạ năng lượng liên tục khi chuyển động đều). "
        "Câu trả lời đã khai sinh ra Cơ học lượng tử thông qua ba trụ cột nhận thức vĩ đại:<br/>"
        "(1) <i>Hàm sóng trạng thái phức và Tiên đề xác suất Max Born (1926):</i> Hàm sóng <i>Ψ</i>(<b>r</b>, <i>t</i>) không đại diện cho một thực thể vật chất phân tán "
        "mà là một trường biên độ xác suất; bình phương môđun |<i>Ψ</i>|<sup>2</sup> biểu diễn mật độ xác suất tìm thấy hạt vi mô trong không gian.<br/>"
        "(2) <i>Khái niệm Bó sóng (Wave Packet) và Sự định xứ vi hạt:</i> Vi hạt không phải là một sóng phẳng đơn sắc vô hạn mà là một nhóm sóng chồng chập Fourier; "
        "tâm bó sóng chuyển động với vận tốc nhóm <i>v</i><sub>g</sub> hoàn toàn trùng khớp với vận tốc hạt cổ điển.<br/>"
        "(3) <i>Nguyên lý bất định Heisenberg (1927) và Phương trình vi phân Schrödinger (1926):</i> Giới hạn căn bản của tự nhiên đối với sự định xứ đồng thời "
        "vị trí và động lượng, dẫn tới hệ quả giam cầm lượng tử bùng nổ năng lượng trong các cấu trúc nano dưới 10 nm. "
        "Chuyên khảo Mục 2.3 bóc tách trọn vẹn 5 Luận điểm Vi mô (MPT) theo chuẩn mực sư phạm 5 giai đoạn lũy tiến, "
        "dẫn xuất tường minh từng phương trình từ nguyên lý đầu và minh họa bằng đồ thị giải tích kỹ thuật chuẩn MATLAB R2014b+."
    )
    story.append(he.make_paragraph(overview_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # =========================================================================
    # LUẬN ĐIỂM 2.3.1: HÀM SÓNG PHẲNG DE BROGLIE DẠNG PHỨC & Ý NGHĨA VẬT LÝ
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.3.1: Hàm sóng phẳng de Broglie dạng phức &amp; Ý nghĩa vật lý", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g1_p1 = (
        "Trong vật lý sóng cổ điển, sự lan truyền của một dao động điều hòa trong không gian và thời gian được biểu diễn qua phương trình sóng thực "
        "<i>D</i>(<i>x</i>, <i>t</i>) = <i>A</i> cos(<i>ωt</i> − <i>kx</i> + <i>α</i>). "
        "Tuy nhiên, đối với một vi hạt tự do chuyển động với động lượng xác định <b>p</b> và năng lượng toàn phần xác định <i>E</i>, "
        "Louis de Broglie đã thiết lập mô hình sóng vật chất phẳng đơn sắc tương ứng. "
        "Để mô tả đồng thời cả biên độ, pha dao động và thỏa mãn tính tuyến tính của nguyên lý chồng chất lượng tử, "
        "hàm sóng bắt buộc phải được mở rộng sang trường số phức theo công thức Euler."
    )
    story.append(he.make_paragraph(g1_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc giao thoa photon/electron tích lũy theo thời gian từ slide 22
    img_wf_orig = os.path.join(kho_anh, "[Goc]_Muc_2.3_Hinh_01_Giao_Thoa_Van_Sang_Toi_Photon.png")
    cap_wf_orig = "Hình 2.3.1: Ảnh thực nghiệm giao thoa vân sáng tối của photon/electron: sự tích lũy dần từng vết hạt riêng lẻ hình thành cấu trúc giao thoa xác suất thống kê."
    story.append(he.embed_figure_with_caption(img_wf_orig, cap_wf_orig, kind="orig", styles=styles))

    wf_ocr_1 = "Giai đoạn đầu khi số lượng hạt ít: các chấm sáng xuất hiện ngẫu nhiên rải rác trên màn chắn như các hạt độc lập."
    wf_ocr_2 = "Giai đoạn tích lũy trung gian: mật độ hạt bắt đầu tập trung dày đặc tại một số dải không gian nhất định."
    wf_ocr_3 = "Giai đoạn dài hạn khi thông lượng hạt lớn: các dải vân giao thoa cực đại cực tiểu sáng tối xen kẽ hiện rõ hoàn hảo."
    wf_ocr_4 = "Tính chất nghịch lý lượng tử: mỗi hạt vi mô đơn lẻ tự giao thoa với chính bản thân nó qua cả hai khe chắn."
    wf_ocr_5 = "Vân sáng tương ứng vùng có xác suất rơi vào cao nhất; vân tối tương ứng vùng biên độ hàm sóng bị triệt tiêu hoàn toàn."
    story.append(he.make_paragraph(wf_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(wf_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(wf_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(wf_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(wf_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g1_p2 = (
        "<b>Hạt nhân vật lý — Dạng hàm phức chuẩn tắc của sóng phẳng de Broglie:</b> "
        "Hàm sóng của một vi hạt tự do chuyển động dọc theo trục <i>x</i> mang động lượng <i>p</i> = <i>ħk</i> và năng lượng <i>E</i> = <i>ħω</i> "
        "được mô tả bằng một hàm mũ phức thuần nhất. Mặt đồng pha của sóng là các mặt phẳng vuông góc với phương truyền sóng, "
        "do đó hàm sóng mang tính chất phẳng (Plane Wave):"
    )
    story.append(he.make_paragraph(g1_p2, styles["Body"]))

    eq_wf = r"\Psi(\vec{r}, t) = A \exp\left( i(\vec{k}\cdot\vec{r} - \omega t) \right) = A \exp\left( \frac{i}{\hbar}(\vec{p}\cdot\vec{r} - E t) \right)"
    nom_wf = [
        ("Hàm sóng trạng thái vi mô", "<i>Ψ</i>(<b>r</b>, <i>t</i>)", "m<sup>−3/2</sup>", "Hàm giải tích phức chứa đựng toàn bộ thông tin vật lý của hệ hạt"),
        ("Véctơ sóng", "<b>k</b>", "rad/m", "Độ lớn bằng 2<i>π</i> nhân nghịch đảo bước sóng <i>λ</i>; chỉ phương truyền sóng"),
        ("Tần số góc", "<i>ω</i>", "rad/s", "Tần số biến thiên pha thời gian: liên hệ với năng lượng qua <i>E</i> = <i>ħω</i>"),
        ("Hằng số Planck rút gọn", "<i>ħ</i>", "J·s", "Hằng số lượng tử Dirac: 1.054571817 × 10<sup>−34</sup> J·s"),
        ("Biên độ chuẩn hóa", "<i>A</i>", "m<sup>−3/2</sup>", "Hệ số biên độ xác định mật độ hạt trong không gian chuẩn hóa")
    ]
    story.append(he.build_target_equation_block(eq_wf, nom_wf, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    wf_step1_txt = (
        "Xuất phát từ hàm dao động cơ học điều hòa một chiều lan truyền theo chiều dương trục <i>x</i>: <i>D</i>(<i>x</i>, <i>t</i>) = <i>A</i> cos(<i>ωt</i> − <i>kx</i>). "
        "Áp dụng hệ thức Euler exp(<i>iφ</i>) = cos <i>φ</i> + <i>i</i> sin <i>φ</i> để biểu diễn dưới dạng phần thực của hàm mũ phức:"
    )
    wf_step1_eq = r"D(x, t) = \mathrm{Re}\left[ A \exp(-i(\omega t - kx)) \right] = \mathrm{Re}\left[ A \exp(i(kx - \omega t)) \right]"
    story.append(he.build_intermediate_equation(wf_step1_txt, wf_step1_eq, styles=styles, is_expanded_from_slide=True))

    wf_step2_txt = (
        "Liên kết các tham số sóng (<i>ω</i>, <i>k</i>) với các đại lượng cơ học lượng tử (<i>E</i>, <i>p</i>) thông qua hệ thức Einstein - de Broglie: "
        "<i>E</i> = <i>hν</i> = <i>ħω</i> suy ra <i>ω</i> = <i>E</i>·<i>ħ</i><sup>−1</sup>; và <i>p</i> = <i>h</i>·<i>λ</i><sup>−1</sup> = <i>ħk</i> suy ra <i>k</i> = <i>p</i>·<i>ħ</i><sup>−1</sup>:"
    )
    wf_step2_eq = r"\omega = \frac{E}{\hbar}, \quad k = \frac{p}{\hbar} \implies kx - \omega t = \frac{p x - E t}{\hbar}"
    story.append(he.build_intermediate_equation(wf_step2_txt, wf_step2_eq, styles=styles, is_expanded_from_slide=True))

    wf_step3_txt = (
        "Mở rộng sang không gian ba chiều bằng cách thay thế tích vô hướng <i>px</i> bằng <b>p</b>·<b>r</b> và số sóng <i>kx</i> bằng <b>k</b>·<b>r</b>, "
        "thu được hàm sóng phẳng de Broglie tổng quát trong không gian ba chiều:"
    )
    wf_step3_eq = r"\Psi(\vec{r}, t) = A \exp\left( \frac{i}{\hbar}(\vec{p}\cdot\vec{r} - E t) \right) = A \exp(i\vec{k}\cdot\vec{r})\exp\left( -i\frac{Et}{\hbar} \right)"
    story.append(he.build_intermediate_equation(wf_step3_txt, wf_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g1_p4 = (
        "<b>Đặc tính tiệm cận của sóng phẳng đơn sắc:</b><br/>"
        "• <i>Sự không định xứ hoàn toàn (Complete Delocalization):</i> Mật độ biên độ của sóng phẳng |<i>Ψ</i>(<i>x</i>, <i>t</i>)|<sup>2</sup> = |<i>A</i>|<sup>2</sup> "
        "là một hằng số bất biến ở mọi điểm trong vũ trụ từ −∞ đến +∞. Một hạt có động lượng <i>p</i> xác định tuyệt đối (Δ<i>p</i> = 0) "
        "thì vị trí của nó hoàn toàn bất định (Δ<i>x</i> → ∞).<br/>"
        "• <i>Vấn đề chuẩn hóa sóng phẳng:</i> Vì tích phân |<i>A</i>|<sup>2</sup> trên toàn bộ không gian vô hạn phân kỳ tới vô cùng, "
        "sóng phẳng đơn sắc lý tưởng không thể chuẩn hóa theo nghĩa thông thường (không phải hàm khả tích bình phương). "
        "Trong vật lý thực tế, một hạt luôn tồn tại dưới dạng một bó sóng định xứ có độ rộng hữu hạn."
    )
    story.append(he.make_paragraph(g1_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_wf = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Hàm sóng trong cơ học lượng tử bắt buộc phải là một hàm giải tích phức (Complex Function), "
        "không thể thuần túy chọn một hàm thực như sóng âm hay sóng điện từ cổ điển.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Phương trình vi phân Schrödinger chứa đơn vị ảo <i>i</i> ở đạo hàm thời gian bậc nhất: "
        "<i>iħ</i> (đạo hàm riêng thời gian của <i>Ψ</i>) = <i>ĤΨ</i>. Nếu <i>Ψ</i> là hàm thuần thực, vế trái là một số thuần ảo trong khi vế phải (với thế năng thực <i>V</i>) "
        "lại là một số thực, dẫn tới mâu thuẫn toán học không thể dung hòa.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Đơn vị ảo <i>i</i> phản ánh mối liên kết nội tại giữa hai bậc tự do dao động trực giao (phần thực và phần ảo). "
        "Chính sự tồn tại của pha lượng tử phức cho phép xuất hiện dòng mật độ xác suất <b>j</b> và các hiện tượng giao thoa sóng lượng tử. "
        "Nếu loại bỏ số phức, cơ học lượng tử sẽ mất đi toàn bộ bản chất động học sóng.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến là ngộ nhận rằng các đại lượng đo đạc vật lý có thể là số phức. "
        "Bản thân hàm sóng <i>Ψ</i> không phải là đại lượng quan sát trực tiếp được bằng mắt hay detector; mọi giá trị đo đạc thực nghiệm "
        "(năng lượng, vị trí, động lượng, mật độ xác suất |<i>Ψ</i>|<sup>2</sup>) bắt buộc đều là các số thực, tương ứng với các giá trị riêng "
        "của các toán tử Hermitian."
    )
    story.append(he.make_paragraph(cer_wf, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.3.2: TIÊN ĐỀ XÁC SUẤT MAX BORN & ĐIỀU KIỆN CHUẨN HÓA HÀM SÓNG
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.3.2: Tiên đề xác suất Max Born &amp; Điều kiện chuẩn hóa hàm sóng", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g2_p1 = (
        "Năm 1926, nhà vật lý Max Born tại Đại học Göttingen đã đề xuất cách giải thích xác suất thống kê mang tính nền tảng cho cơ học lượng tử "
        "(đoạt giải Nobel Vật lý năm 1954). "
        "Born nhận định rằng hàm sóng <i>Ψ</i>(<b>r</b>, <i>t</i>) không mô tả một đám mây điện tích hay một trường vật chất cơ học loãng, "
        "mà là một <i>trường biên độ xác suất</i> (Probability Amplitude). "
        "Bản thân hàm sóng <i>Ψ</i> là một số phức và không mang ý nghĩa đo lường trực tiếp, nhưng bình phương môđun của nó "
        "|<i>Ψ</i>(<b>r</b>, <i>t</i>)|<sup>2</sup> = <i>Ψ</i><sup>*</sup><i>Ψ</i> là một đại lượng thực không âm, "
        "biểu thị <i>mật độ xác suất</i> (Probability Density) tìm thấy hạt tại vị trí <b>r</b> vào thời điểm <i>t</i>."
    )
    story.append(he.make_paragraph(g2_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng đồ thị mô phỏng tiên đề Born và giao thoa 2 khe
    img_born_sim = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.3_Mat_Do_Xac_Suat_Born_Va_Ham_Song.png")
    cap_born_sim = "Hình 2.3.2: Đồ thị mô phỏng giải tích MATLAB tiên đề xác suất Max Born: (a) Phần thực, phần ảo và mật độ xác suất |Psi|^2; (b) Giao thoa lượng tử hai khe so với cộng xác suất cổ điển."
    story.append(he.embed_figure_with_caption(img_born_sim, cap_born_sim, kind="sim", styles=styles))

    born_ocr_1 = "Đường cong phần thực Re[Psi] và phần ảo Im[Psi] dao động lệch pha pi/2 bên trong đường bao hàm Gauss."
    born_ocr_2 = "Mật độ xác suất Born |Psi|^2 là hàm thực dương hoàn toàn, đóng vai trò hàm phân bố thống kê vị trí."
    born_ocr_3 = "Diện tích tích phân gạch chéo dưới đường cong mật độ xác suất đúng bằng 100% theo điều kiện chuẩn hóa."
    born_ocr_4 = "Đặc tuyến giao thoa hai khe lượng tử xuất hiện số hạng kết hợp 2*Re[Psi1* Psi2] tạo các gợn sóng cực đại cực tiểu."
    born_ocr_5 = "Đường nét đứt cộng xác suất cổ điển P1 + P2 hoàn toàn trơn nhẵn, thất bại trong việc mô tả hiện tượng giao thoa."
    story.append(he.make_paragraph(born_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(born_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(born_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(born_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(born_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g2_p2 = (
        "<b>Hạt nhân vật lý — Ý nghĩa xác suất và Điều kiện chuẩn hóa:</b> Xác suất <i>dP</i> để tìm thấy hạt vi mô trong một phần tử thể tích vi phân "
        "<i>dV</i> = <i>dx dy dz</i> quanh điểm <b>r</b> vào thời điểm <i>t</i> tỷ lệ thuận với thể tích <i>dV</i> và mật độ xác suất |<i>Ψ</i>|<sup>2</sup>. "
        "Vì hạt chắc chắn phải tồn tại ở một nơi nào đó trong toàn bộ không gian vô hạn, tổng xác suất tìm thấy hạt trên toàn vũ trụ bắt buộc phải bằng 1 (100%):"
    )
    story.append(he.make_paragraph(g2_p2, styles["Body"]))

    eq_born = r"dP = |\Psi(\vec{r}, t)|^2 dV = \Psi^*(\vec{r}, t)\Psi(\vec{r}, t) dV \quad \text{và} \quad \int_{-\infty}^{\infty} |\Psi(\vec{r}, t)|^2 dV = 1"
    nom_born = [
        ("Xác suất vi phân", "<i>dP</i>", "không thứ nguyên", "Xác suất định xứ vi hạt trong lân cận thể tích vi phân dV"),
        ("Mật độ xác suất Born", "|<i>Ψ</i>(<b>r</b>, <i>t</i>)|<sup>2</sup>", "m<sup>−3</sup>", "Bình phương độ lớn hàm sóng, đại lượng đo lường xác suất trên đơn vị thể tích"),
        ("Hàm liên hợp phức", "<i>Ψ</i><sup>*</sup>", "m<sup>−3/2</sup>", "Số phức liên hợp thu được bằng cách đổi dấu đơn vị ảo i thành −i"),
        ("Phần tử thể tích không gian", "<i>dV</i> = <i>dx dy dz</i>", "m<sup>3</sup>", "Vi phân thể tích toạ độ Descartes ba chiều"),
        ("Điều kiện chuẩn hóa toàn phần", "∫ |<i>Ψ</i>|<sup>2</sup> <i>dV</i> = 1", "không thứ nguyên", "Bảo toàn xác suất tổng thể của trạng thái lượng tử")
    ]
    story.append(he.build_target_equation_block(eq_born, nom_born, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    born_step1_txt = (
        "Thiết lập phép phân tích tương tự giữa quang học sóng và cơ học lượng tử. Trong điện từ học cổ điển, cường độ bức xạ ánh sáng "
        "<i>I</i> = <i>ε</i><sub>0</sub> <i>c</i> <i>E</i><sup>2</sup> tỷ lệ thuận với bình phương biên độ điện trường. Mặt khác, theo thuyết hạt photon, "
        "cường độ chùm sáng tỷ lệ thuận với mật độ thông lượng photon <i>N</i>: <i>I</i> = <i>Nhν</i>. "
        "Do đó, mật độ photon tới tỷ lệ thuận với bình phương biên độ dao động sóng: <i>N</i> ∝ <i>E</i><sup>2</sup>."
    )
    born_step1_eq = r"I = \epsilon_0 c \mathcal{E}^2 = N h\nu \implies N \propto \mathcal{E}^2"
    story.append(he.build_intermediate_equation(born_step1_txt, born_step1_eq, styles=styles, is_expanded_from_slide=True))

    born_step2_txt = (
        "Mở rộng sang sóng vật chất de Broglie. Đối với hạt có khối lượng, đại lượng dao động trường điện từ <i>E</i> được thay thế bằng hàm sóng <i>Ψ</i>. "
        "Vì <i>Ψ</i> là số phức, bình phương biên độ thực được biểu diễn qua tích số của hàm sóng với liên hợp phức của nó:"
    )
    born_step2_eq = r"|\Psi(\vec{r}, t)|^2 = \Psi^*(\vec{r}, t) \cdot \Psi(\vec{r}, t) = \left( \mathrm{Re}[\Psi] \right)^2 + \left( \mathrm{Im}[\Psi] \right)^2 \ge 0"
    story.append(he.build_intermediate_equation(born_step2_txt, born_step2_eq, styles=styles, is_expanded_from_slide=True))

    born_step3_txt = (
        "Dẫn xuất hiện tượng giao thoa lượng tử hai khe theo tiên đề Born. Giả sử <i>Ψ</i><sub>1</sub> và <i>Ψ</i><sub>2</sub> lần lượt là hàm sóng "
        "khi chỉ mở khe 1 hoặc chỉ mở khe 2. Theo nguyên lý chồng chất trạng thái, khi mở đồng thời cả hai khe, hàm sóng tổng hợp là <i>Ψ</i> = <i>Ψ</i><sub>1</sub> + <i>Ψ</i><sub>2</sub>. "
        "Mật độ xác suất trên màn chắn bộc lộ số hạng giao thoa đặc trưng:"
    )
    born_step3_eq = r"P = |\Psi_1 + \Psi_2|^2 = (\Psi_1^* + \Psi_2^*)(\Psi_1 + \Psi_2) = |\Psi_1|^2 + |\Psi_2|^2 + 2\mathrm{Re}\left[ \Psi_1^* \Psi_2 \right]"
    story.append(he.build_intermediate_equation(born_step3_txt, born_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g2_p4 = (
        "<b>Các điều kiện chuẩn mực bắt buộc của hàm sóng vật lý (Well-behaved Wave Function):</b><br/>"
        "Để mang ý nghĩa xác suất vật lý thực tế, hàm sóng <i>Ψ</i>(<b>r</b>, <i>t</i>) phải thỏa mãn nghiêm ngặt bốn điều kiện toán học:<br/>"
        "1. <i>Tính liên tục (Continuous):</i> Hàm sóng <i>Ψ</i> và đạo hàm riêng bậc nhất theo không gian phải liên tục trên toàn không gian.<br/>"
        "2. <i>Tính đơn trị (Single-valued):</i> Tại mỗi điểm toạ độ không gian, xác suất tìm thấy hạt chỉ có thể nhận duy nhất một giá trị.<br/>"
        "3. <i>Tính hữu hạn (Finite):</i> Hàm sóng không được tiến tới vô cùng tại bất kỳ điểm nào, đảm bảo mật độ xác suất luôn xác định.<br/>"
        "4. <i>Tính khả tích bình phương (Square-integrable):</i> Tích phân toàn phần của |<i>Ψ</i>|<sup>2</sup> trên toàn không gian phải là một số thực hữu hạn khác 0, "
        "cho phép nhân với hệ số chuẩn hóa <i>C</i> để đưa tổng xác suất về đúng bằng 1."
    )
    story.append(he.make_paragraph(g2_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_born = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Hiện tượng giao thoa hai khe đối với chùm electron chứng minh rằng xác suất trong cơ học lượng tử "
        "không tuân theo quy tắc cộng xác suất cổ điển thông thường.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Trong lý thuyết xác suất cổ điển, nếu biến cố hạt đi qua khe 1 có xác suất <i>P</i><sub>1</sub> "
        "và qua khe 2 có xác suất <i>P</i><sub>2</sub>, thì khi mở cả hai khe, xác suất tổng hợp bắt buộc phải là: <i>P</i><sub>cổ điển</sub> = <i>P</i><sub>1</sub> + <i>P</i><sub>2</sub>. "
        "Tuy nhiên, thực nghiệm đo được phân bố mật độ hạt trên màn chắn lại có các cực đại đạt <i>P</i><sub>max</sub> ≈ 4<i>P</i><sub>1</sub> (lớn gấp đôi cổ điển) "
        "và các cực tiểu triệt tiêu <i>P</i><sub>min</sub> = 0 (nhỏ hơn xác suất khi chỉ mở 1 khe duy nhất!).<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Cơ học lượng tử không cộng trực tiếp các xác suất thực <i>P</i>, mà cộng các <i>biên độ xác suất phức</i>: "
        "<i>Ψ</i> = <i>Ψ</i><sub>1</sub> + <i>Ψ</i><sub>2</sub>. Khi lấy bình phương môđun, số hạng giao thoa kết hợp 2Re[<i>Ψ</i><sub>1</sub><sup>*</sup> <i>Ψ</i><sub>2</sub>] "
        "xuất hiện. Tại nơi hai sóng ngược pha, số hạng này nhận giá trị âm triệt tiêu hoàn toàn xác suất tìm thấy hạt.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù kinh điển là việc đặt máy dò photon hoặc electron tại các khe để theo dõi "
        "hạt thực sự đi qua khe nào. Thực nghiệm khẳng định: ngay khi đặt thiết bị đo để xác định quỹ đạo của hạt, hiện tượng sụp đổ hàm sóng "
        "(Wavefunction Collapse) xảy ra tức thì, pha kết hợp bị phá hủy, số hạng giao thoa biến mất hoàn toàn và hình ảnh quay trở lại đường cong trơn cổ điển <i>P</i><sub>1</sub> + <i>P</i><sub>2</sub>."
    )
    story.append(he.make_paragraph(cer_born, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.3.3: KHÁI NIỆM BÓ SÓNG (WAVE PACKET), CHỒNG CHẬP SÓNG & VẬN TỐC NHÓM
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.3.3: Khái niệm Bó sóng (Wave Packet), Chồng chập sóng &amp; Vận tốc nhóm", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g3_p1 = (
        "Một vi hạt thực tế trong tự nhiên (như một electron phát ra từ súng điện tử) luôn mang tính chất định xứ trong một vùng không gian hữu hạn "
        "(ví dụ kích thước cỡ vài nanomet hoặc micromet), hoàn toàn không thể trải rộng vô hạn như một sóng phẳng đơn sắc lý tưởng. "
        "Để mô tả một vi hạt định xứ trong cơ học lượng tử, chúng ta phải áp dụng phép biến đổi Fourier để chồng chập vô số các sóng phẳng đơn sắc "
        "có số sóng <i>k</i> khác nhau đôi chút tập trung quanh một giá trị trung bình <i>k</i><sub>0</sub>. "
        "Tập hợp các sóng chồng chập này tạo thành một <i>bó sóng</i> hay <i>gói sóng</i> (Wave Packet)."
    )
    story.append(he.make_paragraph(g3_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng 2 ảnh gốc slide 25
    img_wp_orig1 = os.path.join(kho_anh, "[Goc]_Muc_2.3_Hinh_02_Bo_Song_Wave_Packet.png")
    cap_wp_orig1 = "Hình 2.3.3a: Cấu trúc hình học của bó sóng (Wave Packet): sự kết hợp giữa các gợn sóng mang nhanh và đường bao biên độ định xứ."
    story.append(he.embed_figure_with_caption(img_wp_orig1, cap_wp_orig1, kind="orig", styles=styles))

    wp_ocr_1 = "Đường bao ngoài biên độ xác định vùng không gian hạt tồn tại với xác suất đáng kể."
    wp_ocr_2 = "Các vạch sóng bên trong dao động với tần số nhanh tương ứng với pha của sóng mang."
    wp_ocr_3 = "Bề rộng của bó sóng Delta x đo lường độ bất định về vị trí của hạt trong không gian."
    wp_ocr_4 = "Tâm bó sóng là vị trí có biên độ xác suất đạt cực đại, đại diện cho tọa độ hạt cổ điển."
    wp_ocr_5 = "Sự giao thoa triệt tiêu ở hai rìa ngoài ép biên độ sóng suy giảm nhanh về 0 ở khoảng cách xa."
    story.append(he.make_paragraph(wp_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(wp_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(wp_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(wp_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(wp_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    img_wp_orig2 = os.path.join(kho_anh, "[Goc]_Muc_2.3_Hinh_03_Su_Lan_Truyen_Nhom_Song.png")
    cap_wp_orig2 = "Hình 2.3.3b: Sự lan truyền của nhóm sóng theo thời gian: sự khác biệt động học giữa vận tốc nhóm vg và vận tốc pha vp."
    story.append(he.embed_figure_with_caption(img_wp_orig2, cap_wp_orig2, kind="orig", styles=styles))

    # Nhúng đồ thị mô phỏng bó sóng MATLAB
    img_wp_sim = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.3_Cau_Truc_Bo_Song_Va_Van_Toc_Nhom.png")
    cap_wp_sim = "Hình 2.3.3c: Đồ thị mô phỏng giải tích MATLAB cấu trúc bó sóng lan truyền: (a) Bó sóng tại thời điểm ban đầu t = 0; (b) Bó sóng dịch chuyển với vận tốc nhóm vg và giãn rộng tán sắc tại thời điểm t1."
    story.append(he.embed_figure_with_caption(img_wp_sim, cap_wp_sim, kind="sim", styles=styles))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g3_p2 = (
        "<b>Hạt nhân vật lý — Định nghĩa Vận tốc nhóm và Sự tương thích hạt cổ điển:</b> "
        "Trong một bó sóng, chúng ta phân biệt rạch ròi hai khái niệm vận tốc:<br/>"
        "1. <i>Vận tốc pha (Phase Velocity):</i> Là tốc độ di chuyển của từng mặt đồng pha riêng lẻ: thương số giữa tần số góc <i>ω</i> và số sóng <i>k</i>.<br/>"
        "2. <i>Vận tốc nhóm (Group Velocity):</i> Là tốc độ di chuyển của <i>đường bao biên độ</i> (Envelope) và mang theo năng lượng của hạt: "
        "đạo hàm của tần số góc theo số sóng <i>v</i><sub>g</sub>. "
        "Đối với vi hạt de Broglie, vận tốc nhóm của bó sóng hoàn toàn trùng khớp với vận tốc hạt cơ học cổ điển:"
    )
    story.append(he.make_paragraph(g3_p2, styles["Body"]))

    eq_wp = r"v_g = \frac{d\omega}{dk} = \frac{d(\hbar\omega)}{d(\hbar k)} = \frac{dE}{dp} = \frac{d}{dp}\left(\frac{p^2}{2m_0}\right) = \frac{p}{m_0} = v_{\mathrm{particle}}"
    nom_wp = [
        ("Vận tốc nhóm của bó sóng", "<i>v</i><sub>g</sub>", "m/s", "Tốc độ lan truyền của tâm bó sóng, mang năng lượng và thông tin của vi hạt"),
        ("Vận tốc pha của sóng", "<i>v</i><sub>p</sub>", "m/s", "Tốc độ lan truyền của các gợn sóng mang đơn sắc bên trong bó sóng"),
        ("Tần số góc", "<i>ω</i>(<i>k</i>)", "rad/s", "Hàm tán sắc liên hệ giữa tần số thời gian và số sóng không gian"),
        ("Số sóng de Broglie", "<i>k</i>", "rad/m", "Độ lớn véctơ sóng không gian <i>k</i> = <i>p</i>·<i>ħ</i><sup>−1</sup>"),
        ("Vận tốc chuyển động cơ học của hạt", "<i>v</i><sub>particle</sub>", "m/s", "Vận tốc chuyển động thực tế của hạt vi mô cổ điển")
    ]
    story.append(he.build_target_equation_block(eq_wp, nom_wp, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    wp_step1_txt = (
        "Biểu diễn bó sóng dưới dạng tích phân chồng chập Fourier của các sóng phẳng đơn sắc với phổ biên độ <i>A</i>(<i>k</i>) "
        "trong dải số sóng hẹp quanh giá trị trung tâm <i>k</i><sub>0</sub>:"
    )
    wp_step1_eq = r"\psi(x, t) = \int_{k_0 - \Delta k}^{k_0 + \Delta k} A(k) \exp\left( i(kx - \omega(k) t) \right) dk"
    story.append(he.build_intermediate_equation(wp_step1_txt, wp_step1_eq, styles=styles, is_expanded_from_slide=True))

    wp_step2_txt = (
        "Khai triển chuỗi Taylor hàm tán sắc <i>ω</i>(<i>k</i>) quanh điểm lân cận số sóng trung tâm <i>k</i><sub>0</sub>, "
        "giữ lại số hạng vi phân bậc nhất đối với dải sóng hẹp Δ<i>k</i> ≪ <i>k</i><sub>0</sub>:"
    )
    wp_step2_eq = r"\omega(k) \approx \omega(k_0) + \left.\frac{d\omega}{dk}\right|_{k_0} (k - k_0) = \omega_0 + v_g (k - k_0)"
    story.append(he.build_intermediate_equation(wp_step2_txt, wp_step2_eq, styles=styles, is_expanded_from_slide=True))

    wp_step3_txt = (
        "Thay khai triển Taylor vào tích phân Fourier và tách số hạng pha nhanh <i>k</i><sub>0</sub><i>x</i> − <i>ω</i><sub>0</sub><i>t</i> ra ngoài dấu tích phân, "
        "chứng minh đường bao biên độ chuyển động định tiến với đúng vận tốc nhóm <i>v</i><sub>g</sub>:"
    )
    wp_step3_eq = r"\psi(x, t) = \exp(i(k_0 x - \omega_0 t)) \int_{-\Delta k}^{\Delta k} A(k_0 + u) \exp\left( iu(x - v_g t) \right) du = \exp(i(k_0 x - \omega_0 t)) \cdot \mathcal{A}(x - v_g t)"
    story.append(he.build_intermediate_equation(wp_step3_txt, wp_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g3_p4 = (
        "<b>So sánh động học phi tương đối tính và tương đối tính:</b><br/>"
        "• <i>Hạt phi tương đối tính (v ≪ c):</i> Động năng <i>E</i> = <i>p</i><sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup>. "
        "Vận tốc pha là thương số giữa <i>E</i> và <i>p</i>: <i>v</i><sub>p</sub> = <i>p</i>·(2<i>m</i><sub>0</sub>)<sup>−1</sup> = 0.5<i>v</i>. "
        "Trong khi đó vận tốc nhóm là đạo hàm của <i>E</i> theo <i>p</i>: <i>v</i><sub>g</sub> = <i>p</i>·<i>m</i><sub>0</sub><sup>−1</sup> = <i>v</i>. "
        "Vận tốc nhóm đúng bằng vận tốc hạt, còn vận tốc pha chỉ bằng một nửa vận tốc hạt!<br/>"
        "• <i>Hạt tương đối tính:</i> Năng lượng toàn phần <i>E</i><sup>2</sup> = <i>p</i><sup>2</sup><i>c</i><sup>2</sup> + <i>m</i><sub>0</sub><sup>2</sup><i>c</i><sup>4</sup>. "
        "Lấy vi phân hai vế: 2<i>E dE</i> = 2<i>p c</i><sup>2</sup> <i>dp</i> suy ra đạo hàm của <i>E</i> theo <i>p</i> là <i>v</i><sub>g</sub> = <i>pc</i><sup>2</sup>·<i>E</i><sup>−1</sup> = (<i>m v c</i><sup>2</sup>)·(<i>m c</i><sup>2</sup>)<sup>−1</sup> = <i>v</i>. "
        "Vận tốc pha khi đó là <i>v</i><sub>p</sub> = <i>E</i>·<i>p</i><sup>−1</sup> = <i>c</i><sup>2</sup>·<i>v</i><sup>−1</sup> &gt; <i>c</i>! "
        "Vận tốc pha lớn hơn tốc độ ánh sáng hoàn toàn không vi phạm thuyết tương đối vì các mặt pha không mang năng lượng hay thông tin; "
        "năng lượng thực tế được vận chuyển bởi vận tốc nhóm <i>v</i><sub>g</sub> = <i>v</i> &lt; <i>c</i>."
    )
    story.append(he.make_paragraph(g3_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_wp = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Hiện tượng tán sắc lượng tử (Quantum Dispersion) khiến cho một bó sóng electron tự do trong chân không "
        "không thể duy trì mãi kích thước ban đầu mà bắt buộc phải tự giãn rộng theo thời gian.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Phương trình tán sắc của electron trong chân không là phi tuyến: <i>ω</i>(<i>k</i>) = <i>ħk</i><sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup>. "
        "Đạo hàm bậc hai của tần số góc khác không: đạo hàm cấp hai bằng <i>ħ</i>·<i>m</i><sub>0</sub><sup>−1</sup> ≠ 0. "
        "Đối với bó sóng ban đầu có độ rộng Δ<i>x</i><sub>0</sub> ≈ 1 nm, sau khoảng thời gian chỉ 10<sup>−13</sup> s, bề rộng bó sóng đã tăng gấp đôi!<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Vì vận tốc nhóm phụ thuộc vào số sóng <i>k</i>, các thành phần sóng phẳng mang số sóng lớn hơn "
        "sẽ chuyển động nhanh hơn các thành phần sóng mang số sóng nhỏ hơn. Sự chênh lệch vận tốc giữa các sóng thành phần bên trong bó "
        "khiến bó sóng bị kéo giãn dần dọc theo phương chuyển động.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù thực tế là thắc mắc tại sao electron trong các thiết bị vi điện tử "
        "không bị biến mất do hiện tượng giãn rộng bó sóng. Trong chất rắn bán dẫn, thế năng tuần hoàn của mạng tinh thể và các hiệu ứng tương tác hạt tải "
        "liên tục tái định hình trạng thái định xứ của electron, ngăn chặn sự phân tán vô hạn trong không gian."
    )
    story.append(he.make_paragraph(cer_wp, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.3.4: NGUYÊN LÝ BẤT ĐỊNH HEISENBERG & HỆ QUẢ GIAM CẦM NĂNG LƯỢNG
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.3.4: Nguyên lý bất định Heisenberg &amp; Hệ quả giam cầm năng lượng", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g4_p1 = (
        "Năm 1927, Werner Heisenberg tại Đại học Leipzig đã công bố một trong những nguyên lý vĩ đại và sâu sắc nhất của toàn bộ khoa học tự nhiên: "
        "<i>Nguyên lý bất định</i> (Uncertainty Principle, đoạt giải Nobel Vật lý năm 1932). "
        "Trong cơ học cổ điển Newton, một hạt chuyển động hoàn toàn có thể xác định đồng thời chính xác tuyệt đối cả tọa độ vị trí <i>x</i>(<i>t</i>) "
        "và xung lượng <i>p</i><sub>x</sub>(<i>t</i>) tại mọi thời điểm (khái niệm quỹ đạo xác định). "
        "Tuy nhiên, trong thế giới lượng tử, do bản chất sóng liên kết của vật chất, việc đo đạc chính xác một đại lượng này "
        "sẽ tất yếu làm mất độ chính xác của đại lượng liên hợp tương ứng. Tích độ bất định giữa tọa độ và động lượng luôn bị chặn dưới bởi một giới hạn vật lý bất biến."
    )
    story.append(he.make_paragraph(g4_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng đồ thị mô phỏng nguyên lý bất định Heisenberg
    img_heis_sim = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.3_Nguyen_Ly_Bat_Dinh_Heisenberg.png")
    cap_heis_sim = "Hình 2.3.4: Đồ thị mô phỏng giải tích MATLAB nguyên lý bất định Heisenberg: (a) Sự đánh đổi tương hỗ giữa không gian thực và không gian xung lượng; (b) Năng lượng giam cầm lượng tử <i>E</i><sub>conf</sub> bùng nổ khi kích thước nano L co nhỏ dưới 5 nm."
    story.append(he.embed_figure_with_caption(img_heis_sim, cap_heis_sim, kind="sim", styles=styles))

    heis_ocr_1 = "Đường cong định xứ hẹp trong không gian thực Delta x1 = 0.5 nm dẫn tới độ bất định xung lượng bùng rộng Delta p1 lớn."
    heis_ocr_2 = "Đường nét đứt định xứ rộng Delta x2 = 1.5 nm tương ứng dải phân bố xung lượng co hẹp sắc nét Delta p2."
    heis_ocr_3 = "Đặc tuyến năng lượng giam cầm <i>E</i><sub>conf</sub> trong giếng nano tỷ lệ nghịch với bình phương bề rộng giếng <i>L</i><sup>2</sup>."
    heis_ocr_4 = "Vật liệu bán dẫn GaAs với khối lượng hiệu dụng nhẹ m* = 0.067 m0 có năng lượng giam cầm vượt trội Silicon."
    heis_ocr_5 = "Ngưỡng nhiệt độ phòng 300 K (kBT xấp xỉ 26 meV) bị vượt qua dễ dàng khi kích thước hạt nano co nhỏ dưới 10 nm."
    story.append(he.make_paragraph(heis_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(heis_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(heis_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(heis_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(heis_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g4_p2 = (
        "<b>Hạt nhân vật lý — Hệ thức bất định Heisenberg và Hệ quả Giam cầm lượng tử:</b> "
        "Heisenberg đã thiết lập hai hệ thức bất định cơ bản cho các cặp biến số liên hợp chính tắc:<br/>"
        "1. <i>Hệ thức Tọa độ — Động lượng:</i> Không thể xác định đồng thời chính xác cả vị trí <i>x</i> và thành phần động lượng tương ứng <i>p</i><sub>x</sub>.<br/>"
        "2. <i>Hệ thức Năng lượng — Thời gian:</i> Để đo đạc chính xác năng lượng của một trạng thái lượng tử với độ bất định Δ<i>E</i>, "
        "cần một khoảng thời gian đo tối thiểu Δ<i>t</i>:"
    )
    story.append(he.make_paragraph(g4_p2, styles["Body"]))

    eq_heis = r"\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2} = \frac{h}{4\pi} \quad \text{và} \quad \Delta E \cdot \Delta t \ge \frac{\hbar}{2}"
    nom_heis = [
        ("Độ bất định tọa độ vị trí", "Δ<i>x</i>", "nm", "Độ lệch chuẩn đo lường vị trí của hạt trong không gian thực"),
        ("Độ bất định thành phần động lượng", "Δ<i>p</i><sub>x</sub>", "kg·m/s", "Độ lệch chuẩn đo lường động lượng theo phương tương ứng"),
        ("Độ bất định năng lượng", "Δ<i>E</i>", "eV", "Độ bất định về mức năng lượng của trạng thái lượng tử"),
        ("Thời gian tồn tại / Thời gian đo", "Δ<i>t</i>", "s", "Thời gian sống của trạng thái lượng tử kích thích"),
        ("Năng lượng giam cầm tối thiểu", "<i>E</i><sub>conf</sub>", "eV", "Động năng điểm không xuất hiện do hạt bị giam hãm trong không gian nano")
    ]
    story.append(he.build_target_equation_block(eq_heis, nom_heis, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    heis_step1_txt = (
        "Dẫn xuất từ tính chất toán học của phân tích phổ sóng Fourier. Một bó sóng có độ rộng không gian Δ<i>x</i> và độ rộng phổ số sóng Δ<i>k</i> "
        "luôn thỏa mãn bất đẳng thức Fourier cơ bản đối với hàm Gauss: tích Δ<i>x</i>·Δ<i>k</i> luôn lớn hơn hoặc bằng 0.5:"
    )
    heis_step1_eq = r"\Delta x \cdot \Delta k \ge \frac{1}{2}"
    story.append(he.build_intermediate_equation(heis_step1_txt, heis_step1_eq, styles=styles, is_expanded_from_slide=True))

    heis_step2_txt = (
        "Nhân cả hai vế bất đẳng thức Fourier với hằng số Planck rút gọn <i>ħ</i>. Áp dụng hệ thức liên hệ động lượng de Broglie <i>p</i> = <i>ħk</i> suy ra Δ<i>p</i> = <i>ħ</i> Δ<i>k</i>:"
    )
    heis_step2_eq = r"\Delta x \cdot (\hbar \Delta k) \ge \frac{\hbar}{2} \implies \Delta x \cdot \Delta p_x \ge \frac{\hbar}{2}"
    story.append(he.build_intermediate_equation(heis_step2_txt, heis_step2_eq, styles=styles, is_expanded_from_slide=True))

    heis_step3_txt = (
        "Dẫn xuất hệ quả giam cầm lượng tử trong cấu trúc nano kích thước <i>L</i>. Khi hạt electron bị giam cầm trong hộp thế nano kích thước <i>L</i>, "
        "độ bất định vị trí tối đa là Δ<i>x</i> ≈ <i>L</i>·0.5. Độ bất định động lượng tối thiểu của hạt và động năng điểm không thu được:"
    )
    heis_step3_eq = r"\Delta p \ge \frac{\hbar}{2 \Delta x} \approx \frac{\hbar}{L} \implies E_{\mathrm{conf}} \ge \frac{(\Delta p)^2}{2 m^*} \approx \frac{\hbar^2}{2 m^* L^2} \propto \frac{1}{L^2}"
    story.append(he.build_intermediate_equation(heis_step3_txt, heis_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g4_p4 = (
        "<b>Ý nghĩa sống còn của nguyên lý bất định trong công nghệ Nano:</b><br/>"
        "• <i>Năng lượng điểm không (Zero-point Energy):</i> Một hạt lượng tử không bao giờ có thể đứng yên hoàn toàn ở đáy giếng thế năng. "
        "Nếu hạt đứng yên (<i>v</i> = 0 suy ra <i>p</i> = 0 tuyệt đối), thì Δ<i>p</i> = 0, dẫn tới độ bất định vị trí Δ<i>x</i> → ∞, "
        "mâu thuẫn với việc hạt bị nhốt trong giếng thế! Hạt luôn dao động với động năng tối thiểu khác 0 ngay cả ở nhiệt độ không tuyệt đối 0 K.<br/>"
        "• <i>Hiệu ứng giam cầm lượng tử bùng nổ khi L &lt; 5 nm:</i> Đối với bán dẫn GaAs (khối lượng hiệu dụng <i>m</i><sup>*</sup> = 0.067 <i>m</i><sub>0</sub>), "
        "khi kích thước hạt nano giảm từ 20 nm xuống 2 nm, năng lượng giam cầm <i>E</i><sub>conf</sub> tăng vọt từ 0.007 eV lên tới 0.70 eV (tăng 100 lần!), "
        "vượt trội hoàn toàn năng lượng kích thích nhiệt ở nhiệt độ phòng (khoảng 0.026 eV), làm biến đổi toàn diện màu sắc quang học phát xạ.<br/>"
        "• <i>Độ rộng vạch quang phổ tự nhiên:</i> Trạng thái kích thích có thời gian sống trung bình <i>τ</i> hữu hạn (khoảng 10<sup>−8</sup> s) "
        "sẽ sở hữu độ bất định năng lượng Δ<i>E</i> = <i>ħ·τ</i><sup>−1</sup>, dẫn tới độ giãn rộng vạch quang phổ tự nhiên không thể loại bỏ."
    )
    story.append(he.make_paragraph(g4_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_heis = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Nguyên lý bất định Heisenberg giải thích tại sao electron trong nguyên tử không bao giờ bị rơi vào hạt nhân "
        "dưới tác dụng của lực hút tĩnh điện Coulomb khổng lồ.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Thế năng Coulomb hút electron về hạt nhân là <i>V</i>(<i>r</i>) = −<i>e</i><sup>2</sup>·(4<i>πε</i><sub>0</sub><i>r</i>)<sup>−1</sup> "
        "(tiến tới −∞ khi <i>r</i> → 0). Nếu electron rơi sát hạt nhân ở khoảng cách <i>r</i> cỡ kích thước hạt nhân (~10<sup>−15</sup> m), "
        "độ bất định vị trí co lại Δ<i>x</i> ≈ 10<sup>−15</sup> m.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Theo hệ thức Heisenberg, động lượng bất định bùng nổ: Δ<i>p</i> ≥ <i>ħ</i>·(2Δ<i>x</i>)<sup>−1</sup> ≈ 5 × 10<sup>−20</sup> kg·m/s. "
        "Động năng tương ứng của electron đạt giá trị khổng lồ: <i>E</i><sub>k</sub> ≈ (Δ<i>p</i>)<sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup> ≈ 1.4 × 10<sup>−9</sup> J ≈ 8.6 GeV! "
        "Động năng khổng lồ này vượt trội hoàn toàn độ sâu thế năng tĩnh điện, đẩy electron văng ngược ra xa hạt nhân và cân bằng tại bán kính Bohr <i>a</i><sub>0</sub> ≈ 0.53 Å.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến là quan niệm sai lầm cho rằng độ bất định xuất phát từ "
        "sự yếu kém của thiết bị đo lường hoặc do tác động của dụng cụ đo làm nhiễu loạn hạt. Cần khẳng định dứt khoát: Nguyên lý bất định là "
        "thuộc tính nội tại bản chất của sóng vật chất tự nhiên, tồn tại độc lập với bất kỳ thiết bị đo nào."
    )
    story.append(he.make_paragraph(cer_heis, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.3.5: PHƯƠNG TRÌNH SCHRÖDINGER CƠ BẢN CỦA CƠ HỌC LƯỢNG TỬ
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.3.5: Phương trình Schrödinger cơ bản của cơ học lượng tử", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g5_p1 = (
        "Năm 1926, nhà vật lý người Áo Erwin Schrödinger đã công bố phương trình vi phân chuyển động mang tên ông "
        "(đoạt giải Nobel Vật lý năm 1933). "
        "Phương trình Schrödinger đóng vai trò tương tự như định luật II Newton trong cơ học cổ điển hay phương trình Maxwell trong điện từ học: "
        "nó là phương trình động lực học trung tâm xác định sự biến thiên theo thời gian và không gian của hàm sóng <i>Ψ</i>(<b>r</b>, <i>t</i>) "
        "đối với bất kỳ hệ vi mô nào dưới tác dụng của trường thế năng ngoại đặt <i>V</i>(<b>r</b>, <i>t</i>)."
    )
    story.append(he.make_paragraph(g5_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g5_p2 = (
        "<b>Hạt nhân vật lý — Phương trình Schrödinger phụ thuộc thời gian và độc lập thời gian:</b> "
        "Phương trình Schrödinger được xây dựng dựa trên nguyên lý toán tử lượng tử: năng lượng toàn phần và động lượng được thay thế "
        "bằng các toán tử vi phân tác dụng lên hàm sóng. Trong trường thế dừng <i>V</i>(<b>r</b>) không phụ thuộc thời gian, "
        "hàm sóng được tách biến thành tích giữa hàm không gian <i>ψ</i>(<b>r</b>) và thừa số pha thời gian exp(−<i>iEt</i>·<i>ħ</i><sup>−1</sup>):"
    )
    story.append(he.make_paragraph(g5_p2, styles["Body"]))

    eq_sch = r"i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi = \left( -\frac{\hbar^2}{2m_0}\nabla^2 + V(\vec{r}, t) \right)\Psi \quad \text{và} \quad -\frac{\hbar^2}{2m_0}\nabla^2 \psi + V(\vec{r})\psi = E\psi"
    nom_sch = [
        ("Toán tử vi phân Hamiltonian", "<i>Ĥ</i>", "eV", "Toán tử năng lượng toàn phần gồm toán tử động năng và toán tử thế năng"),
        ("Toán tử vi phân Laplace", "∇<sup>2</sup>", "m<sup>−2</sup>", "Toán tử tổng các đạo hàm riêng bậc hai theo ba phương không gian"),
        ("Trường thế năng ngoại đặt", "<i>V</i>(<b>r</b>, <i>t</i>)", "eV", "Năng lượng tương tác của hạt vi mô với môi trường xung quanh"),
        ("Giá trị riêng năng lượng", "<i>E</i>", "eV", "Mức năng lượng gián đoạn của trạng thái dừng lượng tử"),
        ("Hàm sóng không gian dừng", "<i>ψ</i>(<b>r</b>)", "m<sup>−3/2</sup>", "Hàm số mô tả cấu trúc không gian của trạng thái dừng")
    ]
    story.append(he.build_target_equation_block(eq_sch, nom_sch, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    sch_step1_txt = (
        "Xây dựng toán tử động lượng và toán tử động năng từ hàm sóng phẳng de Broglie: <i>Ψ</i>(<i>x</i>, <i>t</i>) = <i>A</i> exp(<i>i</i>(<i>px</i> − <i>Et</i>)·<i>ħ</i><sup>−1</sup>). "
        "Lấy đạo hàm riêng bậc nhất theo toạ độ <i>x</i>:"
    )
    sch_step1_eq = r"\frac{\partial \Psi}{\partial x} = \frac{i p}{\hbar} \Psi \implies \hat{p}_x = -i\hbar \frac{\partial}{\partial x} \implies \hat{E}_k = \frac{\hat{p}_x^2}{2m_0} = -\frac{\hbar^2}{2m_0} \frac{\partial^2}{\partial x^2}"
    story.append(he.build_intermediate_equation(sch_step1_txt, sch_step1_eq, styles=styles, is_expanded_from_slide=True))

    sch_step2_txt = (
        "Xây dựng toán tử năng lượng toàn phần bằng cách lấy đạo hàm riêng bậc nhất của hàm sóng theo biến thời gian <i>t</i>:"
    )
    sch_step2_eq = r"\frac{\partial \Psi}{\partial t} = -\frac{i E}{\hbar} \Psi \implies \hat{E} = i\hbar \frac{\partial}{\partial t}"
    story.append(he.build_intermediate_equation(sch_step2_txt, sch_step2_eq, styles=styles, is_expanded_from_slide=True))

    sch_step3_txt = (
        "Tổng hợp toán tử năng lượng toàn phần <i>E</i> = <i>E</i><sub>k</sub> + <i>V</i> dẫn tới phương trình Schrödinger phụ thuộc thời gian tổng quát. "
        "Tách biến <i>Ψ</i>(<b>r</b>, <i>t</i>) = <i>ψ</i>(<b>r</b>) exp(−<i>iEt</i>·<i>ħ</i><sup>−1</sup>) để thu được phương trình dừng độc lập thời gian:"
    )
    sch_step3_eq = r"i\hbar \frac{\partial \Psi}{\partial t} = \left( -\frac{\hbar^2}{2m_0}\nabla^2 + V(\vec{r}) \right)\Psi \implies -\frac{\hbar^2}{2m_0}\nabla^2 \psi(\vec{r}) + V(\vec{r})\psi(\vec{r}) = E\psi(\vec{r})"
    story.append(he.build_intermediate_equation(sch_step3_txt, sch_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g5_p4 = (
        "<b>Đặc tính của Trạng thái dừng (Stationary States):</b><br/>"
        "• <i>Mật độ xác suất độc lập thời gian:</i> Đối với nghiệm trạng thái dừng, mật độ xác suất hoàn toàn đứng yên: "
        "|<i>Ψ</i>(<b>r</b>, <i>t</i>)|<sup>2</sup> = |<i>ψ</i>(<b>r</b>)|<sup>2</sup> |exp(−<i>iEt</i>·<i>ħ</i><sup>−1</sup>)|<sup>2</sup> = |<i>ψ</i>(<b>r</b>)|<sup>2</sup>. "
        "Mặc dù bản thân hàm sóng dao động tuần hoàn trong trường phức với tần số <i>E</i>·<i>h</i><sup>−1</sup>, "
        "mọi đại lượng vật lý quan sát được đều bất biến theo thời gian.<br/>"
        "• <i>Bài toán phương trình giá trị riêng (Eigenvalue Problem):</i> Phương trình Schrödinger dừng <i>Ĥψ</i> = <i>Eψ</i> "
        "là một bài toán tìm hàm riêng và giá trị riêng của toán tử vi phân Hermitian. Điều kiện biên vật lý (hàm sóng triệt tiêu ở vô cùng hoặc ở biên hộp thế) "
        "tất yếu buộc năng lượng <i>E</i> chỉ được phép nhận các giá trị rời rạc <i>E</i><sub>1</sub>, <i>E</i><sub>2</sub>, <i>E</i><sub>3</sub>... "
        "Đây chính là cơ chế xuất hiện tự nhiên của hiện tượng lượng tử hóa trong thế giới nano."
    )
    story.append(he.make_paragraph(g5_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_sch = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Phương trình Schrödinger chỉ chứa đạo hàm bậc nhất theo thời gian (đạo hàm riêng thời gian) "
        "nhưng lại chứa đạo hàm bậc hai theo không gian ∇<sup>2</sup>, khác biệt hoàn toàn với phương trình sóng cơ học hay sóng điện từ cổ điển.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Phương trình sóng cổ điển D'Alembert chứa đạo hàm bậc hai theo cả hai biến. "
        "Trong khi đó phương trình Schrödinger biểu diễn đạo hàm bậc nhất thời gian bằng toán tử Laplace bậc hai không gian nhân với −<i>ħ</i><sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup>.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Trong cơ học cổ điển đối với hạt phi tương đối tính, năng lượng toàn phần tỷ lệ bậc nhất với năng lượng "
        "nhưng tỷ lệ bậc hai với động lượng: <i>E</i> = <i>p</i><sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup>. "
        "Toán tử năng lượng thời gian là đạo hàm bậc nhất, còn toán tử động lượng squared là đạo hàm bậc hai không gian. Sự bất đối xứng đạo hàm phản ánh chính xác cấu trúc động học phi tương đối tính của hạt vi mô.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Khi chuyển sang cơ học lượng tử tương đối tính (nơi năng lượng và động lượng đối xứng bậc hai: "
        "<i>E</i><sup>2</sup> = <i>p</i><sup>2</sup><i>c</i><sup>2</sup> + <i>m</i><sub>0</sub><sup>2</sup><i>c</i><sup>4</sup>), phương trình Klein - Gordon "
        "chứa đạo hàm bậc hai thời gian; tuy nhiên nó lại dẫn tới mật độ xác suất âm. Paul Dirac đã giải quyết vấn đề này "
        "bằng phương trình Dirac bậc nhất đối với cả thời gian và không gian sử dụng ma trận spinor 4 chiều."
    )
    story.append(he.make_paragraph(cer_sch, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # TỔNG KẾT MỤC 2.3 & BẢN ĐỒ ĐIỀU HƯỚNG CHƯƠNG 2
    # =========================================================================
    story.append(he.make_paragraph("Tổng kết Mục 2.3 &amp; Bản đồ Điều hướng Mục 2.4 tiếp theo", styles["H2"]))
    summary_text = (
        "<b>Ma trận tổng hợp kiến thức cốt lõi Mục 2.3:</b><br/>"
        "1. <i>Hàm sóng phức de Broglie:</i> Mô tả trạng thái vi hạt tự do bằng hàm sóng điều hòa phức <i>Ψ</i> = <i>A</i> exp(<i>i</i>(<b>p</b>·<b>r</b> − <i>Et</i>)·<i>ħ</i><sup>−1</sup>); "
        "sóng phẳng thuần nhất không định xứ trong không gian vô hạn.<br/>"
        "2. <i>Tiên đề xác suất Max Born:</i> Hàm sóng là trường biên độ xác suất; mật độ xác suất |<i>Ψ</i>|<sup>2</sup> = <i>Ψ</i><sup>*</sup><i>Ψ</i> xác định xác suất định xứ vi hạt; "
        "điều kiện chuẩn hóa toàn phần ∫ |<i>Ψ</i>|<sup>2</sup> <i>dV</i> = 1 bảo toàn xác suất toàn thể.<br/>"
        "3. <i>Bó sóng &amp; Vận tốc nhóm:</i> Chồng chập Fourier vô số sóng phẳng tạo thành bó sóng định xứ; vận tốc nhóm của đường bao "
        "bằng đạo hàm của tần số góc theo số sóng <i>v</i><sub>g</sub> = <i>p</i>·<i>m</i><sub>0</sub><sup>−1</sup> hoàn toàn trùng khớp với vận tốc hạt cổ điển.<br/>"
        "4. <i>Nguyên lý bất định Heisenberg:</i> Ranh giới lượng tử bất biến Δ<i>x</i>·Δ<i>p</i><sub>x</sub> ≥ 0.5<i>ħ</i>; hệ quả giam cầm lượng tử "
        "<i>E</i><sub>conf</sub> tỷ lệ nghịch với bình phương kích thước <i>L</i><sup>2</sup> giải thích tính bền vững của nguyên tử và bùng nổ năng lượng trong cấu trúc nano.<br/>"
        "5. <i>Phương trình Schrödinger:</i> Phương trình vi phân động lực học cơ bản <i>iħ</i> (đạo hàm thời gian của <i>Ψ</i>) = <i>ĤΨ</i>; "
        "trạng thái dừng độc lập thời gian <i>Ĥψ</i> = <i>Eψ</i> thiết lập bài toán giá trị riêng mở ra cấu trúc mức năng lượng gián đoạn.<br/><br/>"
        "<b>Mỏ neo điều hướng Mục 2.4 tiếp theo:</b><br/>"
        "Mục 2.4 sẽ áp dụng trực tiếp Phương trình Schrödinger dừng để giải bài toán cơ bản nhất của vật lý nano: "
        "<i>Hạt trong hộp thế lượng tử (1D, 2D, 3D), Giếng thế thế năng hữu hạn, Rào thế thế năng và Hiệu ứng xuyên hầm lượng tử (Quantum Tunneling)</i>."
    )
    story.append(he.make_paragraph(summary_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # 3. Biên dịch tài liệu
    print("Bắt đầu gọi doc.build(story)...")
    doc.build(story)
    print("Biên dịch thành công Mục 2.3!")

    # 4. Kiểm tra chất lượng và dung lượng
    compliance = he.assert_monograph_compliance(target_pdf, min_pages=5)
    print("Kết quả kiểm toán chất lượng (Compliance) Mục 2.3:", compliance)

    return compliance

if __name__ == "__main__":
    build_pdf()

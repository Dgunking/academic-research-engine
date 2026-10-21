# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Chương 2: Bản chất lượng tử của thế giới nano
Mục 2.1: Giới thiệu chung về công nghệ nano & Vật lý trong thế giới nano
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
    target_pdf = os.path.join(bai_giang, "Chuyen_Khao_Nano_Muc_2.1.pdf")

    print(f"Bắt đầu biên dịch chuyên khảo Mục 2.1: {target_pdf}")

    # 2. Khởi tạo Styles và Document Template
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(target_pdf)
    story = []

    # =========================================================================
    # TIÊU ĐỀ ĐẦU CHUYÊN KHẢO (H1)
    # =========================================================================
    title_main = (
        "CHƯƠNG 2: BẢN CHẤT LƯỢNG TỬ CỦA THẾ GIỚI NANO<br/>"
        "MỤC 2.1: GIỚI THIỆU CHUNG VỀ CÔNG NGHỆ NANO &amp; VẬT LÝ TRONG THẾ GIỚI NANO"
    )
    story.append(he.make_paragraph(title_main, styles["H1"]))
    story.append(Spacer(1, 4))

    meta_info = (
        "<b>Hệ Thống Chuyên Khảo Giảng Dạy &amp; Nghiên Cứu Vật Lý Nano — ĐHBK Hà Nội</b><br/>"
        "<i>Chủ thể nghiên cứu:</i> Bùi Trung Dũng — Khoa Vật lý Kỹ thuật, Trường Đại học Bách khoa Hà Nội (HUST)<br/>"
        "<i>Tài liệu nguồn kép:</i> Bài giảng 'Bài 2-Quantum nature.pdf' (Slide 1–12), Bộ môn Vật liệu Điện tử — HUST; "
        "kết hợp các chuyên khảo quốc tế đỉnh cao: Poole &amp; Owens (<i>Introduction to Nanotechnology</i>), Wolf (<i>Nanophysics</i>)."
    )
    story.append(he.make_paragraph(meta_info, styles["Body"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=he.COLOR_PRIMARY, spaceBefore=4, spaceAfter=10))

    # =========================================================================
    # LỜI NÓI ĐẦU ĐỊNH VỊ HỌC THUẬT & TỔNG QUAN
    # =========================================================================
    overview_text = (
        "<b>Lời nói đầu định vị học thuật:</b> Thế giới nano (quy mô không gian từ 1 nm đến 100 nm) "
        "là ranh giới chuyển tiếp kỳ diệu giữa cơ học cổ điển vĩ mô và cơ học lượng tử vi mô. Ở thang đo này, "
        "vật chất không còn duy trì những tính chất vĩ mô quen thuộc (độ dẫn điện, năng lượng dải cấm, nhiệt độ nóng chảy, "
        "tính chất từ tính hay màu sắc quang học). Thay vào đó, hai hiện tượng vật lý cốt lõi trỗi dậy kiểm soát toàn diện hành vi vật chất: "
        "(1) <i>Sự bùng nổ diện tích bề mặt trên một đơn vị thể tích</i> dẫn tới tỷ lệ nguyên tử bề mặt vượt trội mang năng lượng tự do cao; "
        "và (2) <i>Hiệu ứng giam cầm lượng tử không gian</i> làm lượng tử hóa các mức năng lượng liên tục thành các trạng thái gián đoạn. "
        "Chuyên khảo Mục 2.1 bóc tách trọn vẹn 5 Luận điểm Vi mô (MPT) theo chuẩn mực sư phạm 5 giai đoạn lũy tiến, "
        "dẫn xuất tường minh từng phương trình từ nguyên lý đầu và minh họa bằng đồ thị giải tích kỹ thuật chuẩn MATLAB R2014b+."
    )
    story.append(he.make_paragraph(overview_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # =========================================================================
    # LUẬN ĐIỂM 2.1.1: LỊCH SỬ HÌNH THÀNH & CỘT MỐC CÔNG NGHỆ NANO
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.1.1: Lịch sử hình thành &amp; Cột mốc Công nghệ Nano", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g1_p1 = (
        "Lịch sử công nghệ nano hiện đại được khởi nguồn từ tầm nhìn tiên phong của nhà vật lý đoạt giải Nobel Richard Feynman. "
        "Ngày 29 tháng 12 năm 1959, trong bài phát biểu kinh điển mang tên <i>'There’s Plenty of Room at the Bottom'</i> "
        "tại cuộc họp thường niên của Hội Vật lý Hoa Kỳ (APS) ở Viện Công nghệ California (Caltech), Feynman đã đặt ra câu hỏi mang tính cách mạng: "
        "Tại sao chúng ta không thể thao tác, sắp xếp và kiểm soát vật chất một cách chính xác ở cấp độ từng nguyên tử đơn lẻ? "
        "Feynman chỉ ra rằng các quy luật của vật lý lượng tử không hề cấm việc chế tạo các cỗ máy vi mô hay thao tác nguyên tử, "
        "mà rào cản duy nhất nằm ở giới hạn công cụ kỹ thuật của con người thời bấy giờ.<br/>"
        "Đến năm 1974, Giáo sư Norio Taniguchi tại Đại học Khoa học Tokyo đã lần đầu tiên định nghĩa tường minh thuật ngữ <i>'Nanotechnology'</i> "
        "để mô tả quy trình gia công siêu chính xác (Ultra-precision machining) vật liệu với dung sai kích thước đạt đến cấp độ nanomet. "
        "Tuy nhiên, cuộc cách mạng nano chỉ thực sự bùng nổ khi nhân loại sở hữu đôi mắt và bàn tay để quan sát và điều khiển thế giới nguyên tử: "
        "đó là sự phát minh ra Kính hiển vi quét xuyên hầm (Scanning Tunneling Microscope — STM) năm 1981 bởi Gerd Binnig và Heinrich Rohrer (IBM Zurich, giải Nobel Vật lý 1986), "
        "và tiếp nối là Kính hiển vi lực nguyên tử (Atomic Force Microscope — AFM) năm 1986 bởi Binnig, Quate và Gerber."
    )
    story.append(he.make_paragraph(g1_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh Feynman
    img_feynman = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_01_Richard_Feynman.png")
    cap_feynman = "Hình 2.1.1: Nhà vật lý Richard Feynman (1918–1988) — người đặt nền móng tư tưởng cho công nghệ nano với bài nói lịch sử năm 1959 tại Caltech."
    story.append(he.embed_figure_with_caption(img_feynman, cap_feynman, kind="orig", styles=styles))

    feynman_ocr_1 = "Ghi lại chân dung Richard Feynman, biểu tượng khởi nguồn của kỷ nguyên thao tác vật chất ở cấp độ hạ vi mô."
    feynman_ocr_2 = "Không gian hội trường APS 1959, nơi câu nói bất hủ 'There’s Plenty of Room at the Bottom' được công bố."
    feynman_ocr_3 = "Ý tưởng cốt lõi: Vật lý học không cấm việc sắp xếp nguyên tử theo ý muốn; rào cản chỉ là công nghệ chế tạo công cụ."
    feynman_ocr_4 = "Hạ thang đo từ milimet xuống micromet và chạm tới thang nanomet (10⁻⁹ m) bằng các cỗ máy sao chép thu nhỏ dần."
    feynman_ocr_5 = "Tư tưởng định hình toàn bộ lộ trình phát triển kỹ thuật từ trên xuống (Top-down) và từ dưới lên (Bottom-up)."
    story.append(he.make_paragraph(feynman_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(feynman_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(feynman_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(feynman_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(feynman_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh STM và AFM
    img_stm = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_02_STM.png")
    cap_stm = "Hình 2.1.2: Kính hiển vi quét xuyên hầm (STM) — công cụ đột phá cho phép giải mã cấu trúc bề mặt vật liệu dẫn điện ở quy mô nguyên tử."
    story.append(he.embed_figure_with_caption(img_stm, cap_stm, kind="orig", styles=styles))

    stm_ocr_1 = "Mũi dò kim loại siêu nhọn (Vonfram hoặc Pt-Ir) quét sát bề mặt mẫu dẫn điện ở cự ly dưới 1 nm."
    stm_ocr_2 = "Hệ định vị áp điện gốm Piezoelectric điều khiển tọa độ không gian 3 chiều x, y, z với độ dịch chuyển phân giải dưới 0.01 nm."
    stm_ocr_3 = "Cơ chế hạt tải: Dòng điện tử xuyên hầm lượng tử qua rào thế chân không khi đặt điện áp phân cực vài milivon đến vài von."
    stm_ocr_4 = "Quan hệ hàm số: Dòng xuyên hầm suy giảm theo hàm mũ cực nhanh theo khoảng cách khe hở d."
    stm_ocr_5 = "Hệ thức điều khiển phản hồi: Giữ dòng xuyên hầm không đổi để suy ra bản đồ hình thái học bề mặt mật độ trạng thái cục bộ LDOS."
    story.append(he.make_paragraph(stm_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(stm_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(stm_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(stm_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(stm_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    img_afm = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_03_AFM.png")
    cap_afm = "Hình 2.1.3: Kính hiển vi lực nguyên tử (AFM) — ghi nhận tương tác lực liên nguyên tử Van der Waals, quét được cả mẫu cách điện và mẫu sinh học."
    story.append(he.embed_figure_with_caption(img_afm, cap_afm, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g1_p2 = (
        "<b>Hạt nhân vật lý của STM:</b> STM không dựa trên bất kỳ định luật quang học hay điện từ học cổ điển nào. "
        "Trong vật lý cổ điển, một hạt mang năng lượng <i>E</i> nhỏ hơn chiều cao rào thế năng lượng <i>Φ</i> sẽ bị phản xạ 100% "
        "và tuyệt đối không thể vượt qua khe hở chân không. Tuy nhiên, theo cơ học lượng tử, bản chất sóng của electron cho phép hàm sóng "
        "thâm nhập xuyên qua rào thế hữu hạn và tạo ra một dòng điện tử thực tế chạy qua khe hở chân không bề dày <i>d</i>. "
        "Dòng điện xuyên hầm lượng tử này phụ thuộc cực kỳ nhạy cảm vào khoảng cách khe hở theo hàm mũ."
    )
    story.append(he.make_paragraph(g1_p2, styles["Body"]))

    eq_stm = r"I_{\mathrm{tunnel}} \propto V_{\mathrm{bias}} \cdot \exp\left( - \frac{2 \sqrt{2 m_0 \Phi}}{\hbar} d \right)"
    nom_stm = [
        ("Dòng điện xuyên hầm lượng tử", "<i>I</i><sub>tunnel</sub>", "A", "Cường độ dòng điện tử vượt rào thế chân không"),
        ("Điện áp phân cực đầu dò - mẫu", "<i>V</i><sub>bias</sub>", "V", "Hiệu điện thế kích thích dịch mức Fermi giữa kim dò và mẫu"),
        ("Khoảng cách kim dò đến bề mặt", "<i>d</i>", "m", "Bề dày khe hở chân không giữa nguyên tử đỉnh mũi dò và bề mặt"),
        ("Hàm công thoát hiệu dụng", "<i>Φ</i>", "eV", "Chiều cao rào thế năng lượng chân không trung bình"),
        ("Khối lượng nghỉ của electron", "<i>m</i><sub>0</sub>", "kg", "Hằng số vật lý CODATA 2022: 9.1093837 × 10⁻³¹ kg"),
        ("Hằng số Planck rút gọn", "<i>ℏ</i>", "J·s", "Hằng số tác dụng lượng tử vi mô: 1.054571817 × 10⁻³⁴ J·s")
    ]
    story.append(he.build_target_equation_block(eq_stm, nom_stm, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    step1_text = (
        "Thiết lập phương trình Schrödinger một chiều độc lập thời gian cho electron chuyển động trong vùng rào thế chân không "
        "với thế năng hằng số <i>V</i>(<i>z</i>) = <i>Φ</i> trên đoạn từ <i>z</i> = 0 (đỉnh kim dò) đến <i>z</i> = <i>d</i> (bề mặt mẫu). "
        "Vì năng lượng electron <i>E</i> nhỏ hơn chiều cao rào thế <i>Φ</i>, thừa số động năng trở thành số âm, dẫn tới phương trình vi phân thuần nhất bậc hai:"
    )
    step1_eq = r"-\frac{\hbar^2}{2m_0} \frac{d^2 \psi(z)}{dz^2} + \Phi \psi(z) = E \psi(z) \implies \frac{d^2 \psi(z)}{dz^2} = \kappa^2 \psi(z)"
    story.append(he.build_intermediate_equation(step1_text, step1_eq, styles=styles, is_expanded_from_slide=True))

    step2_text = (
        "Nghiệm tổng quát của phương trình vi phân là tổ hợp tuyến tính của hai hàm mũ thực. Xét sóng tới từ kim dò truyền theo chiều dương trục <i>z</i>, "
        "hàm sóng thâm nhập vào rào thế suy giảm hàm mũ theo tọa độ không gian:"
    )
    step2_eq = r"\psi(z) = \psi(0) \exp(-\kappa z) \quad \text{với} \quad \kappa = \frac{\sqrt{2 m_0 (\Phi - E)}}{\hbar}"
    story.append(he.build_intermediate_equation(step2_text, step2_eq, styles=styles, is_expanded_from_slide=True))

    step3_text = (
        "Mật độ dòng xác suất cơ lượng tử <i>J</i> tỷ lệ thuận với bình phương biên độ hàm sóng tại vị trí bề mặt mẫu <i>z</i> = <i>d</i>. "
        "Khi đặt điện áp phân cực nhỏ <i>V</i><sub>bias</sub> giữa kim dò và mẫu, tích phân dòng qua mật độ trạng thái điện tử cục bộ (LDOS) "
        "cho phương trình thực nghiệm của dòng điện xuyên hầm:"
    )
    step3_eq = r"J \propto |\psi(d)|^2 = |\psi(0)|^2 \exp(-2 \kappa d) \implies I_{\mathrm{tunnel}} \propto V_{\mathrm{bias}} \cdot \rho_{\mathrm{sample}}(E_F) \cdot \exp(-2 \kappa d)"
    story.append(he.build_intermediate_equation(step3_text, step3_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g1_p4 = (
        "<b>Khảo sát độ nhạy không gian siêu việt:</b> Xét bề mặt kim loại điển hình có công thoát <i>Φ</i> ≈ 4.0 eV. "
        "Hệ số suy giảm hàm sóng tính được xấp xỉ 10.2 nm⁻¹.<br/>"
        "Nếu khoảng cách khe hở thay đổi một đoạn vô cùng nhỏ <i>Δd</i> = 0.1 nm (tương đương 1 Å, tức cỡ kích thước bán kính của một nguyên tử), "
        "thừa số hàm mũ suy giảm tính được là exp(−2.04) ≈ 0.13.<br/>"
        "Điều này đồng nghĩa với việc: chỉ cần kim dò nhích ra xa hoặc lại gần bề mặt vỏn vẹn 0.1 nm, cường độ dòng xuyên hầm lập tức thay đổi tới 87% (gần một bậc độ lớn). "
        "Độ dốc hàm mũ cực lớn này bảo đảm rằng 90% dòng điện chỉ tập trung chảy qua duy nhất một nguyên tử nhô cao nhất ở đỉnh mũi dò, "
        "mang lại độ phân giải không gian dọc trục <i>z</i> đạt tới mức hạ picomet (dưới 0.01 nm).<br/>"
        "<b>Giới hạn tiệm cận tiếp xúc điểm (<i>d</i> → 0):</b> Khi kim dò chạm sát bề mặt mẫu, rào thế chân không sụp đổ hoàn toàn. "
        "Kênh dẫn chuyển thành tiếp xúc điểm lượng tử (Quantum Point Contact — QPC), độ dẫn điện không còn phụ thuộc hàm mũ mà bị lượng tử hóa "
        "thành các bậc nguyên lần của lượng tử độ dẫn Landauer <i>G</i><sub>0</sub> có độ lớn xấp xỉ 77.48 μS."
    )
    story.append(he.make_paragraph(g1_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_stm = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Kính hiển vi STM có độ phân giải nguyên tử vượt bậc nhưng bất lực trước các mẫu vật liệu cách điện hoặc mẫu sinh học (màng tế bào, DNA), "
        "trong khi kính hiển vi AFM có thể quét hình thái học không phá hủy trên mọi bề mặt cách điện với độ phân giải cao.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> STM yêu cầu dòng điện chạy qua mạch khép kín tối thiểu <i>I</i><sub>tunnel</sub> ≥ 10 pA dưới điện áp phân cực <i>V</i><sub>bias</sub> ≤ 2 V. "
        "Vật liệu cách điện có điện trở suất <i>ρ</i> &gt; 10¹⁴ Ω·m và khe năng lượng dải cấm <i>E</i><sub>g</sub> &gt; 5 eV, khiến mật độ trạng thái điện tử tại mức Fermi triệt tiêu hoàn toàn (<i>ρ</i>(<i>E</i><sub>F</sub>) = 0). "
        "Ngược lại, AFM ghi nhận độ uốn của thanh cantilever dưới tác dụng của lực liên nguyên tử Van der Waals và lực đẩy Pauli (cỡ piconewton 10⁻¹² N) thông qua cảm biến quang học phản xạ laser, hoàn toàn không cần dòng điện tải.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Cơ chế của STM là đo độ dẫn xuyên hầm của electron giữa hai mức Fermi. Nếu mẫu cách điện, không có hạt tải tự do để tham gia vào quá trình xuyên hầm, mạch hồi tiếp sẽ hiểu nhầm kim dò đang ở quá xa bề mặt và liên tục điều khiển gốm áp điện đâm sập mũi kim vào mẫu gây gãy đầu dò. AFM đo lực cơ học thuần túy xuất phát từ thế Lennard-Jones giữa các đám mây electron của mũi dò và mẫu, độc lập hoàn toàn với tính chất dẫn điện.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến của sinh viên là nghĩ rằng AFM luôn có độ phân giải tốt hơn STM. Thực tế, STM có độ phân giải nguyên tử thật (True atomic resolution) cao hơn AFM vì dòng xuyên hầm tập trung ở nguyên tử đỉnh nhọn nhất theo hàm mũ, trong khi lực Van der Waals của AFM có phạm vi tác dụng dài hơn và tích phân trên toàn bộ hình học chóp nón của mũi dò."
    )
    story.append(he.make_paragraph(cer_stm, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.1.2: THANG ĐO KHÔNG GIAN NANO & HIỆU ỨNG DIỆN TÍCH BỀ MẶT
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.1.2: Thang đo không gian Nano &amp; Hiệu ứng diện tích bề mặt vượt trội", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g2_p1 = (
        "Nanomet (nm) là đơn vị đo chiều dài trong Hệ đơn vị quốc tế SI tương đương với một phần tỷ mét (1 nm = 10⁻⁹ m = 10 Å). "
        "Để hình dung trực quan về thang đo không gian nano so với thế giới vĩ mô đời sống thường nhật:<br/>"
        "• Một inch (25.4 mm) chứa chính xác 25 400 000 nanomet;<br/>"
        "• Một tờ báo in tiêu chuẩn có độ dày khoảng 100 000 nanomet;<br/>"
        "• Sợi tóc người có đường kính dao động từ 50 000 nm đến 80 000 nm;<br/>"
        "• Phân tử chuỗi xoắn kép DNA có đường kính khoảng 2 nm;<br/>"
        "• Ở quy mô so sánh tương đương: Nếu một viên bi ve đồ chơi có đường kính 1 nm, thì Trái Đất của chúng ta sẽ thu nhỏ lại chỉ tương đương một quả cầu đường kính vỏn vẹn 1 m.<br/>"
        "Khi vật chất bị phân cắt từ quy mô khối (Bulk) xuống quy mô hạt nano (kích thước hạt <i>R</i> dưới 100 nm, đặc biệt là vùng <i>R</i> &lt; 10 nm), "
        "hành vi nhiệt động lực học và hóa lý của hệ thống thay đổi hoàn toàn do <b>Hiệu ứng diện tích bề mặt vượt trội</b>. "
        "Trong vật liệu khối, số lượng nguyên tử nằm trên bề mặt chỉ chiếm một phần triệu tổng số nguyên tử và có thể bỏ qua trong tính toán nhiệt động. "
        "Tuy nhiên, ở cấp độ nano, tỷ lệ nguyên tử bề mặt tăng vọt lên tới 50% đến 80%. "
        "Các nguyên tử bề mặt này bị thiếu hụt số phối trí (mất liên kết lân cận), dẫn tới sự tồn tại của các liên kết treo (dangling bonds) "
        "và mật độ năng lượng tự do bề mặt <i>γ</i><sub>sv</sub> cực cao, làm thay đổi toàn bộ cân bằng pha nhiệt động học."
    )
    story.append(he.make_paragraph(g2_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh so sánh thang đo gốc
    img_scale = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_04_So_Sanh_Thang_Do.png")
    cap_scale = "Hình 2.1.4: So sánh thang đo không gian từ kích thước vĩ mô (người, kiến), vi mô (tế bào, vi khuẩn) đến thang nano (virus, phân tử DNA, hạt nano)."
    story.append(he.embed_figure_with_caption(img_scale, cap_scale, kind="orig", styles=styles))

    scale_ocr_1 = "Trục thang đo logarithm trải rộng từ mét (10⁰ m) xuống hạ nanomet (10⁻¹⁰ m)."
    scale_ocr_2 = "Phân định rõ ranh giới tự nhiên: Thế giới vĩ mô mắt thường thấy, thế giới kính hiển vi quang học, và thế giới kính hiển vi điện tử/quét dò."
    scale_ocr_3 = "Vật thể đại diện thang nano: Virus (20 nm đến 100 nm), protein (5 nm đến 10 nm), chấm lượng tử (2 nm đến 8 nm), buckyball C60 (1 nm)."
    scale_ocr_4 = "Tương quan tỷ lệ: Mỗi bước nhảy 1 bậc độ lớn tương ứng giảm thể tích 1000 lần và tăng tỷ số diện tích trên thể tích 10 lần."
    scale_ocr_5 = "Hệ quả vật lý: Thang nano là nơi cơ học lượng tử bắt đầu lấn át hoàn toàn các quy luật chuyển động cổ điển."
    story.append(he.make_paragraph(scale_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(scale_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(scale_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(scale_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(scale_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh mô phỏng tỷ lệ diện tích bề mặt và Gibbs-Thomson
    img_sim_surf = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.1_Ty_Le_Dien_Tich_Be_Mat.png")
    cap_sim_surf = "Hình 2.1.5: Đồ thị mô phỏng giải tích MATLAB R2014b+: (a) Tỷ số diện tích bề mặt trên thể tích S:V và phần trăm nguyên tử bề mặt; (b) Hiện tượng suy giảm nhiệt độ nóng chảy Gibbs-Thomson của hạt nano Vàng."
    story.append(he.embed_figure_with_caption(img_sim_surf, cap_sim_surf, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g2_p2 = (
        "<b>Hạt nhân vật lý của hiệu ứng diện tích bề mặt:</b> Xét một khối vật chất lập phương có cạnh <i>L</i> = 1 cm. "
        "Diện tích bề mặt là <i>S</i> = 6 cm² và thể tích <i>V</i> = 1 cm³. Nếu chia nhỏ khối lập phương này thành các hạt nano lập phương "
        "có cạnh <i>l</i> = 10 nm, số lượng hạt nano sinh ra lên tới 10¹⁸ hạt. "
        "Tổng diện tích bề mặt mới của hệ thống sau khi phân cắt đạt tới 600 m² (tương đương diện tích của cả hai sân bóng rổ tiêu chuẩn). "
        "Sự bùng nổ diện tích bề mặt này dẫn tới hệ quả nhiệt động lực học trực tiếp: năng lượng liên kết trung bình trên mỗi nguyên tử "
        "bị suy giảm mạnh, kéo theo sự hạ thấp đột biến nhiệt độ nóng chảy của hạt nano so với vật liệu khối theo mô hình Gibbs-Thomson."
    )
    story.append(he.make_paragraph(g2_p2, styles["Body"]))

    eq_gt = r"T_m(R) = T_{m,\mathrm{bulk}} \left( 1 - \frac{2 \gamma_{\mathrm{sv}}}{\rho_s \Delta H_f R} \right)"
    nom_gt = [
        ("Nhiệt độ nóng chảy của hạt nano", "<i>T</i><sub>m</sub>(<i>R</i>)", "K", "Nhiệt độ chuyển pha rắn - lỏng của cấu trúc hạt nano bán kính R"),
        ("Nhiệt độ nóng chảy vật liệu khối", "<i>T</i><sub>m,bulk</sub>", "K", "Nhiệt độ nóng chảy nội tại ở quy mô vĩ mô vô hạn"),
        ("Năng lượng tự do bề mặt rắn - hơi", "<i>γ</i><sub>sv</sub>", "J·m⁻²", "Mật độ năng lượng dư thừa của các liên kết nguyên tử bề mặt"),
        ("Khối lượng riêng của pha rắn", "<i>ρ</i><sub>s</sub>", "kg·m⁻³", "Mật độ khối lượng của vật liệu ở pha rắn"),
        ("Nhiệt nóng chảy riêng", "<i>ΔH</i><sub>f</sub>", "J·kg⁻¹", "Nhiệt lượng chuyển pha trên một đơn vị khối lượng"),
        ("Bán kính hình học hạt nano", "<i>R</i>", "m", "Bán kính đặc trưng của hạt nano hình cầu")
    ]
    story.append(he.build_target_equation_block(eq_gt, nom_gt, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step2_1_text = (
        "Biểu diễn diện tích bề mặt <i>S</i> và thể tích <i>V</i> của một hạt nano hình cầu bán kính <i>R</i>. "
        "Thiết lập tỷ số diện tích trên thể tích, chứng minh sự phụ thuộc tỷ lệ nghịch bậc một vào bán kính:"
    )
    step2_1_eq = r"S = 4\pi R^2, \quad V = \frac{4}{3}\pi R^3 \implies \frac{S}{V} = \frac{4\pi R^2}{\frac{4}{3}\pi R^3} = \frac{3}{R}"
    story.append(he.build_intermediate_equation(step2_1_text, step2_1_eq, styles=styles, is_expanded_from_slide=True))

    step2_2_text = (
        "Xác định tỷ lệ số nguyên tử nằm ở lớp bề mặt <i>N</i><sub>s</sub> so với tổng số nguyên tử của hạt <i>N</i><sub>total</sub>. "
        "Giả sử lớp nguyên tử bề mặt có bề dày hiệu dụng <i>d</i><sub>atom</sub> (cỡ hằng số mạng 0.3 nm). "
        "Thể tích phần lõi bên trong là vỏn vẹn hình cầu bán kính <i>R</i> − <i>d</i><sub>atom</sub>:"
    )
    step2_2_eq = r"\frac{N_s}{N_{\mathrm{total}}} = \frac{V_{\mathrm{total}} - V_{\mathrm{core}}}{V_{\mathrm{total}}} = \frac{\frac{4}{3}\pi R^3 - \frac{4}{3}\pi (R - d_{\mathrm{atom}})^3}{\frac{4}{3}\pi R^3} = 1 - \left( 1 - \frac{d_{\mathrm{atom}}}{R} \right)^3"
    story.append(he.build_intermediate_equation(step2_2_text, step2_2_eq, styles=styles, is_expanded_from_slide=True))

    step2_3_text = (
        "Dẫn xuất phương trình suy giảm nhiệt độ nóng chảy Gibbs-Thomson từ cân bằng hóa thế nhiệt động học giữa pha rắn và pha lỏng. "
        "Do mặt cong lồi của hạt nano, áp suất phụ Laplace chênh lệch giữa hai pha được xác định bởi độ cong mặt cầu. "
        "Khai triển hóa thế gần điểm nóng chảy khối và cân bằng thế nhiệt động:"
    )
    step2_3_eq = r"\mu_s(T, P + \Delta P) = \mu_l(T, P) \implies -(S_s - S_l)(T_m - T_{m,\mathrm{bulk}}) + V_s \Delta P = 0 \implies \frac{\Delta T_m}{T_{m,\mathrm{bulk}}} = - \frac{2\gamma_{\mathrm{sv}}}{\rho_s \Delta H_f R}"
    story.append(he.build_intermediate_equation(step2_3_text, step2_3_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g2_p4 = (
        "<b>Khảo sát tiệm cận vật liệu khối (<i>R</i> → ∞):</b> Khi kích thước hạt tăng lên thang micromet và milimet, "
        "số hạng hiệu chỉnh suy giảm nhiệt độ tiến dần về 0. "
        "Nhiệt độ nóng chảy đạt giá trị hằng số nội tại <i>T</i><sub>m</sub>(<i>R</i>) → <i>T</i><sub>m,bulk</sub>, "
        "hệ thống tuân thủ nghiêm ngặt nhiệt động lực học vĩ mô cổ điển.<br/>"
        "<b>Khảo sát tiệm cận bán kính tới hạn sụp đổ pha (<i>R</i> → <i>R</i><sub>crit</sub>):</b> "
        "Đối với hạt nano Vàng (Gold Au), nhiệt độ nóng chảy khối là <i>T</i><sub>m,bulk</sub> = 1337.33 K (1064 °C), "
        "khối lượng riêng <i>ρ</i><sub>s</sub> = 19 300 kg·m⁻³, năng lượng bề mặt <i>γ</i><sub>sv</sub> ≈ 1.4 J·m⁻², "
        "nhiệt nóng chảy <i>ΔH</i><sub>f</sub> = 6.37 × 10⁴ J·kg⁻¹. Hệ số đặc trưng Gibbs-Thomson xấp xỉ 1.4 nm.<br/>"
        "Khi bán kính hạt nano vàng co nhỏ xuống <i>R</i> = 3 nm, nhiệt độ nóng chảy sụt giảm còn khoảng 713 K (khoảng 440 °C).<br/>"
        "Khi hạt giảm xuống <i>R</i> = 1.5 nm, nhiệt độ nóng chảy giảm xuống dưới 300 °C (giảm hơn 760 °C so với vàng khối). "
        "Hiện tượng sụt giảm nhiệt độ nóng chảy đột biến này được ứng dụng trực tiếp trong kỹ thuật in vi mạch bán dẫn bằng mực nano vàng/bạc: "
        "cho phép thiêu kết các đường dẫn nano kim loại ở nhiệt độ thấp mà không làm nóng chảy hay cháy đế polymer mềm dẻo."
    )
    story.append(he.make_paragraph(g2_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_surf = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Một nhóm nghiên cứu tuyên bố sử dụng các hạt xúc tác nano Platin (Pt) có đường kính <i>D</i> = 2 nm "
        "đã nâng cao hoạt tính chuyển hóa phản ứng trong pin nhiên liệu hydro (PEMFC) lên gấp 100 lần so với bột xúc tác Platin thông thường đường kính <i>D</i> = 200 nm "
        "tại cùng một tổng khối lượng kim loại quý tiêu hao.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Hoạt tính phản ứng xúc tác dị thể tỷ lệ thuận trực tiếp với tổng diện tích bề mặt tiếp xúc "
        "và mật độ các nguyên tử bề mặt có liên kết phối trí thấp. "
        "Tại cùng khối lượng kim loại, tổng diện tích bề mặt tỷ lệ nghịch với bán kính hạt. "
        "Tỷ số diện tích bề mặt giữa hạt 2 nm và hạt 200 nm bằng tỷ số nghịch đảo bán kính đạt chính xác 100 lần. "
        "Đồng thời, tỷ lệ nguyên tử bề mặt của hạt 2 nm đạt xấp xỉ 60%, trong khi ở hạt 200 nm tỷ lệ này chỉ vỏn vẹn 0.6%.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Phản ứng xúc tác chỉ xảy ra trên bề mặt chất rắn. Các nguyên tử Platin nằm sâu trong lõi của hạt micro 200 nm hoàn toàn không tham gia phản ứng mà chỉ đóng vai trò chất mang trơ. "
        "Khi thu nhỏ kích thước hạt xuống 2 nm, 60% lượng nguyên tử Platin được phơi lộ ra ngoài bề mặt, giải phóng tối đa số tâm hoạt tính hóa học trên một gram vật liệu.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù nghiêm trọng là bỏ qua hiện tượng lão hóa vón cục (Ostwald Ripening): "
        "hạt nano càng nhỏ mang năng lượng bề mặt càng lớn, khiến chúng có xu hướng nhiệt động tự phát liên kết lại với nhau để giảm diện tích bề mặt, "
        "làm mất hoạt tính xúc tác nhanh chóng sau vài chu kỳ vận hành nếu không được gắn giữ chặt chẽ trên giá đỡ carbon cấu trúc xốp."
    )
    story.append(he.make_paragraph(cer_surf, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.1.3: BIẾN ĐỔI TÍNH CHẤT ĐIỆN & QUANG TRONG NANO BÁN DẪN
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.1.3: Biến đổi tính chất điện &amp; quang trong vật liệu nano bán dẫn", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g3_p1 = (
        "Trong vật liệu bán dẫn khối (Bulk semiconductors), chuyển động của electron trong dải dẫn và lỗ trống trong dải hóa trị "
        "hoàn toàn tự do theo ba chiều không gian, hình thành các dải năng lượng liên tục được ngăn cách bởi năng lượng dải cấm nội tại <i>E</i><sub>g,bulk</sub>. "
        "Tuy nhiên, khi kích thước không gian của tinh thể bán dẫn bị thu hẹp xuống nhỏ hơn hoặc tương đương với <b>Bán kính Bohr của exciton</b> "
        "(ký hiệu <i>a</i><sub>B</sub>, thường nằm trong khoảng 2 nm đến 15 nm), "
        "chuyển động của hạt tải điện bị giam hãm ngặt nghèo trong một hố thế thế năng hữu hạn. "
        "Hiện tượng này được gọi là <b>Hiệu ứng giam cầm lượng tử không gian (Quantum Confinement Effect)</b>.<br/>"
        "Hệ quả trực tiếp của giam cầm lượng tử là các dải năng lượng liên tục bị xé nhỏ thành các mức năng lượng gián đoạn, "
        "đồng thời khoảng cách giữa mức năng lượng thấp nhất của dải dẫn và mức cao nhất của dải hóa trị (dải cấm hiệu dụng <i>E</i><sub>g</sub>(<i>R</i>)) "
        "bị giãn rộng ra khi kích thước hạt nano thu nhỏ lại. Hiện tượng dời năng lượng phát xạ này được gọi là <b>Dịch chuyển sang phía xanh (Blue-shift)</b>. "
        "Song song với bán dẫn vô cơ 0D (chấm lượng tử), vật liệu nano carbon — đặc biệt là Ống nano carbon (Carbon Nanotubes — CNTs) — "
        "đã mở ra một kỷ nguyên mới cho linh kiện điện tử tốc độ cao. Tùy thuộc vào vector định hướng cuộn mạng tổ ong graphene (Chiral vector (<i>n</i>, <i>m</i>)), "
        "ống nano carbon có thể biểu hiện tính kim loại hoàn hảo (vận tốc hạt tải Fermi đạt 10⁶ m/s) hoặc tính bán dẫn với dải cấm điều khiển được, "
        "cho phép chế tạo các transistor trường nano (CNT-FET) vượt qua giới hạn vật lý của định luật Moore trên Silicon."
    )
    story.append(he.make_paragraph(g3_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh ống nano carbon CNT trong bán dẫn
    img_cnt = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_05_Carbon_Nanotubes_Ban_Dan.png")
    cap_cnt = "Hình 2.1.6: Ống nano carbon (CNT) và tiềm năng ứng dụng đột phá trong linh kiện bán dẫn điện tử hiệu suất cao."
    story.append(he.embed_figure_with_caption(img_cnt, cap_cnt, kind="orig", styles=styles))

    cnt_ocr_1 = "Cấu trúc hình học: Ống trụ rỗng hình thành từ tấm graphene cuộn lại theo vector chirality."
    cnt_ocr_2 = "Phân loại vật liệu: Ống nano đơn vách (SWCNT) đường kính 1 nm đến 2 nm và ống đa vách (MWCNT) đồng trục."
    cnt_ocr_3 = "Cơ chế dẫn điện: Vận chuyển đạn đạo (Ballistic transport) không tán xạ mạng trên quãng đường hàng micromet."
    cnt_ocr_4 = "Quy tắc chirality: Nếu hiệu số hai chỉ số n và m chia hết cho 3 thì mang tính kim loại; ngược lại mang tính bán dẫn."
    cnt_ocr_5 = "Ứng dụng đích: Thay thế kênh dẫn silicon trong chip vi xử lý thế hệ mới dưới 2 nm."
    story.append(he.make_paragraph(cnt_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(cnt_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(cnt_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(cnt_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(cnt_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh mô phỏng mô hình Brus
    img_sim_brus = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.1_Dich_Chuyen_Nang_Luong_Brus.png")
    cap_sim_brus = "Hình 2.1.7: Đồ thị mô phỏng giải tích MATLAB R2014b+: (a) Bóc tách thành phần động năng giam cầm và thế tương tác Coulomb trong chấm lượng tử CdSe; (b) Năng lượng dải cấm hiệu dụng theo bán kính cho các bán dẫn CdSe, InP, PbS."
    story.append(he.embed_figure_with_caption(img_sim_brus, cap_sim_brus, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g3_p2 = (
        "<b>Hạt nhân vật lý của phương trình Brus:</b> Louis E. Brus (Bell Labs, giải Nobel Hóa học 2023) đã thiết lập mô hình "
        "giải tích hoàn chỉnh dự đoán năng lượng dải cấm của chấm lượng tử bán dẫn hình cầu bán kính <i>R</i>. "
        "Mô hình Brus chứng minh rằng năng lượng dải cấm hiệu dụng là sự cạnh tranh giữa hai số hạng đối lập: "
        "(1) Số hạng động năng lượng tử hóa làm tăng năng lượng tỷ lệ nghịch với bình phương bán kính hạt; "
        "và (2) Số hạng thế năng tương tác tĩnh điện Coulomb giữa electron và lỗ trống làm giảm nhẹ năng lượng tỷ lệ nghịch bậc một."
    )
    story.append(he.make_paragraph(g3_p2, styles["Body"]))

    eq_brus = r"E_g(R) = E_{g,\mathrm{bulk}} + \frac{\hbar^2 \pi^2}{2 m_r^* R^2} - \frac{1.786\, e^2}{4\pi \varepsilon_0 \varepsilon_r R} - 0.248\, E_{Ry}^*"
    nom_brus = [
        ("Năng lượng dải cấm chấm lượng tử", "<i>E</i><sub>g</sub>(<i>R</i>)", "eV", "Khoảng cách năng lượng quang học phát xạ của chấm lượng tử bán kính R"),
        ("Dải cấm vật liệu bán dẫn khối", "<i>E</i><sub>g,bulk</sub>", "eV", "Năng lượng dải cấm nội tại của tinh thể khối vĩ mô"),
        ("Khối lượng hiệu dụng rút gọn", "<i>m</i><sub>r</sub>*", "kg", "Khối lượng hiệu dụng rút gọn của cặp electron và lỗ trống"),
        ("Độ điện thẩm tương đối (hằng số điện môi)", "<i>ε</i><sub>r</sub>", "1", "Hằng số điện môi tần số quang học của chất bán dẫn"),
        ("Bán kính chấm lượng tử", "<i>R</i>", "m", "Bán kính hình cầu giam cầm thế năng hữu hạn"),
        ("Năng lượng Rydberg exciton hiệu dụng", "<i>E</i><sub>Ry</sub>*", "eV", "Năng lượng liên kết exciton trong vật liệu khối")
    ]
    story.append(he.build_target_equation_block(eq_brus, nom_brus, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step3_1_text = (
        "Xét bài toán electron và lỗ trống bị giam cầm trong một giếng thế cầu vô hạn bán kính <i>R</i>. "
        "Giải phương trình Schrödinger không thời gian ở tọa độ cầu với hàm thế vô hạn bên ngoài. "
        "Nghiệm cơ bản đối xứng cầu là hàm Bessel cầu bậc không. "
        "Điều kiện biên triệt tiêu tại biên hạt đòi hỏi tích số vector sóng và bán kính bằng hằng số pi, dẫn tới động năng giam cầm của cặp hạt:"
    )
    step3_1_eq = r"E_{\mathrm{kin}} = \frac{\hbar^2 k_e^2}{2 m_e^*} + \frac{\hbar^2 k_h^2}{2 m_h^*} = \frac{\hbar^2 \pi^2}{2 R^2} \left( \frac{1}{m_e^*} + \frac{1}{m_h^*} \right) = \frac{\hbar^2 \pi^2}{2 m_r^* R^2}"
    story.append(he.build_intermediate_equation(step3_1_text, step3_1_eq, styles=styles, is_expanded_from_slide=True))

    step3_2_text = (
        "Bổ sung tương tác tĩnh điện Coulomb giữa electron mang điện tích −<i>e</i> và lỗ trống mang điện tích +<i>e</i>. "
        "Sử dụng lý thuyết nhiễu loạn bậc nhất lượng tử, tính kỳ vọng thế năng hút Coulomb trên hàm sóng cơ bản tích của hai hạt:"
    )
    step3_2_eq = r"\langle V_C \rangle = \iint |\psi_e(\mathbf{r}_e)|^2 \left( - \frac{e^2}{4\pi\varepsilon_0 \varepsilon_r |\mathbf{r}_e - \mathbf{r}_h|} \right) |\psi_h(\mathbf{r}_h)|^2 d^3\mathbf{r}_e d^3\mathbf{r}_h = - \frac{1.786\, e^2}{4\pi \varepsilon_0 \varepsilon_r R}"
    story.append(he.build_intermediate_equation(step3_2_text, step3_2_eq, styles=styles, is_expanded_from_slide=True))

    step3_3_text = (
        "Tổng hợp năng lượng trạng thái kích thích exciton nhỏ nhất của chấm lượng tử. "
        "Vì động năng giam cầm tỷ lệ nghịch với bình phương bán kính hạt, trong khi tương tác Coulomb chỉ tỷ lệ nghịch bậc một, "
        "khi bán kính <i>R</i> co nhỏ, số hạng động năng áp đảo tuyệt đối, khiến tổng năng lượng dải cấm tăng vọt:"
    )
    step3_3_eq = r"\Delta E_g(R) = E_g(R) - E_{g,\mathrm{bulk}} = \frac{\hbar^2 \pi^2}{2 m_r^* R^2} - \frac{1.786\, e^2}{4\pi \varepsilon_0 \varepsilon_r R} > 0"
    story.append(he.build_intermediate_equation(step3_3_text, step3_3_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g3_p4 = (
        "<b>Chế độ giam cầm mạnh (Strong Confinement Regime, <i>R</i> &lt;&lt; <i>a</i><sub>B</sub>):</b> "
        "Khi bán kính hạt nhỏ hơn rất nhiều so với bán kính Bohr exciton (ví dụ chấm lượng tử CdSe có <i>a</i><sub>B</sub> ≈ 5.6 nm, hạt chế tạo có <i>R</i> = 1.5 nm đến 3 nm), "
        "năng lượng giam cầm lượng tử (~ 1 eV) vượt trội hoàn toàn so với năng lượng liên kết Coulomb (~ 0.1 eV). "
        "Chuyển động của electron và lỗ trống độc lập nhau, quang phổ hấp thụ và phát quang thu hẹp thành các đỉnh sắc nét như vạch quang phổ của nguyên tử độc lập (nguyên tử nhân tạo).<br/>"
        "<b>Chế độ giam cầm yếu (Weak Confinement Regime, <i>R</i> &gt;&gt; <i>a</i><sub>B</sub>):</b> "
        "Khi bán kính hạt lớn hơn bán kính Bohr exciton, tương tác Coulomb giữ chặt electron và lỗ trống thành một giả hạt exciton chuyển động toàn xứ bên trong hạt nano. "
        "Dải cấm chỉ dời nhẹ một đại lượng tỷ lệ với bình phương nghịch đảo khối lượng tổng hai hạt.<br/>"
        "<b>So sánh vật liệu bán dẫn:</b> Đối với chì sunfua (PbS), hằng số điện môi rất cao (<i>ε</i><sub>r</sub> ≈ 169) làm giảm tương tác Coulomb xuống mức không đáng kể, "
        "và khối lượng hiệu dụng cực nhỏ dẫn tới bán kính Bohr exciton khổng lồ xấp xỉ 18 nm. "
        "Do đó, PbS biểu hiện giam cầm lượng tử cực mạnh trên dải kích thước rộng, cho phép điều chỉnh bước sóng phát xạ từ cận hồng ngoại (1600 nm) về vùng khả kiến."
    )
    story.append(he.make_paragraph(g3_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_brus = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Bằng cách điều khiển duy nhất thời gian phản ứng tổng hợp hóa học để thay đổi bán kính hạt nano CdSe từ <i>R</i> = 1.5 nm đến <i>R</i> = 4.0 nm, "
        "kỹ sư có thể tạo ra các dung dịch phát quang toàn dải màu sắc khả kiến (xanh lam, xanh lục, vàng, cam, đỏ) dưới cùng một nguồn kích thích tia cực tím UV (365 nm).<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Vật liệu khối CdSe có dải cấm <i>E</i><sub>g,bulk</sub> = 1.74 eV (bước sóng phát xạ hồng ngoại xấp xỉ 712 nm). "
        "Theo mô hình Brus, với hạt <i>R</i> = 1.5 nm: độ dịch dải cấm khoảng 1.25 eV, đưa năng lượng dải cấm lên xấp xỉ 2.99 eV (bước sóng phát quang 415 nm, ánh sáng xanh lam tím). "
        "Với hạt <i>R</i> = 4.0 nm: độ dịch dải cấm khoảng 0.22 eV, đưa năng lượng dải cấm lên xấp xỉ 1.96 eV (bước sóng 632 nm, ánh sáng đỏ rực rỡ).<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Bước sóng photon phát xạ khi tái hợp exciton tỷ lệ nghịch với năng lượng dải cấm hiệu dụng. "
        "Vì năng lượng giam cầm lượng tử tăng phi tuyến theo nghịch đảo bình phương bán kính hạt, việc thu nhỏ kích thước hạt làm tăng khoảng cách giữa mức đáy dải dẫn và đỉnh dải hóa trị, "
        "dịch chuyển năng lượng phát xạ trực tiếp sang dải sóng ngắn (Blue-shift). Cùng hấp thụ photon UV mang năng lượng cao hơn dải cấm, các electron bị kích thích sẽ hồi phục về đáy dải dẫn rồi tái hợp phát xạ photon có màu sắc được khóa cứng bởi kích thước hạt.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Sai lầm phổ biến là cho rằng màu phát quang thay đổi là do bản chất pha tinh thể biến tính. "
        "Thực tế cấu trúc mạng tinh thể Wurtzite của CdSe không hề thay đổi; sự biến đổi quang học 100% bắt nguồn từ hiệu ứng thuần túy cơ lượng tử của điều kiện biên giam cầm không gian."
    )
    story.append(he.make_paragraph(cer_brus, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.1.4: TÍNH CHẤT TỪ TÍNH & QUANG HỌC PLASMON
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.1.4: Biến đổi tính chất từ tính &amp; Quang học Plasmon", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g4_p1 = (
        "Trong các vật liệu từ tính cổ điển (như Sắt Fe, Coban Co, Niken Ni và các oxit ferit), cấu trúc từ tính nội tại được phân chia thành "
        "các miền từ hóa tự nhiên gọi là <b>Vùng từ hóa tự nhiên (Magnetic Domains / Miền Weiss)</b> nhằm làm cực tiểu hóa năng lượng từ tĩnh (Magnetostatic energy). "
        "Giữa các domain liền kề là các vách ngăn domain (Domain walls / Vách Bloch hoặc Néel) có bề dày đặc trưng xác định bởi sự cân bằng giữa năng lượng trao đổi lượng tử và năng lượng dị hướng từ tinh thể.<br/>"
        "Khi kích thước của hạt từ tính giảm xuống dưới một ngưỡng đường kính tới hạn <i>D</i><sub>crit</sub> (thường từ 10 nm đến 50 nm), "
        "năng lượng tiêu tốn để hình thành vách domain trở nên lớn hơn sự suy giảm năng lượng từ tĩnh. Khi đó, sự phân chia domain không còn thuận lợi về mặt năng lượng, "
        "và hạt nano bắt buộc phải tồn tại dưới dạng một <b>Hạt đơn domain (Single Domain Particle)</b> đồng nhất mang mômen từ khổng lồ (Siêu mômen từ có độ lớn từ 10³ đến 10⁵ mômen Bohr <i>μ</i><sub>B</sub>).<br/>"
        "Khi kích thước tiếp tục co nhỏ xuống dưới 10 nm, năng lượng dị hướng cản trở sự quay từ giảm xuống tương đương hoặc nhỏ hơn năng lượng dao động nhiệt. "
        "Dao động nhiệt lúc này đủ sức tự phát lật ngược hướng của toàn bộ siêu mômen từ hạt nano giữa các trục từ hóa dễ. "
        "Trạng thái kỳ lạ này được gọi là <b>Hiện tượng Siêu thuận từ (Superparamagnetism)</b>: vật liệu biểu hiện độ từ hóa bão hòa khổng lồ khi có từ trường ngoài, "
        "nhưng khi ngắt từ trường thì lực kháng từ và độ từ dư lập tức triệt tiêu hoàn toàn (<i>H</i><sub>c</sub> = 0, <i>M</i><sub>r</sub> = 0), xóa sạch hiện tượng trễ từ tính.<br/>"
        "Bên cạnh từ tính, tính chất quang học của hạt nano kim loại quý (Vàng Au, Bạc Ag, Đồng Cu) cũng biến đổi kỳ diệu nhờ hiện tượng "
        "<b>Cộng hưởng Plasmon Bề mặt Cục bộ (Localized Surface Plasmon Resonance — LSPR)</b>. Dưới điện trường của sóng ánh sáng tới, "
        "đám mây electron tự do trong hạt nano dao động tập thể lệch khỏi mạng ion dương, tạo ra điện trường cục bộ tăng cường hàng triệu lần "
        "và hấp thụ ánh sáng cực mạnh tại bước sóng cộng hưởng Fröhlich."
    )
    story.append(he.make_paragraph(g4_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh vật liệu từ tính nano gốc
    img_mag = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_06_Hat_Tu_Tinh_Nano.png")
    cap_mag = "Hình 2.1.8: Cấu trúc hạt nano từ tính — sự biến đổi năng lượng dị hướng từ và trạng thái đơn domain chi phối khả năng lưu trữ thông tin."
    story.append(he.embed_figure_with_caption(img_mag, cap_mag, kind="orig", styles=styles))

    mag_ocr_1 = "Sơ đồ chuyển biến domain: Từ vật liệu khối đa domain phân cách bởi vách Bloch chuyển thành hạt nano đơn domain."
    mag_ocr_2 = "Các đại lượng năng lượng cạnh tranh: Năng lượng từ tĩnh, năng lượng trao đổi lượng tử và năng lượng dị hướng từ tinh thể."
    mag_ocr_3 = "Cơ chế siêu thuận từ: Mômen từ khổng lồ dao động hỗn loạn theo nhiệt độ khi kích thước hạt nano dưới ngưỡng tới hạn."
    mag_ocr_4 = "Hệ quả từ trễ: Đường cong từ hóa M(H) không còn diện tích trễ, triệt tiêu lực kháng từ Hc."
    mag_ocr_5 = "Ứng dụng công nghệ: Hạt nano từ tính dẫn thuốc hướng đích và phát nhiệt từ tính diệt khối u ung thư (Hyperthermia)."
    story.append(he.make_paragraph(mag_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(mag_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(mag_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(mag_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(mag_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Nhúng ảnh quang học nano gốc
    img_opt = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_07_Quang_Hoc_Nano.png")
    cap_opt = "Hình 2.1.9: Quang học nano — các ứng dụng lớp phủ nano, bộ tách sóng quang học và phân cực ánh sáng."
    story.append(he.embed_figure_with_caption(img_opt, cap_opt, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    # Nhúng ảnh mô phỏng siêu thuận từ Néel
    img_sim_neel = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.1_Sieu_Thuan_Tu_Neel.png")
    cap_sim_neel = "Hình 2.1.10: Đồ thị mô phỏng giải tích MATLAB R2014b+: (a) Đường cong từ hóa M(H) so sánh sắt từ có trễ và hạt siêu thuận từ theo hàm Langevin; (b) Thời gian hồi phục Néel theo đường kính hạt nano Fe3O4 và xác định nhiệt độ chặn TB."
    story.append(he.embed_figure_with_caption(img_sim_neel, cap_sim_neel, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g4_p2 = (
        "<b>Hạt nhân vật lý của thời gian hồi phục Néel &amp; Cộng hưởng Plasmon:</b><br/>"
        "Đối với hạt nano từ tính đơn domain, rào thế năng lượng ngăn cản sự đảo chiều của mômen từ tỷ lệ thuận với thể tích hạt. "
        "Theo mô hình Néel–Brown, thời gian hồi phục tự phát <i>τ</i><sub>N</sub> tuân theo quy luật kích hoạt nhiệt hàm mũ Arrhenius.<br/>"
        "Đối với hạt nano kim loại trong trường điện từ quang học, tiết diện dập tắt photon cực đại khi phần thực của hằng số điện môi kim loại "
        "thỏa mãn chính xác <b>Điều kiện Fröhlich</b>: Re[<i>ε</i><sub>m</sub>(<i>ω</i>)] = −2<i>ε</i><sub>d</sub>."
    )
    story.append(he.make_paragraph(g4_p2, styles["Body"]))

    eq_neel_plasmon = r"\tau_N = \tau_0 \exp\left( \frac{K V}{k_B T} \right) \quad \text{và} \quad \sigma_{\mathrm{ext}}(\omega) = \frac{9\omega V \varepsilon_d^{3/2}}{c} \frac{\varepsilon_2(\omega)}{[\varepsilon_1(\omega) + 2\varepsilon_d]^2 + \varepsilon_2(\omega)^2}"
    nom_neel_plasmon = [
        ("Thời gian hồi phục Néel", "<i>τ</i><sub>N</sub>", "s", "Thời gian trung bình để mômen từ tự đảo chiều do kích thích nhiệt"),
        ("Thời gian hồi phục tự nhiên", "<i>τ</i><sub>0</sub>", "s", "Thời gian con lắc hồi phục thử nghiệm mômen (thường cỡ 10⁻⁹ s)"),
        ("Hằng số dị hướng từ tinh thể", "<i>K</i>", "J·m⁻³", "Mật độ năng lượng cản trở mômen từ lệch khỏi trục từ hóa dễ"),
        ("Thể tích của hạt nano", "<i>V</i>", "m³", "Thể tích hình học của hạt nano hình cầu đường kính D"),
        ("Hằng số Boltzmann", "<i>k</i><sub>B</sub>", "J·K⁻¹", "Hằng số nhiệt động lực học CODATA 2022: 1.380649 × 10⁻²³ J/K"),
        ("Hằng số điện môi của môi trường", "<i>ε</i><sub>d</sub>", "1", "Độ điện thẩm tương đối của môi trường điện môi bao quanh"),
        ("Hằng số điện môi phức của kim loại", "<i>ε</i>(<i>ω</i>) = <i>ε</i>₁ + <i>iε</i>₂", "1", "Hàm điện môi mô tả đáp ứng của khí electron tự do Drude")
    ]
    story.append(he.build_target_equation_block(eq_neel_plasmon, nom_neel_plasmon, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step4_1_text = (
        "Xác định kích thước tới hạn của hạt đơn domain <i>R</i><sub>c</sub> bằng cách so sánh tổng năng lượng của hạt đơn domain "
        "và hạt bị chia thành hai domain ngăn cách bởi vách Bloch. Năng lượng từ tĩnh giảm tỷ lệ với thể tích, "
        "trong khi năng lượng tạo vách domain tỷ lệ với diện tích mặt cắt hình học:"
    )
    step4_1_eq = r"E_{\mathrm{single}} = \frac{1}{2} \mu_0 N M_s^2 \left( \frac{4}{3}\pi R^3 \right), \quad E_{\mathrm{two}} = \frac{1}{4} \mu_0 N M_s^2 \left( \frac{4}{3}\pi R^3 \right) + \gamma_{\mathrm{wall}} \pi R^2 \implies R_c \approx \frac{9 \gamma_{\mathrm{wall}}}{\mu_0 M_s^2}"
    story.append(he.build_intermediate_equation(step4_1_text, step4_1_eq, styles=styles, is_expanded_from_slide=True))

    step4_2_text = (
        "Xác suất vượt rào thế dị hướng từ trong một đơn vị thời gian tuân theo phân bố thống kê nhiệt Boltzmann. "
        "Độ từ hóa chuẩn hóa của tập hợp các hạt siêu thuận từ dưới từ trường ngoài <i>H</i> được mô tả chính xác bởi hàm Langevin cổ điển:"
    )
    step4_2_eq = r"\frac{M(H)}{M_s} = L(\xi) = \coth(\xi) - \frac{1}{\xi} \quad \text{với} \quad \xi = \frac{\mu H}{k_B T} = \frac{M_s V H}{k_B T}"
    story.append(he.build_intermediate_equation(step4_2_text, step4_2_eq, styles=styles, is_expanded_from_slide=True))

    step4_3_text = (
        "Trong quang học plasmon, hạt nano kim loại hình cầu bán kính nhỏ hơn rất nhiều so với bước sóng được mô tả trong gần đúng tĩnh điện lưỡng cực. "
        "Mômen lưỡng cực cảm ứng của hạt nano đặt trong điện trường tỷ lệ với độ phân cực lưỡng cực. "
        "Độ phân cực lưỡng cực phụ thuộc vào hàm điện môi phức của kim loại và môi trường:"
    )
    step4_3_eq = r"\alpha(\omega) = R^3 \frac{\varepsilon_m(\omega) - \varepsilon_d}{\varepsilon_m(\omega) + 2\varepsilon_d} \implies \sigma_{\mathrm{ext}}(\omega) = k \cdot \mathrm{Im}[\alpha(\omega)] = \frac{9\omega V \varepsilon_d^{3/2}}{c} \frac{\varepsilon_2(\omega)}{[\varepsilon_1(\omega) + 2\varepsilon_d]^2 + \varepsilon_2(\omega)^2}"
    story.append(he.build_intermediate_equation(step4_3_text, step4_3_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g4_p4 = (
        "<b>Nhiệt độ chặn (Blocking Temperature <i>T</i><sub>B</sub>):</b> "
        "Thời gian đo thực nghiệm tiêu chuẩn của các thiết bị đo từ tính (SQUID hoặc VSM) thường khoảng 100 s. "
        "Từ phương trình Néel, điều kiện để hạt chuyển trạng thái tại thời điểm đo là thời gian hồi phục bằng thời gian đo thực nghiệm. "
        "Tỷ số năng lượng dị hướng trên nhiệt năng tại nhiệt độ chặn tính được xấp xỉ 25 lần hằng số Boltzmann nhân nhiệt độ.<br/>"
        "• Khi nhiệt độ cao hơn nhiệt độ chặn (<i>T</i> &gt; <i>T</i><sub>B</sub>): Năng lượng nhiệt làm đảo chiều mômen từ nhanh hơn thời gian đo, hệ thống ở trạng thái siêu thuận từ, không có lực kháng từ (<i>H</i><sub>c</sub> = 0).<br/>"
        "• Khi nhiệt độ thấp hơn nhiệt độ chặn (<i>T</i> &lt; <i>T</i><sub>B</sub>): Siêu mômen từ bị 'đóng băng' cố định dọc theo trục dị hướng từ tinh thể, vật liệu biểu hiện tính sắt từ thông thường với vòng từ trễ mở rộng (<i>H</i><sub>c</sub> &gt; 0).<br/>"
        "<b>Độ dịch chuyển Plasmon Fröhlich theo môi trường:</b> "
        "Vì điều kiện cộng hưởng đòi hỏi phần thực của hàm điện môi kim loại bằng âm hai lần điện thẩm môi trường, "
        "khi chiết suất môi trường xung quanh hạt nano vàng tăng lên (ví dụ khi có kháng thể hoặc phân tử sinh học gắn kết lên bề mặt), "
        "đỉnh hấp thụ LSPR lập tức dịch chuyển về phía bước sóng dài (Red-shift). "
        "Hiệu ứng này là nguyên lý vận hành của các cảm biến sinh học nano không cần chất đánh dấu (Label-free Nanoplasmonic Biosensors) với độ nhạy phát hiện nồng độ phân tử ở mức picomolar."
    )
    story.append(he.make_paragraph(g4_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_mag = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Các nhà sản xuất đĩa cứng máy tính (HDD) không thể tiếp tục thu nhỏ kích thước hạt ghi từ tính (Magnetic grains) "
        "xuống dưới 5 nm để tăng mật độ lưu trữ dữ liệu lên vô hạn trên công nghệ ghi từ hiện tại.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Để lưu trữ dữ liệu bền vững không bị mất mát thông tin trong vòng 10 năm (khoảng 3.15 × 10⁸ s), "
        "thời gian hồi phục Néel đòi hỏi tỷ số giữa năng lượng dị hướng từ và năng lượng nhiệt phải đạt tối thiểu 40 lần (tại 340 K trong ổ cứng). "
        "Nếu thể tích hạt giảm theo lũy thừa ba của đường kính hạt, khi đường kính nhỏ hơn 5 nm, năng lượng dị hướng tụt xuống dưới ngưỡng ổn định nhiệt.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Khi năng lượng dị hướng nhỏ hơn 40 lần năng lượng nhiệt, hạt từ tính chuyển sang trạng thái siêu thuận từ. "
        "Dao động nhiệt ngẫu nhiên ở nhiệt độ hoạt động của máy tính sẽ tự động lật ngược hướng mômen từ của bit ghi (từ trạng thái '1' đảo sang '0' và ngược lại), "
        "dẫn tới sự phá hủy tự phát hoàn toàn toàn bộ dữ liệu số đã ghi. Rào cản vật lý tối thượng này được gọi là <b>Giới hạn siêu thuận từ (Superparamagnetic Limit)</b>.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Kỹ sư thường nghĩ rằng chỉ cần tăng hằng số dị hướng <i>K</i> bằng vật liệu mới (như hợp kim FePt) là giải quyết được vấn đề. "
        "Điểm mù là: khi <i>K</i> quá lớn, từ trường ngoài cần thiết để ghi dữ liệu (đảo chiều từ hóa) vượt quá từ trường bão hòa tối đa của đầu ghi từ thông thường (khoảng 2.4 Tesla), "
        "đòi hỏi phải phát triển công nghệ ghi từ có hỗ trợ nhiệt HAMR (Heat-Assisted Magnetic Recording) bằng laser nano."
    )
    story.append(he.make_paragraph(cer_mag, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.1.5: "IT ALL STARTS WITH A BOX..." - NỀN TẢNG HỆ CHIỀU THẤP
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.1.5: “It all starts with a box…” - Nền tảng Vật lý lượng tử của Hệ chiều thấp", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g5_p1 = (
        "Triết lý sâu sắc của vật lý chất rắn và công nghệ nano hiện đại được gói gọn trong châm ngôn kinh điển: "
        "<i>'It all starts with a box…'</i> (Mọi cấu trúc nano phức tạp đều khởi nguồn từ bài toán hộp thế lượng tử cơ bản). "
        "Trong cơ học lượng tử, hộp thế là mô hình mẫu mực để chứng minh cách thức mà sự giam cầm không gian làm biến đổi hàm sóng và lượng tử hóa phổ năng lượng.<br/>"
        "Từ mô hình hộp thế ba chiều, bằng cách thu hẹp kích thước của một, hai hoặc cả ba chiều không gian xuống thang đo bước sóng De Broglie của hạt tải, "
        "chúng ta tạo ra toàn bộ hệ thống phân loại các <b>Hệ chiều thấp (Low-dimensional Systems)</b> nền tảng của công nghệ nano hiện đại:<br/>"
        "• <b>Vật liệu khối 3D (Bulk):</b> Không có chiều nào bị giam cầm. "
        "Hạt tải chuyển động tự do theo cả 3 chiều, phổ năng lượng liên tục dạng parabol.<br/>"
        "• <b>Giếng lượng tử 2D (Quantum Well):</b> Bị giam cầm theo 1 chiều không gian (bề dày màng bán dẫn cỡ vài nanomet), "
        "hạt tải chỉ tự do chuyển động trong mặt phẳng 2 chiều (<i>x</i>, <i>y</i>).<br/>"
        "• <b>Dây lượng tử 1D (Quantum Wire):</b> Bị giam cầm theo 2 chiều không gian, "
        "hạt tải chỉ có thể di chuyển dọc theo duy nhất 1 trục chiều dài (ống nano carbon, dây nano bán dẫn Si/GaAs).<br/>"
        "• <b>Chấm lượng tử 0D (Quantum Dot):</b> Bị giam cầm ngặt nghèo theo cả 3 chiều không gian, "
        "hạt tải bị giam giữ cố định tại một điểm, triệt tiêu mọi bậc tự do chuyển động tịnh tiến."
    )
    story.append(he.make_paragraph(g5_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh hộp thế lượng tử gốc
    img_box = os.path.join(kho_anh, "[Goc]_Muc_2.1_Hinh_08_Hop_The_Luong_Tu_Box.png")
    cap_box = "Hình 2.1.11: Sơ đồ giam cầm lượng tử từ khối 3D, giếng 2D, dây 1D đến chấm 0D ('It all starts with a box')."
    story.append(he.embed_figure_with_caption(img_box, cap_box, kind="orig", styles=styles))

    box_ocr_1 = "Phân loại phân bậc chiều không gian: Khối 3D (Bulk), Giếng 2D (Well), Dây 1D (Wire) và Chấm 0D (Dot)."
    box_ocr_2 = "Các chiều tự do không bị giam cầm: 3 chiều (3D), 2 chiều (2D), 1 chiều (1D) và 0 chiều (0D)."
    box_ocr_3 = "Cơ chế sóng dừng: Hàm sóng điện tử hình thành các bụng và nút sóng dừng dọc theo các phương bị giam giữ."
    box_ocr_4 = "Tiến hóa mật độ trạng thái DOS g(E): Biến đổi từ đường cong căn bậc hai liên tục thành các vạch delta gián đoạn."
    box_ocr_5 = "Hệ quả linh kiện: Giảm dòng ngưỡng và triệt tiêu độ phụ thuộc nhiệt độ trong laser bán dẫn."
    story.append(he.make_paragraph(box_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(box_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(box_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(box_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(box_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g5_p2 = (
        "<b>Hạt nhân vật lý của hộp thế lượng tử ba chiều:</b> Xét một hạt khối lượng hiệu dụng <i>m</i>* bị giam cầm trong hộp thế năng lập phương "
        "có các cạnh <i>L</i><sub>x</sub>, <i>L</i><sub>y</sub>, <i>L</i><sub>z</sub> với thế năng bằng 0 bên trong và vô hạn bên ngoài. "
        "Các mức năng lượng trị riêng được xác định bằng điều kiện sóng dừng cơ lượng tử ba chiều."
    )
    story.append(he.make_paragraph(g5_p2, styles["Body"]))

    eq_box_3d = r"E_{n_x, n_y, n_z} = \frac{\pi^2 \hbar^2}{2 m^*} \left( \frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2} \right) \quad (n_x, n_y, n_z \in \{1, 2, 3, \dots\})"
    nom_box_3d = [
        ("Mức năng lượng giam cầm lượng tử", "<i>E</i><sub>nx, ny, nz</sub>", "eV", "Trị riêng năng lượng gián đoạn của hạt trong hộp thế"),
        ("Các số lượng tử không gian", "<i>n</i><sub>x</sub>, <i>n</i><sub>y</sub>, <i>n</i><sub>z</sub>", "1", "Các số nguyên dương quy định số nút sóng dọc theo từng trục tọa độ"),
        ("Kích thước giam cầm không gian", "<i>L</i><sub>x</sub>, <i>L</i><sub>y</sub>, <i>L</i><sub>z</sub>", "m", "Độ rộng của hộp thế theo các trục tọa độ Descartes"),
        ("Khối lượng hiệu dụng của hạt tải", "<i>m</i>*", "kg", "Khối lượng hiệu dụng của hạt dẫn xuất từ độ cong dải năng lượng"),
        ("Hằng số Planck rút gọn", "<i>ℏ</i>", "J·s", "Hằng số tác dụng lượng tử vi mô")
    ]
    story.append(he.build_target_equation_block(eq_box_3d, nom_box_3d, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))

    step5_1_text = (
        "Thiết lập phương trình vi phân đạo hàm riêng Schrödinger độc lập thời gian cho hạt chuyển động trong vùng thế năng bằng 0. "
        "Sử dụng phương pháp tách biến hàm sóng tọa độ Descartes thành tích của ba hàm sóng thành phần độc lập:"
    )
    step5_1_eq = r"-\frac{\hbar^2}{2m^*} \left( \frac{1}{X} \frac{d^2 X}{dx^2} + \frac{1}{Y} \frac{d^2 Y}{dy^2} + \frac{1}{Z} \frac{d^2 Z}{dz^2} \right) = E_x + E_y + E_z = E"
    story.append(he.build_intermediate_equation(step5_1_text, step5_1_eq, styles=styles, is_expanded_from_slide=True))

    step5_2_text = (
        "Áp dụng điều kiện biên triệt tiêu nghiêm ngặt của hàm sóng tại các vách thành hộp. "
        "Hàm sóng nghiệm riêng là tích của các hàm sóng dừng dạng sin, khóa cứng các thành phần vector sóng ở giá trị lượng tử hóa:"
    )
    step5_2_eq = r"k_x = \frac{n_x \pi}{L_x}, \quad k_y = \frac{n_y \pi}{L_y}, \quad k_z = \frac{n_z \pi}{L_z} \quad (n_x, n_y, n_z \ge 1)"
    story.append(he.build_intermediate_equation(step5_2_text, step5_2_eq, styles=styles, is_expanded_from_slide=True))

    step5_3_text = (
        "Dẫn xuất hàm Mật độ trạng thái điện tử (Density of States — DOS) định nghĩa là số lượng trạng thái lượng tử khả dụng "
        "trên một đơn vị năng lượng và một đơn vị thể tích. Khi kích thước giam cầm giảm dần số chiều, hình thái hàm DOS biến đổi sâu sắc:"
    )
    step5_3_eq = r"g_{\mathrm{3D}}(E) = \frac{(2m^*)^{3/2}}{2\pi^2 \hbar^3} \sqrt{E - E_c}, \quad g_{\mathrm{2D}}(E) = \frac{m^*}{\pi \hbar^2} \sum_n \Theta(E - E_n), \quad g_{\mathrm{0D}}(E) = 2 \sum_i \delta(E - E_i)"
    story.append(he.build_intermediate_equation(step5_3_text, step5_3_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Phân tích các biến thể & Khảo sát tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Phân tích các biến thể &amp; Khảo sát tiệm cận", styles["H3"]))
    g5_p4 = (
        "<b>Ma trận tiến hóa Mật độ trạng thái (DOS Evolution):</b><br/>"
        "• <b>3D Bulk:</b> Mật độ trạng thái tăng liên tục theo căn bậc hai của năng lượng. "
        "Khi bơm hạt tải, electron phân bố dàn trải trên một khoảng năng lượng rộng, làm giảm mật độ quang phổ tại bước sóng đỉnh.<br/>"
        "• <b>2D Quantum Well:</b> Mật độ trạng thái có dạng bậc thang không phụ thuộc năng lượng (Hàm bước nhảy Heaviside). "
        "Ngay tại đáy dải con, mật độ trạng thái nhảy vọt lên một giá trị hằng số, cho phép hạt tải tập trung mật độ cao ngay tại ngưỡng kích thích.<br/>"
        "• <b>1D Quantum Wire:</b> Mật độ trạng thái biểu hiện các điểm kỳ dị van Hove phân kỳ tiệm cận tỷ lệ nghịch với căn bậc hai năng lượng tại đáy mỗi dải con.<br/>"
        "• <b>0D Quantum Dot:</b> Mật độ trạng thái thu gọn thành các hàm delta Dirac lý tưởng tuyệt đối gián đoạn. "
        "100% hạt tải bơm vào bị ép buộc hội tụ chính xác tại duy nhất mức năng lượng lượng tử mong muốn mà không bị phân tán lãng phí."
    )
    story.append(he.make_paragraph(g5_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (CER)
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_box = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Diode Laser chấm lượng tử 0D (Quantum Dot Laser) sở hữu dòng ngưỡng kích thích (Threshold current <i>I</i><sub>th</sub>) "
        "siêu thấp và hệ số nhạy cảm nhiệt độ lý tưởng (hoạt động hoàn toàn trơ với sự biến thiên nhiệt độ môi trường) "
        "so với Diode Laser bán dẫn khối 3D truyền thống.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Dòng ngưỡng đảo mật độ tích lũy hạt tải tỷ lệ với tích phân dải mật độ trạng thái. "
        "Trong laser 3D, sự giãn rộng nhiệt Fermi-Dirac làm hạt tải tràn lên các trạng thái năng lượng cao, "
        "khiến dòng ngưỡng tăng vọt theo nhiệt độ với hệ số đặc trưng chỉ khoảng 60 K đến 120 K. "
        "Trong chấm lượng tử 0D, hàm DOS là vạch delta cô lập, "
        "không hề tồn tại bất kỳ trạng thái năng lượng lân cận nào để electron tràn nhiệt lên.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Vì hàm mật độ trạng thái của chấm lượng tử cô lập tại duy nhất một mức năng lượng, "
        "mọi electron được tiêm vào vùng tích cực đều rơi thẳng vào trạng thái phát xạ quang học kích thích mode đơn mà không bị phân tán nhiệt động học. "
        "Do đó, điều kiện nghịch đảo độ tích lũy dân số (Population Inversion) đạt được ở mật độ dòng cực tiểu, và sự thay đổi nhiệt độ môi trường "
        "không thể làm biến dạng phân bố hạt tải, mang lại hệ số ổn định nhiệt độ kỷ lục vượt trên 300 K.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù thực tế là hiện tượng phân bố kích thước không đồng đều (Size Inhomogeneity) "
        "của các chấm lượng tử tự lắp ráp (Self-assembled Stranski-Krastanov QDs). Trong chế tạo thực tế, độ thăng giáng kích thước chấm khoảng 10% "
        "làm giãn rộng vạch quang phổ delta thành đường cong phân bố Gauss, "
        "đòi hỏi kỹ thuật kiểm soát chế tạo màng tinh thể Epitaxy chùm phân tử (MBE) hoặc lắng đọng pha hơi hóa học hữu cơ kim loại (MOCVD) siêu chính xác."
    )
    story.append(he.make_paragraph(cer_box, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # TỔNG KẾT MỤC 2.1 & BẢN ĐỒ ĐIỀU HƯỚNG MỤC 2.2
    # =========================================================================
    story.append(he.make_paragraph("Tổng kết Mục 2.1 &amp; Bản đồ Điều hướng Mục 2.2 tiếp theo", styles["H2"]))
    summary_text = (
        "<b>Ma trận tổng hợp kiến thức cốt lõi Mục 2.1:</b><br/>"
        "1. <i>Cột mốc lịch sử:</i> Feynman (1959) khai phóng tư tưởng; Taniguchi (1974) định nghĩa gia công siêu chính xác; "
        "STM (1981) và AFM (1986) trao quyền năng quan sát và thao tác từng nguyên tử đơn lẻ qua cơ học lượng tử.<br/>"
        "2. <i>Hiệu ứng bề mặt:</i> Tỷ số diện tích bề mặt trên thể tích bùng nổ khi kích thước hạt co nhỏ dưới 10 nm; "
        "tỷ lệ nguyên tử bề mặt đạt 50% đến 80%; mô hình Gibbs-Thomson giải thích hiện tượng suy giảm hàng trăm độ của nhiệt độ nóng chảy.<br/>"
        "3. <i>Quang - điện bán dẫn:</i> Giam cầm lượng tử không gian khi kích thước hạt nhỏ hơn bán kính Bohr exciton; "
        "phương trình Brus bóc tách động năng lượng tử và thế Coulomb, mở rộng dải cấm hiệu dụng dời về phía xanh (Blue-shift); "
        "ống nano carbon CNT phân tách tính kim loại và bán dẫn theo vector chirality.<br/>"
        "4. <i>Từ tính &amp; Plasmon:</i> Hạt nano dưới kích thước domain tới hạn chuyển thành hạt đơn domain; "
        "hiện tượng siêu thuận từ Néel xuất hiện khi năng lượng nhiệt thắng rào dị hướng từ tính; "
        "cộng hưởng plasmon bề mặt cục bộ LSPR tăng cường trường quang học tại điều kiện Fröhlich.<br/>"
        "5. <i>Hệ chiều thấp:</i> Triết lý 'It all starts with a box' phân tầng không gian từ khối 3D, giếng 2D, dây 1D đến chấm 0D; "
        "mật độ trạng thái DOS tiến hóa từ liên tục căn bậc hai sang vạch delta Dirac, mở đường cho laser chấm lượng tử dòng ngưỡng siêu thấp.<br/><br/>"
        "<b>Mỏ neo điều hướng Mục 2.2 tiếp theo:</b><br/>"
        "Mục 2.2 sẽ đào sâu trực diện vào bản chất toán học và cơ chế vi mô của <i>Bản chất sóng - hạt của ánh sáng và vật chất</i> "
        "(Lưỡng tính sóng hạt De Broglie, nguyên lý bất định Heisenberg, hệ thức giao thoa hàm sóng và phương trình sóng Schrödinger dạng tổng quát)."
    )
    story.append(he.make_paragraph(summary_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # 3. Biên dịch tài liệu
    print("Bắt đầu gọi doc.build(story)...")
    doc.build(story)
    print("Biên dịch thành công!")

    # 4. Kiểm tra chất lượng và dung lượng
    compliance = he.assert_monograph_compliance(target_pdf, min_pages=5)
    print("Kết quả kiểm toán chất lượng (Compliance):", compliance)

    return compliance

if __name__ == "__main__":
    build_pdf()

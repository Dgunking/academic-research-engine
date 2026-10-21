# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Chương 2: Bản chất lượng tử của thế giới nano
Mục 2.6: Tiềm năng và xu hướng tương lai của công nghệ nano (Slide 71–75)
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
    target_pdf = os.path.join(bai_giang, "Chuyen_Khao_Nano_Muc_2.6.pdf")

    print(f"Bắt đầu biên dịch chuyên khảo Mục 2.6: {target_pdf}")

    # 2. Khởi tạo Styles và Document Template
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(target_pdf)
    story = []

    # =========================================================================
    # TIÊU ĐỀ ĐẦU CHUYÊN KHẢO (H1)
    # =========================================================================
    title_main = (
        "CHƯƠNG 2: BẢN CHẤT LƯỢNG TỬ CỦA THẾ GIỚI NANO<br/>"
        "MỤC 2.6: TIỀM NĂNG VÀ XU HƯỚNG TƯƠNG LAI CỦA CÔNG NGHỆ NANO"
    )
    story.append(he.make_paragraph(title_main, styles["H1"]))
    story.append(Spacer(1, 4))

    meta_info = (
        "<b>Hệ Thống Chuyên Khảo Giảng Dạy &amp; Nghiên Cứu Vật Lý Nano — ĐHBK Hà Nội</b><br/>"
        "<i>Chủ thể nghiên cứu:</i> Bùi Trung Dũng — Khoa Vật lý Kỹ thuật, Trường Đại học Bách khoa Hà Nội (HUST)<br/>"
        "<i>Tài liệu nguồn kép:</i> Bài giảng 'Bài 2-Quantum nature.pdf' (Slide 71–75), Bộ môn Vật liệu Điện tử — HUST; "
        "kết hợp các tài liệu quốc tế đỉnh cao: Lộ trình Thiết bị &amp; Hệ thống Quốc tế (IRDS 2023), "
        "Báo cáo nghiên cứu Viện Max Planck (Markus Antonietti) và Chuyên khảo Khoa học Vật liệu Nano Tiên tiến."
    )
    story.append(he.make_paragraph(meta_info, styles["Body"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=he.COLOR_PRIMARY, spaceBefore=4, spaceAfter=10))

    # =========================================================================
    # LỜI NÓI ĐẦU ĐỊNH VỊ HỌC THUẬT & TỔNG QUAN
    # =========================================================================
    overview_text = (
        "<b>Lời nói đầu định vị học thuật:</b> Công nghệ nano không chỉ là một nhánh kỹ thuật thu nhỏ kích thước vật lý, "
        "mà là một cuộc cách mạng công nghệ nền tảng tái định hình toàn bộ cấu trúc kinh tế, y tế, năng lượng và sinh thái của nhân loại "
        "trong thế kỷ 21. Khi các thiết bị vi điện tử tiếp cận giới hạn vật lý của Định luật Moore với kích thước cổng dưới 2 nm, "
        "các rào cản lượng tử (như dòng rò xuyên hầm) buộc ngành bán dẫn phải chuyển dịch sang kỷ nguyên <i>'More than Moore'</i> "
        "và mạch tích hợp quang tử nano. Đồng thời, các nhánh ứng dụng liên ngành bùng nổ mạnh mẽ: Y sinh học nano mở ra khả năng "
        "dẫn thuốc hướng đích tiêu diệt tế bào ung thư mà không gây độc tính toàn thân; Năng lượng sạch nano khai thác hiệu ứng sinh đa exciton (MEG) "
        "để phá vỡ giới hạn hiệu suất pin mặt trời truyền thống; Vật liệu nano composite mang lại độ bền cơ học siêu việt; "
        "và trên hết, như Giáo sư Markus Antonietti (Giám đốc Viện Max Planck) đã khẳng định, tiềm năng cao cả nhất của công nghệ nano "
        "chính là thanh lọc nguồn nước và bầu không khí để giải cứu hành tinh. Chuyên khảo Mục 2.6 bóc tách trọn vẹn 5 Luận điểm Vi mô (MPT) "
        "theo chuẩn mực sư phạm 5 giai đoạn lũy tiến, bám sát từng slide bài giảng và minh họa bằng đồ thị giải tích kỹ thuật chuẩn MATLAB R2014b+."
    )
    story.append(he.make_paragraph(overview_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # =========================================================================
    # LUẬN ĐIỂM 2.6.1: ĐỊNH LUẬT MOORE & GIỚI HẠN LƯỢNG TỬ
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.6.1: Định luật Moore, Lộ trình vi điện tử &amp; Giới hạn lượng tử", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g1_p1 = (
        "Năm 1965, Gordon Moore (đồng sáng lập tập đoàn Intel) đã đưa ra quan sát lịch sử mang tên <b>Định luật Moore</b>: "
        "Số lượng bóng bán dẫn (transistor) được tích hợp trên một đơn vị diện tích vi mạch vi xử lý sẽ tăng gấp đôi sau mỗi 18 đến 24 tháng, "
        "trong khi giá thành giảm đi một nửa. Lộ trình công nghệ vi điện tử suốt 60 năm qua đã tuân thủ chặt chẽ quy luật này, "
        "đưa số lượng transistor từ con số 2 300 trên chip Intel 4004 (năm 1971) lên tới hơn 100 tỷ transistor trên các chip xử lý hiện đại.<br/>"
        "Tuy nhiên, khi kích thước cổng của transistor thu nhỏ xuống dưới 3 nm (tương đương kích thước của vài chục nguyên tử Silic), "
        "công nghệ bán dẫn va phải <b>Rào cản giới hạn lượng tử</b> không thể đảo ngược: Lớp oxit cách điện cổng (SiO₂) trở nên quá mỏng "
        "(dưới 1.2 nm), khiến các electron dễ dàng xuyên hầm lượng tử trực tiếp qua rào thế, gây ra dòng điện rò rỉ khổng lồ "
        "làm chip quá nhiệt và mất khả năng đóng ngắt logic."
    )
    story.append(he.make_paragraph(g1_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 2.6.1
    img_moore = os.path.join(kho_anh, "[Goc]_Muc_2.6_Hinh_01_Dinh_Luat_Moore_Intel_Transistor.png")
    cap_moore = "Hình 2.6.1: Đường tăng trưởng số lượng transistor trên bộ vi xử lý Intel từ 1971 đến nay theo định luật Moore (Slide 71)."
    story.append(he.embed_figure_with_caption(img_moore, cap_moore, kind="orig", styles=styles))

    moore_ocr_1 = "Ghi lại đường cong tăng trưởng hàm mũ số lượng bóng bán dẫn trên một vi xử lý qua 5 thập kỷ."
    moore_ocr_2 = "Khởi điểm từ bộ vi xử lý 4-bit Intel 4004 (2300 transistor) đến dòng vi xử lý đa nhân Core i9 và Xeon (hàng chục tỷ transistor)."
    moore_ocr_3 = "Động lực kinh tế - kỹ thuật thúc đẩy sự bùng nổ của máy tính cá nhân, mạng Internet và trí tuệ nhân tạo."
    moore_ocr_4 = "Giai đoạn chuyển tiếp: Sự chậm lại của chu kỳ thu nhỏ kích thước hình học thuần túy từ sau năm 2010."
    moore_ocr_5 = "Chuyển dịch kiến trúc: Chuyển từ bóng bán dẫn phẳng MOSFET 2D sang cấu trúc 3D FinFET và bóng bán dẫn dây nano GAA-FET."
    story.append(he.make_paragraph(moore_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(moore_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(moore_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(moore_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(moore_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối thiểu & Trực giác vi mô
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g1_p2 = (
        "<b>Trực giác vi mô về sự phá hủy kênh dẫn bởi dòng rò xuyên hầm:</b> Hãy hình dung cực cổng (Gate) của transistor "
        "như một chiếc van nước kiểm soát dòng electron chảy từ cực nguồn (Source) sang cực máng (Drain). "
        "Lớp oxit cách điện bên dưới cổng đóng vai trò như đệm cao su ngăn không cho nước rò rỉ ra ngoài. "
        "Khi thu nhỏ transistor theo quy tắc Dennard scaling, lớp đệm cao su này bị mài mỏng dần. "
        "Khi bề dày chỉ còn 1 nm (khoảng 4 lớp nguyên tử SiO₂), bản chất sóng của electron trỗi dậy: hàm sóng của electron "
        "trong kênh dẫn thâm nhập xuyên qua lớp oxit sang cực cổng mà không cần leo qua rào thế năng lượng. "
        "Dòng rò ký sinh này làm tiêu tốn điện năng liên tục ngay cả khi chip đang ở chế độ nghỉ (Idle), "
        "biến vi xử lý thành một chiếc bàn là tỏa nhiệt hàng trăm watt trên một diện tích vỏn vẹn 1 cm²."
    )
    story.append(he.make_paragraph(g1_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 3: Trụ cột toán học & Dẫn xuất từng bước
    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_tunnel_gate = r"J_{\mathrm{tunnel}} = J_0 \left( \frac{V_{\mathrm{ox}}}{d_{\mathrm{ox}}} \right)^2 \exp\left( - \frac{4 \sqrt{2 m^*} \Phi_B^{3/2}}{3 \hbar q \mathcal{E}} \right) \approx J_0 \exp(- 2 \kappa d_{\mathrm{ox}})"
    nom_tunnel_gate = [
        ("Mật độ dòng rò xuyên hầm qua lớp cách điện cổng", "<i>J</i><sub>tunnel</sub>", "A/m²", "Cường độ dòng điện rò rỉ ký sinh trên một đơn vị diện tích cổng"),
        ("Bề dày lớp oxit cách điện cổng", "<i>d</i><sub>ox</sub>", "nm", "Khoảng cách cách điện vật lý giữa cực cổng kim loại và kênh dẫn bán dẫn"),
        ("Chiều cao rào thế năng lượng giao diện", "<i>Φ</i><sub>B</sub>", "eV", "Độ lệch dải dẫn giữa bán dẫn kênh và điện môi oxit (3.15 eV đối với Si/SiO₂)"),
        ("Điện trường bên trong oxit", "<i>E</i><sub>ox</sub>", "V/m", "Cường độ điện trường phân cực cực cổng: bằng hiệu điện thế chia cho bề dày oxit"),
        ("Khối lượng hiệu dụng xuyên hầm của electron", "<i>m</i>*", "kg", "Khối lượng hiệu dụng trong vùng cấm của điện môi oxit: xấp xỉ 0.5 <i>m</i><sub>0</sub> trong SiO₂")
    ]
    story.append(he.build_target_equation_block(eq_tunnel_gate, nom_tunnel_gate, styles=styles))
    story.append(Spacer(1, 6))

    step1_1_text = (
        "Thiết lập hệ số suy giảm hàm sóng electron bên trong rào thế năng lượng hình thang của lớp điện môi cổng theo phép gần đúng WKB:"
    )
    step1_1_eq = r"\kappa(z) = \frac{\sqrt{2 m^* \left( \Phi_B - q \mathcal{E} z \right)}}{\hbar} \implies T_{\mathrm{WKB}} = \exp\left( - 2 \int_0^{d_{\mathrm{ox}}} \kappa(z) dz \right)"
    story.append(he.build_intermediate_equation(step1_1_text, step1_1_eq, styles=styles, is_expanded_from_slide=True))

    step1_2_text = (
        "Thực hiện tích phân giải tích theo tọa độ không gian rào thế. Dưới điện áp phân cực thấp, rào thế xấp xỉ hình chữ nhật, "
        "dẫn tới sự phụ thuộc hàm mũ trực tiếp của mật độ dòng rò vào bề dày lớp oxit:"
    )
    step1_2_eq = r"J_{\mathrm{tunnel}} \approx J_0 \exp\left( - \frac{2 \sqrt{2 m^* \Phi_B}}{\hbar} d_{\mathrm{ox}} \right) = J_0 \exp(- 2 \kappa_0 d_{\mathrm{ox}})"
    story.append(he.build_intermediate_equation(step1_1_text, step1_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Biến thiên tham số & Quét tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g1_p4 = (
        "<b>Đột phá vật liệu High-k và Kiến trúc nano 3D:</b><br/>"
        "• <i>Vấn đề của SiO₂:</i> Với hằng số điện môi thấp <i>k</i> = 3.9, khi thu nhỏ kích thước cổng, bề dày <i>d</i><sub>ox</sub> "
        "phải giảm xuống dưới 1.2 nm để duy trì điện dung cổng điều khiển. Khi đó dòng rò xuyên hầm vượt quá 100 A/cm², "
        "làm công suất tiêu tán tĩnh vượt trần nhiệt lượng 100 W/cm².<br/>"
        "• <i>Giải pháp vật liệu High-k (HfO₂):</i> Hafni dioxide có hằng số điện môi <i>k</i> = 25 (cao gấp 6.4 lần SiO₂). "
        "Điều này cho phép chế tạo lớp cách điện có bề dày vật lý thực tế dày tới 3.0 nm (chặn đứng hoàn toàn dòng xuyên hầm lượng tử) "
        "mà vẫn đạt được Độ dày oxit tương đương điện dung (EOT) cực mỏng dưới 0.8 nm.<br/>"
        "• <i>Kiến trúc 3D FinFET và GAA-FET:</i> Chuyển từ kênh dẫn phẳng sang cánh đứng (Fin) và các tấm nano xếp chồng (Gate-All-Around Nanosheet), "
        "cho phép cực cổng bao bọc toàn diện 4 mặt của kênh dẫn, kiểm soát tĩnh điện tối ưu và kéo dài Định luật Moore tới tiến trình 2 nm."
    )
    story.append(he.make_paragraph(g1_p4, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng đồ thị mô phỏng 1
    img_sim_moore = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.6_Dinh_Luat_Moore_Va_Gioi_Han_Luong_Tu.png")
    cap_sim_moore = "Hình 2.6.2: Đồ thị mô phỏng định luật Moore từ 1970 đến 2030 và điểm bẻ gãy do rào cản dòng rò xuyên hầm lượng tử."
    story.append(he.embed_figure_with_caption(img_sim_moore, cap_sim_moore, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_1 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Định luật Moore không phải là một định luật vật lý tự nhiên bất biến, mà là một lộ trình kinh tế – kỹ thuật "
        "đang tiến sát tới giới hạn lượng tử tối hậu của cấu trúc nguyên tử.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Khoảng cách giữa hai nguyên tử Silic kề nhau trong mạng tinh thể kim cương là 0.235 nm "
        "(thông số mạng tinh thể <i>a</i> = 0.543 nm). Ở tiến trình công nghệ 1 nm, chiều rộng kênh dẫn chỉ tương đương vỏn vẹn 4 đến 5 nguyên tử Silic. "
        "Độ bất định vị trí của electron theo nguyên lý Heisenberg trở nên tương đương với toàn bộ chiều dài kênh dẫn.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Khi kênh dẫn chỉ gồm vài nguyên tử, khái niệm dải năng lượng liên tục (Dải dẫn, Dải hóa trị) "
        "bị phá vỡ do hiệu ứng lượng tử hóa kích thước giam cầm. Thăng giáng ngẫu nhiên của chỉ một nguyên tử tạp chất pha tạp đơn lẻ "
        "cũng làm thay đổi điện áp ngưỡng <i>V</i><sub>th</sub> tới hơn 50%, khiến việc chế tạo hàng tỷ transistor giống hệt nhau trở nên bất khả thi.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Nhiều quan điểm cho rằng 'Định luật Moore đã chết'. "
        "Thực tế, định luật Moore hình học (thu nhỏ kích thước 2D) đã bão hòa, nhưng định luật Moore chức năng (More than Moore) "
        "vẫn đang tiếp tục phát triển mạnh mẽ thông qua công nghệ đóng gói chip đa tầng 3D (Chiplet), mạch tích hợp quang tử nano và tính toán dị thể."
    )
    story.append(he.make_paragraph(cer_1, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.6.2: Y SINH HỌC NANO & HỆ DẪN THUỐC HƯỚNG ĐÍCH
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.6.2: Y sinh học nano: Hệ dẫn thuốc hướng đích &amp; Theranostics", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g2_p1 = (
        "Y sinh học nano (Nanomedicine) là ứng dụng mang tính nhân văn sâu sắc nhất của công nghệ nano, cho phép can thiệp và sửa chữa "
        "các cấu trúc sinh học ở cấp độ phân tử và tế bào. Trong điều trị ung thư truyền thống, các loại thuốc hóa trị là những chất độc tế bào "
        "không có tính chọn lọc: chúng tiêu diệt tế bào u nhưng đồng thời tàn phá các tế bào lành phân chia nhanh (tế bào tủy xương, nang tóc, niêm mạc ruột), "
        "gây tác dụng phụ nguy hiểm.<br/>"
        "Hệ thống dẫn thuốc nano (Nanocarriers) sử dụng các hạt nano polyme phân hủy sinh học (PLGA), hạt nano lipid (LNP) hoặc hạt liposome "
        "có kích thước từ 20 nm đến 100 nm để đóng gói phân tử thuốc bên trong. Nhờ kích thước nano siêu việt và khả năng chức năng hóa bề mặt, "
        "các hạt này vận chuyển thuốc an toàn qua dòng tuần hoàn máu và giải phóng hoạt chất tập trung chính xác tại mô bệnh."
    )
    story.append(he.make_paragraph(g2_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_drug = os.path.join(kho_anh, "[Goc]_Muc_2.6_Hinh_02_Y_Sinh_Hoc_Nano_Drug_Delivery.png")
    cap_drug = "Hình 2.6.3: Ứng dụng công nghệ nano trong y sinh học — hệ thống dẫn thuốc hướng đích gắn kháng thể nhận diện tế bào đích (Slide 72)."
    story.append(he.embed_figure_with_caption(img_drug, cap_drug, kind="orig", styles=styles))

    drug_ocr_1 = "Sơ đồ hạt nano mang thuốc được gắn các phối tử (ligand) đặc hiệu trên bề mặt ngoài."
    drug_ocr_2 = "Cơ chế nhận diện sinh học: Kháng thể trên hạt nano khóa liên kết chọn lọc với các thụ thể biểu hiện quá mức trên màng tế bào u."
    drug_ocr_3 = "Xâm nhập nội bào: Quá trình nội thực bào (Endocytosis) đưa hạt nano vào bên trong tế bào ung thư."
    drug_ocr_4 = "Giải phóng thuốc có kiểm soát: Độ pH axit của lysosome phân cắt liên kết hóa học, giải phóng phân tử thuốc tiêu diệt nhân tế bào."
    drug_ocr_5 = "Bảo vệ mô lành: Hạn chế tối đa sự rò rỉ thuốc ra ngoài cơ thể trong suốt quá trình lưu thông tuần hoàn."
    story.append(he.make_paragraph(drug_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(drug_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(drug_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(drug_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(drug_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g2_p2 = (
        "<b>Hiệu ứng thấm và giữ nâng cao (EPR Effect):</b> Khối u ung thư phát triển cực nhanh đòi hỏi nguồn cung cấp oxy và dưỡng chất liên tục. "
        "Do đó, các mạch máu nuôi khối u được hình thành vội vã, tạo nên các khe hở nội mô thành mạch rất lớn (từ 100 nm đến 500 nm), "
        "đồng thời hệ thống thoát bạch huyết tại khối u bị tê liệt. Các phân tử thuốc tự do kích thước nhỏ (dưới 1 nm) dễ dàng khuếch tán ra mọi mô lành "
        "và bị thận đào thải chỉ sau vài phút. Ngược lại, hạt nano có kích thước tối ưu (cỡ 50 nm) không thể lọt qua thành mạch máu bình thường (khe hở dưới 5 nm), "
        "nhưng lại dễ dàng chui qua các khe hở thành mạch u và bị giữ lại tại đó với nồng độ cao gấp hàng chục lần so với mô khỏe mạnh."
    )
    story.append(he.make_paragraph(g2_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_korsmeyer = r"\frac{M_t}{M_\infty} = k t^n, \quad \sigma_{\mathrm{EPR}} = \frac{C_{\mathrm{tumor}}}{C_{\mathrm{normal}}} \gg 1"
    nom_korsmeyer = [
        ("Phân số khối lượng thuốc giải phóng tại thời điểm t", "<i>M</i><sub>t</sub> · <i>M</i><sub>∞</sub><sup>−1</sup>", "không thứ nguyên", "Tỷ lệ khối lượng phân tử thuốc đã khuếch tán ra ngoài môi trường sinh học"),
        ("Hằng số tốc độ giải phóng động học", "<i>k</i>", "s<sup>−<i>n</i></sup>", "Thông số phụ thuộc vào độ nhớt, hệ số khuếch tán và tương tác mạng polyme nano"),
        ("Chỉ số cơ chế khuếch tán Peppas", "<i>n</i>", "không thứ nguyên", "Xác định cơ chế giải phóng: <i>n</i> = 0.43 (khuếch tán Fick), 0.43 &lt; <i>n</i> &lt; 0.85 (dị thường)"),
        ("Hệ số tích tụ chọn lọc mô u (EPR)", "<i>σ</i><sub>EPR</sub>", "không thứ nguyên", "Tỷ số nồng độ tích tụ thuốc tại mô khối u so với mô lành xung quanh")
    ]
    story.append(he.build_target_equation_block(eq_korsmeyer, nom_korsmeyer, styles=styles))
    story.append(Spacer(1, 6))

    step2_1_text = (
        "Thiết lập phương trình vi phân khuếch tán Fick bậc hai cho hoạt chất thuốc bên trong hạt nano hình cầu bán kính <i>R</i>:"
    )
    step2_1_eq = r"\frac{\partial C(r,t)}{\partial t} = D_{\mathrm{eff}} \left( \frac{\partial^2 C}{\partial r^2} + \frac{2}{r} \frac{\partial C}{\partial r} \right)"
    story.append(he.build_intermediate_equation(step2_1_text, step2_1_eq, styles=styles, is_expanded_from_slide=True))

    step2_2_text = (
        "Giải phương trình với điều kiện biên nồng độ ban đầu đồng nhất và nồng độ bề mặt ngoài bằng 0. "
        "Ở giai đoạn đầu của quá trình giải phóng (phân số thuốc dưới 60%), nghiệm chuỗi hội tụ về phương trình Korsmeyer-Peppas:"
    )
    step2_2_eq = r"\frac{M_t}{M_\infty} = 6 \left( \frac{D_{\mathrm{eff}} t}{\pi R^2} \right)^{1/2} - 3 \frac{D_{\mathrm{eff}} t}{R^2} \approx k \cdot t^{0.43}"
    story.append(he.build_intermediate_equation(step2_1_text, step2_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g2_p4 = (
        "<b>Dải kích thước vàng và Xu hướng Theranostics tích hợp:</b><br/>"
        "• <i>Giới hạn lọc thận (kích thước dưới 10 nm):</i> Các hạt nano quá nhỏ sẽ bị lọc thải siêu tốc qua cầu thận vào nước tiểu "
        "với thời gian bán thải tuần hoàn dưới 30 phút, không kịp tích tụ vào mô u.<br/>"
        "• <i>Giới hạn thực bào gan – lách (kích thước trên 200 nm):</i> Các hạt quá lớn lập tức bị hệ lưới nội mô (đại thực bào tại gan và lách) "
        "bắt giữ và tiêu hủy trước khi đến được khối u.<br/>"
        "• <i>Dải kích thước tối ưu (30 nm đến 100 nm):</i> Cho phép hạt nano lưu thông tuần hoàn kéo dài trong máu nhiều ngày "
        "nhờ lớp phủ polyme tàng hình PEG (Polyethylene glycol).<br/>"
        "• <i>Nền tảng Theranostics:</i> Tích hợp đồng thời chức năng chẩn đoán (Therapy + Diagnostics) bằng cách bọc hạt nano oxit sắt từ tính (Fe₃O₄) "
        "cho chụp cộng hưởng từ MRI, kết hợp gắn thuốc hóa trị và thuốc phát huỳnh quang chấm lượng tử để phẫu thuật viên cắt bỏ chính xác từng tế bào u."
    )
    story.append(he.make_paragraph(g2_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_2 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Vắc xin mRNA phòng ngừa đại dịch COVID-19 (Pfizer-BioNTech, Moderna) là một sản phẩm thương mại đột phá "
        "của công nghệ nano y sinh học, không thể tồn tại nếu thiếu cấu trúc hạt nano lipid (LNP).<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Phân tử mRNA mang điện tích âm lớn và kích thước cồng kềnh, bị các enzyme ribonuclease (RNase) "
        "trong cơ thể phân hủy chỉ sau vài giây nếu tiêm trần vào máu. Hạt nano lipid LNP kích thước 80 nm bảo vệ nguyên vẹn sợi mRNA "
        "và giúp chúng dung hợp qua màng tế bào với hiệu suất chuyển nhiễm (Transfection efficiency) đạt trên 90%.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Hạt LNP chứa lipid ion hóa có thể chuyển đổi điện tích theo pH: trung hòa ở pH sinh lý 7.4 trong máu "
        "để tránh độc tính, nhưng chuyển sang tích điện dương trong môi trường axit nhẹ của endosome (pH 5.5 - 6.0), làm phá vỡ màng endosome "
        "và giải phóng mRNA trực tiếp vào tế bào chất để dịch mã thành kháng nguyên protein gai.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến là cho rằng vắc xin nano làm thay đổi hệ gen người. "
        "Về mặt sinh học phân tử, mRNA được hạt nano đưa vào chỉ nằm ở tế bào chất và bị dịch mã protein rồi tiêu hủy tự nhiên, "
        "hoàn toàn không thể đi vào nhân tế bào hay tích hợp vào DNA của con người."
    )
    story.append(he.make_paragraph(cer_2, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.6.3: NĂNG LƯỢNG SẠCH NANO & HIỆU ỨNG SINH ĐA EXCITON (MEG)
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.6.3: Năng lượng sạch nano: Pin mặt trời &amp; Hiệu ứng sinh đa exciton MEG", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g3_p1 = (
        "Năng lượng mặt trời là nguồn năng lượng tái tạo vô tận, nhưng hiệu suất của các tấm pin mặt trời Silicon đơn tinh thể truyền thống "
        "bị giới hạn nghiêm ngặt bởi <b>Giới hạn Shockley – Queisser</b> (chặn trên lý thuyết 33.7% cho pin mặt trời chuyển tiếp đơn p–n). "
        "Nguyên nhân cốt lõi của sự giới hạn này là do <b>Sự tổn thất nhiệt hóa</b> (Thermalization loss): Phổ bức xạ mặt trời chứa nhiều photon "
        "có năng lượng cao hơn năng lượng dải cấm <i>E</i><sub>g</sub> (đặc biệt là vùng ánh sáng xanh và tử ngoại). "
        "Trong vật liệu khối, mỗi photon dù có năng lượng lớn đến đâu cũng chỉ sinh ra duy nhất một cặp electron – lỗ trống (hiệu suất lượng tử nội tối đa 100%), "
        "trong khi phần năng lượng dư thừa bị lãng phí hoàn toàn dưới dạng dao động nhiệt mạng tinh thể (phát xạ phonon).<br/>"
        "Công nghệ nano đã tạo nên cuộc cách mạng với sự phát hiện ra <b>Hiệu ứng sinh đa exciton</b> (Multiple Exciton Generation — MEG) "
        "trong các chấm lượng tử nano (Quantum Dots): Một photon năng lượng cao duy nhất có thể kích thích đồng thời 2 hoặc 3 cặp electron – lỗ trống, "
        "nâng hiệu suất lượng tử nội vượt ngưỡng 100% (đạt tới 200% – 300%) và nâng trần hiệu suất lý thuyết lên 44.4%."
    )
    story.append(he.make_paragraph(g3_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_solar = os.path.join(kho_anh, "[Goc]_Muc_2.6_Hinh_03_Nang_Luong_Mat_Troi_Nano.png")
    cap_solar = "Hình 2.6.4: Ứng dụng công nghệ nano trong năng lượng mặt trời — chấm lượng tử và cấu trúc nano quang điện (Slide 72)."
    story.append(he.embed_figure_with_caption(img_solar, cap_solar, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g3_p2 = (
        "<b>Cơ chế vi mô của hiệu ứng nút thắt phonon (Phonon Bottleneck):</b> Trong chất bán dẫn khối, khoảng cách giữa các mức năng lượng "
        "trong dải dẫn là liên tục. Hạt tải điện nhiệt làm nguội cực nhanh bằng cách liên tục phát ra chuỗi các phonon âm thanh năng lượng nhỏ "
        "trong khoảng thời gian vài trăm femtogiây (10⁻¹³ s).<br/>"
        "Ngược lại, trong chấm lượng tử nano 0D (như PbSe, PbS), hiệu ứng giam cầm lượng tử mạnh biến các dải năng lượng liên tục "
        "thành các mức năng lượng gián đoạn giống hệt mức năng lượng nguyên tử. Khoảng cách giữa mức năng lượng thứ nhất và thứ hai "
        "lớn hơn nhiều so với năng lượng của một phonon đơn lẻ, tạo ra hiện tượng 'nút thắt phonon' khiến hạt tải nhiệt không thể mất năng lượng nhanh qua dao động mạng. "
        "Thay vào đó, nó tương tác tĩnh điện Coulomb cực mạnh với electron ở dải hóa trị (quá trình ion hóa va chạm ngược — Inverse Auger), "
        "truyền năng lượng dư thừa để đánh bật thêm một electron nữa lên dải dẫn trước khi năng lượng kịp tiêu tán thành nhiệt."
    )
    story.append(he.make_paragraph(g3_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_meg = r"\eta_{\mathrm{int}}(h\nu) = 1 + \eta_{\mathrm{MEG}} \left( \frac{h\nu}{E_g} - 2 \right) \quad \text{khi } h\nu \ge 2 E_g, \quad \eta_{\mathrm{SQ,max}} \uparrow 44.4\%"
    nom_meg = [
        ("Hiệu suất lượng tử nội", "<i>η</i><sub>int</sub>", "%", "Số cặp exciton (electron – lỗ trống) sinh ra trên một photon bị hấp thụ"),
        ("Hiệu suất kích hoạt gia tăng MEG", "<i>η</i><sub>MEG</sub>", "% trên <i>E</i><sub>g</sub>", "Độ dốc phát sinh hạt tải phụ thuộc vào tương tác Coulomb giam cầm"),
        ("Ngưỡng năng lượng kích hoạt MEG", "2 <i>E</i><sub>g</sub>", "eV", "Mức năng lượng photon tối thiểu theo định luật bảo toàn năng lượng để sinh 2 exciton"),
        ("Hiệu suất Shockley – Queisser cực đại", "44.4%", "%", "Trần hiệu suất nhiệt động học cho pin mặt trời tiếp giáp đơn có hiệu ứng sinh đa exciton")
    ]
    story.append(he.build_target_equation_block(eq_meg, nom_meg, styles=styles))
    story.append(Spacer(1, 6))

    step3_1_text = (
        "Thiết lập điều kiện bảo toàn năng lượng và động lượng trong quá trình ion hóa va chạm ngược (Impact Ionization) bên trong chấm lượng tử. "
        "Do không có sự bảo toàn giả động lượng tinh thể trong cấu trúc giam cầm 0D, ngưỡng năng lượng kích hoạt đạt giới hạn tối thiểu:"
    )
    step3_1_eq = r"h\nu_{\mathrm{threshold}} = 2 E_g \quad (\text{so với ngưỡng } 3 E_g \text{ trong bán dẫn khối do ràng buộc bảo toàn động lượng})"
    story.append(he.build_intermediate_equation(step3_1_text, step3_1_eq, styles=styles, is_expanded_from_slide=True))

    step3_2_text = (
        "Tốc độ sinh đa hạt tải <i>Γ</i><sub>MEG</sub> cạnh tranh trực tiếp với tốc độ làm nguội nhiệt qua phonon <i>Γ</i><sub>cool</sub>. "
        "Hiệu suất lượng tử nội biểu diễn qua tỷ số tốc độ chuyển dời lượng tử:"
    )
    step3_2_eq = r"\eta_{\mathrm{int}} = 1 + \frac{\Gamma_{\mathrm{MEG}}}{\Gamma_{\mathrm{MEG}} + \Gamma_{\mathrm{cool}}} \approx 1 + \frac{\tau_{\mathrm{cool}}}{\tau_{\mathrm{MEG}}}"
    story.append(he.build_intermediate_equation(step3_1_text, step3_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g3_p4 = (
        "<b>Khảo sát hiệu suất lượng tử nội theo tỷ số năng lượng photon:</b><br/>"
        "• Khi <i>hν</i> nhỏ hơn 2 <i>E</i><sub>g</sub>: <i>η</i><sub>int</sub> = 100% (ứng xử giống hệt pin mặt trời truyền thống).<br/>"
        "• Khi <i>hν</i> đạt từ 2 <i>E</i><sub>g</sub> đến 3 <i>E</i><sub>g</sub>: Hiệu ứng MEG kích hoạt, <i>η</i><sub>int</sub> tăng tuyến tính vượt 100% lên tới 160% – 180%.<br/>"
        "• Khi <i>hν</i> lớn hơn 4 <i>E</i><sub>g</sub> (vùng tia tử ngoại sâu UV): Trung bình 1 photon tới kích thích tạo ra tới gần 3 electron dẫn (<i>η</i><sub>int</sub> xấp xỉ 280%).<br/>"
        "• Ưu thế chế tạo: Pin mặt trời chấm lượng tử có thể gia công bằng công nghệ in dung dịch (Roll-to-roll printing) ở nhiệt độ phòng, "
        "giá thành chỉ bằng một phần ba so với tinh luyện thỏi Silic đơn tinh thể ở 1400 °C."
    )
    story.append(he.make_paragraph(g3_p4, styles["Body"]))
    story.append(Spacer(1, 4))

    img_sim_meg = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.6_Hieu_Ung_Sinh_Da_Exciton_MEG_Pin_Mat_Troi.png")
    cap_sim_meg = "Hình 2.6.5: Đồ thị hiệu suất lượng tử nội η_int vượt 100% nhờ hiệu ứng sinh đa exciton (MEG) trong chấm lượng tử nano PbSe/PbS."
    story.append(he.embed_figure_with_caption(img_sim_meg, cap_sim_meg, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_3 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Hiện tượng sinh đa exciton MEG trong chấm lượng tử không hề vi phạm Định luật bảo toàn năng lượng, "
        "mặc dù hiệu suất lượng tử nội vượt qua mốc 100%.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Để sinh ra 2 exciton cần tối thiểu năng lượng 2 <i>E</i><sub>g</sub>. "
        "Một photon ánh sáng xanh tím mang năng lượng <i>hν</i> = 3.1 eV khi chiếu vào chấm lượng tử PbSe có dải cấm <i>E</i><sub>g</sub> = 0.8 eV "
        "sẽ có tỷ số năng lượng là 3.88 lần <i>E</i><sub>g</sub>. Năng lượng của photon đơn lẻ này hoàn toàn thừa đủ để cung cấp năng lượng tạo ra 3 cặp hạt tải (3 × 0.8 = 2.4 eV &lt; 3.1 eV).<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> 'Hiệu suất lượng tử' là thước đo số lượng hạt (số electron trên một photon), chứ không phải tỷ số năng lượng. "
        "Hiệu suất chuyển đổi năng lượng toàn phần vẫn tuân thủ định luật nhiệt động học 2 và luôn nhỏ hơn 100%. "
        "MEG đơn giản là thu hồi lại phần năng lượng photon dư thừa vốn bị lãng phí thành nhiệt trong pin mặt trời cổ điển.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Nút thắt lớn nhất của pin mặt trời chấm lượng tử hiện nay là tái hợp Auger: "
        "Khi 2 exciton cùng tồn tại trong một chấm lượng tử nhỏ, chúng có xu hướng triệt tiêu lẫn nhau qua tái hợp không bức xạ trong vài chục picosecond. "
        "Kỹ thuật nano hiện đại phải thiết kế cấu trúc vỏ bọc dị thể (Core/Shell) để phân tách nhanh chóng electron và lỗ trống ra hai vùng không gian khác nhau."
    )
    story.append(he.make_paragraph(cer_3, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.6.4: VẬT LIỆU NANO COMPOSITE & MẠCH QUANG TỬ TÍCH HỢP
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.6.4: Vật liệu nano composite siêu bền &amp; Mạch tích hợp quang tử nano", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g4_p1 = (
        "<b>Vật liệu Nano Composite siêu bền:</b> Là sự kết hợp giữa nền polyme, gốm hoặc kim loại với các hạt pha gia cường quy mô nano "
        "(ống nano carbon CNT, graphene, thanh nano oxit kim loại). Ống nano carbon đơn vách (SWCNT) sở hữu liên kết cộng hóa trị carbon – carbon lai hóa <i>sp</i>² "
        "bền vững nhất trong tự nhiên, mang lại module Young đàn hồi lên tới 1.0 TPa (1 000 GPa, gấp 5 lần thép tốt nhất) "
        "và độ bền kéo đứt vượt quá 50 GPa, trong khi khối lượng riêng chỉ bằng một phần sáu của thép.<br/>"
        "<b>Mạch tích hợp quang tử nano (Silicon Photonics):</b> Thay thế dây dẫn kim loại truyền thống bằng các ống dẫn sóng quang học silicon cỡ nano "
        "(kích thước tiết diện 220 nm × 500 nm). Việc truyền dẫn tín hiệu bằng các xung ánh sáng photon thay cho dòng electron cho phép triệt tiêu hoàn toàn "
        "tổn hao nhiệt điện trở Joule, tăng băng thông truyền dẫn dữ liệu lên hàng Terabit trên giây và giảm tiêu thụ năng lượng tới 90% trong các trung tâm dữ liệu AI."
    )
    story.append(he.make_paragraph(g4_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_comp = os.path.join(kho_anh, "[Goc]_Muc_2.6_Hinh_04_Vat_Lieu_Composite_Nano.png")
    cap_comp = "Hình 2.6.6: Cấu trúc vật liệu nano composite siêu bền — mạng lưới ống nano carbon gia cường cơ tính vượt bậc (Slide 72)."
    story.append(he.embed_figure_with_caption(img_comp, cap_comp, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_chip = os.path.join(kho_anh, "[Goc]_Muc_2.6_Hinh_05_Chip_Ban_Dan_Tich_Hop_Nano.png")
    cap_chip = "Hình 2.6.7: Chip bán dẫn và mạch tích hợp quang tử quy mô nano — nền tảng vi xử lý tương lai (Slide 72)."
    story.append(he.embed_figure_with_caption(img_chip, cap_chip, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g4_p2 = (
        "<b>Cơ chế truyền ứng suất giao diện (Interfacial Stress Transfer):</b> Trong composite truyền thống (sợi thủy tinh, sợi carbon vĩ mô), "
        "diện tích tiếp xúc giữa sợi và nhựa rất nhỏ, các vết nứt vi mô dễ dàng lan truyền dọc theo bề mặt ranh giới làm vật liệu bị tách lớp gãy vỡ. "
        "Ngược lại, 1 gam ống nano carbon CNT có tổng diện tích bề mặt tiếp xúc lên tới 1 300 m² (tương đương diện tích của hai sân bóng đá). "
        "Khi pha vào nhựa chỉ vỏn vẹn 1% thể tích CNT, mạng lưới hàng nghìn tỷ ống nano đan xen chằng chịt khóa chặt các chuỗi đại phân tử polyme. "
        "Mỗi khi một vết nứt tế vi xuất hiện, nó bị các sợi CNT bắc cầu (Nanotube bridging) ghim chặt lại, tiêu tán năng lượng phá hủy "
        "và ngăn chặn hoàn toàn sự lan truyền nứt vỡ."
    )
    story.append(he.make_paragraph(g4_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_composite = r"E_c = V_f E_f + (1 - V_f) E_m, \quad \sigma_{\mathrm{CNT}} > 50\ \mathrm{GPa}, \quad E_{\mathrm{CNT}} \approx 1.0\ \mathrm{TPa}"
    nom_composite = [
        ("Module Young của vật liệu composite hoàn chỉnh", "<i>E</i><sub>c</sub>", "GPa", "Độ cứng đàn hồi chống biến dạng kéo dọc của vật liệu tổ hợp"),
        ("Phân số thể tích pha gia cường nano", "<i>V</i><sub>f</sub>", "không thứ nguyên", "Tỷ lệ thể tích của ống nano carbon hoặc hạt nano trong khối vật liệu"),
        ("Module Young của pha gia cường nano CNT", "<i>E</i><sub>f</sub>", "GPa", "Độ cứng đàn hồi cực đại của ống nano carbon đơn vách: xấp xỉ 1000 GPa"),
        ("Module Young của pha nền polyme", "<i>E</i><sub>m</sub>", "GPa", "Độ cứng của chất dẻo nền (Epoxy): dao động từ 3 GPa đến 5 GPa"),
        ("Độ bền kéo đứt tới hạn của CNT", "<i>σ</i><sub>CNT</sub>", "GPa", "Ứng suất kéo phá hủy liên kết cộng hóa trị carbon sp²: lớn hơn 50 GPa")
    ]
    story.append(he.build_target_equation_block(eq_composite, nom_composite, styles=styles))
    story.append(Spacer(1, 6))

    step4_1_text = (
        "Xét cân bằng lực trên một sợi nano có bán kính <i>r</i> và chiều dài <i>L</i> nhúng trong nền polyme dưới ứng suất trượt giao diện <i>τ</i><sub>i</sub>:"
    )
    step4_1_eq = r"\pi r^2 \sigma_f = 2\pi r \int_0^{L/2} \tau_i(z) dz \implies L_c = \frac{r \sigma_f}{\tau_i}"
    story.append(he.build_intermediate_equation(step4_1_text, step4_1_eq, styles=styles, is_expanded_from_slide=True))

    step4_2_text = (
        "Khi chiều dài sợi nano <i>L</i> vượt quá chiều dài tới hạn <i>L</i><sub>c</sub>, ứng suất kéo được truyền hoàn toàn vào sợi nano, "
        "cho phép khai thác tối đa độ bền kéo 50 GPa của ống nano carbon để tăng cường cơ tính của vật liệu tổ hợp:"
    )
    step4_2_eq = r"\sigma_c = V_f \sigma_f \left( 1 - \frac{L_c}{2L} \right) + (1 - V_f) \sigma_m^* \approx V_f \sigma_f + (1 - V_f) \sigma_m^*"
    story.append(he.build_intermediate_equation(step4_1_text, step4_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g4_p4 = (
        "<b>Thách thức phân tán và Ứng dụng công nghiệp quốc phòng:</b><br/>"
        "• <i>Vấn đề vón cục nano (Agglomeration):</i> Do diện tích bề mặt riêng khổng lồ, năng lượng tự do bề mặt cao khiến các ống CNT "
        "có xu hướng hút nhau cực mạnh bởi lực Van der Waals, vón cục thành từng bó sợi lớn. Các bó vón cục này đóng vai trò như các khuyết tật tập trung ứng suất, "
        "làm giảm độ bền thay vì gia cường. Giải pháp bắt buộc là biến tính hóa học bề mặt (cắt gọt bằng axit để gắn nhóm chức carboxyl −COOH) "
        "kết hợp siêu âm công suất cao để phân tán đơn lập từng sợi.<br/>"
        "• <i>Ứng dụng hàng không vũ trụ và quân sự:</i> Thân vỏ máy bay tàng hình chế tạo từ composite CNT vừa siêu nhẹ (tiết kiệm 30% nhiên liệu), "
        "chống chịu va đập đạn pháo và sét đánh trực tiếp (nhờ độ dẫn điện cao), vừa hấp thụ sóng radar trinh sát."
    )
    story.append(he.make_paragraph(g4_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_4 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Ống dẫn sóng silicon nano trong mạch tích hợp quang tử có thể giam cầm và uốn cong ánh sáng ở góc cua bán kính siêu nhỏ (dưới 5 μm), "
        "điều mà sợi quang thủy tinh thông thường tuyệt đối không thể làm được.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Sợi quang học viễn thông thủy tinh silica có độ chênh chiết suất lõi – vỏ rất nhỏ (<i>Δn</i> ≈ 0.005), "
        "khiến bán kính uốn cong tối thiểu phải lớn hơn 3 cm để tránh rò rỉ bức xạ ánh sáng ra ngoài. "
        "Ống dẫn sóng silicon nano có chiết suất lõi cực cao <i>n</i><sub>Si</sub> = 3.45 đặt trên nền oxit <i>n</i><sub>SiO₂</sub> = 1.45, "
        "tạo ra độ tương phản chiết suất khổng lồ <i>Δn</i> = 2.0.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Góc phản xạ toàn phần tới hạn tính theo định luật Snell: <i>θ</i><sub>c</sub> = arcsin(0.420) ≈ 24.8° (lấy tỷ số chiết suất 1.45 chia cho 3.45). "
        "Độ chênh chiết suất cực lớn tạo ra rào thế giam cầm trường quang học cực mạnh, giam giữ toàn bộ trường điện từ bên trong lõi silicon 220 nm "
        "và cho phép bẻ cua ánh sáng 90° với bán kính chỉ 2 μm mà không suy hao tín hiệu.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù kinh điển là nghĩ rằng quang tử sẽ thay thế hoàn toàn điện tử trong mọi tác vụ. "
        "Thực tế, photon không có tương tác trực tiếp với nhau (không có điện tích), nên việc chế tạo bộ nhớ logic quang tử (Optical RAM) "
        "cực kỳ khó khăn và cồng kềnh. Xu hướng tối ưu là vi mạch lai Quang – Điện (Optoelectronic Co-packaged Optics): "
        "Dùng điện tử để tính toán logic và dùng quang tử nano để truyền dẫn dữ liệu tốc độ cao."
    )
    story.append(he.make_paragraph(cer_4, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.6.5: TẦM NHÌN MARKUS ANTONIETTI & MÔI TRƯỜNG TƯƠNG LAI
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.6.5: Tầm nhìn GS. Markus Antonietti &amp; Định hướng tương lai của công nghệ nano", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g5_p1 = (
        "Trong khi phần lớn các nghiên cứu công nghệ nano tập trung vào vi điện tử thương mại, <b>Giáo sư Markus Antonietti</b> "
        "(Giám đốc Viện Chất keo và Bề mặt – Viện Sinh học Tiến hóa Max Planck, CHLB Đức) đã định hình một tầm nhìn mang tính bước ngoặt sinh thái: "
        "<i>'Tiềm năng lớn nhất của công nghệ nano để cải thiện tình trạng của thế giới là thanh lọc không khí và nguồn nước.'</i> (Slide 73).<br/>"
        "Biến đổi khí hậu, ô nhiễm nguồn nước ngầm bởi hóa chất vĩnh cửu PFAS, dư lượng thuốc kháng sinh, vi nhựa và khí thải nhà kính CO₂ "
        "là những thách thức đe dọa trực tiếp sự tồn vong của nhân loại. Công nghệ nano cung cấp các giải pháp hóa học xanh và xúc tác nano "
        "với diện tích bề mặt riêng khổng lồ, cho phép quang phân hủy các chất độc hại thành các chất vô hại dưới ánh sáng mặt trời tự nhiên."
    )
    story.append(he.make_paragraph(g5_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_antonietti = os.path.join(kho_anh, "[Goc]_Muc_2.6_Hinh_06_GS_Markus_Antonietti_Max_Planck.png")
    cap_antonietti = "Hình 2.6.8: GS. Markus Antonietti (Viện Max Planck) — định hình sứ mệnh công nghệ nano cứu rỗi sinh thái toàn cầu (Slide 73)."
    story.append(he.embed_figure_with_caption(img_antonietti, cap_antonietti, kind="orig", styles=styles))

    antonietti_ocr_1 = "Chân dung GS. Markus Antonietti, nhà khoa học hóa học vật liệu nano hàng đầu thế giới tại Viện Max Planck."
    antonietti_ocr_2 = "Tầm nhìn cốt lõi: Ứng dụng vật liệu keo và bề mặt nano để giải quyết các cuộc khủng hoảng sinh thái toàn cầu."
    antonietti_ocr_3 = "Vật liệu đột phá: Tiên phong phát minh chất xúc tác quang học phi kim Carbon Nitride polymer (g-C3N4)."
    antonietti_ocr_4 = "Cơ chế: Sử dụng ánh sáng mặt trời khả kiến để tách hydro từ nước và chuyển hóa CO2 thành nhiên liệu xanh."
    antonietti_ocr_5 = "Sứ mệnh nhân văn: Mang lại nguồn nước sạch và không khí trong lành cho hàng tỷ người dân ở các nước đang phát triển."
    story.append(he.make_paragraph(antonietti_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(antonietti_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(antonietti_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(antonietti_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(antonietti_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g5_p2 = (
        "<b>Trực giác vi mô về sự bùng nổ diện tích bề mặt quang xúc tác:</b> Một viên đá sỏi TiO₂ kích thước 1 cm có diện tích bề mặt vỏn vẹn vài cm², "
        "khi thả vào cốc nước ô nhiễm hầu như không có bất kỳ tác dụng lọc nào. Tuy nhiên, nếu nghiền viên đá đó thành các hạt nano kích thước 10 nm, "
        "tổng diện tích bề mặt của cùng khối lượng vật liệu đó tăng vọt lên tới hơn 150 m² (tương đương mặt sàn một ngôi nhà rộng). "
        "Hàng triệu tỷ tâm hoạt tính trên bề mặt hạt nano được phơi bày ra dung dịch. Dưới tác dụng của ánh sáng, các electron và lỗ trống quang sinh "
        "dễ dàng di chuyển ra bề mặt mà không bị tái hợp, phản ứng tức thì với các phân tử nước để tạo thành các gốc tự do oxy hóa cực mạnh (Hydroxyl *OH), "
        "tấn công bẻ gãy hoàn toàn các vòng benzen của chất nhuộm công nghiệp, thuốc trừ sâu và vi khuẩn chỉ trong vài phút."
    )
    story.append(he.make_paragraph(g5_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_langmuir = r"r = -\frac{dC}{dt} = \frac{k K C}{1 + K C} \approx k_{\mathrm{app}} C \implies \ln\left(\frac{C_0}{C(t)}\right) = k_{\mathrm{app}} t, \quad k_{\mathrm{app}} \propto S_{\mathrm{BET}}"
    nom_langmuir = [
        ("Tốc độ phản ứng phân hủy quang xúc tác", "<i>r</i>", "mol·L⁻¹·s⁻¹", "Tốc độ làm giảm nồng độ chất ô nhiễm hữu cơ trong dung dịch"),
        ("Nồng độ chất ô nhiễm tại thời điểm t", "<i>C</i>(<i>t</i>)", "mol/L", "Hàm lượng hoạt chất độc hại còn tồn dư trong nguồn nước sau thời gian xử lý"),
        ("Hằng số tốc độ phản ứng biểu kiến", "<i>k</i><sub>app</sub>", "phút<sup>−1</sup>", "Hệ số tỷ lệ tốc độ phân hủy bậc một: tỷ lệ thuận trực tiếp với diện tích bề mặt nano"),
        ("Diện tích bề mặt riêng đo theo chuẩn BET", "<i>S</i><sub>BET</sub>", "m²·g⁻¹", "Tổng diện tích bề mặt tiếp xúc hiệu dụng của hạt nano trên một đơn vị khối lượng"),
        ("Hằng số cân bằng hấp phụ Langmuir", "<i>K</i>", "L·mol⁻¹", "Ái lực liên kết hấp phụ giữa phân tử chất ô nhiễm và tâm hoạt tính bề mặt nano")
    ]
    story.append(he.build_target_equation_block(eq_langmuir, nom_langmuir, styles=styles))
    story.append(Spacer(1, 6))

    step5_1_text = (
        "Thiết lập cơ chế động học phản ứng dị thể bề mặt theo mô hình Langmuir – Hinshelwood. "
        "Tốc độ phản ứng tỷ lệ thuận với độ che phủ bề mặt <i>θ</i><sub>cov</sub> = <i>K</i>·<i>C</i> · (1 + <i>K</i>·<i>C</i>)<sup>−1</sup>:"
    )
    step5_1_eq = r"r = k \cdot \theta_{\mathrm{cov}} = \frac{k K C}{1 + K C}"
    story.append(he.build_intermediate_equation(step5_1_text, step5_1_eq, styles=styles, is_expanded_from_slide=True))

    step5_2_text = (
        "Ở nồng độ chất ô nhiễm thấp thường gặp trong nguồn nước tự nhiên (<i>C</i> ≪ 1 mM, tức <i>K</i>·<i>C</i> ≪ 1), mẫu số xấp xỉ bằng 1. "
        "Phương trình chuyển thành động học giả bậc một, tích phân hai vế thu được hàm suy giảm nồng độ theo hàm mũ:"
    )
    step5_2_eq = r"-\frac{dC}{dt} \approx (k K) C = k_{\mathrm{app}} C \implies C(t) = C_0 \exp(- k_{\mathrm{app}} t)"
    story.append(he.build_intermediate_equation(step5_1_text, step5_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g5_p4 = (
        "<b>Động học quang xúc tác và Vật liệu Carbon Nitride đột phá của Antonietti:</b><br/>"
        "• <i>Hạt nano TiO₂ kích thước 10 nm:</i> Diện tích bề mặt riêng đạt <i>S</i><sub>BET</sub> ≈ 150 m²·g⁻¹. Hằng số tốc độ <i>k</i><sub>app</sub> = 0.065 phút⁻¹, "
        "phân hủy trên 86% chất ô nhiễm sau 30 phút và trên 98% sau 60 phút chiếu xạ UV.<br/>"
        "• <i>Vật liệu micro thô (1 μm):</i> Diện tích bề mặt chỉ đạt 5 m²·g⁻¹, hằng số <i>k</i><sub>app</sub> = 0.005 phút⁻¹ (chậm hơn 13 lần), "
        "sau 60 phút chỉ phân hủy được dưới 25% chất ô nhiễm.<br/>"
        "• <i>Đột phá Carbon Nitride (g-C₃N₄) của Markus Antonietti:</i> Xúc tác nano hữu cơ phi kim có dải cấm <i>E</i><sub>g</sub> = 2.7 eV, "
        "hấp thụ hoàn hảo ánh sáng khả kiến mặt trời (bước sóng dưới 460 nm, chiếm 45% năng lượng mặt trời, so với chỉ 4% của tia UV). "
        "Vật liệu này cho phép lọc nước ô nhiễm và quang phân tách nước sinh khí Hydro sạch hoàn toàn thụ động mà không cần dùng điện lưới."
    )
    story.append(he.make_paragraph(g5_p4, styles["Body"]))
    story.append(Spacer(1, 4))

    img_sim_photo = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.6_Hieu_Suat_Quang_Xuc_Tac_Nano_Moi_Truong.png")
    cap_sim_photo = "Hình 2.6.9: Đồ thị động học phân hủy quang xúc tác theo mô hình Langmuir – Hinshelwood — so sánh hạt nano và vật liệu vi mô."
    story.append(he.embed_figure_with_caption(img_sim_photo, cap_sim_photo, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_5 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Tiềm năng lớn nhất của công nghệ nano trong thế kỷ 21 không phải là chế tạo các siêu máy tính nhanh hơn, "
        "mà là giải quyết cuộc khủng hoảng sinh thái toàn cầu về nước sạch và không khí (theo đúng tầm nhìn của Markus Antonietti).<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Hiện có hơn 2 tỷ người trên Trái Đất thiếu nước uống an toàn. Các chất ô nhiễm vi lượng thế hệ mới "
        "(hóa chất vĩnh cửu PFAS, thuốc kháng sinh, vi nhựa) có nồng độ cực thấp (cỡ ppb đến ppm) nhưng gây ung thư và phá hủy nội tiết, "
        "hoàn toàn không thể xử lý bằng các bể lắng lọc cát hay khử trùng clo truyền thống. "
        "Màng lọc nano thẩm thấu ngược (TFC-RO) có kích thước lỗ xốp dưới 0.5 nm kết hợp xúc tác nano có thể loại bỏ 99.9% các chất độc này.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Ô nhiễm môi trường là bài toán tương tác ở cấp độ phân tử. Chỉ có các cấu trúc vật liệu nano "
        "với mật độ tâm hoạt tính nguyên tử bề mặt khổng lồ và khả năng tương tác chọn lọc ở quy mô nanomet mới có thể bẫy bắt và phân hủy triệt để "
        "các phân tử độc hại ở nồng độ cực loãng với chi phí năng lượng thấp nhất.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù về an toàn độc tính sinh thái (Nanotoxicology): "
        "Các hạt nano xúc tác sau khi xử lý nước nếu bị rò rỉ ra môi trường tự nhiên có thể xâm nhập vào chuỗi thức ăn sinh học. "
        "Vì vậy, xu hướng tương lai bắt buộc phải cố định hóa các hạt nano lên màng nền xốp (Immobilized photocatalytic membranes) "
        "hoặc sử dụng vật liệu xúc tác nano từ tính để thu hồi 100% hạt nano sau phản ứng bằng nam châm vĩnh cửu."
    )
    story.append(he.make_paragraph(cer_5, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # TỔNG KẾT MỤC 2.6 & KẾT THÚC CHƯƠNG 2
    # =========================================================================
    summary_text = (
        "<b>Tổng kết Mục 2.6 &amp; Bế mạc Toàn văn Chương 2:</b> Khép lại Chương 2 'Bản chất lượng tử của thế giới nano', "
        "chúng ta đã đi trọn một hành trình nhận thức sâu sắc từ nguyên lý đầu: Bắt đầu từ lịch sử hình thành và hiệu ứng diện tích bề mặt vượt trội (Mục 2.1); "
        "qua bản chất sóng hạt của ánh sáng và electron trong hiệu ứng quang điện, tán xạ Compton và nhiễu xạ Davisson – Germer (Mục 2.2); "
        "sự hình thành bó sóng, vận tốc nhóm và hệ thức bất định Heisenberg (Mục 2.3); cơ học lượng tử nguyên tử Hydro, các orbital s, p, d "
        "và phổ dao động – quay phân tử (Mục 2.4); bản chất vướng víu lượng tử, nghịch lý EPR, định lý Bell và các giải Nobel 2022 (Mục 2.5); "
        "cho đến tiềm năng tương lai vô hạn của công nghệ nano trong vi điện tử, y sinh học, năng lượng sạch và môi trường sinh thái (Mục 2.6). "
        "Thế giới nano chính là đấu trường kỳ diệu nơi cơ học lượng tử không còn là lý thuyết trừu tượng trên giấy, "
        "mà trở thành công cụ kỹ thuật thực tế xây dựng nên tương lai của nền văn minh nhân loại."
    )
    story.append(he.make_paragraph(summary_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # Xây dựng tài liệu PDF
    print("Đang tiến hành build PDF Mục 2.6 với BookmarkDocTemplate...")
    doc.build(story)
    print(f"Hoàn tất biên dịch PDF Mục 2.6: {target_pdf}")
    print(f"Kích thước tệp: {os.path.getsize(target_pdf)/1024:.1f} KB")

if __name__ == "__main__":
    build_pdf()

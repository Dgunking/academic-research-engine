# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Chương 2: Bản chất lượng tử của thế giới nano
Mục 2.5: Bản chất và công nghệ nano lượng tử (Vướng víu, EPR, Bell, Nobel 2022)
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
    target_pdf = os.path.join(bai_giang, "Chuyen_Khao_Nano_Muc_2.5.pdf")

    print(f"Bắt đầu biên dịch chuyên khảo Mục 2.5: {target_pdf}")

    # 2. Khởi tạo Styles và Document Template
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(target_pdf)
    story = []

    # =========================================================================
    # TIÊU ĐỀ ĐẦU CHUYÊN KHẢO (H1)
    # =========================================================================
    title_main = (
        "CHƯƠNG 2: BẢN CHẤT LƯỢNG TỬ CỦA THẾ GIỚI NANO<br/>"
        "MỤC 2.5: BẢN CHẤT VÀ CÔNG NGHỆ NANO LƯỢNG TỬ"
    )
    story.append(he.make_paragraph(title_main, styles["H1"]))
    story.append(Spacer(1, 4))

    meta_info = (
        "<b>Hệ Thống Chuyên Khảo Giảng Dạy &amp; Nghiên Cứu Vật Lý Nano — ĐHBK Hà Nội</b><br/>"
        "<i>Chủ thể nghiên cứu:</i> Bùi Trung Dũng — Khoa Vật lý Kỹ thuật, Trường Đại học Bách khoa Hà Nội (HUST)<br/>"
        "<i>Tài liệu nguồn kép:</i> Bài giảng 'Bài 2-Quantum nature.pdf' (Slide 54–70), Bộ môn Vật liệu Điện tử — HUST; "
        "kết hợp các chuyên khảo quốc tế đỉnh cao: Nielsen &amp; Chuang (<i>Quantum Computation and Quantum Information</i>), "
        "John Bell (<i>Speakable and Unspeakable in Quantum Mechanics</i>) và Hồ sơ Khoa học Giải Nobel Vật lý 2022."
    )
    story.append(he.make_paragraph(meta_info, styles["Body"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=he.COLOR_PRIMARY, spaceBefore=4, spaceAfter=10))

    # =========================================================================
    # LỜI NÓI ĐẦU ĐỊNH VỊ HỌC THUẬT & TỔNG QUAN
    # =========================================================================
    overview_text = (
        "<b>Lời nói đầu định vị học thuật:</b> Khoa học nano lượng tử (Quantum Nanoscience) là lĩnh vực nghiên cứu "
        "mũi nhọn nằm tại giao điểm giữa khoa học nano và vật lý lượng tử hiện đại. Mục tiêu cốt lõi của lĩnh vực này là "
        "khai thác các hiện tượng thuần túy lượng tử — đặc biệt là tính kết hợp lượng tử (Coherence), sự chồng chất lượng tử "
        "(Superposition), và hiện tượng vướng víu lượng tử (Entanglement) — để thiết kế và chế tạo các linh kiện, mạch tích hợp "
        "và vật liệu quy mô nano với những chức năng vượt xa giới hạn cổ điển. Từ cuộc tranh luận lịch sử thế kỷ giữa Einstein và "
        "Niels Bohr xoay quanh Nghịch lý EPR (1935), qua bước ngoặt định lượng của Định lý Bell (1964), đến chuỗi thí nghiệm "
        "thực nghiệm đột phá đoạt giải Nobel Vật lý 2022 của John Clauser, Alain Aspect và Anton Zeilinger: bản chất lượng tử đã "
        "chuyển hóa từ một câu hỏi triết học thuần túy thành nền tảng công nghệ thực tiễn của Cuộc cách mạng lượng tử lần thứ hai "
        "(The Second Quantum Revolution). Chuyên khảo Mục 2.5 triển khai trọn vẹn 5 Luận điểm Vi mô (MPT) theo chuẩn mực sư phạm "
        "5 giai đoạn lũy tiến, bám sát từng slide bài giảng và minh họa bằng đồ thị giải tích kỹ thuật chuẩn MATLAB R2014b+."
    )
    story.append(he.make_paragraph(overview_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # =========================================================================
    # LUẬN ĐIỂM 2.5.1: KHOA HỌC NANO LƯỢNG TỬ & ĐỘ KẾT HỢP LƯỢNG TỬ
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.5.1: Khoa học nano lượng tử &amp; Khái niệm Độ kết hợp lượng tử (Coherence)", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g1_p1 = (
        "Khoa học nano lượng tử định nghĩa thế giới vi mô không phải bằng cách thu nhỏ cơ học vĩ mô, mà bằng cách tiếp cận "
        "vật chất như các hàm sóng lượng tử có thể kiểm soát được. Mọi vi hạt (electron, lỗ trống, photon, ion) đều mang bản chất "
        "lưỡng tính sóng – hạt. Khái niệm trung tâm của lĩnh vực này là <b>Độ kết hợp lượng tử</b> (Quantum Coherence). "
        "Độ kết hợp lượng tử đề cập đến khả năng của một hệ lượng tử duy trì được mối quan hệ pha xác định giữa các trạng thái sóng "
        "thành phần trong sự chồng chất và vướng víu khi đối mặt với các tương tác nhiệt động học từ môi trường xung quanh."
    )
    story.append(he.make_paragraph(g1_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc 1 & 2
    img_nano_q = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_01_Khoa_Hoc_Nano_Luong_Tu.png")
    cap_nano_q = "Hình 2.5.1: Sơ đồ Khoa học nano lượng tử — lĩnh vực giao thoa giữa khoa học nano và vật lý lượng tử (Slide 56)."
    story.append(he.embed_figure_with_caption(img_nano_q, cap_nano_q, kind="orig", styles=styles))

    nano_q_ocr_1 = "Trình bày cấu trúc giao thoa liên ngành giữa vật lý lượng tử cơ bản và công nghệ chế tạo nano thực nghiệm."
    nano_q_ocr_2 = "Các khái niệm nền tảng: Chồng chất lượng tử, vướng víu lượng tử, độ kết hợp pha và tính không địa phương."
    nano_q_ocr_3 = "Cơ chế ứng dụng: Điều khiển hàm sóng vi hạt trong các cấu trúc nano giam cầm (chấm lượng tử, dây nano, màng mỏng)."
    nano_q_ocr_4 = "Hạ tầng kỹ thuật: Chế tạo vật liệu nano có trật tự nguyên tử chính xác cao để bảo vệ trạng thái lượng tử."
    nano_q_ocr_5 = "Định hướng phát triển: Thiết kế các thiết bị quy mô nano mang chức năng lượng tử hoàn toàn mới."
    story.append(he.make_paragraph(nano_q_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(nano_q_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(nano_q_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(nano_q_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(nano_q_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    img_coherence = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_02_Do_Ket_Hop_Luong_Tu_Coherence.png")
    cap_coherence = "Hình 2.5.2: Khái niệm Độ kết hợp lượng tử (Quantum Coherence) — bảo toàn pha sóng trước các nhiễu loạn nhiệt (Slide 57)."
    story.append(he.embed_figure_with_caption(img_coherence, cap_coherence, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối thiểu & Trực giác vi mô
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g1_p2 = (
        "<b>Trực giác vi mô về sự mất kết hợp (Decoherence):</b> Hãy tưởng tượng một con quay lượng tử (Qubit) đang quay "
        "ở trạng thái chồng chất hoàn hảo giữa hướng lên và hướng xuống. Trong chân không tuyệt đối ở 0 K, con quay này sẽ giữ "
        "pha quay vĩnh cửu. Tuy nhiên, trong một tinh thể bán dẫn thực tế ở nhiệt độ phòng (300 K), hàng tỷ nguyên tử xung quanh "
        "không ngừng dao động nhiệt (sóng âm thanh mạng tinh thể — Phonon). Mỗi khi một phonon va chạm tán xạ với electron, "
        "nó làm dịch chuyển một lượng pha ngẫu nhiên không thể đảo ngược. Quá trình tích lũy các va chạm vi mô này dẫn tới "
        "<b>Sự giải kết hợp lượng tử</b> (Decoherence), làm suy thoái hàm sóng lượng tử thuần khiết thành một tập hợp xác suất "
        "cổ điển hỗn loạn chỉ sau vài phần nghìn tỷ giây (picosecond)."
    )
    story.append(he.make_paragraph(g1_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 3: Trụ cột toán học & Dẫn xuất từng bước
    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_coherence = r"\rho(t) = \begin{pmatrix} \rho_{00} & \rho_{01}(0) e^{-\frac{t}{T_2}} \\ \rho_{10}(0) e^{-\frac{t}{T_2}} & \rho_{11} \end{pmatrix}, \quad \frac{1}{T_2} = \frac{1}{2 T_1} + \frac{1}{T_\phi}"
    nom_coherence = [
        ("Ma trận mật độ trạng thái lượng tử", "<i>ρ</i>(<i>t</i>)", "không thứ nguyên", "Toán tử thống kê mô tả toàn diện hệ lượng tử đóng hoặc mở"),
        ("Phần tử ngoài đường chéo", "<i>ρ</i><sub>01</sub>(<i>t</i>)", "không thứ nguyên", "Biên độ kết hợp pha lượng tử giữa hai mức năng lượng |0⟩ và |1⟩"),
        ("Thời gian giải kết hợp ngang", "<i>T</i><sub>2</sub>", "s", "Thời gian suy giảm độ kết hợp pha lượng tử do tán xạ vi mô"),
        ("Thời gian hồi phục năng lượng dọc", "<i>T</i><sub>1</sub>", "s", "Thời gian phân rã năng lượng về trạng thái cơ bản cân bằng nhiệt"),
        ("Thời gian lệch pha thuần túy", "<i>T</i><sub>ϕ</sub>", "s", "Thời gian thăng giáng pha ngẫu nhiên không tiêu hao năng lượng")
    ]
    story.append(he.build_target_equation_block(eq_coherence, nom_coherence, styles=styles))
    story.append(Spacer(1, 6))

    step1_text = (
        "Thiết lập phương trình chủ vi phân Lindblad mô tả động học mở của ma trận mật độ dưới tác động của toán tử giải pha:"
    )
    step1_eq = r"\frac{d\rho}{dt} = -\frac{i}{\hbar} [H_0, \rho] + \frac{1}{2 T_\phi} \left( \sigma_z \rho \sigma_z - \rho \right)"
    story.append(he.build_intermediate_equation(step1_text, step1_eq, styles=styles, is_expanded_from_slide=True))

    step2_text = (
        "Chiếu phương trình lên các phần tử ma trận trong cơ sở trạng thái hai mức. Phần tử đường chéo bảo toàn dân số hạt, "
        "trong khi phần tử ngoài đường chéo thỏa mãn phương trình phân rã hàm mũ bậc nhất:"
    )
    step2_eq = r"\frac{d\rho_{01}(t)}{dt} = -\left( \frac{1}{2 T_1} + \frac{1}{T_\phi} \right) \rho_{01}(t) = -\frac{1}{T_2} \rho_{01}(t)"
    story.append(he.build_intermediate_equation(step2_text, step2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    # Giai đoạn 4: Biến thiên tham số & Quét tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g1_p4 = (
        "<b>Khảo sát động học giải kết hợp theo nhiệt độ và cấu trúc nano:</b><br/>"
        "• <i>Ở nhiệt độ phòng (T = 300 K):</i> Mật độ phonon âm thanh tỷ lệ thuận với nhiệt độ <i>T</i>. Tán xạ liên tục làm thời gian "
        "lệch pha <i>T</i><sub>ϕ</sub> rút ngắn xuống dưới 1 ps (10⁻¹² s), khiến mọi hiệu ứng lượng tử bị xóa sổ ngay tức khắc.<br/>"
        "• <i>Ở nhiệt độ đông lạnh (T = 4 K hoặc mK):</i> Tán xạ phonon bị đóng băng hoàn toàn. Thời gian <i>T</i><sub>2</sub> trong "
        "các chấm lượng tử bán dẫn (GaAs, InAs) tăng vọt lên hàng chục microgiây (μs), và trong tâm khuyết tật kim cương NV-center "
        "có thể đạt tới hàng mili-giây (ms), mở ra khả năng thực hiện hàng triệu phép tính cổng lượng tử liên tiếp.<br/>"
        "• <i>Giới hạn tiệm cận (t ≫ T₂):</i> Khi thời gian khảo sát vượt xa <i>T</i><sub>2</sub>, phần tử ngoài đường chéo <i>ρ</i><sub>01</sub> "
        "triệt tiêu về 0, độ tinh khiết lượng tử <i>γ</i>(<i>t</i>) = Tr(<i>ρ</i>²) giảm từ 1 (trạng thái tinh khiết) xuống 0.5 (trạng thái hỗn hợp tối đa)."
    )
    story.append(he.make_paragraph(g1_p4, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng đồ thị mô phỏng 1
    img_sim_decoherence = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.5_Suy_Giam_Do_Ket_Hop_Decoherence_Qubit.png")
    cap_sim_decoherence = "Hình 2.5.3: Đồ thị mô phỏng giải tích động học suy giảm độ kết hợp lượng tử (Decoherence) và độ tinh khiết ma trận mật độ."
    story.append(he.embed_figure_with_caption(img_sim_decoherence, cap_sim_decoherence, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách tự luyện CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_1 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Để hiện thực hóa các mạch xử lý thông tin lượng tử trên cấu trúc nano bán dẫn, việc cô lập nhiệt "
        "ở nhiệt độ siêu hàn (Cryogenic temperatures &lt; 1 K) là điều kiện bắt buộc tiên quyết không thể thay thế.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Thời gian phân rã pha <i>T</i><sub>2</sub> của hạt tải trong chấm lượng tử tỷ lệ nghịch "
        "với mật độ tán xạ phonon (tỷ lệ thuận với <i>k</i><sub>B</sub><i>T</i> chia cho năng lượng phonon <i>ℏω</i><sub>ph</sub>). Tại 300 K, <i>T</i><sub>2</sub> &lt; 1 ps, "
        "trong khi thời gian thực thi một xung cổng lượng tử vi sóng <i>τ</i><sub>gate</sub> tối thiểu là 10 ns (chậm hơn 10 000 lần so với tốc độ mất kết hợp). "
        "Chỉ khi hạ nhiệt độ xuống dưới 100 mK, <i>T</i><sub>2</sub> mới kéo dài lên &gt; 10 μs, bảo đảm số lượng phép tính <i>N</i><sub>ops</sub> = <i>T</i><sub>2</sub> · <i>τ</i><sub>gate</sub><sup>−1</sup> &gt; 1000.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Cơ học lượng tử đòi hỏi bảo toàn pha tương đối của hàm sóng trong suốt chuỗi thuật toán. Mọi tương tác nhiệt vi mô "
        "đóng vai trò như một phép đo vô thức liên tục của môi trường lên hệ, làm sụp đổ hàm sóng và xóa sạch thông tin pha lượng tử trước khi kịp tính toán.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Sinh viên thường ngộ nhận rằng làm kích thước hạt nano càng nhỏ thì thời gian kết hợp càng dài. "
        "Thực tế, hạt nano càng nhỏ thì tỷ lệ diện tích bề mặt càng lớn, dẫn tới mật độ bẫy điện tích và liên kết treo bề mặt càng cao, gây ra nhiễu điện tích cục bộ (Charge noise) "
        "làm <i>T</i><sub>2</sub> suy giảm nghiêm trọng nếu bề mặt không được thụ động hóa hoàn hảo."
    )
    story.append(he.make_paragraph(cer_1, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.5.2: CHỒNG CHẤT LƯỢNG TỬ & VƯỚNG VÍU LƯỢNG TỬ
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.5.2: Chồng chất lượng tử &amp; Hiện tượng Vướng víu lượng tử (Entanglement)", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g2_p1 = (
        "<b>Nguyên lý chồng chất lượng tử:</b> Tương tự như sóng cổ điển, bất kỳ hai hoặc nhiều trạng thái lượng tử hợp lệ nào cũng có thể "
        "được cộng lại với nhau để tạo thành một trạng thái lượng tử mới. Ngược lại, mọi trạng thái lượng tử bất kỳ đều có thể phân tích thành "
        "tổng của các trạng thái cơ sở độc lập.<br/>"
        "<b>Hiện tượng Vướng víu lượng tử (Quantum Entanglement):</b> Là hệ quả sâu sắc nhất của nguyên lý chồng chất áp dụng cho hệ đa hạt. "
        "Đây là một hiệu ứng kỳ lạ trong đó trạng thái của hai hay nhiều vật thể có liên hệ tức thời với nhau bất kể khoảng cách không gian giữa chúng "
        "xa đến đâu. Khi một cặp hạt bị vướng víu, trạng thái lượng tử của toàn hệ thống không thể phân tích thành tích đại số của các trạng thái từng hạt riêng lẻ."
    )
    story.append(he.make_paragraph(g2_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_superpos = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_03_Su_Chong_Chat_Luong_Tu.png")
    cap_superpos = "Hình 2.5.4: Nguyên lý chồng chất lượng tử — cơ sở cho sự tồn tại đồng thời của nhiều trạng thái thành phần (Slide 58)."
    story.append(he.embed_figure_with_caption(img_superpos, cap_superpos, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_entangle = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_04_Cap_Hat_Roi_Luong_Tu.png")
    cap_entangle = "Hình 2.5.5: Minh họa cặp hạt bị vướng víu (rối lượng tử) — liên hệ tức thời không phụ thuộc khoảng cách (Slide 59)."
    story.append(he.embed_figure_with_caption(img_entangle, cap_entangle, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g2_p2 = (
        "<b>Ví dụ tối thiểu về cặp photon vướng víu phân cực:</b> Xét một nguồn sáng phát xạ đồng thời hai photon A và B truyền về hai hướng ngược nhau. "
        "Trạng thái của cặp photon không phải là 'A phân cực ngang và B phân cực dọc', cũng không phải 'A phân cực dọc và B phân cực ngang'. "
        "Trước khi thực hiện phép đo, cả hai photon đều không sở hữu bất kỳ trạng thái phân cực xác định nào; chúng tồn tại trong sự chồng chất đồng thời "
        "của cả hai khả năng. Tuy nhiên, ngay khoảnh khắc Alice đặt kính phân cực và phát hiện photon A có phân cực ngang, trạng thái của photon B tại trạm Bob "
        "— dù cách xa hàng năm ánh sáng — lập tức sụp đổ thành phân cực dọc với xác suất 100% không có bất kỳ độ trễ thời gian nào."
    )
    story.append(he.make_paragraph(g2_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_entangle = r"|\Psi^-\rangle = \frac{1}{\sqrt{2}} \left( |H\rangle_A |V\rangle_B - |V\rangle_A |H\rangle_B \right), \quad E(a, b) = -\cos\left(2 (\theta_a - \theta_b)\right)"
    nom_entangle = [
        ("Trạng thái vướng víu Bell singlet", "|<i>Ψ</i><sup>−</sup>⟩", "vectơ Hilbert", "Trạng thái vướng víu cực đại có tổng spin bằng 0"),
        ("Trạng thái phân cực cơ sở", "|<i>H</i>⟩, |<i>V</i>⟩", "vectơ trực chuẩn", "Trạng thái phân cực tuyến tính ngang (Horizontal) và dọc (Vertical)"),
        ("Góc định hướng kính phân cực Alice và Bob", "<i>θ</i><sub>a</sub>, <i>θ</i><sub>b</sub>", "rad (hoặc độ)", "Góc nghiêng của trục quang học trên hai kính phân cực độc lập"),
        ("Hàm tương quan phân cực lượng tử", "<i>E</i>(<i>a</i>, <i>b</i>)", "không thứ nguyên", "Giá trị kỳ vọng toán học của tích kết quả đo nhị phân giữa hai trạm")
    ]
    story.append(he.build_target_equation_block(eq_entangle, nom_entangle, styles=styles))
    story.append(Spacer(1, 6))

    step2_1_text = (
        "Biểu diễn trạng thái photon truyền qua kính phân cực nghiêng góc <i>θ</i> dưới dạng tổ hợp tuyến tính của cơ sở ngang – dọc:"
    )
    step2_1_eq = r"|\theta\rangle = \cos\theta |H\rangle + \sin\theta |V\rangle, \quad |\theta^\perp\rangle = -\sin\theta |H\rangle + \cos\theta |V\rangle"
    story.append(he.build_intermediate_equation(step2_1_text, step2_1_eq, styles=styles, is_expanded_from_slide=True))

    step2_2_text = (
        "Toán tử đo phân cực gán giá trị +1 cho photon truyền qua và −1 cho photon bị chặn: <i>Â</i>(<i>θ</i><sub>a</sub>) = |<i>θ</i><sub>a</sub>⟩⟨<i>θ</i><sub>a</sub>| − |<i>θ</i><sub>a</sub><sup>⊥</sup>⟩⟨<i>θ</i><sub>a</sub><sup>⊥</sup>|. "
        "Tính toán tích tenxơ tác dụng lên trạng thái singlet |<i>Ψ</i><sup>−</sup>⟩ thu được hàm tương quan góc lượng tử:"
    )
    step2_2_eq = r"E(a, b) = \langle\Psi^-| \hat{A}(\theta_a) \otimes \hat{B}(\theta_b) |\Psi^-\rangle = -\left(\cos^2(\theta_a - \theta_b) - \sin^2(\theta_a - \theta_b)\right) = -\cos\left(2(\theta_a - \theta_b)\right)"
    story.append(he.build_intermediate_equation(step2_1_text, step2_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g2_p4 = (
        "<b>So sánh tương quan lượng tử với mô hình cổ điển:</b><br/>"
        "• Khi hai kính phân cực song song (<i>θ</i><sub>a</sub> = <i>θ</i><sub>b</sub>): <i>E</i> = −cos(0) = −1. Tương quan nghịch tuyệt đối (100% photon ngược chiều).<br/>"
        "• Khi hai kính phân cực vuông góc (<i>θ</i><sub>a</sub> − <i>θ</i><sub>b</sub> = 90°): <i>E</i> = −cos(180°) = +1. Tương quan thuận tuyệt đối.<br/>"
        "• Khi hiệu góc là 22.5°: Cơ học lượng tử cho <i>E</i><sub>QM</sub> = −cos(45°) ≈ −0.707 (tức bằng một nửa căn bậc hai của 2 mang dấu âm). "
        "Trong khi đó, mọi mô hình biến ẩn địa phương cổ điển chỉ có thể đạt tối đa <i>E</i><sub>LHV</sub> = −0.500. "
        "Chính sự chênh lệch sâu sắc ở các góc trung gian này là bằng chứng không thể bác bỏ về tính phi cục bộ của tự nhiên."
    )
    story.append(he.make_paragraph(g2_p4, styles["Body"]))
    story.append(Spacer(1, 4))

    img_sim_pol = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.5_Tuong_Quan_Phan_Cuc_Photon_Vuong_Viu.png")
    cap_sim_pol = "Hình 2.5.6: Đồ thị hàm tương quan phân cực photon vướng víu E(a, b) — so sánh lý thuyết lượng tử, mô hình cổ điển và thực nghiệm."
    story.append(he.embed_figure_with_caption(img_sim_pol, cap_sim_pol, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_2 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Hiện tượng vướng víu lượng tử không cho phép gửi tín hiệu thông tin hữu ích nhanh hơn vận tốc ánh sáng (Định lý Không truyền tin nhanh hơn ánh sáng — No-Communication Theorem).<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Xác suất đo được của Bob khi nhận photon B độc lập với góc chọn <i>θ</i><sub>a</sub> của Alice: "
        "<i>P</i><sub>Bob</sub>(+1) = Tr<sub>A,B</sub>[(<i>I</i> ⊗ |<i>θ</i><sub>b</sub>⟩⟨<i>θ</i><sub>b</sub>|) <i>ρ</i><sub>AB</sub>] = 0.5. Dù Alice đo ở bất kỳ góc nào, "
        "chuỗi kết quả đo của Bob luôn là một chuỗi bit ngẫu nhiên hoàn toàn (50% +1 và 50% −1).<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Bob không thể nhận biết được Alice đã đo hay chưa đo nếu không có thông tin đối chiếu gửi qua kênh truyền thông cổ điển (tốc độ ánh sáng). "
        "Tương quan vướng víu chỉ bộc lộ khi Alice và Bob gặp nhau hoặc gọi điện thoại đối chiếu hai bảng số liệu.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù kinh điển của sinh viên là nghĩ rằng 'tác động tức thời' đồng nghĩa với 'truyền tin tức thời'. "
        "Vướng víu lượng tử thiết lập mối tương quan giữa các sự kiện ngẫu nhiên, chứ không thiết lập kênh truyền tin nhân quả có thể điều khiển được."
    )
    story.append(he.make_paragraph(cer_2, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.5.3: NGHỊCH LÝ EPR & BIẾN ẨN ĐỊA PHƯƠNG
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.5.3: Nghịch lý EPR (1935) &amp; Cuộc tranh luận về Biến ẩn địa phương", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g3_p1 = (
        "Năm 1935, Albert Einstein, Boris Podolsky và Nathan Rosen công bố bài báo lịch sử trên tạp chí <i>Physical Review</i> "
        "mang tựa đề: <i>'Can Quantum-Mechanical Description of Physical Reality be Considered Complete?'</i> (Mô tả của Cơ học lượng tử về "
        "thực tại vật lý có thể coi là đầy đủ không?). Nhóm EPR đưa ra định nghĩa về <b>Yếu tố thực tại vật lý</b>: "
        "'Nếu không làm xáo trộn hệ mà chúng ta có thể dự đoán chắc chắn 100% giá trị của một đại lượng vật lý, thì phải tồn tại một yếu tố thực tại "
        "tương ứng với đại lượng đó.'<br/>"
        "EPR lập luận rằng nếu cơ học lượng tử đúng, ta có thể đo vị trí của hạt 1 để suy ra vị trí hạt 2, đồng thời đo động lượng của hạt 1 để suy ra "
        "động lượng hạt 2. Vì hai hạt ở xa nhau không thể tương tác tức thời (Thuyết tương đối hẹp), hạt 2 bắt buộc phải sở hữu sẵn cả vị trí và động lượng "
        "xác định từ trước khi đo. Nhưng cơ học lượng tử qua Hệ thức bất định Heisenberg lại khẳng định không thể tồn tại đồng thời cả vị trí và động lượng chính xác. "
        "Do đó, EPR kết luận: Cơ học lượng tử chưa hoàn chỉnh và tự nhiên phải chứa các <b>Biến ẩn địa phương</b> (Local Hidden Variables) mà con người chưa biết."
    )
    story.append(he.make_paragraph(g3_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_epr_35 = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_05_Nghich_Ly_EPR_1935.png")
    cap_epr_35 = "Hình 2.5.7: Nghịch lý EPR (Einstein – Podolsky – Rosen 1935) — cuộc tranh luận lịch sử về tính đầy đủ của cơ học lượng tử (Slide 60)."
    story.append(he.embed_figure_with_caption(img_epr_35, cap_epr_35, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_epr_meas = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_06_Phep_Do_EPR_Vi_Tri_Dong_Luong.png")
    cap_epr_meas = "Hình 2.5.8: Phép đo tương quan vị trí và động lượng trong nghịch lý EPR (Slide 61)."
    story.append(he.embed_figure_with_caption(img_epr_meas, cap_epr_meas, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_hidden_var = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_07_Mo_Hinh_Bien_An_Dia_Phuong.png")
    cap_hidden_var = "Hình 2.5.9: Mô hình lý thuyết cặp quả bóng chứa biến ẩn địa phương — giả thiết thông tin được lập trình sẵn trước khi tách rời (Slide 62)."
    story.append(he.embed_figure_with_caption(img_hidden_var, cap_hidden_var, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_qm_pair = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_08_Mo_Hinh_Luong_Tu_Cap_Hat_Roi.png")
    cap_qm_pair = "Hình 2.5.10: Mô hình cơ học lượng tử về cặp hạt vướng víu — trạng thái không định trước cho tới khi thực hiện phép đo (Slide 63)."
    story.append(he.embed_figure_with_caption(img_qm_pair, cap_qm_pair, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g3_p2 = (
        "<b>Ẩn dụ đôi giày của Bertlmann và Biến ẩn địa phương:</b> Giáo sư John Bell từng đưa ra ẩn dụ hóm hỉnh về đôi tất của đồng nghiệp Reinhold Bertlmann: "
        "Bertlmann luôn có thói quen đi hai chiếc tất khác màu nhau. Nếu bạn nhìn thấy chân trái ông ấy đi tất màu hồng, bạn lập tức biết chắc chắn 100% "
        "rằng chân phải đi tất màu khác (không phải màu hồng). Đây là sự tương quan cổ điển hoàn toàn bình thường, bởi vì màu sắc của từng chiếc tất "
        "đã được định hình sẵn ngay từ sáng khi Bertlmann xỏ chân vào giày (biến ẩn địa phương). "
        "Einstein tin rằng cặp photon vướng víu cũng giống như đôi tất của Bertlmann: mọi thông tin đều đã được lập trình sẵn từ nguồn phát. "
        "Tuy nhiên, cơ học lượng tử lại khẳng định điều kỳ quặc hơn nhiều: Chiếc tất thực sự không có màu sắc nào cho tới tận khoảnh khắc bạn nhìn vào nó!"
    )
    story.append(he.make_paragraph(g3_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_epr = r"[\hat{x}_1 - \hat{x}_2, \hat{p}_1 + \hat{p}_2] = [\hat{x}_1, \hat{p}_1] - [\hat{x}_2, \hat{p}_2] = i\hbar - i\hbar = 0"
    nom_epr = [
        ("Toán tử hiệu khoảng cách hai hạt", "<i>x̂</i><sub>1</sub> − <i>x̂</i><sub>2</sub>", "m", "Tọa độ không gian tương đối giữa hạt thứ nhất và hạt thứ hai"),
        ("Toán tử tổng động lượng", "<i>p̂</i><sub>1</sub> + <i>p̂</i><sub>2</sub>", "kg·m/s", "Tổng động lượng toàn phần của hệ hai hạt cô lập"),
        ("Giao hoán tử Heisenberg", "[<i>Â</i>, <i>B̂</i>]", "J·s", "Đại lượng đo lường tính tương thích của hai toán tử quan sát"),
        ("Hằng số Dirac rút gọn", "<i>ℏ</i>", "J·s", "Hằng số tác dụng lượng tử vi mô: 1.054571817 × 10⁻³⁴ J·s")
    ]
    story.append(he.build_target_equation_block(eq_epr, nom_epr, styles=styles))
    story.append(Spacer(1, 6))

    step3_1_text = (
        "Xét hàm sóng EPR hai hạt chuyển động một chiều trong không gian Hilbert liên tục thỏa mãn điều kiện delta Dirac:"
    )
    step3_1_eq = r"\Psi(x_1, x_2) = \int_{-\infty}^{+\infty} \exp\left( \frac{i}{\hbar} p (x_1 - x_2 + x_0) \right) dp \propto \delta(x_1 - x_2 + x_0)"
    story.append(he.build_intermediate_equation(step3_1_text, step3_1_eq, styles=styles, is_expanded_from_slide=True))

    step3_2_text = (
        "Hàm sóng này đồng thời là trạng thái riêng của hiệu tọa độ (trị riêng −<i>x</i><sub>0</sub>) và tổng động lượng (trị riêng 0). "
        "Do giao hoán tử triệt tiêu, tích độ bất định của chúng bằng 0 mà không vi phạm nguyên lý Heisenberg tổng quát:"
    )
    step3_2_eq = r"\Delta(x_1 - x_2) \cdot \Delta(p_1 + p_2) \ge \frac{1}{2} | \langle [\hat{x}_1 - \hat{x}_2, \hat{p}_1 + \hat{p}_2] \rangle | = 0"
    story.append(he.build_intermediate_equation(step3_1_text, step3_2_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g3_p4 = (
        "<b>Phân kỳ quan điểm giữa Einstein và Niels Bohr:</b><br/>"
        "• <i>Lập trường Einstein (Local Realism):</i> Tính thực tại (Realism) đòi hỏi các đại lượng vật lý phải tồn tại độc lập với quan sát. "
        "Tính địa phương (Locality) đòi hỏi không có tác động nào truyền nhanh hơn ánh sáng. Do đó, cơ học lượng tử là một lý thuyết thống kê chưa hoàn chỉnh.<br/>"
        "• <i>Lập trường Niels Bohr (Bổ sung học Copenhagen):</i> Không thể phân chia hệ lượng tử thành các thực thể độc lập khi chúng đang vướng víu. "
        "Phép đo trên hạt 1 làm thay đổi toàn bộ điều kiện biên của toàn hệ thống, do đó việc gán 'thực tại' cho hạt 2 trước khi đo là vô nghĩa về mặt vật lý."
    )
    story.append(he.make_paragraph(g3_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_3 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Nghịch lý EPR không phải là một mâu thuẫn toán học nội tại của cơ học lượng tử, mà là sự xung đột sâu sắc giữa hai thế giới quan triết học về bản chất của thực tại.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Về mặt toán học, hàm sóng EPR hoàn toàn tuân thủ chặt chẽ phương trình Schrödinger và đại số toán tử giao hoán [<i>x̂</i><sub>1</sub> − <i>x̂</i><sub>2</sub>, <i>p̂</i><sub>1</sub> + <i>p̂</i><sub>2</sub>] = 0. "
        "Không có bất kỳ tiên đề toán học nào bị vi phạm.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Mâu thuẫn nảy sinh khi EPR áp đặt giả định tiên nghiệm của cơ học cổ điển: 'thế giới khách quan phải bao gồm các hạt mang sẵn tính chất cục bộ'. "
        "Khi cơ học lượng tử phủ nhận giả định này, EPR cho rằng lý thuyết chưa đầy đủ, thay vì chấp nhận rằng bản thân tự nhiên không tuân theo tính thực tại địa phương.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Nhiều sinh viên nhầm lẫn rằng EPR đã chứng minh cơ học lượng tử sai. "
        "Thực tế, EPR chỉ chứng minh rằng: Hoặc cơ học lượng tử chưa đầy đủ, hoặc tự nhiên mang tính phi địa phương (Non-local). "
        "Và các giải Nobel thực nghiệm sau này đã chứng minh rằng vế thứ hai mới là sự thật!"
    )
    story.append(he.make_paragraph(cer_3, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.5.4: BẤT ĐẲNG THỨC BELL & MỞ RỘNG CHSH
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.5.4: Bất đẳng thức Bell và Mở rộng CHSH", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g4_p1 = (
        "Suốt 30 năm sau bài báo EPR, cuộc tranh luận giữa Einstein và Bohr rơi vào bế tắc triết học vì cả hai bên đều không thể đưa ra một thí nghiệm "
        "để phân định đúng sai. Bước ngoặt lịch sử xảy ra vào năm 1964, khi nhà vật lý lý thuyết người Bắc Ireland John Stewart Bell "
        "tại Trung tâm Nghiên cứu Hạt nhân Châu Âu (CERN) đã tìm ra một công cụ toán học định lượng: <b>Bất đẳng thức Bell</b> (Bell's Theorem).<br/>"
        "Bell chứng minh rằng: Nếu tự nhiên thực sự tuân theo nguyên lý Thực tại Địa phương của Einstein (tức kết quả đo chỉ phụ thuộc vào biến ẩn cục bộ <i>λ</i> "
        "và các thiết lập tại chỗ), thì độ tương quan thống kê giữa hai hạt bắt buộc phải bị chặn bởi một giới hạn số học xác định. "
        "Đến năm 1969, John Clauser, Michael Horne, Abner Shimony và Richard Holt đã mở rộng định lý này thành dạng khả thi cho thực nghiệm quang học: "
        "<b>Bất đẳng thức CHSH</b> với giới hạn |<i>S</i>| ≤ 2."
    )
    story.append(he.make_paragraph(g4_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_bell_limit = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_09_Bat_Dang_Thuc_Bell_Gioi_Han.png")
    cap_bell_limit = "Hình 2.5.11: Bất đẳng thức Bell — giới hạn tương quan xác định của các lý thuyết biến ẩn địa phương (Slide 64)."
    story.append(he.embed_figure_with_caption(img_bell_limit, cap_bell_limit, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g4_p2 = (
        "<b>Ý tưởng toán học của phép đo CHSH:</b> Alice có thể chọn đo ở một trong hai góc (<i>a</i> hoặc <i>a</i>′), cho kết quả <i>A</i> ∈ {+1, −1}. "
        "Bob có thể chọn đo ở một trong hai góc (<i>b</i> hoặc <i>b</i>′), cho kết quả <i>B</i> ∈ {+1, −1}. "
        "Xét đại lượng số học đơn giản: <i>A</i>·<i>B</i> + <i>A</i>·<i>B</i>′ + <i>A</i>′·<i>B</i> − <i>A</i>′·<i>B</i>′ = <i>A</i>(<i>B</i> + <i>B</i>′) + <i>A</i>′(<i>B</i> − <i>B</i>′). "
        "Vì <i>B</i> và <i>B</i>′ chỉ nhận giá trị ±1, nên một trong hai số (<i>B</i> + <i>B</i>′) hoặc (<i>B</i> − <i>B</i>′) bắt buộc phải bằng ±2, và số còn lại phải bằng 0. "
        "Do đó, đối với từng cặp hạt đơn lẻ mang biến ẩn cổ điển, đại lượng này luôn luôn bằng ±2. "
        "Khi lấy trung bình thống kê trên hàng triệu phép đo, giá trị kỳ vọng |<i>S</i>| tuyệt đối không thể vượt quá 2."
    )
    story.append(he.make_paragraph(g4_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_chsh = r"S = E(a, b) + E(a, b') + E(a', b) - E(a', b') \implies |S_{\mathrm{classical}}| \le 2, \quad |S_{\mathrm{QM}}| \le 2\sqrt{2} \approx 2.8284"
    nom_chsh = [
        ("Tham số tương quan CHSH", "<i>S</i>", "không thứ nguyên", "Tổ hợp tuyến tính của 4 hàm tương quan giữa 2 cấu hình góc của Alice và 2 góc của Bob"),
        ("Giới hạn biến ẩn cổ điển Bell", "<i>S</i><sub>classical</sub>", "không thứ nguyên", "Chặn trên lý thuyết của mọi mô hình thực tại địa phương: |<i>S</i>| ≤ 2"),
        ("Giới hạn Cirel'son lượng tử", "2√2", "không thứ nguyên", "Chặn trên toán học tối cao của cơ học lượng tử đối với trạng thái hai mức"),
        ("Hàm tương quan thống kê", "<i>E</i>(<i>a</i>, <i>b</i>)", "không thứ nguyên", "Kỳ vọng toán học của tích kết quả đo giữa hai trạm")
    ]
    story.append(he.build_target_equation_block(eq_chsh, nom_chsh, styles=styles))
    story.append(Spacer(1, 6))

    step4_1_text = (
        "Trong lý thuyết biến ẩn địa phương, kết quả đo của Alice <i>A</i>(<i>a</i>, <i>λ</i>) và Bob <i>B</i>(<i>b</i>, <i>λ</i>) được quyết định bởi tham số ẩn <i>λ</i> với hàm mật độ xác suất <i>ρ</i>(<i>λ</i>) ≥ 0 thỏa mãn ∫ <i>ρ</i>(<i>λ</i>) <i>dλ</i> = 1:"
    )
    step4_1_eq = r"E(a, b) = \int_{\Lambda} A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda \quad \text{với} \quad A(a, \lambda) \in \{-1, +1\}, \; B(b, \lambda) \in \{-1, +1\}"
    story.append(he.build_intermediate_equation(step4_1_text, step4_1_eq, styles=styles, is_expanded_from_slide=True))

    step4_2_text = (
        "Lấy tích phân hiệu tương quan và áp dụng bất đẳng thức tam giác tích phân, ta chứng minh được bất đẳng thức CHSH cổ điển:"
    )
    step4_2_eq = r"|S_{\mathrm{classical}}| = \left| \int \left[ A(a,\lambda)B(b,\lambda) + A(a,\lambda)B(b',\lambda) + A(a',\lambda)B(b,\lambda) - A(a',\lambda)B(b',\lambda) \right] \rho(\lambda) d\lambda \right| \le 2"
    story.append(he.build_intermediate_equation(step4_1_text, step4_2_eq, styles=styles, is_expanded_from_slide=True))

    step4_3_text = (
        "Trong cơ học lượng tử, chọn hệ 4 góc tối ưu: <i>a</i> = 0°, <i>a</i>′ = 45°, <i>b</i> = 22.5°, <i>b</i>′ = 67.5°. "
        "Thay hàm tương quan lượng tử <i>E</i>(<i>x</i>, <i>y</i>) = −cos(2(<i>x</i> − <i>y</i>)) vào biểu thức <i>S</i>:"
    )
    step4_3_eq = r"S_{\mathrm{QM}} = -\cos(-45^\circ) - \cos(-135^\circ) - \cos(45^\circ) + \cos(-45^\circ) = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = 2\sqrt{2} \approx 2.8284"
    story.append(he.build_intermediate_equation(step4_1_text, step4_3_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g4_p4 = (
        "<b>Phân tích miền vi phạm bất đẳng thức Bell (Quantum Violation):</b><br/>"
        "• Tại <i>θ</i> = 0° và <i>θ</i> = 45°: <i>S</i> = 2, giá trị lượng tử chạm đúng giới hạn cổ điển.<br/>"
        "• Tại <i>θ</i> = 22.5°: <i>S</i> đạt cực đại toàn cục <i>S</i> = 2√2 ≈ 2.8284, vi phạm vượt ngưỡng cổ điển tới 41.4%. "
        "Khoảng chênh lệch 0.8284 này là bằng chứng định lượng tuyệt đối, không thể giải thích bằng bất kỳ sai số đo đạc hay giả thiết ngẫu nhiên nào."
    )
    story.append(he.make_paragraph(g4_p4, styles["Body"]))
    story.append(Spacer(1, 4))

    img_sim_chsh = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.5_Bat_Dang_Thuc_Bell_CHSH.png")
    cap_sim_chsh = "Hình 2.5.12: Đồ thị kiểm chứng bất đẳng thức Bell-CHSH — vùng bóng vi phạm lượng tử S > 2 và đỉnh cực đại Cirel'son."
    story.append(he.embed_figure_with_caption(img_sim_chsh, cap_sim_chsh, kind="sim", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_4 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Giá trị tương quan CHSH của cơ học lượng tử có thể đạt tới 2√2 ≈ 2.828 nhưng tuyệt đối không thể đạt tới giá trị cực đại đại số bằng 4.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Định lý Cirel'son (1980) chứng minh rằng đối với mọi trạng thái lượng tử trên không gian Hilbert và mọi toán tử Hermite có trị riêng ±1: "
        "||<i>Â</i> ⊗ <i>B̂</i> + <i>Â</i> ⊗ <i>B̂</i>′ + <i>Â</i>′ ⊗ <i>B̂</i> − <i>Â</i>′ ⊗ <i>B̂</i>′|| ≤ 2√2.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Để <i>S</i> = 4, cả 4 số hạng <i>E</i>(<i>a</i>, <i>b</i>) đều phải bằng ±1 đồng thời. "
        "Tuy nhiên, hai toán tử đo <i>Â</i>(<i>a</i>) và <i>Â</i>(<i>a</i>′) của Alice là hai toán tử không giao hoán ([<i>Â</i>, <i>Â</i>′] ≠ 0). "
        "Hệ thức bất định Heisenberg giữa hai phép đo trực giao ngăn cản việc photon thỏa mãn đồng thời tính xác định tuyệt đối ở cả hai góc đo.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Một số lý thuyết hậu lượng tử giả định (như Hộp PR - Popescu-Rohrlich box) có thể đạt <i>S</i> = 4 "
        "mà vẫn không truyền tin nhanh hơn ánh sáng, nhưng chúng không tồn tại trong vũ trụ vật lý của chúng ta vì vi phạm các nguyên lý bảo toàn thông tin lượng tử."
    )
    story.append(he.make_paragraph(cer_4, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.5.5: THỰC NGHIỆM NOBEL 2022 & ỨNG DỤNG NANO LƯỢNG TỬ
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.5.5: Các mốc thực nghiệm Nobel 2022 &amp; Ứng dụng công nghệ nano lượng tử", styles["H2"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g5_p1 = (
        "Giải Nobel Vật lý năm 2022 đã được trao cho ba nhà khoa học tiên phong: <b>John F. Clauser</b> (Hoa Kỳ), "
        "<b>Alain Aspect</b> (Pháp) và <b>Anton Zeilinger</b> (Áo) <i>'cho các thí nghiệm với các photon vướng víu, "
        "thiết lập sự vi phạm các bất đẳng thức Bell và tiên phong trong khoa học thông tin lượng tử'</i>.<br/>"
        "Lịch sử kiểm chứng thực nghiệm trải qua ba giai đoạn mang tính quyết định:<br/>"
        "1. <b>John Clauser (1972):</b> Cùng nghiên cứu sinh Stuart Freedman tại UC Berkeley, Clauser chế tạo nguồn phát photon vướng víu từ "
        "phân rã bậc thang của nguyên tử Canxi, lần đầu tiên đo được <i>S</i> vi phạm bất đẳng thức Bell với độ tin cậy thống kê 5<i>σ</i>.<br/>"
        "2. <b>Alain Aspect (1982):</b> Tại Viện Quang học Orsay (Paris), Aspect đưa vào thiết bị chuyển mạch quang âm (Acousto-optic switch) "
        "cho phép đổi hướng phân cực ngẫu nhiên cứ sau mỗi 10 ns khi photon đang bay trên quãng đường 6 m, đóng hoàn toàn <b>Kẽ hở định vị địa phương</b> (Locality loophole).<br/>"
        "3. <b>Anton Zeilinger (1998–nay):</b> Tại Đại học Vienna, Zeilinger sử dụng tinh thể phi tuyến sinh cặp photon SPDC, áp dụng máy phát số ngẫu nhiên lượng tử "
        "và sợi quang học, thực hiện viễn tải lượng tử (Quantum Teleportation) và đóng <b>Kẽ hở tự do lựa chọn</b> (Freedom-of-choice loophole)."
    )
    story.append(he.make_paragraph(g5_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    img_clauser_photo = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_10_John_Clauser_Berkeley_1976.png")
    cap_clauser_photo = "Hình 2.5.13: Nhà vật lý John Clauser bên cạnh hệ thí nghiệm vướng víu lượng tử tại UC Berkeley năm 1976 (Slide 65)."
    story.append(he.embed_figure_with_caption(img_clauser_photo, cap_clauser_photo, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_clauser_setup = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_11_Thi_Nghiem_Clauser_1972.png")
    cap_clauser_setup = "Hình 2.5.14: Sơ đồ khối hệ thí nghiệm của John Clauser với cặp photon vướng víu từ nguyên tử Canxi năm 1972 (Slide 66)."
    story.append(he.embed_figure_with_caption(img_clauser_setup, cap_clauser_setup, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_aspect_setup = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_12_Thi_Nghiem_Alain_Aspect_1982.png")
    cap_aspect_setup = "Hình 2.5.15: Mô hình thí nghiệm của Alain Aspect (1982) — chuyển mạch cực nhanh 10 ns trên cự ly 6 m (Slide 67)."
    story.append(he.embed_figure_with_caption(img_aspect_setup, cap_aspect_setup, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_zeilinger_setup = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_13_Thi_Nghiem_Anton_Zeilinger.png")
    cap_zeilinger_setup = "Hình 2.5.16: Sơ đồ thí nghiệm của Anton Zeilinger — laser xung kích hoạt tinh thể phi tuyến SPDC và điều khiển ngẫu nhiên (Slide 68)."
    story.append(he.embed_figure_with_caption(img_zeilinger_setup, cap_zeilinger_setup, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_nano_app = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_14_Ung_Dung_Vat_Lieu_Nano_Luong_Tu.png")
    cap_nano_app = "Hình 2.5.17: Định hướng tích hợp lượng tử vào mọi vật liệu và thiết bị cấu trúc nano (Slide 69)."
    story.append(he.embed_figure_with_caption(img_nano_app, cap_nano_app, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    img_nano_future = os.path.join(kho_anh, "[Goc]_Muc_2.5_Hinh_15_Cong_Nghe_Nano_Luong_Tu_Tuong_Lai.png")
    cap_nano_future = "Hình 2.5.18: Khoa học nano lượng tử — nền tảng công nghệ cho tính toán và truyền thông thế hệ mới (Slide 70)."
    story.append(he.embed_figure_with_caption(img_nano_future, cap_nano_future, kind="orig", styles=styles))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối thiểu &amp; Trực giác vi mô", styles["H3"]))
    g5_p2 = (
        "<b>Kẽ hở định vị (Locality Loophole) và giải pháp của Alain Aspect:</b> Trong thí nghiệm Clauser 1972, các kính phân cực được cố định sẵn. "
        "Một người hoài nghi theo thuyết biến ẩn có thể lập luận rằng: Khi photon rời khỏi nguồn, nó có thể 'phát tín hiệu cổ điển' báo trước cho kính phân cực "
        "để phối hợp kết quả đo. Để triệt tiêu hoàn toàn kẽ hở này, Alain Aspect đã sử dụng hai bộ lọc phân cực cách nhau 6 m. "
        "Thời gian để ánh sáng truyền giữa hai bộ lọc được tính bằng cự ly 6 m chia cho vận tốc ánh sáng 3 × 10⁸ m/s tương đương 20 ns. "
        "Bộ chuyển mạch của Aspect đổi hướng phân cực ngẫu nhiên cứ sau mỗi 10 ns (nhanh gấp đôi thời gian ánh sáng truyền qua). "
        "Theo thuyết tương đối hẹp, không có bất kỳ tín hiệu vật lý nào có thể truyền tin kịp giữa hai trạm đo. "
        "Kết quả đo vẫn vi phạm bất đẳng thức Bell với độ tin cậy vượt bậc: <i>S</i><sub>exp</sub> = 2.697 ± 0.015 > 2."
    )
    story.append(he.make_paragraph(g5_p2, styles["Body"]))
    story.append(Spacer(1, 4))

    story.append(he.make_paragraph("Giai đoạn 3: Trụ cột toán học &amp; Dẫn xuất từng bước", styles["H3"]))
    eq_nobel = r"S_{\mathrm{exp}} = 2.697 \pm 0.015 > 2, \quad \mathrm{QBER} = \frac{N_{\mathrm{error}}}{N_{\mathrm{total}}} < 11\%"
    nom_nobel = [
        ("Tham số CHSH thực nghiệm Aspect", "<i>S</i><sub>exp</sub>", "không thứ nguyên", "Giá trị đo đạc thực tế khẳng định vi phạm Bell với độ lệch chuẩn > 46σ"),
        ("Tỷ lệ lỗi bit lượng tử", "QBER", "%", "Tỷ lệ số bit bị lỗi trên tổng số bit khóa thu nhận trong giao thức phân phối khóa lượng tử"),
        ("Ngưỡng an toàn bảo mật tuyệt đối", "11%", "%", "Ngưỡng sai số tối đa để thuật toán khuếch đại bảo mật trích xuất được khóa an toàn")
    ]
    story.append(he.build_target_equation_block(eq_nobel, nom_nobel, styles=styles))
    story.append(Spacer(1, 6))

    step5_1_text = (
        "Trong giao thức phân phối khóa lượng tử dựa trên vướng víu E91 (Artur Ekert 1991), Alice và Bob sử dụng các cặp photon vướng víu. "
        "Khi kẻ nghe lén Eve cố tình can thiệp đo photon trên đường truyền, trạng thái vướng víu sụp đổ thành hỗn hợp thống kê. "
        "Tham số Bell đo được suy giảm lập tức từ 2√2 về dưới ngưỡng cổ điển:"
    )
    step5_1_eq = r"S_{\mathrm{Eve}} \le \sqrt{2} \approx 1.414 < 2, \quad \mathrm{QBER}_{\mathrm{Eve}} \approx 25\% > 11\%"
    story.append(he.build_intermediate_equation(step5_1_text, step5_1_eq, styles=styles, is_expanded_from_slide=True))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 4: Biến thiên tham số &amp; Quét tiệm cận", styles["H3"]))
    g5_p4 = (
        "<b>Các ứng dụng công nghệ nano lượng tử đột phá:</b><br/>"
        "• <i>Nguồn phát photon đơn lẻ nano:</i> Sử dụng các chấm lượng tử InAs tự lắp ráp bên trong hốc vi cộng hưởng quang học nano (Photonic Crystal Cavities), "
        "đạt hiệu suất phát photon đơn phân biệt được lên tới > 99%.<br/>"
        "• <i>Mạch tích hợp quang tử lượng tử (Quantum PIC):</i> Tích hợp nguồn phát photon, bộ chuyển mạch giao thoa Mach-Zehnder nano và máy dò photon đơn dây nano siêu dẫn (SNSPD) "
        "trên cùng một chip silicon đơn tinh thể kích thước vài milimet.<br/>"
        "• <i>Cảm biến nano lượng tử:</i> Tâm khuyết tật Nitơ-chân không (NV center) trong hạt nano kim cương kích thước 20 nm cho phép đo từ trường cực yếu "
        "với độ nhạy picotesla (10⁻¹² T) và độ phân giải không gian cấp độ nanomet ở nhiệt độ phòng, ứng dụng trong giải trình tự chuỗi xoắn kép DNA."
    )
    story.append(he.make_paragraph(g5_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự luyện &amp; Dự đoán lỗi sai", styles["H3"]))
    cer_5 = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Giải Nobel Vật lý 2022 đánh dấu sự chuyển dịch căn bản từ 'Cuộc cách mạng lượng tử lần thứ nhất' sang 'Cuộc cách mạng lượng tử lần thứ hai'.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Cuộc cách mạng lượng tử lần thứ nhất (thế kỷ 20) dựa trên việc khai thác hành vi lượng tử tập thể của hàng tỷ hạt "
        "(hiệu ứng dải năng lượng trong bóng bán dẫn vi xử lý, phát xạ kích thích trong chùm laser). Cuộc cách mạng lượng tử lần thứ hai (thế kỷ 21) "
        "dựa trên khả năng thao tác, kiểm soát và đo đạc có chủ đích trên từng trạng thái lượng tử đơn lẻ và từng cặp hạt vướng víu cá thể.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Các kỹ thuật chế tạo nano hiện đại (E-beam lithography, MBE, STM/AFM) cho phép con người giam cầm chính xác từng electron đơn lẻ "
        "trong chấm lượng tử và tích hợp chúng vào các mạch vi mạch quang học, biến những hiệu ứng nghịch lý EPR và định lý Bell thành các ứng dụng công nghệ hiện thực.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến là cho rằng máy tính lượng tử sẽ thay thế hoàn toàn máy tính thông thường trong mọi tác vụ. "
        "Thực tế, máy tính lượng tử chỉ vượt trội ở các bài toán có cấu trúc toán học đặc thù (phân tích thừa số nguyên tử Shor, mô phỏng phản ứng hóa học lượng tử, tối ưu hóa tổ hợp), "
        "trong khi các tác vụ tính toán thông thường máy tính bán dẫn cổ điển vẫn nhanh và hiệu quả hơn rất nhiều."
    )
    story.append(he.make_paragraph(cer_5, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # TỔNG KẾT MỤC 2.5
    # =========================================================================
    summary_text = (
        "<b>Tổng kết Mục 2.5:</b> Bản chất và công nghệ nano lượng tử đã làm thay đổi hoàn toàn cách nhân loại hiểu và kiểm soát vật chất. "
        "Từ những nghịch lý tư tưởng ban đầu của Einstein về tính phi địa phương, qua sự định lượng của Bell, đến các thực nghiệm Nobel 2022: "
        "cơ học lượng tử đã chứng minh tính đúng đắn tối thượng. Ngày nay, việc làm chủ độ kết hợp lượng tử và sự vướng víu trên các cấu trúc nano "
        "chính là chìa khóa mở ra kỷ nguyên tính toán lượng tử, mật mã bất khả xâm phạm và công nghệ nano thế hệ mới."
    )
    story.append(he.make_paragraph(summary_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # Xây dựng tài liệu PDF
    print("Đang tiến hành build PDF với BookmarkDocTemplate...")
    doc.build(story)
    print(f"Hoàn tất biên dịch PDF Mục 2.5: {target_pdf}")
    print(f"Kích thước tệp: {os.path.getsize(target_pdf)/1024:.1f} KB")

if __name__ == "__main__":
    build_pdf()

# -*- coding: utf-8 -*-
"""
gen_clean_2_8.py
Biên dịch Chuyên khảo Toàn văn Mục 2.8: Đặc trưng hóa thực nghiệm diode laser thực tế
Coldren & Corzine, trang 52-61.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak

sys.path.append(r"d:\antigravity\academic-research-engine")
sys.path.append(r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")

import hust_pdf_engine as he

drive_base = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý"
img_dir = os.path.join(drive_base, "Kho_Hinh_Anh")
pdf_dir = os.path.join(drive_base, "Bai_Giang_Dong_Goi")
os.makedirs(pdf_dir, exist_ok=True)

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.8.pdf")

# Hình ảnh gốc và mô phỏng
fig_goc_2_13 = os.path.join(img_dir, "[Goc]_Figure_2.13_Nghich_dao_hieu_suat_vi_phan_ngoai_theo_chieu_dai_hoc.png")
fig_goc_2_14 = os.path.join(img_dir, "[Goc]_Figure_2.14_Thuc_nghiem_do_loi_theo_mat_do_dong_InGaAs_GaAs.png")
fig_goc_2_15 = os.path.join(img_dir, "[Goc]_Figure_2.15_Mo_hinh_hinh_hoc_dong_nhiet_1D_2D_3D_trong_laser.png")
fig_goc_2_16 = os.path.join(img_dir, "[Goc]_Figure_2.16_Khao_sat_thuc_nghiem_L_I_V_va_dao_ham_vi_phan.png")
fig_goc_2_17 = os.path.join(img_dir, "[Goc]_Figure_2.17_Dac_tuyen_L_I_V_va_dao_ham_VCSEL_suy_hao_nhiet.png")
fig_sim_2_8a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.8_Trich_Xuat_Hieu_Suat_Noi_Va_Ton_Hao.png")
fig_sim_2_8b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.8_Dac_Tuyen_L_I_V_Va_Dao_Ham_Vi_Phan.png")


def build_monograph_muc_2_8():
    print(f"Building monograph PDF: {pdf_filename}...")
    doc = he.BookmarkDocTemplate(pdf_filename)
    styles = he.get_hust_styles()
    styles["BodyText"] = styles["Body"]
    story = []

    def add_p(text, style_name="Body"):
        p = he.Paragraph(he.wrap_math_glyphs(text), styles[style_name])
        p.keepWithNext = False
        story.append(p)

    def add_spacer(height_pt=8):
        story.append(he.Spacer(1, height_pt))

    # =========================================================================
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.8
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.8: Đặc trưng hóa thực nghiệm diode laser thực tế (Characterizing Real Diode Lasers)", "H2")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Kỹ thuật Đo đạc Thực nghiệm Lab &amp; Trích xuất Tham số"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 52–61)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Sze (Ch. 12) &amp; Casey &amp; Panish (Vol. B)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.8 (Chương 2)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Quy chuẩn:</b> Độc lập tự chứa (1 Mục = 1 File PDF)"), styles["TableCell"])],
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.8 đúc kết các phương pháp đo đạc và giao thức phân tích thực nghiệm "
        "tiêu chuẩn trong phòng thí nghiệm nghiên cứu và dây chuyền chế tạo công nghiệp diode laser "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 52–61). "
        "Nội dung chuyên khảo triển khai sâu 3 Luận điểm Vi mô (MPT): "
        "(1) Phương pháp phân tích cụm chiều dài hốc (Cavity-Length Series Analysis), "
        "đồ thị tuyến tính nghịch đảo hiệu suất <i>η<sub>d</sub></i><sup>−1</sup> theo <i>L</i> để trích xuất hiệu suất tiêm nội <i>η<sub>i</sub></i> "
        "và hệ số tổn hao quang học nội ⟨<i>α<sub>i</sub></i>⟩; "
        "(2) Đặc trưng hóa nhiệt động học, mô hình tản nhiệt hình học 1D/2D/3D, "
        "điện trở nhiệt <i>R</i><sub>th</sub> và định luật nhiệt độ thực nghiệm Pankove (<i>T</i><sub>0</sub>, <i>T</i><sub>1</sub>); "
        "và (3) Kỹ thuật đo đồng thời <i>L</i>–<i>I</i>–<i>V</i>, "
        "chẩn đoán bước nhảy rơi sụt của đạo hàm tiếp giáp <i>I · R</i><sub>diff</sub> tại ngưỡng, "
        "và phương pháp trích xuất điện trở nối tiếp <i>R<sub>s</sub></i> phục vụ kiểm định chất lượng wafer."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.8
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.8.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Trích xuất <i>η<sub>i</sub></i> &amp; ⟨<i>α<sub>i</sub></i>⟩ từ chuỗi <i>L</i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>η<sub>d</sub></i><sup>−1</sup> = <i>η<sub>i</sub></i><sup>−1</sup> + [⟨<i>α<sub>i</sub></i>⟩ · (<i>η<sub>i</sub></i> ln <i>R</i><sup>−1</sup>)<sup>−1</sup>] · <i>L</i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.13, 2.14 &amp; Mô phỏng hồi quy <i>L</i>"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.8.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Đặc trưng hóa nhiệt động học &amp; Trở kháng <i>R</i><sub>th</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>R</i><sub>th</sub> = ln(4<i>h · w</i><sup>−1</sup>) · (<i>π K<sub>s</sub> L</i>)<sup>−1</sup>, <i>I</i><sub>th</sub>(<i>T</i>) ∝ exp(Δ<i>T · T</i><sub>0</sub><sup>−1</sup>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.15 (Mô hình tản nhiệt 1D/2D/3D)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.8.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Đo vi phân <i>L</i>–<i>I</i>–<i>V</i> &amp; Đạo hàm tiếp giáp"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Δ(<i>I · R</i><sub>diff</sub>) = −<i>n</i><sub>ideal</sub> <i>k<sub>B</sub> T · q</i><sup>−1</sup> tại <i>I</i> = <i>I</i><sub>th</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.16, 2.17 &amp; Mô phỏng bước nhảy vi phân"), styles["TableCellCenter"]),
        ],
    ]
    matrix_t = he.Table(matrix_rows, colWidths=[70.0, 150.0, 160.0, he.PRINTABLE_WIDTH - 380.0])
    matrix_t.setStyle(he.TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#002B49')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CED4DA')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(matrix_t)
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.8.1: PHƯƠNG PHÁP TRÍCH XUẤT eta_i VÀ <alpha_i>
    # =========================================================================
    add_p("Luận điểm 2.8.1: Phương pháp đo đạc trích xuất hiệu suất tiêm nội và tổn hao nội", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu phương pháp phân tích chuỗi chiều dài hốc và nguyên lý cô lập thông số", "H3")
    add_p(
        "Hiệu suất lượng tử vi phân <i>η<sub>d</sub></i> đo được tại hai mặt gương là một đại lượng tổng hợp, "
        "bị chi phối đồng thời bởi chất lượng tiếp xúc p-n (hiệu suất tiêm nội <i>η<sub>i</sub></i>) "
        "và phẩm chất dẫn sóng quang học (hệ số tổn hao nội ⟨<i>α<sub>i</sub></i>⟩). "
        "Để bóc tách độc lập hai thông số cốt lõi này mà không cần phá hủy linh kiện, "
        "phòng thí nghiệm thực hiện quy trình chuẩn: chế tạo một thanh laser (laser bar) "
        "chứa nhiều diode giống hệt nhau về cấu trúc mặt cắt ngang nhưng được chẻ với các chiều dài hốc <i>L</i> khác nhau "
        "(thường từ 250 μm đến 1500 μm). "
        "Bằng cách đo đặc tuyến <i>P</i>–<i>I</i> của từng linh kiện ở chế độ xung đẳng nhiệt, "
        "kỹ sư thu được tập hợp các giá trị <i>η<sub>d</sub></i> tương ứng với từng chiều dài <i>L</i>. "
        "Khi biểu diễn nghịch đảo hiệu suất <i>η<sub>d</sub></i><sup>−1</sup> theo biến số <i>L</i>, "
        "toàn bộ các điểm đo thực nghiệm sẽ phân bố thẳng hàng trên một đường tuyến tính tuyệt đối, "
        "cho phép trích xuất trực tiếp <i>η<sub>i</sub></i> và ⟨<i>α<sub>i</sub></i>⟩."
    )
    add_spacer(8)

    # Embed Hình gốc 2.13 và 2.14
    story.append(he.embed_figure_with_caption(
        fig_goc_2_13,
        "Hình 2.13: Đồ thị nghịch đảo hiệu suất lượng tử vi sai ngoài theo chiều dài hốc <i>L</i> (Coldren &amp; Corzine, trang 53). "
        "Ba mắt xích thực nghiệm: (a) Điểm ngoại suy tại trục tung <i>L</i> = 0 xác lập trực tiếp <i>η<sub>i</sub></i><sup>−1</sup>; "
        "(b) Độ dốc của đường thẳng tỉ lệ với hệ số tổn hao quang học nội ⟨<i>α<sub>i</sub></i>⟩; "
        "(c) Sự phân tán cực nhỏ của các điểm đo khẳng định tính đồng nhất cao của công nghệ epitaxy.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_2_14,
        "Hình 2.14: Khảo sát thực nghiệm mật độ dòng ngưỡng <i>J</i><sub>th</sub> và độ lợi mode theo chiều dài hốc của laser InGaAs/GaAs (Coldren &amp; Corzine, trang 54). "
        "Ba mắt xích vật lý: (a) <i>J</i><sub>th</sub> tăng vọt ở vùng hốc ngắn dưới 300 μm; "
        "(b) Độ lợi mode cân bằng chính xác với tổng tổn hao; "
        "(c) Trích xuất mật độ dòng trong suốt <i>J</i><sub>tr</sub> từ đồ thị hàm logarit.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ tuyến tính hóa nghịch đảo hiệu suất", "H3")
    add_p(
        "Phương trình hồi quy tuyến tính chuẩn mực xác lập mối liên hệ giữa hiệu suất vi phân và chiều dài hốc:"
    )

    pillar_eq_2_8_1 = r"\frac{1}{\eta_d} = \frac{1}{\eta_i} \left[1 + \frac{\langle\alpha_i\rangle}{\alpha_m}\right] = \frac{1}{\eta_i} + \left[\frac{\langle\alpha_i\rangle}{\eta_i \ln(1/R)}\right] L"
    nom_data_2_8_1 = [
        {"name": "Nghịch đảo hiệu suất vi phân ngoài", "symbol": "<i>η<sub>d</sub></i><sup>−1</sup>", "unit": "không thứ nguyên", "meaning": "Tỷ số hạt tải tiêm trên photon hữu ích thoát qua gương"},
        {"name": "Hiệu suất tiêm nội tại tiếp giáp", "symbol": "<i>η<sub>i</sub></i>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ hạt tải tiêm tái hợp bức xạ trong vùng giếng lượng tử (trích xuất tại <i>L</i> = 0)"},
        {"name": "Hệ số tổn hao quang học nội", "symbol": "⟨<i>α<sub>i</sub></i>⟩", "unit": "cm<sup>−1</sup>", "meaning": "Tổn hao do hấp thụ hạt tải tự do và tán xạ thô ráp mép dẫn sóng (tính từ độ dốc)"},
        {"name": "Hệ số phản xạ công suất gương", "symbol": "<i>R</i>", "unit": "không thứ nguyên", "meaning": "Độ phản xạ mặt gương chẻ tự nhiên tinh thể bán dẫn (<i>R</i> ≈ 0,32)"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_8_1, nom_data_2_8_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phương trình hồi quy tuyến tính", "H3")
    add_p("Dẫn xuất tường minh phương trình tuyến tính từ định nghĩa hiệu suất trích xuất:")

    eq_deriv_2_8_1a = r"\eta_d = \eta_i \frac{\alpha_m}{\langle\alpha_i\rangle + \alpha_m} \implies \frac{1}{\eta_d} = \frac{1}{\eta_i} \frac{\langle\alpha_i\rangle + \alpha_m}{\alpha_m}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi nghịch đảo hiệu suất vi phân ngoài:", eq_deriv_2_8_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_8_1b = r"\frac{1}{\eta_d} = \frac{1}{\eta_i} \left[1 + \frac{\langle\alpha_i\rangle}{\alpha_m}\right] = \frac{1}{\eta_i} + \frac{\langle\alpha_i\rangle}{\eta_i} \frac{1}{\alpha_m}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tách thành phần đơn vị và tỷ số tổn hao nội trên tổn hao gương:", eq_deriv_2_8_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_8_1c = r"\alpha_m = \frac{1}{L}\ln\left(\frac{1}{R}\right) \implies \frac{1}{\alpha_m} = \frac{L}{\ln(1/R)} \implies \frac{1}{\eta_d} = \frac{1}{\eta_i} + \left[\frac{\langle\alpha_i\rangle}{\eta_i \ln(1/R)}\right] L"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tuyến tính hóa hoàn toàn theo biến số chiều dài hốc L:", eq_deriv_2_8_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Hệ thức giải tích trên là công cụ kinh điển nhất để đánh giá phẩm chất công nghệ chế tạo: "
        "<br/>• Giao điểm trục tung (khi ngoại suy <i>L</i> → 0) tương ứng với trạng thái lý tưởng tổn hao gương vô hạn <i>α<sub>m</sub></i> → ∞, "
        "khi đó 100% photon sinh ra đều thoát ra ngoài hốc lập tức mà không bị hấp thụ nội, "
        "giúp đo lường trực tiếp giá trị thực của hiệu suất tiêm nội <i>η<sub>i</sub></i>. "
        "<br/>• Độ dốc của đường hồi quy tỉ lệ thuận với ⟨<i>α<sub>i</sub></i>⟩: "
        "đường hồi quy càng nằm ngang (độ dốc càng nhỏ) chứng tỏ vật liệu có độ tinh khiết quang học càng cao, "
        "nồng độ pha tạp vùng bao hợp lý và chất lượng khắc vạch dẫn sóng nhẵn mịn."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.8a
    story.append(he.embed_figure_with_caption(
        fig_sim_2_8a,
        "Hình mô phỏng 2.8.1: Đường hồi quy tuyến tính thực nghiệm trích xuất <i>η<sub>i</sub></i> và ⟨<i>α<sub>i</sub></i>⟩ của chuỗi laser InGaAs/GaAs ở 300 K. "
        "Từ dữ liệu đo đạc tại 5 chiều dài hốc từ 250 μm đến 1000 μm, phép hồi quy ngoại suy điểm cắt trục tung "
        "xác định <i>η<sub>i</sub></i> = 81,6% và độ dốc xác định tổn hao nội ⟨<i>α<sub>i</sub></i>⟩ = 7,6 cm<sup>−1</sup>.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận chiều dài hốc và bẫy sai số thực nghiệm", "H3")
    add_p(
        "Khảo sát các hiện tượng sai lệch trong phòng thí nghiệm: "
        "<br/>1. <b>Bẫy đo ở hốc quá ngắn (<i>L</i> < 200 μm):</b> Các điểm đo thực tế thường bị trôi dạt lệch lên phía trên đường hồi quy thẳng. "
        "Nguyên nhân vi mô: ở hốc rất ngắn, dòng ngưỡng bùng nổ đẩy mật độ hạt tải ngưỡng <i>N</i><sub>th</sub> lên rất cao, "
        "kích hoạt hiện tượng tái hợp Auger (<i>C N</i><sup>3</sup>) và rò rỉ hạt tải qua rào thế (Carrier Leakage), "
        "làm hiệu suất tiêm nội <i>η<sub>i</sub></i> bị suy giảm cục bộ. "
        "<br/>2. <b>Bẫy đo ở chế độ liên tục CW:</b> Nếu đo bằng dòng một chiều DC thay vì xung ngắn, "
        "nhiệt lượng tích tụ trên các linh kiện hốc ngắn sẽ lớn hơn hốc dài do mật độ dòng cao hơn, "
        "làm sai lệch độ dốc của đường thẳng và dẫn đến việc đánh giá sai lệch tổn hao nội ⟨<i>α<sub>i</sub></i>⟩."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.8.2: ĐẶC TRƯNG HÓA NHIỆT ĐỘNG HỌC & TRỞ KHÁNG NHIỆT
    # =========================================================================
    add_p("Luận điểm 2.8.2: Đặc trưng hóa nhiệt động học và Mô hình tản nhiệt hình học 1D, 2D, 3D", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm trở kháng nhiệt và các cơ chế lan truyền nhiệt lượng trong chip", "H3")
    add_p(
        "Nhiệt lượng là kẻ thù số một của linh kiện bán dẫn quang điện tử. "
        "Toàn bộ công suất điện cấp vào không chuyển hóa thành ánh sáng (<i>P</i><sub>diss</sub> = <i>I · V − P</i><sub>0</sub>) "
        "đều bị biến thành nhiệt lượng tập trung tại vùng tích cực có thể tích siêu nhỏ (chỉ vài micromet khối). "
        "Nhiệt lượng này phải được truyền dẫn qua lớp bán dẫn dày hàng trăm micromet để thoát xuống đế tản nhiệt kim loại (Heat Sink). "
        "Đặc trưng hóa nhiệt động học nghiên cứu trở kháng nhiệt <i>R</i><sub>th</sub> (đơn vị K·W<sup>−1</sup>) "
        "và sự lan tỏa của dòng nhiệt theo các chiều không gian (Heat Spreading) từ dải hẹp 1D, "
        "lan tỏa góc mở 2D, đến khuếch tán bán cầu 3D."
    )
    add_spacer(8)

    # Embed Hình gốc 2.15
    story.append(he.embed_figure_with_caption(
        fig_goc_2_15,
        "Hình 2.15: Mô hình hình học dòng nhiệt 1D, 2D và 3D trong phiến bán dẫn diode laser (Coldren &amp; Corzine, trang 57). "
        "Ba mắt xích truyền nhiệt: (a) Dòng nhiệt 1D thẳng đứng khi nguồn nhiệt rộng bằng đế; "
        "(b) Dòng nhiệt 2D lan tỏa góc mở logarit từ dải hẹp vùng tích cực; "
        "(c) Dòng nhiệt 3D bán cầu cho các cấu hình tiếp xúc điểm hoặc laser VCSEL diện tích nhỏ.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ trở kháng nhiệt và định luật Pankove", "H3")
    add_p(
        "Biểu thức giải tích của điện trở nhiệt lan tỏa 2D và định luật suy thoái nhiệt Pankove:"
    )

    pillar_eq_2_8_2 = r"R_{\mathrm{th}} \approx \frac{\ln(4h/w)}{\pi K_s L}, \quad I_{\mathrm{th}}(T) = I_{\mathrm{th}}(T_{\mathrm{ref}}) \exp\left(\frac{T - T_{\mathrm{ref}}}{T_0}\right)"
    nom_data_2_8_2 = [
        {"name": "Điện trở nhiệt lan tỏa hình học", "symbol": "<i>R</i><sub>th</sub>", "unit": "K·W<sup>−1</sup>", "meaning": "Độ tăng nhiệt độ tiếp giáp trên một đơn vị công suất nhiệt tiêu tán"},
        {"name": "Độ dẫn nhiệt của đế bán dẫn", "symbol": "<i>K<sub>s</sub></i>", "unit": "W·cm<sup>−1</sup>·K<sup>−1</sup>", "meaning": "Hệ số dẫn nhiệt của vật liệu đế (GaAs ≈ 0,45; InP ≈ 0,68; Cu ≈ 4,0)"},
        {"name": "Khoảng cách từ nguồn nhiệt tới đế", "symbol": "<i>h</i>", "unit": "μm", "meaning": "Bề dày lớp bán dẫn giữa vùng tích cực và đế tản nhiệt"},
        {"name": "Nhiệt độ đặc trưng ngưỡng Pankove", "symbol": "<i>T</i><sub>0</sub>", "unit": "K", "meaning": "Đại lượng đo độ nhạy cảm của dòng ngưỡng theo nhiệt độ (càng lớn càng bền nhiệt)"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_8_2, nom_data_2_8_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phương trình lan truyền nhiệt logarit", "H3")
    add_p("Dẫn xuất tường minh điện trở nhiệt từ phương trình vi phân Fourier:")

    eq_deriv_2_8_2a = r"\nabla \cdot \left(K_s \nabla T\right) = 0 \implies \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phương trình Laplace truyền nhiệt trạng thái dừng trong môi trường đẳng hướng:", eq_deriv_2_8_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_8_2b = r"T(r) = \frac{P_{\mathrm{diss}}}{\pi K_s L} \ln\left(\frac{r_2}{r_1}\right) \implies R_{\mathrm{th}} = \frac{\Delta T}{P_{\mathrm{diss}}} = \frac{\ln(4h/w)}{\pi K_s L}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tích phân phân bố nhiệt độ theo góc mở hình học lan tỏa 2D:", eq_deriv_2_8_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_8_2c = r"\ln I_{\mathrm{th}}(T) = \ln I_{\mathrm{th}0} + \frac{T - T_{\mathrm{ref}}}{T_0} \implies T_0 = \left[\frac{\mathrm{d}\ln I_{\mathrm{th}}}{\mathrm{d}T}\right]^{-1}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phương pháp trích xuất thực nghiệm thông số nhiệt độ Pankove <i>T</i><sub>0</sub>:", eq_deriv_2_8_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Từ nghiệm giải tích <i>R</i><sub>th</sub>, ta rút ra hai kết luận công nghệ quyết định: "
        "<br/>1. Chiều dài hốc <i>L</i> nằm ở mẫu số: kéo dài hốc <i>L</i> làm tăng diện tích tiếp xúc với đế tản nhiệt, "
        "giúp hạ thấp trực tiếp điện trở nhiệt <i>R</i><sub>th</sub>. "
        "<br/>2. Bề dày <i>h</i> nằm trong hàm logarit: nếu đóng gói chip theo kiểu truyền thống (mặt p quay lên trên, p-side up), "
        "nhiệt lượng phải đi qua toàn bộ bề dày đế bán dẫn <i>h</i> ≈ 100–150 μm có độ dẫn nhiệt kém. "
        "Nếu chuyển sang kỹ thuật đóng gói tiên tiến (mặt p quay xuống dưới, p-side down), "
        "khoảng cách dẫn nhiệt <i>h</i> rút ngắn xuống chỉ còn vài micromet, "
        "làm điện trở nhiệt giảm 2 đến 3 lần, giải phóng công suất phát xạ của laser."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận nhiệt độ Pankove giữa các hệ vật liệu", "H3")
    add_p(
        "So sánh các hệ vật liệu bán dẫn: "
        "<br/>1. <b>Hệ vật liệu InGaAs/GaAs (bước sóng 980 nm):</b> Có hố thế lượng tử sâu (độ lệch dải dẫn Δ<i>E<sub>c</sub></i> lớn), "
        "ngăn chặn triệt để hạt tải nhiệt thoát ra ngoài rào thế, đạt <i>T</i><sub>0</sub> từ 120 K đến 180 K. "
        "Linh kiện có thể hoạt động bền bỉ ở nhiệt độ cao mà không cần bộ làm mát TEC. "
        "<br/>2. <b>Hệ vật liệu InGaAsP/InP (bước sóng 1310/1550 nm):</b> Có độ lệch dải dẫn nhỏ hơn và năng lượng vùng cấm hẹp, "
        "khiến quá trình tái hợp Auger không bức xạ gia tăng mãnh liệt theo nhiệt độ, làm <i>T</i><sub>0</sub> chỉ đạt 50–70 K. "
        "Khi nhiệt độ môi trường tăng từ 20 °C lên 60 °C, dòng ngưỡng tăng vọt gấp 2–3 lần, "
        "đòi hỏi hệ thống viễn thông phải trang bị mạch bù nhiệt điện tử hoặc bộ ổn nhiệt Peltier."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.8.3: ĐO VI PHÂN L-I-V VÀ ĐẠO HÀM TIẾP GIÁP
    # =========================================================================
    add_p("Luận điểm 2.8.3: Đo đạc vi phân L–I–V, Đạo hàm tiếp giáp và Chẩn đoán khuyết tật linh kiện", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu kỹ thuật đo vi sai L–I–V và cơ chế bộc lộ bước nhảy tiếp giáp", "H3")
    add_p(
        "Kỹ thuật đo đạc hiện đại không chỉ quan sát đường cong dòng – áp <i>I</i>–<i>V</i> hay công suất – dòng <i>L</i>–<i>I</i> thông thường, "
        "mà sử dụng các bộ khuếch đại khóa pha (Lock-in Amplifier) hoặc vi phân số liệu số học độ chính xác cao để tính toán "
        "đạo hàm tiếp giáp có trọng số: <i>I · R</i><sub>diff</sub> (đơn vị Volt). "
        "Dưới ngưỡng phát xạ, điện áp đặt lên hai cực diode tăng dần theo hàm logarit của dòng tiêm, "
        "do đó đạo hàm vi phân chứa thành phần điện áp nhiệt <i>n</i><sub>ideal</sub> <i>k<sub>B</sub> T · q</i><sup>−1</sup>. "
        "Đúng tại thời điểm phát laser (<i>I = I</i><sub>th</sub>), hiện tượng ghim mức Fermi (Fermi-level Clamping) xảy ra: "
        "điện áp tiếp giáp nội tại bị khóa cứng (đạo hàm thế tiếp giáp triệt tiêu bằng 0), "
        "khiến thành phần điện áp nhiệt lập tức biến mất hoàn toàn! "
        "Hệ quả là trên đường cong đạo hàm tiếp giáp xuất hiện một bước nhảy rơi sụt thẳng đứng sắc nét, "
        "tạo nên một dấu chỉ nhị phân hoàn hảo xác lập ngưỡng phát laser."
    )
    add_spacer(8)

    # Embed Hình gốc 2.16 và 2.17
    story.append(he.embed_figure_with_caption(
        fig_goc_2_16,
        "Hình 2.16: Khảo sát thực nghiệm đặc tuyến <i>L</i>–<i>I</i>–<i>V</i> và các đạo hàm vi phân của laser dị thể (Coldren &amp; Corzine, trang 59). "
        "Ba mắt xích đo đạc: (a) Đồ thị công suất quang <i>L</i> và điện áp <i>V</i>; "
        "(b) Bước nhảy rơi sụt sắc nét của đạo hàm tiếp giáp đúng tại dòng ngưỡng <i>I</i><sub>th</sub>; "
        "(c) Độ dốc của đường vi phân trên ngưỡng xác định chính xác điện trở tiếp xúc <i>R<sub>s</sub></i>.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    story.append(he.embed_figure_with_caption(
        fig_goc_2_17,
        "Hình 2.17: Đặc tuyến <i>L</i>–<i>I</i>–<i>V</i> và đạo hàm vi sai của laser phát xạ bề mặt hốc đứng VCSEL có suy hao nhiệt (Coldren &amp; Corzine, trang 60). "
        "Ba mắt xích chẩn đoán: (a) Điện áp ngưỡng cao hơn do điện trở gương DBR lớn; "
        "(b) Bước nhảy đạo hàm tiếp giáp bị nhòe nhẹ do phát xạ tự phát mạnh; "
        "(c) Hiện tượng uốn cong nhiệt Rollover xuất hiện sớm ở dòng bơm nhỏ.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ đạo hàm tiếp giáp", "H3")
    add_p(
        "Biểu thức giải tích của đạo hàm tiếp giáp có trọng số dưới và trên ngưỡng:"
    )

    pillar_eq_2_8_3 = r"I \frac{\mathrm{d}V}{\mathrm{d}I} = \begin{cases} \frac{n_{\mathrm{ideal}} k_B T}{q} + I R_s & (I < I_{\mathrm{th}}) \\ I R_s & (I \ge I_{\mathrm{th}}) \end{cases} \implies \Delta\left(I \frac{\mathrm{d}V}{\mathrm{d}I}\right) = -\frac{n_{\mathrm{ideal}} k_B T}{q}"
    nom_data_2_8_3 = [
        {"name": "Đạo hàm tiếp giáp có trọng số", "symbol": "<i>I · R</i><sub>diff</sub>", "unit": "V", "meaning": "Tích của dòng tiêm và điện trở vi phân toàn phần của diode"},
        {"name": "Hệ số lý tưởng tiếp giáp diode", "symbol": "<i>n</i><sub>ideal</sub>", "unit": "không thứ nguyên", "meaning": "Đặc trưng cho cơ chế tái hợp tiếp giáp (<i>n</i> ≈ 1 do phát xạ, <i>n</i> ≈ 2 do SRH)"},
        {"name": "Thế nhiệt tiếp giáp", "symbol": "<i>k<sub>B</sub> T · q</i><sup>−1</sup>", "unit": "V", "meaning": "Năng lượng nhiệt tương đương điện thế (≈ 25,85 mV ở 300 K)"},
        {"name": "Bước nhảy rơi sụt tại ngưỡng", "symbol": "Δ(<i>I · R</i><sub>diff</sub>)", "unit": "mV", "meaning": "Độ sâu sụt giảm đột ngột xác nhận sự khóa cứng mức Fermi giả"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_8_3, nom_data_2_8_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất bước nhảy vi phân và trích xuất điện trở nối tiếp", "H3")
    add_p("Dẫn xuất tường minh sự suy giảm của đạo hàm tiếp giáp từ hiện tượng kẹp chặt:")

    eq_deriv_2_8_3a = r"V(I) = V_j(I) + I R_s \implies \frac{\mathrm{d}V}{\mathrm{d}I} = \frac{\mathrm{d}V_j}{\mathrm{d}I} + R_s"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phân tách đạo hàm điện áp thành thành phần tiếp giáp và điện trở ohmic:", eq_deriv_2_8_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_8_3b = r"I < I_{\mathrm{th}}: I = I_0 \exp\left(\frac{q V_j}{n k_B T}\right) \implies \frac{\mathrm{d}V_j}{\mathrm{d}I} = \frac{n k_B T}{q I} \implies I \frac{\mathrm{d}V_j}{\mathrm{d}I} = \frac{n k_B T}{q}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu thức đạo hàm tiếp giáp dưới ngưỡng tuân theo định luật Shockley:", eq_deriv_2_8_3b, styles=styles))
    add_spacer(6)

    eq_deriv_2_8_3c = r"I \ge I_{\mathrm{th}}: V_j = \text{const} \implies \frac{\mathrm{d}V_j}{\mathrm{d}I} = 0 \implies I \frac{\mathrm{d}V}{\mathrm{d}I} = I R_s \implies \frac{\mathrm{d}}{\mathrm{d}I}\left(I \frac{\mathrm{d}V}{\mathrm{d}I}\right) = R_s"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Trên ngưỡng, đạo hàm tiếp giáp triệt tiêu và độ dốc đường vi phân bằng <i>R<sub>s</sub></i>:", eq_deriv_2_8_3c, styles=styles))
    add_spacer(8)

    add_p(
        "Chuỗi nhân quả dẫn xuất làm sáng tỏ giá trị chẩn đoán thực nghiệm tuyệt đối của phép đo: "
        "<br/>1. Độ sâu bước nhảy rơi sụt Δ(<i>I · R</i><sub>diff</sub>) bằng chính xác −<i>n</i><sub>ideal</sub> <i>k<sub>B</sub> T · q</i><sup>−1</sup> "
        "(khoảng −40 đến −55 mV ở 300 K). Nếu linh kiện không xuất hiện bước nhảy này, "
        "chứng tỏ độ lợi chưa đạt ngưỡng hoặc mật độ hạt tải chưa bị kẹp chặt (linh kiện bị lỗi chế tạo). "
        "<br/>2. Trên ngưỡng, đường cong vi phân <i>I · R</i><sub>diff</sub> trở thành một đường thẳng tuyến tính đi qua gốc tọa độ với độ dốc bằng đúng <i>R<sub>s</sub></i>. "
        "Nhờ đó, kỹ sư trích xuất được điện trở vi phân tiếp xúc <i>R<sub>s</sub></i> mà không bị ảnh hưởng bởi sụt áp phi tuyến của tiếp giáp p-n."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.8b
    story.append(he.embed_figure_with_caption(
        fig_sim_2_8b,
        "Hình mô phỏng 2.8.2: Đo đạc đồng thời công suất <i>P</i><sub>0</sub>, điện áp <i>V</i> và đạo hàm tiếp giáp <i>I · R</i><sub>diff</sub> của laser GaAs ở 300 K. "
        "Đồ thị tái hiện hoàn hảo bước nhảy rơi sụt sắc nét của đạo hàm tiếp giáp đúng tại dòng ngưỡng <i>I</i><sub>th</sub> = 20 mA, "
        "đồng thời xác định độ dốc tuyến tính trên ngưỡng tương ứng điện trở tiếp xúc <i>R<sub>s</sub></i> = 2,5 Ω.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận chẩn đoán khuyết tật wafer trong công nghiệp", "H3")
    add_p(
        "Ứng dụng trong kiểm định chất lượng sản xuất wafer hàng loạt: "
        "<br/>1. <b>Phát hiện tiếp xúc Ohmic kém:</b> Nếu độ dốc trên ngưỡng quá dốc, <i>R<sub>s</sub></i> lớn "
        "(vượt quá tiêu chuẩn thiết kế > 5 Ω đối với laser cạnh), chứng tỏ lớp hợp kim hóa kim loại tiếp xúc p-Ohmic bị oxy hóa "
        "hoặc nồng độ pha tạp lớp tiếp xúc p<sup>+</sup>-GaAs chưa đạt chuẩn (> 10<sup>19</sup> cm<sup>−3</sup>). "
        "<br/>2. <b>Phát hiện rò rỉ dòng cạnh (Shunt Leakage):</b> Nếu bước nhảy vi phân bị nhòe, "
        "độ sâu sụt giảm nhỏ hơn nhiều so với 40 mV, điều này cảnh báo dòng điện đang rò rỉ qua các kênh ký sinh mép rãnh cách ly, "
        "chưa tập trung 100% vào vùng giếng lượng tử trung tâm."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN & DỰ ĐOÁN LỖI SAI (BẪY ĐIỂM MÙ R&D)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")
    add_p(
        "Phần thử thách áp dụng phương pháp lập luận ba bước CER (Claim – Evidence – Reasoning) "
        "kết hợp mổ xẻ các tình huống đo đạc thực nghiệm phức tạp trong phòng sạch bán dẫn:"
    )
    add_spacer(8)

    cer_style = he.TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#002B49')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8F9FA')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#002B49')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ])

    cer_card_1 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.8.1: BẪY TRÍCH XUẤT HIỆU SUẤT TIÊM NỘI LỚN HƠN 100%</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống phản biện:</b> Trong quá trình đo đạc đồ thị 1/<i>η<sub>d</sub></i> theo <i>L</i>, "
            "một kỹ sư thực hiện hồi quy tuyến tính và thu được điểm cắt trục tung 1/<i>η<sub>i</sub></i> = 0,92, "
            "tương ứng với hiệu suất tiêm nội <i>η<sub>i</sub></i> = 108,7%. "
            "Kỹ sư này hào hứng báo cáo rằng công nghệ epitaxy mới đã phá vỡ giới hạn lượng tử. Nhận định này có đúng không?<br/>"
            "<b>1. Luận điểm (Claim):</b> Kết quả <i>η<sub>i</sub></i> > 100% là phi vật lý và hoàn toàn do sai số hệ thống trong phép đo công suất quang gây ra.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Về mặt nguyên lý đầu, hiệu suất tiêm <i>η<sub>i</sub></i> là xác suất hạt tải đi vào vùng tích cực (<i>η<sub>i</sub> ≤ 1</i>). "
            "Nguyên nhân trực tiếp: cảm biến đo công suất quang (Optical Power Meter) bị hiệu chuẩn sai hệ số đáp ứng (Responsivity <i>R<sub>λ</sub></i>), "
            "hoặc bộ thu quang tích hợp (Integrating Sphere) thu nhận cả ánh sáng phản xạ tán xạ từ đế kim loại làm công suất đo được cao giả tạo.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Ngoài ra, góc chẻ mặt gương của các hốc ngắn bị lệch so với mặt tinh thể (110) "
            "làm độ phản xạ <i>R</i> sụt giảm, kéo tổn hao gương tăng cao không kiểm soát, làm sai lệch độ dốc của chuỗi <i>L</i>. "
            "Cần hiệu chuẩn lại thiết bị đo quang bằng nguồn laser chuẩn và kiểm tra góc chẻ bằng kính hiển vi điện tử quét SEM."
        ), styles["TableCell"])]
    ]
    t1 = he.Table(cer_card_1, colWidths=[he.PRINTABLE_WIDTH])
    t1.setStyle(cer_style)
    story.append(t1)
    add_spacer(10)

    cer_card_2 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.8.2: TẠI SAO BƯỚC NHẢY ĐẠO HÀM TIẾP GIÁP CHÍNH XÁC HƠN ĐO QUANG L–I?</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống chẩn đoán:</b> Đối với các diode laser kích thước vi mô (Micro-lasers) hoặc laser hốc đứng VCSEL có hệ số ghép phát xạ tự phát cao "
            "(<i>β</i><sub>sp</sub> ≈ 10<sup>−2</sup> đến 10<sup>−1</sup>), đặc tuyến quang <i>L</i>–<i>I</i> chuyển tiếp rất êm dịu, "
            "không có điểm gãy sắc nét (Soft Turn-on), khiến việc xác định dòng ngưỡng quang học <i>I</i><sub>th</sub> bị sai lệch lớn. "
            "Tại sao phép đo đạo hàm tiếp giáp <i>I · R</i><sub>diff</sub> lại định vị ngưỡng chính xác vượt trội?<br/>"
            "<b>1. Luận điểm (Claim):</b> Phép đo đạo hàm <i>I · R</i><sub>diff</sub> phản ánh trực tiếp bản chất lượng tử của thế hóa học hạt tải (Mức Fermi giả), "
            "vốn bị khóa cứng đột ngột tại ngưỡng bất kể hiệu suất ghép phát xạ tự phát lớn đến mức nào.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Dù photon tự phát có lọt vào mode laser nhiều đến đâu, "
            "thì hiện tượng dao động phát laser dừng chỉ xảy ra khi độ lợi mode cân bằng chính xác với tổn hao: <i>Γ g</i> = ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>. "
            "Tại điểm cân bằng này, phương trình vi phân tốc độ hạt tải bắt buộc mật độ <i>N</i> phải bị ghim chặt, kéo theo hiệu số mức Fermi <i>E<sub>Fc</sub> − E<sub>Fv</sub> = q V<sub>j</sub></i> bị ghim cứng.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Sự khóa cứng của điện áp tiếp giáp <i>V<sub>j</sub></i> làm đạo hàm thế tiếp giáp triệt tiêu về 0 "
            "tạo ra bước nhảy rơi sụt rõ rệt, không phụ thuộc vào đường cong công suất quang bị làm mờ bởi phát xạ tự phát."
        ), styles["TableCell"])]
    ]
    t2 = he.Table(cer_card_2, colWidths=[he.PRINTABLE_WIDTH])
    t2.setStyle(cer_style)
    story.append(t2)
    add_spacer(10)

    cer_card_3 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.8.3: THIẾT KẾ GIẢI PHÁP TẢN NHIỆT CHO MODULE LASER 1550 nm CÔNG SUẤT</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống công nghệ:</b> Một module diode laser InGaAsP/InP 1550 nm công suất phát 50 mW "
            "bị hiện tượng uốn cong suy hao nhiệt Rollover ở nhiệt độ môi trường 50 °C do hệ số nhiệt độ Pankove thấp (<i>T</i><sub>0</sub> = 55 K). "
            "Đóng gói hiện tại sử dụng cấu hình truyền thống p-side up trên đế đồng với <i>R</i><sub>th</sub> = 45 K·W<sup>−1</sup>. "
            "Hãy đề xuất giải pháp kỹ thuật cụ thể để nâng cao công suất phát và đẩy mốc Rollover lên trên 80 °C.<br/>"
            "<b>1. Luận điểm (Claim):</b> Giải pháp tối ưu kết hợp: chuyển đổi đóng gói sang cấu hình hàn lật p-side down "
            "trên đế tản nhiệt phụ bằng kim cương nhân tạo CVD (hoặc AlN), kết hợp tối ưu hóa chiều dài hốc <i>L</i>.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Cấu hình p-side down đưa vùng tích cực tiếp xúc gần sát đế tản nhiệt qua lớp hàn AuSn mỏng (<i>h</i> ≈ 3 μm thay vì 120 μm). "
            "Kim cương CVD có độ dẫn nhiệt <i>K<sub>s</sub></i> ≈ 15–20 W·cm<sup>−1</sup>·K<sup>−1</sup> (gấp 30 lần đế InP và 5 lần đồng). "
            "Điện trở nhiệt <i>R</i><sub>th</sub> sẽ giảm từ 45 K·W<sup>−1</sup> xuống dưới 12 K·W<sup>−1</sup>.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Giảm <i>R</i><sub>th</sub> gần 4 lần làm độ dâng nhiệt tiếp giáp Δ<i>T</i> = <i>R</i><sub>th</sub> <i>P</i><sub>diss</sub> giảm 4 lần "
            "ở cùng một dòng bơm. Nhờ đó, dòng ngưỡng <i>I</i><sub>th</sub>(<i>T</i>) không bị bùng nổ hàm mũ theo định luật Pankove, "
            "triệt tiêu nguy cơ trôi dạt bước sóng và bảo toàn công suất phát xạ 50 mW ổn định ở nhiệt độ môi trường khắc nghiệt."
        ), styles["TableCell"])]
    ]
    t3 = he.Table(cer_card_3, colWidths=[he.PRINTABLE_WIDTH])
    t3.setStyle(cer_style)
    story.append(t3)
    add_spacer(14)

    # Lời kết luận học thuật
    conclusion_text = (
        "<b>KẾT LUẬN TOÀN CHƯƠNG 2:</b> Phương pháp tiếp cận hiện tượng luận đối với laser diode "
        "đã hoàn thành sứ mệnh thiết lập bức tranh vật lý hoàn chỉnh: từ cân bằng phát xạ tự phát dưới ngưỡng (Mục 2.2), "
        "quang học dẫn sóng và tổn hao gương hốc cộng hưởng (Mục 2.4), điều kiện kẹp chặt độ lợi ngưỡng (Mục 2.5), "
        "đặc tuyến công suất quang phát xạ và hiệu suất vi sai (Mục 2.6), động học điều chế cao tần (Mục 2.7), "
        "cho đến các kỹ thuật đặc trưng hóa thực nghiệm kiểm chứng tại Lab (Mục 2.8). "
        "Toàn bộ hệ thống 8 chuyên khảo Mục 2.1 đến 2.8 tạo thành một bách khoa toàn thư vi mô hoàn chỉnh, "
        "làm bệ phóng vững chắc cho các nghiên cứu chuyên sâu về vi cấu trúc giếng lượng tử và vi mạch quang tử tích hợp."
    )
    add_p(conclusion_text, "Body")
    add_spacer(10)

    # Build document
    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_8()

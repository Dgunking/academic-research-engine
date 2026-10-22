# -*- coding: utf-8 -*-
"""
gen_clean_2_6.py
Biên dịch Chuyên khảo Toàn văn Mục 2.6: Dòng ngưỡng và công suất bức xạ ngõ ra theo dòng tiêm
Coldren & Corzine, trang 41-48.
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

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.6.pdf")

# Hình ảnh gốc và mô phỏng
fig_goc_2_9 = os.path.join(img_dir, "[Goc]_Figure_2.9_Dac_tuyen_cong_suat_quang_theo_dong_P_I_laser_diode.png")
fig_goc_2_11 = os.path.join(img_dir, "[Goc]_Figure_2.11_Do_thi_3D_va_dong_muc_dong_dien_yeu_cau_10mW.png")
fig_sim_2_6a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.6_Dac_Tuyen_P_I_Va_Suy_Hao_Nhiet.png")
fig_sim_2_6b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.6_Toi_Uu_Hoa_Chieu_Dai_Hoc_Cho_Dong_10mW.png")


def build_monograph_muc_2_6():
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
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.6
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.6: Dòng ngưỡng và công suất bức xạ ngõ ra theo dòng tiêm (Threshold Current and Power Out vs. Injection Current)", "H2")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Đặc tuyến Công suất – Dòng tiêm &amp; Tối ưu hóa"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 41–48)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Sze (Ch. 12) &amp; Yariv (Ch. 15)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.6 (Chương 2)"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.6 giải phẫu mối quan hệ giữa công suất phát xạ quang học "
        "ngõ ra và dòng điện tiêm bơm vào diode laser (đặc tuyến <i>L</i>–<i>I</i> hay <i>P</i>–<i>I</i>) "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 41–48). "
        "Nội dung chuyên khảo triển khai sâu 3 Luận điểm Vi mô (MPT): "
        "(1) Đặc tuyến công suất quang ngõ ra <i>P</i><sub>0</sub>(<i>I</i>), hiệu suất lượng tử vi sai <i>η<sub>d</sub></i>, "
        "độ dốc hiệu suất <i>SE</i>, và sự phân chia công suất qua hai mặt gương phản xạ; "
        "(2) Bài toán tối ưu hóa chiều dài hốc cộng hưởng <i>L</i> và cấu hình phủ gương chọn lọc (AR–HR) "
        "để đạt công suất quang mục tiêu (10 mW) với dòng tiêu thụ tối thiểu; "
        "và (3) Hiệu suất chuyển đổi năng lượng toàn phần (Wall-Plug Efficiency <i>η<sub>c</sub></i>), "
        "điện trở tiếp xúc nối tiếp <i>R<sub>s</sub></i>, sự suy hao nhiệt (Thermal Rollover) và điều kiện vận hành tối ưu."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.6
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.6.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Đặc tuyến <i>P</i>–<i>I</i> &amp; Hiệu suất vi phân <i>η<sub>d</sub></i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>P</i><sub>0</sub> = <i>η<sub>d</sub> · hν · q</i><sup>−1</sup> (<i>I − I</i><sub>th</sub>), <i>η<sub>d</sub> = η<sub>i</sub> · α<sub>m</sub> · α</i><sub>tot</sub><sup>−1</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.9 &amp; Mô phỏng <i>P</i><sub>0</sub>(<i>I</i>) suy hao nhiệt"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.6.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Tối ưu hóa hốc <i>L</i> &amp; Phủ gương AR–HR cho 10 mW"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>I</i><sub>req</sub> = <i>I</i><sub>th</sub>(<i>L</i>) + <i>P</i><sub>0</sub> · [<i>SE(L)</i>]<sup>−1</sup>, cực tiểu tại <i>L</i><sub>opt</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.11 &amp; Mô phỏng quét <i>L</i> cho 10 mW"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.6.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hiệu suất Wall-Plug &amp; Điểm làm việc tối ưu"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>η<sub>c</sub> = P</i><sub>0</sub> · [<i>I (V<sub>j</sub> + I R<sub>s</sub>)</i>]<sup>−1</sup>, cực đại tại <i>I</i><sub>opt</sub> ≈ 2–3 <i>I</i><sub>th</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô hình giải tích &amp; Bẫy điểm mù R&amp;D CER"), styles["TableCellCenter"]),
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
    # LUẬN ĐIỂM 2.6.1: ĐẶC TUYẾN P-I VÀ HIỆU SUẤT LƯỢNG TỬ VI PHÂN
    # =========================================================================
    add_p("Luận điểm 2.6.1: Đặc tuyến công suất quang theo dòng tiêm P–I và Hiệu suất lượng tử vi phân", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm, bước nhảy độ dốc tại ngưỡng và sự phân chia photon qua hai gương", "H3")
    add_p(
        "Dưới ngưỡng phát xạ (<i>I</i> < <i>I</i><sub>th</sub>), diode laser hoạt động như một LED thông thường: "
        "bức xạ hoàn toàn do tái hợp tự phát không kết hợp điều khiển, "
        "photon phát xạ đẳng hướng vào không gian 4π steradian với hiệu suất lượng tử vi phân cực thấp (chỉ khoảng 0,5–1%). "
        "Khi dòng tiêm vượt qua dòng ngưỡng <i>I</i><sub>th</sub>, hiện tượng bức xạ kích thích bùng nổ, "
        "đặc tuyến <i>P</i>–<i>I</i> xuất hiện một điểm bẻ gập sắc nét (kink). "
        "Trên ngưỡng, toàn bộ lượng dòng tiêm gia tăng (<i>I</i> − <i>I</i><sub>th</sub>) được chuyển hóa gần như hoàn toàn "
        "thành thông lượng photon kết hợp định hướng đơn mode, khiến công suất ngõ ra tăng vọt theo một đường thẳng tuyến tính dốc đứng."
    )
    add_spacer(8)

    # Embed Hình gốc 2.9
    story.append(he.embed_figure_with_caption(
        fig_goc_2_9,
        "Hình 2.9: Đặc tuyến công suất quang ngõ ra theo dòng tiêm <i>P</i>–<i>I</i> của diode laser (Coldren &amp; Corzine, trang 41). "
        "Ba mắt xích động học: (a) Dưới ngưỡng <i>I</i> < <i>I</i><sub>th</sub>, phát xạ tự phát LED có công suất không đáng kể; "
        "(b) Điểm bẻ gập ngưỡng <i>I</i><sub>th</sub> phân tách hai chế độ lượng tử; "
        "(c) Trên ngưỡng <i>I</i> > <i>I</i><sub>th</sub>, công suất quang tăng tuyến tính với độ dốc tỉ lệ trực tiếp với hiệu suất vi phân <i>η<sub>d</sub></i>.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ công suất phát xạ trên ngưỡng", "H3")
    add_p(
        "Phương trình giải tích chuẩn mực xác định công suất quang ngõ ra toàn phần phát qua gương:"
    )

    pillar_eq_2_6_1 = r"P_0 = \eta_d \frac{h\nu}{q} (I - I_{\mathrm{th}}), \quad \eta_d = \eta_i \frac{\alpha_m}{\langle\alpha_i\rangle + \alpha_m} = \eta_i \frac{\alpha_m}{\alpha_{\mathrm{tot}}}"
    nom_data_2_6_1 = [
        {"name": "Công suất quang phát xạ hữu ích", "symbol": "<i>P</i><sub>0</sub>", "unit": "W (hoặc mW)", "meaning": "Tổng thông lượng photon kết hợp thoát qua các mặt gương hốc cộng hưởng"},
        {"name": "Hiệu suất lượng tử vi phân", "symbol": "<i>η<sub>d</sub></i>", "unit": "không thứ nguyên", "meaning": "Xác suất một hạt tải tiêm vượt ngưỡng sinh ra một photon thoát ra ngoài hốc"},
        {"name": "Dòng điện ngưỡng phát laser", "symbol": "<i>I</i><sub>th</sub>", "unit": "A (hoặc mA)", "meaning": "Dòng tiêm tối thiểu bắt đầu xuất hiện bức xạ kích thích kết hợp"},
        {"name": "Độ dốc hiệu suất phát xạ", "symbol": "<i>SE</i>", "unit": "W·A<sup>−1</sup> (hoặc mW·mA<sup>−1</sup>)", "meaning": "Tỷ số vi phân giữa biến thiên công suất và biến thiên dòng tiêm trên ngưỡng"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_6_1, nom_data_2_6_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất công suất ngõ ra từ thông lượng photon qua gương", "H3")
    add_p("Dẫn xuất tường minh biểu thức công suất quang từ phương trình trạng thái dừng:")

    eq_deriv_2_6_1a = r"P_0 = v_g \alpha_m h\nu S V_{\mathrm{mode}} = v_g \alpha_m h\nu \left[\frac{\eta_i (I - I_{\mathrm{th}})}{q v_g g_{\mathrm{th}} V_{\mathrm{mode}}}\right] V_{\mathrm{mode}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi công suất từ thông lượng photon thoát qua gương:", eq_deriv_2_6_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_6_1b = r"P_0 = \eta_i \frac{\alpha_m}{\Gamma g_{\mathrm{th}}} \frac{h\nu}{q} (I - I_{\mathrm{th}}) = \eta_i \frac{\alpha_m}{\langle\alpha_i\rangle + \alpha_m} \frac{h\nu}{q} (I - I_{\mathrm{th}})"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thế điều kiện cân bằng ngưỡng <i>Γ g</i><sub>th</sub> = ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>:", eq_deriv_2_6_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_6_1c = r"F_1 = \frac{1 - R_1}{(1 - R_1) + \sqrt{\frac{R_1}{R_2}}(1 - R_2)} \implies P_1 = F_1 P_0, \quad P_2 = (1 - F_1) P_0"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phân bố tỷ trọng công suất thoát ra ở hai mặt gương bất đối xứng <i>R</i><sub>1</sub> ≠ <i>R</i><sub>2</sub>:", eq_deriv_2_6_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Từ hệ thức dẫn xuất, ta nhận thấy hiệu suất lượng tử vi phân <i>η<sub>d</sub></i> là tích của hai xác suất độc lập: "
        "<br/>1. Hiệu suất tiêm nội <i>η<sub>i</sub></i>: Xác suất hạt tải đi vào đúng vùng tích cực và tái hợp bức xạ kích thích. "
        "<br/>2. Hiệu suất trích xuất quang học <i>α<sub>m</sub> · (⟨α<sub>i</sub>⟩ + α<sub>m</sub>)</i><sup>−1</sup>: "
        "Tỷ số giữa tổn hao gương hữu ích <i>α<sub>m</sub></i> và tổng tổn hao toàn phần <i>α</i><sub>tot</sub>. "
        "Khi tổn hao nội ⟨<i>α<sub>i</sub></i>⟩ càng nhỏ so với <i>α<sub>m</sub></i>, "
        "gần như 100% photon sinh ra đều thoát ra ngoài làm ánh sáng hữu ích, đưa <i>η<sub>d</sub></i> tiệm cận <i>η<sub>i</sub></i>."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.6a
    story.append(he.embed_figure_with_caption(
        fig_sim_2_6a,
        "Hình mô phỏng 2.6.1: Đặc tuyến công suất quang <i>P</i><sub>0</sub>(<i>I</i>) của diode laser InGaAs/GaAs 980 nm ở các nhiệt độ vận hành 20 °C và 60 °C. "
        "Đồ thị chỉ rõ điểm bẻ gập tại dòng ngưỡng <i>I</i><sub>th</sub> = 20 mA, độ dốc tuyến tính <i>SE</i> = 0,73 W·A<sup>−1</sup>, "
        "sự dịch chuyển ngưỡng khi nhiệt độ tăng cao, và hiện tượng uốn cong bão hòa suy hao nhiệt (Thermal Rollover) ở dòng bơm cực lớn.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận nhiệt độ và cơ chế suy hao nhiệt Rollover", "H3")
    add_p(
        "Khảo sát các vùng vận hành thực tế: "
        "<br/>1. <b>Vùng dòng làm việc danh định (<i>I</i><sub>th</sub> < <i>I</i> < 4 <i>I</i><sub>th</sub>):</b> "
        "Đặc tuyến giữ độ tuyến tính cao, thích hợp cho điều chế tín hiệu analog hoặc số trong viễn thông cáp quang. "
        "<br/>2. <b>Vùng quá tải nhiệt (Thermal Rollover):</b> Khi tăng dòng bơm lên rất cao, "
        "công suất tiêu tán Joule trong điện trở tiếp xúc <i>P</i><sub>diss</sub> = <i>I · V</i> − <i>P</i><sub>0</sub> "
        "đốt nóng phiến bán dẫn làm nhiệt độ lớp tiếp giáp tăng thêm Δ<i>T</i> = <i>R</i><sub>th</sub> <i>P</i><sub>diss</sub>. "
        "Nhiệt độ dâng cao khiến dòng ngưỡng tăng theo quy luật hàm mũ <i>I</i><sub>th</sub>(<i>T</i>) "
        "và độ dốc hiệu suất suy giảm <i>SE</i>(<i>T</i>), làm đường cong <i>P</i>–<i>I</i> bị uốn cong, đạt đỉnh cực đại "
        "rồi sụt giảm nhanh chóng. Kỹ sư quang điện tử bắt buộc phải thiết kế bộ tản nhiệt (Heat Sink) "
        "hoặc làm mát bằng bộ điều nhiệt TEC để đẩy mốc Rollover ra xa dải công tác."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.6.2: TỐI ƯU HÓA CHIỀU DÀI HỐC VÀ PHỦ GƯƠNG CHỌN LỌC
    # =========================================================================
    add_p("Luận điểm 2.6.2: Tối ưu hóa chiều dài hốc và Cấu hình phủ gương chọn lọc cho công suất mục tiêu", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm bài toán tối ưu
    add_p("Giai đoạn 1: Giới thiệu bài toán đánh đổi giữa dòng ngưỡng và hiệu suất trích xuất gương", "H3")
    add_p(
        "Trong thiết kế module phát laser công suất cố định (ví dụ phát 10 mW cho đầu đọc quang hoặc phát 500 mW cho bơm EDFA), "
        "mục tiêu cốt lõi của kỹ sư là cực tiểu hóa dòng điện tiêm <i>I</i> cần thiết từ bộ nguồn DC. "
        "Bài toán này chứa đựng một sự đánh đổi sâu sắc giữa dòng ngưỡng <i>I</i><sub>th</sub> và hiệu suất vi phân <i>η<sub>d</sub></i>: "
        "Nếu thiết kế hốc quá ngắn, tổn hao gương <i>α<sub>m</sub></i> lớn giúp hiệu suất vi sai <i>η<sub>d</sub></i> rất cao, "
        "nhưng mật độ hạt tải ngưỡng <i>N</i><sub>th</sub> bị đẩy vọt lên cao khiến dòng ngưỡng <i>I</i><sub>th</sub> bùng nổ; "
        "ngược lại, nếu thiết kế hốc quá dài, dòng ngưỡng trên đơn vị thể tích giảm nhưng thể tích hốc <i>V</i> quá lớn "
        "đồng thời tổn hao nội ⟨<i>α<sub>i</sub></i>⟩ nuốt trọn ánh sáng, làm hiệu suất vi phân suy kiệt."
    )
    add_spacer(8)

    # Embed Hình gốc 2.11
    story.append(he.embed_figure_with_caption(
        fig_goc_2_11,
        "Hình 2.11: Đồ thị đường đồng mức và bề mặt 3D của dòng điện yêu cầu để phát 10 mW theo chiều dài hốc <i>L</i> và độ phản xạ gương (Coldren &amp; Corzine, trang 46). "
        "Ba mắt xích thiết kế: (a) Miền cực tiểu dòng điện tạo thành thung lũng lòng chảo trên không gian tham số; "
        "(b) Đường biên dốc đứng ở vùng hốc ngắn do bùng nổ mật độ ngưỡng; "
        "(c) Đường dốc thoải ở vùng hốc dài do suy giảm hiệu suất lượng tử vi sai.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ dòng điện yêu cầu", "H3")
    add_p(
        "Biểu thức giải tích của dòng điện bơm cần thiết để tạo ra công suất quang xác định <i>P</i><sub>0</sub>:"
    )

    pillar_eq_2_6_2 = r"I_{\mathrm{req}} = I_{\mathrm{th}} + \frac{P_0}{SE} = \frac{q V}{\eta_i} R(N_{\mathrm{th}}) + \frac{P_0}{\eta_i \frac{\alpha_m}{\langle\alpha_i\rangle + \alpha_m} F_1 \frac{h\nu}{q}}"
    nom_data_2_6_2 = [
        {"name": "Dòng điện yêu cầu cho công suất mục tiêu", "symbol": "<i>I</i><sub>req</sub>", "unit": "mA", "meaning": "Dòng tiêm cấp từ nguồn nuôi để linh kiện phát ra đúng công suất <i>P</i><sub>0</sub>"},
        {"name": "Công suất mục tiêu thiết kế", "symbol": "<i>P</i><sub>0</sub>", "unit": "mW", "meaning": "Mức công suất quang phát xạ mong muốn tại mặt gương chính (ví dụ 10 mW)"},
        {"name": "Hệ số định hướng mặt gương ngõ ra", "symbol": "<i>F</i><sub>1</sub>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ thông lượng photon phát qua mặt gương trước so với tổng cả hai gương"},
        {"name": "Thể tích tích cực giam giữ hạt tải", "symbol": "<i>V</i>", "unit": "cm<sup>3</sup>", "meaning": "Thể tích hình học <i>V = w · d · L</i> của vùng giếng lượng tử"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_6_2, nom_data_2_6_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất sự phụ thuộc phi tuyến của dòng điện theo chiều dài hốc", "H3")
    add_p("Dẫn xuất tường minh sự đánh đổi hai số hạng cấu thành dòng điện yêu cầu:")

    eq_deriv_2_6_2a = r"I_{\mathrm{th}}(L) = \frac{q w d L}{\eta_i} \left[A N_{\mathrm{th}}(L) + B N_{\mathrm{th}}(L)^2 + C N_{\mathrm{th}}(L)^3\right]"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Dòng ngưỡng tăng theo thể tích hốc nhưng chịu số mũ phụ thuộc tổn hao gương:", eq_deriv_2_6_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_6_2b = r"N_{\mathrm{th}}(L) = N_{\mathrm{tr}} \exp\left(\frac{\langle\alpha_i\rangle + \frac{1}{2L}\ln\frac{1}{R_1 R_2}}{\Gamma g_0}\right)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mật độ ngưỡng bùng nổ theo hàm mũ khi L co ngắn:", eq_deriv_2_6_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_6_2c = r"\Delta I_{\mathrm{power}}(L) = \frac{P_0}{SE(L)} = \frac{P_0}{F_1 \eta_i \frac{h\nu}{q}} \left[1 + \frac{2 L \langle\alpha_i\rangle}{\ln\frac{1}{R_1 R_2}}\right]"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Dòng bù công suất tăng tuyến tính theo chiều dài hốc L do tổn hao nội:", eq_deriv_2_6_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Kết hợp hai thành phần đối nghịch <i>I</i><sub>th</sub>(<i>L</i>) và Δ<i>I</i><sub>power</sub>(<i>L</i>), "
        "hàm tổng <i>I</i><sub>req</sub>(<i>L</i>) xuất hiện một điểm cực tiểu toàn cục duy nhất tại <i>L</i> = <i>L</i><sub>opt</sub>. "
        "Tại điểm cực tiểu này, đạo hàm biến thiên dòng điện theo chiều dài hốc triệt tiêu bằng 0, "
        "xác lập chiều dài hốc cộng hưởng hoàng kim cho từng cấu hình công nghệ chế tạo."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.6b
    story.append(he.embed_figure_with_caption(
        fig_sim_2_6b,
        "Hình mô phỏng 2.6.2: Khảo sát dòng điện yêu cầu để phát 10 mW theo chiều dài hốc <i>L</i> ở 3 cấu hình gương (Mặt chẻ 0,32 và 0,32; AR–HR 0,05 và 0,95; HR–HR 0,70 và 0,90). "
        "Đồ thị chứng minh cấu hình phủ màng mỏng chống phản xạ và phản xạ cao (AR–HR) mang lại hiệu quả vượt trội, "
        "đạt điểm cực tiểu tại <i>L</i><sub>opt</sub> ≈ 350 μm với dòng tiêu thụ chỉ 21,5 mA, "
        "tiết kiệm hơn 40% công suất nguồn so với mặt chẻ tự nhiên.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận cấu hình phủ gương và thực chiến tối ưu hóa linh kiện", "H3")
    add_p(
        "So sánh các chiến lược phủ gương: "
        "<br/>1. <b>Mặt chẻ tự nhiên (Cleaved facets, <i>R</i><sub>1</sub> = <i>R</i><sub>2</sub> ≈ 0,32):</b> "
        "Chỉ cần cắt dọc theo mặt phẳng tinh thể (110) của GaAs/InP. Tuy nhiên, <i>F</i><sub>1</sub> = 0,5 "
        "khiến một nửa công suất quang bị rò rỉ vô ích về phía gương sau, làm tăng dòng tiêu thụ. "
        "<br/>2. <b>Cấu hình bất đối xứng AR–HR (<i>R</i><sub>1</sub> ≈ 0,05, <i>R</i><sub>2</sub> ≈ 0,95):</b> "
        "Phủ màng mỏng điện môi SiO<sub>2</sub>/TiO<sub>2</sub> nhiều lớp: mặt trước chống phản xạ (AR) để giải phóng ánh sáng, "
        "mặt sau phản xạ cực đại (HR) để chặn rò rỉ. Cấu hình này đẩy <i>F</i><sub>1</sub> lên trên 90%, "
        "vừa giảm dòng yêu cầu vừa bảo vệ mặt gương khỏi hiện tượng phá hủy quang học thảm khốc (COD). "
        "<br/>3. <b>Cấu hình HR–HR (<i>R</i><sub>1</sub>, <i>R</i><sub>2</sub> > 0,90):</b> "
        "Dùng cho laser phát xạ bề mặt hốc đứng VCSEL có thể tích tích cực cực ngắn (<i>L</i> ≈ vài chục nanomet), "
        "giúp hạ dòng ngưỡng xuống dưới 1 mA."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.6.3: HIỆU SUẤT WALL-PLUG & TỐI ƯU HÓA ĐIỂM LÀM VIỆC
    # =========================================================================
    add_p("Luận điểm 2.6.3: Hiệu suất chuyển đổi năng lượng toàn phần (Wall-Plug Efficiency) và Tối ưu hóa điểm làm việc", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm hiệu suất Wall-Plug và các kênh tổn hao điện thế", "H3")
    add_p(
        "Hiệu suất chuyển đổi năng lượng toàn phần (Wall-Plug Efficiency <i>η<sub>c</sub></i> hay WPE) "
        "là tỷ số trực tiếp giữa công suất phát xạ quang hữu ích ngõ ra <i>P</i><sub>0</sub> "
        "và toàn bộ công suất điện một chiều <i>P</i><sub>elec</sub> mà hệ thống cấp nguồn phải cung cấp. "
        "Khác với hiệu suất lượng tử vi phân <i>η<sub>d</sub></i> chỉ đo lường tỷ lệ hạt tải trên ngưỡng, "
        "hiệu suất Wall-Plug phản ánh toàn bộ các hao phí vật lý của diode laser: "
        "tổn hao dòng dưới ngưỡng nuôi tái hợp tự phát, tổn hao lượng tử photon (<i>hν < qV</i>), "
        "tổn hao hấp thụ nội của hốc quang, và tổn hao nhiệt Joule trên điện trở tiếp xúc <i>R<sub>s</sub></i>."
    )
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hiệu suất Wall-Plug", "H3")
    add_p(
        "Biểu thức toán học hoàn chỉnh của hiệu suất chuyển đổi năng lượng Wall-Plug:"
    )

    pillar_eq_2_6_3 = r"\eta_c = \frac{P_0}{P_{\mathrm{elec}}} = \frac{\eta_d \frac{h\nu}{q} (I - I_{\mathrm{th}})}{I \cdot V(I)} = \frac{\eta_d \frac{h\nu}{q} (I - I_{\mathrm{th}})}{I \cdot (V_j + I R_s)}"
    nom_data_2_6_3 = [
        {"name": "Hiệu suất chuyển đổi Wall-Plug", "symbol": "<i>η<sub>c</sub></i>", "unit": "% (hoặc không thứ nguyên)", "meaning": "Tỷ số giữa công suất quang ngõ ra và công suất điện tiêu thụ toàn phần"},
        {"name": "Điện áp hoạt động trên hai cực diode", "symbol": "<i>V</i>(<i>I</i>)", "unit": "V", "meaning": "Tổng sụt áp tiếp giáp <i>V<sub>j</sub></i> và sụt áp thuần trở <i>I · R<sub>s</sub></i>"},
        {"name": "Điện áp tiếp giáp p-n", "symbol": "<i>V<sub>j</sub></i>", "unit": "V", "meaning": "Hiệu số mức Fermi giả qua vùng tích cực (<i>V<sub>j</sub> ≈ hν / q</i>)"},
        {"name": "Điện trở vi phân tiếp xúc nối tiếp", "symbol": "<i>R<sub>s</sub></i>", "unit": "Ω", "meaning": "Tổng điện trở thuần của tiếp xúc kim loại-bán dẫn và các lớp bao bọc"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_6_3, nom_data_2_6_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất điểm cực đại của hiệu suất Wall-Plug", "H3")
    add_p("Dẫn xuất tường minh vị trí dòng điện bơm tối ưu hóa hiệu suất năng lượng:")

    eq_deriv_2_6_3a = r"V(I) = V_j + I R_s \implies P_{\mathrm{elec}} = I V_j + I^2 R_s"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển công suất điện tiêu thụ bao gồm thành phần tiếp giáp và thành phần Joule:", eq_deriv_2_6_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_6_3b = r"\eta_c(I) = \eta_d \frac{h\nu}{q} \frac{1 - \frac{I_{\mathrm{th}}}{I}}{V_j + I R_s}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi hàm hiệu suất Wall-Plug theo biến số dòng tiêm I:", eq_deriv_2_6_3b, styles=styles))
    add_spacer(6)

    eq_deriv_2_6_3c = r"\frac{\mathrm{d}\eta_c}{\mathrm{d}I} = 0 \implies I_{\mathrm{opt}} \approx I_{\mathrm{th}} \left[1 + \sqrt{1 + \frac{V_j}{I_{\mathrm{th}} R_s}}\right]"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm giải tích của dòng bơm đạt đỉnh hiệu suất chuyển đổi Wall-Plug:", eq_deriv_2_6_3c, styles=styles))
    add_spacer(8)

    add_p(
        "Nghiệm giải tích <i>I</i><sub>opt</sub> mang lại định hướng vận hành thực tế sâu sắc: "
        "<br/>• Nếu điện trở tiếp xúc <i>R<sub>s</sub></i> rất nhỏ (tiếp xúc ohmic hoàn hảo), "
        "tỷ số <i>V<sub>j</sub> · (I</i><sub>th</sub> <i>R<sub>s</sub>)</i><sup>−1</sup> rất lớn, "
        "dòng tối ưu dịch chuyển về vùng 3–4 lần dòng ngưỡng, cho phép khai thác công suất quang lớn với hiệu suất cao. "
        "<br/>• Ngược lại, nếu điện trở tiếp xúc bị lỗi công nghệ khiến <i>R<sub>s</sub></i> cao, "
        "tổn hao nhiệt Joule <i>I</i><sup>2</sup> <i>R<sub>s</sub></i> bùng nổ sớm, đỉnh hiệu suất bị dìm xuống thấp "
        "và dịch sát về dòng ngưỡng, thu hẹp dải vận hành kinh tế của laser."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận các giới hạn hiệu suất và so sánh liên công nghệ", "H3")
    add_p(
        "Khảo sát các miền tiệm cận: "
        "<br/>1. <b>Tiệm cận sát ngưỡng (<i>I → I</i><sub>th</sub>):</b> Hiệu suất <i>η<sub>c</sub></i> → 0 vì dòng điện chủ yếu "
        "bù đắp tái hợp tự phát vô ích. "
        "<br/>2. <b>Miền cực đại tối ưu (<i>I = I</i><sub>opt</sub> ≈ 2–3 <i>I</i><sub>th</sub>):</b> "
        "Diode laser bán dẫn hiện đại đạt hiệu suất Wall-Plug từ 50% đến 65% (đối với laser phát thanh GaAs 980 nm công suất lớn). "
        "Đây là mức hiệu suất chuyển đổi năng lượng cao nhất trong toàn bộ thế giới quang học, "
        "vượt trội hoàn toàn so với laser khí He-Ne (dưới 0,1%), laser rắn tinh thể Nd:YAG bơm đèn flash (khoảng 1–3%), "
        "và đèn LED chiếu sáng thương mại (khoảng 20–30%). "
        "<br/>3. <b>Tiệm cận dòng cực lớn (<i>I ≫ I</i><sub>opt</sub>):</b> Tổn hao Joule <i>I</i><sup>2</sup> <i>R<sub>s</sub></i> "
        "áp đảo hoàn toàn trong mẫu số, kéo <i>η<sub>c</sub></i> sụt giảm theo quy luật tỉ lệ nghịch <i>I</i><sup>−1</sup>, "
        "khiến phần lớn công suất cấp vào biến thành nhiệt phá hủy phiến bán dẫn."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN & DỰ ĐOÁN LỖI SAI (BẪY ĐIỂM MÙ R&D)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")
    add_p(
        "Phần thử thách áp dụng phương pháp lập luận ba bước CER (Claim – Evidence – Reasoning) "
        "kết hợp mổ xẻ các lỗi tư duy kinh điển trong phòng thí nghiệm quang điện tử bán dẫn:"
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
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.6.1: NGHỊCH LÝ ĐỘ PHẢN XẠ GƯƠNG VÀ CÔNG SUẤT NGÕ RA</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống phản biện:</b> Một kỹ sư đề xuất phủ lớp phản xạ cao HR lên cả hai mặt gương "
            "(<i>R</i><sub>1</sub> = <i>R</i><sub>2</sub> = 0,95) để giảm thiểu tổn hao gương <i>α<sub>m</sub></i>, "
            "với kỳ vọng dòng ngưỡng <i>I</i><sub>th</sub> sẽ cực nhỏ và do đó ở cùng một dòng tiêm cố định (ví dụ 50 mA), "
            "laser sẽ phát ra công suất quang <i>P</i><sub>0</sub> lớn hơn.<br/>"
            "<b>1. Luận điểm (Claim):</b> Đề xuất của kỹ sư hoàn toàn sai lầm; việc phủ HR cả hai mặt sẽ khiến công suất quang ngõ ra <i>P</i><sub>0</sub> suy giảm nghiêm trọng, thậm chí gần như triệt tiêu tại 50 mA.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Hiệu suất lượng tử vi phân tỉ lệ với hệ số trích xuất: "
            "<i>η<sub>d</sub> = η<sub>i</sub> · α<sub>m</sub> · (⟨α<sub>i</sub>⟩ + α<sub>m</sub>)</i><sup>−1</sup>. "
            "Khi <i>R</i><sub>1</sub><i>R</i><sub>2</sub> = (0,95)<sup>2</sup> ≈ 0,9025 với <i>L</i> = 300 μm, "
            "tổn hao gương <i>α<sub>m</sub></i> sụt giảm từ 38 cm<sup>−1</sup> (mặt chẻ) xuống chỉ còn 1,7 cm<sup>−1</sup>. "
            "Nếu tổn hao nội ⟨<i>α<sub>i</sub></i>⟩ = 10 cm<sup>−1</sup>, tỷ số trích xuất sụt giảm thảm hại từ 79% xuống chỉ còn 14%.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Mặc dù dòng ngưỡng giảm nhẹ, nhưng độ dốc vi sai <i>SE</i> bị giảm gần 6 lần. "
            "Các photon kích thích sinh ra bị giam chặt trong hốc và phần lớn bị hấp thụ bởi các hạt tải tự do và tán xạ khuyết tật nội (⟨<i>α<sub>i</sub></i>⟩) "
            "trước khi kịp thoát ra ngoài qua gương. Muốn trích xuất công suất cao, bắt buộc phải dùng cấu hình bất đối xứng AR–HR."
        ), styles["TableCell"])]
    ]
    t1 = he.Table(cer_card_1, colWidths=[he.PRINTABLE_WIDTH])
    t1.setStyle(cer_style)
    story.append(t1)
    add_spacer(10)

    cer_card_2 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.6.2: ĐO ĐẠC ĐẶC TUYẾN P–I CHẾ ĐỘ XUNG (PULSED) SO VỚI LIÊN TỤC (CW)</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống thí nghiệm:</b> Khi tiến hành đặc trưng hóa diode laser tại phòng Lab, "
            "kỹ sư đo đặc tuyến <i>P</i>–<i>I</i> ở hai chế độ: Chế độ xung ngắn (độ rộng xung 100 ns, chu kỳ nhiệm vụ 0,1%) "
            "và Chế độ sóng liên tục (CW). Hãy dự đoán và đối chiếu kết quả đo giữa hai chế độ.<br/>"
            "<b>1. Luận điểm (Claim):</b> Ở chế độ xung ngắn, dòng ngưỡng <i>I</i><sub>th</sub> sẽ thấp hơn, "
            "độ dốc hiệu suất <i>SE</i> duy trì tuyến tính không đổi lên tới dòng rất lớn, "
            "và hoàn toàn không xuất hiện hiện tượng uốn cong suy hao nhiệt Rollover như ở chế độ liên tục CW.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Công suất tiêu tán nhiệt trung bình ở chế độ xung chỉ bằng 0,1% so với chế độ CW: "
            "⟨<i>P</i><sub>diss</sub>⟩ = <i>Duty Cycle · P</i><sub>diss,peak</sub> = 10<sup>−3</sup> <i>P</i><sub>diss,peak</sub>. "
            "Với độ rộng xung 100 ns nhỏ hơn rất nhiều so với hằng số thời gian cân bằng nhiệt của phiến bán dẫn (cỡ vài micro giây đến mili giây), "
            "nhiệt độ lớp chuyển tiếp p-n không kịp dâng lên (Δ<i>T</i> ≈ 0).<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Chế độ xung phản ánh chính xác bản chất lượng tử thuần khiết đẳng nhiệt của vật liệu bán dẫn (Isothermal Behavior). "
            "Sự sai lệch giữa đường CW và đường xung chính là bằng chứng thực nghiệm trực tiếp để kỹ sư đo lường điện trở nhiệt <i>R</i><sub>th</sub> "
            "và các thông số suy thoái nhiệt <i>T</i><sub>0</sub>, <i>T</i><sub>1</sub> của linh kiện đóng gói."
        ), styles["TableCell"])]
    ]
    t2 = he.Table(cer_card_2, colWidths=[he.PRINTABLE_WIDTH])
    t2.setStyle(cer_style)
    story.append(t2)
    add_spacer(10)

    cer_card_3 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.6.3: BẪY CO NGẮN HỐC CỘNG HƯỞNG TRONG THIẾT KẾ LASER CÔNG SUẤT</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống thiết kế:</b> Một kỹ sư muốn chế tạo diode laser công suất 100 mW, "
            "quyết định thu ngắn chiều dài hốc xuống <i>L</i> = 100 μm để cực đại hóa hiệu suất trích xuất gương <i>η<sub>d</sub></i>. "
            "Linh kiện sau chế tạo không thể đạt được công suất 100 mW mà bị phá hủy ở dòng bơm cao. Tại sao?<br/>"
            "<b>1. Luận điểm (Claim):</b> Việc co ngắn hốc xuống 100 μm gây ra hiện tượng bùng nổ mật độ dòng ngưỡng "
            "và tăng vọt điện trở thuần nối tiếp <i>R<sub>s</sub></i>, dẫn đến thảm họa quá nhiệt phá hủy phiến bán dẫn.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Tổn hao gương tỉ lệ nghịch với chiều dài hốc: "
            "khi <i>L</i> = 100 μm, <i>α<sub>m</sub></i> = 114 cm<sup>−1</sup>, đòi hỏi độ lợi ngưỡng <i>g</i><sub>th</sub> vượt quá 3800 cm<sup>−1</sup>, "
            "tiệm cận mức bão hòa độ lợi tối đa của giếng lượng tử GaAs. "
            "Đồng thời, điện trở tiếp xúc tỉ lệ nghịch với diện tích hốc: <i>R<sub>s</sub> ∝ 1 · (w · L)</i><sup>−1</sup> tăng gấp 3 lần so với hốc 300 μm.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Mật độ dòng ngưỡng <i>J</i><sub>th</sub> tăng vọt kéo theo mật độ phát nhiệt Joule <i>J</i><sup>2</sup> <i>R<sub>s</sub></i> "
            "tập trung trên một thể tích quá nhỏ. Mật độ công suất quang trên mặt gương vượt ngưỡng phá hủy quang học thảm khốc COD "
            "(khoảng vài MW·cm<sup>−2</sup>), làm nóng chảy cục bộ bề mặt gương trước khi đạt được công suất mong muốn."
        ), styles["TableCell"])]
    ]
    t3 = he.Table(cer_card_3, colWidths=[he.PRINTABLE_WIDTH])
    t3.setStyle(cer_style)
    story.append(t3)
    add_spacer(14)

    # Lời kết luận học thuật
    conclusion_text = (
        "<b>KẾT LUẬN CHUYÊN KHẢO MỤC 2.6:</b> Đặc tuyến <i>P</i>–<i>I</i> là bức tranh toàn cảnh phản ánh "
        "sự tương tác phức tạp giữa hiện tượng phát xạ lượng tử trên ngưỡng, quang học hốc cộng hưởng bất đối xứng, "
        "và nhiệt động học bán dẫn thực tế. Nắm vững bài toán tối ưu hóa chiều dài hốc <i>L</i><sub>opt</sub> "
        "và cấu hình màng mỏng gương AR–HR là chìa khóa để kỹ sư chế tạo thành công các module laser hiệu suất cao "
        "đáp ứng các tiêu chuẩn quân sự và công nghiệp khắt khe."
    )
    add_p(conclusion_text, "Body")
    add_spacer(10)

    # Build document
    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_6()

# -*- coding: utf-8 -*-
"""
gen_clean_2_5.py
Chế bản chuyên khảo toàn văn PDF cho Mục 2.5: Điều kiện ngưỡng hoặc trạng thái dừng của độ lợi trong laser.
"""
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak

sys.path.append(r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as he

drive_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý"
img_dir = os.path.join(drive_dir, "Kho_Hinh_Anh")
pdf_dir = os.path.join(drive_dir, "Bai_Giang_Dong_Goi")
os.makedirs(pdf_dir, exist_ok=True)

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.5.pdf")

# Tài nguyên hình ảnh
fig_goc_2_7 = os.path.join(img_dir, "[Goc]_Figure_2.7_Mo_hinh_ho_chua_tren_nguong_co_dap_tran.png")
fig_goc_2_8 = os.path.join(img_dir, "[Goc]_Figure_2.8_Do_loi_theo_mat_do_hat_tai_va_hien_tuong_clamping.png")
fig_goc_2_10 = os.path.join(img_dir, "[Goc]_Figure_2.10_Do_loi_mode_theo_mat_do_hat_tai_tiem_va_ton_hao.png")
fig_sim_2_5a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.5_Do_Loi_Vat_Lieu_Va_Ghim_Do_Loi.png")
fig_sim_2_5b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.5_Kep_Chat_Hat_Tai_Va_Photon.png")


def build_monograph_muc_2_5():
    print(f"Building monograph PDF: {pdf_filename}...")
    styles = he.get_hust_styles()
    styles["BodyText"] = styles["Body"]
    doc = he.BookmarkDocTemplate(pdf_filename)
    story = []

    def add_p(text, style_name="Body"):
        safe_text = he.wrap_math_glyphs(text)
        story.append(he.make_paragraph(safe_text, styles[style_name]))

    def add_spacer(pt=8):
        story.append(Spacer(1, pt))

    # =========================================================================
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.5
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.5: Điều kiện ngưỡng hoặc trạng thái dừng của độ lợi trong laser (Threshold or Steady-State Condition in Lasers)", "H2")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Động học Trạng thái Dừng &amp; Ngưỡng Laser"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 37–41)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Yariv (Ch. 15) &amp; Sze (Ch. 12)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.5 (Chương 2)"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.5 giải phẫu bản chất động học của sự chuyển pha từ trạng thái phát xạ tự phát "
        "dưới ngưỡng sang trạng thái tự dao động phát laser dừng trên ngưỡng "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 37–41). "
        "Hệ thống làm sáng tỏ 3 mắt xích vật lý: (1) Mô hình hồ chứa tương đương có đập tràn phát xạ kích thích (Spillway); "
        "(2) Phương trình độ lợi vật liệu bán dẫn phi tuyến <i>g(N)</i> và hiện tượng ghim độ lợi tại ngưỡng (Gain Clamping); "
        "và (3) Cơ chế kẹp chặt mật độ hạt tải (Carrier Clamping) và biểu thức giải tích xác lập dòng ngưỡng <i>I</i><sub>th</sub>."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.5
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Mô hình hồ chứa trên ngưỡng &amp; Đập tràn phát xạ"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>R</i><sub>st</sub> = <i>v<sub>g</sub> g S</i>, lưu lượng tràn ∝ (<i>I</i> − <i>I</i><sub>th</sub>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.7 (Tr. 38) Mô hình hồ chứa có đập tràn"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Đặc tuyến độ lợi <i>g(N)</i> &amp; Ghim độ lợi tại ngưỡng"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>g(N)</i> = <i>g</i><sub>0</sub> ln(<i>N</i> · <i>N</i><sub>tr</sub><sup>−1</sup>), <i>Γ g</i><sub>th</sub> = ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.8 &amp; Mô phỏng <i>g(N)</i> ghim tại ngưỡng"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.5.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Kẹp chặt hạt tải &amp; Dòng ngưỡng giải tích <i>I</i><sub>th</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>N</i> = <i>N</i><sub>th</sub> (hằng số), <i>I</i><sub>th</sub> = <i>q V</i> · <i>η<sub>i</sub></i><sup>−1</sup> (<i>A N</i><sub>th</sub> + <i>B N</i><sub>th</sub><sup>2</sup> + <i>C N</i><sub>th</sub><sup>3</sup>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.10 &amp; Mô phỏng kẹp chặt <i>N</i> và <i>S</i>"), styles["TableCellCenter"]),
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
    # LUẬN ĐIỂM 2.5.1: MÔ HÌNH HỒ CHỨA TRÊN NGƯỠNG & ĐẬP TRÀN
    # =========================================================================
    add_p("Luận điểm 2.5.1: Mô hình hồ chứa trên ngưỡng và Cơ chế đập tràn phát xạ kích thích", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm & Cơ chế đập tràn
    add_p("Giai đoạn 1: Giới thiệu khái niệm, sự chuyển tiếp dòng chảy hạt tải và cơ chế đập tràn", "H3")
    add_p(
        "Ở chế độ dưới ngưỡng (Mục 2.2), hạt tải chỉ thoát ra qua 3 lỗ thủng tự nhiên dưới đáy hồ (SRH, tự phát, Auger). "
        "Mực nước trong hồ (tương ứng với mật độ hạt tải <i>N</i>) dâng cao dần khi ta tăng lưu lượng bơm dòng tiêm. "
        "Khi mực nước chạm đúng mép đập tràn ở độ cao <i>N</i><sub>th</sub>, điều kiện ngưỡng phát laser được thỏa mãn: "
        "độ lợi mode vừa vặn bù trừ toàn bộ tổn hao hốc. "
        "Ngay lập tức, kênh phát xạ kích thích mở toang như một đập tràn thủy điện khổng lồ. "
        "Mọi giọt nước (hạt tải) bơm thêm vượt trên ngưỡng <i>I</i><sub>th</sub> đều bị cuốn phăng qua đập tràn "
        "để chuyển hóa trực tiếp thành photon kết hợp, giữ cho mực nước trong hồ không thể dâng cao thêm được nữa."
    )
    add_spacer(8)

    # Embed Hình gốc 2.7
    story.append(he.embed_figure_with_caption(
        fig_goc_2_7,
        "Hình 2.7: Mô hình hồ chứa hạt tải tương đương của diode laser ở chế độ trên ngưỡng (Coldren &amp; Corzine, trang 38). "
        "Ba mắt xích cơ học: (a) Lưu lượng bơm dòng tiêm vượt ngưỡng <i>I</i> > <i>I</i><sub>th</sub>; "
        "(b) Mực nước trong hồ bị khóa cứng tại độ cao đập tràn tương ứng mật độ ngưỡng <i>N</i><sub>th</sub>; "
        "(c) Kênh xả lũ đập tràn phát xạ kích thích chuyển hóa toàn bộ dòng thặng dư thành photon hữu ích.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ cân bằng hồ chứa trên ngưỡng", "H3")
    add_p(
        "Phương trình cân bằng dòng chảy hạt tải tại trạng thái dừng trên ngưỡng:"
    )

    pillar_eq_2_5_1 = r"\frac{\eta_i I}{q V} = R(N_{\mathrm{th}}) + R_{\mathrm{st}} = \left(A N_{\mathrm{th}} + B N_{\mathrm{th}}^2 + C N_{\mathrm{th}}^3\right) + v_g g S"
    nom_data_2_5_1 = [
        {"name": "Tốc độ phát xạ kích thích", "symbol": "<i>R</i><sub>st</sub>", "unit": "cm<sup>−3</sup>·s<sup>−1</sup>", "meaning": "Số lượng cặp hạt tải tái hợp phát xạ photon kết hợp trên một đơn vị thể tích trong một giây"},
        {"name": "Mật độ hạt tải ngưỡng", "symbol": "<i>N</i><sub>th</sub>", "unit": "cm<sup>−3</sup>", "meaning": "Mật độ hạt tải tại đó độ lợi cân bằng chính xác với tổn hao"},
        {"name": "Mật độ photon trong mode", "symbol": "<i>S</i>", "unit": "cm<sup>−3</sup>", "meaning": "Số photon kết hợp tích lũy trong thể tích mode quang"},
        {"name": "Độ lợi quang học ngưỡng", "symbol": "<i>g</i>", "unit": "cm<sup>−1</sup>", "meaning": "Độ lợi vật liệu tại trạng thái dừng trên ngưỡng (bằng <i>g</i><sub>th</sub>)"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_5_1, nom_data_2_5_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất sự phân chia dòng tiêm hữu ích trên ngưỡng", "H3")
    add_p("Dẫn xuất tường minh mối quan hệ giữa tốc độ phát xạ kích thích và dòng vượt ngưỡng:")

    eq_deriv_2_5_1a = r"I_{\mathrm{th}} = \frac{q V}{\eta_i} R(N_{\mathrm{th}}) = \frac{q V}{\eta_i} \left(A N_{\mathrm{th}} + B N_{\mathrm{th}}^2 + C N_{\mathrm{th}}^3\right)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Định nghĩa dòng điện ngưỡng từ tốc độ tái hợp tự nhiên:", eq_deriv_2_5_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_5_1b = r"\frac{\eta_i I}{q V} - \frac{\eta_i I_{\mathrm{th}}}{q V} = v_g g S \implies v_g g S = \frac{\eta_i (I - I_{\mathrm{th}})}{q V}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tốc độ phát xạ kích thích tỉ lệ trực tiếp với dòng vượt ngưỡng:", eq_deriv_2_5_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_5_1c = r"S = \frac{\eta_i \tau_p}{q V_{\mathrm{mode}}} (I - I_{\mathrm{th}}) \quad (I \ge I_{\mathrm{th}})"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mật độ photon tăng trưởng tuyến tính nghiêm ngặt trên ngưỡng:", eq_deriv_2_5_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Phương trình trên phản ánh sự phân chia dòng điện tuyệt đối trên ngưỡng: "
        "dòng điện dưới ngưỡng <i>I</i><sub>th</sub> dùng để 'giữ chân' mực nước hạt tải tại đập tràn "
        "và duy trì các kênh tái hợp tự nhiên không đổi. "
        "Toàn bộ lượng dòng tiêm bổ sung (<i>I − I</i><sub>th</sub>) được chuyển hóa 100% với hiệu suất vi sai "
        "thành thông lượng photon kết hợp của chùm tia laser."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận công suất bơm và giới hạn bão hòa đập tràn", "H3")
    add_p(
        "Khảo sát các miền tiệm cận: "
        "<br/>1. <b>Tiệm cận sát ngưỡng (<i>I → I</i><sub>th</sub>):</b> Mật độ photon <i>S</i> bắt đầu thoát khỏi nhiễu tự phát, "
        "tăng vọt với độ dốc lớn. Hiện tượng kết hợp quang học bắt đầu chiếm lĩnh. "
        "<br/>2. <b>Dòng bơm cực lớn (<i>I ≫ I</i><sub>th</sub>):</b> Mật độ photon trong hốc tăng cao đến mức gây ra hiện tượng cháy lỗ không gian (Spatial Hole Burning) "
        "và suy giảm độ lợi phi tuyến (Gain Compression). Khi đó, mực nước có thể hơi dâng nhẹ cục bộ, "
        "đòi hỏi kỹ sư phải kiểm soát nhiệt độ để chống hiện tượng tắt ngưỡng (thermal rollover)."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.5.2: ĐẶC TUYẾN ĐỘ LỢI VẬT LIỆU & GHIM ĐỘ LỢI
    # =========================================================================
    add_p("Luận điểm 2.5.2: Phương trình độ lợi vật liệu phi tuyến g(N) và Hiện tượng ghim độ lợi tại ngưỡng", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm độ lợi phi tuyến
    add_p("Giai đoạn 1: Giới thiệu khái niệm, sự chuyển tiếp từ hấp thụ sang khuếch đại và mật độ trong suốt", "H3")
    add_p(
        "Khi mật độ hạt tải <i>N</i> còn nhỏ, xác suất hấp thụ kích thích lớn hơn phát xạ kích thích, "
        "môi trường bán dẫn đóng vai trò là môi trường hấp thụ quang học (độ lợi âm <i>g</i> < 0). "
        "Khi tiêm hạt tải đến một giá trị tới hạn gọi là mật độ trong suốt <i>N</i><sub>tr</sub> (Transparency Carrier Density), "
        "hai mức Fermi giả phân tách bằng đúng năng lượng photon phát xạ <i>E<sub>Fc</sub> − E<sub>Fv</sub> = hν</i>. "
        "Tại điểm này, tốc độ phát xạ kích thích cân bằng chính xác với tốc độ hấp thụ kích thích, độ lợi vật liệu bằng 0. "
        "Vượt qua <i>N</i><sub>tr</sub>, độ lợi vật liệu <i>g(N)</i> trở nên dương và tăng trưởng phi tuyến theo quy luật logarit."
    )
    add_spacer(8)

    # Embed Hình gốc 2.8
    story.append(he.embed_figure_with_caption(
        fig_goc_2_8,
        "Hình 2.8: Đặc tuyến độ lợi theo mật độ hạt tải và minh họa hiện tượng kẹp chặt độ lợi trên ngưỡng (Coldren &amp; Corzine, trang 39). "
        "Ba mắt xích động học: (a) Mật độ trong suốt <i>N</i><sub>tr</sub> tại đó độ lợi chuyển từ âm sang dương; "
        "(b) Đường cong độ lợi tăng trưởng logarit dưới ngưỡng; "
        "(c) Sự ghim cứng đường cong độ lợi tại mức tổn hao hốc <i>g</i><sub>th</sub> khi dòng tiêm vượt ngưỡng.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hàm độ lợi logarit", "H3")
    add_p(
        "Mô hình giải tích logarit kinh điển của Coldren &amp; Corzine mô tả độ lợi vật liệu giếng lượng tử:"
    )

    pillar_eq_2_5_2 = r"g(N) = g_0 \ln\left(\frac{N}{N_{\mathrm{tr}}}\right), \quad \Gamma g_{\mathrm{th}} = \langle\alpha_i\rangle + \alpha_m \implies g_{\mathrm{th}} = \frac{1}{\Gamma} \left[\langle\alpha_i\rangle + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)\right]"
    nom_data_2_5_2 = [
        {"name": "Hệ số độ lợi vật liệu kinh nghiệm", "symbol": "<i>g</i><sub>0</sub>", "unit": "cm<sup>−1</sup>", "meaning": "Độ dốc tỉ lệ đặc trưng của hệ vật liệu giếng lượng tử (thường từ 1200 đến 2500 cm<sup>−1</sup>)"},
        {"name": "Mật độ hạt tải trong suốt", "symbol": "<i>N</i><sub>tr</sub>", "unit": "cm<sup>−3</sup>", "meaning": "Mật độ hạt tải tối thiểu để triệt tiêu sự hấp thụ nội (≈ 1,2–1,8 × 10<sup>18</sup> cm<sup>−3</sup> ở 300 K)"},
        {"name": "Độ lợi vật liệu tại ngưỡng", "symbol": "<i>g</i><sub>th</sub>", "unit": "cm<sup>−1</sup>", "meaning": "Độ lợi vật liệu tối thiểu cần thiết để cân bằng tổng tổn hao hốc"},
        {"name": "Độ lợi mode tại ngưỡng", "symbol": "<i>Γ g</i><sub>th</sub>", "unit": "cm<sup>−1</sup>", "meaning": "Độ lợi hiệu dụng của mode quang tại ngưỡng"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_5_2, nom_data_2_5_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất mật độ hạt tải ngưỡng <i>N</i><sub>th</sub> từ mô hình logarit", "H3")
    add_p("Dẫn xuất tường minh mật độ hạt tải tại ngưỡng phát laser:")

    eq_deriv_2_5_2a = r"g(N_{\mathrm{th}}) = g_{\mathrm{th}} \implies g_0 \ln\left(\frac{N_{\mathrm{th}}}{N_{\mathrm{tr}}}\right) = g_{\mathrm{th}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập phương trình cân bằng tại ngưỡng:", eq_deriv_2_5_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_5_2b = r"\ln\left(\frac{N_{\mathrm{th}}}{N_{\mathrm{tr}}}\right) = \frac{g_{\mathrm{th}}}{g_0} \implies N_{\mathrm{th}} = N_{\mathrm{tr}} \exp\left(\frac{g_{\mathrm{th}}}{g_0}\right)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm giải tích của mật độ hạt tải ngưỡng:", eq_deriv_2_5_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_5_2c = r"N_{\mathrm{th}} = N_{\mathrm{tr}} \exp\left(\frac{\langle\alpha_i\rangle + \alpha_m}{\Gamma g_0}\right)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu thức toàn phần liên hệ mật độ ngưỡng với toàn bộ thông số hốc:", eq_deriv_2_5_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Hệ thức giải tích trên mang ý nghĩa thiết kế sống còn: "
        "mật độ hạt tải ngưỡng <i>N</i><sub>th</sub> tăng theo hàm mũ của tổng tổn hao hốc (⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>). "
        "Nếu tổn hao tăng gấp đôi, mật độ ngưỡng sẽ tăng theo cấp số nhân, kéo theo dòng ngưỡng bùng nổ theo hàm bậc ba (do tái hợp Auger <i>C N</i><sup>3</sup>). "
        "Vì vậy, giảm thiểu tổn hao nội ⟨<i>α<sub>i</sub></i>⟩ và tăng hệ số giam giữ <i>Γ</i> là hai chìa khóa quyết định để hạ thấp dòng ngưỡng linh kiện."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.5a (Độ lợi vật liệu & Ghim độ lợi tại ngưỡng)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_5a,
        "Hình mô phỏng 2.5.1: Đặc tuyến độ lợi vật liệu <i>g(N)</i> theo mật độ hạt tải trong giếng lượng tử GaAs ở 300 K. "
        "Đồ thị vạch rõ mốc mật độ trong suốt <i>N</i><sub>tr</sub> = 1,5 × 10<sup>18</sup> cm<sup>−3</sup>, "
        "mức độ lợi ngưỡng <i>g</i><sub>th</sub> ≈ 833 cm<sup>−1</sup>, và sự ghim cứng tuyệt đối của độ lợi trên ngưỡng (Gain Clamping) "
        "khi dòng tiêm tiếp tục tăng cao.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận chiều dài hốc và tối ưu hóa mật độ ngưỡng", "H3")
    add_p(
        "Khảo sát các trường hợp thiết kế: "
        "<br/>1. <b>Hốc quá ngắn (<i>L</i> nhỏ hơn 150 μm):</b> Tổn hao gương <i>α<sub>m</sub></i> quá lớn khiến số mũ vượt quá 2, <i>N</i><sub>th</sub> tăng vọt tới vùng bão hòa độ lợi, linh kiện không thể phát laser. "
        "<br/>2. <b>Hốc tối ưu (<i>L</i> từ 300 đến 600 μm):</b> Tổn hao gương vừa đủ nhỏ (30–40 cm<sup>−1</sup>), bảo đảm <i>N</i><sub>th</sub> nằm trong vùng dốc tuyến tính của hàm logarit, đạt hiệu suất vận hành cao nhất."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.5.3: KẸP CHẶT HẠT TẢI & DÒNG NGƯỠNG GIẢI TÍCH
    # =========================================================================
    add_p("Luận điểm 2.5.3: Cơ chế kẹp chặt hạt tải (Carrier Clamping) và Dòng ngưỡng giải tích <i>I</i><sub>th</sub>", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm kẹp chặt hạt tải
    add_p("Giai đoạn 1: Giới thiệu khái niệm kẹp chặt hạt tải và phương trình vi phân tốc độ photon", "H3")
    add_p(
        "Tại sao độ lợi quang học lại bị ghim cứng? Câu trả lời nằm ở phương trình vi phân tốc độ photon: "
        "tốc độ biến thiên mật độ photon theo thời gian triệt tiêu ở trạng thái dừng, cho phương trình: "
        "(<i>Γ v<sub>g</sub> g</i> − <i>v<sub>g</sub> α</i><sub>tot</sub>) <i>S</i> = 0. "
        "Ở chế độ phát laser khi đã tích lũy mật độ photon kết hợp trong hốc (<i>S</i> > 0), "
        "đại lượng trong ngoặc bắt buộc phải triệt tiêu chính xác bằng 0: <i>Γ g = α</i><sub>tot</sub>. "
        "Vì độ lợi <i>g</i> là hàm đơn điệu tăng theo mật độ hạt tải <i>N</i>, "
        "việc độ lợi <i>g</i> bị ghim tại <i>g</i><sub>th</sub> kéo theo hệ quả tất yếu: "
        "mật độ hạt tải <i>N</i> cũng bị kẹp chặt không đổi tại giá trị <i>N</i><sub>th</sub> trên toàn bộ dải dòng tiêm trên ngưỡng."
    )
    add_spacer(8)

    # Embed Hình gốc 2.10
    story.append(he.embed_figure_with_caption(
        fig_goc_2_10,
        "Hình 2.10: Đặc tuyến độ lợi mode quang học theo mật độ hạt tải tiêm và vị trí cân bằng với tổn hao hốc (Coldren &amp; Corzine, trang 40). "
        "Ba mắt xích cân bằng: (a) Điểm cân bằng dừng <i>Γ g</i><sub>th</sub> = ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>; "
        "(b) Dưới ngưỡng, độ lợi tăng dần khi tiêm hạt tải; "
        "(c) Trên ngưỡng, mật độ hạt tải bị kẹp chặt tại <i>N</i><sub>th</sub>.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ dòng điện ngưỡng giải tích", "H3")
    add_p(
        "Biểu thức giải tích của dòng điện ngưỡng toàn phần:"
    )

    pillar_eq_2_5_3 = r"I_{\mathrm{th}} = \frac{q V}{\eta_i} R(N_{\mathrm{th}}) = \frac{q V}{\eta_i} \left(A N_{\mathrm{th}} + B N_{\mathrm{th}}^2 + C N_{\mathrm{th}}^3\right)"
    nom_data_2_5_3 = [
        {"name": "Dòng điện ngưỡng phát laser", "symbol": "<i>I</i><sub>th</sub>", "unit": "A (hoặc mA)", "meaning": "Dòng tiêm tối thiểu bắt đầu xuất hiện bức xạ kích thích kết hợp"},
        {"name": "Mật độ hạt tải ngưỡng", "symbol": "<i>N</i><sub>th</sub>", "unit": "cm<sup>−3</sup>", "meaning": "Mật độ hạt tải kẹp chặt không đổi trên ngưỡng"},
        {"name": "Thể tích vùng tích cực", "symbol": "<i>V</i>", "unit": "cm<sup>3</sup>", "meaning": "Thể tích hình học lõi giam giữ <i>V = d · w · L</i>"},
        {"name": "Hiệu suất tiêm nội tại ngưỡng", "symbol": "<i>η<sub>i</sub></i>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ hạt tải tiêm đi vào vùng tích cực tại ngưỡng"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_5_3, nom_data_2_5_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất tỷ trọng các thành phần dòng ngưỡng", "H3")
    add_p("Dẫn xuất phân rã dòng ngưỡng thành 3 thành phần vi mô riêng biệt:")

    eq_deriv_2_5_3a = r"I_{\mathrm{th}} = I_{\mathrm{srh}} + I_{\mathrm{rad}} + I_{\mathrm{aug}} = \frac{q V}{\eta_i} A N_{\mathrm{th}} + \frac{q V}{\eta_i} B N_{\mathrm{th}}^2 + \frac{q V}{\eta_i} C N_{\mathrm{th}}^3"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phân tách dòng ngưỡng theo ba kênh tái hợp:", eq_deriv_2_5_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_5_3b = r"J_{\mathrm{th}} = \frac{I_{\mathrm{th}}}{w L} = \frac{q d}{\eta_i} \left(A N_{\mathrm{th}} + B N_{\mathrm{th}}^2 + C N_{\mathrm{th}}^3\right)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mật độ dòng ngưỡng tính trên một đơn vị diện tích:", eq_deriv_2_5_3b, styles=styles))
    add_spacer(6)

    eq_deriv_2_5_3c = r"d \to 10\ \mathrm{nm}\ (\mathrm{QW}) \implies J_{\mathrm{th}} \approx 100 - 300\ \mathrm{A}\cdot\mathrm{cm}^{-2} \quad (\text{giảm 50 lần so với DH 200 nm})"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Ưu thế vượt bậc của cấu trúc giếng lượng tử trong việc hạ thấp dòng ngưỡng:", eq_deriv_2_5_3c, styles=styles))
    add_spacer(8)

    add_p(
        "Từ phương trình mật độ dòng ngưỡng <i>J</i><sub>th</sub>, ta thấy rõ: "
        "dòng ngưỡng tỉ lệ thuận trực tiếp với bề dày vùng tích cực <i>d</i>. "
        "Chuyển từ cấu trúc dị thể kép DH (<i>d</i> = 200 nm) sang cấu trúc giếng lượng tử đơn SQW (<i>d</i> = 8 nm) "
        "làm giảm thể tích vùng tích cực 25 lần, cho phép đưa mật độ dòng ngưỡng từ 1000–5000 A/cm<sup>2</sup> "
        "xuống chỉ còn 100–200 A/cm<sup>2</sup>, giải phóng hoàn toàn linh kiện khỏi nguy cơ phá hủy do quá nhiệt."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.5b (Kẹp chặt hạt tải & Tăng trưởng photon trên ngưỡng)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_5b,
        "Hình mô phỏng 2.5.2: Minh chứng định lượng hiện tượng kẹp chặt hạt tải (Carrier Clamping) và sự bùng nổ mật độ photon trên ngưỡng. "
        "Dưới ngưỡng (<i>I</i> < <i>I</i><sub>th</sub>), mật độ hạt tải tăng theo căn bậc hai của dòng tiêm trong khi photon hầu như bằng 0. "
        "Ngay khi vượt qua <i>I</i><sub>th</sub>, mật độ hạt tải bị khóa cứng tuyệt đối tại 1,0, và 100% dòng bơm tăng thêm chuyển hóa thành photon kết hợp.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận nhiệt độ và định luật thực nghiệm Pankove", "H3")
    add_p(
        "Sự phụ thuộc nhiệt độ của dòng ngưỡng tuân theo định luật hàm mũ thực nghiệm Pankove: "
        "<br/><i>I</i><sub>th</sub>(<i>T</i>) = <i>I</i><sub>0</sub> exp(<i>T · T</i><sub>0</sub><sup>−1</sup>). "
        "<br/>Trong đó <i>T</i><sub>0</sub> là nhiệt độ đặc trưng của linh kiện: "
        "<br/>• Với laser bước sóng ngắn GaAs/AlGaAs (0,85 μm), <i>T</i><sub>0</sub> đạt 120–180 K (rất ổn định với nhiệt độ). "
        "<br/>• Với laser bước sóng dài InGaAsP/InP (1,3–1,55 μm), <i>T</i><sub>0</sub> chỉ đạt 50–70 K do ảnh hưởng áp đảo của tái hợp Auger và rò rỉ nhiệt, "
        "khiến linh kiện bắt buộc phải tích hợp bộ làm lạnh nhiệt điện TEC trong các module truyền thông đường dài."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN CER & ĐIỂM MÙ THIẾT KẾ
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")

    cer_card = [
        [Paragraph(he.wrap_math_glyphs("<b>BÀI TOÁN THỬ THÁCH CHẨN ĐOÁN CER 2.5: ĐỘ LỢI CÓ THỰC SỰ BỊ GHIM 100% TRÊN NGƯỠNG KHÔNG?</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Bối cảnh bài toán R&amp;D:</b> Trong một báo cáo kỹ thuật, một kỹ sư trẻ khẳng định rằng: "
            "'Trên ngưỡng phát laser, mật độ hạt tải <i>N</i> và độ lợi quang học <i>g</i> bị kẹp chặt tuyệt đối 100% không đổi tại mọi điểm trong toàn bộ thể tích vùng tích cực, "
            "do đó phổ phát xạ tự phát đo được từ cạnh bên của laser sẽ giữ nguyên giá trị không tăng thêm dù dòng tiêm tăng gấp 5 lần dòng ngưỡng'. "
            "Tuy nhiên, khi trưởng phòng đo phổ phát xạ tự phát từ cạnh bên của một laser stripe-geometry ở dòng <i>I</i> = 3 <i>I</i><sub>th</sub>, "
            "ông quan sát thấy cường độ phát xạ tự phát vẫn tăng thêm khoảng 8–12%.<br/><br/>"
            "• <b>Luận điểm (Claim):</b> Nhận định của kỹ sư trẻ đúng hay sai? Tại sao cường độ phát xạ tự phát thực tế vẫn tăng nhẹ trên ngưỡng?<br/>"
            "• <b>Bằng chứng (Evidence):</b> Dựa vào hiện tượng cháy lỗ không gian theo phương ngang (Lateral Spatial Hole Burning) và hiện tượng nén độ lợi phi tuyến (Gain Compression Factor <i>ε</i>) ở mật độ photon cao.<br/>"
            "• <b>Lập luận (Reasoning):</b> Phân tích sự không đồng nhất về mặt không gian của mật độ photon <i>S(x, y, z)</i>: photon tập trung cao ở tâm mode quang làm tiêu hao hạt tải ở tâm nhanh hơn mép, "
            "dẫn đến việc hạt tải ở hai rìa ngoài của dải tiếp xúc vẫn tiếp tục tích lũy và phát xạ tự phát tăng thêm."
        ), styles["TableCell"])]
    ]
    cer_t = he.Table(cer_card, colWidths=[he.PRINTABLE_WIDTH])
    cer_t.setStyle(he.TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#002B49')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8F9FA')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#002B49')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(cer_t)
    add_spacer(14)

    # Khâu nối biên độ DOC (Transition Anchor sang Mục 2.6)
    add_p(
        "<b>Khâu nối biên độ và Tiền đề chuyển tiếp sang Mục 2.6:</b> "
        "Mục 2.5 đã giải phẫu trọn vẹn hiện tượng kẹp chặt độ lợi và cơ chế hình thành dòng ngưỡng <i>I</i><sub>th</sub>. "
        "Khi dòng tiêm vượt ngưỡng (<i>I</i> > <i>I</i><sub>th</sub>), công suất quang ngõ ra <i>P</i><sub>out</sub> sẽ tăng trưởng như thế nào theo dòng điện tiêm <i>I</i>? "
        "Khái niệm hiệu suất lượng tử vi phân (Differential Quantum Efficiency - <i>η<sub>d</sub></i>) và độ dốc đặc tuyến <i>L–I</i> (Slope Efficiency) được định nghĩa ra sao? "
        "Các yếu tố nào làm bẻ cong đặc tuyến công suất ở vùng dòng cao (hiện tượng cuộn nhiệt - Thermal Rollover)? "
        "Tất cả các quy luật vận hành thực nghiệm này sẽ được giải phẫu toàn diện trong <b>Mục 2.6: Dòng ngưỡng và công suất bức xạ ngõ ra theo dòng tiêm</b>."
    )

    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename) / 1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_5()

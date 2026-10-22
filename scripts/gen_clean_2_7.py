# -*- coding: utf-8 -*-
"""
gen_clean_2_7.py
Biên dịch Chuyên khảo Toàn văn Mục 2.7: Cộng hưởng hồi phục và đáp ứng tần số điều chế
Coldren & Corzine, trang 48-52.
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

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.7.pdf")

# Hình ảnh gốc và mô phỏng
fig_goc_2_12 = os.path.join(img_dir, "[Goc]_Figure_2.12_Dap_ung_tan_so_dieu_che_tin_hieu_nho_laser_diode.png")
fig_sim_2_7a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.7_Ham_Truyen_Dieu_Che_Tan_So.png")
fig_sim_2_7b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.7_He_So_Tat_Dan_Va_Gioi_Han_Bang_Thong_K_Factor.png")


def build_monograph_muc_2_7():
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
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.7
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.7: Cộng hưởng hồi phục và đáp ứng tần số điều chế (Relaxation Resonance and Frequency Response)", "H2")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Động học Điều chế Tốc độ cao &amp; Băng thông"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 48–52)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Yariv (Ch. 15) &amp; Agrawal (Ch. 3)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.7 (Chương 2)"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.7 giải phẫu đáp ứng tần số động học của diode laser "
        "khi điều chế tín hiệu nhỏ tốc độ cao phục vụ các tuyến thông tin quang gigabit và xử lý tín hiệu vi ba "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 48–52). "
        "Nội dung chuyên khảo triển khai sâu 3 Luận điểm Vi mô (MPT): "
        "(1) Hiện tượng dao động hồi phục (Relaxation Oscillations), ghép cặp động học phi tuyến hạt tải – photon, "
        "và tần số dao động tự do <i>ω<sub>R</sub></i>; "
        "(2) Hàm truyền điều chế tín hiệu nhỏ <i>H(ω)</i>, sự dịch chuyển đỉnh cộng hưởng theo căn bậc hai công suất bơm, "
        "và công thức xác lập băng thông điều chế 3 dB (<i>f</i><sub>3dB</sub>); "
        "và (3) Hệ số tắt dần <i>γ</i>, hệ số <i>K</i>-factor, hiện tượng nén độ lợi phi tuyến (Gain Compression <i>ε</i>), "
        "và các giới hạn vật lý chặn đứng băng thông điều chế tối đa trong thực tế."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.7
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.7.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Dao động hồi phục &amp; Tần số cộng hưởng <i>ω<sub>R</sub></i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>ω<sub>R</sub></i> = (<i>v<sub>g</sub> a S</i><sub>0</sub> · <i>τ<sub>p</sub></i><sup>−1</sup>)<sup>0,5</sup> ∝ <i>P</i><sub>0</sub><sup>0,5</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.12 (Tr. 50) Đáp ứng tần số tín hiệu nhỏ"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.7.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hàm truyền <i>H(ω)</i> &amp; Băng thông điều chế <i>f</i><sub>3dB</sub>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>H(ω) = ω<sub>R</sub></i><sup>2</sup> · (<i>ω<sub>R</sub></i><sup>2</sup> − <i>ω</i><sup>2</sup> + <i>jωγ</i>)<sup>−1</sup>, <i>f</i><sub>3dB</sub> ≈ 1,55 <i>f<sub>R</sub></i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng đáp ứng biên độ |<i>H(f)</i>|<sup>2</sup> (dB)"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.7.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hệ số <i>K</i>-factor &amp; Giới hạn băng thông tối đa"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>γ = K f<sub>R</sub></i><sup>2</sup> + <i>γ</i><sub>0</sub>, <i>f</i><sub>3dB,max</sub> = 2√2 <i>π · K</i><sup>−1</sup> ≈ 8,88 · <i>K</i><sup>−1</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng <i>γ(f<sub>R</sub></i><sup>2</sup>) &amp; Bẫy điểm mù CER"), styles["TableCellCenter"]),
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
    # LUẬN ĐIỂM 2.7.1: DAO ĐỘNG HỒI PHỤC VÀ GHÉP CẶP ĐỘNG HỌC
    # =========================================================================
    add_p("Luận điểm 2.7.1: Hiện tượng dao động hồi phục (Relaxation Oscillations) và Ghép cặp động học hạt tải – photon", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm dao động hồi phục và cơ chế chuyển đổi năng lượng tuần hoàn", "H3")
    add_p(
        "Khi một xung dòng điện đột ngột tiêm vào diode laser hoặc khi tín hiệu điều chế cao tần tác động lên linh kiện, "
        "hệ thống không chuyển tức thời sang trạng thái dừng mới mà trải qua một quá trình chuyển tiếp dao động tắt dần "
        "gọi là dao động hồi phục (Relaxation Oscillations). "
        "Bản chất vật lý của hiện tượng này tương tự như một dao động tử điều hòa hai bậc tự do: "
        "Dòng tiêm làm mật độ hạt tải <i>N</i> tăng vọt vượt ngưỡng, kéo theo độ lợi quang học vượt quá tổn hao hốc. "
        "Độ lợi thặng dư kích hoạt phát xạ kích thích bùng nổ, sinh ra lượng photon khổng lồ tích lũy trong hốc. "
        "Mật độ photon cao này quay lại quét sạch (burn out) lượng hạt tải dự trữ khiến <i>N</i> sụt giảm xuống dưới mức ngưỡng, "
        "làm độ lợi suy yếu và số lượng photon bắt đầu suy tàn. Chu trình trao đổi năng lượng tuần hoàn này lặp đi lặp lại "
        "với biên độ giảm dần do các cơ chế tiêu tán năng lượng, xác lập tần số dao động tự nhiên đặc trưng <i>ω<sub>R</sub></i>."
    )
    add_spacer(8)

    # Embed Hình gốc 2.12
    story.append(he.embed_figure_with_caption(
        fig_goc_2_12,
        "Hình 2.12: Đáp ứng tần số điều chế tín hiệu nhỏ của diode laser ở các mức công suất quang khác nhau (Coldren &amp; Corzine, trang 50). "
        "Ba mắt xích động học: (a) Đỉnh cộng hưởng dịch chuyển về phía tần số cao khi tăng công suất bơm; "
        "(b) Độ dốc suy giảm −40 dB mỗi decade ở vùng tần số cao vượt xa tần số cộng hưởng; "
        "(c) Sự là phẳng đỉnh cộng hưởng ở mức công suất rất cao do hiện tượng tắt dần phi tuyến.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ tần số cộng hưởng hồi phục", "H3")
    add_p(
        "Biểu thức giải tích của tần số góc dao động hồi phục tự nhiên:"
    )

    pillar_eq_2_7_1 = r"\omega_R = \sqrt{\frac{v_g a S_0}{\tau_p}} = \sqrt{\frac{\Gamma v_g a}{\eta_i q V} (I - I_{\mathrm{th}})} \implies f_R = \frac{\omega_R}{2\pi} = D \sqrt{P_0}"
    nom_data_2_7_1 = [
        {"name": "Tần số góc cộng hưởng hồi phục", "symbol": "<i>ω<sub>R</sub></i>", "unit": "rad·s<sup>−1</sup>", "meaning": "Tần số dao động tuần hoàn tự nhiên giữa hạt tải và photon trong hốc"},
        {"name": "Độ lợi vi phân vật liệu", "symbol": "<i>a</i>", "unit": "cm<sup>2</sup>", "meaning": "Độ dốc của hàm độ lợi theo mật độ hạt tải tại điểm làm việc"},
        {"name": "Mật độ photon dừng trung bình", "symbol": "<i>S</i><sub>0</sub>", "unit": "cm<sup>−3</sup>", "meaning": "Số lượng photon kết hợp tích lũy trong thể tích mode ở trạng thái tĩnh"},
        {"name": "Hệ số độ dốc tần số D-factor", "symbol": "<i>D</i>", "unit": "GHz·mW<sup>−1/2</sup>", "meaning": "Tỷ số tỉ lệ giữa tần số cộng hưởng <i>f<sub>R</sub></i> và căn bậc hai công suất quang"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_7_1, nom_data_2_7_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phương trình dao động điều hòa từ hệ vi phân tốc độ", "H3")
    add_p("Dẫn xuất tường minh phương trình dao động bằng phương pháp tuyến tính hóa tín hiệu nhỏ:")

    eq_deriv_2_7_1a = r"\frac{\mathrm{d}N}{\mathrm{d}t} = \frac{\eta_i I}{q V} - \frac{N}{\tau} - v_g g(N) S, \quad \frac{\mathrm{d}S}{\mathrm{d}t} = \left[\Gamma v_g g(N) - \frac{1}{\tau_p}\right] S"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Cặp phương trình vi phân tốc độ phi tuyến ghép cặp hạt tải – photon:", eq_deriv_2_7_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_7_1b = r"N(t) = N_0 + n_1 e^{j\omega t}, \quad S(t) = S_0 + s_1 e^{j\omega t} \quad (n_1 \ll N_0,\ s_1 \ll S_0)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển dao động điều hòa tín hiệu nhỏ quanh điểm làm việc dừng:", eq_deriv_2_7_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_7_1c = r"\det \begin{bmatrix} j\omega + \gamma_{NN} & \gamma_{NS} \\ -\gamma_{SN} & j\omega + \gamma_{SS} \end{bmatrix} = 0 \implies -\omega^2 + j\omega \gamma + \omega_R^2 = 0"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phương trình đặc trưng của ma trận Jacobi xác lập tần số dao động tự do:", eq_deriv_2_7_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Kết quả giải tích chứng minh rằng hệ thống hạt tải – photon hành xử chính xác như một mạch dao động RLC "
        "hoặc một quả lắc cơ học có ma sát. Tần số dao động <i>ω<sub>R</sub></i> tỉ lệ thuận với căn bậc hai của mật độ photon <i>S</i><sub>0</sub>: "
        "càng bơm mạnh dòng điện (tăng công suất quang <i>P</i><sub>0</sub>), "
        "thông lượng photon trong hốc càng đậm đặc, khiến tương tác phát xạ kích thích diễn ra càng dồn dập, "
        "đẩy tần số cộng hưởng <i>f<sub>R</sub></i> dịch chuyển mạnh mẽ lên dải tần số cao."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận đáp ứng xung và hiện tượng biến điệu tần số quang (Frequency Chirp)", "H3")
    add_p(
        "Khảo sát các hệ quả kỹ thuật trong truyền dẫn quang: "
        "<br/>1. <b>Hiện tượng vọt lố (Overshoot) và dao động chuông (Ringing):</b> Trong điều chế số xung NRZ (Non-Return-to-Zero), "
        "dao động hồi phục tạo ra các đỉnh nhọn vọt lố ở sườn trước của xung ánh sáng. "
        "Nếu tần số lấy mẫu tín hiệu gần với <i>f<sub>R</sub></i>, hiện tượng này sẽ làm biến dạng giản đồ mắt (Eye Diagram) và tăng tỷ lệ lỗi bit BER. "
        "<br/>2. <b>Hiện tượng dạt tần số quang (Chirp):</b> Sự dao động mạnh của mật độ hạt tải <i>n</i><sub>1</sub>(<i>t</i>) "
        "trong quá trình hồi phục dẫn đến sự biến thiên chiết suất vùng tích cực Δ<i>n</i><sub>re</sub> "
        "thông qua hệ số tăng cường độ rộng vạch phổ Henry (Linewidth Enhancement Factor <i>α<sub>H</sub></i>). "
        "Hệ quả là tần số sóng mang quang bị biến điệu theo thời gian (Frequency Chirping), "
        "làm xung quang bị dãn rộng nghiêm trọng khi truyền qua sợi quang có tán sắc sắc sắc ký (Chromatic Dispersion)."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.7.2: HÀM TRUYỀN TÍN HIỆU NHỎ VÀ BĂNG THÔNG ĐIỀU CHẾ 3 dB
    # =========================================================================
    add_p("Luận điểm 2.7.2: Hàm truyền điều chế tín hiệu nhỏ và Băng thông điều chế 3 dB", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm hàm truyền
    add_p("Giai đoạn 1: Giới thiệu khái niệm hàm truyền điều chế và chuẩn hóa đáp ứng tần số", "H3")
    add_p(
        "Để đánh giá khả năng truyền tải dữ liệu của diode laser trong các hệ thống viễn thông, "
        "ta kích thích linh kiện bằng một dòng xoay chiều biên độ nhỏ <i>i</i><sub>1</sub>(<i>ω</i>) "
        "chồng lên dòng phân cực một chiều <i>I</i><sub>0</sub> > <i>I</i><sub>th</sub>. "
        "Hàm truyền điều chế tín hiệu nhỏ <i>H(ω)</i> được định nghĩa là tỷ số giữa biên độ dao động công suất quang ngõ ra "
        "<i>p</i><sub>1</sub>(<i>ω</i>) và biên độ dòng điện kích thích <i>i</i><sub>1</sub>(<i>ω</i>), "
        "chuẩn hóa về 0 dB tại tần số rất thấp (<i>ω</i> → 0). "
        "Đồ thị đáp ứng biên độ |<i>H(ω)</i>|<sup>2</sup> biểu diễn trên thang logarit (dB) "
        "là công cụ trực quan duy nhất xác định băng thông điều chế thực tế của linh kiện."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.7a
    story.append(he.embed_figure_with_caption(
        fig_sim_2_7a,
        "Hình mô phỏng 2.7.1: Đáp ứng tần số điều chế tín hiệu nhỏ |<i>H(f)</i>|<sup>2</sup> (dB) của diode laser InGaAsP/InP 1550 nm ở các mức công suất quang 1 mW, 3 mW, 8 mW và 16 mW. "
        "Đồ thị chứng minh rõ ràng: khi công suất quang tăng từ 1 mW lên 16 mW, "
        "đỉnh cộng hưởng <i>f<sub>R</sub></i> dịch chuyển từ 2,5 GHz lên 10,0 GHz, "
        "mở rộng băng thông điều chế <i>f</i><sub>3dB</sub> từ 3,8 GHz lên vượt mức 15,2 GHz.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hàm truyền tín hiệu nhỏ", "H3")
    add_p(
        "Biểu thức giải tích của hàm truyền chuẩn hóa bậc hai và công thức xác định băng thông 3 dB:"
    )

    pillar_eq_2_7_2 = r"H(\omega) = \frac{\omega_R^2}{\omega_R^2 - \omega^2 + j\omega\gamma}, \quad f_{3\mathrm{dB}} \approx f_R \sqrt{1 + \sqrt{2}} \approx 1{,}55 f_R \quad (\text{khi }\gamma \ll \omega_R)"
    nom_data_2_7_2 = [
        {"name": "Hàm truyền điều chế chuẩn hóa", "symbol": "<i>H(ω)</i>", "unit": "không thứ nguyên", "meaning": "Tỷ số biến thiên công suất quang trên biến thiên dòng kích thích"},
        {"name": "Hệ số tắt dần toàn phần", "symbol": "<i>γ</i>", "unit": "rad·s<sup>−1</sup> (hoặc ns<sup>−1</sup>)", "meaning": "Độ rộng bán phần của đỉnh cộng hưởng và tốc độ tiêu tán dao động"},
        {"name": "Tần số điều chế góc", "symbol": "<i>ω</i> = 2<i>πf</i>", "unit": "rad·s<sup>−1</sup>", "meaning": "Tần số góc của tín hiệu thông tin điều chế đầu vào"},
        {"name": "Băng thông điều chế 3 dB", "symbol": "<i>f</i><sub>3dB</sub>", "unit": "GHz", "meaning": "Tần số tại đó đáp ứng công suất quang suy giảm 3 dB so với giá trị DC"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_7_2, nom_data_2_7_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất băng thông điều chế 3 dB", "H3")
    add_p("Dẫn xuất tường minh điều kiện xác lập mốc băng thông −3 dB:")

    eq_deriv_2_7_2a = r"|H(\omega)|^2 = \frac{\omega_R^4}{(\omega_R^2 - \omega^2)^2 + \omega^2 \gamma^2} = \frac{1}{2}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập phương trình suy giảm một nửa công suất tại tần số cắt 3 dB:", eq_deriv_2_7_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_7_2b = r"(\omega_R^2 - \omega^2)^2 + \omega^2 \gamma^2 = 2 \omega_R^4 \implies \omega^4 + (\gamma^2 - 2\omega_R^2) \omega^2 - \omega_R^4 = 0"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển phương trình trùng phương theo biến số bình phương tần số ω^2:", eq_deriv_2_7_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_7_2c = r"\omega_{3\mathrm{dB}} = \sqrt{\left(\omega_R^2 - \frac{\gamma^2}{2}\right) + \sqrt{\left(\omega_R^2 - \frac{\gamma^2}{2}\right)^2 + \omega_R^4}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm giải tích chính xác toàn phần của băng thông điều chế:", eq_deriv_2_7_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Khi hệ số tắt dần nhỏ (<i>γ</i> ≪ <i>ω<sub>R</sub></i>), nghiệm giải tích thu gọn về hệ thức kinh điển: "
        "<i>ω</i><sub>3dB</sub> = <i>ω<sub>R</sub></i> √(1 + √2) ≈ 1,55 <i>ω<sub>R</sub></i>. "
        "Hệ thức này mang ý nghĩa thiết kế cực kỳ to lớn: "
        "băng thông điều chế khả dụng của một diode laser luôn vượt qua tần số cộng hưởng tự do khoảng 55%. "
        "Do đó, mọi nỗ lực công nghệ nhằm nâng cao tần số <i>f<sub>R</sub></i> "
        "đều trực tiếp giải phóng băng thông truyền dữ liệu của hệ thống."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận công suất bơm và hành vi quá tắt dần (Overdamped)", "H3")
    add_p(
        "Khảo sát các vùng vận hành điều chế: "
        "<br/>1. <b>Miền công suất thấp (Dưới tắt dần, Underdamped):</b> Đỉnh cộng hưởng nổi cao sắc nhọn "
        "(độ nhọn vọt lố có thể lên tới +6 đến +10 dB). Mặc dù băng thông mở rộng nhưng đỉnh nhọn này gây méo tín hiệu vi ba "
        "và làm tăng nhiễu pha. "
        "<br/>2. <b>Miền công suất tối ưu (Tắt dần tới hạn, Critically Damped):</b> Đỉnh cộng hưởng hơi nhô nhẹ (khoảng +1 đến +2 dB), "
        "đáp ứng tần số phẳng tối đa trong toàn dải thông (tương tự bộ lọc Butterworth), "
        "đây là trạng thái lý tưởng nhất cho truyền dẫn cáp quang tốc độ cao 25–50 Gbps. "
        "<br/>3. <b>Miền công suất rất lớn (Quá tắt dần, Overdamped):</b> Hệ số tắt dần <i>γ</i> tăng nhanh hơn <i>ω<sub>R</sub></i>, "
        "đè bẹp hoàn toàn đỉnh cộng hưởng, khiến đáp ứng tần số suy giảm đơn điệu ngay từ tần số thấp, "
        "chặn đứng sự tăng trưởng tiếp theo của băng thông 3 dB."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.7.3: HỆ SỐ K-FACTOR VÀ GIỚI HẠN BĂNG THÔNG TỐI ĐA
    # =========================================================================
    add_p("Luận điểm 2.7.3: Hệ số K-factor, Nén độ lợi phi tuyến và Giới hạn băng thông tối đa", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm
    add_p("Giai đoạn 1: Giới thiệu khái niệm hệ số K-factor và hiện tượng nén độ lợi phi tuyến", "H3")
    add_p(
        "Tại sao băng thông điều chế của diode laser không thể tăng mãi mãi khi ta liên tục tăng dòng bơm? "
        "Có hai rào cản vật lý cốt tử chặn đứng tốc độ của linh kiện: "
        "(1) Hiện tượng nén độ lợi phi tuyến (Gain Compression): ở mật độ photon rất cao, "
        "các hiệu ứng đốt nóng hạt tải (Carrier Heating) và đốt cháy lỗ phổ (Spectral Hole Burning) "
        "làm độ lợi vi mô bị suy giảm nhẹ theo quy luật <i>g(N, S) = g(N) · (1 + ε S)</i><sup>−1</sup>, "
        "trong đó <i>ε</i> là hệ số nén độ lợi phi tuyến; "
        "và (2) Hệ số tắt dần <i>γ</i> tăng tuyến tính với bình phương tần số cộng hưởng <i>f<sub>R</sub></i><sup>2</sup> "
        "thông qua một tham số đặc trưng gọi là hệ số <i>K</i>-factor. "
        "Chính độ dốc <i>K</i>-factor này đặt ra một trần băng thông tối đa tuyệt đối mà linh kiện không thể vượt qua."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.7b
    story.append(he.embed_figure_with_caption(
        fig_sim_2_7b,
        "Hình mô phỏng 2.7.2: Đồ thị tuyến tính của hệ số tắt dần <i>γ</i> theo bình phương tần số cộng hưởng <i>f<sub>R</sub></i><sup>2</sup> ở các giá trị <i>K</i>-factor (0,25 ns, 0,38 ns, 0,55 ns). "
        "Đồ thị chứng minh độ dốc của đường thẳng xác định trực tiếp hệ số <i>K</i>. "
        "Giá trị <i>K</i> càng nhỏ (0,25 ns), trần băng thông cực đại do tắt dần <i>f</i><sub>max</sub> càng lớn (đạt tới 35,5 GHz).",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ giới hạn băng thông tối đa do K-factor", "H3")
    add_p(
        "Hệ thức liên hệ tuyến tính giữa hệ số tắt dần và trần băng thông điều chế cực đại nội tại:"
    )

    pillar_eq_2_7_3 = r"\gamma = K f_R^2 + \gamma_0, \quad K = 4\pi^2 \left(\tau_p + \frac{\epsilon}{v_g a}\right) \implies f_{3\mathrm{dB},\max} = \frac{2\sqrt{2}\pi}{K} \approx \frac{8{,}88}{K}"
    nom_data_2_7_3 = [
        {"name": "Hệ số tắt dần K-factor", "symbol": "<i>K</i>", "unit": "ns", "meaning": "Độ dốc của hàm <i>γ</i> theo <i>f<sub>R</sub></i><sup>2</sup>, đại lượng đo mức độ tắt dần nội tại"},
        {"name": "Hệ số nén độ lợi phi tuyến", "symbol": "<i>ε</i>", "unit": "cm<sup>3</sup>", "meaning": "Hệ số suy giảm độ lợi quang học ở mật độ photon cao (≈ 10<sup>−17</sup> cm<sup>3</sup>)"},
        {"name": "Thời gian sống của photon trong hốc", "symbol": "<i>τ<sub>p</sub></i>", "unit": "ps", "meaning": "Thời gian photon tồn tại trước khi thoát qua gương hoặc bị hấp thụ nội"},
        {"name": "Trần băng thông điều chế tối đa", "symbol": "<i>f</i><sub>3dB,max</sub>", "unit": "GHz", "meaning": "Giới hạn băng thông điều chế cực đại bị chặn bởi sự tắt dần phi tuyến"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_7_3, nom_data_2_7_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất trần băng thông cực đại từ điều kiện cực trị", "H3")
    add_p("Dẫn xuất tường minh vị trí cực đại của hàm băng thông điều chế theo tần số cộng hưởng:")

    eq_deriv_2_7_3a = r"f_{3\mathrm{dB}}(f_R) = f_R \sqrt{\left(1 - \frac{K^2 f_R^2}{8\pi^2}\right) + \sqrt{\left(1 - \frac{K^2 f_R^2}{8\pi^2}\right)^2 + 1}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu thức băng thông 3 dB toàn phần phụ thuộc K-factor và <i>f<sub>R</sub></i>:", eq_deriv_2_7_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_7_3b = r"\frac{\mathrm{d}f_{3\mathrm{dB}}}{\mathrm{d}f_R} = 0 \implies f_R^{\mathrm{opt}} = \frac{2\pi}{K} \implies \gamma = \frac{4\pi^2}{K}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điều kiện đạo hàm triệt tiêu xác định tần số cộng hưởng tối ưu:", eq_deriv_2_7_3b, styles=styles))
    add_spacer(6)

    eq_deriv_2_7_3c = r"f_{3\mathrm{dB},\max} = \frac{2\sqrt{2}\pi}{K} \approx \frac{8{,}885}{K} \quad (\text{với } K \text{ tính bằng ns, } f \text{ tính bằng GHz})"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Công thức xác lập trần băng thông cực đại nội tại của diode laser:", eq_deriv_2_7_3c, styles=styles))
    add_spacer(8)

    add_p(
        "Công thức <i>f</i><sub>3dB,max</sub> ≈ 8,88 · <i>K</i><sup>−1</sup> là một trong những định luật kinh điển và đẹp đẽ nhất "
        "của ngành vật lý laser bán dẫn. Nó khẳng định: "
        "để chế tạo một diode laser có băng thông điều chế 40 GHz, "
        "kỹ sư bắt buộc phải chế tạo được cấu trúc bán dẫn có <i>K</i>-factor nhỏ hơn 0,22 ns! "
        "Muốn hạ thấp <i>K</i>-factor, ta phải đồng thời rút ngắn thời gian sống photon <i>τ<sub>p</sub></i> (dùng hốc ngắn) "
        "và cực đại hóa độ lợi vi sai <i>a</i>."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận các giới hạn thực tế (RC Ký sinh & Vận chuyển hạt tải)", "H3")
    add_p(
        "So sánh ba rào cản hạn chế băng thông trong thực tế: "
        "<br/>1. <b>Giới hạn tắt dần nội tại (Damping Limit):</b> Bị chặn bởi <i>K</i>-factor (thường từ 30 đến 50 GHz trong laser giếng lượng tử biến dạng hiện đại). "
        "<br/>2. <b>Giới hạn ký sinh điện trở – điện dung (RC Parasitic Limit):</b> Tần số cắt của mạch lọc thông thấp hình thành bởi "
        "điện trở tiếp xúc <i>R<sub>s</sub></i> và điện dung ký sinh <i>C<sub>p</sub></i> của lớp tiếp giáp p-n: "
        "<i>f<sub>RC</sub></i> = [2<i>π R<sub>s</sub> C<sub>p</sub></i>]<sup>−1</sup>. "
        "Nếu <i>R<sub>s</sub></i> = 5 Ω và <i>C<sub>p</sub></i> = 2 pF, <i>f<sub>RC</sub></i> chỉ đạt khoảng 16 GHz, "
        "trở thành nút thắt cổ chai bóp nghẹt toàn bộ tiềm năng quang học nội tại. "
        "<br/>3. <b>Giải pháp công nghệ đỉnh cao:</b> Áp dụng cấu trúc giếng lượng tử biến dạng nén (Compressive Strained QW) "
        "để tách dải lỗ trống nặng và nhẹ, tăng vọt độ dốc vi sai <i>a</i>; "
        "đồng thời chế tạo điện cực coplanar trên đế bán cách điện (Semi-Insulating InP Substrate) "
        "để nén điện dung <i>C<sub>p</sub></i> xuống dưới 0,3 pF."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN & DỰ ĐOÁN LỖI SAI (BẪY ĐIỂM MÙ R&D)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")
    add_p(
        "Phần thử thách áp dụng phương pháp lập luận ba bước CER (Claim – Evidence – Reasoning) "
        "kết hợp mổ xẻ các lỗi tư duy kinh điển trong thiết kế module laser tốc độ cao:"
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
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.7.1: BẪY TĂNG BĂNG THÔNG BẰNG CÁCH TĂNG DÒNG BƠM VÔ HẠN</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống phản biện:</b> Một kỹ sư cho rằng vì tần số cộng hưởng <i>f<sub>R</sub> ∝ √(I − I</i><sub>th</sub>), "
            "ta chỉ cần tăng dòng bơm lên thật lớn (ví dụ gấp 10 lần dòng ngưỡng) là có thể đạt được băng thông điều chế 50 GHz cho tuyến truyền dẫn quang 100G.<br/>"
            "<b>1. Luận điểm (Claim):</b> Nhận định này hoàn toàn sai lầm và nguy hiểm; việc tăng dòng tiêm quá lớn không những không đạt được 50 GHz "
            "mà còn làm băng thông bị sụt giảm và linh kiện bị phá hủy nhiệt.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Hệ số tắt dần tăng theo bình phương tần số: <i>γ = K f<sub>R</sub></i><sup>2</sup>. "
            "Khi dòng bơm tăng cao, <i>γ</i> tăng vượt trội làm dập tắt đỉnh cộng hưởng (Overdamping). "
            "Đồng thời, hiệu ứng tự đốt nóng làm tăng nhiệt độ tiếp giáp, suy giảm độ dốc độ lợi <i>a(T)</i> "
            "và kéo <i>f<sub>R</sub></i> sụt giảm theo hiện tượng suy hao nhiệt Rollover.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Băng thông điều chế nội tại bị chặn đứng bởi trần <i>f</i><sub>max</sub> ≈ 8,88 · <i>K</i><sup>−1</sup>. "
            "Khi đạt tới điểm tắt dần tới hạn, việc tăng dòng bơm chỉ làm công suất tiêu tán Joule <i>I</i><sup>2</sup> <i>R<sub>s</sub></i> tăng vọt, "
            "nung nóng linh kiện và làm tăng hiện tượng dạt tần chirp, làm hỏng hoàn toàn phẩm chất truyền dẫn của hệ thống."
        ), styles["TableCell"])]
    ]
    t1 = he.Table(cer_card_1, colWidths=[he.PRINTABLE_WIDTH])
    t1.setStyle(cer_style)
    story.append(t1)
    add_spacer(10)

    cer_card_2 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.7.2: NÚT THẮT CỔ CHAI KÝ SINH RC VÀ ĐIỆN CẢM DÂY HÀN</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống chẩn đoán:</b> Một nhóm nghiên cứu chế tạo diode laser giếng lượng tử InGaAsP với thông số lý thuyết nội tại "
            "cho phép đạt <i>f</i><sub>3dB,max</sub> = 28 GHz. Tuy nhiên, khi đo trên máy phân tích mạng vector (VNA), "
            "đáp ứng tần số đo được bị suy giảm dốc đứng ngay tại 8 GHz. Hãy chẩn đoán nguyên nhân và đề xuất phương án khắc phục.<br/>"
            "<b>1. Luận điểm (Claim):</b> Nút thắt cổ chai nằm ở mạch lọc thông thấp hình thành bởi các phần tử ký sinh đóng gói: "
            "điện trở tiếp xúc <i>R<sub>s</sub></i>, điện dung tiếp xúc <i>C<sub>p</sub></i> và điện cảm dây hàn nối chip (Wire Bond Inductance <i>L<sub>b</sub></i>).<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Đáp ứng tần số tổng của module là tích của hàm truyền quang nội tại và hàm truyền ký sinh: "
            "<i>H</i><sub>tot</sub>(<i>ω</i>) = <i>H</i><sub>laser</sub>(<i>ω</i>) · [1 + <i>jω R<sub>s</sub> C<sub>p</sub></i> − <i>ω</i><sup>2</sup> <i>L<sub>b</sub> C<sub>p</sub></i>]<sup>−1</sup>. "
            "Nếu dây hàn dài 1 mm (<i>L<sub>b</sub></i> ≈ 1 nH) và pad tiếp xúc có <i>C<sub>p</sub></i> ≈ 1 pF, tần số cắt ký sinh chỉ rơi vào khoảng 5–8 GHz.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Dù vùng tích cực quang học có phản ứng tức thời ở tốc độ hàng chục GHz, "
            "nhưng tín hiệu dòng điện điều chế cao tần không thể nạp vào vùng giếng lượng tử vì bị nghẽn ở bộ lọc thông thấp ký sinh bên ngoài. "
            "Giải pháp bắt buộc: chuyển sang công nghệ hàn lật lật chip (Flip-Chip Bonding) trực tiếp lên đường truyền đồng phẳng Coplanar Waveguide (CPW) "
            "để triệt tiêu hoàn toàn dây hàn và hạ <i>C<sub>p</sub></i> xuống dưới 0,2 pF."
        ), styles["TableCell"])]
    ]
    t2 = he.Table(cer_card_2, colWidths=[he.PRINTABLE_WIDTH])
    t2.setStyle(cer_style)
    story.append(t2)
    add_spacer(10)

    cer_card_3 = [
        [Paragraph(he.wrap_math_glyphs("<b>THỬ THÁCH CER 2.7.3: TẠI SAO ỨNG SUẤT BIẾN DẠNG LẠI TĂNG BĂNG THÔNG ĐIỀU CHẾ?</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Tình huống vật lý:</b> Tại sao trong công nghệ chế tạo laser viễn thông tốc độ cao, "
            "người ta luôn sử dụng các giếng lượng tử biến dạng nén (Compressive Strained QW) thay vì giếng lượng tử phối mạng hoàn hảo (Lattice-Matched)?<br/>"
            "<b>1. Luận điểm (Claim):</b> Ứng suất nén làm thay đổi cấu trúc vùng năng lượng, làm giảm mật độ trạng thái dải hóa trị "
            "và tăng vọt độ lợi vi sai <i>a</i> (độ dốc độ lợi theo hạt tải), trực tiếp nâng cao tần số cộng hưởng <i>f<sub>R</sub></i> và hạ thấp <i>K</i>-factor.<br/>"
            "<b>2. Bằng chứng (Evidence):</b> Tần số cộng hưởng <i>ω<sub>R</sub></i> tỉ lệ với √<i>a</i>, và <i>K</i>-factor tỉ lệ nghịch với <i>a</i>: "
            "<i>K ∝ (τ<sub>p</sub> + ε · [v<sub>g</sub> a]</i><sup>−1</sup>). "
            "Khi có ứng suất nén 1–1,5%, độ lợi vi phân <i>a</i> của giếng lượng tử InGaAs/InP tăng từ 2 đến 3 lần so với cấu trúc không biến dạng.<br/>"
            "<b>3. Lập luận vi mô (Reasoning):</b> Trong bán dẫn khối hoặc giếng lượng tử thông thường, dải hóa trị có khối lượng hiệu dụng lớn (lỗ trống nặng), "
            "khiến mức Fermi giả dải hóa trị dịch chuyển rất chậm khi tiêm hạt tải. "
            "Ứng suất nén phá vỡ tính suy biến tại đỉnh dải hóa trị, đẩy dải lỗ trống nhẹ lên trên dải lỗ trống nặng, "
            "làm giảm khối lượng hiệu dụng của lỗ trống tại đỉnh dải. Nhờ đó, hạt tải phân bố tập trung hơn, "
            "dẫn đến tốc độ tăng trưởng độ lợi theo hạt tải (độ dốc <i>a</i>) bùng nổ, tạo nên những laser siêu nhanh đạt băng thông 40 GHz."
        ), styles["TableCell"])]
    ]
    t3 = he.Table(cer_card_3, colWidths=[he.PRINTABLE_WIDTH])
    t3.setStyle(cer_style)
    story.append(t3)
    add_spacer(14)

    # Lời kết luận học thuật
    conclusion_text = (
        "<b>KẾT LUẬN CHUYÊN KHẢO MỤC 2.7:</b> Động học điều chế tốc độ cao của diode laser là sự kết tinh "
        "giữa hiện tượng trao đổi năng lượng lượng tử hạt tải – photon và kỹ thuật vi ba bán dẫn tần số siêu cao. "
        "Nắm vững mối quan hệ giữa tần số cộng hưởng hồi phục <i>f<sub>R</sub></i>, hệ số tắt dần <i>K</i>-factor "
        "và các giới hạn ký sinh <i>RC</i> là nền tảng thiết kế cốt tử cho các kỹ sư quang điện tử trong kỷ nguyên mạng truyền dẫn quang Terabit."
    )
    add_p(conclusion_text, "Body")
    add_spacer(10)

    # Build document
    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename)/1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_7()

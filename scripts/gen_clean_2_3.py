# -*- coding: utf-8 -*-
"""
gen_clean_2_3.py
Chế bản chuyên khảo toàn văn PDF cho Mục 2.3: Phát xạ tự phát và vận hành linh kiện LED.
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

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.3.pdf")

# Tài nguyên hình ảnh
fig_goc_2_3 = os.path.join(img_dir, "[Goc]_Figure_2.3_So_do_phat_xa_va_phan_xa_toan_phan_trong_LED.png")
fig_sim_2_3a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.3_Hieu_Suat_Trich_Xuat_Quang_LED.png")
fig_sim_2_3b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.3_Pho_Phat_Xa_Tu_Phat_GaAs.png")


def build_monograph_muc_2_3():
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
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.3
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.3: Phát xạ tự phát và vận hành linh kiện LED (Spontaneous Photon Generation and LEDs)", "H2")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Quang học Phát xạ Tự phát &amp; LED"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 32–34)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Saleh &amp; Teich (Ch. 17) &amp; Sze (Ch. 12)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.3 (Chương 2)"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.3 khảo sát toàn diện quá trình sinh photon tự phát và các quy luật quang hình học "
        "chi phối hoạt động của diode phát quang (LED) cũng như trạng thái dưới ngưỡng của laser diode "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 32–34). "
        "Mục tiêu trọng tâm bao gồm 3 mắt xích vật lý: (1) Khảo sát phổ phát xạ tự phát lưỡng phân tử, xác lập định lượng độ dịch đỉnh phổ và độ rộng vạch phổ FWHM theo nhiệt năng Boltzmann; "
        "(2) Giải phẫu hiện tượng phản xạ toàn phần tại mặt phân giới phẳng bán dẫn – không khí, dẫn xuất công thức nón thoát Snell-Descartes; "
        "và (3) Thiết lập biểu thức hiệu suất trích xuất quang học ngoài, phân tích nghịch lý hiệu suất trích xuất chỉ dưới 2% ở bán dẫn dải cấm thẳng GaAs."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.3
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.3.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Phổ phát xạ tự phát &amp; Mở rộng nhiệt Boltzmann"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>R</i><sub>sp</sub>(<i>E</i>) ∝ (<i>E</i> − <i>E<sub>g</sub></i>)<sup>½</sup> exp(−(<i>E</i> − <i>E<sub>g</sub></i>) · (<i>k<sub>B</sub> T</i>)<sup>−1</sup>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng phổ phát xạ tự phát GaAs 300 K"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.3.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Nón thoát Snell &amp; Phản xạ toàn phần"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("sin <i>θ<sub>c</sub></i> = <i>n<sub>r</sub></i><sup>−1</sup>, <i>Ω<sub>c</sub></i> = 2π (1 − cos <i>θ<sub>c</sub></i>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.3 (Tr. 33) Sơ đồ nón thoát &amp; Phản xạ"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.3.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Hiệu suất trích xuất ngoài &amp; Công suất phát quang"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>η</i><sub>ext</sub> = <i>η</i><sub>int</sub> · (4 <i>n<sub>r</sub></i><sup>2</sup>)<sup>−1</sup>, <i>P</i><sub>out</sub> = <i>η</i><sub>ext</sub> <i>hν</i> · <i>I</i> · <i>q</i><sup>−1</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng <i>η</i><sub>ex</sub> theo chiết suất <i>n<sub>r</sub></i>"), styles["TableCellCenter"]),
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
    # LUẬN ĐIỂM 2.3.1: PHỔ PHÁT XẠ TỰ PHÁT & MỞ RỘNG NHIỆT
    # =========================================================================
    add_p("Luận điểm 2.3.1: Phổ phát xạ tự phát lưỡng phân tử và Sự mở rộng nhiệt Boltzmann", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm & Nghịch lý độ rộng vạch
    add_p("Giai đoạn 1: Giới thiệu khái niệm, phân bố năng lượng hạt tải và nghịch lý độ rộng vạch phổ", "H3")
    add_p(
        "Trong vật lý nguyên tử cổ điển, sự chuyển dời giữa hai mức năng lượng rời rạc phát ra một vạch phổ vô cùng đơn sắc. "
        "Tuy nhiên, trong chất bán dẫn tinh thể khối như GaAs, các mức năng lượng liên kết mở rộng thành các dải năng lượng liên tục. "
        "Khi phân cực thuận tiêm hạt tải vào vùng tích cực, các electron trong dải dẫn và lỗ trống trong dải hóa trị "
        "nhanh chóng nhiệt hóa (thermalize) trong thang thời gian pico-giây (10<sup>−13</sup> s) qua tương tác tán xạ phonon, "
        "phân bố theo các hàm phân bố giả Fermi-Dirac tiệm cận đuôi hàm mũ Maxwell-Boltzmann. "
        "Do đó, photon phát xạ tự phát không mang một tần số đơn nhất, mà trải rộng trên một dải năng lượng có độ rộng tỉ lệ trực tiếp với nhiệt độ tuyệt đối <i>T</i>."
    )
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ phổ phát xạ tự phát", "H3")
    add_p(
        "Phổ phát xạ tự phát <i>R</i><sub>sp</sub>(<i>E</i>) theo năng lượng photon <i>E = hν</i> "
        "là tích phân của mật độ trạng thái kết hợp khử tích (Joint Density of States) và xác suất chiếm chỗ hạt tải:"
    )

    pillar_eq_2_3_1 = r"R_{\mathrm{sp}}(E) \propto \sqrt{E - E_g} \exp\left(-\frac{E - E_g}{k_B T}\right) \quad (E \ge E_g), \quad \Delta E_{\mathrm{FWHM}} \approx 1{,}8\, k_B T"
    nom_data_2_3_1 = [
        {"name": "Mật độ phổ phát xạ tự phát", "symbol": "<i>R</i><sub>sp</sub>(<i>E</i>)", "unit": "cm<sup>−3</sup>·s<sup>−1</sup>·eV<sup>−1</sup>", "meaning": "Số photon tự phát sinh ra trên một đơn vị thể tích trong một giây trên một đơn vị năng lượng"},
        {"name": "Năng lượng photon phát xạ", "symbol": "<i>E</i>", "unit": "eV", "meaning": "Năng lượng photon tương ứng tần số quang học <i>E = hν</i>"},
        {"name": "Độ rộng vùng cấm", "symbol": "<i>E<sub>g</sub></i>", "unit": "eV", "meaning": "Ngưỡng năng lượng tối thiểu để xảy ra chuyển dời vùng–vùng"},
        {"name": "Độ rộng phổ bán công", "symbol": "<i>ΔE</i><sub>FWHM</sub>", "unit": "eV", "meaning": "Độ rộng vạch phổ đo tại vị trí một nửa cường độ cực đại"},
        {"name": "Nhiệt năng cơ bản", "symbol": "<i>k<sub>B</sub> T</i>", "unit": "eV", "meaning": "Độ tản mạn nhiệt năng lượng (≈ 25,85 meV tại 300 K)"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_3_1, nom_data_2_3_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất vị trí đỉnh phổ và bề rộng vạch phổ FWHM", "H3")
    add_p("Dẫn xuất tường minh vị trí cực đại của phổ phát xạ tự phát:")

    eq_deriv_2_3_1a = r"\frac{\mathrm{d}R_{\mathrm{sp}}(E)}{\mathrm{d}E} = 0 \implies \frac{\mathrm{d}}{\mathrm{d}E} \left[ (E - E_g)^{1/2} \exp\left(-\frac{E - E_g}{k_B T}\right) \right] = 0"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điều kiện cực trị đạo hàm bậc nhất của mật độ phổ:", eq_deriv_2_3_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_3_1b = r"\frac{1}{2 (E - E_g)^{1/2}} - \frac{(E - E_g)^{1/2}}{k_B T} = 0 \implies E_{\mathrm{peak}} = E_g + \frac{1}{2} k_B T"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Năng lượng tại đỉnh cực đại phát xạ tự phát:", eq_deriv_2_3_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_3_1c = r"\Delta\lambda_{\mathrm{FWHM}} \approx \frac{\lambda_0^2}{h c} \Delta E_{\mathrm{FWHM}} = \frac{\lambda_0^2}{h c} (1{,}8\, k_B T) \approx 30 - 40\ \mathrm{nm}\quad (\mathrm{GaAs\ 300\ K})"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chuyển đổi bề rộng phổ sang thang bước sóng:", eq_deriv_2_3_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Kết quả giải tích trên giải thích tường minh vì sao đỉnh phát xạ của LED không nằm chính xác tại độ rộng dải cấm <i>E<sub>g</sub></i>, "
        "mà luôn bị dịch chuyển về phía năng lượng cao hơn một lượng bằng <i>k<sub>B</sub> T · 2<sup>−1</sup></i> (khoảng 12,9 meV ở 300 K). "
        "Đồng thời, bề rộng phổ tự nhiên của LED ở nhiệt độ phòng luôn dao động trong khoảng 30–50 nm. "
        "Đây chính là nhược điểm căn bản của LED trong thông tin quang tốc độ cao: độ rộng phổ lớn gây tán sắc sắc độ (chromatic dispersion) "
        "nghiêm trọng khi lan truyền trong sợi quang."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.3b (Phổ phát xạ tự phát GaAs 300 K)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_3b,
        "Hình mô phỏng 2.3.1: Phổ phát xạ tự phát <i>R</i><sub>sp</sub>(<i>E</i>) của bán dẫn GaAs khối ở nhiệt độ phòng 300 K. "
        "Đồ thị định vị chính xác ngưỡng dải cấm <i>E<sub>g</sub></i> = 1,424 eV, đỉnh cực đại dịch lên <i>E</i><sub>peak</sub> ≈ 1,437 eV, "
        "và bề rộng vạch phổ FWHM ≈ 46 meV do sự phân bố nhiệt theo quy luật Boltzmann.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận nhiệt độ và dịch chuyển vạch phổ phát xạ", "H3")
    add_p(
        "Khảo sát hành vi của phổ phát xạ tự phát ở hai cực hạn nhiệt độ: "
        "<br/>1. <b>Nhiệt độ tiến về 0 K:</b> Nhiệt năng <i>k<sub>B</sub> T</i> triệt tiêu, hàm phân bố Boltzmann tiệm cận hàm bậc thang Dirac. "
        "Bề rộng phổ <i>ΔE</i><sub>FWHM</sub> co hẹp về 0, đỉnh phổ dịch sát về đúng bằng độ rộng vùng cấm <i>E<sub>g</sub>(0 K)</i>. "
        "<br/>2. <b>Nhiệt độ cao (<i>T</i> tăng từ 300 K lên 400 K):</b> Vùng cấm <i>E<sub>g</sub>(T)</i> bị thu hẹp theo quy luật Varshni, "
        "khiến bước sóng phát xạ bị dịch đỏ (redshift) với tốc độ khoảng 0,3 nm/K trong GaAs. "
        "Đồng thời, sự mở rộng nhiệt làm phổ trải rộng, làm loãng mật độ photon tại đỉnh phổ."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.3.2: NÓN THOÁT SNELL VÀ PHẢN XẠ TOÀN PHẦN
    # =========================================================================
    add_p("Luận điểm 2.3.2: Nón thoát quang học và Giới hạn phản xạ toàn phần Snell-Descartes", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm bẫy quang
    add_p("Giai đoạn 1: Giới thiệu khái niệm, nghịch lý bẫy quang học trong chất bán dẫn chiết suất cao", "H3")
    add_p(
        "Một trong những trở ngại lớn nhất trong công nghệ chiếu sáng bán dẫn là: mặc dù các photon tự phát được sinh ra "
        "với hiệu suất lượng tử nội <i>η</i><sub>int</sub> rất cao (lên tới 80–90% trong các giếng lượng tử chất lượng cao), "
        "nhưng phần lớn số photon này vĩnh viễn không bao giờ thoát được ra ngoài không khí. "
        "Nguyên nhân xuất phát từ định luật khúc xạ ánh sáng Snell-Descartes: chất bán dẫn III–V có chiết suất quang học cực kỳ cao "
        "(GaAs có <i>n<sub>r</sub></i> ≈ 3,65; InP có <i>n<sub>r</sub></i> ≈ 3,45). "
        "Khi ánh sáng đi từ môi trường chiết suất cao sang không khí (<i>n</i> = 1), góc tới hạn phản xạ toàn phần <i>θ<sub>c</sub></i> "
        "cực kỳ hẹp. Chỉ những tia sáng nằm trong một góc khối nón hình học rất nhỏ (Escape Cone) mới có cơ hội lọt ra ngoài."
    )
    add_spacer(8)

    # Embed Hình gốc 2.3
    story.append(he.embed_figure_with_caption(
        fig_goc_2_3,
        "Hình 2.3: Sơ đồ phát xạ ánh sáng và hiện tượng phản xạ toàn phần tại mặt phân giới bán dẫn – không khí trong linh kiện LED (Coldren &amp; Corzine, trang 33). "
        "Ba mắt xích hình học: (a) Vùng tích cực phát xạ đẳng hướng trong góc khối 4π; "
        "(b) Nón thoát quang học xác định bởi góc tới hạn <i>θ<sub>c</sub></i>; "
        "(c) Các tia sáng có góc tới lớn hơn <i>θ<sub>c</sub></i> bị phản xạ toàn phần và tiêu hao thành nhiệt.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ góc tới hạn và góc khối nón thoát", "H3")
    add_p(
        "Góc tới hạn phản xạ toàn phần <i>θ<sub>c</sub></i> và góc khối nón thoát <i>Ω<sub>c</sub></i> "
        "được thiết lập trực tiếp từ định luật Snell tại mặt phân giới phẳng bán dẫn – không khí:"
    )

    pillar_eq_2_3_2 = r"\sin\theta_c = \frac{1}{n_r}, \quad \Omega_c = 2\pi (1 - \cos\theta_c), \quad \eta_{\mathrm{ex}} = \frac{\Omega_c}{4\pi} = \frac{1 - \cos\theta_c}{2}"
    nom_data_2_3_2 = [
        {"name": "Góc tới hạn phản xạ toàn phần", "symbol": "<i>θ<sub>c</sub></i>", "unit": "độ (°)", "meaning": "Góc tới tối đa mà tại đó tia sáng còn có thể khúc xạ ra ngoài không khí"},
        {"name": "Chiết suất quang học bán dẫn", "symbol": "<i>n<sub>r</sub></i>", "unit": "không thứ nguyên", "meaning": "Tỷ số giữa vận tốc ánh sáng trong chân không và trong môi trường bán dẫn"},
        {"name": "Góc khối nón thoát", "symbol": "<i>Ω<sub>c</sub></i>", "unit": "steradian (sr)", "meaning": "Góc khối không gian ba chiều mà ánh sáng phát xạ có thể thoát ra ngoài"},
        {"name": "Hiệu suất trích xuất quang học", "symbol": "<i>η</i><sub>ex</sub>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ số photon thoát được ra ngoài không gian tự do trên một mặt phẳng"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_3_2, nom_data_2_3_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất xấp xỉ góc hẹp hiệu suất trích xuất", "H3")
    add_p("Dẫn xuất tường minh biểu thức xấp xỉ hiệu suất trích xuất cho môi trường chiết suất cao:")

    eq_deriv_2_3_2a = r"\cos\theta_c = \sqrt{1 - \sin^2\theta_c} = \sqrt{1 - \frac{1}{n_r^2}} \approx 1 - \frac{1}{2 n_r^2} \quad (n_r \gg 1)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển chuỗi Taylor căn bậc hai khi chiết suất lớn:", eq_deriv_2_3_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_3_2b = r"\eta_{\mathrm{ex}} = \frac{1 - \cos\theta_c}{2} \approx \frac{1 - \left(1 - \frac{1}{2 n_r^2}\right)}{2} = \frac{1}{4 n_r^2}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu thức kinh điển hiệu suất trích xuất nón thoát một mặt:", eq_deriv_2_3_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_3_2c = r"n_{\mathrm{GaAs}} = 3{,}65 \implies \theta_c = \arcsin\left(\frac{1}{3{,}65}\right) \approx 15{,}9^\circ \implies \eta_{\mathrm{ex}} \approx \frac{1}{4(3{,}65)^2} \approx 1{,}88\%"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay số cụ thể cho chất bán dẫn GaAs:", eq_deriv_2_3_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Con số 1,88% là một kết quả gây sốc đối với các kỹ sư quang điện tử: "
        "trên 98% số photon phát xạ tự phát sinh ra bên trong phiến bán dẫn phẳng bị giam cầm vĩnh viễn "
        "bởi phản xạ toàn phần nội. Các tia sáng phản xạ liên tục giữa hai mặt đáy và mặt lưng, "
        "cuối cùng bị tái hấp thụ bởi lớp đế hoặc tái hợp vô ích sinh nhiệt."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận hình học nón thoát và bẫy sóng dẫn đường", "H3")
    add_p(
        "Khảo sát hành vi của tia sáng ở các góc tới khác nhau đối chiếu với nón thoát: "
        "<br/>1. <b>Tia sáng trong nón thoát (<i>θ</i> nhỏ hơn <i>θ<sub>c</sub></i>):</b> Tia sáng khúc xạ trực tiếp ra không khí. Tuy nhiên, hệ số phản xạ Fresnel tại góc tới 0 độ <i>R = (n − 1)<sup>2</sup> · (n + 1)<sup>−2</sup></i> ≈ 32% đối với GaAs vẫn cản trở gần một phần ba lượng ánh sáng này, đòi hỏi phải phủ màng chống phản xạ AR. "
        "<br/>2. <b>Tia sáng ngoài nón thoát (<i>θ</i> lớn hơn <i>θ<sub>c</sub></i>):</b> Toàn bộ năng lượng phản xạ 100% quay trở lại lòng khối bán dẫn. Khối bán dẫn phẳng vô tình biến thành một ống dẫn sóng phẳng giam cầm ánh sáng, buộc người thiết kế phải phá vỡ tính đối xứng phẳng bằng kỹ thuật tạo cấu trúc kim tự tháp micro."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.3.3: HIỆU SUẤT LƯỢNG TỬ NGOÀI VÀ CÔNG NGHỆ TRÍCH XUẤT
    # =========================================================================
    add_p("Luận điểm 2.3.3: Hiệu suất lượng tử ngoài và Các giải pháp đột phá trích xuất ánh sáng", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm hiệu suất ngoài
    add_p("Giai đoạn 1: Giới thiệu khái niệm hiệu suất lượng tử ngoài và công suất phát xạ vĩ mô", "H3")
    add_p(
        "Hiệu suất lượng tử ngoài <i>η</i><sub>ext</sub> (External Quantum Efficiency - EQE) là thước đo cuối cùng "
        "đánh giá chất lượng của một linh kiện phát quang, định nghĩa bằng tỷ số giữa số photon thực tế đo được ngoài không gian "
        "và số electron tiêm vào linh kiện qua dòng điện ngoài. "
        "Nó là tích số của hiệu suất lượng tử nội <i>η</i><sub>int</sub> và hiệu suất trích xuất quang học <i>η</i><sub>ex</sub>."
    )
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hiệu suất lượng tử ngoài", "H3")
    add_p(
        "Mối quan hệ liên chuỗi giữa công suất phát quang ngõ ra <i>P</i><sub>out</sub>, dòng tiêm <i>I</i> và các hiệu suất thành phần:"
    )

    pillar_eq_2_3_3 = r"\eta_{\mathrm{ext}} = \eta_{\mathrm{int}} \cdot \eta_{\mathrm{ex}} \approx \frac{\eta_{\mathrm{int}}}{4 n_r^2}, \quad P_{\mathrm{out}} = \eta_{\mathrm{ext}} \frac{h\nu}{q} I = \eta_{\mathrm{int}} \eta_{\mathrm{ex}} \frac{h\nu}{q} I"
    nom_data_2_3_3 = [
        {"name": "Hiệu suất lượng tử ngoài", "symbol": "<i>η</i><sub>ext</sub>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ photon thu được ở ngoài linh kiện trên số hạt tải tiêm"},
        {"name": "Hiệu suất lượng tử nội", "symbol": "<i>η</i><sub>int</sub>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ hạt tải tiêm tái hợp phát ra photon tự phát <i>η</i><sub>int</sub> = <i>η<sub>i</sub> B N</i><sup>2</sup> · <i>R(N)</i><sup>−1</sup>"},
        {"name": "Công suất bức xạ quang ngõ ra", "symbol": "<i>P</i><sub>out</sub>", "unit": "W", "meaning": "Tổng công suất quang trích xuất được ra ngoài không gian tự do"},
        {"name": "Năng lượng photon phát xạ", "symbol": "<i>hν</i>", "unit": "J (hoặc eV)", "meaning": "Năng lượng của một lượng tử ánh sáng phát xạ"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_3_3, nom_data_2_3_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất các giải pháp kỹ thuật phá vỡ giới hạn Snell", "H3")
    add_p("Các giải pháp công nghệ nâng cao hiệu suất trích xuất ánh sáng:")

    eq_deriv_2_3_3a = r"\text{Vỏ bọc Epoxy } (n_{\mathrm{epoxy}} \approx 1{,}5): \quad \theta_c' = \arcsin\left(\frac{1{,}5}{3{,}65}\right) \approx 24{,}3^\circ \implies \eta_{\mathrm{ex}}' \approx n_{\mathrm{epoxy}}^2 \eta_{\mathrm{ex}} \approx 2{,}25 \times \eta_{\mathrm{ex}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hiệu quả tăng nón thoát của thấu kính vòm Epoxy:", eq_deriv_2_3_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_3_3b = r"\text{Linh kiện RC-LED: } \quad F_P = \frac{3}{4\pi^2} \left(\frac{\lambda}{n}\right)^3 \frac{Q}{V_{\mathrm{mode}}} \implies \eta_{\mathrm{int}} \to 95\%, \quad \eta_{\mathrm{ex}} \to 20 - 30\%"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hiệu ứng Purcell trong hốc cộng hưởng micro-cavity RC-LED:", eq_deriv_2_3_3b, styles=styles))
    add_spacer(8)

    add_p(
        "Chuỗi giải pháp trên mở ra lộ trình phát triển của ngành công nghiệp LED hiện đại: "
        "<br/>1. Đóng gói vòm cầu epoxy hoặc silicone giúp nâng hiệu suất trích xuất lên gấp 2,25 lần nhờ thu hẹp độ chênh lệch chiết suất. "
        "<br/>2. Tạo bề mặt nhám gồ ghề (surface texturing) hoặc cấu trúc tinh thể quang tử (photonic crystals) để tán xạ ngẫu nhiên các tia sáng phản xạ toàn phần, cho phép chúng đổi góc và thoát ra ngoài sau nhiều lần va chạm. "
        "<br/>3. Chế tạo LED hốc cộng hưởng (Resonant Cavity LED - RC-LED) sử dụng gương Bragg phân bố DBR để tái định hướng trường phát xạ tự phát vào trục thẳng đứng."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.3a (Hiệu suất trích xuất theo chiết suất)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_3a,
        "Hình mô phỏng 2.3.2: Hiệu suất trích xuất ánh sáng <i>η</i><sub>ex</sub> qua một mặt phẳng theo chiết suất bán dẫn <i>n<sub>r</sub></i>. "
        "Đồ thị đối chiếu giữa công thức giải tích chính xác và xấp xỉ góc hẹp (4 <i>n<sub>r</sub></i><sup>2</sup>)<sup>−1</sup>. "
        "Mốc vật liệu GaAs (<i>n</i> = 3,65) định vị rõ giới hạn vật lý 1,92%, minh chứng sự cần thiết của các công nghệ tạo vân nhám bề mặt và thấu kính đóng gói.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận chiết suất và ranh giới giữa LED và Laser", "H3")
    add_p(
        "So sánh bản chất tiệm cận giữa hai linh kiện: "
        "<br/>• <b>Đối với LED:</b> Ánh sáng là bức xạ tự phát đẳng hướng không kết hợp. Hiệu suất trích xuất bị trói buộc bởi nón thoát Snell-Descartes. Dù dòng tiêm tăng cao đến đâu, hiệu suất trích xuất vẫn giữ nguyên ở mức vài phần trăm. "
        "<br/>• <b>Đối với Laser Diode:</b> Khi đạt ngưỡng, phát xạ kích thích vượt trội hoàn toàn. Các photon được sinh ra đồng pha, kết hợp và định hướng hoàn hảo dọc theo trục ống dẫn sóng quang. Hiệu suất trích xuất qua gương phản xạ hốc cộng hưởng (gương cleaved facet) đạt tới 70–90%, xóa bỏ hoàn toàn giới hạn nón thoát của LED."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN CER & ĐIỂM MÙ THIẾT KẾ
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")

    cer_card = [
        [Paragraph(he.wrap_math_glyphs("<b>BÀI TOÁN THỬ THÁCH CHẨN ĐOÁN CER 2.3: NGHỊCH LÝ HIỆU SUẤT TRÍCH XUẤT CỦA LED MẶT ĐÁY VÀ BẪY BỀ MẶT NHẴN</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Bối cảnh bài toán R&amp;D:</b> Một nhóm nghiên cứu chế tạo chip LED công suất cao GaAs với bề mặt được đánh bóng gương quang học hoàn hảo (độ nhám bề mặt dưới 1 nm). "
            "Nhóm đo kiểm và kỳ vọng rằng bề mặt càng nhẵn bóng thì ánh sáng thoát ra càng ít bị tán xạ tổn hao, từ đó công suất phát quang sẽ đạt cực đại. "
            "Tuy nhiên, kết quả đo kiểm thực nghiệm cho thấy hiệu suất lượng tử ngoài EQE chỉ đạt 2,1%. "
            "Sau đó, một kỹ sư trẻ cố tình ăn mòn hóa học làm nhám xù xì bề mặt chip thì hiệu suất EQE đo được lại tăng vọt lên 18,5%.<br/><br/>"
            "• <b>Luận điểm (Claim):</b> Nhận định ban đầu của nhóm nghiên cứu về bề mặt nhẵn bóng quang học có sai lầm không? Bản chất vật lý vi mô nào giải thích sự nhảy vọt hiệu suất khi bề mặt bị làm nhám?<br/>"
            "• <b>Bằng chứng (Evidence):</b> Dựa vào quỹ đạo tia sáng phản xạ toàn phần giữa hai mặt phẳng song song lý tưởng và định luật bảo toàn góc tới hạn <i>θ<sub>c</sub></i> qua các lần phản xạ liên tiếp.<br/>"
            "• <b>Lập luận (Reasoning):</b> Phân tích cơ chế tái phân bố góc tới (Angle Randomization) khi photon va chạm vào bề mặt nhám đa diện, từ đó tạo cơ hội cho các photon bị bẫy rơi trở lại vào nón thoát quang học."
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

    # Khâu nối biên độ DOC (Transition Anchor sang Mục 2.4)
    add_p(
        "<b>Khâu nối biên độ và Tiền đề chuyển tiếp sang Mục 2.4:</b> "
        "Mục 2.3 đã làm sáng tỏ cơ chế phát xạ tự phát và nguyên nhân vì sao LED bị giới hạn bởi nón thoát quang học. "
        "Để vượt qua giới hạn này và đạt tới phát xạ kích thích kết hợp, ta bắt buộc phải giam giữ photon bên trong một hốc cộng hưởng quang học (Optical Cavity). "
        "Làm thế nào để photon được giữ lại và phản hồi liên tục giữa hai đầu gương? "
        "Độ lợi quang học và các kênh tổn hao nội, tổn hao gương được cân bằng như thế nào? "
        "Toàn bộ các nguyên lý nền tảng này sẽ được giải phẫu trong <b>Mục 2.4: Sinh và tổn hao photon trong hốc cộng hưởng laser</b>."
    )

    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename) / 1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_3()

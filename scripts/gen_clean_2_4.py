# -*- coding: utf-8 -*-
"""
gen_clean_2_4.py
Chế bản chuyên khảo toàn văn PDF cho Mục 2.4: Sinh và tổn hao photon trong hốc cộng hưởng laser.
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

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.4.pdf")

# Tài nguyên hình ảnh
fig_goc_2_4 = os.path.join(img_dir, "[Goc]_Figure_2.4_So_do_cau_truc_laser_in_plane_va_VCSEL.png")
fig_goc_2_5 = os.path.join(img_dir, "[Goc]_Figure_2.5_Dinh_nghia_he_so_khuech_dai_quang_vi_phan_dz.png")
fig_sim_2_4a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.4_Ton_Hao_Guong_Theo_Chieu_Dai_Hoc.png")
fig_sim_2_4b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.4_Thoi_Gian_Song_Photon_Trong_Hoc.png")


def build_monograph_muc_2_4():
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
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.4
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.4: Sinh và tổn hao photon trong hốc cộng hưởng laser (Photon Generation and Loss in Laser Cavities)", "H2")
    add_spacer(6)

    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Quang học Hốc Cộng hưởng &amp; Tổn hao"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 34–37)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Yariv (Ch. 5 &amp; 15) &amp; Sze (Ch. 12)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.4 (Chương 2)"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.4 phân tích cơ chế vật lý của sự tương tác giữa sóng ánh sáng lan truyền "
        "và môi trường khuếch đại bên trong hốc cộng hưởng quang học của laser diode "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 34–37). "
        "Hệ thống khảo sát tường minh 3 mắt xích then chốt: (1) Cấu trúc hình học của hốc Fabry-Pérot truyền thống phát xạ mép (In-plane) "
        "đối sánh với hốc cộng hưởng vi mô phát xạ bề mặt (VCSEL); (2) Phương trình vi phân truyền sóng quang vi sai dọc trục <i>z</i>, "
        "thiết lập định nghĩa hệ số giam giữ quang học <i>Γ</i> và độ lợi mode <i>Γ g</i>; "
        "và (3) Giải phẫu toàn bộ các kênh tiêu tán photon, dẫn xuất biểu thức tổn hao gương <i>α<sub>m</sub></i> và thời gian sống photon <i>τ<sub>p</sub></i>."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.4
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.4.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Cấu trúc hốc cộng hưởng: In-plane vs. VCSEL"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("2 <i>β L</i> = 2 <i>m</i> π, <i>Δλ</i> = <i>λ</i><sub>0</sub><sup>2</sup> · (2 <i>n<sub>g</sub> L</i>)<sup>−1</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.4 (Tr. 35) Sơ đồ In-plane &amp; VCSEL"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.4.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Khuếch đại quang vi phân &amp; Độ lợi mode <i>Γ g</i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("d<i>P</i> · (d<i>z</i>)<sup>−1</sup> = (<i>Γ g</i> − ⟨<i>α<sub>i</sub></i>⟩) <i>P</i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.5 (Tr. 36) Khuếch đại vi phân d<i>z</i>"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.4.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Tổn hao gương <i>α<sub>m</sub></i> &amp; Thời gian sống photon <i>τ<sub>p</sub></i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>α<sub>m</sub></i> = (2<i>L</i>)<sup>−1</sup> ln((<i>R</i><sub>1</sub> <i>R</i><sub>2</sub>)<sup>−1</sup>), <i>τ<sub>p</sub></i><sup>−1</sup> = <i>v<sub>g</sub></i> (⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>)"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng <i>α<sub>m</sub>(L)</i> &amp; <i>τ<sub>p</sub>(α)</i>"), styles["TableCellCenter"]),
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
    # LUẬN ĐIỂM 2.4.1: CẤU TRÚC HỐC CỘNG HƯỞNG FABRY-PEROT VÀ VCSEL
    # =========================================================================
    add_p("Luận điểm 2.4.1: Cấu trúc hốc cộng hưởng Fabry-Pérot và Phân loại Laser In-plane vs. VCSEL", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm & Cơ chế phản hồi quang học
    add_p("Giai đoạn 1: Giới thiệu khái niệm, nguyên lý phản hồi quang học và sự chọn lọc mode dọc", "H3")
    add_p(
        "Một môi trường có độ lợi quang học thuần túy chỉ đóng vai trò như một bộ khuếch đại quang học (Optical Amplifier). "
        "Để chuyển hóa từ trạng thái khuếch đại sang trạng thái tự dao động phát laser, "
        "hệ thống bắt buộc phải có cơ chế phản hồi dương quang học (optical positive feedback). "
        "Cơ chế này được hiện thực hóa bằng cách đặt môi trường khuếch đại bên trong một hốc cộng hưởng quang học. "
        "Ánh sáng lan truyền dọc trục sẽ liên tục được phản xạ qua lại giữa hai đầu gương, "
        "chỉ những bước sóng thỏa mãn điều kiện giao thoa tăng cường (pha quay về sau một vòng round-trip là bội số nguyên của 2π) "
        "mới có thể tồn tại và hình thành các mode sóng đứng dọc (longitudinal modes)."
    )
    add_spacer(8)

    # Embed Hình gốc 2.4
    story.append(he.embed_figure_with_caption(
        fig_goc_2_4,
        "Hình 2.4: So sánh cấu trúc hốc cộng hưởng của hai họ diode laser tiêu biểu (Coldren &amp; Corzine, trang 35). "
        "Ba mắt xích cấu trúc: (a) Laser trong mặt phẳng phát xạ mép (In-plane / Edge-emitting) với chiều dài hốc lớn <i>L</i> ≈ 250–500 μm; "
        "(b) Laser phát xạ bề mặt hốc đứng (VCSEL) với hốc vi mô siêu ngắn <i>L</i> ≈ 1–2 μm kẹp giữa hai gương phản xạ DBR đa lớp; "
        "(c) Sự định hướng vuông góc của dòng tiêm và trục lan truyền photon giữa hai cấu hình.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ điều kiện cộng hưởng pha", "H3")
    add_p(
        "Điều kiện cộng hưởng sóng đứng và khoảng cách giữa hai mode dọc liên tiếp trong hốc Fabry-Pérot:"
    )

    pillar_eq_2_4_1 = r"2 \beta L = 2 m \pi \implies m \frac{\lambda_0}{2 n_r} = L, \quad \Delta\lambda = \frac{\lambda_0^2}{2 n_g L}"
    nom_data_2_4_1 = [
        {"name": "Hằng số truyền sóng quang học", "symbol": "<i>β</i>", "unit": "rad·cm<sup>−1</sup>", "meaning": "Độ dịch pha của sóng trên một đơn vị chiều dài <i>β = 2π n<sub>r</sub> · λ</i><sub>0</sub><sup>−1</sup>"},
        {"name": "Chiều dài hốc cộng hưởng", "symbol": "<i>L</i>", "unit": "cm (hoặc μm)", "meaning": "Khoảng cách vật lý giữa hai mặt gương phản xạ"},
        {"name": "Bậc mode cộng hưởng dọc", "symbol": "<i>m</i>", "unit": "số nguyên", "meaning": "Số lượng nửa bước sóng quang học chứa vừa vặn trong hốc"},
        {"name": "Khoảng cách mode dọc", "symbol": "<i>Δλ</i>", "unit": "nm", "meaning": "Độ chênh lệch bước sóng giữa hai mode sóng đứng kề nhau"},
        {"name": "Chiết suất nhóm quang học", "symbol": "<i>n<sub>g</sub></i>", "unit": "không thứ nguyên", "meaning": "Chiết suất hiệu dụng tính đến tán sắc vật liệu <i>n<sub>g</sub> = n<sub>r</sub> − λ</i><sub>0</sub> · (d<i>n<sub>r</sub></i> · (d<i>λ</i>)<sup>−1</sup>)"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_4_1, nom_data_2_4_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất khoảng cách mode dọc theo chiết suất nhóm", "H3")
    add_p("Dẫn xuất vi phân khoảng cách mode giữa hai mode dọc kề nhau m và m + 1:")

    eq_deriv_2_4_1a = r"\nu_m = m \frac{c}{2 n_r L} \implies \Delta\nu = \nu_{m+1} - \nu_m \approx \frac{c}{2 n_g L}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khoảng cách tần số quang giữa hai mode dọc liên tiếp:", eq_deriv_2_4_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_4_1b = r"|\Delta\lambda| = \frac{\lambda_0^2}{c} \Delta\nu = \frac{\lambda_0^2}{2 n_g L}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chuyển đổi vi phân từ tần số sang bước sóng chân không:", eq_deriv_2_4_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_4_1c = r"\text{Laser In-plane } (L = 300\ \mu\mathrm{m}): \Delta\lambda \approx \frac{(0{,}85)^2}{2(4{,}0)(300)} \approx 0{,}30\ \mathrm{nm}; \quad \text{VCSEL } (L = 1{,}5\ \mu\mathrm{m}): \Delta\lambda \approx 60\ \mathrm{nm}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đối sánh khoảng cách mode giữa Laser In-plane và VCSEL:", eq_deriv_2_4_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Chuỗi dẫn xuất định lượng trên vạch rõ sự khác biệt bản chất giữa hai họ linh kiện: "
        "<br/>• <b>Laser phát xạ mép (In-plane):</b> Vì hốc dài (<i>L</i> = 300 μm), khoảng cách mode <i>Δλ</i> rất hẹp (chỉ khoảng 0,3 nm). "
        "Bên dưới dải phổ độ lợi rộng khoảng vài chục nanomet của bán dẫn có thể chứa tới hàng trăm mode dọc, khiến laser dễ vận hành đa mode (multimode). "
        "<br/>• <b>VCSEL:</b> Vì chiều dài hốc vi mô siêu ngắn (<i>L</i> ≈ 1–2 μm), khoảng cách mode <i>Δλ</i> lên tới 60 nm, "
        "vượt xa bề rộng dải phổ độ lợi. Do đó, chỉ có duy nhất một mode dọc duy nhất nằm lọt vào vùng độ lợi, "
        "bảo đảm linh kiện phát đơn mode dọc tuyệt đối (single longitudinal mode)."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận chiều dài hốc và đánh đổi công nghệ", "H3")
    add_p(
        "Đánh đổi thiết kế giữa laser in-plane và VCSEL: "
        "<br/>1. <b>Hốc cực dài (In-plane <i>L</i> > 1000 μm):</b> Thể tích vùng tích cực lớn giúp tản nhiệt tốt, chịu được công suất quang cao hàng watt, "
        "nhưng dòng ngưỡng tuyệt đối cao do thể tích lớn. "
        "<br/>2. <b>Hốc siêu ngắn (VCSEL <i>L</i> < 2 μm):</b> Thể tích nhỏ giúp dòng ngưỡng cực thấp (dưới 1 mA), "
        "chùm tia tròn góc phân kỳ nhỏ dễ ghép vào sợi quang, kiểm thử trực tiếp trên phiến wafer (on-wafer testing) giảm 80% chi phí đóng gói."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.4.2: KHUẾCH ĐẠI QUANG DỌC TRỤC VÀ ĐỘ LỢI MODE
    # =========================================================================
    add_p("Luận điểm 2.4.2: Cơ chế khuếch đại quang dọc trục vi phân và Định nghĩa độ lợi mode Γ g", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm tăng trưởng quang
    add_p("Giai đoạn 1: Giới thiệu khái niệm, tăng trưởng cường độ vi phân dọc trục và hệ số giam giữ", "H3")
    add_p(
        "Khi sóng quang lan truyền dọc theo trục <i>z</i> của ống dẫn sóng, trường điện từ trải rộng trong không gian ba chiều "
        "vượt ra ngoài ranh giới vùng tích cực. Vùng tích cực chỉ chiếm một phần tiết diện ngang của mode quang. "
        "Chỉ có phần năng lượng trường quang nằm đè lên vùng tích cực mới nhận được sự khuếch đại kích thích từ các hạt tải đảo lộn mật độ. "
        "Phần năng lượng còn lại lan truyền trong các lớp bao bị suy hao do hấp thụ hạt tải tự do và tán xạ bề mặt. "
        "Do đó, khái niệm hệ số giam giữ quang học <i>Γ</i> (Optical Confinement Factor) và độ lợi mode <i>Γ g</i> "
        "đóng vai trò là cầu nối định lượng giữa độ lợi vật liệu vi mô <i>g</i> và sự tăng trưởng quang học thực tế vĩ mô."
    )
    add_spacer(8)

    # Embed Hình gốc 2.5
    story.append(he.embed_figure_with_caption(
        fig_goc_2_5,
        "Hình 2.5: Định nghĩa vi phân hệ số khuếch đại quang học và tổn hao dọc theo một lát cắt chiều dài d<i>z</i> trong ống dẫn sóng laser (Coldren &amp; Corzine, trang 36). "
        "Ba mắt xích vật lý: (a) Công suất quang ngõ vào <i>P(z)</i>; "
        "(b) Sự khuếch đại tỷ lệ với độ lợi mode <i>Γ g</i> và suy hao nội ⟨<i>α<sub>i</sub></i>⟩ trong vi phân d<i>z</i>; "
        "(c) Công suất quang ngõ ra <i>P(z +</i> d<i>z)</i> biểu diễn định luật tăng trưởng hàm mũ Beer-Lambert mở rộng.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ phương trình truyền sóng quang vi sai", "H3")
    add_p(
        "Phương trình vi phân mô tả sự biến thiên công suất quang dọc theo trục lan truyền <i>z</i>:"
    )

    pillar_eq_2_4_2 = r"\frac{\mathrm{d}P}{\mathrm{d}z} = \left(\Gamma g - \langle\alpha_i\rangle\right) P \implies P(z) = P(0) \exp\left[\left(\Gamma g - \langle\alpha_i\rangle\right) z\right]"
    nom_data_2_4_2 = [
        {"name": "Công suất sóng quang học dọc trục", "symbol": "<i>P(z)</i>", "unit": "W", "meaning": "Thông lượng năng lượng quang truyền qua tiết diện ngang tại tọa độ <i>z</i>"},
        {"name": "Hệ số giam giữ quang học", "symbol": "<i>Γ</i>", "unit": "không thứ nguyên", "meaning": "Tỷ số tích phân cường độ trường quang trong vùng tích cực trên toàn không gian"},
        {"name": "Độ lợi quang học vật liệu", "symbol": "<i>g</i>", "unit": "cm<sup>−1</sup>", "meaning": "Hệ số khuếch đại phát xạ kích thích nội tại của chất bán dẫn"},
        {"name": "Độ lợi mode quang học", "symbol": "<i>Γ g</i>", "unit": "cm<sup>−1</sup>", "meaning": "Độ lợi hiệu dụng thực tế mà mode quang nhận được khi truyền sóng"},
        {"name": "Hệ số tổn hao nội trung bình", "symbol": "⟨<i>α<sub>i</sub></i>⟩", "unit": "cm<sup>−1</sup>", "meaning": "Hấp thụ hạt tải tự do và tán xạ tại các mặt dị tiếp xúc"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_4_2, nom_data_2_4_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất hệ số giam giữ quang học Γ từ tích phân Poynting", "H3")
    add_p("Dẫn xuất định nghĩa hệ số giam giữ quang học từ thông lượng vector Poynting:")

    eq_deriv_2_4_2a = r"\Gamma \equiv \frac{\iint_{\mathrm{active}} |E(x, y)|^2 \, \mathrm{d}x\mathrm{d}y}{\iint_{-\infty}^{\infty} |E(x, y)|^2 \, \mathrm{d}x\mathrm{d}y}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Định nghĩa tỷ lệ tích phân mật độ năng lượng trường quang:", eq_deriv_2_4_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_4_2b = r"\Gamma_{\mathrm{DH}} \approx \frac{D^2}{2 + D^2}, \quad D = k_0 d \sqrt{n_{\mathrm{act}}^2 - n_{\mathrm{cladd}}^2}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Xấp xỉ hệ số giam giữ trong dị thể kép DH bề dày d:", eq_deriv_2_4_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_4_2c = r"d = 200\ \mathrm{nm} \implies \Gamma \approx 0{,}30 - 0{,}40; \quad d = 10\ \mathrm{nm}\ (\mathrm{QW}) \implies \Gamma \approx 0{,}01 - 0{,}03"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: So sánh giá trị Gamma giữa tiếp giáp dị thể kép DH và giếng lượng tử:", eq_deriv_2_4_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Kết quả trên chỉ ra một nghịch lý kỹ thuật quan trọng: khi ta thu nhỏ bề dày vùng tích cực xuống cỡ giếng lượng tử (10 nm) "
        "để giảm thể tích và giảm dòng ngưỡng, hệ số giam giữ quang học <i>Γ</i> bị tụt dốc thảm hại từ 0,35 xuống chỉ còn 0,02. "
        "Để bù đắp lại sự sụt giảm <i>Γ</i> này, các nhà thiết kế bắt buộc phải phát minh ra cấu trúc dẫn sóng dị thể giam giữ tách biệt "
        "(Separate Confinement Heterostructure - SCH), trong đó giếng lượng tử mỏng được bao bọc bởi một lớp lõi dẫn sóng trung gian dày hơn."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận độ lợi ròng và ngưỡng khuếch đại", "H3")
    add_p(
        "Khảo sát dấu của số mũ tăng trưởng (<i>Γ g</i> − ⟨<i>α<sub>i</sub></i>⟩): "
        "<br/>1. <b>Miền hấp thụ suy hao (<i>Γ g</i> nhỏ hơn ⟨<i>α<sub>i</sub></i>⟩):</b> Sóng quang bị suy giảm theo hàm mũ khi lan truyền. Năng lượng ánh sáng bị dập tắt nhanh chóng dọc theo trục <i>z</i>. "
        "<br/>2. <b>Miền khuếch đại ròng (<i>Γ g</i> lớn hơn ⟨<i>α<sub>i</sub></i>⟩):</b> Công suất quang tăng trưởng bùng nổ theo hàm mũ. Đây là điều kiện tiên quyết để tích lũy năng lượng bù đắp cho tổn hao gương tại hai đầu hốc."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.4.3: TỔN HAO GƯƠNG VÀ THỜI GIAN SỐNG PHOTON
    # =========================================================================
    add_p("Luận điểm 2.4.3: Các kênh tổn hao photon, Tổn hao gương α_m và Thời gian sống photon τ_p", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm chu trình vòng tròn round-trip
    add_p("Giai đoạn 1: Giới thiệu khái niệm, chu trình truyền sóng khép kín round-trip và tổn hao gương", "H3")
    add_p(
        "Để duy trì dao động laser dừng, sóng ánh sáng sau khi thực hiện trọn vẹn một chu trình khép kín (round-trip) "
        "— xuất phát từ gương 1, truyền qua chiều dài hốc <i>L</i> đến phản xạ tại gương 2, "
        "rồi truyền ngược lại chiều dài <i>L</i> để phản xạ tại gương 1 — phải bảo toàn năng lượng và pha. "
        "Tại hai đầu gương, một phần công suất quang bị truyền qua mặt gương thoát ra ngoài (chính là chùm tia laser hữu ích ngõ ra). "
        "Đối với năng lượng bên trong hốc, phần thoát ra này được xem như một kênh tổn hao phân bố tương đương, gọi là tổn hao gương <i>α<sub>m</sub></i>."
    )
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ tổn hao gương và thời gian sống photon", "H3")
    add_p(
        "Hệ thức giải tích xác định hệ số tổn hao gương phân bố <i>α<sub>m</sub></i> và thời gian sống photon trong hốc <i>τ<sub>p</sub></i>:"
    )

    pillar_eq_2_4_3 = r"\alpha_m = \frac{1}{2 L} \ln\left(\frac{1}{R_1 R_2}\right), \quad \frac{1}{\tau_p} = v_g \left(\langle\alpha_i\rangle + \alpha_m\right) = v_g \alpha_{\mathrm{tot}}"
    nom_data_2_4_3 = [
        {"name": "Hệ số tổn hao gương phân bố", "symbol": "<i>α<sub>m</sub></i>", "unit": "cm<sup>−1</sup>", "meaning": "Tổn hao tương đương trên một đơn vị chiều dài do ánh sáng thoát qua hai mặt gương"},
        {"name": "Hệ số phản xạ công suất gương 1 và 2", "symbol": "<i>R</i><sub>1</sub>, <i>R</i><sub>2</sub>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ công suất quang được phản xạ ngược lại lòng hốc tại hai mặt phân giới"},
        {"name": "Thời gian sống photon trong hốc", "symbol": "<i>τ<sub>p</sub></i>", "unit": "s (hoặc ps)", "meaning": "Thời gian trung bình một photon tồn tại trong hốc trước khi bị hấp thụ hoặc thoát ra ngoài"},
        {"name": "Vận tốc nhóm ánh sáng", "symbol": "<i>v<sub>g</sub></i>", "unit": "cm·s<sup>−1</sup>", "meaning": "Vận tốc lan truyền bó năng lượng quang <i>v<sub>g</sub> = c · n<sub>g</sub><sup>−1</sup></i>"},
        {"name": "Tổng tổn hao quang học toàn phần", "symbol": "<i>α</i><sub>tot</sub>", "unit": "cm<sup>−1</sup>", "meaning": "Tổng tổn hao nội và tổn hao gương <i>α</i><sub>tot</sub> = ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_4_3, nom_data_2_4_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất điều kiện biên độ round-trip", "H3")
    add_p("Dẫn xuất tường minh điều kiện biên độ sau một vòng truyền sóng round-trip:")

    eq_deriv_2_4_3a = r"P(2L) = P(0) \cdot R_1 R_2 \exp\left[2 \left(\Gamma g - \langle\alpha_i\rangle\right) L\right]"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Công suất sau một chu trình truyền sóng khép kín:", eq_deriv_2_4_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_4_3b = r"P(2L) = P(0) \implies R_1 R_2 \exp\left[2 \left(\Gamma g - \langle\alpha_i\rangle\right) L\right] = 1"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điều kiện cân bằng dừng biên độ sóng quang:", eq_deriv_2_4_3b, styles=styles))
    add_spacer(6)

    eq_deriv_2_4_3c = r"2 \left(\Gamma g - \langle\alpha_i\rangle\right) L = \ln\left(\frac{1}{R_1 R_2}\right) \implies \Gamma g = \langle\alpha_i\rangle + \frac{1}{2 L} \ln\left(\frac{1}{R_1 R_2}\right) = \langle\alpha_i\rangle + \alpha_m"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Rút ra độ lợi ngưỡng cân bằng chính xác với tổng tổn hao:", eq_deriv_2_4_3c, styles=styles))
    add_spacer(8)

    add_p(
        "Hệ thức kinh điển trên là trái tim của vật lý diode laser: "
        "tại trạng thái dao động dừng, độ lợi mode quang học <i>Γ g</i> bắt buộc phải cân bằng chính xác 100% "
        "với tổng tổn hao nội ⟨<i>α<sub>i</sub></i>⟩ và tổn hao gương <i>α<sub>m</sub></i>. "
        "Thời gian sống photon <i>τ<sub>p</sub></i> trong các laser bán dẫn thông thường nằm trong khoảng 1–3 ps. "
        "Khoảng thời gian này ngắn hơn thời gian sống hạt tải (1–3 ns) tới 1000 lần, "
        "chứng minh rằng trường quang đáp ứng tức thời cực kỳ nhanh so với sự biến thiên của mật độ hạt tải."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.4a (Tổn hao gương theo chiều dài hốc)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_4a,
        "Hình mô phỏng 2.4.1: Hệ số tổn hao gương <i>α<sub>m</sub></i> theo chiều dài hốc cộng hưởng <i>L</i> tại các cấu hình phản xạ khác nhau. "
        "Đồ thị chứng minh rõ rệt: khi hốc càng ngắn, tổn hao gương tăng vọt theo hàm <i>L<sup>−1</sup></i>, đòi hỏi phải phủ lớp phản xạ cao HR "
        "để kìm hãm tổn hao và hạ thấp dòng ngưỡng phát xạ.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Embed Hình mô phỏng 2.4b (Thời gian sống photon trong hốc)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_4b,
        "Hình mô phỏng 2.4.2: Thời gian sống photon <i>τ<sub>p</sub></i> trong hốc cộng hưởng theo tổng tổn hao quang học <i>α</i><sub>tot</sub> và chiết suất nhóm <i>n<sub>g</sub></i>. "
        "Thang đo định vị chính xác thời gian sống photon trong khoảng 1 đến 5 ps, xác lập cơ sở động học cho đáp ứng chuyển mạch siêu nhanh của diode laser.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận gương phản xạ và bài toán tối ưu công suất ngõ ra", "H3")
    add_p(
        "Khảo sát các giới hạn cực trị của hệ số phản xạ gương: "
        "<br/>1. <b>Gương lý tưởng không thoát (<i>R</i><sub>1</sub> = <i>R</i><sub>2</sub> = 1):</b> Tổn hao gương <i>α<sub>m</sub></i> = 0. "
        "Dòng ngưỡng phát laser đạt mức tối thiểu tuyệt đối, nhưng công suất quang hữu ích thoát ra ngoài bằng 0! Linh kiện trở nên vô dụng đối với việc truyền phát tín hiệu. "
        "<br/>2. <b>Cấu hình bất đối xứng AR–HR tối ưu (<i>R</i><sub>1</sub> ≈ 0,05, <i>R</i><sub>2</sub> ≈ 0,95):</b> "
        "Gương sau được phủ lớp phản xạ cao HR (95%) để ngăn ánh sáng thoát về phía sau, "
        "trong khi gương trước phủ lớp chống phản xạ AR (5%) để ép 90% công suất quang hữu ích bắn thẳng ra cửa sổ phía trước. "
        "Đây là cấu hình chuẩn mực của mọi diode laser công nghiệp và truyền thông sợi quang hiện đại."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN CER & ĐIỂM MÙ THIẾT KẾ
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")

    cer_card = [
        [Paragraph(he.wrap_math_glyphs("<b>BÀI TOÁN THỬ THÁCH CHẨN ĐOÁN CER 2.4: BẪY PHẢN XẠ GƯƠNG VCSEL VÀ THẢM HỌA DÒNG NGƯỠNG</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Bối cảnh bài toán R&amp;D:</b> Một nhóm nghiên cứu thiết kế linh kiện laser VCSEL bước sóng 850 nm có chiều dài hốc siêu ngắn <i>L</i> = 1 μm. "
            "Nhóm quyết định sử dụng mặt chẻ tự nhiên của tinh thể bán dẫn GaAs làm gương phản xạ ở hai đầu với hệ số phản xạ <i>R</i><sub>1</sub> = <i>R</i><sub>2</sub> = 0,32 "
            "(tương tự như laser in-plane truyền thống) để tiết kiệm chi phí lắng đọng màng mỏng DBR. "
            "Sau khi chế tạo, nhóm nhận thấy linh kiện không thể nào phát laser được dù tiêm dòng điện lên tới mức làm cháy tiếp giáp.<br/><br/>"
            "• <b>Luận điểm (Claim):</b> Thiết kế gương phản xạ tự nhiên <i>R</i> = 0,32 cho VCSEL có khả thi về mặt vật lý không? Tại sao VCSEL bắt buộc phải sử dụng gương phản xạ DBR với <i>R</i> > 99,5%?<br/>"
            "• <b>Bằng chứng (Evidence):</b> Tính toán giá trị tổn hao gương <i>α<sub>m</sub></i> của VCSEL khi <i>L</i> = 1 μm và <i>R</i><sub>1</sub> = <i>R</i><sub>2</sub> = 0,32. "
            "Đối chiếu con số này với độ lợi mode khả dĩ cực đại <i>Γ g</i><sub>max</sub> của một giếng lượng tử GaAs.<br/>"
            "• <b>Lập luận (Reasoning):</b> Xây dựng chuỗi nhân quả chứng minh rằng khi hốc co ngắn lại 300 lần, tổn hao gương sẽ bùng nổ vượt quá giới hạn vật lý của độ lợi bán dẫn nếu không nâng hệ số phản xạ lên sát 100%."
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

    # Khâu nối biên độ DOC (Transition Anchor sang Mục 2.5)
    add_p(
        "<b>Khâu nối biên độ và Tiền đề chuyển tiếp sang Mục 2.5:</b> "
        "Mục 2.4 đã thiết lập trọn vẹn phương trình vi sai truyền sóng quang và định lượng các kênh tổn hao trong hốc. "
        "Tuy nhiên, khi dòng tiêm tăng dần từ 0, độ lợi <i>g(N)</i> tăng theo mật độ hạt tải cho đến khi chạm đúng điều kiện ngưỡng <i>Γ g = ⟨α<sub>i</sub>⟩ + α<sub>m</sub></i>. "
        "Điều gì sẽ xảy ra tiếp theo khi ta tiếp tục bơm dòng vượt qua ngưỡng này? "
        "Tại sao độ lợi quang học và mật độ hạt tải lại bị 'kẹp chặt' (clamped) không đổi trên ngưỡng? "
        "Toàn bộ bí ẩn vật lý về hiện tượng ghim độ lợi và cân bằng trạng thái dừng sẽ được mổ xẻ trong <b>Mục 2.5: Điều kiện ngưỡng hoặc trạng thái dừng của độ lợi trong laser</b>."
    )

    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename) / 1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_4()

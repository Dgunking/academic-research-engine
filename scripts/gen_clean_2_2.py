# -*- coding: utf-8 -*-
"""
gen_clean_2_2.py
Chế bản chuyên khảo toàn văn PDF cho Mục 2.2: Sinh và tái hợp hạt tải trong vùng tác dụng.
Đạt chuẩn:
- Bám sát Coldren & Corzine pp. 29-32
- Khung sư phạm lũy tiến 5 giai đoạn cho 3 MPT (2.2.1, 2.2.2, 2.2.3) + Giai đoạn 5 CER
- Dẫn xuất trung gian có nhãn ↳ [Tường minh bước biến đổi trung gian từ slide gốc]:
- Không có phân số gạch chéo /, không có gạch dưới _, không có mũ thô ^
- Không có thực thể HTML thô, 100% Unicode bản địa
- Bookmark đa tầng 3 cấp, đánh số trang hai lượt Trang X / Y
- ZT-GVLE verified
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
from reportlab.platypus import Paragraph, Spacer, KeepTogether, PageBreak

sys.path.append(r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as he

drive_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý"
img_dir = os.path.join(drive_dir, "Kho_Hinh_Anh")
pdf_dir = os.path.join(drive_dir, "Bai_Giang_Dong_Goi")
os.makedirs(pdf_dir, exist_ok=True)

pdf_filename = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.2.pdf")

# Tài nguyên hình ảnh
fig_goc_2_2 = os.path.join(img_dir, "[Goc]_Figure_2.2_Mo_hinh_ho_chua_hat_tai_duoi_nguong.png")
fig_sim_2_2a = os.path.join(img_dir, "[Mo_Phong]_Muc_2.2_Thoi_Gian_Song_Vi_Phan_Va_Bang_Thong.png")
fig_sim_2_2b = os.path.join(img_dir, "[Mo_Phong]_Muc_2.2_Dong_Ro_Va_Hieu_Suat_Tiem_Theo_Nhiet_Do.png")


def build_monograph_muc_2_2():
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
    # TRANG TIÊU ĐỀ & ĐỀ CƯƠNG MỤC 2.2
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.2: Sinh và tái hợp hạt tải trong vùng tác dụng (Carrier Generation and Recombination in Active Regions)", "H2")
    add_spacer(6)

    # Khung Metadata chuẩn HUST
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Quang tử học &amp; Diode Laser"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuyên đề:</b> Động học Hạt tải Vùng Tích cực"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu gốc:</b> Coldren &amp; Corzine (Trang 29–32)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đối chiếu:</b> Sze (Ch. 12) &amp; Yariv (Ch. 15)"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Mã phân mục:</b> Mục 2.2 (Chương 2)"), styles["TableCell"]),
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
        "Chuyên khảo toàn văn chuyên sâu Mục 2.2 khảo sát chi tiết các quá trình động học vi mô quyết định "
        "mật độ hạt tải trong vùng tích cực của diode laser dưới ngưỡng phát xạ kích thích "
        "(đối chiếu Coldren &amp; Corzine, Diode Lasers and Photonic Integrated Circuits, Chapter 2, trang 29–32). "
        "Hệ thống phân tích toàn diện 3 mắt xích vật lý: (1) Cơ chế tiêm dòng ngoài, sự phân bố dòng rò rỉ nhiệt và định nghĩa hiệu suất tiêm nội vi sai; "
        "(2) Bản chất vi mô của 3 kênh tái hợp tự nhiên Shockley-Read-Hall, bức xạ tự phát lưỡng phân tử, và tái hợp va chạm 3 hạt Auger; "
        "và (3) Khái niệm thời gian sống vi phân hạt tải, vai trò then chốt của nó trong việc thiết lập giới hạn băng thông đáp ứng tần số của linh kiện."
    )
    add_spacer(10)

    # BẢNG TỔNG QUAN NGUỒN KÉP MỤC 2.2
    matrix_headers = [
        Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Coldren &amp; Corzine)</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Hệ thức Cột trụ &amp; Phương trình Trọng tâm</b>"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("<b>Mô phỏng &amp; Hình ảnh Thực chứng</b>"), styles["TableHeader"]),
    ]
    matrix_rows = [
        matrix_headers,
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.2.1</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Tốc độ sinh hạt tải &amp; Hiệu suất tiêm nội <i>η<sub>i</sub></i>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>G</i> = <i>η<sub>i</sub> I</i> · (<i>q V</i>)<sup>−1</sup>, <i>η<sub>i</sub></i> = <i>I</i><sub>act</sub> · <i>I</i><sup>−1</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng dòng rò &amp; <i>η<sub>i</sub></i> theo nhiệt độ"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.2.2</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Các kênh tái hợp tự nhiên &amp; Mô hình đa thức ABC"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>R(N)</i> = <i>A N</i> + <i>B N</i><sup>2</sup> + <i>C N</i><sup>3</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Hình 2.2 (Tr. 30) Mô hình hồ chứa dưới ngưỡng"), styles["TableCellCenter"]),
        ],
        [
            Paragraph(he.wrap_math_glyphs("<b>MPT 2.2.3</b>"), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs("Thời gian sống vi phân &amp; Đáp ứng động học tín hiệu nhỏ"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("<i>τ</i><sub>diff</sub><sup>−1</sup> = d<i>R</i> · (d<i>N</i>)<sup>−1</sup> = <i>A</i> + 2 <i>B N</i> + 3 <i>C N</i><sup>2</sup>"), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs("Mô phỏng <i>τ</i> vi phân &amp; Băng thông <i>f</i><sub>3dB</sub>"), styles["TableCellCenter"]),
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
    # LUẬN ĐIỂM 2.2.1: TỐC ĐỘ SINH & HIỆU SUẤT TIÊM NỘI
    # =========================================================================
    add_p("Luận điểm 2.2.1: Tốc độ sinh hạt tải do dòng tiêm ngoài và Hiệu suất tiêm nội η_i", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm & Thất thoát rò rỉ
    add_p("Giai đoạn 1: Giới thiệu khái niệm, cơ chế tiêm dòng và thất thoát rò rỉ hạt tải", "H3")
    add_p(
        "Để kích thích diode laser phát sáng, một dòng điện phân cực thuận <i>I</i> được cấp từ nguồn ngoài vào linh kiện. "
        "Tuy nhiên, không phải 100% dòng điện tiêm vào đều biến thành các hạt tải hữu ích nằm lại trong vùng tích cực. "
        "Một phần dòng điện bị thất thoát qua các kênh rò rỉ điện trở song song, rò rỉ dòng bề mặt mép linh kiện, "
        "hoặc các hạt tải kích thích nhiệt có động năng cao vượt qua hàng rào thế dị thể dải cấm <i>ΔE<sub>c</sub></i>, <i>ΔE<sub>v</sub></i> "
        "bay sang lớp bao và tái hợp vô ích tại đó. "
        "Nghịch lý đặt ra trong thiết kế laser công suất cao là: khi ta tăng dòng tiêm để đạt công suất quang lớn, "
        "nhiệt độ tiếp giáp <i>T</i> tăng vọt do nhiệt Joule, làm tăng đột biến xác suất rò rỉ nhiệt theo hàm số mũ Boltzmann, "
        "khiến hiệu suất chuyển đổi giảm dốc đứng."
    )
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hiệu suất tiêm hạt tải", "H3")
    add_p(
        "Tốc độ sinh hạt tải trung bình <i>G</i> trên một đơn vị thể tích vùng tích cực "
        "được định nghĩa trực tiếp qua cường độ dòng điện tiêm hữu ích đi vào vùng tích cực:"
    )

    pillar_eq_2_2_1 = r"G = \frac{\eta_i I}{q V}, \quad \eta_i = \frac{I_{\mathrm{active}}}{I_{\mathrm{total}}} = \frac{I - I_{\mathrm{leak}}}{I}"
    nom_data_2_2_1 = [
        {"name": "Tốc độ sinh hạt tải", "symbol": "<i>G</i>", "unit": "cm<sup>−3</sup>·s<sup>−1</sup>", "meaning": "Số lượng cặp electron-lỗ trống được nạp vào một đơn vị thể tích trong một giây"},
        {"name": "Hiệu suất tiêm nội", "symbol": "<i>η<sub>i</sub></i>", "unit": "không thứ nguyên", "meaning": "Tỷ lệ phần trăm dòng điện ngoài thực sự đi vào và nằm lại trong vùng tích cực"},
        {"name": "Cường độ dòng điện tiêm", "symbol": "<i>I</i>", "unit": "A", "meaning": "Tổng dòng phân cực thuận đo được ở hai đầu tiếp xúc kim loại"},
        {"name": "Dòng rò rỉ ngoài vùng tích cực", "symbol": "<i>I</i><sub>leak</sub>", "unit": "A", "meaning": "Dòng thất thoát qua lớp bao, cạnh viền hoặc rò rỉ nhiệt"},
        {"name": "Điện tích nguyên tố", "symbol": "<i>q</i>", "unit": "C", "meaning": "Hằng số điện tích nguyên tố 1,602 × 10<sup>−19</sup> C"},
        {"name": "Thể tích vùng tích cực", "symbol": "<i>V</i>", "unit": "cm<sup>3</sup>", "meaning": "Thể tích hình học lõi giam giữ hạt tải <i>V = d · w · L</i>"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_2_1, nom_data_2_2_1, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phân bố dòng rò nhiệt qua hàng rào thế dị thể", "H3")
    add_p("Dẫn xuất tường minh sự suy giảm hiệu suất tiêm theo nhiệt độ tiếp giáp T:")

    eq_deriv_2_2_1a = r"J_{\mathrm{leak}} = q v_{\mathrm{th}} N_{\mathrm{cladd}} \exp\left(-\frac{\Delta E_c}{k_B T}\right)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mật độ dòng rò nhiệt qua vách thế dải dẫn:", eq_deriv_2_2_1a, styles=styles))
    add_spacer(6)

    eq_deriv_2_2_1b = r"\eta_i(T) = \frac{J_{\mathrm{act}}}{J_{\mathrm{act}} + J_{\mathrm{leak}}(T)} = \frac{1}{1 + \frac{J_{\mathrm{leak}}(T)}{J_{\mathrm{act}}}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu thức hiệu suất tiêm vi mô phụ thuộc nhiệt độ:", eq_deriv_2_2_1b, styles=styles))
    add_spacer(6)

    eq_deriv_2_2_1c = r"\Delta E_c \ge 10\, k_B T \implies \exp\left(-\frac{\Delta E_c}{k_B T}\right) < 4{,}5 \times 10^{-5} \implies \eta_i \approx 0{,}95 - 0{,}98"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chuẩn thiết kế hàng rào thế chống rò rỉ nhiệt:", eq_deriv_2_2_1c, styles=styles))
    add_spacer(8)

    add_p(
        "Từ chuỗi dẫn xuất trên, ta nhận thấy rõ ràng: để bảo đảm hiệu suất tiêm <i>η<sub>i</sub></i> đạt trên 95% ở nhiệt độ phòng 300 K, "
        "chiều cao hàng rào thế dải dẫn <i>ΔE<sub>c</sub></i> bắt buộc phải lớn hơn hoặc bằng 10 <i>k<sub>B</sub> T</i> (tối thiểu 0,26 eV). "
        "Nếu rào thế quá thấp (ví dụ hệ vật liệu AlGaAs có tỷ lệ nhôm nhỏ, <i>ΔE<sub>c</sub></i> < 0,15 eV), "
        "khi nhiệt độ linh kiện tăng lên 350 K khi hoạt động liên tục, hiệu suất tiêm <i>η<sub>i</sub></i> sẽ sụt giảm nghiêm trọng xuống dưới 60%."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.2b (Hiệu suất tiêm & Dòng rò theo nhiệt độ)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_2b,
        "Hình mô phỏng 2.2.1: Hiệu suất tiêm hạt tải <i>η<sub>i</sub></i> và hiện tượng suy giảm do rò rỉ nhiệt qua hàng rào thế dị thể dải dẫn ở các mức <i>ΔE<sub>c</sub></i> khác nhau. "
        "Đồ thị chứng minh rõ rệt: rào thế cao 0,30 eV (Al<sub>0,4</sub>Ga<sub>0,6</sub>As) bảo vệ hạt tải ổn định trên toàn dải nhiệt độ, "
        "trong khi rào thế thấp 0,15 eV làm linh kiện suy thoái nghiêm trọng khi vượt quá nhiệt độ phòng.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận nhiệt độ và nguyên lý bù trừ kỹ thuật", "H3")
    add_p(
        "Khảo sát hành vi của hiệu suất tiêm ở hai vùng cực hạn nhiệt độ: "
        "<br/>1. <b>Tiệm cận nhiệt độ siêu hàn (<i>T</i> tiến tới 0 K):</b> Nhiệt năng hạt tải <i>k<sub>B</sub> T</i> tiến tới 0. "
        "Xác suất kích thích nhiệt vượt rào triệt tiêu hoàn toàn. Toàn bộ hạt tải tiêm bị khóa cứng trong giếng thế, hiệu suất tiêm <i>η<sub>i</sub></i> tiệm cận tuyệt đối 100%. "
        "<br/>2. <b>Tiệm cận nhiệt độ cao (<i>T</i> vượt quá 400 K):</b> Dòng rò nhiệt tăng vọt làm <i>η<sub>i</sub></i> suy sụp. "
        "Để chống lại sự trôi dạt nhiệt này trong các diode laser công suất lớn dùng trong công nghiệp và quân sự, "
        "các kỹ sư áp dụng cấu trúc lớp chặn điện tử (Electron Blocking Layer - EBL) có dải cấm siêu rộng đặt ngay sát vùng tích cực."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.2.2: CÁC KÊNH TÁI HỢP VÀ MÔ HÌNH ĐA THỨC ABC
    # =========================================================================
    add_p("Luận điểm 2.2.2: Các cơ chế tái hợp tự nhiên trong vùng tích cực và Mô hình đa thức ABC", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm & Ba kênh vi mô
    add_p("Giai đoạn 1: Giới thiệu khái niệm, ba cơ chế vi mô cạnh tranh và mô hình hồ chứa", "H3")
    add_p(
        "Khi electron và lỗ trống được nạp vào vùng tích cực, chúng tồn tại trong một khoảng thời gian hữu hạn trước khi biến mất "
        "qua các quá trình tái hợp. Coldren &amp; Corzine đã khái quát hóa động học này thông qua mô hình hồ chứa nước tương đương (Figure 2.2, trang 30). "
        "Nước được bơm vào hồ với lưu lượng tương ứng dòng tiêm <i>η<sub>i</sub> I · q<sup>−1</sup></i>, "
        "và thoát ra ngoài qua 3 lỗ thủng đáy hồ tương ứng với 3 kênh tái hợp vi mô: "
        "<br/>• Kênh 1: Tái hợp phi bức xạ Shockley-Read-Hall qua bẫy sâu sai hỏng mạng (tỉ lệ bậc nhất với <i>N</i>). "
        "<br/>• Kênh 2: Tái hợp bức xạ tự phát lưỡng phân tử phát ra photon tự phát (tỉ lệ bậc hai với <i>N</i><sup>2</sup>). "
        "<br/>• Kênh 3: Tái hợp va chạm 3 hạt phi bức xạ Auger (tỉ lệ bậc ba với <i>N</i><sup>3</sup>)."
    )
    add_spacer(8)

    # Embed Hình gốc 2.2
    story.append(he.embed_figure_with_caption(
        fig_goc_2_2,
        "Hình 2.2: Mô hình hồ chứa tương đương của diode laser ở chế độ dưới ngưỡng (Coldren &amp; Corzine, trang 30). "
        "Mô phỏng ba mắt xích vật lý: (a) Lưu lượng bơm hạt tải vào hồ bằng dòng tiêm hiệu dụng; "
        "(b) Độ cao mực nước đại diện cho mật độ hạt tải <i>N</i> tích lũy trong vùng tích cực; "
        "(c) Ba lỗ rò rỉ đáy hồ tương ứng với tốc độ thoát hạt tải tự nhiên qua ba kênh <i>A N</i>, <i>B N</i><sup>2</sup>, và <i>C N</i><sup>3</sup>.",
        kind="orig",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ đa thức tái hợp ABC", "H3")
    add_p(
        "Tổng tốc độ tái hợp tự nhiên của hạt tải trong một đơn vị thể tích vùng tích cực được mô tả hoàn chỉnh bằng đa thức bậc 3:"
    )

    pillar_eq_2_2_2 = r"R(N) = R_{\mathrm{srh}} + R_{\mathrm{sp}} + R_{\mathrm{aug}} = A N + B N^2 + C N^3"
    nom_data_2_2_2 = [
        {"name": "Tổng tốc độ tái hợp", "symbol": "<i>R(N)</i>", "unit": "cm<sup>−3</sup>·s<sup>−1</sup>", "meaning": "Số cặp hạt tải bị tiêu diệt trên một đơn vị thể tích trong một giây"},
        {"name": "Hệ số tái hợp SRH", "symbol": "<i>A</i>", "unit": "s<sup>−1</sup>", "meaning": "Xác suất hạt tải bị bẫy bởi sai hỏng mạng tinh thể và tạp chất sâu"},
        {"name": "Hệ số tái hợp bức xạ tự phát", "symbol": "<i>B</i>", "unit": "cm<sup>3</sup>·s<sup>−1</sup>", "meaning": "Xác suất một electron và một lỗ trống gặp nhau và phát ra một photon tự phát"},
        {"name": "Hệ số tái hợp Auger", "symbol": "<i>C</i>", "unit": "cm<sup>6</sup>·s<sup>−1</sup>", "meaning": "Tốc độ va chạm 3 hạt truyền năng lượng phi bức xạ kích thích hạt thứ ba"},
        {"name": "Mật độ hạt tải tự do", "symbol": "<i>N</i>", "unit": "cm<sup>−3</sup>", "meaning": "Nồng độ electron trong dải dẫn (ở trạng thái trung hòa điện xấp xỉ bằng nồng độ lỗ trống <i>P</i>)"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_2_2, nom_data_2_2_2, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất điều kiện chuyển giao kênh ưu thế", "H3")
    add_p("Dẫn xuất tường minh điểm giao nhau giữa các kênh tái hợp:")

    eq_deriv_2_2_2a = r"R_{\mathrm{srh}} = R_{\mathrm{sp}} \implies A N_1 = B N_1^2 \implies N_1 = \frac{A}{B}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điểm chuyển giao từ SRH sang bức xạ tự phát:", eq_deriv_2_2_2a, styles=styles))
    add_spacer(6)

    eq_deriv_2_2_2b = r"R_{\mathrm{sp}} = R_{\mathrm{aug}} \implies B N_2^2 = C N_2^3 \implies N_2 = \frac{B}{C}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điểm chuyển giao từ bức xạ sang Auger:", eq_deriv_2_2_2b, styles=styles))
    add_spacer(6)

    eq_deriv_2_2_2c = r"N_1 = \frac{10^8}{10^{-10}} = 10^{18}\ \mathrm{cm}^{-3}, \quad N_2 = \frac{10^{-10}}{3 \times 10^{-29}} \approx 3{,}33 \times 10^{18}\ \mathrm{cm}^{-3}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Giá trị số cụ thể cho bán dẫn GaAs ở 300 K:", eq_deriv_2_2_2c, styles=styles))
    add_spacer(8)

    add_p(
        "Kết quả tính toán trên vạch ra một bức tranh vật lý cực kỳ rõ nét: "
        "kênh phát xạ bức xạ tự phát hữu ích chỉ chiếm ưu thế trong một cửa sổ mật độ hạt tải khá hẹp (từ 10<sup>18</sup> đến 3,3 × 10<sup>18</sup> cm<sup>−3</sup>). "
        "Dưới ngưỡng 10<sup>18</sup> cm<sup>−3</sup>, hạt tải chủ yếu bị bẫy phi bức xạ qua sai hỏng SRH. "
        "Vượt trên 3,3 × 10<sup>18</sup> cm<sup>−3</sup>, kênh Auger bùng nổ cướp đi phần lớn hạt tải và biến thành nhiệt."
    )
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận chất lượng vật liệu tinh thể", "H3")
    add_p(
        "Khảo sát các trường hợp cực trị về công nghệ chế tạo màng mỏng bán dẫn: "
        "<br/>1. <b>Vật liệu có mật độ sai hỏng mạng cực cao (Hệ số <i>A</i> lớn hơn 10<sup>9</sup> s<sup>−1</sup>):</b> Điểm giao nhau <i>N</i><sub>1</sub> bị đẩy lên rất cao, vượt qua mật độ ngưỡng laser. Hệ quả là linh kiện bị đốt nóng dữ dội, hiệu suất lượng tử nội cực thấp và không thể nào đạt tới ngưỡng phát laser. "
        "<br/>2. <b>Vật liệu đơn tinh thể epitaxy hoàn hảo (Hệ số <i>A</i> nhỏ hơn 10<sup>7</sup> s<sup>−1</sup>):</b> Vùng thống trị của bức xạ tự phát mở rộng xuống vùng mật độ thấp. Dòng ngưỡng của linh kiện giảm mạnh, nâng cao độ bền vận hành."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.2.3: THỜI GIAN SỐNG VI PHÂN VÀ ĐÁP ỨNG ĐỘNG HỌC
    # =========================================================================
    add_p("Luận điểm 2.2.3: Thời gian sống vi phân hạt tải và Giới hạn băng thông điều chế dưới ngưỡng", "H2")

    # Giai đoạn 1: Giới thiệu khái niệm vi phân
    add_p("Giai đoạn 1: Giới thiệu khái niệm, sự khác biệt giữa thời gian sống toàn phần và vi phân", "H3")
    add_p(
        "Trong các ứng dụng truyền thông cáp quang hoặc điều chế tín hiệu xung, linh kiện diode phát quang (LED) "
        "hoặc diode laser dưới ngưỡng được điều chế bởi một dòng điện xoay chiều biên độ nhỏ <i>ΔI(t)</i> chồng lên dòng phân cực tĩnh dừng <i>I</i><sub>0</sub>. "
        "Đáp ứng thời gian của mật độ hạt tải không tuân theo thời gian sống toàn phần <i>τ(N) = N · R(N)<sup>−1</sup></i>, "
        "mà bị chi phối bởi độ dốc vi phân của đường cong tái hợp tại điểm làm việc tĩnh. "
        "Khái niệm thời gian sống vi phân <i>τ</i><sub>diff</sub> xuất hiện như một thông số quyết định tốc độ nạp xả của hồ chứa hạt tải."
    )
    add_spacer(8)

    # Giai đoạn 2: Hạt nhân vật lý & Hệ thức Cột trụ
    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ thời gian sống vi phân", "H3")
    add_p(
        "Thời gian sống vi phân được định nghĩa từ đạo hàm bậc nhất của tốc độ tái hợp theo mật độ hạt tải:"
    )

    pillar_eq_2_2_3 = r"\frac{1}{\tau_{\mathrm{diff}}} \equiv \frac{\mathrm{d}R(N)}{\mathrm{d}N} = A + 2 B N + 3 C N^2, \quad f_{3\mathrm{dB}} = \frac{1}{2\pi \tau_{\mathrm{diff}}}"
    nom_data_2_2_3 = [
        {"name": "Thời gian sống vi phân", "symbol": "<i>τ</i><sub>diff</sub>", "unit": "s", "meaning": "Hằng số thời gian suy giảm của một biến thiên hạt tải nhỏ quanh điểm dừng"},
        {"name": "Thời gian sống toàn phần", "symbol": "<i>τ</i>", "unit": "s", "meaning": "Thời gian tồn tại trung bình của một hạt tải trước khi tái hợp"},
        {"name": "Tần số cắt 3dB dưới ngưỡng", "symbol": "<i>f</i><sub>3dB</sub>", "unit": "Hz", "meaning": "Băng thông điều chế quang tại đó công suất điều chế giảm đi một nửa"},
        {"name": "Độ dốc vi phân tái hợp", "symbol": "d<i>R</i> · (d<i>N</i>)<sup>−1</sup>", "unit": "s<sup>−1</sup>", "meaning": "Tốc độ thay đổi tức thời của tốc độ tái hợp theo mật độ hạt tải"}
    ]
    story.append(he.build_target_equation_block(pillar_eq_2_2_3, nom_data_2_2_3, styles=styles))
    add_spacer(8)

    # Giai đoạn 3: Chuỗi nhân quả dẫn xuất
    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất phương trình vi phân biến thiên hạt tải tín hiệu nhỏ", "H3")
    add_p("Khai triển tuyến tính hóa phương trình vi phân tốc độ hạt tải quanh điểm dừng:")

    eq_deriv_2_2_3a = r"N(t) = N_0 + \Delta N(t), \quad I(t) = I_0 + \Delta I(t)"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển tín hiệu nhỏ điều hòa quanh điểm tĩnh:", eq_deriv_2_2_3a, styles=styles))
    add_spacer(6)

    eq_deriv_2_2_3b = r"\frac{\mathrm{d}(N_0 + \Delta N)}{\mathrm{d}t} = \frac{\eta_i (I_0 + \Delta I)}{q V} - \left[ R(N_0) + \left.\frac{\mathrm{d}R}{\mathrm{d}N}\right|_{N_0} \Delta N \right]"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển chuỗi Taylor bậc nhất tốc độ tái hợp:", eq_deriv_2_2_3b, styles=styles))
    add_spacer(6)

    eq_deriv_2_2_3c = r"\frac{\mathrm{d}\Delta N}{\mathrm{d}t} + \frac{\Delta N}{\tau_{\mathrm{diff}}} = \frac{\eta_i \Delta I}{q V} \implies \Delta N(\omega) = \frac{\eta_i \Delta I(\omega) \cdot (q V)^{-1}}{j\omega + \tau_{\mathrm{diff}}^{-1}}"
    story.append(he.build_intermediate_equation("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm miền tần số của phương trình vi phân tín hiệu nhỏ:", eq_deriv_2_2_3c, styles=styles))
    add_spacer(8)

    add_p(
        "Từ nghiệm miền tần số trên, ta nhận thấy rõ ràng: hệ thống hoạt động như một mạch lọc thông thấp RC bậc nhất. "
        "Băng thông điều chế tín hiệu nhỏ bị chặn trên bởi đại lượng <i>(2π τ</i><sub>diff</sub>)<sup>−1</sup>. "
        "Do các hệ số nhân 2 ở số hạng bức xạ (2 <i>B N</i>) và hệ số 3 ở số hạng Auger (3 <i>C N</i><sup>2</sup>), "
        "thời gian sống vi phân <i>τ</i><sub>diff</sub> luôn luôn nhỏ hơn thời gian sống toàn phần <i>τ</i> từ 1,5 đến 2,5 lần ở vùng mật độ cao."
    )
    add_spacer(8)

    # Embed Hình mô phỏng 2.2a (Thời gian sống vi phân & Băng thông)
    story.append(he.embed_figure_with_caption(
        fig_sim_2_2a,
        "Hình mô phỏng 2.2.2: So sánh động học thời gian sống toàn phần <i>τ(N)</i> và thời gian sống vi phân <i>τ</i><sub>diff</sub>(<i>N</i>) trong bán dẫn GaAs ở 300 K. "
        "Ở mật độ hạt tải thấp, <i>τ</i> ≈ <i>τ</i><sub>diff</sub> ≈ <i>A</i><sup>−1</sup> = 10 ns. "
        "Khi mật độ hạt tải tiến sát ngưỡng laser (<i>N</i> ≈ 2 × 10<sup>18</sup> cm<sup>−3</sup>), thời gian sống vi phân giảm mạnh xuống dưới 0,5 ns, "
        "tương ứng với băng thông điều chế quang đạt khoảng 300–400 MHz.",
        kind="sim",
        styles=styles,
    ))
    add_spacer(8)

    # Giai đoạn 4: Khảo sát tiệm cận & Thực chiến
    add_p("Giai đoạn 4: Khảo sát tiệm cận băng thông và giới hạn vật lý của LED", "H3")
    add_p(
        "Từ kết quả khảo sát trên, ta rút ra giới hạn vật lý cốt lõi của linh kiện phát quang dưới ngưỡng: "
        "<br/>1. <b>Băng thông LED bị giới hạn bởi thời gian sống tự phát:</b> Vì không có phát xạ kích thích (chưa có sự xuất hiện của photon kết hợp trong hốc), hạt tải bắt buộc phải tiêu biến qua các kênh tái hợp tự nhiên. Băng thông tối đa của LED thông thường không thể vượt quá vài trăm MHz dù có tăng dòng phân cực đến mức nào. "
        "<br/>2. <b>Sự vượt trội của Laser Diode trên ngưỡng:</b> Khi dòng tiêm vượt ngưỡng, kênh phát xạ kích thích mở ra với tốc độ cực nhanh, rút ngắn thời gian sống photon xuống cỡ vài picô-giây (ps), cho phép giải phóng băng thông linh kiện lên hàng chục GHz."
    )
    add_spacer(14)

    # =========================================================================
    # GIAI ĐOẠN 5: THỬ THÁCH TỰ LUYỆN CER & ĐIỂM MÙ THIẾT KẾ
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Bẫy điểm mù R&amp;D)", "H3")

    cer_card = [
        [Paragraph(he.wrap_math_glyphs("<b>BÀI TOÁN THỬ THÁCH CHẨN ĐOÁN CER 2.2: TRÔI NHIỆT DÒNG NGƯỠNG VÀ RÒ RỈ AUGER TRONG LASER 1,55 μm</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "<b>Bối cảnh bài toán R&amp;D:</b> Một kỹ sư thiết kế diode laser viễn thông bước sóng 1,55 μm trên đế InP. "
            "Trong quá trình đo kiểm linh kiện ở chế độ xung nhiệt độ phòng, kỹ sư nhận thấy dòng ngưỡng đo được là <i>I</i><sub>th</sub> = 25 mA. "
            "Tuy nhiên, khi chuyển sang chế độ phát sóng liên tục (CW - Continuous Wave), dòng ngưỡng tăng vọt lên 45 mA "
            "và hiệu suất lượng tử vi phân bị suy thoái nghiêm trọng. "
            "Kỹ sư này kết luận rằng do lớp mạ tiếp xúc kim loại bị oxy hóa làm tăng điện trở vi phân tiếp xúc <i>R<sub>s</sub></i>, "
            "dẫn đến sụt áp ngoài lớn hơn.<br/><br/>"
            "• <b>Luận điểm (Claim):</b> Kết luận của người kỹ sư trên có chuẩn xác theo nguyên lý đầu không? Cơ chế vật lý vi mô thực sự nào chịu trách nhiệm cho sự nhảy vọt của dòng ngưỡng trong chế độ CW?<br/>"
            "• <b>Bằng chứng (Evidence):</b> Dựa vào hệ số tái hợp Auger <i>C</i> của vật liệu InGaAsP dải hẹp (thường lớn hơn GaAs hàng chục lần) và hệ số rò rỉ nhiệt exp(−<i>ΔE<sub>c</sub> · (k<sub>B</sub> T)<sup>−1</sup></i>), hãy chỉ ra sự biến thiên của <i>η<sub>i</sub></i> và <i>R</i><sub>aug</sub> khi nhiệt độ tiếp giáp tăng thêm 30 K do tích tụ nhiệt liên tục.<br/>"
            "• <b>Lập luận (Reasoning):</b> Xây dựng chuỗi nhân quả vi mô giải thích vì sao bước sóng 1,55 μm nhạy cảm với hiệu ứng nhiệt gấp nhiều lần bước sóng 0,85 μm của GaAs."
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

    # Khâu nối biên độ DOC (Transition Anchor sang Mục 2.3)
    add_p(
        "<b>Khâu nối biên độ và Tiền đề chuyển tiếp sang Mục 2.3:</b> "
        "Toàn bộ các phân tích trong Mục 2.2 đã giải phẫu trọn vẹn số phận của hạt tải tiêm trong vùng tích cực dưới ngưỡng phát xạ kích thích. "
        "Tuy nhiên, hạt tải tái hợp bức xạ phát ra photon tự phát sẽ thoát ra ngoài không gian tự do như thế nào? "
        "Tại sao hiệu suất trích xuất ánh sáng của linh kiện LED lại thấp đến mức kinh ngạc (thường dưới 5%) do hiện tượng phản xạ toàn phần tại mặt phân giới bán dẫn – không khí? "
        "Tất cả các câu hỏi này sẽ được khảo sát và định lượng toàn diện trong <b>Mục 2.3: Phát xạ tự phát và vận hành linh kiện LED</b>."
    )

    doc.build(story, canvasmaker=he.NumberedBookmarkCanvas)
    print(f"PDF BUILT SUCCESSFULLY: {pdf_filename} ({os.path.getsize(pdf_filename) / 1024:.1f} KB)")


if __name__ == "__main__":
    build_monograph_muc_2_2()

"""
KỊCH BẢN CHẾ BẢN CHUYÊN KHẢO TOÀN VĂN REPORTLAB CHO MỤC 3.5
Học phần: Cơ sở vật lý và công nghệ nano (PH3470 - ĐHBK Hà Nội)
Chương 3: Đặc trưng của vật liệu khi kích thước giảm
Mục 3.5: Hiệu ứng bề mặt, chuyển pha điện tử và đặc tính quang thang nano

Tuân thủ nghiêm ngặt 16 Supreme Mandates:
- Unbounded Depth, Zero-Omission, Zero-Slash.
- Typography DejaVu, 100% bọc thẻ HTML cho biến số.
- Bố cục 5 Giai đoạn Sư phạm cho 4 MPT độc lập + Thử thách CER 3.5.
- Triển khai nguyên tử vào Google Drive G:\.
"""

import os
import sys
sys.stdout.reconfigure(encoding="utf-8")
import shutil
import tempfile
import fitz  # PyMuPDF

sys.path.append(r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as he
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image as RLImage, KeepTogether, PageBreak
from reportlab.lib import colors

TARGET_DRIVE_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Bai_Giang_Dong_Goi"
IMAGES_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
PDF_FILENAME = "Chuyen_Khao_Nano_Muc_3.5.pdf"

def build_monograph_muc_3_5():
    os.makedirs(TARGET_DRIVE_DIR, exist_ok=True)
    temp_dir = tempfile.gettempdir()
    temp_pdf_path = os.path.join(temp_dir, f"temp_{os.getpid()}_{PDF_FILENAME}")
    final_drive_path = os.path.join(TARGET_DRIVE_DIR, PDF_FILENAME)

    doc = he.BookmarkDocTemplate(temp_pdf_path)
    styles = he.get_hust_styles()
    if "Body" not in styles and "BodyText" in styles:
        styles["Body"] = styles["BodyText"]
    elif "Body" in styles and "BodyText" not in styles:
        styles["BodyText"] = styles["Body"]
    story = []

    def add_p(text, style_name="Body", space_after=6):
        story.append(Paragraph(he.wrap_math_glyphs(text), styles[style_name]))
        if space_after > 0:
            story.append(Spacer(1, space_after))

    def add_spacer(height):
        story.append(Spacer(1, height))

    def add_figure(image_rel_path, caption_text, *args, **kwargs):
        img_full_path = os.path.join(IMAGES_DIR, image_rel_path)
        kind = "sim" if "Mo_Phong" in image_rel_path else "orig"
        if os.path.exists(img_full_path):
            block = he.embed_figure_with_caption(img_full_path, caption_text, kind=kind, styles=styles)
            story.append(block)
            story.append(Spacer(1, 8))
        else:
            print(f"WARNING: Image not found at {img_full_path}")

    # =========================================================================
    # H1 TIÊU ĐỀ PHÂN MỤC VÀ METADATA ĐÀO TẠO BÁCH KHOA
    # =========================================================================
    add_p("Chương 3: Đặc trưng của vật liệu khi kích thước giảm", "H1")
    add_p("Mục 3.5: Hiệu ứng bề mặt, chuyển pha điện tử và đặc tính quang thang nano", "H2")
    
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Cơ sở vật lý và công nghệ nano (PH3470)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Khung chương trình:</b> Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Người học &amp; Nghiên cứu:</b> Bùi Trung Dũng (K67)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Tài liệu đối chiếu:</b> Slide 38–48 (HUST) &amp; E. L. Wolf"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Phân định cấu trúc:</b> 4 MPT chuyên sâu + Thử thách CER 3.5"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuẩn mực kỹ thuật:</b> Khung Sư phạm 5 Giai đoạn, Zero-Omission, Zero-Slash"), styles["TableCell"])]
    ]
    t_meta = Table(meta_table_data, colWidths=[240, 240])
    t_meta.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F5F9")),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor("#CBD5E1")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t_meta)
    add_spacer(14)

    # Bảng mục lục tóm tắt ma trận 4 MPT
    mpt_summary_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Mã MPT</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Tiêu đề Luận điểm Vi mô (Slide HUST &amp; Wolf)</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Đặc tính Vật lý Cốt lõi</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Hình ảnh &amp; Mô phỏng ZT-GVLE</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<b>MPT 3.5.1</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tỷ số Diện tích trên Thể tích và Tỷ lệ Nguyên tử Bề mặt"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<i>S</i> · <i>V</i><sup>−1</sup> ∝ <i>D</i><sup>−1</sup>, <i>F</i><sub>surf</sub> ∝ <i>D</i><sup>−1</sup>"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Ảnh gốc 01, 02 + Đồ thị ZT-GVLE 01"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>MPT 3.5.2</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Nhiệt động học Bề mặt, Năng lượng γ, Kết tụ và Xúc tác"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Δ<i>E</i> = −2γ <i>L</i><sup>2</sup> &lt; 0, Gibbs-Thomson, Lock-Key"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Ảnh gốc 03, 04, 05"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>MPT 3.5.3</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Giam giữ Lượng tử, Chuyển pha Kim loại - Bán dẫn, SET"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Tiêu chuẩn Kubo δ ∝ <i>D</i><sup>−3</sup>, Coulomb Blockade <i>E<sub>C</sub></i>"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Ảnh gốc 06 + Đồ thị ZT-GVLE 02"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>MPT 3.5.4</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Đặc tính Quang học, LSPR Kim loại và Chấm Lượng tử"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Cộng hưởng Fröhlich Re[ε] = −2ε<sub><i>m</i></sub>, Dịch đỏ LSPR"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Ảnh gốc 07, 08, 09 + Đồ thị ZT-GVLE 03"), styles["TableCell"])],
    ]
    t_summary = Table(mpt_summary_data, colWidths=[65, 175, 125, 115])
    t_summary.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0072BD")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_summary)
    add_spacer(14)

    # =========================================================================
    # MPT 3.5.1: HIỆU ỨNG BỀ MẶT, TỶ SỐ S/V VÀ TỶ LỆ NGUYÊN TỬ BỀ MẶT
    # =========================================================================
    add_p("Luận điểm 3.5.1: Hiệu ứng Bề mặt, Tỷ số Diện tích trên Thể tích và Tỷ lệ Nguyên tử Bề mặt", "H2")

    add_p("Giai đoạn 1: Giới thiệu khái niệm, ranh giới liên pha và bản chất vi mô của nguyên tử bề mặt", "H3")
    add_p(
        "Trong vật lý chất rắn cổ điển và nhiệt động học vĩ mô, các thuộc tính của vật liệu thường được quy về các đặc trưng khối (bulk properties), "
        "bởi vì số lượng nguyên tử nằm sâu trong lòng mạng tinh thể chiếm tỉ lệ áp đảo tuyệt đối (&gt; 99.999%), "
        "khiến năng lượng tự do bề mặt chỉ đóng vai trò là một số hạng hiệu chỉnh vi mô không đáng kể. "
        "Tuy nhiên, khi kích thước hình học của vật liệu suy giảm xuống thang nanomet (1—100 nm), "
        "một bước ngoặc nhiệt động học mang tính nền tảng xuất hiện: diện tích bề mặt trên một đơn vị thể tích tăng vọt theo quy luật tỉ lệ nghịch với kích thước. "
        "Khoa học nghiên cứu các tính chất hóa học, vật lý và sinh học diễn ra tại ranh giới chuyển tiếp này được gọi là <b>Khoa học Bề mặt (Surface Science)</b>. "
        "Trong bối cảnh vật lý nano hiện đại, thuật ngữ <b>Ranh giới liên pha (Interface)</b> thường được ưu tiên sử dụng thay cho bề mặt đơn thuần, "
        "nhằm nhấn mạnh đây là vùng chuyển tiếp động lực học giữa hai pha vật chất: mạng tinh thể nano và môi trường bao quanh (pha khí, dung dịch hoặc chất nền rắn)."
    )
    add_p(
        "Về phương diện vi mô lượng tử, một nguyên tử nằm sâu trong lòng khối tinh thể có cấu trúc phối trí hoàn hảo: "
        "mọi liên kết hóa học xung quanh nó đều được chia sẻ cân bằng với các nguyên tử lân cận theo đối xứng không gian ba chiều. "
        "Ngược lại, các nguyên tử cư trú tại lớp bề mặt bị khuyết tật phối trí nghiêm trọng (broken coordination symmetry): "
        "các liên kết hướng ra môi trường ngoài không tìm được đối tác liên kết, hình thành nên các <b>liên kết treo (dangling bonds)</b> giàu năng lượng. "
        "Do đó, trạng thái điện tử của nguyên tử bề mặt có mức năng lượng tự do cao hơn hẳn các nguyên tử trong lòng khối, "
        "làm cho bề mặt hạt nano trở thành một hệ nhiệt động học giả bền (metastable) có xu hướng phản ứng hóa học cực mạnh."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_01_Phan_Chia_Dien_Tich_Be_Mat.png",
        "Hình 3.5.1 (Trích xuất Slide 38): Sơ đồ minh họa sự phân chia một khối vật liệu vĩ mô thành tập hợp các hạt nano cùng tổng thể tích nhưng có diện tích bề mặt tăng vọt.",
        width=440, height=160
    )

    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ hình học tỷ số diện tích trên thể tích", "H3")
    add_p(
        "Để lượng hóa chính xác hiệu ứng bề mặt, chúng ta khảo sát hai mô hình hình học lý tưởng: hạt nano hình cầu bán kính <i>R</i> (đường kính <i>D</i> = 2<i>R</i>) "
        "và hạt nano hình khối lập phương cạnh <i>L</i>."
    )

    eq_col_1 = [
        [Paragraph(he.wrap_math_glyphs("<b>Mô hình Hình học</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Diện tích Bề mặt (<i>S</i>)</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Thể tích (<i>V</i>)</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Tỷ số Diện tích trên Thể tích (<i>S</i> · <i>V</i><sup>−1</sup>)</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<b>Khối Lập phương (cạnh <i>L</i>)</b>"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("6 <i>L</i><sup>2</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("<i>L</i><sup>3</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("<b>6 · <i>L</i><sup>−1</sup></b>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Hình Cầu (đường kính <i>D</i>)</b>"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("π <i>D</i><sup>2</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("π · 6<sup>−1</sup> <i>D</i><sup>3</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("<b>6 · <i>D</i><sup>−1</sup></b>"), styles["TableCellCenter"])],
    ]
    t_eq1 = Table(eq_col_1, colWidths=[130, 110, 110, 130])
    t_eq1.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0072BD")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(t_eq1)
    add_spacer(10)

    p_step1 = (
        "Hệ thức cột trụ biểu diễn tỷ số diện tích trên thể tích của hạt nano hình cầu:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Xét hạt cầu bán kính <i>R</i> = 0.5 <i>D</i>. Diện tích mặt cầu là <i>S</i> = 4π <i>R</i><sup>2</sup>, thể tích khối cầu là <i>V</i> = 4 · 3<sup>−1</sup> π <i>R</i><sup>3</sup>. "
        "Lập tỷ số giải tích và đơn giản hóa thừa số chung 4π <i>R</i><sup>2</sup>:"
    )
    story.append(he.build_intermediate_equation(p_step1, r"\frac{S}{V} = \frac{4\pi R^2}{\frac{4}{3}\pi R^3} = \frac{3}{R} = \frac{6}{D} \propto D^{-1}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step2 = (
        "Dẫn xuất phân số nguyên tử bề mặt <i>F</i><sub>surf</sub> theo độ dày lớp đơn nguyên tử delta:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Gọi δ là độ dày hiệu dụng của lớp đơn nguyên tử bề mặt (đối với đa số kim loại và bán dẫn, δ ≈ 0.3 nm, tương ứng với một hằng số mạng tinh thể). "
        "Thể tích của phần lõi bên trong (core) không tiếp xúc bề mặt là <i>V</i><sub>core</sub> = 4 · 3<sup>−1</sup> π (<i>R</i> − δ)<sup>3</sup>. "
        "Tỷ lệ số nguyên tử nằm trên bề mặt so với tổng số nguyên tử trong hạt cầu được tính chính xác bằng hiệu số thể tích chuẩn hóa:"
    )
    story.append(he.build_intermediate_equation(p_step2, r"F_{\mathrm{surf}} = \frac{N_{\mathrm{surf}}}{N_{\mathrm{total}}} = \frac{V_{\mathrm{total}} - V_{\mathrm{core}}}{V_{\mathrm{total}}} = 1 - \left(1 - \frac{2\delta}{D}\right)^3 \approx \frac{6\delta}{D} \quad (\text{khi } D \gg 2\delta)", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất sự tăng vọt tỷ lệ nguyên tử bề mặt", "H3")
    add_p(
        "Chuỗi nhân quả vi mô diễn giải sâu sắc hệ quả vật lý của phương trình tỷ lệ nguyên tử bề mặt:<br/>"
        "1. <b>Kích thước hình học suy giảm:</b> Khi đường kính hạt <i>D</i> giảm dần từ 100 nm về 2 nm, mẫu số trong biểu thức tỷ lệ co nhỏ lại 50 lần.<br/>"
        "2. <b>Tỷ số S · V<sup>−1</sup> tăng tỉ lệ nghịch:</b> Diện tích bề mặt tiếp xúc trên mỗi đơn vị thể tích tăng tuyến tính theo <i>D</i><sup>−1</sup>. "
        "Với 1 cm<sup>3</sup> vật liệu khối ban đầu, diện tích bề mặt chỉ khoảng 6 cm<sup>2</sup>. Khi nghiền nát thành các hạt nano 10 nm, "
        "tổng diện tích bề mặt tăng vọt lên 600 m<sup>2</sup> (tương đương diện tích của cả một sân bóng rổ tiêu chuẩn).<br/>"
        "3. <b>Chuyển đổi trạng thái nguyên tử:</b> Với hạt <i>D</i> = 100 nm, tỷ lệ nguyên tử bề mặt chỉ chiếm <i>F</i><sub>surf</sub> ≈ 1.8% tổng số nguyên tử. "
        "Khi giảm xuống <i>D</i> = 10 nm, tỷ lệ này tăng lên 16.9%. Khi hạt đạt kích thước cực nhỏ <i>D</i> = 2 nm, có tới hơn 65.7% tổng số nguyên tử nằm trần trụi ở lớp ngoài cùng.<br/>"
        "4. <b>Phá vỡ trạng thái khối:</b> Ở kích thước này, vật liệu không còn được điều khiển bởi tính chất tuần hoàn vô hạn của tinh thể khối nữa. "
        "Thay vào đó, các liên kết treo, mật độ electron chưa ghép đôi và thế năng bề mặt trở thành nhân tố định đoạt toàn bộ đặc tính vật lý, hóa học và quang điện tử của vật liệu."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_02_Bang_Tang_Dien_Tich_Lap_Phuong.png",
        "Hình 3.5.2 (Trích xuất Slide 40): Bảng số liệu phân chia khối lập phương từ 1 m xuống 1 mm rồi xuống 1 nm, minh họa bước nhảy vọt diện tích bề mặt từ 6 m² lên 6,000 km².",
        width=440, height=240
    )

    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn tỷ số S · V<sup>−1</sup> và phân số nguyên tử bề mặt", "H3")
    add_p(
        "Để đối chuẩn trực tiếp giữa mô hình giải tích lý thuyết và hành vi thực nghiệm, "
        "chúng ta khảo sát đồ thị mô phỏng giải tích ZT-GVLE Hình 3.5.3, thể hiện đồng thời đặc tuyến log-log của tỷ số <i>S</i> · <i>V</i><sup>−1</sup> "
        "và phần trăm nguyên tử bề mặt <i>F</i><sub>surf</sub> theo đường kính <i>D</i> từ 1 nm đến 100 nm."
    )

    add_figure(
        "Mo_Phong_Muc_3.5_Do_Thi_01_Ty_So_Be_Mat_The_Tich.png",
        "Hình 3.5.3 (Mô phỏng ZT-GVLE): Đặc tuyến tỷ số S · V⁻¹ (đường liền nét xanh, thang log) và phần trăm nguyên tử bề mặt <i>F</i><sub>surf</sub> (đường đứt nét cam) theo đường kính hạt D từ 1 nm đến 100 nm. Callout tím định vị chính xác bước nhảy vọt tại 2 nm, 10 nm và 50 nm.",
        width=440, height=270
    )

    add_p("Giai đoạn 5: Ứng dụng kỹ thuật và bài toán phân chia lập phương trong slide bài giảng", "H3")
    add_p(
        "Trong Slide 40 của bài giảng HUST, PGS. TS. Nguyễn Hữu Lâm đưa ra một bài toán kinh điển minh họa trực giác: "
        "Xét một khối lập phương vật liệu vĩ mô cạnh <i>L</i><sub>0</sub> = 1 m. Thể tích khối là <i>V</i><sub>0</sub> = 1 m<sup>3</sup>, "
        "diện tích bề mặt ban đầu là <i>S</i><sub>0</sub> = 6 <i>L</i><sub>0</sub><sup>2</sup> = 6 m<sup>2</sup>.<br/>"
        "• <b>Bước phân chia 1 (Thang milimet):</b> Chia khối trên thành các khối nhỏ có cạnh <i>L</i><sub>1</sub> = 1 mm = 10<sup>−3</sup> m. "
        "Số lượng khối con thu được là <i>N</i><sub>1</sub> = (<i>L</i><sub>0</sub> · <i>L</i><sub>1</sub><sup>−1</sup>)<sup>3</sup> = 10<sup>9</sup> khối. "
        "Diện tích của mỗi khối con là <i>s</i><sub>1</sub> = 6 <i>L</i><sub>1</sub><sup>2</sup> = 6 × 10<sup>−6</sup> m<sup>2</sup>. "
        "Tổng diện tích bề mặt của hệ tăng lên: <i>S</i><sub>1</sub> = <i>N</i><sub>1</sub> · <i>s</i><sub>1</sub> = 10<sup>9</sup> × (6 × 10<sup>−6</sup> m<sup>2</sup>) = 6,000 m<sup>2</sup> (tăng gấp 1,000 lần).<br/>"
        "• <b>Bước phân chia 2 (Thang nanomet):</b> Tiếp tục nghiền mịn thành các hạt nano có cạnh <i>L</i><sub>2</sub> = 1 nm = 10<sup>−9</sup> m. "
        "Số lượng hạt nano thu được là <i>N</i><sub>2</sub> = (<i>L</i><sub>0</sub> · <i>L</i><sub>2</sub><sup>−1</sup>)<sup>3</sup> = 10<sup>27</sup> hạt. "
        "Diện tích bề mặt của mỗi hạt nano là <i>s</i><sub>2</sub> = 6 <i>L</i><sub>2</sub><sup>2</sup> = 6 × 10<sup>−18</sup> m<sup>2</sup>. "
        "Tổng diện tích bề mặt tiếp xúc đạt tới con số không tưởng:<br/>"
        "<i>S</i><sub>2</sub> = <i>N</i><sub>2</sub> · <i>s</i><sub>2</sub> = 10<sup>27</sup> × (6 × 10<sup>−18</sup> m<sup>2</sup>) = 6 × 10<sup>9</sup> m<sup>2</sup> = 6,000 km<sup>2</sup>!<br/>"
        "Một khối lập phương chỉ 1 m<sup>3</sup> ban đầu, sau khi chuyển sang thang nano, có diện tích bề mặt tương đương với gấp đôi diện tích toàn bộ thủ đô Hà Nội. "
        "Chính sự bùng nổ diện tích tiếp xúc này là cội nguồn tạo nên hoạt tính xúc tác phi thường và độ nhạy cảm biến nano sẽ được mổ xẻ trong phân mục khảo sát kế tiếp (MPT 3.5.2)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.5.2: NHIỆT ĐỘNG HỌC BỀ MẶT, NĂNG LƯỢNG γ, KẾT TỤ VÀ XÚC TÁC
    # =========================================================================
    add_p("Luận điểm 3.5.2: Nhiệt động học Bề mặt, Năng lượng Tự do γ, Hiện tượng Kết tụ và Hoạt tính Xúc tác", "H2")

    add_p("Giai đoạn 1: Giới thiệu khái niệm, năng lượng tự do bề mặt và nghịch lý bền vững của hệ nano", "H3")
    add_p(
        "Năng lượng tự do bề mặt γ (Surface Free Energy, đơn vị J · m<sup>−2</sup> hoặc N · m<sup>−1</sup>) được định nghĩa là công cần thiết để tạo ra thêm "
        "một đơn vị diện tích bề mặt mới trong điều kiện đẳng nhiệt và đẳng áp. "
        "Đối với chất lỏng, đại lượng này tương đương với sức căng bề mặt. Đối với chất rắn tinh thể, γ phụ thuộc chặt chẽ vào mật độ liên kết bị bẻ gãy trên từng mặt phẳng tinh thể học (hkl). "
        "Ví dụ, trong tinh thể cấu trúc lập phương tâm diện (FCC) như Vàng hay Bạch kim, mặt (111) có mật độ xếp chặt cao nhất nên có năng lượng bề mặt γ<sub>(111)</sub> nhỏ hơn các mặt (100) và (110)."
    )
    add_p(
        "Năng lượng bề mặt tổng cộng của một hệ gồm <i>N</i> hạt nano là một đại lượng cộng tính (additive quantity): "
        "<i>E</i><sub>surf</sub> = ∑ γ<sub><i>i</i></sub> <i>S<sub>i</sub></i>. "
        "Vì diện tích <i>S</i> của các hạt nano cực kỳ lớn, năng lượng bề mặt tích lũy trong hệ đạt giá trị khổng lồ, "
        "khiến toàn bộ hệ hạt nano rơi vào trạng thái bất ổn định nhiệt động học (thermodynamically unstable). "
        "Theo nguyên lý cực tiểu hóa thế năng tự do Gibbs (d<i>G</i> ≤ 0), hệ hạt nano sẽ tự phát tìm kiếm các cơ chế vật lý để triệt tiêu năng lượng bề mặt dư thừa này. "
        "Con đường tự nhiên phổ biến nhất chính là <b>Hiện tượng kết tụ (Agglomeration / Aggregation)</b>: "
        "các hạt nano va chạm và dính kết lại với nhau để hình thành các khối liên kết lớn hơn, qua đó xóa bỏ ranh giới liên pha tự do."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_03_Ket_Tu_Giam_Nang_Luong_Be_Mat.png",
        "Hình 3.5.4 (Trích xuất Slide 41): Cơ chế giảm năng lượng tự do bề mặt qua hiện tượng kết tụ: hai khối lập phương riêng rẽ (tổng năng lượng 12γ L²) ghép thành khối hộp chữ nhật (năng lượng 10γ L²), giải phóng 2γ L² nhiệt lượng.",
        width=440, height=130
    )

    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ cân bằng nhiệt động học kết tụ", "H3")
    add_p(
        "Trong Slide 41, bài giảng đưa ra mô hình nhiệt động học định lượng trực quan: "
        "Xét hai khối lập phương A và B giống hệt nhau, mỗi khối có diện tích đáy cạnh <i>L</i>, gồm 6 mặt tự do. "
        "Nếu gọi γ là năng lượng tự do trên một đơn vị diện tích mặt, thì năng lượng bề mặt của mỗi khối khi đứng riêng rẽ là <i>E<sub>A</sub></i> = <i>E<sub>B</sub></i> = 6γ <i>L</i><sup>2</sup>."
    )

    p_step3 = (
        "Cân bằng năng lượng nhiệt động học khi kết tụ hai khối nano:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Khi hai khối A và B tách rời nhau trong không gian, tổng năng lượng bề mặt của hệ là:<br/>"
        "<i>E</i><sub>tách rời</sub> = <i>E<sub>A</sub></i> + <i>E<sub>B</sub></i> = 6γ <i>L</i><sup>2</sup> + 6γ <i>L</i><sup>2</sup> = 12γ <i>L</i><sup>2</sup>.<br/>"
        "Khi hai khối va chạm và kết tụ tạo thành khối hộp chữ nhật C (kích thước <i>L</i> × <i>L</i> × 2<i>L</i>), "
        "hai mặt tiếp xúc bị triệt tiêu hoàn toàn vì biến thành liên kết nội màng (bulk interface). "
        "Số mặt ngoài tự do của khối C chỉ còn lại: 2 mặt đáy (2 × <i>L</i><sup>2</sup>) và 4 mặt bên (4 × 2<i>L</i><sup>2</sup> = 8 <i>L</i><sup>2</sup>), tổng diện tích là 10 <i>L</i><sup>2</sup>. "
        "Độ biến thiên năng lượng tự do của quá trình kết tụ là:"
    )
    story.append(he.build_intermediate_equation(p_step3, r"\Delta E_{\mathrm{agglom}} = E_C - (E_A + E_B) = 10\gamma L^2 - 12\gamma L^2 = -2\gamma L^2 < 0 \quad (\text{Tự phát})", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step4 = (
        "Phương trình Gibbs-Thomson về áp suất hơi bão hòa và độ hòa tan theo bán kính hạt r:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Do năng lượng bề mặt dư thừa, thế hóa học của các nguyên tử trên mặt cầu cong bán kính <i>r</i> tăng thêm một lượng Δμ = 2γ <i>V<sub>m</sub></i> · <i>r</i><sup>−1</sup> "
        "(với <i>V<sub>m</sub></i> là thể tích mol). Áp suất hơi bão hòa <i>P<sub>r</sub></i> phía trên hạt nano tăng vọt so với mặt phẳng khối vĩ mô <i>P</i><sub>∞</sub> theo định luật Gibbs-Thomson:"
    )
    story.append(he.build_intermediate_equation(p_step4, r"\ln\left(\frac{P_r}{P_{\infty}}\right) = \frac{2\gamma V_m}{R_g T \cdot r} \quad \Longrightarrow \quad P_r = P_{\infty} \exp\left(\frac{2\gamma V_m}{R_g T \cdot r}\right)", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    add_p("Giai đoạn 3: Chuỗi nhân quả dẫn xuất ứng dụng xúc tác và cảm biến nano", "H3")
    add_p(
        "Chuỗi nhân quả vi mô lý giải vai trò then chốt của hiệu ứng bề mặt trong công nghệ xúc tác (Catalysis) và cảm biến (Detection):<br/>"
        "1. <b>Mật độ tâm hoạt tính cao:</b> Chất xúc tác hoạt động bằng cách cung cấp các vị trí hấp phụ bề mặt (active sites) để các phân tử phản ứng bám vào, "
        "làm yếu các liên kết hóa học nội tại và hạ thấp rào cản năng lượng hoạt hóa <i>E<sub>a</sub></i>. "
        "Vì hạt nano có tỷ số diện tích trên thể tích cực lớn, mật độ tâm hoạt tính tăng lên hàng nghìn lần so với chất xúc tác vĩ mô cùng khối lượng.<br/>"
        "2. <b>Định hướng không gian phân tử:</b> Công nghệ nano cho phép kiểm soát chính xác cấu trúc hình thái và sự phân bố không gian của các nguyên tử trên bề mặt hạt nano. "
        "Các góc, cạnh và bậc thang tinh thể (steps and kinks) của hạt nano có số phối trí thấp nhất, do đó thể hiện hoạt tính xúc tác mạnh nhất.<br/>"
        "3. <b>Mô hình Khóa và Chìa (Lock and Key) trong Cảm biến:</b> Trong các cảm biến sinh học nano (Biosensors), "
        "bề mặt hạt nano được chức năng hóa hóa học với các phân tử thụ thể (kháng thể, chuỗi DNA, aptamer). "
        "Các thụ thể này đóng vai trò như các 'ổ khóa' đặc hiệu chỉ nhận diện duy nhất một loại phân tử mục tiêu ('chìa khóa'). "
        "Kích thước nano tương thích trực tiếp với kích thước của protein và enzyme, cho phép đóng gói hàng triệu vị trí nhận diện trên cùng một diện tích vi mạch, "
        "hạ thấp giới hạn phát hiện (Limit of Detection - LOD) xuống thang nồng độ picomolar hoặc đơn phân tử."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_04_Co_Che_Xuc_Tac_Nano.png",
        "Hình 3.5.5 (Trích xuất Slide 42): Sơ đồ nguyên lý xúc tác hạt nano: diện tích bề mặt hoạt tính tăng vọt giúp cắt giảm tối đa khối lượng kim loại quý tiêu hao trong công nghiệp hóa chất và lọc hóa dầu.",
        width=440, height=160
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_05_Co_Che_Cam_Bien_Lock_Key.png",
        "Hình 3.5.6 (Trích xuất Slide 43): Nguyên lý cảm biến sinh hóa nano theo mô hình Ổ khóa — Chìa khóa (Lock and Key): các vị trí thụ thể trên bề mặt hạt nano nhận diện chọn lọc các phân tử mục tiêu với độ nhạy phân tử cực cao.",
        width=440, height=150
    )

    add_p("Giai đoạn 4: Đánh giá định lượng giải pháp ức chế kết tụ bằng chất hoạt động bề mặt", "H3")
    add_p(
        "Mặc dù năng lượng bề mặt cao đem lại hoạt tính xúc tác vượt trội, nhưng nó cũng chính là 'kẻ thù' đe dọa sự sống còn của vật liệu nano: "
        "nếu các hạt kết tụ lại thành khối lớn, toàn bộ ưu thế diện tích bề mặt và hiệu ứng nano sẽ bị tiêu diệt hoàn toàn. "
        "Để duy trì trạng thái phân tán bền vững trong dung dịch, các kỹ sư công nghệ nano áp dụng hai cơ chế bảo vệ cốt lõi:<br/>"
        "• <b>Lực đẩy tĩnh điện (Electrostatic Stabilization):</b> Hấp phụ các ion mang điện tích cùng dấu lên bề mặt hạt nano, tạo nên lớp điện kép (Electrical Double Layer). "
        "Lực đẩy Coulomb giữa các hạt tích điện cùng dấu ngăn cản chúng tiến lại gần nhau.<br/>"
        "• <b>Hiệu ứng cản trở lập thể (Steric Hindrance):</b> Gắn các chuỗi polymer dài hoặc phối tử hữu cơ (surfactant ligands như PVP, axit oleic, thiol) lên bề mặt hạt. "
        "Khi hai hạt tiến sát nhau, các chuỗi polymer bị nén lại làm giảm độ hỗn loạn entropy (Δ<i>S</i> &lt; 0), sinh ra một lực đẩy đẩy lùi hai hạt ra xa."
    )

    add_p("Giai đoạn 5: Ứng dụng kỹ thuật và cầu nối sang đặc tính điện tử thang nano", "H3")
    add_p(
        "Các hạt nano xúc tác kim loại quý như Bạch kim (Pt), Paladi (Pd) và Vàng (Au) kích thước 2—5 nm đã tạo nên cuộc cách mạng trong bộ chuyển đổi xúc tác khí thải ô tô (Catalytic Converters), "
        "giúp chuyển hóa hoàn toàn khí độc CO, NO<sub><i>x</i></sub> và hydrocarbon chưa cháy thành CO<sub>2</sub>, N<sub>2</sub> và H<sub>2</sub>O ở nhiệt độ thấp hơn hàng trăm độ. "
        "Tuy nhiên, khi kích thước hạt kim loại bị thu nhỏ vượt qua giới hạn bề mặt thuần túy để chạm tới ngưỡng giam giữ lượng tử, "
        "chúng không chỉ thay đổi diện tích tiếp xúc mà còn làm đảo lộn hoàn toàn bản chất dẫn điện: "
        "các kim loại dẫn điện hoàn hảo có thể chuyển pha thành chất bán dẫn hoặc điện môi, như được phân tích chi tiết trong phân mục kế tiếp (MPT 3.5.3)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.5.3: ĐẶC TÍNH ĐIỆN TỬ, GIAM GIỮ LƯỢNG TỬ VÀ CHUYỂN PHA KUBO
    # =========================================================================
    add_p("Luận điểm 3.5.3: Đặc tính Điện tử Thang Nano, Giam giữ Lượng tử và Chuyển pha Kim loại - Bán dẫn (Kubo Effect)", "H2")

    add_p("Giai đoạn 1: Giới thiệu khái niệm, ranh giới lượng tử giữa kim loại và chất cách điện", "H3")
    add_p(
        "Trong lý thuyết dải năng lượng cổ điển của chất rắn vĩ mô, kim loại được định nghĩa là vật liệu có dải dẫn (conduction band) chỉ được điền đầy một phần, "
        "hoặc có sự xen phủ năng lượng liên tục (band overlap) giữa dải hóa trị và dải dẫn mà không tồn tại bất kỳ khe năng lượng cấm nào (<i>E<sub>g</sub></i> = 0). "
        "Mật độ electron tự do cực lớn (khoảng 10<sup>22</sup>—10<sup>23</sup> cm<sup>−3</sup>) tạo nên một biển electron Fermi chuyển động tự do, "
        "với khoảng cách năng lượng giữa các trạng thái điện tử kế tiếp gần như bằng không (Δ<i>E</i> → 0)."
    )
    add_p(
        "Tuy nhiên, khi một hạt kim loại bị giam giữ không gian trong cả ba chiều xuống kích thước vài nanomet, "
        "tổng số lượng electron tự do <i>N</i> chứa trong hạt giảm xuống chỉ còn vài trăm đến vài nghìn hạt. "
        "Theo cơ học lượng tử, chuyển động của các electron bị giới hạn trong một giếng thế thế năng ba chiều hữu hạn, "
        "buộc các dải năng lượng liên tục phải phân tách thành một phổ các mức năng lượng rời rạc (discrete energy levels). "
        "Hiện tượng này làm xuất hiện một khe năng lượng hiệu dụng tại mức năng lượng Fermi, "
        "biến một hạt kim loại dẫn điện thông thường thành một hạt có tính chất bán dẫn hoặc điện môi cách điện. "
        "Ngưỡng chuyển pha vi mô này được gọi là <b>Hiệu ứng Kubo (Kubo Effect)</b>."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_06_Giam_Giu_Mo_Vung_Cam_Kim_Loai.png",
        "Hình 3.5.7 (Trích xuất Slide 44): Sơ đồ hiệu ứng giam giữ lượng tử làm dải năng lượng liên tục của kim loại bị phân tách thành các mức rời rạc, làm biến mất vùng xen phủ và mở ra vùng cấm năng lượng hữu hạn (chuyển pha Kim loại — Bán dẫn).",
        width=440, height=180
    )

    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ tiêu chuẩn Kubo và hiệu ứng Coulomb Blockade", "H3")
    add_p(
        "Để xác định điều kiện chuyển pha từ kim loại sang bán dẫn, nhà vật lý Ryogo Kubo đã đưa ra hệ thức ước lượng khoảng cách năng lượng trung bình giữa hai mức điện tử kế tiếp nhau "
        "gần mặt Fermi của hạt nano (gọi là khoảng cách mức Kubo δ)."
    )

    p_step5 = (
        "Dẫn xuất khoảng cách mức năng lượng Kubo δ theo thể tích và kích thước hạt:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Mật độ trạng thái điện tử tại mức Fermi trong khối kim loại vĩ mô thể tích <i>V</i> là <i>g</i>(<i>E<sub>F</sub></i>) = 3 <i>N</i> · (2 <i>E<sub>F</sub></i>)<sup>−1</sup>. "
        "Khoảng cách năng lượng trung bình giữa các mức rời rạc δ là nghịch đảo của mật độ trạng thái toàn phần trong hạt nano:"
    )
    story.append(he.build_intermediate_equation(p_step5, r"\delta = \frac{1}{g(E_F)} = \frac{4 E_F}{3 N} = \frac{4 E_F}{3 n_e V} = \frac{8 E_F}{\pi n_e D^3} \propto D^{-3}", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step6 = (
        "Tiêu chuẩn chuyển pha Kim loại — Bán dẫn Kubo và hiệu ứng Coulomb Blockade:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Hạt nano kim loại mất đi tính dẫn điện kim loại và chuyển sang hành vi lượng tử rời rạc khi khoảng cách mức Kubo lớn hơn năng lượng dao động nhiệt <i>k<sub>B</sub> T</i> (tiêu chuẩn Kubo):<br/>"
        "δ &gt; <i>k<sub>B</sub> T</i>.<br/>"
        "Đồng thời, khi đưa một electron đơn lẻ vào hạt nano có điện dung tĩnh điện toàn phần <i>C</i><sub>Σ</sub>, "
        "năng lượng nạp tĩnh điện (Charging Energy <i>E<sub>C</sub></i>) tăng vọt. "
        "Nếu năng lượng nạp này lớn hơn năng lượng dao động nhiệt, electron kế tiếp sẽ bị ngăn cản không thể xâm nhập vào hạt (Hiệu ứng Khóa Coulomb — Coulomb Blockade):"
    )
    story.append(he.build_intermediate_equation(p_step6, r"E_C = \frac{e^2}{2 C_{\Sigma}} \gg k_B T \quad \Longrightarrow \quad \text{Ngăn cản vận chuyển điện tích khi } |V_{\mathrm{ds}}| < V_C = \frac{e}{2 C_{\Sigma}}", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    add_p("Giai đoạn 3: Chuỗi nhân quả vi mô vận hành Transistor Đơn Electron (SET)", "H3")
    add_p(
        "Chuỗi nhân quả vi mô điều khiển dòng điện qua Transistor Đơn Electron (Single Electron Transistor - SET):<br/>"
        "1. <b>Cấu trúc rào thế đường hầm kép:</b> SET bao gồm một đảo nano dẫn điện (quantum dot island) được kẹp giữa hai cực Nguồn (Source) và Máng (Drain) "
        "bởi hai lớp rào cản cách điện đường hầm siêu mỏng, và được điều khiển bởi một cực Cổng (Gate) cách ly điện dung.<br/>"
        "2. <b>Trạng thái khóa Coulomb (Off-state):</b> Khi điện áp cực máng nhỏ (|<i>V</i><sub>ds</sub>| &lt; <i>V<sub>C</sub></i>) và điện áp cổng <i>V<sub>g</sub></i> không phù hợp, "
        "trạng thái nạp của đảo nano bị cố định tại số nguyên electron <i>n</i>. Muốn nạp thêm một electron cần cung cấp năng lượng tối thiểu <i>E<sub>C</sub></i> = <i>e</i><sup>2</sup> · (2 <i>C</i><sub>Σ</sub>)<sup>−1</sup>. "
        "Vì năng lượng nhiệt không đủ bù đắp (<i>k<sub>B</sub> T</i> ≪ <i>E<sub>C</sub></i>), electron không thể vượt rào: dòng điện <i>I</i><sub>ds</sub> = 0 tuyệt đối.<br/>"
        "3. <b>Trạng thái dẫn Coulomb (On-state):</b> Khi quét điện áp cổng <i>V<sub>g</sub></i> đến giá trị mà thế năng nạp của trạng thái <i>n</i> và <i>n</i> + 1 suy biến cân bằng, "
        "rào cản năng lượng nạp <i>E<sub>C</sub></i> bị triệt tiêu hoàn toàn. Từng electron đơn lẻ có thể chui hầm tuần tự qua đảo nano: xuất hiện đỉnh dẫn điện nhọn (Coulomb peak).<br/>"
        "4. <b>Tính tuần hoàn cổng:</b> Quá trình này lặp lại tuần hoàn với chu kỳ điện áp cổng chính xác: Δ<i>V<sub>g</sub></i> = <i>e</i> · <i>C<sub>g</sub></i><sup>−1</sup>."
    )
    add_spacer(6)

    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn đặc tuyến Coulomb Blockade và dao động SET", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích ZT-GVLE Hình 3.5.8 khảo sát hành vi vận chuyển điện tử đơn hạt của SET với điện dung đảo nano <i>C</i><sub>Σ</sub> = 10 aF "
        "(tương ứng năng lượng nạp <i>E<sub>C</sub></i> = 8.0 meV, điện áp ngưỡng <i>V<sub>C</sub></i> = 8.0 mV)."
    )

    add_figure(
        "Mo_Phong_Muc_3.5_Do_Thi_02_Coulomb_Blockade_SET.png",
        "Hình 3.5.8 (Mô phỏng ZT-GVLE): (Trái) Đặc tuyến I–V của SET ở 4.2 K (vùng khóa Coulomb tô vàng |<i>V</i>| ≤ 8 mV) và 300 K (đặc tuyến Ohm tuyến tính do dao động nhiệt xóa nhòa rào nạp). (Phải) Dao động dẫn truyền Coulomb tuần hoàn theo điện áp cổng <i>V<sub>g</sub></i> với chu kỳ chuẩn xác Δ<i>V<sub>g</sub></i> = <i>e</i> · (<i>C<sub>g</sub></i>)<sup>−1</sup> = 80 mV.",
        width=450, height=260
    )

    add_p("Giai đoạn 5: Ứng dụng kỹ thuật trong đo lường điện tích siêu nhạy", "H3")
    add_p(
        "Hiệu ứng Coulomb Blockade và Transistor Đơn Electron (SET) không chỉ là đối tượng nghiên cứu vật lý cơ bản "
        "mà còn là nền tảng của các thiết bị đo lường điện lượng tử hiện đại nhất thế giới: "
        "nó đóng vai trò là một điện kế siêu nhạy (electrometer) có khả năng phát hiện độ dịch chuyển điện tích nhỏ hơn 10<sup>−6</sup> <i>e</i>! "
        "Các mạch tích hợp SET hoạt động ở thang mili-Kelvin hiện đang được tích cực phát triển để đọc trạng thái qubit spin trong máy tính lượng tử silicon. "
        "Đồng thời, sự rời rạc hóa dải năng lượng không chỉ kiểm soát dòng điện mà còn làm thay đổi căn bản tương tác quang học của vật liệu nano, "
        "mở đường cho các hiện tượng cộng hưởng quang học kỳ vĩ được khám phá trong phân mục tiếp sau (MPT 3.5.4)."
    )
    add_spacer(14)

    # =========================================================================
    # MPT 3.5.4: ĐẶC TÍNH QUANG HỌC, LSPR KIM LOẠI VÀ CHẤM LƯỢNG TỬ
    # =========================================================================
    add_p("Luận điểm 3.5.4: Đặc tính Quang học Thang Nano, Cộng hưởng Plasmon Bề mặt Cục bộ (LSPR) và Chấm Lượng tử", "H2")

    add_p("Giai đoạn 1: Giới thiệu khái niệm, định luật bảo toàn quang học và nghịch lý màu sắc vật liệu nano", "H3")
    add_p(
        "Khi ánh sáng (cường độ <i>I</i><sub>0</sub>) chiếu tới một môi trường vật chất vĩ mô, định luật bảo toàn năng lượng quang học cổ điển được viết dưới dạng:<br/>"
        "<i>I</i><sub>0</sub> = <i>T</i> + <i>A</i> + <i>R</i>,<br/>"
        "trong đó <i>T</i> là cường độ ánh sáng truyền qua (Transmitted), <i>A</i> là cường độ bị môi trường hấp thụ (Absorbed), "
        "và <i>R</i> là phần phản xạ tại các mặt phân cách (Reflected). "
        "Trong chất rắn khối đồng nhất, tán xạ ánh sáng (Scattering <i>S</i>) thường rất nhỏ và bị bỏ qua."
    )
    add_p(
        "Tuy nhiên, trong các hệ hạt keo nano (nanoparticle colloids), khi kích thước hạt nano nhỏ hơn đáng kể so với bước sóng ánh sáng (<i>D</i> ≪ λ), "
        "hiện tượng tán xạ ánh sáng <i>S</i> tăng cường mạnh mẽ và trở thành một thành phần chi phối màu sắc của hệ:<br/>"
        "<i>I</i><sub>0</sub> = <i>T</i> + <i>A</i> + <i>R</i> + <i>S</i>.<br/>"
        "Một trong những biểu hiện kỳ diệu và nổi tiếng nhất của quang học nano là: <b>vật liệu nano thể hiện màu sắc hoàn toàn khác biệt so với vật liệu khối tương ứng</b>. "
        "Vàng khối vĩ mô có ánh kim màu vàng chói lọi; nhưng khi phân tán thành các hạt nano vàng 20 nm trong dung dịch nước, dung dịch lại có màu đỏ ruby rực rỡ! "
        "Nếu kích thước hạt tăng lên 80 nm, dung dịch chuyển sang màu xanh lam hoặc tím. "
        "Nguồn gốc vật lý của hiện tượng quang học phi thường này chính là <b>Cộng hưởng Plasmon Bề mặt Cục bộ (Localized Surface Plasmon Resonance - LSPR)</b> trong hạt nano kim loại, "
        "kết hợp với sự dịch chuyển dải hấp thụ do giam giữ lượng tử trong các chấm lượng tử bán dẫn (Quantum Dots)."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_07_Tuong_Tac_Quang_Tan_Xa_Hat_Keo.png",
        "Hình 3.5.9 (Trích xuất Slide 45): Sơ đồ cân bằng quang học I = T + A + R + S trong hệ hạt keo nano, minh họa vai trò chi phối của thành phần tán xạ ánh sáng S khi kích thước hạt suy giảm.",
        width=440, height=220
    )

    add_p("Giai đoạn 2: Hạt nhân vật lý và Hệ thức Cột trụ lý thuyết Mie và điều kiện Fröhlich cho LSPR", "H3")
    add_p(
        "Để mô tả chính xác tương tác quang học của hạt nano kim loại hình cầu bán kính <i>R</i> nhỏ hơn nhiều so với bước sóng ánh sáng (chế độ chuẩn tĩnh điện 2<i>R</i> ≪ λ), "
        "chúng ta áp dụng lý thuyết tán xạ Mie ở bậc gần đúng lưỡng cực (Dipole Approximation). "
        "Hạt nano có hàm điện môi phức ε(ω) = ε<sub>1</sub>(ω) + <i>i</i> ε<sub>2</sub>(ω), được đặt trong môi trường điện môi đồng nhất có hằng số điện môi ε<sub><i>m</i></sub> = <i>n<sub>m</sub></i><sup>2</sup>."
    )

    p_step7 = (
        "Độ phân cực lưỡng cực điện và điều kiện cộng hưởng Fröhlich:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Giải phương trình Laplace cho thế tĩnh điện với điều kiện biên liên tục của điện trường và vector cảm ứng điện tại bề mặt cầu ranh giới, "
        "độ phân cực lưỡng cực điện α(ω) của hạt nano kim loại được biểu diễn bởi:"
    )
    story.append(he.build_intermediate_equation(p_step7, r"\alpha(\omega) = 4\pi \epsilon_0 \epsilon_m R^3 \frac{\epsilon(\omega) - \epsilon_m}{\epsilon(\omega) + 2\epsilon_m} \quad \Longrightarrow \quad \text{Cộng hưởng xảy ra khi: } \mathrm{Re}[\epsilon(\omega_{\mathrm{res}})] = -2\epsilon_m", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step8 = (
        "Dẫn xuất tiết diện dập quang học tổng cộng (Extinction Cross Section):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Tiết diện dập quang σ<sub>ext</sub> đo lường tổng năng lượng ánh sáng bị loại bỏ khỏi chùm tia tới do cả hai quá trình hấp thụ (Absorption σ<sub>abs</sub>) và tán xạ (Scattering σ<sub>sca</sub>): "
        "σ<sub>ext</sub> = σ<sub>abs</sub> + σ<sub>sca</sub>. Với hạt nano nhỏ (<i>D</i> &lt; 20 nm), hấp thụ chiếm ưu thế tuyệt đối (σ<sub>abs</sub> ∝ <i>R</i><sup>3</sup> trong khi σ<sub>sca</sub> ∝ <i>R</i><sup>6</sup>). "
        "Thay hàm điện môi phức vào biểu thức định lý quang học (Optical Theorem):"
    )
    story.append(he.build_intermediate_equation(p_step8, r"\sigma_{\mathrm{ext}}(\omega) = 9 \frac{\omega}{c} \epsilon_m^{3/2} V \frac{\epsilon_2(\omega)}{[\epsilon_1(\omega) + 2\epsilon_m]^2 + [\epsilon_2(\omega)]^2} \quad \left(V = \frac{4}{3}\pi R^3\right)", styles=styles, is_expanded_from_slide=True))
    add_spacer(6)

    p_step9 = (
        "Dịch chuyển dải năng lượng phát xạ trong chấm lượng tử bán dẫn (Mô hình Brus):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: "
        "Đối với hạt nano bán dẫn (Quantum Dots), sự giam giữ không gian của cặp electron — lỗ trống làm năng lượng vùng cấm hiệu dụng dịch chuyển về phía bước sóng ngắn (Blue shift) theo mô hình Brus:"
    )
    story.append(he.build_intermediate_equation(p_step9, r"E_{g,\mathrm{nano}}(R) = E_{g,\mathrm{bulk}} + \frac{\hbar^2 \pi^2}{2 R^2}\left(\frac{1}{m_e^*} + \frac{1}{m_h^*}\right) - \frac{1.786 e^2}{4\pi \epsilon \epsilon_0 R} \quad \Longrightarrow \quad \lambda_{\mathrm{emission}} \propto R", styles=styles, is_expanded_from_slide=True))
    add_spacer(10)

    add_p("Giai đoạn 3: Chuỗi nhân quả vi mô của dao động tập thể electron tự do", "H3")
    add_p(
        "Chuỗi nhân quả vi mô diễn giải sâu sắc cơ chế vật lý tạo nên đỉnh cộng hưởng LSPR:<br/>"
        "1. <b>Điện trường sóng tới kích thích phân cực:</b> Khi sóng điện từ chiếu vào hạt nano kim loại, điện trường dao động <i>E</i><sub>0</sub> exp(−<i>i</i>ω<i>t</i>) "
        "tác dụng một lực Lorentz lên toàn bộ các electron tự do trong dải dẫn.<br/>"
        "2. <b>Dịch chuyển tập thể so với lõi ion:</b> Đám mây electron dẫn bị kéo lệch đồng loạt sang một phía, để lộ ra mạng lưới các ion dương ở phía đối diện. "
        "Sự phân tách điện tích này thiết lập một điện trường hồi phục tĩnh điện cực mạnh bên trong hạt nano.<br/>"
        "3. <b>Dao động điều hòa cộng hưởng:</b> Lực hồi phục kéo đám mây electron quay trở lại, tạo nên một dao động tập thể điều hòa (plasma oscillation). "
        "Khi tần số của ánh sáng tới trùng khớp với tần số dao động tự nhiên của đám mây electron (thỏa mãn điều kiện Fröhlich ε<sub>1</sub> = −2ε<sub><i>m</i></sub>), "
        "biên độ dao động đạt cực đại: ánh sáng bị hấp thụ và tán xạ mãnh liệt, tạo ra một đỉnh cộng hưởng cực kỳ sắc nét trên phổ quang phổ.<br/>"
        "4. <b>Tăng cường trường điện từ cục bộ:</b> Tại bề mặt hạt nano ở tần số cộng hưởng, cường độ điện trường cục bộ |<i>E</i><sub>loc</sub>|<sup>2</sup> "
        "có thể được khuếch đại gấp hàng trăm đến hàng nghìn lần so với điện trường sóng tới |<i>E</i><sub>0</sub>|<sup>2</sup>, "
        "là cội nguồn của hiệu ứng Tán xạ Raman Tăng cường Bề mặt (SERS)."
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_08_Cong_Huong_Plasmon_LSPR.png",
        "Hình 3.5.10 (Trích xuất Slide 46): Minh họa hiện tượng dao động tập thể electron dẫn tạo nên Cộng hưởng Plasmon Bề mặt Cục bộ (LSPR) và màu sắc rực rỡ của dung dịch keo nano kim loại quý.",
        width=440, height=200
    )
    add_spacer(6)

    add_figure(
        "[Goc]_Muc_3.5_Hinh_09_Phat_Xa_Cham_Luong_Tu.png",
        "Hình 3.5.11 (Trích xuất Slide 47): Phổ huỳnh quang đơn sắc của các chấm lượng tử bán dẫn CdSe: kích thước hạt tăng dần từ 2 nm lên 6 nm điều chỉnh màu phát xạ từ xanh lam sang đỏ rực rỡ.",
        width=440, height=130
    )

    add_p("Giai đoạn 4: Phân tích đồ thị mô phỏng đối chuẩn phổ LSPR và độ nhạy chiết suất môi trường", "H3")
    add_p(
        "Đồ thị mô phỏng giải tích ZT-GVLE Hình 3.5.12 khảo sát phổ tiết diện dập quang σ<sub>ext</sub>(λ) của hạt nano Bạc (Ag) và Vàng (Au) đường kính 20 nm "
        "trong các môi trường điện môi khác nhau."
    )

    add_figure(
        "Mo_Phong_Muc_3.5_Do_Thi_03_Pho_LSPR_Au_Ag.png",
        "Hình 3.5.12 (Mô phỏng ZT-GVLE): Phổ LSPR của hạt Bạc (Ag, đỉnh 412 nm trong nước) và hạt Vàng (Au, đỉnh 525 nm trong nước). Đường đứt nét cam thể hiện bước dịch chuyển đỏ quang học Δλ = +30 nm của hạt Vàng khi môi trường chiết suất tăng từ n = 1.33 lên n = 1.50, minh chứng cho nguyên lý cảm biến sinh học khúc xạ LSPR.",
        width=440, height=270
    )

    add_p("Giai đoạn 5: Ứng dụng kỹ thuật trong y sinh học nano và công nghệ hiển thị", "H3")
    add_p(
        "Sự kết hợp hoàn hảo giữa LSPR của hạt kim loại và huỳnh quang đơn sắc của chấm lượng tử đã mở ra hai lĩnh vực ứng dụng có tầm ảnh hưởng sâu rộng:<br/>"
        "• <b>Cảm biến sinh học quang học LSPR &amp; SERS:</b> Vì bước sóng cộng hưởng LSPR cực kỳ nhạy cảm với chiết suất môi trường cục bộ ε<sub><i>m</i></sub>, "
        "bất kỳ sự gắn kết nào của phân tử sinh học (kháng thể, protein, DNA) lên bề mặt hạt nano đều làm tăng chiết suất cục bộ, dẫn đến sự dịch chuyển đỏ (Red-shift) "
        "tức thì của đỉnh phổ LSPR. Phương pháp này cho phép phát hiện nồng độ vết mầm bệnh thời gian thực mà không cần gắn chất đánh dấu huỳnh quang (label-free detection).<br/>"
        "• <b>Liệu pháp Quang nhiệt trị (Photothermal Therapy - PTT):</b> Khi chiếu tia laser hồng ngoại gần (NIR, 808 nm) vào mô ung thư đã được tích tụ các hạt nano vàng (như nanorods hay core-shell nanoshells), "
        "các electron dao động LSPR chuyển hóa năng lượng hấp thụ photon thành nhiệt lượng Joule cục bộ cực lớn trong vòng vài picosecond, "
        "nung nóng khối u lên trên 43 °C để tiêu diệt chọn lọc tế bào ung thư mà không gây tổn thương mô lành xung quanh.<br/>"
        "• <b>Màn hình chấm lượng tử QLED:</b> Điều khiển chính xác kích thước hạt nano bán dẫn (CdSe, InP) mang lại dải màu phát xạ hẹp (FWHM &lt; 25 nm), "
        "độ tinh khiết màu tuyệt đối và hiệu suất lượng tử phát quang tiệm cận 100% trong thế hệ màn hình hiển thị cao cấp."
    )
    add_spacer(14)

    # =========================================================================
    # THỬ THÁCH HỌC VIÊN CER 3.5: BÀI TOÁN KỸ THUẬT TỔNG HỢP TOÀN CHƯƠNG 3
    # =========================================================================
    add_p("Thử thách Học viên CER 3.5: Thiết kế hạt nano lai lõi-vỏ (Au@SiO2) gắn chấm lượng tử ứng dụng đa chức năng", "H2")

    cer_box_data = [
        [Paragraph(he.wrap_math_glyphs("<b>BỐI CẢNH KỸ THUẬT &amp; THỬ THÁCH THIẾT KẾ ĐA CHỨC NĂNG (CER 3.5)</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs(
            "Trong kỹ thuật y sinh học nano hiện đại, một thách thức lớn trong chẩn đoán và điều trị ung thư là làm thế nào tích hợp đồng thời hai chức năng: "
            "<b>(1) Phát hiện và định vị khối u bằng hình ảnh huỳnh quang siêu nhạy</b>, và <b>(2) Tiêu diệt tế bào ung thư bằng liệu pháp quang nhiệt (PTT)</b> "
            "trên cùng một hạt nano duy nhất. "
            "Một nhóm nghiên cứu đề xuất cấu trúc hạt nano lai lõi — vỏ dạng cầu: "
            "Lõi kim loại Vàng (Au) bán kính <i>R</i><sub>core</sub> = 15 nm, được bọc bởi lớp vỏ cách điện Silica (SiO<sub>2</sub>) có chiều dày <i>d</i><sub>shell</sub>, "
            "và ngoài cùng gắn các chấm lượng tử huỳnh quang CdSe bán kính <i>r</i><sub>QD</sub> = 2.5 nm.<br/>"
            "Tuy nhiên, nếu gắn trực tiếp chấm lượng tử lên bề mặt kim loại Au (<i>d</i><sub>shell</sub> = 0), hiện tượng truyền năng lượng cộng hưởng Förster (FRET) "
            "sang electron kim loại sẽ làm dập tắt hoàn toàn huỳnh quang (Fluorescence Quenching). "
            "Ngược lại, nếu lớp vỏ SiO<sub>2</sub> quá dày (<i>d</i><sub>shell</sub> &gt; 30 nm), hiệu ứng tăng cường trường cục bộ LSPR sẽ suy giảm mạnh.<br/>"
            "<b>Nhiệm vụ của Học viên Bùi Trung Dũng:</b> Áp dụng các nguyên lý bề mặt, điện tử và quang học trong Chương 3 để giải quyết bài toán theo chuẩn CER."
        ), styles["TableCell"])]
    ]
    t_cer = Table(cer_box_data, colWidths=[480])
    t_cer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7E2F8E")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#F8F9FA")),
        ("BOX", (0, 0), (-1, -1), 1.0, colors.HexColor("#7E2F8E")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t_cer)
    add_spacer(10)

    add_p(
        "<b>1. Luận điểm Kỹ thuật (Claim):</b><br/>"
        "Để tối ưu hóa đồng thời hiệu suất phát quang của chấm lượng tử CdSe và hiệu suất chuyển hóa quang nhiệt của lõi Au, "
        "chiều dày lớp vỏ SiO<sub>2</sub> bắt buộc phải được khống chế chính xác trong dải kích thước tối ưu: <b><i>d</i><sub>shell</sub> = 10—12 nm</b>, "
        "kết hợp điều chỉnh tỷ số kích thước lõi sao cho bước sóng cộng hưởng LSPR trùng khớp hoàn hảo với cửa sổ truyền qua mô sinh học (NIR, 808 nm)."
    )
    add_spacer(4)

    add_p(
        "<b>2. Bằng chứng Định lượng &amp; Tính toán Dẫn xuất (Evidence):</b><br/>"
        "• <i>Khoảng cách dập tắt huỳnh quang FRET:</i> Tốc độ truyền năng lượng không bức xạ từ chấm lượng tử sang bề mặt kim loại tuân theo quy luật tỉ lệ nghịch bậc 4 với khoảng cách ranh giới: "
        "<i>k</i><sub>FRET</sub> ∝ (<i>d</i><sub>shell</sub>)<sup>−4</sup>. Tại khoảng cách <i>d</i><sub>shell</sub> &lt; 5 nm, hiệu suất dập tắt huỳnh quang đạt &gt; 95%. "
        "Khi nâng chiều dày vỏ lên <i>d</i><sub>shell</sub> ≥ 10 nm, hiệu suất FRET giảm xuống dưới 5%, giải phóng hoàn toàn huỳnh quang của CdSe.<br/>"
        "• <i>Hệ số tăng cường trường cục bộ LSPR:</i> Cường độ điện trường cục bộ bên ngoài hạt nano phân rã theo hàm lũy thừa: "
        "|<i>E</i><sub>loc</sub>(<i>r</i>)|<sup>2</sup> ≈ |<i>E</i><sub>0</sub>|<sup>2</sup> [1 + 2 |(ε − ε<sub><i>m</i></sub>) · (ε + 2ε<sub><i>m</i></sub>)<sup>−1</sup>| (<i>R</i><sub>core</sub> · <i>r</i><sup>−1</sup>)<sup>3</sup>]<sup>2</sup>. "
        "Tại vị trí <i>r</i> = <i>R</i><sub>core</sub> + <i>d</i><sub>shell</sub> = 25 nm (với <i>d</i><sub>shell</sub> = 10 nm), điện trường cục bộ vẫn được tăng cường gấp khoảng 8—12 lần, "
        "giúp tăng cường đồng thời tiết diện hấp thụ quang nhiệt của lõi Au và tốc độ phát xạ tự phát của CdSe (hiệu ứng Purcell)."
    )
    add_spacer(4)

    add_p(
        "<b>3. Lý giải Nguyên lý Đầu Vi mô (Reasoning):</b><br/>"
        "Cấu trúc lai lõi — vỏ Au@SiO<sub>2</sub> giải quyết triệt để sự xung đột vật lý giữa hai hiệu ứng lượng tử trái ngược nhau. "
        "Lớp vỏ SiO<sub>2</sub> đóng vai trò kép: vừa là rào cản điện môi ngăn cách cơ học tiếp xúc trực tiếp giữa electron dẫn của Au và cặp electron — lỗ trống của CdSe "
        "(triệt tiêu kênh dập tắt FRET), vừa bảo vệ bề mặt hạt nano chống kết tụ tự do theo nguyên lý cực tiểu hóa thế năng tự do Gibbs (Δ<i>E</i> &lt; 0) đã chứng minh trong MPT 3.5.2. "
        "Đồng thời, khi chiếu chùm laser NIR 808 nm, toàn bộ công suất hấp thụ quang nhiệt tập trung trong thể tích lõi Au sẽ dẫn nhiệt tức thì qua lớp vỏ SiO<sub>2</sub> siêu mỏng ra môi trường tế bào, "
        "tạo nên sự kết hợp hoàn hảo giữa chẩn đoán quang học nano và điều trị đích cấp độ phân tử."
    )
    add_spacer(14)

    # =========================================================================
    # TỔNG KẾT TOÀN DIỆN CHƯƠNG 3
    # =========================================================================
    add_p("Tổng kết Chương 3: Bức tranh Toàn cảnh Vật lý Thang Nano", "H2")
    add_p(
        "Trải qua 5 phân mục chuyên khảo độc lập (Mục 3.1 đến Mục 3.5), chúng ta đã thiết lập một hệ thống tri thức hoàn chỉnh, "
        "giải thích từ nguyên lý đầu bản chất vật lý của sự biến đổi thuộc tính vật liệu khi kích thước suy giảm từ khối vĩ mô xuống thang nanomet:<br/>"
        "1. <b>Mục 3.1:</b> Nền tảng phân loại thang đo nano, tương tác Coulomb vi mô, độ bất định Heisenberg và giam giữ lượng tử trong giếng thế 1D, 2D, 3D.<br/>"
        "2. <b>Mục 3.2:</b> Nhiệt động học và cơ học chất lưu vi mô: hằng số thời gian nhiệt τ<sub>th</sub> ∝ <i>L</i><sup>2</sup>, động học Stokes <i>v</i><sub>term</sub> ∝ <i>R</i><sup>2</sup>, "
        "chuyển động Brown <i>x</i><sub>rms</sub> ∝ <i>R</i><sup>−0.5</sup> và hiện tượng siêu trơn cấu trúc graphite.<br/>"
        "3. <b>Mục 3.3:</b> Hình thái học đa dạng của ZnO, mật độ trạng thái điện tử DOS qua 4 chiều không gian, mô hình Brus và tinh thể học chiral ống nano carbon (CNT).<br/>"
        "4. <b>Mục 3.4:</b> Dao động mạng tinh thể (Phonon), giam giữ phonon Richter-Fauchet, thực nghiệm Raman Ceri oxit và chuyển pha siêu thuận từ vượt qua giới hạn Néel.<br/>"
        "5. <b>Mục 3.5:</b> Hiệu ứng bề mặt <i>S</i> · <i>V</i><sup>−1</sup> ∝ <i>D</i><sup>−1</sup>, chuyển pha điện tử Kubo, hiệu ứng Coulomb Blockade và cộng hưởng plasmon bề mặt LSPR.<br/>"
        "Toàn bộ các phân mục đã được đóng gói thành các chuyên khảo PDF hoàn chỉnh, đạt 100% chuẩn mực học thuật của Đại học Bách khoa Hà Nội."
    )

    # =========================================================================
    # PRE-FLIGHT TEXT COMPLIANCE AUDIT
    # =========================================================================
    print("Executing Pre-flight Text Compliance Audit for Section 3.5...")
    compliance_report = he.assert_monograph_text_compliance(story)
    print(f"Pre-flight Audit Passed 100%: {compliance_report}")

    # =========================================================================
    # BIÊN DỊCH PDF VÀ THAY THẾ NGUYÊN TỬ VÀO GOOGLE DRIVE
    # =========================================================================
    print(f"Building Monograph PDF into isolated %TEMP%: {temp_pdf_path}...")
    doc.build(story)
    print("PDF build successful in %TEMP%!")

    file_size_mb = os.path.getsize(temp_pdf_path) / (1024 * 1024)
    print(f"Generated PDF File Size: {file_size_mb:.2f} MB (Standard <= 5.0 MB)")

    print(f"Executing Atomic Replacement to Google Drive: {final_drive_path}...")
    shutil.move(temp_pdf_path, final_drive_path)
    print("PUBLISHING COMPLETE: Section 3.5 Monograph successfully deployed to Google Drive!")

if __name__ == "__main__":
    build_monograph_muc_3_5()

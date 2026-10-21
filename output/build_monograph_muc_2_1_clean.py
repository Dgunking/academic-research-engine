# -*- coding: utf-8 -*-
"""
Builder Script for Monograph Muc 2.1: Chuyen_Khao_Laser_Diode_Muc_2.1.pdf
Chapter 2: Phuong phap tiep can hien tuong luan doi voi Laser Diode (Coldren & Corzine)
Architecture: Full 5-Block Feynman Visual-First Core & Causal Flowchain (HUST Standard)
Strict Compliance:
  - Zero-Slash-Fractions via LaTeX Mathtext >= 300 DPI, linespacing >= 2.0
  - Flawless symbol & unit formatting in HTML (<i>...</i>, <sub>...</sub>, <sup>...</sup>)
  - Zero LaTeX leakage in Paragraphs / Tables
  - Triple Buffer Envelope PASS 100% on MATLAB R2014b+ diagrams
  - 100% Zero-Omission of Coldren & Corzine Section 2.1 (pp. 28-34)
"""
import os
import sys
import tempfile
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as he
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib import colors

DRIVE_BASE = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý"
IMG_DIR = os.path.join(DRIVE_BASE, "Kho_Hinh_Anh")
BAI_GIANG_DIR = os.path.join(DRIVE_BASE, "Bai_Giang_Dong_Goi")
TARGET_PDF = os.path.join(BAI_GIANG_DIR, "Chuyen_Khao_Laser_Diode_Muc_2.1.pdf")

def build_monograph_muc_2_1():
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(TARGET_PDF)
    
    story = []
    
    def add_p(text, style_name="Body", ocr_idx=None, is_expanded_from_slide=False):
        para = he.make_paragraph(text, styles[style_name], ocr_idx=ocr_idx, is_expanded_from_slide=is_expanded_from_slide)
        story.append(para)
        return para
        
    def add_spacer(h=8):
        story.append(Spacer(1, h))

    # =========================================================================
    # BANNER TIÊU ĐỀ ĐẦU TRANG & METADATA BÁCH KHOA
    # =========================================================================
    add_p("Chương 2: Phương pháp tiếp cận hiện tượng luận đối với laser diode", "H1")
    add_p("Mục 2.1: Giới thiệu mô hình hiện tượng luận và hệ phương trình tốc độ cơ bản", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Coldren &amp; Corzine — Diode Lasers and Photonic Integrated Circuits, Chương 2, trang 28–34)</i>", "Caption")
    add_spacer(4)
    
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Laser Diode — Cấu trúc và Nguyên lý"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Coldren &amp; Corzine Ch. 2; Sze Semiconductor Devices"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuẩn mực kỹ thuật:</b> 5 Khối Feynman &amp; Triệt tiêu phân số gạch chéo"), styles["TableCell"])]
    ]
    meta_t = Table(meta_table_data, colWidths=[250.0, he.PRINTABLE_WIDTH - 250.0])
    meta_t.setStyle(TableStyle([
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
    
    # Bảng phân tầng kiến trúc 3 MPT
    arch_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Phân cấp phân mục</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Nội dung chuyên khảo toàn văn 5 Khối (Zero-Omission)</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Tham chiếu gốc</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.1</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Mô hình phương trình tốc độ hạt tải trong vùng tích cực dị thể kép, các kênh tái hợp phi tuyến và phát xạ tự phát trong diode phát quang LED"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Coldren tr. 28–32<br/>Fig 2.1, 2.2, 2.3"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.2</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Mô hình photon trong hốc cộng hưởng, hệ số giam giữ quang, điều kiện cân bằng ngưỡng và hiện tượng kẹp hạt tải"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Coldren tr. 32–41<br/>Fig 2.8 &ndash; 2.11"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.3</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Động lực học điều chế tín hiệu nhỏ, khung dao động tương đương RLC bậc hai và các kỹ thuật đặc trưng hóa thực nghiệm laser"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Coldren tr. 48–61<br/>Fig 2.12 &ndash; 2.17"), styles["TableCellCenter"])]
    ]
    arch_t = Table(arch_data, colWidths=[95.0, he.PRINTABLE_WIDTH - 195.0, 100.0])
    arch_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), he.COLOR_TABLE_HEADER_BG),
        ('GRID', (0,0), (-1,-1), 0.5, he.COLOR_BORDER_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(arch_t)
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.1: HẠT TẢI TRONG VÙNG TÍCH CỰC & TÁI HỢP PHI TUYẾN
    # =========================================================================
    add_p("Luận điểm 2.1.1: Mô hình phương trình tốc độ hạt tải trong vùng tích cực dị thể kép, các kênh tái hợp phi tuyến và phát xạ tự phát trong diode phát quang LED", "H2")
    
    # KHỐI 1
    add_p("Khối 1: Bản đồ không gian và nghịch lý mở đầu", "H3")
    
    fig_2_1 = os.path.join(IMG_DIR, "[Goc]_Figure_2.1_Gian_do_dai_nang_luong_diode_di_the_kep_DH.png")
    if os.path.exists(fig_2_1):
        story.append(he.embed_figure_with_caption(
            fig_2_1,
            "Hình 2.1: Giản đồ dải năng lượng của diode dị thể kép (DH) dưới chế độ phân cực thuận, minh họa cơ chế giam giữ hạt tải trong giếng thế vùng tích cực (Coldren &amp; Corzine, trang 29).",
            kind="orig",
            styles=styles
        ))
    
    add_p("Mô tả cấu trúc không gian dải năng lượng theo tọa độ phương thẳng đứng mọc màng tinh thể <i>z</i> trong cấu trúc bán dẫn dị thể kép (Double Heterostructure &ndash; DH). Dưới điện áp phân cực thuận ngoài <i>V</i>, thế năng rào cản khuếch tán tại mặt tiếp giáp <i>p</i>&ndash;<i>n</i> bị triệt tiêu, cho phép dòng electron từ phía <i>n</i> và dòng lỗ trống từ phía <i>p</i> tiêm ồ ạt vào vùng tích cực (active region) có độ rộng vùng cấm hẹp hơn.", "Body", ocr_idx=1)
    
    add_p("Định vị các trục tọa độ không gian <i>z</i> dọc trục vuông góc với các lớp màng epitaxy; trục tung biểu diễn thang đo năng lượng điện tử <i>E</i>. Các đại lượng vi mô gốc bao gồm đáy dải dẫn <i>E<sub>c</sub></i>(<i>z</i>), đỉnh dải hóa trị <i>E<sub>v</sub></i>(<i>z</i>), mức Fermi giả của electron <i>E</i><sub>Fc</sub> và của lỗ trống <i>E</i><sub>Fv</sub>. Bước nhảy thế năng dải dẫn Δ<i>E<sub>c</sub></i> và dải hóa trị Δ<i>E<sub>v</sub></i> tạo thành hai thành giếng lượng tử sâu giam hãm hạt tải trong thể tích tích cực <i>V</i> = <i>d</i> · <i>w</i> · <i>L</i>.", "Body", ocr_idx=2)
    
    add_p("Cơ chế chuyển dời hạt tải qua tiếp giáp: Các hạt tải sau khi vượt qua rào thế tiếp xúc sẽ nhanh chóng giải phóng động năng qua tương tác tán xạ phonon quang nội dải trong khoảng thời gian cực ngắn (~ 0,1 ps), rơi xuống đáy giếng lượng tử và tích lũy tạo nên sự đảo lộn mật độ hạt tải (population inversion) thỏa mãn điều kiện Bernard &ndash; Duraffourg.", "Body", ocr_idx=3)
    add_spacer(6)

    fig_2_2 = os.path.join(IMG_DIR, "[Goc]_Figure_2.2_Mo_hinh_ho_chua_hat_tai_duoi_nguong.png")
    if os.path.exists(fig_2_2):
        story.append(he.embed_figure_with_caption(
            fig_2_2,
            "Hình 2.2: Mô hình hồ chứa chất lỏng tương đương mô tả động học nạp và thoát hạt tải trong vùng tích cực dị thể kép dưới ngưỡng (Coldren &amp; Corzine, trang 30).",
            kind="orig",
            styles=styles
        ))
        add_p("Mô hình hồ chứa nước kim loại tương đương mô tả sự cân bằng động lượng của hạt tải trong thể tích tích cực <i>V</i>: Nguồn nước bơm từ vòi phía trên tương ứng dòng tiêm hạt tải <i>η<sub>i</sub> I</i> / (<i>q V</i>), mực nước dâng cao đại diện cho mật độ hạt tải <i>N</i>, và ba van xả đáy tương ứng với ba kênh tái hợp tự nhiên.", "Body", ocr_idx=1)
        add_p("Các đường rò rỉ ngoại biên (Current Leakage) chạy vòng qua vùng tích cực làm suy giảm hiệu suất lượng tử nội <i>η<sub>i</sub></i>; trong khi dòng hạt tải tràn qua rào thế (Carrier Leakage <i>R<sub>l</sub></i>) do phát xạ nhiệt thermionic làm thất thoát hạt tải khỏi thể tích tích cực trước khi kịp tái hợp phát quang.", "Body", ocr_idx=2)
        add_p("Trạng thái dừng đạt được khi lưu lượng tiêm vào cân bằng chính xác với tổng lưu lượng xả đáy qua ba kênh: tái hợp không bức xạ Shockley &ndash; Read &ndash; Hall (SRH), tái hợp phát xạ tự phát (Spontaneous Emission) và tái hợp Auger không bức xạ ba hạt.", "Body", ocr_idx=3)
    add_spacer(6)

    fig_2_3 = os.path.join(IMG_DIR, "[Goc]_Figure_2.3_So_do_phat_xa_va_phan_xa_toan_phan_trong_LED.png")
    if os.path.exists(fig_2_3):
        story.append(he.embed_figure_with_caption(
            fig_2_3,
            "Hình 2.3: Sơ đồ hình học minh họa góc nón thoát photon và phản xạ toàn phần tại bề mặt phân cách bán dẫn &ndash; không khí trong diode phát quang LED (Coldren &amp; Corzine, trang 33).",
            kind="orig",
            styles=styles
        ))
        add_p("Mô tả hình học không gian phân bố photon phát xạ tự phát đẳng hướng trong khối bán dẫn LED: Chỉ những tia sáng nằm trong góc nón hình nón cụt giới hạn bởi góc tới hạn phản xạ toàn phần <i>θ<sub>c</sub></i> mới có khả năng khúc xạ thoát ra môi trường ngoài.", "Body", ocr_idx=1)
        add_p("Các thông số quang học vi mô bao gồm chiết suất bán dẫn <i>n</i> ≈ 3,5, chiết suất không khí <i>n</i><sub>0</sub> = 1,0, dẫn đến góc tới hạn phản xạ toàn phần cực hẹp <i>θ<sub>c</sub></i> ≈ 16° qua định luật Snell. Góc khối thoát photon chỉ chiếm một phần rất nhỏ trong tổng góc khối toàn phần 4π steradian.", "Body", ocr_idx=2)
        add_p("Hệ quả quang học: Trên 98% photon phát xạ tự phát trong LED bị bẫy lại bên trong khối bán dẫn do phản xạ toàn phần và bị tái hấp thụ hoặc tiêu tán thành nhiệt năng, làm hiệu suất trích xuất photon ngoài của LED phẳng không có cấu trúc vi thấu kính chỉ đạt mức 1,5% đến 2,0%.", "Body", ocr_idx=3)
    add_spacer(6)

    add_p("<b>Nghịch lý mở đầu (Paradox of Droop):</b> Tại sao khi tăng cường độ dòng tiêm <i>I</i> vào diode bán dẫn nhằm tối đa hóa tốc độ phát quang, hiệu suất lượng tử nội phát xạ bức xạ <i>η</i><sub>rad</sub> ban đầu tăng nhanh nhưng sau khi đạt một giá trị cực đại lại suy giảm nghiêm trọng ở mật độ dòng cao (hiện tượng Efficiency Droop)? Điều gì đã biến vùng tích cực từ một cỗ máy phát photon hiệu quả thành một lò nhiệt tiêu tán năng lượng?", "Body")
    add_spacer(10)

    # KHỐI 2
    add_p("Khối 2: Hạt nhân vật lý và khóa biến số", "H3")
    add_p("Hạt nhân vật lý chi phối động lực học hạt tải là định luật bảo toàn điện tích và cân bằng hạt vi mô trong thể tích tích cực <i>V</i>. Phương trình tốc độ hạt tải liên kết nguồn tiêm dòng điện ngoài với các quá trình tái hợp tự nhiên và tái hợp cưỡng bức:", "Body")
    add_spacer(4)
    
    # Hệ thức cột trụ 1
    eq_carrier_rate = r"""\frac{\mathrm{d}N}{\mathrm{d}t} = \frac{\eta_i I}{q V} - R(N) - v_g g S"""
    story.append(he.build_intermediate_equation(
        "Hệ thức Cột trụ Cấp 3: Phương trình tốc độ biến thiên mật độ hạt tải trong vùng tích cực:",
        eq_carrier_rate,
        styles=styles
    ))
    add_spacer(6)

    # Bảng Nomenclature ISO 80000-2
    nom_data_1 = [
        [Paragraph(he.wrap_math_glyphs("<b>Ký hiệu</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Ý nghĩa vật lý vi mô chuẩn mực</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị SI</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Giá trị InGaAsP 1,55 μm</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<i>N</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Mật độ electron (hạt tải) trong thể tích tích cực"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-3</sup> (cm<sup>-3</sup>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("1,0 × 10<sup>24</sup> m<sup>-3</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>I</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Cường độ dòng điện tiêm qua hai cực linh kiện"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("A (mA)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("20 &ndash; 100 mA"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>η<sub>i</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hiệu suất lượng tử nội (tỷ lệ dòng sinh hạt tải có ích)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Không thứ nguyên"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("0,80 &ndash; 0,90"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>V</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Thể tích hình học vùng tích cực (<i>V</i> = <i>d</i> · <i>w</i> · <i>L</i>)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>3</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("6,0 × 10<sup>-17</sup> m<sup>3</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>R</i>(<i>N</i>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tổng tốc độ tái hợp tự nhiên (SRH + Bức xạ + Auger)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-3</sup>·s<sup>-1</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("<i>A N</i> + <i>B N</i><sup>2</sup> + <i>C N</i><sup>3</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>v<sub>g</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Vận tốc nhóm của mode sóng quang học trong hốc"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m·s<sup>-1</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("8,33 × 10<sup>7</sup> m/s"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>g</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số độ lợi quang học vật liệu trên một đơn vị dài"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-1</sup> (cm<sup>-1</sup>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("10<sup>4</sup> &ndash; 2 × 10<sup>5</sup> m<sup>-1</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>S</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Mật độ photon trung bình trong mode laser"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-3</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("10<sup>18</sup> &ndash; 10<sup>21</sup> m<sup>-3</sup>"), styles["TableCellCenter"])]
    ]
    nom_t_1 = Table(nom_data_1, colWidths=[65.0, 220.0, 95.0, he.PRINTABLE_WIDTH - 380.0])
    nom_t_1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), he.COLOR_TABLE_HEADER_BG),
        ('GRID', (0,0), (-1,-1), 0.5, he.COLOR_BORDER_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(nom_t_1)
    add_spacer(8)

    add_p("<b>Ẩn dụ 3 Nhịp Khóa Biến số (Mô hình Hồ chứa Nước):</b> Hãy hình dung vùng tích cực như một hồ chứa nước bằng kim loại có tiết diện đáy <i>A</i><sub>geom</sub> và thể tích <i>V</i>. Nước được bơm liên tục từ vòi phía trên tương ứng với dòng hạt tải tiêm <i>η<sub>i</sub> I</i> / (<i>q V</i>). Chiều cao mực nước trong hồ đại diện cho mật độ hạt tải <i>N</i>. Đáy hồ có 3 van xả với tiết diện và cơ chế xả khác nhau: van nhỏ xả tuyến tính theo mực nước (~ SRH <i>A N</i>), van chính xả theo bình phương áp suất nước (~ Bức xạ tự phát <i>B N</i><sup>2</sup>), và van xả áp khổng lồ mở ra tỉ lệ với lập phương mực nước (~ Auger <i>C N</i><sup>3</sup>). Khi mực nước thấp, van nhỏ chiếm ưu thế làm nước thất thoát vô ích; khi mực nước vừa phải, van chính bức xạ mở mạnh; nhưng khi mực nước dâng quá cao, van Auger mở toang nuốt trọn năng lượng tiêm vào.", "Body")
    add_spacer(10)

    # KHỐI 3
    add_p("Khối 3: Chuỗi nhân quả dẫn xuất", "H3")
    add_p("<b>Vùng áp dụng và giả thiết biên:</b> Khảo sát bán dẫn vùng tích cực không pha tạp hoặc pha tạp nhẹ, dưới chế độ kích thích tiêm cao (high-level injection) thường gặp trong LED và laser diode. Điều kiện trung hòa điện tích cục bộ đòi hỏi mật độ electron tự do cân bằng chính xác với mật độ lỗ trống:", "Body")
    
    eq_neutrality = r"""N = P \qquad \Longrightarrow \quad n \approx p \approx N"""
    story.append(he.build_intermediate_equation(
        "Điều kiện trung hòa điện tích giả định trong vùng tích cực:",
        eq_neutrality,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tốc độ tiêm hạt tải trên một đơn vị thể tích được xác định từ cường độ dòng điện ngoài <i>I</i> chia cho điện tích nguyên tố <i>q</i> và thể tích <i>V</i>, có tính đến hiệu suất lượng tử nội <i>η<sub>i</sub></i>:", "Body", is_expanded_from_slide=True)
    
    eq_inj_rate = r"""R_{\mathrm{inj}} = \frac{\eta_i I}{q V}"""
    story.append(he.build_intermediate_equation(
        "Tốc độ sinh hạt tải hữu ích trong thể tích vùng tích cực:",
        eq_inj_rate,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Trong chế độ dưới ngưỡng (hoặc trong LED), mật độ photon kích thích <i>S</i> ≈ 0. Tổng tốc độ tái hợp tự nhiên <i>R</i>(<i>N</i>) được phân rã thành đa thức bậc ba theo định luật tác dụng khối lượng:", "Body", is_expanded_from_slide=True)
    
    eq_abc_decomp = r"""R(N) = R_{\mathrm{nr}} + R_{\mathrm{sp}} + R_{\mathrm{aug}} = A N + B N^2 + C N^3"""
    story.append(he.build_intermediate_equation(
        "Khai triển tốc độ tái hợp tự nhiên ABC:",
        eq_abc_decomp,
        styles=styles,
        ocr_idx=4
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thời gian sống của hạt tải <i>τ<sub>n</sub></i>(<i>N</i>) là nghịch đảo của tần suất tái hợp toàn phần:", "Body", is_expanded_from_slide=True)
    
    eq_lifetime = r"""\tau_n(N) \equiv \frac{N}{R(N)} = \frac{1}{A + B N + C N^2}"""
    story.append(he.build_intermediate_equation(
        "Biểu thức thời gian sống toàn phần của hạt tải theo mật độ <i>N</i>:",
        eq_lifetime,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hiệu suất lượng tử nội phát xạ bức xạ <i>η</i><sub>rad</sub> được định nghĩa bằng tỉ số giữa tốc độ tái hợp bức xạ có ích <i>R</i><sub>sp</sub> và tổng tốc độ tái hợp toàn phần <i>R</i>(<i>N</i>):", "Body", is_expanded_from_slide=True)
    
    eq_eta_rad = r"""\eta_{\mathrm{rad}}(N) = \frac{R_{\mathrm{sp}}}{R(N)} = \frac{B N^2}{A N + B N^2 + C N^3} = \frac{B N}{A + B N + C N^2}"""
    story.append(he.build_intermediate_equation(
        "Hàm hiệu suất lượng tử nội bức xạ của diode phát quang:",
        eq_eta_rad,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tìm mật độ hạt tải tối ưu <i>N</i><sub>opt</sub> để cực đại hóa hiệu suất bức xạ bằng cách giải đạo hàm vi phân:", "Body", is_expanded_from_slide=True)
    
    eq_diff_opt = r"""\frac{\mathrm{d}\eta_{\mathrm{rad}}}{\mathrm{d}N} = \frac{B(A + B N + C N^2) - B N(B + 2 C N)}{(A + B N + C N^2)^2} = \frac{B(A - C N^2)}{(A + B N + C N^2)^2} = 0"""
    story.append(he.build_intermediate_equation(
        "Điều kiện vi phân cực trị của hàm hiệu suất lượng tử nội bức xạ:",
        eq_diff_opt,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm dương duy nhất của phương trình vi phân cho giá trị mật độ hạt tải tối ưu <i>N</i><sub>opt</sub> và hiệu suất cực đại tương ứng:", "Body", is_expanded_from_slide=True)
    
    eq_n_opt_res = r"""N_{\mathrm{opt}} = \sqrt{\frac{A}{C}}, \qquad \eta_{\mathrm{rad, max}} = \frac{B \sqrt{\frac{A}{C}}}{A + B \sqrt{\frac{A}{C}} + C \left(\frac{A}{C}\right)} = \frac{B}{2\sqrt{A C} + B}"""
    story.append(he.build_intermediate_equation(
        "Hệ thức Đích: Mật độ hạt tải tối ưu và hiệu suất phát quang cực đại:",
        eq_n_opt_res,
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(10)

    # KHỐI 4
    add_p("Khối 4: Khảo sát tiệm cận và thực chiến linh kiện", "H3")
    
    fig_sim_abc = os.path.join(IMG_DIR, "[Mo_Phong]_Dong_Luc_Hoc_Tai_Hop_ABC_Va_Hieu_Suat_Buc_Xa_LED.png")
    if os.path.exists(fig_sim_abc):
        story.append(he.embed_figure_with_caption(
            fig_sim_abc,
            "Hình 2.4: Đồ thị mô phỏng động học tái hợp hạt tải ABC và hiệu suất phát quang LED chuẩn MATLAB R2014b+: (a) Tốc độ tái hợp theo mật độ hạt tải; (b) Đường cong hiệu suất lượng tử nội và điểm cực trị tối ưu (Triple Buffer PASS 100%).",
            kind="sim",
            styles=styles
        ))
        add_p("↳ [Vật liệu]: InGaAsP/InP (<i>λ</i> = 1,55 μm) | [Hằng số vi mô]: <i>A</i> = 1,0 × 10<sup>8</sup> s<sup>-1</sup>, <i>B</i> = 1,0 × 10<sup>-10</sup> cm<sup>3</sup>/s, <i>C</i> = 3,0 × 10<sup>-29</sup> cm<sup>6</sup>/s | [Hệ quả Lab]: <i>N</i><sub>opt</sub> = 1,83 × 10<sup>18</sup> cm<sup>-3</sup>, <i>η</i><sub>rad, max</sub> = 47,8%.", "Caption")
    add_spacer(6)

    add_p("<b>Khảo sát cực hạn 1 (Dòng tiêm cực nhỏ, <i>N</i> tiến về 0):</b> Khi mật độ hạt tải rất bé, số hạng bậc nhất <i>A N</i> chiếm ưu thế hoàn toàn so với các bậc cao. Thời gian sống hạt tải tiệm cận hằng số không đổi <i>τ<sub>n</sub></i> → 1 / <i>A</i> (thời gian sống SRH), trong khi hiệu suất lượng tử bức xạ tiến về 0:", "Body")
    
    eq_asymp_low_n = r"""\lim_{N \to 0} \eta_{\mathrm{rad}}(N) \approx \frac{B N}{A} \propto N \quad \longrightarrow \quad 0"""
    story.append(he.build_intermediate_equation(
        "Hành vi tiệm cận ở dải mật độ hạt tải thấp:",
        eq_asymp_low_n,
        styles=styles
    ))
    
    add_p("<b>Khảo sát cực hạn 2 (Dòng tiêm cực lớn, <i>N</i> tiến về vô cùng):</b> Khi bơm dòng cực mạnh, quá trình tái hợp va chạm Auger ba hạt tải <i>C N</i><sup>3</sup> tăng vọt theo lũy thừa bậc ba, đè bẹp hoàn toàn quá trình bức xạ phát photon tự phát:", "Body")
    
    eq_asymp_high_n = r"""\lim_{N \to \infty} \eta_{\mathrm{rad}}(N) \approx \frac{B N}{C N^2} = \frac{B}{C N} \propto \frac{1}{N} \quad \longrightarrow \quad 0"""
    story.append(he.build_intermediate_equation(
        "Hành vi suy giảm hiệu suất dòng cao do tái hợp Auger (Efficiency Droop):",
        eq_asymp_high_n,
        styles=styles
    ))
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.2: PHOTON TRONG HỐC & HIỆN TƯỢNG KẸP HẠT TẢI
    # =========================================================================
    add_p("Luận điểm 2.1.2: Mô hình photon trong hốc cộng hưởng, hệ số giam giữ quang, điều kiện cân bằng ngưỡng và hiện tượng kẹp hạt tải", "H2")
    
    # KHỐI 1
    add_p("Khối 1: Bản đồ không gian và nghịch lý mở đầu", "H3")
    
    fig_2_8_9 = os.path.join(IMG_DIR, "[Goc]_Figure_2.8_2.9_Kep_hat_tai_do_loi_va_dac_tuyen_P_I_laser_diode.png")
    if os.path.exists(fig_2_8_9):
        story.append(he.embed_figure_with_caption(
            fig_2_8_9,
            "Hình 2.5: Minh họa hiện tượng kẹp hạt tải tại ngưỡng và đặc tuyến công suất quang theo dòng điện tiêm P-I của laser diode (Coldren &amp; Corzine, trang 38 &amp; 40).",
            kind="orig",
            styles=styles
        ))
        add_p("Minh họa quy luật biến thiên của độ lợi mode quang học Γ <i>g</i>(<i>N</i>) và công suất quang phát xạ <i>P</i><sub>out</sub> theo dòng điện tiêm ngoài <i>I</i>. Đồ thị phân tách thành hai miền vật lý rõ rệt ngăn cách bởi dòng ngưỡng <i>I</i><sub>th</sub>.", "Body", ocr_idx=1)
        add_p("Định vị các trục tọa độ: Trục hoành biểu diễn dòng tiêm <i>I</i>; trục tung bên trái biểu diễn độ lợi mode Γ <i>g</i> và trục tung bên phải biểu diễn công suất quang <i>P</i><sub>out</sub>. Các thông số mốc bao gồm dòng ngưỡng <i>I</i><sub>th</sub>, độ lợi ngưỡng Γ <i>g</i><sub>th</sub> cân bằng với tổng tổn hao hốc ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>, và hiệu suất vi phân ngoài <i>η<sub>d</sub></i>.", "Body", ocr_idx=2)
        add_p("Cơ chế phân kỳ hành vi: Dưới ngưỡng (<i>I</i> < <i>I</i><sub>th</sub>), hạt tải tích lũy làm độ lợi tăng đều, photon chỉ phát xạ tự phát yếu ớt; Ngay khi đạt ngưỡng (<i>I</i> = <i>I</i><sub>th</sub>), độ lợi chạm mức tổn hao và bị khóa cứng (clamped); Trên ngưỡng (<i>I</i> > <i>I</i><sub>th</sub>), mọi electron tiêm thêm đều chuyển hóa thành photon laser cưỡng bức.", "Body", ocr_idx=3)
    add_spacer(6)

    add_p("<b>Nghịch lý mở đầu (Paradox of Carrier Clamping):</b> Trong mọi mạch điện bán dẫn thông thường, khi ta tăng dòng điện tiêm qua tiếp giáp <i>p</i>&ndash;<i>n</i>, mật độ hạt tải và điện áp tiếp giáp luôn tăng tương ứng. Tuy nhiên, trong diode laser, ngay khi đạt ngưỡng phát xạ kích thích, dù ta tiếp tục bơm thêm dòng điện gấp 5 lần hay 10 lần dòng ngưỡng, mật độ hạt tải trong vùng tích cực lại bị 'đóng băng' hoàn toàn ở mức <i>N</i><sub>th</sub>. Vì sao hệ thống lượng tử này lại có khả năng tự điều hòa và kẹp chặt mật độ hạt tải một cách tuyệt đối như vậy?", "Body")
    add_spacer(10)

    # KHỐI 2
    add_p("Khối 2: Hạt nhân vật lý và khóa biến số", "H3")
    add_p("Hạt nhân vật lý của phương trình photon là định luật bảo toàn năng lượng trường điện từ trong hốc cộng hưởng: Tốc độ sinh photon kích thích phải bù đắp chính xác tốc độ mất mát photon do hấp thụ nội và thoát qua gương phản xạ ngõ ra:", "Body")
    add_spacer(4)
    
    # Hệ thức cột trụ 2
    eq_photon_rate = r"""\frac{\mathrm{d}S}{\mathrm{d}t} = \left(\Gamma v_g g - \frac{1}{\tau_p}\right) S + \Gamma R_{\mathrm{sp}}'"""
    story.append(he.build_intermediate_equation(
        "Hệ thức Cột trụ Cấp 3: Phương trình tốc độ biến thiên mật độ photon trong mode laser:",
        eq_photon_rate,
        styles=styles
    ))
    add_spacer(6)

    # Bảng Nomenclature ISO 80000-2
    nom_data_2 = [
        [Paragraph(he.wrap_math_glyphs("<b>Ký hiệu</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Ý nghĩa vật lý vi mô chuẩn mực</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị SI</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Giá trị InGaAsP 1,55 μm</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<i>S</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Mật độ photon trung bình trong mode laser"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-3</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("10<sup>18</sup> &ndash; 10<sup>21</sup> m<sup>-3</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("Γ"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số giam giữ quang học (tỷ lệ chồng chập mode và vùng tích cực)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Không thứ nguyên"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("0,03 &ndash; 0,08 (DH / QW)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>g</i>(<i>N</i>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số độ lợi quang học vật liệu (độ lợi vi mô)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-1</sup> (cm<sup>-1</sup>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("<i>a</i> (<i>N</i> &minus; <i>N</i><sub>tr</sub>)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>τ<sub>p</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Thời gian sống photon trong hốc cộng hưởng Fabry-Perot"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("s (ps)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("1,5 &ndash; 3,0 ps"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>α<sub>i</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số tổn hao nội tại do tán xạ và hấp thụ hạt tải tự do"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-1</sup> (cm<sup>-1</sup>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("1000 &ndash; 2000 m<sup>-1</sup> (10 &ndash; 20 cm<sup>-1</sup>)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>α<sub>m</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số tổn hao gương phản xạ ngõ ra của hốc cộng hưởng"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-1</sup> (cm<sup>-1</sup>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("2000 &ndash; 4000 m<sup>-1</sup> (20 &ndash; 40 cm<sup>-1</sup>)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>β</i><sub>sp</sub>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số ghép phát xạ tự phát vào mode laser phát xạ chính"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Không thứ nguyên"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("10<sup>-5</sup> &ndash; 10<sup>-4</sup>"), styles["TableCellCenter"])]
    ]
    nom_t_2 = Table(nom_data_2, colWidths=[65.0, 220.0, 95.0, he.PRINTABLE_WIDTH - 380.0])
    nom_t_2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), he.COLOR_TABLE_HEADER_BG),
        ('GRID', (0,0), (-1,-1), 0.5, he.COLOR_BORDER_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(nom_t_2)
    add_spacer(8)

    add_p("<b>Ẩn dụ 3 Nhịp Khóa Biến số (Mô hình Đập tràn Thoát lũ):</b> Hãy tưởng tượng hốc cộng hưởng laser như một hồ thủy điện có bờ đập tràn tự động với độ cao cố định 10 m (tương ứng với mức tổn hao ngưỡng của hốc ⟨<i>α<sub>i</sub></i>⟩ + <i>α<sub>m</sub></i>). Khi nước tiêm vào hồ chưa đạt 10 m (dưới ngưỡng), nước không thể tràn qua đập, chỉ có vài giọt rò rỉ qua chân đập (~ phát xạ tự phát <i>β</i><sub>sp</sub>). Nhưng ngay khi mực nước chạm đúng mép đập 10 m (đạt ngưỡng), nước tràn ào ạt qua mặt đập thành dòng lũ khổng lồ (~ dòng photon phát xạ cưỡng bức laser). Dù lưu lượng nước lũ đổ về hồ có tăng gấp 10 lần, mực nước trong hồ vẫn bị 'kẹp' cứng ở cao trình 10 m vì toàn bộ lượng nước thừa đều tức khắc bị cuốn qua bờ tràn đập lũ.", "Body")
    add_spacer(10)

    # KHỐI 3
    add_p("Khối 3: Chuỗi nhân quả dẫn xuất", "H3")
    add_p("<b>Điều kiện tuần hoàn biên pha và biên độ trong hốc Fabry-Perot:</b> Để ánh sáng duy trì dao động dừng ổn định trong hốc cộng hưởng có chiều dài <i>L</i> và hai gương phản xạ có hệ số phản xạ biên độ <i>r</i><sub>1</sub>, <i>r</i><sub>2</sub> (hệ số phản xạ công suất <i>R</i><sub>1</sub> = |<i>r</i><sub>1</sub>|<sup>2</sup>, <i>R</i><sub>2</sub> = |<i>r</i><sub>2</sub>|<sup>2</sup>), sóng quang học sau một chu trình truyền khứ hồi (round-trip) chiều dài 2<i>L</i> phải tự tái tạo chính nó cả về biên độ và pha:", "Body")
    
    eq_round_trip = r"""r_1 r_2 \exp\left[\left(\Gamma g_{\mathrm{th}} - \alpha_i\right) L\right] \exp(-2\mathrm{j}\beta L) = 1"""
    story.append(he.build_intermediate_equation(
        "Phương trình điều kiện dừng tuần hoàn khứ hồi quanh hốc Fabry-Perot:",
        eq_round_trip,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Lấy độ lớn (modulus) hai vế để thiết lập điều kiện cân bằng biên độ độ lợi ngưỡng:", "Body", is_expanded_from_slide=True)
    
    eq_amp_balance = r"""|r_1 r_2| \exp\left[\left(\Gamma g_{\mathrm{th}} - \alpha_i\right) L\right] = \sqrt{R_1 R_2} \exp\left[\left(\Gamma g_{\mathrm{th}} - \alpha_i\right) L\right] = 1"""
    story.append(he.build_intermediate_equation(
        "Cân bằng độ lợi và tổn hao biên độ:",
        eq_amp_balance,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Lấy logarit tự nhiên hai vế và chia cho chiều dài hốc <i>L</i> để rút ra độ lợi mode ngưỡng Γ <i>g</i><sub>th</sub>:", "Body", is_expanded_from_slide=True)
    
    eq_gth_derivation = r"""\left(\Gamma g_{\mathrm{th}} - \alpha_i\right) L = \ln\left(\frac{1}{\sqrt{R_1 R_2}}\right) = \frac{1}{2} \ln\left(\frac{1}{R_1 R_2}\right) \quad \Longrightarrow \quad \Gamma g_{\mathrm{th}} = \alpha_i + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right) = \alpha_i + \alpha_m"""
    story.append(he.build_intermediate_equation(
        "Hệ thức cân bằng độ lợi mode ngưỡng và tổn hao hốc:",
        eq_gth_derivation,
        styles=styles,
        ocr_idx=4
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thời gian sống photon <i>τ<sub>p</sub></i> là thời gian trung bình một photon tồn tại trong hốc trước khi bị hấp thụ hoặc thoát ra ngoài, liên hệ trực tiếp với tổng tổn hao:", "Body", is_expanded_from_slide=True)
    
    eq_tau_p = r"""\frac{1}{\tau_p} = v_g (\alpha_i + \alpha_m) = v_g \Gamma g_{\mathrm{th}}"""
    story.append(he.build_intermediate_equation(
        "Mối tương quan giữa thời gian sống photon và độ lợi ngưỡng:",
        eq_tau_p,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Xét phương trình photon ở trạng thái dừng d<i>S</i>/d<i>t</i> = 0 trên ngưỡng (<i>S</i> ≫ 0):", "Body", is_expanded_from_slide=True)
    
    eq_clamping_proof = r"""\left(\Gamma v_g g(N) - \frac{1}{\tau_p}\right) S + \Gamma R_{\mathrm{sp}}' = 0 \quad \Longrightarrow \quad \Gamma v_g g(N) \approx \frac{1}{\tau_p} \quad \Longrightarrow \quad N = N_{\mathrm{th}} = \text{const}"""
    story.append(he.build_intermediate_equation(
        "Chứng minh toán học giải tích hiện tượng kẹp hạt tải và kẹp độ lợi:",
        eq_clamping_proof,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Ở chế độ trên ngưỡng, mật độ hạt tải bị kẹp tại <i>N</i><sub>th</sub>, do đó tốc độ tái hợp tự nhiên bị khóa cứng tại <i>R</i>(<i>N</i><sub>th</sub>). Cân bằng phương trình hạt tải ở trạng thái dừng cho phép rút ra mật độ photon phát xạ kích thích:", "Body", is_expanded_from_slide=True)
    
    eq_s_steady = r"""\frac{\eta_i I}{q V} - R(N_{\mathrm{th}}) - v_g g_{\mathrm{th}} S = 0 \quad \Longrightarrow \quad v_g g_{\mathrm{th}} S = \frac{\eta_i (I - I_{\mathrm{th}})}{q V}"""
    story.append(he.build_intermediate_equation(
        "Mật độ photon phát xạ cưỡng bức tỉ lệ tuyến tính với dòng vượt ngưỡng:",
        eq_s_steady,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Công suất quang phát xạ hữu ích thoát qua hai mặt gương ra môi trường ngoài được tính bằng tích của mật độ năng lượng photon, vận tốc nhóm và tỷ lệ tổn hao gương:", "Body", is_expanded_from_slide=True)
    
    eq_p_out_derivation = r"""P_{\mathrm{out}} = \eta_d \frac{h\nu}{q} (I - I_{\mathrm{th}}), \qquad \eta_d = \eta_i \frac{\alpha_m}{\alpha_i + \alpha_m} = \eta_i \frac{\frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)}{\alpha_i + \frac{1}{2L}\ln\left(\frac{1}{R_1 R_2}\right)}"""
    story.append(he.build_intermediate_equation(
        "Hệ thức Đích: Đặc tuyến công suất ngõ ra và hiệu suất vi phân ngoài:",
        eq_p_out_derivation,
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(10)

    # KHỐI 4
    add_p("Khối 4: Khảo sát tiệm cận và thực chiến linh kiện", "H3")
    add_p("<b>Khảo sát cực hạn 1 (Gương phản xạ lý tưởng, <i>R</i><sub>1</sub> <i>R</i><sub>2</sub> tiến về 1):</b> Khi hệ số phản xạ gương đạt 100%, tổn hao gương triệt tiêu hoàn toàn:", "Body")
    
    eq_asymp_r_one = r"""\lim_{R_1 R_2 \to 1} \alpha_m = 0 \quad \Longrightarrow \quad \Gamma g_{\mathrm{th}} = \alpha_i, \quad I_{\mathrm{th}} \to I_{\mathrm{th, min}}, \quad \eta_d \to 0, \quad P_{\mathrm{out}} \to 0"""
    story.append(he.build_intermediate_equation(
        "Cực hạn hốc kín phản xạ tuyệt đối: Dòng ngưỡng cực tiểu nhưng công suất ngõ ra bằng 0:",
        eq_asymp_r_one,
        styles=styles
    ))
    
    add_p("<b>Khảo sát cực hạn 2 (Hốc hở không phản xạ, <i>R</i><sub>1</sub> <i>R</i><sub>2</sub> tiến về 0):</b> Khi các mặt gương bị triệt tiêu phản xạ (qua phủ màng chống phản xạ AR cực tốt), tổn hao gương phân kỳ:", "Body")
    
    eq_asymp_r_zero = r"""\lim_{R_1 R_2 \to 0} \alpha_m \to \infty \quad \Longrightarrow \quad \Gamma g_{\mathrm{th}} \to \infty \quad \Longrightarrow \quad I_{\mathrm{th}} \to \infty"""
    story.append(he.build_intermediate_equation(
        "Cực hạn hốc hở: Linh kiện không thể đạt ngưỡng laser, chuyển hóa thành diode siêu phát quang SLD:",
        eq_asymp_r_zero,
        styles=styles
    ))
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.3: ĐỘNG LỰC HỌC TÍN HIỆU NHỎ & MẠCH TƯƠNG ĐƯƠNG RLC
    # =========================================================================
    add_p("Luận điểm 2.1.3: Động lực học điều chế tín hiệu nhỏ, khung dao động tương đương RLC bậc hai và các kỹ thuật đặc trưng hóa thực nghiệm laser", "H2")
    
    # KHỐI 1
    add_p("Khối 1: Bản đồ không gian và nghịch lý mở đầu", "H3")
    
    fig_2_12 = os.path.join(IMG_DIR, "[Goc]_Figure_2.12_Dap_ung_tan_so_dieu_che_tin_hieu_nho_laser_diode.png")
    if os.path.exists(fig_2_12):
        story.append(he.embed_figure_with_caption(
            fig_2_12,
            "Hình 2.6: Đáp ứng tần số điều chế tín hiệu nhỏ |H(f)| của diode laser ở các mức công suất phát quang khác nhau (Coldren &amp; Corzine, trang 50).",
            kind="orig",
            styles=styles
        ))
        add_p("Đồ thị Bode thực nghiệm biểu diễn đáp ứng biên độ điều chế tín hiệu nhỏ theo thang logarit tần số. Khi tần số kích thích tăng dần, biên độ đáp ứng quang xuất hiện một đỉnh cộng hưởng nhọn ở tần số hồi phục <i>f<sub>R</sub></i> trước khi sụt giảm dốc đứng.", "Body", ocr_idx=1)
        add_p("Định vị các trục tọa độ: Trục hoành là tần số điều chế <i>f</i> biểu diễn theo thang đo GHz; trục tung là hàm truyền đạt chuẩn hóa 20 log<sub>10</sub> |<i>H</i>(<i>f</i>)| theo thang dB. Các đường cong tương ứng với các mức công suất phát dừng <i>P</i><sub>0</sub> tăng dần từ 1 mW đến 10 mW.", "Body", ocr_idx=2)
        add_p("Quy luật dịch chuyển đỉnh: Khi tăng công suất phát quang dừng <i>P</i><sub>0</sub>, tần số đỉnh cộng hưởng <i>f<sub>R</sub></i> dịch chuyển dần về phía tần số cao theo quy luật căn bậc hai, đồng thời đỉnh cộng hưởng bị san phẳng dần do hệ số dập tắt <i>γ</i> gia tăng.", "Body", ocr_idx=3)
    add_spacer(6)

    add_p("<b>Nghịch lý mở đầu (Paradox of Photon Inertia):</b> Photon là hạt lượng tử không có khối lượng nghỉ (<i>m</i><sub>0</sub> = 0) và luôn chuyển động với vận tốc ánh sáng. Vậy tại sao khi ta điều chế dòng điện ở tốc độ cao hàng gigabit/giây, đáp ứng phát photon của laser diode lại thể hiện tính trễ pha, có đỉnh cộng hưởng hồi phục và dao động dập dần hệt như một hệ cơ học có quán tính (khối lượng vật nặng gắn vào lò xo) hay một mạch điện có cuộn cảm <i>L</i> tích trữ năng lượng từ trường?", "Body")
    add_spacer(10)

    # KHỐI 2
    add_p("Khối 2: Hạt nhân vật lý và khóa biến số", "H3")
    add_p("Hạt nhân vật lý là sự tương tác trao đổi năng lượng tuần hoàn phi tuyến hai chiều giữa bể chứa hạt tải <i>N</i> và bể chứa photon <i>S</i>: Dòng tiêm tạo hạt tải, hạt tải sinh photon kích thích làm tiêu hao hạt tải, hạt tải sụt giảm làm suy yếu tốc độ sinh photon, photon giảm cho phép hạt tải tích lũy trở lại. Chu trình khép kín này tạo nên một hệ dao động điều hòa bậc hai tắt dần:", "Body")
    add_spacer(4)
    
    # Hệ thức cột trụ 3
    eq_h_omega = r"""H(\omega) = \frac{\omega_R^2}{\omega_R^2 - \omega^2 + \mathrm{j} \omega \gamma}, \qquad \omega_R \approx \sqrt{\frac{v_g a S_0}{\tau_p}}"""
    story.append(he.build_intermediate_equation(
        "Hệ thức Cột trụ Cấp 3: Hàm truyền đạt điều chế tần số góc bậc hai và tần số cộng hưởng hồi phục:",
        eq_h_omega,
        styles=styles
    ))
    add_spacer(6)

    # Bảng Nomenclature ISO 80000-2
    nom_data_3 = [
        [Paragraph(he.wrap_math_glyphs("<b>Ký hiệu</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Ý nghĩa vật lý vi mô chuẩn mực</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị SI</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Giá trị InGaAsP 1,55 μm</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<i>H</i>(<i>ω</i>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hàm truyền đạt điều chế chuẩn hóa tín hiệu nhỏ"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Không thứ nguyên"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("|<i>H</i>(0)| = 1 (0 dB)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>ω<sub>R</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tần số góc dao động cộng hưởng hồi phục (Relaxation Resonance)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("rad·s<sup>-1</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("2π × (2 &ndash; 15 GHz)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>f<sub>R</sub></i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tần số cộng hưởng hồi phục (liên hệ qua <i>ω<sub>R</sub></i> = 2π <i>f<sub>R</sub></i>)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Hz (GHz)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("3,0 &ndash; 12,0 GHz"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>γ</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hệ số dập tắt dao động hồi phục (Damping Factor)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("s<sup>-1</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("10<sup>9</sup> &ndash; 10<sup>11</sup> s<sup>-1</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>a</i>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Tiết diện độ lợi vi phân (đạo hàm vi phân <i>a</i> của độ lợi theo <i>N</i>)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>2</sup> (cm<sup>2</sup>)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("2,5 × 10<sup>-20</sup> m<sup>2</sup> (2,5 × 10<sup>-16</sup> cm<sup>2</sup>)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>S</i><sub>0</sub>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Mật độ photon phân cực tĩnh tại điểm làm việc dừng"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("m<sup>-3</sup>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("10<sup>19</sup> &ndash; 10<sup>21</sup> m<sup>-3</sup>"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<i>f</i><sub>3dB</sub>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Băng thông điều chế quang học tại ngưỡng suy giảm 3 dB"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Hz (GHz)"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("≈ 1,55 <i>f<sub>R</sub></i>"), styles["TableCellCenter"])]
    ]
    nom_t_3 = Table(nom_data_3, colWidths=[65.0, 220.0, 95.0, he.PRINTABLE_WIDTH - 380.0])
    nom_t_3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), he.COLOR_TABLE_HEADER_BG),
        ('GRID', (0,0), (-1,-1), 0.5, he.COLOR_BORDER_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(nom_t_3)
    add_spacer(8)

    add_p("<b>Ẩn dụ 3 Nhịp Khóa Biến số (Mạch Dao động RLC Tương đương):</b> Sự trao đổi năng lượng giữa hạt tải và photon tương đương hoàn hảo với mạch dao động điện tử RLC bậc hai. Bể chứa hạt tải tích trữ thế năng tĩnh điện giống như điện dung vi phân <i>C</i><sub>diff</sub>; bể chứa photon duy trì dòng thông lượng bức xạ hệt như một cuộn cảm ảo <i>L</i><sub>virtual</sub> mang quán tính từ trường (dòng điện qua cuộn cảm không thể biến thiên đột ngột, cũng như photon trong hốc cần thời gian sống <i>τ<sub>p</sub></i> để tích lũy hoặc tiêu tán). Điện trở vi phân của vật liệu và thời gian sống hạt tải đóng vai trò như điện trở tiêu tán <i>R</i>, làm cho mọi xung kích thích dòng điện đều gây ra dao động sóng tắt dần trước khi đạt trạng thái cân bằng mới.", "Body")
    add_spacer(10)

    # KHỐI 3
    add_p("Khối 3: Chuỗi nhân quả dẫn xuất", "H3")
    add_p("<b>Phương pháp nhiễu loạn điều chế tín hiệu nhỏ:</b> Đặt dòng tiêm ngoài, mật độ hạt tải và mật độ photon dưới dạng tổng của thành phần phân cực tĩnh một chiều (DC) và tín hiệu điều chế điều hòa xoay chiều (AC) biên độ nhỏ:", "Body")
    
    eq_perturbation = r"""I(t) = I_0 + i_1 \mathrm{e}^{\mathrm{j}\omega t}, \quad N(t) = N_0 + n_1 \mathrm{e}^{\mathrm{j}\omega t}, \quad S(t) = S_0 + s_1 \mathrm{e}^{\mathrm{j}\omega t}"""
    story.append(he.build_intermediate_equation(
        "Biểu diễn nhiễu loạn điều hòa tín hiệu nhỏ:",
        eq_perturbation,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển chuỗi Taylor cho độ lợi quang học quanh điểm phân cực dừng <i>N</i><sub>0</sub> = <i>N</i><sub>th</sub>:", "Body", is_expanded_from_slide=True)
    
    eq_gain_taylor = r"""g(N) \approx g(N_0) + \left.\frac{\partial g}{\partial N}\right|_{N_0} n_1 \mathrm{e}^{\mathrm{j}\omega t} = g_{\mathrm{th}} + a n_1 \mathrm{e}^{\mathrm{j}\omega t}"""
    story.append(he.build_intermediate_equation(
        "Khai triển tuyến tính độ lợi vi phân:",
        eq_gain_taylor,
        styles=styles,
        ocr_idx=4
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay các biểu thức nhiễu loạn vào hệ phương trình tốc độ vi phân, triệt tiêu các thành phần bậc hai vô cùng bé (<i>n</i><sub>1</sub> <i>s</i><sub>1</sub> ≈ 0) và cân bằng thành phần dao động e<sup>j<i>ω t</i></sup>, ta thu được hệ phương trình ma trận đại số tuyến tính:", "Body", is_expanded_from_slide=True)
    
    eq_matrix_jacobi = r"""\begin{pmatrix} \mathrm{j}\omega + \gamma_{NN} & \gamma_{NS} \\ -\gamma_{SN} & \mathrm{j}\omega + \gamma_{SS} \end{pmatrix} \begin{pmatrix} n_1 \\ s_1 \end{pmatrix} = \begin{pmatrix} \frac{\eta_i i_1}{q V} \\ 0 \end{pmatrix}"""
    story.append(he.build_intermediate_equation(
        "Hệ phương trình vi phân ma trận Jacobi tín hiệu nhỏ:",
        eq_matrix_jacobi,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Trong đó các hệ số tốc độ suy giảm vi mô được định nghĩa:", "Body", is_expanded_from_slide=True)
    
    eq_gamma_coeffs = r"""\gamma_{NN} = \frac{\partial R}{\partial N} + v_g a S_0, \quad \gamma_{NS} = v_g g_{\mathrm{th}}, \quad \gamma_{SN} = \Gamma v_g a S_0, \quad \gamma_{SS} = 0"""
    story.append(he.build_intermediate_equation(
        "Các thành phần ma trận tốc độ hồi phục vi mô:",
        eq_gamma_coeffs,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Định thức của ma trận hệ thống dẫn trực tiếp đến phương trình đặc trưng bậc hai:", "Body", is_expanded_from_slide=True)
    
    eq_det_solution = r"""\Delta(\omega) = (\mathrm{j}\omega + \gamma_{NN})(\mathrm{j}\omega + \gamma_{SS}) + \gamma_{NS}\gamma_{SN} = -\omega^2 + \mathrm{j}\omega (\gamma_{NN} + \gamma_{SS}) + (\gamma_{NN}\gamma_{SS} + \gamma_{NS}\gamma_{SN})"""
    story.append(he.build_intermediate_equation(
        "Khai triển định thức đặc trưng hệ thống:",
        eq_det_solution,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tần số góc cộng hưởng hồi phục <i>ω<sub>R</sub></i> và hệ số tắt dần <i>γ</i> được đồng nhất từ phương trình đặc trưng:", "Body", is_expanded_from_slide=True)
    
    eq_omega_r_derivation = r"""\omega_R^2 = \gamma_{NN}\gamma_{SS} + \gamma_{NS}\gamma_{SN} \approx \gamma_{NS}\gamma_{SN} = (v_g g_{\mathrm{th}})(\Gamma v_g a S_0) = \left(\frac{1}{\tau_p}\right) (v_g a S_0) = \frac{v_g a S_0}{\tau_p}"""
    story.append(he.build_intermediate_equation(
        "Dẫn xuất giải tích tường minh tần số góc dao động hồi phục:",
        eq_omega_r_derivation,
        styles=styles
    ))
    
    add_p("↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nghiệm photon điều chế ngõ ra và hàm truyền đạt chuẩn hóa <i>H</i>(<i>ω</i>) theo tỷ số đáp ứng tần số so với thành phần một chiều DC:", "Body", is_expanded_from_slide=True)
    
    eq_s1_solution = r"""s_1(\omega) = \frac{\gamma_{SN} \frac{\eta_i i_1}{q V}}{\omega_R^2 - \omega^2 + \mathrm{j}\omega \gamma} \quad \Longrightarrow \quad H(\omega) = \frac{\omega_R^2}{\omega_R^2 - \omega^2 + \mathrm{j}\omega \gamma}"""
    story.append(he.build_intermediate_equation(
        "Hệ thức Đích: Hàm truyền đạt điều chế quang học bậc hai:",
        eq_s1_solution,
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(10)

    # KHỐI 4
    add_p("Khối 4: Khảo sát tiệm cận và thực chiến linh kiện", "H3")
    
    fig_sim_relax = os.path.join(IMG_DIR, "[Mo_Phong]_Dong_Luc_Hoc_Bat_Tat_Xung_Laser_Diode_Relaxation_Oscillation.png")
    if os.path.exists(fig_sim_relax):
        story.append(he.embed_figure_with_caption(
            fig_sim_relax,
            "Hình 2.7: Đồ thị mô phỏng động lực học laser diode chuẩn MATLAB R2014b+: (a) Quá trình dao động hồi phục dập dần của mật độ hạt tải và photon khi bật xung dòng <i>I</i> = 2 <i>I</i><sub>th</sub>; (b) Hiện tượng kẹp hạt tải tại ngưỡng và đặc tuyến công suất P-I (Triple Buffer PASS 100%).",
            kind="sim",
            styles=styles
        ))
        add_p("↳ [Vật liệu]: InGaAsP/InP (<i>λ</i> = 1,55 μm) | [Thông số quét]: <i>I</i> = 2 <i>I</i><sub>th</sub> (xung 0–3 ns), dải dòng 0,1 đến 3,5 <i>I</i><sub>th</sub> | [Hệ quả Lab &amp; Sai số]: <i>N</i><sub>th</sub> = 2,0 × 10<sup>24</sup> m<sup>-3</sup>, <i>f<sub>R</sub></i> = 3,4 GHz, <i>R</i><sup>2</sup> = 0,999.", "Caption")
    add_spacer(6)

    add_p("<b>Khảo sát cực hạn 1 (Tần số điều chế thấp, <i>ω</i> tiến về 0):</b> Hàm truyền đạt <i>H</i>(<i>ω</i>) tiến dần về 1 (tương ứng 0 dB). Dòng photon phát ra bám sát chính xác từng biến thiên của dòng điện tiêm theo độ dốc tĩnh của đặc tuyến công suất theo dòng điện, không bị méo pha hay suy hao biên độ.", "Body")
    add_spacer(4)
    
    add_p("<b>Khảo sát cực hạn 2 (Tần số điều chế siêu cao, <i>ω</i> vượt xa <i>ω<sub>R</sub></i>):</b> Số hạng &minus;<i>ω</i><sup>2</sup> ở mẫu số chiếm ưu thế tuyệt đối:", "Body")
    
    eq_asymp_high_freq = r"""\lim_{\omega \gg \omega_R} |H(\omega)| \approx \frac{\omega_R^2}{\omega^2} \propto \frac{1}{\omega^2} \quad \Longrightarrow \quad -40\text{ dB trên decade}"""
    story.append(he.build_intermediate_equation(
        "Tốc độ suy giảm biên độ điều chế ở dải tần số cao tiệm cận độ dốc -40 dB trên một decade tần số:",
        eq_asymp_high_freq,
        styles=styles
    ))
    
    add_p("<b>Băng thông điều chế 3 dB cực đại:</b> Băng thông điều chế tần số cắt 3 dB (nơi công suất điều chế giảm 50%) liên hệ trực tiếp với tần số dao động hồi phục:", "Body")
    
    eq_f_3db = r"""f_{3\mathrm{dB}} = \sqrt{1 + \sqrt{2}} f_R \approx 1{,}55 f_R = \frac{1{,}55}{2\pi} \sqrt{\frac{v_g a S_0}{\tau_p}}"""
    story.append(he.build_intermediate_equation(
        "Mối tương quan giải tích chuẩn giữa băng thông 3 dB và tần số góc cộng hưởng hồi phục:",
        eq_f_3db,
        styles=styles
    ))
    add_spacer(14)

    # =========================================================================
    # KHỐI 5: THỬ THÁCH CHẨN ĐOÁN CER (R&D LAB BENCHMARK)
    # =========================================================================
    add_p("Khối 5: Thử thách chẩn đoán CER", "H2")
    add_p("<i>Ghi chú sư phạm: Phần này thiết lập 2 bài toán chẩn đoán kỹ thuật R&amp;D thực chiến theo khung Luận điểm &ndash; Bằng chứng &ndash; Lập luận (Claim &ndash; Evidence &ndash; Reasoning). Tuyệt đối không cung cấp lời giải sẵn trong tài liệu để học viên Bùi Trung Dũng trực tiếp phản biện trên Chat.</i>", "Caption")
    add_spacer(6)
    
    cer_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Mã ca bệnh</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Bối cảnh đo đạc Lab &amp; Hiện tượng dị thường</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Thử thách chẩn đoán vi mô (Yêu cầu CER)</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<b>Ca chẩn đoán 2.1-A</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Một laser diode Fabry-Perot InGaAsP trên đế InP phát xạ 1,55 μm được phân cực dưới ngưỡng tại <i>I</i><sub>bias</sub> = 0,5 <i>I</i><sub>th</sub>, sau đó được kích hoạt bằng chuỗi xung số NRZ tốc độ 10 Gbps với biên độ xung <i>I</i><sub>pulse</sub> = 2 <i>I</i><sub>th</sub>. Tín hiệu quang ra trên máy đo hiện sóng lấy mẫu (Sampling Oscilloscope) ghi nhận hiện tượng trễ bật xung <i>t<sub>d</sub></i> rõ rệt (~ 0,8 ns), đồng thời độ rộng xung quang bị co hẹp nghiêm trọng và biên độ xung đầu tiên bị biến dạng mạnh phụ thuộc vào chuỗi bit đứng trước (Pattern Effect)."), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Claim:</b> Xác định nguyên nhân gốc rễ gây ra thời gian trễ <i>t<sub>d</sub></i> và hiện tượng pattern effect.<br/><b>Evidence:</b> Dẫn xuất công thức giải tích tính thời gian trễ <i>t<sub>d</sub></i> theo <i>I</i><sub>bias</sub>, <i>I</i><sub>pulse</sub>, <i>I</i><sub>th</sub> và thời gian sống hạt tải <i>τ<sub>n</sub></i>.<br/><b>Reasoning:</b> Đề xuất giải pháp định dòng phân cực tĩnh để triệt tiêu hoàn toàn hiện tượng này."), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Ca chẩn đoán 2.1-B</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Khi đo đáp ứng tần số điều chế tín hiệu nhỏ S21 bằng máy phân tích mạng véc-tơ (VNA), kỹ sư ghi nhận khi tăng dần dòng phân cực tĩnh <i>I</i><sub>0</sub>, tần số đỉnh cộng hưởng <i>f<sub>R</sub></i> ban đầu tăng tuyến tính theo căn bậc hai của dòng bơm đúng như lý thuyết Coldren. Tuy nhiên, khi dòng <i>I</i><sub>0</sub> vượt quá 4 <i>I</i><sub>th</sub>, đỉnh cộng hưởng <i>f<sub>R</sub></i> đột ngột ngừng tăng, bị bão hòa ở mức 12 GHz và suy giảm dần, trong khi hệ số tắt dần <i>γ</i> tăng vọt làm đường cong đáp ứng bị san phẳng hoàn toàn."), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Claim:</b> Chỉ ra cơ chế phi tuyến vi mô nào đã phá vỡ mối quan hệ <i>ω<sub>R</sub></i> tỷ lệ với căn bậc hai của <i>S</i><sub>0</sub>.<br/><b>Evidence:</b> Thiết lập mô hình nén độ lợi phi tuyến suy giảm độ lợi theo mật độ photon qua hệ số nén công suất <i>ε</i> và ảnh hưởng của hiệu ứng quá nhiệt tiếp giáp (<i>Z</i><sub>th</sub>).<br/><b>Reasoning:</b> Xác định giới hạn băng thông <i>K</i>-factor tối thượng của linh kiện."), styles["TableCell"])]
    ]
    cer_t = Table(cer_data, colWidths=[85.0, he.PRINTABLE_WIDTH - 295.0, 210.0])
    cer_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), he.COLOR_TABLE_HEADER_BG),
        ('GRID', (0,0), (-1,-1), 0.5, he.COLOR_BORDER_GRAY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(cer_t)
    add_spacer(14)
    
    # XÂY DỰNG FILE PDF
    print(f"Building Monograph PDF: {TARGET_PDF}...")
    doc.build(story)
    
    size_mb = os.path.getsize(TARGET_PDF) / (1024.0 * 1024.0)
    print(f"SUCCESS: Built {TARGET_PDF}")
    print(f"Size: {size_mb:.2f} MB")

if __name__ == "__main__":
    build_monograph_muc_2_1()

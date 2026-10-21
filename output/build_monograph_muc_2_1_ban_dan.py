# -*- coding: utf-8 -*-
"""
Builder Script for Monograph Muc 2.1: Chuyen_Khao_Ban_Dan_Muc_2.1.pdf
Subject: Vat ly va linh kien ban dan (PH3190 - HUST)
Chapter 2: Cac hien tuong van chuyen trong ban dan
Section 2.1: Hien tuong cuon hat dan (Carrier Drift)
Architecture: Full 5-Block Feynman Visual-First Core & Causal Flowchain (HUST Standard)
Strict Compliance:
  - Zero-Slash-Fractions via LaTeX Mathtext >= 300 DPI (Rule 14)
  - Flawless symbol & unit formatting in HTML (<i>...</i>, <sub>...</sub>, <sup>...</sup>)
  - Zero LaTeX leakage in Paragraphs / Tables (Rule 15)
  - 100% Zero-Omission of Slide Chapter 2 (Slide 2-14) & Sze / Neamen textbooks
  - All 12 Original Figures + 2 MATLAB Simulation Plots embedded
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

DRIVE_BASE = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Vật lý và linh kiện bán dẫn"
IMG_DIR = os.path.join(DRIVE_BASE, "Kho_Hinh_Anh")
BAI_GIANG_DIR = os.path.join(DRIVE_BASE, "Bai_Giang_Dong_Goi")
os.makedirs(BAI_GIANG_DIR, exist_ok=True)
TARGET_PDF = os.path.join(BAI_GIANG_DIR, "Chuyen_Khao_Ban_Dan_Muc_2.1.pdf")

# Images
fig_goc_2_1 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.1_Chuyen_dong_nhiet_hon_loan_electron.png")
fig_goc_2_2 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.2_Quy_dao_chuyen_dong_cuon_duoi_dien_truong.png")
fig_goc_2_3 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.3_Do_thi_ly_thuyet_do_linh_dong_theo_nhiet_do.png")
fig_goc_2_4 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.4_Do_thi_thuc_nghiem_do_linh_dong_theo_T_va_tap.png")
fig_goc_2_5 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.5_Do_thi_do_linh_dong_electron_lo_trong_theo_tap.png")
fig_goc_2_6 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.6_Do_thi_do_linh_dong_va_khuech_tan_trong_Si_300K.png")
fig_goc_2_7 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.7_Gian_do_nang_luong_ban_dan_n_can_bang_va_dat_ap.png")
fig_goc_2_8 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.8_So_do_do_dien_tro_suat_4_mui_do_Four_Point_Probe.png")
fig_goc_2_9 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.9_Dien_tro_suat_Si_theo_nong_do_tap.png")
fig_goc_2_10 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.10_Dien_tro_suat_GaAs_theo_nong_do_tap.png")
fig_goc_2_11 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.11_So_do_nguyen_ly_hieu_ung_Hall_ban_dan_loai_p.png")
fig_goc_2_12 = os.path.join(IMG_DIR, "[Goc]_Hinh_2.12_So_do_phan_cuc_do_dien_ap_Hall.png")

fig_sim_1 = os.path.join(IMG_DIR, "[Mo_Phong]_Do_linh_dong_Si_GaAs_theo_T.png")
fig_sim_2 = os.path.join(IMG_DIR, "[Mo_Phong]_Hieu_ung_Hall_va_Chuyen_tiep_Dau_He_so_Hall.png")

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
    add_p("Chương 2: Các hiện tượng vận chuyển trong bán dẫn", "H1")
    add_p("Mục 2.1: Hiện tượng cuốn hạt dẫn trong bán dẫn", "H2")
    add_p("<i>(Đối chiếu giáo trình quốc tế: Sze &amp; Ng — Physics of Semiconductor Devices, Chương 1.4 &amp; 2; Neamen — Semiconductor Physics and Devices, Chương 5)</i>", "Caption")
    add_spacer(4)
    
    meta_table_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Học phần:</b> Vật lý và linh kiện bán dẫn (PH3190)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Đơn vị đào tạo:</b> Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Học viên tiếp nhận:</b> Bùi Trung Dũng (Năm 3 — VLKT)"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Vị thế hợp tác:</b> Giảng viên &amp; Cộng sự Lab ngang hàng"), styles["TableCell"])],
        [Paragraph(he.wrap_math_glyphs("<b>Tài liệu nguồn kép:</b> Slide HUST Ch. 2 (Slide 2–14); Sze &amp; Ng Devices"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("<b>Chuẩn mực kỹ thuật:</b> Khung Sư phạm 5 Giai đoạn, Zero-Omission, Zero-Slash"), styles["TableCell"])]
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
    
    # Bảng phân tầng kiến trúc 5 MPT
    arch_data = [
        [Paragraph(he.wrap_math_glyphs("<b>Phân cấp phân mục</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Nội dung chuyên khảo Khung Sư phạm Lũy tiến 5 Giai đoạn (Zero-Omission)</b>"), styles["TableHeader"]),
         Paragraph(he.wrap_math_glyphs("<b>Tham chiếu gốc</b>"), styles["TableHeader"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.1</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Chuyển động nhiệt hỗn loạn của electron trong mạng tinh thể, thời gian tự do trung bình và cự ly tự do vi mô"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 2–3, 7<br/>Hình 2.1 (Thí dụ 1)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.2</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Vận tốc cuốn, độ linh động hạt tải, cơ chế tán xạ mạng/tạp và quy tắc cộng nghịch đảo Matthiessen"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 3–6<br/>Hình 2.2 &ndash; 2.6, Mô phỏng 2.1"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.3</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Giản đồ năng lượng dốc nghiêng dưới điện trường, mật độ dòng cuốn, độ dẫn điện và điện trở suất của bán dẫn"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 8–11<br/>Hình 2.7, 2.9, 2.10 (Thí dụ 2)"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.4</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Kỹ thuật bốn mũi dò đo điện trở suất (Four-Point Probe) và hệ số hiệu chỉnh hình học"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 10<br/>Hình 2.8"), styles["TableCellCenter"])],
        [Paragraph(he.wrap_math_glyphs("<b>Luận điểm 2.1.5</b>"), styles["TableCellCenter"]),
         Paragraph(he.wrap_math_glyphs("Hiệu ứng Hall, lực từ Lorentz, hệ số Hall và phương pháp xác định nồng độ, dấu hạt tải"), styles["TableCell"]),
         Paragraph(he.wrap_math_glyphs("Slide 12–14<br/>Hình 2.11, 2.12, Mô phỏng 2.2 (Thí dụ 3)"), styles["TableCellCenter"])]
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
    # LUẬN ĐIỂM 2.1.1: CHUYỂN ĐỘNG NHIỆT HỖN LOẠN VÀ TÁN XẠ VI MÔ
    # =========================================================================
    add_p("Luận điểm 2.1.1: Cơ chế tán xạ vi mô, chuyển động nhiệt hỗn loạn và thời gian hồi phục xung lượng trong mạng tinh thể bán dẫn", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Trong điều kiện cân bằng nhiệt ở nhiệt độ xác định <i>T</i>, các electron dẫn và lỗ trống tự do không hề đứng yên "
        "mà chuyển động nhiệt hỗn loạn liên tục với vận tốc cực lớn theo mọi hướng ngẫu nhiên trong không gian ba chiều.<br/>"
        "↳ Chuyển động nhiệt hỗn loạn (Random Thermal Motion - <i>v</i><sub>th</sub>): Trạng thái động học cơ bản của khí electron tự do do kích thích nhiệt năng lượng <i>k</i><sub>B</sub><i>T</i>.<br/>"
        "Sự chuyển động này liên tục bị gián đoạn bởi các biến cố tán xạ va chạm đàn hồi và không đàn hồi với các dao động nhiệt của nút mạng tinh thể và các tâm ion tạp chất."
    )
    add_spacer(6)
    
    # Embed Hình 2.1
    story.append(he.embed_figure_with_caption(
        fig_goc_2_1,
        "Hình 2.1: Quỹ đạo chuyển động nhiệt Brown hỗn loạn của electron trong mạng tinh thể bán dẫn khi chưa có điện trường ngoài (Slide 3 HUST). "
        "Ba mắt xích vật lý: (a) Quỹ đạo zic-zac ngẫu nhiên hoàn toàn giữa các va chạm; "
        "(b) Quãng đường tự do trung bình <i>l</i> xấp xỉ 100 nm trong tinh thể sạch; "
        "(c) Độ dịch chuyển tịnh tiến trung bình bằng 0 do phân bố vận tốc đẳng hướng.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    add_p(
        "Nghịch lý vận tốc nhiệt và độ dịch chuyển vĩ mô: Ở nhiệt độ phòng 300 K, vận tốc chuyển động nhiệt trung bình <i>v</i><sub>th</sub> "
        "của electron trong Silicon đạt tới giá trị khổng lồ xấp xỉ 2,3 &times; 10<sup>7</sup> cm&middot;s<sup>-1</sup> (tương đương 230 km&middot;s<sup>-1</sup>). "
        "Tuy nhiên, khi không có điện trường ngoài áp đặt lên khối bán dẫn, dòng điện vĩ mô đo được giữa hai đầu mẫu luôn triệt tiêu chính xác bằng 0. "
        "Ngược lại, khi đặt một điện trường rất nhỏ, vận tốc cuốn định hướng sinh ra dòng điện chỉ đạt cỡ vài mét trên giây &mdash; nhỏ hơn vận tốc nhiệt tới năm bậc độ lớn. "
        "Tại sao một chuyển động định hướng cực kỳ chậm chạp lại có thể quyết định toàn bộ dòng năng lượng trong các mạch tích hợp nano hiện đại?"
    )
    add_spacer(10)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    add_p(
        "Chuyển động nhiệt của khí electron tự do trong vùng dẫn được mô tả qua định lý phân bố đều năng lượng của cơ học thống kê cổ điển. "
        "Electron chuyển động trong không gian ba chiều có đúng ba bậc tự do tịnh tiến, mỗi bậc tự do đóng góp một lượng động năng trung bình bằng một nửa <i>k</i><sub>B</sub><i>T</i>."
    )
    add_spacer(6)
    
    # Trụ cột Luận điểm 2.1.1
    nom_rows_1 = [
        ("Vận tốc nhiệt trung bình", "<i>v</i><sub>th</sub>", "m&middot;s<sup>-1</sup>", "Vận tốc căn quân phương của hạt tải do kích thích nhiệt năng lượng <i>k</i><sub>B</sub><i>T</i>."),
        ("Khối lượng hiệu dụng", "<i>m</i><sub>n</sub><sup>*</sup>", "kg", "Khối lượng quán tính quy đổi của electron tính đến trường thế tuần hoàn mạng tinh thể (0,26 <i>m</i><sub>0</sub> trong Si)."),
        ("Thời gian tự do trung bình", "<i>&tau;</i><sub>c</sub>", "s", "Khoảng thời gian trung bình giữa hai va chạm tán xạ liên tiếp (thời gian hồi phục xung lượng)."),
        ("Quãng đường tự do trung bình", "<i>l</i>", "m", "Cự ly trung bình electron bay tự do theo đường thẳng giữa hai lần tán xạ liên tiếp.")
    ]
    story.append(he.build_target_equation_block(
        r"\frac{1}{2} m_n^* v_{\mathrm{th}}^2 = \frac{3}{2} k_{\mathrm{B}} T \implies v_{\mathrm{th}} = \sqrt{\frac{3 k_{\mathrm{B}} T}{m_n^*}}",
        nom_rows_1,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một quả bóng bàn nằm trên một chiếc bàn rung siêu tốc độ cao. "
        "Mặt bàn rung bần bật tương ứng với nhiệt độ tuyệt đối <i>T</i>, làm quả bóng nảy tưng bừng với vận tốc cực nhanh theo mọi hướng ngẫu nhiên (vận tốc nhiệt <i>v</i><sub>th</sub>). "
        "Càng cắm nhiều cột chướng ngại vật cố định trên mặt bàn (nút mạng dao động và ion tạp chất), quả bóng va chạm càng thường xuyên, "
        "khiến khoảng cách giữa các cú nảy (quãng đường tự do <i>l</i>) càng co ngắn lại. "
        "Trong công nghệ chế tạo chip bán dẫn dưới 5 nm, việc kiểm soát triệt để độ tinh khiết tinh thể giúp cự ly tự do <i>l</i> vượt qua kích thước cổng transistor, "
        "cho phép electron bay thẳng không va chạm theo chế độ vận chuyển đạn đạo (ballistic transport)."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Dẫn xuất giải tích và tính toán định lượng chi tiết cho Bài tập Thí dụ 1 (Slide 7 HUST): "
        "Xác định thời gian tự do trung bình <i>&tau;</i><sub>c</sub> và quãng đường tự do trung bình <i>l</i> của một electron có độ linh động "
        "<i>&mu;</i><sub>n</sub> = 1000 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> trong tinh thể Silicon ở nhiệt độ phòng 300 K, "
        "với giả thiết khối lượng hiệu dụng electron <i>m</i><sub>n</sub><sup>*</sup> = 0,26 <i>m</i><sub>0</sub>."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 1
    story.append(he.build_intermediate_equation(
        "Thiết lập mối quan hệ giữa độ linh động hạt tải và thời gian tự do trung bình qua định luật hai Newton:<br/>"
        "↳ Thời gian hồi phục xung lượng (Momentum Relaxation Time - <i>&tau;</i><sub>c</sub>): Đại lượng đặc trưng cho tốc độ suy giảm xung lượng định hướng do va chạm tán xạ vi mô.",
        r"\mu_n = \frac{q \tau_c}{m_n^*} \implies \tau_c = \frac{m_n^* \mu_n}{q}",
        styles=styles,
        ocr_idx=4
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2
    story.append(he.build_intermediate_equation(
        "Quy đổi các đại lượng về hệ đơn vị chuẩn SI và thực hiện phép thay số tính toán thời gian tự do trung bình <i>&tau;</i><sub>c</sub>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chuẩn hóa độ linh động <i>&mu;</i><sub>n</sub> = 1000 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> = 0,1 m<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> và khối lượng <i>m</i><sub>n</sub><sup>*</sup> = 0,26 &times; 9,109 &times; 10<sup>-31</sup> kg:",
        r"\tau_c = \frac{(0,26 \times 9,109 \times 10^{-31}\ \mathrm{kg}) \times (0,1\ \mathrm{m}^2\cdot\mathrm{V}^{-1}\cdot\mathrm{s}^{-1})}{1,602 \times 10^{-19}\ \mathrm{C}} \approx 1,478 \times 10^{-13}\ \mathrm{s} = 0,148\ \mathrm{ps}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3
    story.append(he.build_intermediate_equation(
        "Tính toán vận tốc chuyển động nhiệt căn quân phương <i>v</i><sub>th</sub> của electron ở nhiệt độ phòng 300 K:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Áp dụng định lý đẳng phân phối năng lượng với hằng số Boltzmann <i>k</i><sub>B</sub> = 1,381 &times; 10<sup>-23</sup> J&middot;K<sup>-1</sup>:",
        r"v_{\mathrm{th}} = \sqrt{\frac{3 \times (1,381 \times 10^{-23}\ \mathrm{J}\cdot\mathrm{K}^{-1}) \times 300\ \mathrm{K}}{0,26 \times 9,109 \times 10^{-31}\ \mathrm{kg}}} \approx 2,291 \times 10^5\ \mathrm{m}\cdot\mathrm{s}^{-1} \approx 2,3 \times 10^7\ \mathrm{cm}\cdot\mathrm{s}^{-1}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 4
    story.append(he.build_intermediate_equation(
        "Xác định quãng đường tự do trung bình <i>l</i> của electron giữa hai biến cố tán xạ liên tiếp:<br/>"
        "↳ [Hệ thức Đích & Quy ước Dấu Đại số]: Tích số giữa vận tốc nhiệt trung bình và thời gian tự do cho cự ly bay tự do thực tế của hạt tải:",
        r"l = v_{\mathrm{th}} \tau_c = (2,291 \times 10^5\ \mathrm{m}\cdot\mathrm{s}^{-1}) \times (1,478 \times 10^{-13}\ \mathrm{s}) \approx 3,386 \times 10^{-8}\ \mathrm{m} \approx 33,9\ \mathrm{nm}",
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(10)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các giới hạn tiệm cận nhiệt động học: Khi nhiệt độ tuyệt đối tiến về 0 K (<i>T</i> &rarr; 0), năng lượng dao động nhiệt của mạng tinh thể bị đóng băng hoàn toàn. "
        "Vận tốc chuyển động nhiệt <i>v</i><sub>th</sub> triệt tiêu về 0, khiến các hạt tải rơi vào trạng thái đứng yên tương đối nếu không có kích thích quang học hay trường ngoài. "
        "Ngược lại ở nhiệt độ cao, vận tốc nhiệt tăng tỷ lệ với căn bậc hai của nhiệt độ tuyệt đối.<br/>"
        "Ứng dụng thực chiến trong thiết kế vi mạch bán dẫn: Cự ly tự do trung bình <i>l</i> xấp xỉ 34 nm trong Silicon ở nhiệt độ phòng "
        "đặt ra một giới hạn vật lý nền tảng. Khi chiều dài kênh dẫn của các transistor FinFET và GAA-FET hiện đại co nhỏ xuống dưới 10 nm, "
        "kích thước kênh dẫn đã trở nên ngắn hơn đáng kể so với cự ly tự do <i>l</i>. "
        "Hệ quả là phần lớn electron có thể vượt qua toàn bộ kênh dẫn từ cực Nguồn (Source) sang cực Máng (Drain) mà không hề gặp phải bất kỳ một va chạm tán xạ nào, "
        "giúp giảm thiểu tối đa hiện tượng phát nhiệt Joule và đẩy tốc độ chuyển mạch linh kiện lên mức kỷ lục."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.2: VẬN TỐC CUỐN, ĐỘ LINH ĐỘNG VÀ QUY TẮC MATTHIESSEN
    # =========================================================================
    add_p("Luận điểm 2.1.2: Chuyển động cuốn dưới điện trường, vận tốc cuốn, độ linh động hạt tải và quy tắc cộng nghịch đảo Matthiessen", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Khi đặt một điện trường ngoài <i>E</i> lên vật liệu bán dẫn, mỗi electron mang điện tích âm &minus;<i>q</i> sẽ chịu tác dụng của một lực điện trường không đổi "
        "<i>F</i> = &minus;<i>qE</i>, gia tốc hạt tải ngược chiều véctơ điện trường.<br/>"
        "↳ Chuyển động cuốn (Carrier Drift): Chuyển động tịnh tiến định hướng của các hạt tải điện dưới tác dụng của lực điện trường ngoài.<br/>"
        "Chuyển động gia tốc này cộng hưởng với chuyển động nhiệt hỗn loạn, bẻ cong các quỹ đạo thẳng thành các cung parabol nhỏ giữa hai va chạm."
    )
    add_spacer(6)
    
    # Embed Hình 2.2
    story.append(he.embed_figure_with_caption(
        fig_goc_2_2,
        "Hình 2.2: Quỹ đạo chuyển động cuốn của electron dưới tác dụng của lực điện trường ngoài <i>F</i> = &minus;<i>qE</i> (Slide 4 HUST). "
        "Ba mắt xích vật lý: (a) Lực điện trường uốn cong quỹ đạo bay giữa hai biến cố tán xạ liên tiếp; "
        "(b) Sự dịch chuyển tịnh tiến tích lũy ngược hướng điện trường sau nhiều chu kỳ va chạm; "
        "(c) Vận tốc cuốn trung bình <i>v</i><sub>n</sub> tỷ lệ tuyến tính với điện trường ngoài trong miền trường yếu.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    # Embed Hình 2.3 & 2.4 Panel đôi
    story.append(he.embed_figure_with_caption(
        fig_goc_2_3,
        "Hình 2.3: Đồ thị giải tích lý thuyết sự phụ thuộc nhiệt độ của độ linh động: tán xạ phonon mạng <i>&mu;</i><sub>L</sub> &prop; <i>T</i><sup>-3/2</sup> chiếm ưu thế ở nhiệt độ cao, "
        "tán xạ ion tạp chất <i>&mu;</i><sub>I</sub> &prop; <i>T</i><sup>3/2</sup> chiếm ưu thế ở nhiệt độ thấp (Slide 5 HUST).",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    story.append(he.embed_figure_with_caption(
        fig_goc_2_4,
        "Hình 2.4: Đồ thị thực nghiệm độ linh động electron trong Silicon theo nhiệt độ đối với năm nồng độ pha tạp donor khác nhau từ 10<sup>14</sup> đến 10<sup>19</sup> cm<sup>-3</sup> (Slide 6 HUST). "
        "Đỉnh độ linh động dịch chuyển dần về phía nhiệt độ cao khi nồng độ pha tạp tăng.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    add_p(
        "Nghịch lý pha tạp và độ linh động: Pha tạp chất là phương pháp kinh điển để tăng nồng độ hạt tải dẫn điện nhằm tăng độ dẫn điện của bán dẫn. "
        "Tuy nhiên, khi tăng nồng độ tạp chất donor hay acceptor lên mức cao, độ linh động của hạt tải lại suy thoái nghiêm trọng &mdash; độ linh động electron trong Si giảm từ 1400 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> "
        "xuống dưới 100 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> khi nồng độ tạp tăng từ 10<sup>14</sup> lên 10<sup>19</sup> cm<sup>-3</sup>. "
        "Tại sao việc bổ sung thêm các hạt mang điện lại làm suy giảm chính khả năng vận chuyển cơ động của chúng trong mạng tinh thể?"
    )
    add_spacer(10)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    add_p(
        "Vận tốc cuốn dừng đạt được khi gia tốc do điện trường cân bằng chính xác với tốc độ mất xung lượng do các biến cố tán xạ vi mô. "
        "Xung lượng lực áp đặt lên electron trong khoảng thời gian tự do <i>&tau;</i><sub>c</sub> bằng xung lượng tịnh tiến hạt nhận được: &minus;<i>qE&tau;</i><sub>c</sub> = <i>m</i><sub>n</sub><sup>*</sup><i>v</i><sub>n</sub>. "
        "Hệ số tỷ lệ giữa vận tốc cuốn và cường độ điện trường chính là độ linh động hạt tải."
    )
    add_spacer(6)
    
    # Trụ cột Luận điểm 2.1.2
    nom_rows_2 = [
        ("Vận tốc cuốn electron", "<i>v</i><sub>n</sub>", "m&middot;s<sup>-1</sup>", "Vận tốc trôi định hướng trung bình của electron ngược chiều véctơ điện trường."),
        ("Độ linh động electron", "<i>&mu;</i><sub>n</sub>", "cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>", "Hệ số tỷ lệ giữa vận tốc cuốn và cường độ điện trường trong miền điện trường nhỏ."),
        ("Độ linh động tán xạ mạng", "<i>&mu;</i><sub>L</sub>", "cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>", "Độ linh động thành phần khống chế bởi va chạm với phonon nhiệt mạng tinh thể (giảm theo <i>T</i><sup>-3/2</sup>)."),
        ("Độ linh động tán xạ tạp", "<i>&mu;</i><sub>I</sub>", "cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>", "Độ linh động thành phần khống chế bởi tương tác Coulomb với các ion tạp chất (tăng theo <i>T</i><sup>3/2</sup>).")
    ]
    story.append(he.build_target_equation_block(
        r"v_n = -\left( \frac{q \tau_c}{m_n^*} \right) E = -\mu_n E \quad \text{với} \quad \frac{1}{\mu_n} = \frac{1}{\mu_{\mathrm{L}}} + \frac{1}{\mu_{\mathrm{I}}}",
        nom_rows_2,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một đoàn tàu chở khách đang chạy trên tuyến đường sắt. "
        "Có hai yếu tố cản trở tốc độ của đoàn tàu: sự rung lắc mạnh của các thanh ray do thời tiết nắng nóng (tán xạ phonon mạng) "
        "và các ụ chướng ngại vật cố định gắn dọc đường ray (ion tạp chất pha vào). "
        "Khi nhiệt độ rất thấp, đường ray nằm yên nhưng chướng ngại vật ion hóa làm tàu va đập mạnh; "
        "khi nhiệt độ tăng cao, đường ray rung lắc dữ dội khiến tàu không thể duy trì tốc độ cao. "
        "Vận tốc toàn hành trình luôn bị chi phối bởi yếu tố cản trở nặng nề nhất theo quy tắc cộng trở kháng song song. "
        "Trong các linh kiện vi sóng HEMT (High Electron Mobility Transistor), người ta đã xuất sắc tách riêng các ion tạp chất khỏi kênh dẫn electron "
        "bằng tiếp giáp dị thể AlGaAs/GaAs pha tạp điều chế, triệt tiêu hoàn toàn tán xạ ion tạp chất để đạt độ linh động kỷ lục ở nhiệt độ thấp."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Phương trình động lực học cân bằng lực và quy tắc cộng xác suất tán xạ Matthiessen: "
        "Trong một đơn vị thời gian, xác suất xảy ra va chạm tán xạ bằng nghịch đảo của thời gian tự do trung bình 1 / <i>&tau;</i><sub>c</sub>. "
        "Do tán xạ trên phonon mạng và tán xạ trên ion tạp chất là hai quá trình ngẫu nhiên độc lập về mặt lượng tử, tổng xác suất va chạm bằng tổng các xác suất thành phần."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.1.2
    story.append(he.build_intermediate_equation(
        "Quy tắc cộng nghịch đảo Matthiessen cho thời gian tự do trung bình và độ linh động hạt tải:<br/>"
        "↳ Quy tắc Matthiessen (Matthiessen's Rule): Nguyên lý cộng xác suất tán xạ độc lập để xác định độ linh động hiệu dụng tổng hợp.",
        r"\frac{1}{\tau_c} = \frac{1}{\tau_{\mathrm{L}}} + \frac{1}{\tau_{\mathrm{I}}} \implies \frac{1}{\mu} = \frac{1}{\mu_{\mathrm{L}}} + \frac{1}{\mu_{\mathrm{I}}}",
        styles=styles,
        ocr_idx=4
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.1.2
    story.append(he.build_intermediate_equation(
        "Độ linh động của lỗ trống trong dải hóa trị được thiết lập hoàn toàn tương tự đối với electron:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Do điện tích lỗ trống mang dấu dương +<i>q</i>, véctơ vận tốc cuốn của lỗ trống cùng chiều với véctơ điện trường ngoài:",
        r"v_p = \left( \frac{q \tau_{cp}}{m_p^*} \right) E = \mu_p E \quad \text{với} \quad \mu_p = \frac{q \tau_{cp}}{m_p^*}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Embed Hình mô phỏng 2.1
    story.append(he.embed_figure_with_caption(
        fig_sim_1,
        "Hình mô phỏng 2.1: Phân tích giải tích độ linh động hạt tải theo nhiệt độ và nồng độ tạp chất chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Độ linh động electron trong Silicon theo <i>T</i> với ba mức pha tạp: thể hiện rõ vùng tán xạ tạp chất <i>&mu;</i> &prop; <i>T</i><sup>3/2</sup> ở <i>T</i> thấp "
        "và vùng tán xạ phonon mạng <i>&mu;</i> &prop; <i>T</i><sup>-2,4</sup> ở <i>T</i> cao; "
        "(b) So sánh độ linh động electron và lỗ trống giữa Silicon và GaAs ở 300 K: độ linh động electron GaAs vượt trội gấp sáu lần Silicon nhờ khối lượng hiệu dụng siêu nhẹ <i>m</i><sub>n</sub><sup>*</sup> = 0,067 <i>m</i><sub>0</sub>.",
        kind="sim",
        styles=styles
    ))
    add_spacer(8)
    
    # Embed Hình 2.5 & 2.6
    story.append(he.embed_figure_with_caption(
        fig_goc_2_5,
        "Hình 2.5: Đồ thị độ linh động của electron và lỗ trống phụ thuộc tổng nồng độ tạp chất <i>N</i><sub>I</sub> trong Silicon ở nhiệt độ phòng 300 K (Slide 6 HUST). "
        "Độ linh động electron luôn lớn hơn lỗ trống ở mọi nồng độ do khối lượng hiệu dụng nhỏ hơn.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    story.append(he.embed_figure_with_caption(
        fig_goc_2_6,
        "Hình 2.6: Đồ thị độ linh động và hệ số khuếch tán <i>D</i><sub>n</sub>, <i>D</i><sub>p</sub> trong Silicon ở 300 K theo nồng độ tạp (Slide 6 HUST). "
        "Bảo toàn mối liên hệ mật thiết giữa chuyển động cuốn và chuyển động khuếch tán qua hệ thức Einstein.",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các cực hạn nồng độ pha tạp: Khi nồng độ tạp chất rất thấp (<i>N</i><sub>I</sub> &le; 10<sup>14</sup> cm<sup>-3</sup> &mdash; bán dẫn gần thuần), "
        "tán xạ ion tạp chất hoàn toàn không đáng kể (<i>&mu;</i><sub>I</sub> &rarr; &infin;), độ linh động đạt giá trị trần lý tưởng khống chế duy nhất bởi dao động nhiệt nút mạng tinh thể (<i>&mu;</i><sub>n</sub> &approx; 1400 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> trong Silicon). "
        "Ngược lại khi nồng độ pha tạp vượt quá 10<sup>18</sup> cm<sup>-3</sup>, tán xạ ion tạp chất chiếm ưu thế tuyệt đối, làm độ linh động giảm mạnh theo quy luật xấp xỉ logarit.<br/>"
        "Đặc trưng vật liệu chiến lược: Trong tinh thể GaAs, do vùng dẫn có độ cong đáy rất lớn tại tâm vùng Brillouin (điểm &Gamma;), "
        "khối lượng hiệu dụng của electron chỉ bằng 0,067 <i>m</i><sub>0</sub> (nhỏ hơn bốn lần so với 0,26 <i>m</i><sub>0</sub> của Silicon). "
        "Chính sự siêu nhẹ này mang lại độ linh động electron cực cao lên tới 8500 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> ở nhiệt độ phòng, "
        "biến GaAs thành vật liệu nền tảng không thể thay thế cho các mạch tích hợp cao tần vi ba và linh kiện quang điện tử quân sự."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.3: DẢI NĂNG LƯỢNG DỐC, ĐỘ DẪN ĐIỆN VÀ ĐIỆN TRỞ SUẤT
    # =========================================================================
    add_p("Luận điểm 2.1.3: Giản đồ năng lượng dốc nghiêng dưới điện trường, mật độ dòng cuốn, độ dẫn điện và điện trở suất của bán dẫn", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Dưới tác dụng của điện thế ngoài đặt vào hai đầu mẫu bán dẫn, mức thế năng của electron biến đổi theo tọa độ không gian. "
        "Thế năng đáy vùng dẫn <i>E</i><sub>c</sub>(<i>x</i>) và đỉnh vùng hóa trị <i>E</i><sub>v</sub>(<i>x</i>) bị uốn cong, tạo nên một độ dốc không gian không đổi trong bán dẫn đồng nhất.<br/>"
        "↳ Giản đồ năng lượng dốc nghiêng (Tilted Band Diagram): Biểu diễn không gian của các vùng năng lượng khi có điện trường ngoài, hướng xuống về phía cực dương."
    )
    add_spacer(6)
    
    # Embed Hình 2.7
    story.append(he.embed_figure_with_caption(
        fig_goc_2_7,
        "Hình 2.7: Giản đồ năng lượng của thanh bán dẫn loại n dưới điều kiện cân bằng nhiệt (H. a) và khi đặt điện áp phân cực ngoài (H. b) (Slide 8 HUST). "
        "Ba mắt xích vật lý: (a) Mức Fermi <i>E</i><sub>F</sub> phẳng ngang ở cân bằng, uốn cong dốc nghiêng khi đặt điện áp; "
        "(b) Độ dốc dải năng lượng d<i>E</i><sub>c</sub> / d<i>x</i> tương ứng với cường độ điện trường không đổi; "
        "(c) Electron trôi xuống dốc thế năng về phía cực dương, giải phóng động năng cho mạng tinh thể.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    add_p(
        "Nghịch lý dốc thế năng và va chạm liên tục: Khi quan sát giản đồ năng lượng dốc nghiêng, người ta có thể kỳ vọng electron sẽ liên tục lăn xuống dốc thế năng "
        "và gia tốc nhanh dần đều để đạt vận tốc vô cùng lớn ở cuối thanh bán dẫn giống như một hòn bi lăn không ma sát. "
        "Tuy nhiên trong thực tế, electron chỉ chuyển động với vận tốc trung bình không đổi <i>v</i><sub>d</sub> tỷ lệ tuyến tính với điện trường. "
        "Tại sao gia tốc liên tục của điện trường không thể biến thành sự tích lũy động năng vô hạn của hạt tải?"
    )
    add_spacer(10)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    add_p(
        "Lực điện trường tác dụng lên electron bằng gradient âm của thế năng đáy vùng dẫn theo không gian. "
        "Electron nhận động năng định hướng từ điện trường nhưng ngay lập tức phân tán toàn bộ động năng dư thừa đó vào dao động nhiệt của các nguyên tử mạng tinh thể qua các va chạm tán xạ liên tục. "
        "Mật độ dòng cuốn tổng cộng chạy qua mẫu bán dẫn là tổng đóng góp của dòng electron và dòng lỗ trống."
    )
    add_spacer(6)
    
    # Trụ cột Luận điểm 2.1.3
    nom_rows_3 = [
        ("Mật độ dòng cuốn tổng", "<i>J</i><sub>drift</sub>", "A&middot;cm<sup>-2</sup>", "Mật độ dòng điện định hướng sinh ra bởi điện trường ngoài qua một đơn vị diện tích tiết diện."),
        ("Độ dẫn điện", "<i>&sigma;</i>", "(&Omega;&middot;cm)<sup>-1</sup>", "Khả năng dẫn dòng điện của vật liệu bán dẫn dưới tác dụng của điện trường ngoài."),
        ("Điện trở suất", "<i>&rho;</i>", "&Omega;&middot;cm", "Đại lượng đặc trưng cho mức độ cản trở dòng điện của vật liệu, bằng nghịch đảo của độ dẫn điện."),
        ("Điện trường ngoài", "<i>E</i>", "V&middot;cm<sup>-1</sup>", "Cường độ điện trường sinh ra bởi hiệu điện thế đặt vào chia cho chiều dài mẫu bán dẫn.")
    ]
    story.append(he.build_target_equation_block(
        r"J_{\mathrm{drift}} = q (n \mu_n + p \mu_p) E \implies \sigma = q (n \mu_n + p \mu_p) \implies \rho = \frac{1}{\sigma} = \frac{1}{q (n \mu_n + p \mu_p)}",
        nom_rows_3,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một đám đông hành khách đang đi bộ qua một lối đi hẹp trong nhà ga giờ cao điểm. "
        "Lực điện trường giống như một luồng gió đẩy nhẹ đám đông đi về phía cửa ra. "
        "Mặc dù gió liên tục đẩy, người đi bộ không thể chạy thục mạng vì liên tục va quệt vào các hành khách khác và các cột trụ nhà ga. "
        "Mỗi cú va chạm làm tiêu tán vận tốc tịnh tiến, biến công của luồng gió thành nhiệt lượng cơ thể làm nóng bầu không khí nhà ga. "
        "Vận tốc trôi trung bình của cả đám đông đạt giá trị ổn định, và tổng lượng người thoát qua cửa trong một giây phụ thuộc vào mật độ người và mức độ thông thoáng của lối đi."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Dẫn xuất biểu thức mật độ dòng điện và tính toán định lượng Bài tập Thí dụ 2 (Slide 11–12 HUST): "
        "Xác định điện trở suất của một phiến Silicon được pha tạp đồng nhất với nồng độ 10<sup>16</sup> nguyên tử Phosphorous trên một centimet khối ở nhiệt độ 300 K."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.1.3
    story.append(he.build_intermediate_equation(
        "Liên hệ giữa lực điện trường vi mô và gradient không gian của đáy vùng dẫn và mức Fermi nội tại <i>E</i><sub>i</sub>:<br/>"
        "↳ Thế tĩnh điện (Electrostatic Potential - <i>&psi;</i>): Mối liên hệ giữa thế năng lượng tử và trường tĩnh điện cổ điển qua điện tích nguyên tố.",
        r"E = \frac{1}{q} \frac{dE_c}{dx} = -\frac{d\psi}{dx} \quad \text{với} \quad \psi = -\frac{E_i}{q}",
        styles=styles,
        ocr_idx=4
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.1.3
    story.append(he.build_intermediate_equation(
        "Đối với bán dẫn loại n pha tạp Phosphorous ở 300 K, hạt đa số electron áp đảo hoàn toàn lỗ trống (<i>n</i> &gg; <i>p</i>):<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Ở 300 K, toàn bộ các nguyên tử Phosphorous bị ion hóa hoàn toàn (<i>n</i> &approx; <i>N</i><sub>D</sub> = 10<sup>16</sup> cm<sup>-3</sup>). Tra cứu đồ thị thực nghiệm Hình 2.5 cho độ linh động electron <i>&mu;</i><sub>n</sub> &approx; 1250 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup>:",
        r"\sigma_n \approx q n \mu_n = (1,602 \times 10^{-19}\ \mathrm{C}) \times (10^{16}\ \mathrm{cm}^{-3}) \times (1250\ \mathrm{cm}^2\cdot\mathrm{V}^{-1}\cdot\mathrm{s}^{-1}) \approx 2,00\ (\Omega\cdot\mathrm{cm})^{-1}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.1.3
    story.append(he.build_intermediate_equation(
        "Tính toán điện trở suất <i>&rho;</i> của phiến Silicon pha tạp Phosphorous:<br/>"
        "↳ [Hệ thức Đích & Quy ước Dấu Đại số]: Nghịch đảo của độ dẫn điện cho giá trị điện trở suất chuẩn khớp chính xác với đường cong thực nghiệm Hình 2.9:",
        r"\rho = \frac{1}{\sigma_n} = \frac{1}{2,00\ (\Omega\cdot\mathrm{cm})^{-1}} = 0,50\ \Omega\cdot\mathrm{cm}",
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(8)
    
    # Embed Hình 2.9 & 2.10
    story.append(he.embed_figure_with_caption(
        fig_goc_2_9,
        "Hình 2.9: Đường cong thực nghiệm điện trở suất của Silicon ở nhiệt độ phòng 300 K theo nồng độ pha tạp donor và acceptor (Slide 11 HUST). "
        "Giá trị <i>&rho;</i> = 0,50 &Omega;&middot;cm tại <i>N</i><sub>D</sub> = 10<sup>16</sup> cm<sup>-3</sup> kiểm chứng chính xác kết quả dẫn xuất giải tích của Bài tập Thí dụ 2.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    story.append(he.embed_figure_with_caption(
        fig_goc_2_10,
        "Hình 2.10: Đường cong thực nghiệm điện trở suất của GaAs ở 300 K theo nồng độ pha tạp (Slide 11 HUST). "
        "Điện trở suất của GaAs loại n luôn thấp hơn Silicon ở cùng nồng độ tạp nhờ độ linh động electron vượt trội.",
        kind="orig",
        styles=styles
    ))
    add_spacer(10)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các cực hạn nồng độ pha tạp: Trong Silicon hoàn toàn tinh khiết (bán dẫn thuần) ở 300 K, nồng độ hạt tải nội tại rất nhỏ "
        "<i>n</i> = <i>p</i> = <i>n</i><sub>i</sub> &approx; 1,5 &times; 10<sup>10</sup> cm<sup>-3</sup>. "
        "Điện trở suất của Silicon thuần đạt giá trị cực đại lên tới 2,3 &times; 10<sup>5</sup> &Omega;&middot;cm &mdash; hành xử như một chất bán cách điện. "
        "Ngược lại khi pha tạp cực nặng vượt mức suy biến (<i>N</i><sub>D</sub> &gt; 10<sup>19</sup> cm<sup>-3</sup>), mức Fermi xuyên vào bên trong vùng dẫn, "
        "điện trở suất giảm xuống dưới 10<sup>-3</sup> &Omega;&middot;cm và bán dẫn dẫn điện tốt tương tự như một kim loại.<br/>"
        "Thực chiến thiết kế linh kiện công suất: Điện trở suất của lớp bán dẫn quyết định trực tiếp điện trở nối tiếp ký sinh (series resistance <i>R</i><sub>s</sub>) của linh kiện. "
        "Trong các diode laser và transistor công suất cao, việc tối ưu hóa nồng độ pha tạp vùng đế và vùng tiếp xúc ohmic là yêu cầu sống còn "
        "để triệt tiêu sụt áp ký sinh và kiểm soát hiện tượng quá nhiệt phá hủy (thermal runaway)."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.4: PHƯƠNG PHÁP BỐN MŨI DÒ ĐO ĐIỆN TRỞ SUẤT
    # =========================================================================
    add_p("Luận điểm 2.1.4: Kỹ thuật bốn mũi dò đo điện trở suất (Four-Point Probe) và hệ số hiệu chỉnh hình học", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Để kiểm soát chất lượng màng mỏng bán dẫn và các phiến wafer sau công đoạn cấy ion pha tạp, người ta cần đo chính xác điện trở suất khối của lớp vật liệu.<br/>"
        "↳ Phương pháp bốn mũi dò (Four-Point Probe Method): Kỹ thuật đo điện trở suất màng mỏng bằng cách tách biệt độc lập mạch bơm dòng điện và mạch đo thế tĩnh điện."
    )
    add_spacer(6)
    
    # Embed Hình 2.8
    story.append(he.embed_figure_with_caption(
        fig_goc_2_8,
        "Hình 2.8: Sơ đồ nguyên lý kỹ thuật bốn mũi dò thẳng hàng cách đều khoảng cách <i>s</i> đo điện trở suất phiến bán dẫn mỏng bề dày <i>W</i> (Slide 10 HUST). "
        "Ba mắt xích vật lý: (a) Hai mũi dò ngoài (mũi 1 và 4) bơm dòng điện không đổi <i>I</i>; "
        "(b) Hai mũi dò trong (mũi 2 và 3) cảm nhận hiệu điện thế <i>V</i> với nội trở vôn kế vô cùng lớn; "
        "(c) Triệt tiêu hoàn toàn sụt áp trên điện trở tiếp xúc que đo và dây dẫn.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    add_p(
        "Nghịch lý que đo hai cực thông thường: Khi dùng đồng hồ vạn năng hai que đo thông thường để đo điện trở của một phiến Silicon đã pha tạp dẫn điện, "
        "giá trị hiển thị luôn lên tới hàng Megaohm hoặc dao động bất định. "
        "Sai số khổng lồ này xuất phát từ việc tiếp xúc kim loại &ndash; bán dẫn luôn hình thành hàng rào thế năng Schottky có điện trở tiếp xúc rất lớn. "
        "Dòng điện đo đi qua que đo gây sụt áp chủ yếu trên lớp tiếp xúc thay vì trên khối vật liệu. "
        "Làm thế nào phương pháp bốn mũi dò có thể loại bỏ 100% ảnh hưởng của điện trở tiếp xúc mà không cần chế tạo tiếp xúc Ohmic phức tạp?"
    )
    add_spacer(10)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    add_p(
        "Bí quyết của kỹ thuật bốn mũi dò nằm ở việc tách rời hoàn toàn đường đi của dòng điện và đường đo của điện thế. "
        "Nguồn dòng độc lập bơm dòng <i>I</i> qua hai mũi ngoài, trong khi vôn kế có trở kháng đầu vào cực cao (hàng Gigaohm) nối vào hai mũi trong, "
        "khiến dòng điện chạy qua tiếp xúc của mũi đo thế triệt tiêu về 0, loại bỏ hoàn toàn sụt thế tiếp xúc <i>I</i><sub>volt</sub><i>R</i><sub>contact</sub> = 0."
    )
    add_spacer(6)
    
    # Trụ cột Luận điểm 2.1.4
    nom_rows_4 = [
        ("Hiệu điện thế đo được", "<i>V</i>", "V", "Hiệu điện thế đo được giữa hai mũi dò trong (mũi 2 và 3) bằng vôn kế có nội trở cực lớn."),
        ("Dòng điện bơm", "<i>I</i>", "A", "Dòng điện một chiều ổn định được bơm qua hai mũi dò ngoài (mũi 1 và 4)."),
        ("Bề dày phiến bán dẫn", "<i>W</i>", "cm", "Chiều dày của phiến wafer hoặc lớp màng mỏng epitaxy cần đo đạc."),
        ("Hệ số hiệu chỉnh hình học", "<i>CF</i>", "1", "Hệ số không thứ nguyên bù trừ ảnh hưởng biên và kích thước hữu hạn của mẫu (<i>CF</i> &approx; 4,532 khi <i>d</i> / <i>s</i> &gt; 20).")
    ]
    story.append(he.build_target_equation_block(
        r"\rho = \frac{\pi}{\ln 2} W \left( \frac{V}{I} \right) \cdot CF \approx 4,532 W \left( \frac{V}{I} \right) \quad \text{với phiến mỏng } W \ll s",
        nom_rows_4,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng việc đo lưu lượng nước chảy qua một khúc sông có nhiều rong rêu bám chặt ở hai bờ. "
        "Nếu người đo thả một chiếc phao cản nước lớn xuống sông để đo lực đẩy, chính chiếc phao sẽ làm xáo trộn dòng chảy (điện trở tiếp xúc làm sai lệch phép đo). "
        "Kỹ thuật bốn mũi dò giống như việc dùng hai máy bơm công suất lớn đặt cách xa nhau để tạo dòng nước ổn định, "
        "sau đó thả nhẹ hai cảm biến áp suất siêu nhỏ không chạm đáy vào giữa lòng sông để đo chênh lệch thế nước mà không hề cản trở dòng chảy. "
        "Trong các dây chuyền sản xuất chip bán dẫn 300 mm, các máy đo bốn mũi dò tự động quét trên toàn bộ bề mặt phiến wafer để vẽ bản đồ đồng đều điện trở suất sau mỗi mẻ cấy ion."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Dẫn xuất giải tích thế tĩnh điện từ nguồn dòng điểm đối với mẫu bán vô hạn và phiến mỏng hữu hạn: "
        "Xét dòng điện <i>I</i> bơm vào bề mặt bán vô hạn qua mũi dò điểm tại gốc tọa độ. Do tính đối xứng cầu bán phần, mật độ dòng điện tại khoảng cách <i>r</i> tỷ lệ nghịch với diện tích mặt bán cầu 2&pi;<i>r</i><sup>2</sup>."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.1.4
    story.append(he.build_intermediate_equation(
        "Tích phân điện trường tĩnh điện từ khoảng cách <i>r</i> ra vô cùng cho điện thế tại một điểm trên bề mặt khối bán vô hạn:<br/>"
        "↳ Phân bố thế bán cầu (Hemispherical Potential Distribution): Thế tĩnh điện suy giảm tỷ lệ nghịch với khoảng cách từ nguồn dòng điểm.",
        r"V(r) = \int_r^\infty E\, dr = \int_r^\infty \frac{\rho I}{2 \pi r^2}\, dr = \frac{\rho I}{2 \pi r}",
        styles=styles,
        ocr_idx=4
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.1.4
    story.append(he.build_intermediate_equation(
        "Cộng thế từ nguồn dòng vào (+<i>I</i> tại mũi 1) và nguồn dòng ra (&minus;<i>I</i> tại mũi 4) lên hai mũi dò trong (mũi 2 và 3) cách đều <i>s</i>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hiệu điện thế giữa mũi 2 và mũi 3 đối với khối bán vô hạn có bề dày rất lớn (<i>W</i> &gg; <i>s</i>):",
        r"V = V_2 - V_3 = \frac{\rho I}{2 \pi} \left[ \left( \frac{1}{s} - \frac{1}{2s} \right) - \left( \frac{1}{2s} - \frac{1}{s} \right) \right] = \frac{\rho I}{2 \pi s} \implies \rho = 2 \pi s \left( \frac{V}{I} \right)",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.1.4
    story.append(he.build_intermediate_equation(
        "Đối với phiến mỏng có bề dày <i>W</i> &ll; <i>s</i>, dòng điện bị giới hạn lan truyền hai chiều theo hình trụ bán phần:<br/>"
        "↳ [Hệ thức Đích & Quy ước Dấu Đại số]: Phương pháp ảnh điện tích và tích phân hai chiều dẫn xuất hệ số chuẩn xấp xỉ 4,532:",
        r"\rho = \left( \frac{\pi}{\ln 2} \right) W \left( \frac{V}{I} \right) \cdot CF = 4,532 W \left( \frac{V}{I} \right) \cdot CF",
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(10)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Khảo sát các giới hạn hình học mẫu đo: Khi bề dày phiến rất lớn so với khoảng cách mũi dò (<i>W</i> &gg; <i>s</i>), "
        "điện trường phân bố theo hình cầu ba chiều, điện trở suất <i>&rho;</i> tỷ lệ thuận với tích của khoảng cách <i>s</i> và tỷ số thế trên dòng <i>V</i> trên <i>I</i>, hoàn toàn không phụ thuộc vào bề dày <i>W</i>. "
        "Ngược lại khi đo các lớp màng mỏng hay vùng cấy ion nông (<i>W</i> &ll; <i>s</i>), điện trường bị ép phẳng thành hai chiều, "
        "điện trở suất tỷ lệ thuận với bề dày <i>W</i>. "
        "Hệ số hiệu chỉnh hình học <i>CF</i> phụ thuộc vào tỷ số giữa đường kính mẫu <i>d</i> và khoảng cách mũi dò <i>s</i> &mdash; khi tỷ số này lớn hơn 20, "
        "<i>CF</i> hội tụ về 1 và hệ số 4,532 trở thành hằng số chuẩn tuyệt đối.<br/>"
        "Điện trở lớp mỏng (Sheet Resistance <i>R</i><sub>sq</sub>): Trong thực tế chế tạo vi điện tử, người ta thường sử dụng đại lượng điện trở lớp mỏng "
        "<i>R</i><sub>sq</sub> bằng điện trở suất chia cho bề dày <i>W</i>, với đơn vị là Ohm trên một ô vuông (&Omega;&middot;sq<sup>-1</sup>). "
        "Đại lượng này cho phép kỹ sư đánh giá trực tiếp chất lượng lớp dẫn điện mà không cần đo chính xác bề dày vật lý của lớp màng."
    )
    add_spacer(14)

    # =========================================================================
    # LUẬN ĐIỂM 2.1.5: HIỆU ỨNG HALL VÀ XÁC ĐỊNH LOẠI HẠT TẢI
    # =========================================================================
    add_p("Luận điểm 2.1.5: Hiệu ứng Hall, lực từ Lorentz, hệ số Hall và phương pháp xác định nồng độ, dấu hạt tải", "H2")
    add_spacer(4)
    
    # KHỐI 1
    add_p("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu (Concept Introduction & Visual Anchor)", "H3")
    add_p(
        "Năm 1879, nhà vật lý người Mỹ Edwin Hall phát hiện ra rằng khi đặt một thanh dẫn điện có dòng điện chạy qua vào trong một từ trường vuông góc, "
        "giữa hai mặt bên của thanh sẽ xuất hiện một hiệu điện thế ngang.<br/>"
        "↳ Hiệu ứng Hall (Hall Effect): Hiện tượng xuất hiện điện trường ngang vuông góc với cả véctơ mật độ dòng điện và véctơ cảm ứng từ ngoài do tác dụng của lực từ Lorentz.<br/>"
        "Đây là một trong những phát kiến thực nghiệm vĩ đại nhất của vật lý chất rắn, cung cấp bằng chứng thực nghiệm không thể chối cãi "
        "về sự tồn tại độc lập của lỗ trống mang điện tích dương trong chất bán dẫn."
    )
    add_spacer(6)
    
    # Embed Hình 2.11 & 2.12
    story.append(he.embed_figure_with_caption(
        fig_goc_2_11,
        "Hình 2.11: Sơ đồ nguyên lý hiệu ứng Hall trong bán dẫn loại p dưới tác dụng của lực từ Lorentz (Slide 12 HUST). "
        "Ba mắt xích vật lý: (a) Lỗ trống trôi dọc trục <i>x</i> bị bẻ cong về phía mặt trước (trục <i>y</i>); "
        "(b) Tích tụ điện tích dương tại mặt trước sinh ra điện trường Hall <i>E</i><sub>y</sub> hướng từ trước ra sau; "
        "(c) Cân bằng động học triệt tiêu dòng điện ngang ở trạng thái dừng.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    story.append(he.embed_figure_with_caption(
        fig_goc_2_12,
        "Hình 2.12: Sơ đồ mạch phân cực đo điện áp Hall <i>V</i><sub>H</sub> trong mẫu bán dẫn có kích thước xác định (Slide 13 HUST). "
        "Dòng điện <i>I</i> chạy dọc trục <i>x</i>, từ trường <i>B</i><sub>z</sub> đặt dọc trục <i>z</i>, điện áp Hall <i>V</i><sub>H</sub> đo dọc trục <i>y</i>.",
        kind="orig",
        styles=styles
    ))
    add_spacer(6)
    
    add_p(
        "Nghịch lý lực Lorentz và cực tính điện áp Hall: Lực từ Lorentz tác dụng lên điện tích chuyển động luôn tuân theo quy tắc bàn tay trái <i>F</i> = <i>q</i>(<i>v</i> &times; <i>B</i>). "
        "Xét bán dẫn loại n: electron mang điện tích âm &minus;<i>q</i> chuyển động ngược chiều điện trường (ngược chiều trục <i>x</i>) trong từ trường <i>B</i><sub>z</sub> hướng lên. "
        "Lực từ Lorentz bẻ cong electron về phía mặt bên <i>y</i>. "
        "Bây giờ xét bán dẫn loại p: lỗ trống mang điện tích dương +<i>q</i> chuyển động cùng chiều điện trường (cùng chiều trục <i>x</i>). "
        "Điều kỳ lạ là lực từ Lorentz vẫn đẩy các lỗ trống về cùng một phía mặt bên <i>y</i> như electron! "
        "Nếu cả electron và lỗ trống đều bị bẻ cong dạt về cùng một bên của thanh bán dẫn, tại sao điện áp Hall đo được giữa hai cạnh bên lại có thể đảo dấu hoàn toàn đối lập giữa bán dẫn loại p và bán dẫn loại n?"
    )
    add_spacer(10)
    
    # KHỐI 2
    add_p("Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý (Minimal Working Example & Physical Core)", "H3")
    add_p(
        "Mặc dù lực từ Lorentz uốn cong cả hai loại hạt về cùng một phía của thanh bán dẫn, điện tích mà chúng mang theo lại hoàn toàn trái dấu. "
        "Sự tích tụ electron làm mặt bên tích điện âm sinh ra điện áp Hall âm, trong khi sự tích tụ lỗ trống làm mặt bên tích điện dương sinh ra điện áp Hall dương. "
        "Ở trạng thái dừng tĩnh tại, sự tích tụ điện tích ở hai cạnh bên tạo ra điện trường Hall <i>E</i><sub>y</sub>, sinh lực điện trường cân bằng chính xác với lực từ Lorentz: "
        "<i>qE</i><sub>y</sub> = <i>qv</i><sub>x</sub><i>B</i><sub>z</sub>."
    )
    add_spacer(6)
    
    # Trụ cột Luận điểm 2.1.5
    nom_rows_5 = [
        ("Điện áp Hall", "<i>V</i><sub>H</sub>", "V", "Hiệu điện thế xuất hiện giữa hai bề mặt đối diện theo phương vuông góc với cả dòng điện và từ trường."),
        ("Hệ số Hall", "<i>R</i><sub>H</sub>", "cm<sup>3</sup>&middot;C<sup>-1</sup>", "Tham số vật liệu định lượng độ lớn và cực tính của điện trường Hall sinh ra trên một đơn vị dòng và cảm ứng từ."),
        ("Cảm ứng từ ngoài", "<i>B</i><sub>z</sub>", "T", "Độ lớn véctơ cảm ứng từ đặt vuông góc với mặt phẳng dẫn dòng (1 Wb&middot;cm<sup>-2</sup> = 10<sup>4</sup> T)."),
        ("Bề dày theo phương từ trường", "<i>W</i>", "cm", "Kích thước hình học của thanh bán dẫn đo dọc theo phương của véctơ từ trường ngoài.")
    ]
    story.append(he.build_target_equation_block(
        r"E_y = R_{\mathrm{H}} J_x B_z \implies V_{\mathrm{H}} = \frac{R_{\mathrm{H}} I_x B_z}{W} \quad \text{với} \quad R_{\mathrm{H}} = \frac{1}{q p} \text{ (loại p)} \quad \text{và} \quad R_{\mathrm{H}} = -\frac{1}{q n} \text{ (loại n)}",
        nom_rows_5,
        styles=styles
    ))
    add_spacer(8)
    
    add_p(
        "Ẩn dụ cơ học vĩ mô khóa biến số ba nhịp: Hãy tưởng tượng một đoàn tàu thủy đang di chuyển dọc theo một con kênh đào hẹp và có một luồng gió bão thổi tạt ngang từ bờ trái sang bờ phải (lực Lorentz). "
        "Tất cả các con tàu đều bị dạt tấp vào bờ bên phải. "
        "Nếu đoàn tàu chở toàn bộ là các thùng sơn màu xanh (lỗ trống tích điện dương), bờ phải sẽ nhuộm một màu xanh rực rỡ làm xuất hiện điện thế dương. "
        "Nếu đoàn tàu chở các thùng sơn màu đỏ nhưng đang chạy lùi ngược chiều (electron mang điện âm chuyển động ngược chiều dòng điện), luồng gió bão vẫn tạt con tàu về bờ bên phải, "
        "nhưng lúc này bờ phải lại bị nhuộm một màu đỏ rực rỡ làm xuất hiện điện thế âm. "
        "Bằng cách cắm hai đầu que đo vào hai bên bờ kênh đào, màu sơn (loại hạt dẫn) và số lượng tàu (nồng độ hạt tải) được nhận diện chuẩn xác 100% mà không cần phải chặn đứng đoàn tàu lại."
    )
    add_spacer(10)
    
    # KHỐI 3
    add_p("Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước (Guided Practice & Step-by-Step Derivation)", "H3")
    add_p(
        "Dẫn xuất giải tích điều kiện cân bằng Lorentz và tính toán số học chi tiết Bài tập Thí dụ 3 (Slide 14 HUST): "
        "Một mẫu Silicon loại n pha tạp Phosphorous với nồng độ 10<sup>16</sup> cm<sup>-3</sup> có diện tích tiết diện ngang <i>A</i> = 0,0025 cm<sup>2</sup>, "
        "dòng điện <i>I</i> = 1 mA, cảm ứng từ ngoài <i>B</i><sub>z</sub> = 10<sup>-4</sup> Wb&middot;cm<sup>-2</sup> (tương đương 1 T). "
        "Tính toán điện áp Hall <i>V</i><sub>H</sub> trong hai trường hợp bề dày mẫu <i>W</i> = 300 &mu;m và <i>W</i> = 500 &mu;m."
    )
    add_spacer(6)
    
    # Bước biến đổi trung gian 1 MPT 2.1.5
    story.append(he.build_intermediate_equation(
        "Thiết lập điều kiện triệt tiêu lực tổng hợp tác dụng lên hạt tải theo phương ngang trục <i>y</i>:<br/>"
        "↳ Cân bằng lực Lorentz (Lorentz Force Balance): Trạng thái cân bằng động lực học giữa lực điện trường Hall và lực từ trường.",
        r"F_y = q (E_y - v_x B_z) = 0 \implies E_y = v_x B_z",
        styles=styles,
        ocr_idx=4
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 2 MPT 2.1.5
    story.append(he.build_intermediate_equation(
        "Liên hệ giữa vận tốc trôi <i>v</i><sub>x</sub> và mật độ dòng điện <i>J</i><sub>x</sub> qua tiết diện ngang <i>A</i>:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu diễn điện trường Hall theo dòng điện và nồng độ hạt tải:",
        r"J_x = -q n v_x \implies v_x = -\frac{J_x}{q n} = -\frac{I}{q n A} \implies E_y = -\left( \frac{1}{q n} \right) \frac{I B_z}{A} = R_{\mathrm{H}} \frac{I B_z}{A}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 3 MPT 2.1.5
    story.append(he.build_intermediate_equation(
        "Tính toán hệ số Hall <i>R</i><sub>H</sub> của mẫu Silicon loại n pha 10<sup>16</sup> cm<sup>-3</sup> Phosphorous:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Cực tính âm của hệ số Hall khẳng định hạt tải đa số là electron:",
        r"R_{\mathrm{H}} = -\frac{1}{q n} = -\frac{1}{(1,602 \times 10^{-19}\ \mathrm{C}) \times (10^{16}\ \mathrm{cm}^{-3})} \approx -624,2\ \mathrm{cm}^3\cdot\mathrm{C}^{-1}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 4 MPT 2.1.5
    story.append(he.build_intermediate_equation(
        "Tính toán điện áp Hall <i>V</i><sub>H</sub> đối với trường hợp bề dày mẫu <i>W</i> = 300 &mu;m = 0,03 cm:<br/>"
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay số trực tiếp với dòng <i>I</i> = 1 mA = 10<sup>-3</sup> A và cảm ứng từ <i>B</i><sub>z</sub> = 10<sup>-4</sup> Wb&middot;cm<sup>-2</sup>:",
        r"V_{\mathrm{H}} = \frac{R_{\mathrm{H}} I B_z}{W} = \frac{(-624,2\ \mathrm{cm}^3\cdot\mathrm{C}^{-1}) \times (10^{-3}\ \mathrm{A}) \times (10^{-4}\ \mathrm{Wb}\cdot\mathrm{cm}^{-2})}{0,03\ \mathrm{cm}} \approx -2,08 \times 10^{-3}\ \mathrm{V} = -2,08\ \mathrm{mV}",
        styles=styles,
        is_expanded_from_slide=True
    ))
    add_spacer(6)
    
    # Bước biến đổi trung gian 5 MPT 2.1.5
    story.append(he.build_intermediate_equation(
        "Tính toán điện áp Hall <i>V</i><sub>H</sub> đối với trường hợp bề dày mẫu <i>W</i> = 500 &mu;m = 0,05 cm:<br/>"
        "↳ [Hệ thức Đích & Quy ước Dấu Đại số]: Điện áp Hall tỷ lệ nghịch với bề dày mẫu <i>W</i> theo phương từ trường:",
        r"V_{\mathrm{H}} = \frac{R_{\mathrm{H}} I B_z}{W} = \frac{(-624,2\ \mathrm{cm}^3\cdot\mathrm{C}^{-1}) \times (10^{-3}\ \mathrm{A}) \times (10^{-4}\ \mathrm{Wb}\cdot\mathrm{cm}^{-2})}{0,05\ \mathrm{cm}} \approx -1,25 \times 10^{-3}\ \mathrm{V} = -1,25\ \mathrm{mV}",
        styles=styles,
        ocr_idx=5
    ))
    add_spacer(8)
    
    # Embed Hình mô phỏng 2.2
    story.append(he.embed_figure_with_caption(
        fig_sim_2,
        "Hình mô phỏng 2.2: Đặc tuyến đo kiểm hiệu ứng Hall và cơ chế đảo dấu hệ số Hall theo nhiệt độ chuẩn MATLAB R2014b+ (Lab Quang điện tử HUST). "
        "(a) Điện áp Hall <i>V</i><sub>H</sub> theo cảm ứng từ <i>B</i><sub>z</sub> từ 0 đến 2 T: độ dốc đường thẳng xác định trực tiếp hệ số Hall và nồng độ hạt tải; "
        "(b) Hiện tượng đảo dấu hệ số Hall <i>R</i><sub>H</sub> trong bán dẫn loại p khi tăng nhiệt độ: sự bùng nổ nồng độ hạt tải nội tại <i>n</i><sub>i</sub>(<i>T</i>) "
        "kết hợp với độ linh động electron vượt trội (<i>&mu;</i><sub>n</sub> &gt; <i>&mu;</i><sub>p</sub>) làm hệ số Hall đổi từ cực tính dương sang cực tính âm tại nhiệt độ nghịch đảo <i>T</i><sub>inv</sub>.",
        kind="sim",
        styles=styles
    ))
    add_spacer(10)
    
    # KHỐI 4
    add_p("Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật (Variations & Asymptotic Sweep)", "H3")
    add_p(
        "Mô hình hai hạt tải và hiện tượng đảo dấu hệ số Hall: Trong trường hợp tổng quát bán dẫn chứa đồng thời cả electron và lỗ trống, "
        "hệ số Hall tổng hợp được xác định bằng công thức hai hạt tải:"
    )
    add_spacer(4)
    story.append(he.build_intermediate_equation(
        "Hệ thức hệ số Hall tổng quát cho bán dẫn chứa đồng thời cả hai loại hạt tải mang điện tích trái dấu:<br/>"
        "↳ Hệ số Hall hai hạt tải (Two-Carrier Hall Coefficient): Mối quan hệ vi mô tính đến sự cạnh tranh độ linh động giữa electron và lỗ trống.",
        r"R_{\mathrm{H}} = \frac{p \mu_p^2 - n \mu_n^2}{q (p \mu_p + n \mu_n)^2}",
        styles=styles,
        ocr_idx=4
    ))
    add_spacer(6)
    add_p(
        "Do độ linh động của electron <i>&mu;</i><sub>n</sub> luôn lớn hơn đáng kể so với <i>&mu;</i><sub>p</sub> (tỷ số độ linh động <i>b</i> xấp xỉ 3 trong Silicon), "
        "đại lượng <i>n&mu;</i><sub>n</sub><sup>2</sup> có thể vượt qua <i>p&mu;</i><sub>p</sub><sup>2</sup> ngay cả khi nồng độ lỗ trống <i>p</i> lớn hơn nồng độ electron <i>n</i>. "
        "Khi nhiệt độ thanh bán dẫn tăng cao, nồng độ hạt tải nội tại <i>n</i><sub>i</sub>(<i>T</i>) tăng vọt theo hàm số mũ, khiến hệ số Hall của bán dẫn loại p bị đảo dấu từ dương sang âm tại nhiệt độ nghịch đảo <i>T</i><sub>inv</sub>.<br/>"
        "Ứng dụng cảm biến Hall trong công nghiệp quân sự và tự động hóa: Hiệu ứng Hall là nguyên lý hoạt động của các cảm biến đo từ trường siêu nhạy, "
        "cảm biến đo vị trí góc quay không tiếp xúc trong hệ thống dẫn đường quán tính của tên lửa, động cơ phản lực, "
        "và cảm biến đo dòng điện công suất lớn cách ly galvanic an toàn tuyệt đối trong các hệ thống điện cao thế."
    )
    add_spacer(14)

    # =========================================================================
    # KHỐI 5: THỬ THÁCH CHẨN ĐOÁN CER (HỘI TỤ CUỐI TỆP)
    # =========================================================================
    add_p("Giai đoạn 5: Thử thách tự luyện và dự đoán lỗi sai kỹ thuật (Student Challenges & Error Anticipation)", "H2")
    add_spacer(4)
    add_p(
        "Khối thử thách chẩn đoán độc lập (Claim &ndash; Evidence &ndash; Reasoning): Bẫy điểm mù kỹ thuật thực chiến trong Lab và phòng sạch. "
        "Học viên Bùi Trung Dũng tiếp nhận phân tích bản chất vi mô bằng nguyên lý đầu, tuyệt đối không đoán mò theo cảm tính."
    )
    add_spacer(6)
    
    # Ca chẩn đoán 1
    add_p(
        "<b>Ca chẩn đoán 1: Bẫy điểm mù đảo dấu điện áp Hall trong bán dẫn bù tạp chất.</b><br/>"
        "Một kỹ sư phòng sạch tiến hành đo hiệu ứng Hall trên một phiến bán dẫn Silicon được pha tạp bù đồng thời cả Donors (Phosphorous: <i>N</i><sub>D</sub> = 2 &times; 10<sup>16</sup> cm<sup>-3</sup>) "
        "và Acceptors (Boron: <i>N</i><sub>A</sub> = 1,6 &times; 10<sup>16</sup> cm<sup>-3</sup>) ở nhiệt độ phòng 300 K. "
        "Sau khi đo, kỹ sư quan sát thấy điện áp Hall mang cực tính âm và kết luận chắc chắn rằng phiến Silicon này sẽ luôn thể hiện tính chất dẫn điện của bán dẫn loại n ở mọi dải nhiệt độ "
        "vì nồng độ donor luôn lớn hơn acceptor (<i>N</i><sub>D</sub> &gt; <i>N</i><sub>A</sub>).<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Sử dụng hệ thức hệ số Hall hai hạt tải và cơ chế bẫy hạt tải nhiệt độ thấp (carrier freeze-out), "
        "hãy phân tích xem khi hạ nhiệt độ xuống dải nhiệt độ siêu thấp (<i>T</i> &lt; 50 K) hoặc khi nâng nhiệt độ lên vùng dẫn nội tại (<i>T</i> &gt; 600 K), "
        "kết luận của kỹ sư trên có còn chuẩn xác hay không? Điều kiện định lượng nào sẽ làm điện áp Hall bị triệt tiêu hoàn toàn về 0?",
        "Body"
    )
    add_spacer(8)
    
    # Ca chẩn đoán 2
    add_p(
        "<b>Ca chẩn đoán 2: Nghịch lý độ linh động trong cấu trúc dị thể điều chế pha tạp HEMT.</b><br/>"
        "Khi đo độ linh động hạt tải trong một lớp bán dẫn GaAs khối đồng nhất pha tạp <i>N</i><sub>D</sub> = 10<sup>18</sup> cm<sup>-3</sup> ở 77 K (nhiệt độ Nitơ lỏng), "
        "độ linh động đo được rất thấp, chỉ đạt khoảng 2500 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> do tán xạ ion tạp chất Coulomb chiếm ưu thế. "
        "Tuy nhiên, khi đưa cùng một mật độ electron đó vào một kênh dẫn dị thể GaAs không pha tạp kẹp giữa hai lớp rào AlGaAs pha tạp donor (cấu trúc 2DEG trong transistor HEMT), "
        "độ linh động đo được ở 77 K vọt lên tới hơn 200.000 cm<sup>2</sup>&middot;V<sup>-1</sup>&middot;s<sup>-1</sup> &mdash; tăng gần 100 lần so với vật liệu khối.<br/>"
        "↳ <i>Nhiệm vụ phản biện:</i> Áp dụng quy tắc cộng nghịch đảo Matthiessen và thế tương tác Coulomb vi mô, "
        "hãy giải trình cơ chế vật lý nào cho phép nén mật độ electron cực cao mà lại triệt tiêu được hoàn toàn tán xạ ion tạp chất trong cấu trúc khí electron hai chiều (2DEG)?",
        "Body"
    )
    add_spacer(14)
    
    # Pre-flight build
    print("Pre-flight build starting...")
    doc.build(story)
    print(f"SUCCESS: Generated {TARGET_PDF}")
    
    # Post-build assertion
    res = he.assert_monograph_compliance(TARGET_PDF, story, require_5_blocks=True, min_pages=15)
    print("POST-BUILD ASSERTION PASS 100%:", res)
    return TARGET_PDF

if __name__ == "__main__":
    build_monograph_muc_2_1()

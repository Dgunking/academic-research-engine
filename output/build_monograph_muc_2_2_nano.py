# -*- coding: utf-8 -*-
"""
HUST Monograph PDF Typesetting Script
Chương 2: Bản chất lượng tử của thế giới nano
Mục 2.2: Lưỡng tính sóng - hạt của bức xạ và vật chất (Slide 13–19)
Sinh viên: Bùi Trung Dũng (ĐHBK Hà Nội - HUST)
"""

import os
import sys
import tempfile
import shutil

# Thêm đường dẫn thư viện hust_pdf_engine
engine_dir = r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts"
if engine_dir not in sys.path:
    sys.path.insert(0, engine_dir)

import hust_pdf_engine as he
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib import colors

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding="utf-8")

def build_pdf():
    # 1. Đường dẫn thư mục & tệp đích
    drive_base = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano"
    kho_anh = os.path.join(drive_base, "Kho_Hinh_Anh")
    bai_giang = os.path.join(drive_base, "Bai_Giang_Dong_Goi")
    os.makedirs(bai_giang, exist_ok=True)
    target_pdf = os.path.join(bai_giang, "Chuyen_Khao_Nano_Muc_2.2.pdf")

    print(f"Bắt đầu biên dịch chuyên khảo Mục 2.2: {target_pdf}")

    # 2. Khởi tạo Styles và Document Template
    styles = he.get_hust_styles()
    doc = he.BookmarkDocTemplate(target_pdf)
    story = []

    # =========================================================================
    # TIÊU ĐỀ ĐẦU CHUYÊN KHẢO (H1)
    # =========================================================================
    title_main = (
        "CHƯƠNG 2: BẢN CHẤT LƯỢNG TỬ CỦA THẾ GIỚI NANO<br/>"
        "MỤC 2.2: LƯỠNG TÍNH SÓNG - HẠT CỦA BỨC XẠ VÀ VẬT CHẤT"
    )
    story.append(he.make_paragraph(title_main, styles["H1"]))
    story.append(Spacer(1, 4))

    meta_info = (
        "<b>Hệ Thống Chuyên Khảo Giảng Dạy &amp; Nghiên Cứu Vật Lý Nano — ĐHBK Hà Nội</b><br/>"
        "<i>Chủ thể nghiên cứu:</i> Bùi Trung Dũng — Khoa Vật lý Kỹ thuật, Trường Đại học Bách khoa Hà Nội (HUST)<br/>"
        "<i>Tài liệu nguồn kép:</i> Bài giảng 'Bài 2-Quantum nature.pdf' (Slide 13–19), Bộ môn Vật liệu Điện tử — Viện Vật lý Kỹ thuật HUST; "
        "kết hợp các chuyên khảo quốc tế đỉnh cao: Poole &amp; Owens (<i>Introduction to Nanotechnology</i>), Wolf (<i>Nanophysics</i>), "
        "Beiser (<i>Concepts of Modern Physics</i>)."
    )
    story.append(he.make_paragraph(meta_info, styles["Body"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=he.COLOR_PRIMARY, spaceBefore=4, spaceAfter=10))

    # =========================================================================
    # LỜI NÓI ĐẦU ĐỊNH VỊ HỌC THUẬT & TỔNG QUAN
    # =========================================================================
    overview_text = (
        "<b>Lời nói đầu định vị học thuật:</b> Khái niệm lưỡng tính sóng - hạt (Wave-Particle Duality) là bước ngoặt nhận thức cách mạng "
        "đặt nền tảng cho sự hình thành của cơ học lượng tử hiện đại. Trong suốt thế kỷ XIX, quang học sóng của Huygens, Young, Fresnel "
        "và lý thuyết điện từ cổ điển của Maxwell đã thống trị vật lý với niềm tin tuyệt đối rằng ánh sáng thuần túy là sóng điện từ lan truyền liên tục. "
        "Tuy nhiên, khi bước sang đầu thế kỷ XX, sự bế tắc hoàn toàn của thuyết sóng trước bức xạ vật đen, hiệu ứng quang điện ngoài và tán xạ Compton "
        "đã buộc các nhà vật lý phải thừa nhận rằng bức xạ điện từ còn sở hữu các tính chất hạt gián đoạn (photon mang năng lượng <i>E</i> = <i>hν</i> "
        "và động lượng <i>p</i> = <i>h</i>·<i>λ</i><sup>−1</sup>). Đỉnh cao của sự phát triển này là giả thuyết thiên tài của Louis de Broglie (1924): "
        "nếu bức xạ sóng có bản chất hạt, thì các thực thể vật chất có khối lượng (electron, proton, nguyên tử) cũng bắt buộc phải sở hữu bản chất sóng liên kết. "
        "Chuyên khảo Mục 2.2 bóc tách trọn vẹn 5 Luận điểm Vi mô (MPT) theo chuẩn mực sư phạm 5 giai đoạn lũy tiến, "
        "dẫn xuất tường minh từng phương trình từ nguyên lý đầu, đối chiếu thực nghiệm lịch sử và mô phỏng giải tích kỹ thuật chuẩn MATLAB R2014b+."
    )
    story.append(he.make_paragraph(overview_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # =========================================================================
    # LUẬN ĐIỂM 2.2.1: LƯỠNG TÍNH SÓNG - HẠT CỦA BỨC XẠ ĐIỆN TỪ & HIỆU ỨNG QUANG ĐIỆN
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.2.1: Lưỡng tính sóng - hạt của bức xạ điện từ &amp; Hiệu ứng quang điện", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g1_p1 = (
        "Hiệu ứng quang điện ngoài (Photoelectric Effect) được phát hiện lần đầu tiên bởi Heinrich Hertz năm 1887 và được Philipp Lenard nghiên cứu định lượng năm 1902. "
        "Khi chiếu một chùm bức xạ điện từ có bước sóng thích hợp vào bề mặt kim loại đặt trong bình chân không cao, các electron dẫn trong kim loại hấp thụ năng lượng "
        "và bứt ra khỏi bề mặt, tạo thành dòng quang điện chạy về phía cực anot dưới tác dụng của điện trường gia tốc. "
        "Thực nghiệm đã xác lập ba quy luật cơ bản không thể bác bỏ:<br/>"
        "1. <i>Quy luật về giới hạn quang điện:</i> Đối với mỗi kim loại xác định, chỉ khi tần số bức xạ tới <i>ν</i> lớn hơn hoặc bằng một tần số ngưỡng <i>ν</i><sub>0</sub> "
        "(tương ứng bước sóng <i>λ</i> ≤ <i>λ</i><sub>0</sub>) thì hiệu ứng quang điện mới xảy ra, hoàn toàn không phụ thuộc vào cường độ chùm sáng tới.<br/>"
        "2. <i>Quy luật về động năng ban đầu cực đại:</i> Động năng ban đầu cực đại của quang electron bứt ra phụ thuộc tuyến tính vào tần số bức xạ tới <i>ν</i>, "
        "và tuyệt đối không phụ thuộc vào cường độ bức xạ tới.<br/>"
        "3. <i>Quy luật về tính tức thời:</i> Dòng quang điện xuất hiện gần như tức thì ngay khi chiếu sáng, với thời gian trễ đo được nhỏ hơn 10<sup>−9</sup> s, "
        "ngay cả khi cường độ bức xạ tới cực kỳ yếu."
    )
    story.append(he.make_paragraph(g1_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc sơ đồ thí nghiệm quang điện
    img_pe = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_01_So_Do_Thi_Nghiem_Quang_Dien.png")
    cap_pe = "Hình 2.2.1: Sơ đồ bố trí thí nghiệm hiệu ứng quang điện ngoài, mạch đo dòng quang điện và điện thế hãm triệt tiêu Uh."
    story.append(he.embed_figure_with_caption(img_pe, cap_pe, kind="orig", styles=styles))

    pe_ocr_1 = "Tế bào quang điện hình cầu bằng thủy tinh thạch anh hút chân không cao nhằm loại bỏ sự tán xạ va chạm của electron với phân tử khí."
    pe_ocr_2 = "Điện cực catot K phủ kim loại kiềm nhạy quang tiếp nhận chùm photon tới; điện cực anot A hình vành khuyên thu gom quang electron."
    pe_ocr_3 = "Mạch điện phân cực đổi chiều cho phép đặt hiệu điện thế gia tốc thuận (VA > VK) hoặc hiệu điện thế cản hãm (VA < VK)."
    pe_ocr_4 = "Điện kế micro-ampe kế G đo dòng quang điện cực nhạy; vôn kế đo chính xác giá trị hiệu điện thế hãm Uh khi dòng quang điện triệt tiêu về 0."
    pe_ocr_5 = "Chùm ánh sáng đơn sắc tới được lọc lựa chuẩn xác qua lăng kính đơn sắc sắc ký nhằm kiểm soát tuyệt đối tần số dao động nu."
    story.append(he.make_paragraph(pe_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(pe_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(pe_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(pe_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(pe_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g1_p2 = (
        "<b>Hạt nhân vật lý — Thuyết lượng tử ánh sáng Einstein (1905):</b> Albert Einstein đã giải quyết triệt để sự bế tắc của vật lý cổ điển "
        "bằng giả thuyết cách mạng: Bức xạ điện từ không chỉ phát xạ và hấp thụ theo từng lượng tử gián đoạn (như Planck đề xuất năm 1900), "
        "mà bản thân chùm sáng được cấu tạo từ các gói năng lượng định xứ trong không gian gọi là <i>lượng tử ánh sáng</i> hay <i>photon</i>. "
        "Mỗi photon mang năng lượng tỉ lệ với tần số <i>E</i> = <i>hν</i>. Quá trình quang điện là tương tác va chạm đơn hạt 1:1 "
        "giữa một photon duy nhất và một electron liên kết trong mạng kim loại. Toàn bộ năng lượng của photon được chuyển giao tức thời cho electron."
    )
    story.append(he.make_paragraph(g1_p2, styles["Body"]))

    eq_pe = r"h\nu = A_{\mathrm{exit}} + E_{k,\mathrm{max}} = e\Phi + \frac{1}{2}m_0 v_{\mathrm{max}}^2 = e\Phi + e U_h"
    nom_pe = [
        ("Năng lượng photon tới", "<i>hν</i>", "eV", "Gói năng lượng gián đoạn của lượng tử ánh sáng tới bề mặt kim loại"),
        ("Công thoát của kim loại", "<i>A</i><sub>exit</sub> = <i>eΦ</i>", "eV", "Năng lượng tối thiểu cần cung cấp để giải phóng electron khỏi liên kết mạng"),
        ("Động năng ban đầu cực đại", "<i>E</i><sub>k,max</sub>", "eV", "Động năng lớn nhất của quang electron ngay sau khi bứt ra khỏi bề mặt catot"),
        ("Hiệu điện thế hãm triệt tiêu", "<i>U</i><sub>h</sub>", "V", "Điện thế ngược cực tiểu đặt giữa anot và catot để triệt tiêu dòng quang điện"),
        ("Khối lượng electron", "<i>m</i><sub>0</sub>", "kg", "Hằng số CODATA 2022: 9.1093837 × 10<sup>−31</sup> kg"),
        ("Hằng số Planck", "<i>h</i>", "J·s", "Hằng số phổ quát lượng tử: 6.62607015 × 10<sup>−34</sup> J·s")
    ]
    story.append(he.build_target_equation_block(eq_pe, nom_pe, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    pe_step1_txt = (
        "Thiết lập định luật bảo toàn năng lượng cho biến cố hấp thụ photon đơn lẻ. Khi photon năng lượng <i>hν</i> va chạm với electron liên kết, "
        "một phần năng lượng tiêu tốn để thắng lực liên kết mạng tinh thể (công thoát <i>A</i><sub>exit</sub>), phần năng lượng dư thừa chuyển hóa "
        "thành động năng chuyển động của electron. Đối với các electron nằm ngay sát bề mặt catot (không bị mất năng lượng do va chạm thứ cấp trong lòng khối), "
        "động năng thu được đạt giá trị cực đại:"
    )
    pe_step1_eq = r"E_{k,\mathrm{max}} = \frac{1}{2}m_0 v_{\mathrm{max}}^2 = h\nu - A_{\mathrm{exit}}"
    story.append(he.build_intermediate_equation(pe_step1_txt, pe_step1_eq, styles=styles, is_expanded_from_slide=True))

    pe_step2_txt = (
        "Xác định điều kiện biên để hiệu ứng quang điện xảy ra. Vì động năng của electron không thể nhận giá trị âm, điều kiện tồn tại quang electron "
        "đòi hỏi <i>E</i><sub>k,max</sub> ≥ 0. Từ đó suy ra tần số ngưỡng quang điện <i>ν</i><sub>0</sub> và bước sóng giới hạn quang điện <i>λ</i><sub>0</sub>:"
    )
    pe_step2_eq = r"h\nu \ge A_{\mathrm{exit}} \implies \nu \ge \nu_0 = \frac{A_{\mathrm{exit}}}{h} \quad \text{hoặc} \quad \lambda \le \lambda_0 = \frac{hc}{A_{\mathrm{exit}}}"
    story.append(he.build_intermediate_equation(pe_step2_txt, pe_step2_eq, styles=styles, is_expanded_from_slide=True))

    pe_step3_txt = (
        "Dẫn xuất hệ thức điện thế hãm triệt tiêu <i>U</i><sub>h</sub>. Khi đặt điện thế ngược <i>U</i><sub>AK</sub> = −<i>U</i><sub>h</sub> &lt; 0, "
        "lực điện trường thực hiện công cản <i>eU</i><sub>h</sub> làm giảm động năng của electron. Dòng quang điện triệt tiêu hoàn toàn khi công cản "
        "triệt tiêu toàn bộ động năng ban đầu cực đại của electron nhanh nhất:"
    )
    pe_step3_eq = r"e U_h = E_{k,\mathrm{max}} = h\nu - A_{\mathrm{exit}} \implies U_h = \left(\frac{h}{e}\right)\nu - \frac{A_{\mathrm{exit}}}{e} = \left(\frac{h}{e}\right)\nu - \Phi"
    story.append(he.build_intermediate_equation(pe_step3_txt, pe_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g1_p4 = (
        "<b>Phân tích tiệm cận và ý nghĩa thực nghiệm của hệ thức Millikan:</b><br/>"
        "• <i>Trường hợp ν &lt; ν<sub>0</sub> (Dưới ngưỡng):</i> Động năng tính toán sẽ cho giá trị âm, điều không thể xảy ra trong vật lý thực. "
        "Do đó, dù cường độ chùm sáng tới có tăng lên hàng triệu lần (mật độ photon cực lớn), hiệu ứng quang điện ngoài vẫn hoàn toàn không xảy ra.<br/>"
        "• <i>Trường hợp ν ≥ ν<sub>0</sub> (Vượt ngưỡng):</i> Điện thế hãm <i>U</i><sub>h</sub> biến thiên hoàn toàn tuyến tính theo tần số <i>ν</i>. "
        "Hệ số góc của đường thẳng thực nghiệm (đạo hàm của <i>U</i><sub>h</sub> theo <i>ν</i>) bằng thương số giữa <i>h</i> và <i>e</i> là một hằng số phổ quát tuyệt đối, "
        "hoàn toàn độc lập với bản chất hóa học của kim loại làm catot. Robert Millikan (1916) đã tận dụng đặc tính này để đo đạc chuẩn xác hằng số Planck <i>h</i>, "
        "đem lại giải Nobel Vật lý năm 1923 và minh chứng hùng hồn cho thuyết photon của Einstein.<br/>"
        "• <i>Sự độc lập của dòng bão hòa:</i> Cường độ dòng quang điện bão hòa <i>I</i><sub>bh</sub> tỷ lệ thuận với số electron bứt ra trong một giây, "
        "do đó tỷ lệ thuận với thông lượng photon tới (cường độ sáng <i>I</i>), nhưng không làm thay đổi vận tốc hay điện thế hãm."
    )
    story.append(he.make_paragraph(g1_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_pe = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Thuyết sóng điện từ cổ điển của Maxwell hoàn toàn bất lực trong việc giải thích quy luật về giới hạn quang điện "
        "và tính tức thời của hiệu ứng quang điện ngoài.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Theo điện động lực học cổ điển, năng lượng sóng ánh sáng phân bố liên tục trên toàn bộ mặt sóng "
        "với mật độ năng lượng <i>w</i> = <i>ε</i><sub>0</sub> <i>E</i><sup>2</sup>. Khi chiếu sáng với chùm sáng yếu (ví dụ công suất 10<sup>−6</sup> W/m<sup>2</sup>), "
        "diện tích tiết diện hứng năng lượng của một nguyên tử chỉ cỡ kích thước bán kính Bohr <i>σ</i> ≈ <i>π r</i><sup>2</sup> ≈ 10<sup>−19</sup> m<sup>2</sup>. "
        "Công suất hấp thụ của mỗi nguyên tử chỉ đạt ~10<sup>−25</sup> W. Để tích lũy đủ công thoát <i>A</i> ≈ 2 eV ≈ 3.2 × 10<sup>−19</sup> J, "
        "electron cần thời gian tích lũy liên tục: thời gian <i>t</i> = <i>A</i>·<i>P</i><sup>−1</sup> xấp xỉ 3.2 × 10<sup>6</sup> s (gần 1 tháng)! "
        "Trong khi đó, thực nghiệm đo được thời gian trễ nhỏ hơn 10<sup>−9</sup> s.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Sự bất lực của thuyết cổ điển xuất phát từ giả định năng lượng trải rộng liên tục. Trong thực tế, "
        "năng lượng bức xạ bị lượng tử hóa thành các gói cục bộ photon <i>E</i> = <i>hν</i>. Quá trình truyền năng lượng là một biến cố va chạm đơn hạt tức thời. "
        "Nếu photon đơn lẻ có năng lượng <i>hν</i> &lt; <i>A</i>, electron không thể tích lũy năng lượng từ nhiều photon liên tiếp vì thời gian hồi phục nội tại "
        "của mạng tinh thể rất nhanh (~10<sup>−14</sup> s), dẫn tới sự tồn tại bất biến của tần số ngưỡng quang điện <i>ν</i><sub>0</sub>.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù học thuật thường gặp là ngộ nhận rằng hiệu ứng quang điện không bao giờ xảy ra "
        "với photon dưới ngưỡng. Trong vật lý laser hiện đại, khi mật độ thông lượng photon cực cao (chùm laser xung femto-giây với cường độ &gt; 10<sup>14</sup> W/cm<sup>2</sup>), "
        "xác suất để electron hấp thụ đồng thời 2 hoặc nhiều photon (Hiệu ứng quang điện đa photon — Multiphoton Photoelectric Effect) trở nên đáng kể, "
        "cho phép bứt electron khi tổng năng lượng <i>n·hν</i> ≥ <i>A</i><sub>exit</sub>."
    )
    story.append(he.make_paragraph(cer_pe, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.2.2: HIỆU ỨNG TÁN XẠ COMPTON & DẪN XUẤT ĐỊNH LƯỢNG BƯỚC SÓNG DỊCH CHUYỂN
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.2.2: Hiệu ứng tán xạ Compton &amp; Dẫn xuất định lượng bước sóng dịch chuyển", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g2_p1 = (
        "Năm 1923, Arthur Holly Compton tại Đại học Washington (St. Louis) đã thực hiện thí nghiệm tán xạ tia X đơn sắc trên bia graphite (than chì) "
        "và khám phá ra một hiện tượng chấn động vật lý thế giới: Trong chùm tia X tán xạ, bên cạnh thành phần bức xạ có bước sóng nguyên thủy <i>λ</i><sub>0</sub>, "
        "luôn xuất hiện một thành phần bức xạ mới có bước sóng <i>λ</i>′ lớn hơn bước sóng tới (<i>λ</i>′ &gt; <i>λ</i><sub>0</sub>, tương ứng tần số giảm đi). "
        "Độ tăng bước sóng Δ<i>λ</i> = <i>λ</i>′ − <i>λ</i><sub>0</sub> chỉ phụ thuộc duy nhất vào góc tán xạ <i>θ</i>, hoàn toàn độc lập với bước sóng tới <i>λ</i><sub>0</sub> "
        "và bản chất vật liệu bia tán xạ.<br/>"
        "Điện từ học sóng cổ điển của Thomson dự đoán rằng dưới tác dụng của điện trường sóng tới, electron sẽ dao động cưỡng bức với đúng tần số của sóng tới, "
        "và do đó bức xạ thứ cấp phát ra bắt buộc phải có cùng tần số <i>ν</i>′ = <i>ν</i><sub>0</sub>. Thuyết sóng hoàn toàn bất lực không thể giải thích sự xuất hiện của bước sóng dài hơn <i>λ</i>′."
    )
    story.append(he.make_paragraph(g2_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng 3 ảnh gốc Compton từ slide 15 và 16
    img_cp_exp = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_03_Bo_Tri_Thi_Nghiem_Compton.png")
    cap_cp_exp = "Hình 2.2.2a: Sơ đồ bố trí thực nghiệm tán xạ Compton (1923) với nguồn tia X Molybdenum, bia tán xạ Graphite và tinh thể tán sắc Bragg."
    story.append(he.embed_figure_with_caption(img_cp_exp, cap_cp_exp, kind="orig", styles=styles))

    cp_ocr_1 = "Nguồn phát tia X đơn sắc Ka của Molybdenum bước sóng chuẩn xác lambda_0 = 71.1 pm (0.711 Angstrom)."
    cp_ocr_2 = "Bia tán xạ Carbon graphite chứa mật độ lớn các electron liên kết yếu ở lớp vỏ ngoài nguyên tử."
    cp_ocr_3 = "Máy quang phổ kế tinh thể phản xạ Bragg quay quanh bia tán xạ để phân tích bước sóng chùm tán xạ theo góc theta."
    cp_ocr_4 = "Buồng ion hóa thu gom dòng điện đo cường độ bức xạ tán xạ tại từng góc quay của máy phân tích."
    cp_ocr_5 = "Hệ thống khe chuẩn trực chì định hướng chùm tia hẹp và triệt tiêu tia tán xạ thứ cấp ký sinh từ môi trường."
    story.append(he.make_paragraph(cp_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(cp_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(cp_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(cp_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(cp_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    img_cp_kin = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_04_Va_Cham_Dan_Hoi_Photon_Electron.png")
    cap_cp_kin = "Hình 2.2.2b: Cơ chế va chạm đàn hồi tương đối tính 2 chiều giữa photon tia X tới và electron tự do đứng yên ban đầu."
    story.append(he.embed_figure_with_caption(img_cp_kin, cap_cp_kin, kind="orig", styles=styles))

    # Nhúng đồ thị mô phỏng giải tích MATLAB phổ tán xạ Compton
    img_cp_sim = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.2_Pho_Tan_Xa_Compton_Cac_Goc.png")
    cap_cp_sim = "Hình 2.2.2c: Đồ thị mô phỏng giải tích MATLAB phổ tán xạ Compton: sự dịch chuyển bước sóng vạch modified theo góc tán xạ theta = 0°, 45°, 90°, 135°."
    story.append(he.embed_figure_with_caption(img_cp_sim, cap_cp_sim, kind="sim", styles=styles))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g2_p2 = (
        "<b>Hạt nhân vật lý — Tán xạ đàn hồi photon - electron tương đối tính:</b> Compton đã mô hình hóa tán xạ như một va chạm đàn hồi cơ học "
        "giữa hai hạt vi mô: photon tới mang năng lượng <i>E</i><sub>0</sub> = <i>hν</i><sub>0</sub> và động lượng <i>p</i><sub>0</sub> = <i>h</i>·<i>λ</i><sub>0</sub><sup>−1</sup> "
        "va chạm với electron đứng yên có khối lượng nghỉ <i>m</i><sub>0</sub> (năng lượng nghỉ <i>E</i><sub>0,e</sub> = <i>m</i><sub>0</sub> <i>c</i><sup>2</sup>). "
        "Sau va chạm, photon bị tán xạ theo góc <i>θ</i> với năng lượng giảm còn <i>E</i>′ = <i>hν</i>′, truyền một phần năng lượng và động lượng "
        "cho electron giật lùi (recoil electron) bay theo góc <i>φ</i>."
    )
    story.append(he.make_paragraph(g2_p2, styles["Body"]))

    eq_cp = r"\Delta\lambda = \lambda' - \lambda_0 = \frac{h}{m_0 c}(1 - \cos\theta) = \lambda_C (1 - \cos\theta)"
    nom_cp = [
        ("Độ dịch bước sóng Compton", "Δ<i>λ</i> = <i>λ</i>′ − <i>λ</i><sub>0</sub>", "pm", "Độ tăng bước sóng của photon sau va chạm tán xạ với electron"),
        ("Bước sóng Compton của electron", "<i>λ</i><sub>C</sub> = <i>h</i>·(<i>m</i><sub>0</sub><i>c</i>)<sup>−1</sup>", "pm", "Hằng số phổ quát đặc trưng: 2.42631023867 pm (0.02426 Å)"),
        ("Góc tán xạ photon", "<i>θ</i>", "độ", "Góc lệch phương giữa photon sau tán xạ so với phương chùm tia tới ban đầu"),
        ("Khối lượng nghỉ electron", "<i>m</i><sub>0</sub>", "kg", "Hằng số CODATA 2022: 9.1093837 × 10<sup>−31</sup> kg"),
        ("Vận tốc ánh sáng trong chân không", "<i>c</i>", "m/s", "Hằng số phổ quát: 2.99792458 × 10<sup>8</sup> m/s")
    ]
    story.append(he.build_target_equation_block(eq_cp, nom_cp, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    cp_step1_txt = (
        "Thiết lập định luật bảo toàn năng lượng toàn phần theo thuyết tương đối hẹp. Tổng năng lượng trước va chạm bằng tổng năng lượng sau va chạm:"
    )
    cp_step1_eq = r"h\nu_0 + m_0 c^2 = h\nu' + E_e = h\nu' + \sqrt{p_e^2 c^2 + m_0^2 c^4} \implies \sqrt{p_e^2 c^2 + m_0^2 c^4} = h(\nu_0 - \nu') + m_0 c^2"
    story.append(he.build_intermediate_equation(cp_step1_txt, cp_step1_eq, styles=styles, is_expanded_from_slide=True))

    cp_step2_txt = (
        "Bình phương hai vế phương trình bảo toàn năng lượng để giải phóng biểu thức chứa động lượng electron <i>p</i><sub>e</sub><sup>2</sup> <i>c</i><sup>2</sup>:"
    )
    cp_step2_eq = r"p_e^2 c^2 + m_0^2 c^4 = h^2(\nu_0 - \nu')^2 + 2 m_0 c^2 h(\nu_0 - \nu') + m_0^2 c^4 \implies p_e^2 c^2 = h^2(\nu_0 - \nu')^2 + 2 m_0 c^2 h(\nu_0 - \nu')"
    story.append(he.build_intermediate_equation(cp_step2_txt, cp_step2_eq, styles=styles, is_expanded_from_slide=True))

    cp_step3_txt = (
        "Thiết lập định luật bảo toàn véctơ động lượng trong mặt phẳng va chạm: <b>p</b><sub>0</sub> = <b>p</b>′ + <b>p</b><sub>e</sub>. "
        "Bình phương vô hướng véctơ để tìm biểu thức độc lập thứ hai cho <i>p</i><sub>e</sub><sup>2</sup>:"
    )
    cp_step3_eq = r"\vec{p}_e = \vec{p}_0 - \vec{p}' \implies p_e^2 = p_0^2 + p'^2 - 2 p_0 p' \cos\theta \implies p_e^2 c^2 = (h\nu_0)^2 + (h\nu')^2 - 2 (h\nu_0)(h\nu') \cos\theta"
    story.append(he.build_intermediate_equation(cp_step3_txt, cp_step3_eq, styles=styles, is_expanded_from_slide=True))

    cp_step4_txt = (
        "Đồng nhất hai biểu thức của <i>p</i><sub>e</sub><sup>2</sup> <i>c</i><sup>2</sup> từ phương trình năng lượng và phương trình động lượng, "
        "triệt tiêu các số hạng bậc hai và chia cả hai vế cho tích <i>h</i><sup>2</sup> <i>c</i><sup>2</sup> <i>ν</i><sub>0</sub> <i>ν</i>′ để thu được công thức kinh điển:"
    )
    cp_step4_eq = r"2 m_0 c^2 h(\nu_0 - \nu') = 2 h^2 \nu_0 \nu' (1 - \cos\theta) \implies \frac{c}{\nu'} - \frac{c}{\nu_0} = \frac{h}{m_0 c}(1 - \cos\theta) \implies \lambda' - \lambda_0 = \lambda_C (1 - \cos\theta)"
    story.append(he.build_intermediate_equation(cp_step4_txt, cp_step4_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g2_p4 = (
        "<b>Khảo sát các trường hợp giới hạn đặc biệt:</b><br/>"
        "• <i>Tán xạ thẳng về phía trước (θ = 0°):</i> cos 0° = 1 kéo theo Δ<i>λ</i> = 0. Photon không bị lệch hướng, không truyền năng lượng cho electron.<br/>"
        "• <i>Tán xạ vuông góc (θ = 90°):</i> cos 90° = 0 kéo theo Δ<i>λ</i> = <i>λ</i><sub>C</sub> = 2.426 pm. Bước sóng photon tăng thêm đúng bằng bước sóng Compton.<br/>"
        "• <i>Tán xạ bật lùi cực đại (θ = 180°):</i> cos 180° = −1 kéo theo Δ<i>λ</i> = 2<i>λ</i><sub>C</sub> = 4.853 pm. Photon truyền động lượng cực đại cho electron giật lùi.<br/>"
        "• <i>Giải thích sự tồn tại của vạch không dịch chuyển λ<sub>0</sub>:</i> Trong tinh thể graphite, bên cạnh các electron liên kết yếu ở lớp ngoài cùng "
        "(hoạt động như electron gần như tự do), còn có các electron liên kết rất chặt với hạt nhân Carbon. Khi photon va chạm với electron liên kết chặt, "
        "năng lượng và động lượng được hấp thụ bởi toàn bộ nguyên tử Carbon có khối lượng <i>M</i> ≈ 12 × 1836 <i>m</i><sub>0</sub> ≈ 22000 <i>m</i><sub>0</sub>. "
        "Bước sóng dịch chuyển khi đó tỷ lệ nghịch với <i>M</i> (xấp xỉ 10<sup>−4</sup> pm), hoàn toàn không thể phát hiện được bằng máy đo, tạo thành vạch nguyên thủy <i>λ</i><sub>0</sub>."
    )
    story.append(he.make_paragraph(g2_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_cp = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Hiệu ứng tán xạ Compton chỉ có thể quan sát rõ rệt đối với bức xạ sóng ngắn mang năng lượng cao (tia X, tia gamma) "
        "và hoàn toàn chìm nghỉm không thể quan sát được trong vùng ánh sáng khả kiến.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Độ dịch chuyển bước sóng cực đại trong tán xạ Compton là Δ<i>λ</i><sub>max</sub> = 2<i>λ</i><sub>C</sub> ≈ 0.0485 Å. "
        "Đối với tia X (bước sóng <i>λ</i><sub>0</sub> ≈ 0.711 Å), tỷ số độ dịch tương đối Δ<i>λ</i> trên <i>λ</i><sub>0</sub> đạt xấp xỉ 6.8% (dễ dàng phân tách). "
        "Đối với ánh sáng khả kiến (bước sóng <i>λ</i><sub>0</sub> ≈ 5000 Å), tỷ số độ dịch tương đối chỉ đạt khoảng 0.00097% "
        "(nhỏ hơn nhiều so với độ rộng phổ tự nhiên và sai số thiết bị đo).<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Năng lượng của photon ánh sáng khả kiến chỉ cỡ ~2.5 eV, nhỏ hơn nhiều so với năng lượng liên kết nguyên tử "
        "và năng lượng nghỉ của electron (<i>m</i><sub>0</sub><i>c</i><sup>2</sup> ≈ 511 keV). Do đó, photon ánh sáng nhìn thấy chủ yếu tương tác theo kiểu tán xạ Thomson "
        "hoặc Rayleigh với toàn bộ nguyên tử mà không làm bộc lộ tính chất va chạm hạt đàn hồi.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù kinh điển là việc áp dụng cơ học cổ điển Newton để tính động lượng electron giật lùi. "
        "Vì năng lượng tia X photon truyền cho electron có thể đạt hàng chục keV, vận tốc electron sau va chạm đạt tới phân số đáng kể của vận tốc ánh sáng <i>c</i>, "
        "bắt buộc phải sử dụng hệ thức tương đối tính hẹp của Einstein; việc dùng công thức cổ điển <i>E</i><sub>k</sub> = <i>p</i><sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup> "
        "sẽ dẫn tới sai số nghiêm trọng khi góc tán xạ <i>θ</i> lớn."
    )
    story.append(he.make_paragraph(cer_cp, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.2.3: GIẢ THIẾT SÓNG VẬT CHẤT DE BROGLIE & Ý NGHĨA CƠ BẢN
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.2.3: Giả thiết sóng vật chất de Broglie &amp; Ý nghĩa cơ bản", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g3_p1 = (
        "Năm 1924, trong luận án tiến sĩ bảo vệ tại Đại học Sorbonne (Paris), Louis de Broglie đã đề xuất một giả thuyết táo bạo làm thay đổi vĩnh viễn "
        "diện mạo của nền vật lý học: <i>Thiên nhiên vốn yêu chuộng sự đối xứng</i>. Nếu bức xạ điện từ (vốn được coi là sóng) có thể hành xử như những hạt photon mang động lượng, "
        "thì ngược lại, các đối tượng vật chất (vốn được coi là các hạt có khối lượng như electron, proton, neutron) cũng bắt buộc phải sở hữu bản chất sóng liên kết. "
        "Mỗi vi hạt tự do chuyển động với động lượng <i>p</i> đều gắn liền với một sóng đơn sắc phẳng lan truyền có bước sóng <i>λ</i> = <i>h</i>·<i>p</i><sup>−1</sup> "
        "và tần số <i>ν</i> = <i>E</i>·<i>h</i><sup>−1</sup>."
    )
    story.append(he.make_paragraph(g3_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng đồ thị mô phỏng bước sóng de Broglie
    img_db_sim = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.2_Buoc_Song_De_Broglie_Theo_Dien_The.png")
    cap_db_sim = "Hình 2.2.3: Đồ thị log-log mô phỏng bước sóng de Broglie của electron theo điện thế gia tốc U từ 1 V đến 1 MV, đối chiếu mô hình cổ điển và tương đối tính."
    story.append(he.embed_figure_with_caption(img_db_sim, cap_db_sim, kind="sim", styles=styles))

    db_ocr_1 = "Đặc tuyến cổ điển biểu diễn bước sóng lambda suy giảm đơn điệu theo hàm lũy thừa trên thang toạ độ log-log."
    db_ocr_2 = "Đặc tuyến tương đối tính tách dần ở điện áp gia tốc cao U > 10 kV do khối lượng tương đối tính tăng làm giảm bước sóng sâu hơn."
    db_ocr_3 = "Điểm mốc Davisson - Germer tại U = 54 V cho bước sóng thực nghiệm 1.67 Angstrom, nằm đúng trong dải nhiễu xạ mạng tinh thể."
    db_ocr_4 = "Điểm mốc kính hiển vi điện tử truyền qua TEM tại U = 100 kV cho bước sóng siêu ngắn lambda = 3.7 pm, vượt trội giới hạn nhiễu xạ quang học."
    db_ocr_5 = "Vùng điện thế hạ thế U < 10 V tương ứng bước sóng lớn hơn 4 Angstrom, phù hợp thăm dò bề mặt vật liệu 2D như Graphene."
    story.append(he.make_paragraph(db_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(db_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(db_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(db_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(db_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g3_p2 = (
        "<b>Hạt nhân vật lý — Hệ thức bước sóng liên kết de Broglie:</b> Bước sóng de Broglie thiết lập cầu nối định lượng bất biến giữa "
        "hai phạm trù đối lập trong vật lý: đại lượng đặc trưng cho tính chất hạt (khối lượng <i>m</i>, vận tốc <i>v</i>, động lượng <i>p</i>, động năng <i>E</i><sub>k</sub>) "
        "và đại lượng đặc trưng cho tính chất sóng (bước sóng <i>λ</i>, tần số <i>ν</i>, số sóng <i>k</i>). Đối với electron được gia tốc từ trạng thái nghỉ "
        "qua hiệu điện thế tĩnh điện <i>U</i>:"
    )
    story.append(he.make_paragraph(g3_p2, styles["Body"]))

    eq_db = r"\lambda = \frac{h}{p} = \frac{h}{m_0 v} = \frac{h}{\sqrt{2 m_0 e U}} \approx \frac{1{,}226}{\sqrt{U(\mathrm{V})}}\ \mathrm{nm} = \frac{12{,}26}{\sqrt{U(\mathrm{V})}}\ \mathrm{\AA}"
    nom_db = [
        ("Bước sóng de Broglie của electron", "<i>λ</i>", "nm", "Bước sóng của sóng vật chất liên kết với chùm electron chuyển động"),
        ("Động lượng của hạt", "<i>p</i> = <i>m</i><sub>0</sub><i>v</i>", "kg·m/s", "Đại lượng cơ học mô tả chuyển động hạt vi mô"),
        ("Điện thế gia tốc chùm electron", "<i>U</i>", "V", "Hiệu điện thế tĩnh điện cấp động năng eU cho electron trong súng phóng điện tử"),
        ("Hằng số Planck", "<i>h</i>", "J·s", "Hằng số lượng tử: 6.62607015 × 10<sup>−34</sup> J·s"),
        ("Điện tích nguyên tố", "<i>e</i>", "C", "Hằng số CODATA 2022: 1.602176634 × 10<sup>−19</sup> C")
    ]
    story.append(he.build_target_equation_block(eq_db, nom_db, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    db_step1_txt = (
        "Dẫn xuất bước sóng de Broglie đối với hạt phi tương đối tính (vận tốc <i>v</i> ≪ <i>c</i>). Động năng hạt nhận được từ điện trường "
        "bằng độ giảm thế năng tĩnh điện: <i>eU</i> = <i>p</i><sup>2</sup>·(2<i>m</i><sub>0</sub>)<sup>−1</sup>. Từ đó biểu diễn động lượng <i>p</i> theo điện thế <i>U</i>:"
    )
    db_step1_eq = r"p = \sqrt{2 m_0 E_k} = \sqrt{2 m_0 e U} \implies \lambda = \frac{h}{p} = \frac{h}{\sqrt{2 m_0 e U}}"
    story.append(he.build_intermediate_equation(db_step1_txt, db_step1_eq, styles=styles, is_expanded_from_slide=True))

    db_step2_txt = (
        "Thay thế các hằng số vật lý chuẩn mực CODATA 2022 (<i>h</i> = 6.62607 × 10<sup>−34</sup> J·s, <i>m</i><sub>0</sub> = 9.10938 × 10<sup>−31</sup> kg, "
        "<i>e</i> = 1.60218 × 10<sup>−19</sup> C) để thiết lập công thức tính nhanh kỹ thuật tiện dụng:"
    )
    db_step2_eq = r"\lambda = \frac{6{,}62607 \times 10^{-34}}{\sqrt{2 \times (9{,}10938 \times 10^{-31}) \times (1{,}60218 \times 10^{-19})}} \frac{1}{\sqrt{U}} = \frac{1{,}2264 \times 10^{-9}}{\sqrt{U(\mathrm{V})}}\ \mathrm{m} = \frac{12{,}264}{\sqrt{U(\mathrm{V})}}\ \mathrm{\AA}"
    story.append(he.build_intermediate_equation(db_step2_txt, db_step2_eq, styles=styles, is_expanded_from_slide=True))

    db_step3_txt = (
        "Mở rộng sang trường hợp tương đối tính tổng quát khi điện thế gia tốc <i>U</i> &gt; 10 kV (như trong kính hiển vi TEM 100–300 kV). "
        "Hệ thức liên hệ giữa động năng và động lượng tương đối tính khai căn năng lượng toàn phần trừ năng lượng nghỉ "
        "dẫn tới công thức hiệu chỉnh chính xác:"
    )
    db_step3_eq = r"p = \frac{1}{c}\sqrt{eU(eU + 2 m_0 c^2)} \implies \lambda_{\mathrm{rel}} = \frac{hc}{\sqrt{eU(eU + 2 m_0 c^2)}} = \frac{h}{\sqrt{2 m_0 e U}} \frac{1}{\sqrt{1 + \frac{eU}{2 m_0 c^2}}}"
    story.append(he.build_intermediate_equation(db_step3_txt, db_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g3_p4 = (
        "<b>So sánh thang đo thế giới vĩ mô và vi mô:</b><br/>"
        "• <i>Vật thể vĩ mô:</i> Một quả bóng khối lượng <i>m</i> = 0.1 kg bay với vận tốc <i>v</i> = 10 m/s sở hữu bước sóng de Broglie "
        "tính toán cho giá trị cực tiểu <i>λ</i> = 6.63 × 10<sup>−34</sup> m. Thang đo này nhỏ hơn bán kính hạt nhân nguyên tử hàng tỷ tỷ lần, "
        "hoàn toàn không tồn tại bất kỳ một khe chắn hay cách tử vật lý nào có kích thước tương thích để tạo ra hiện tượng nhiễu xạ. "
        "Do đó các quy luật cơ học cổ điển hoàn toàn đúng đối với thế giới vĩ mô.<br/>"
        "• <i>Hạt vi mô (Electron trong điện trường U = 54 V):</i> Bước sóng thu được <i>λ</i> xấp xỉ 0.167 nm (1.67 Å). "
        "Giá trị này nằm đúng vào thang khoảng cách giữa các nguyên tử trong mạng tinh thể chất rắn (cỡ 1–3 Å), biến tinh thể thành cách tử nhiễu xạ tự nhiên lý tưởng.<br/>"
        "• <i>Kính hiển vi điện tử truyền qua (TEM 200 kV):</i> Bước sóng de Broglie giảm xuống chỉ còn <i>λ</i><sub>rel</sub> ≈ 0.00251 nm (2.51 pm), "
        "nhỏ hơn bước sóng ánh sáng khả kiến 200,000 lần, cho phép kính hiển vi đạt độ phân giải cấp độ hạ-Angstrom, quan sát rõ từng cột nguyên tử đơn lẻ."
    )
    story.append(he.make_paragraph(g3_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_db = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Bước sóng de Broglie giải thích một cách tự nhiên và hoàn hảo điều kiện lượng tử hóa mômen động lượng "
        "của tiên đề Bohr <i>L</i> = <i>nħ</i> cho nguyên tử Hydro, biến giả định tiên nghiệm của Bohr thành một hệ quả toán học tất yếu.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Xét electron chuyển động trên quỹ đạo tròn bán kính <i>r</i> với vận tốc <i>v</i>. "
        "Để sóng liên kết de Broglie không bị tự triệt tiêu sau nhiều chu kỳ quay quanh hạt nhân, chu vi quỹ đạo tròn 2<i>πr</i> bắt buộc phải chứa "
        "đúng một số nguyên lần bước sóng: 2<i>πr</i> = <i>nλ</i>.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Thay thế bước sóng liên kết de Broglie vào điều kiện sóng dừng trên quỹ đạo khép kín: "
        "hệ thức 2<i>πr</i> = <i>nλ</i> dẫn tới <i>mvr</i> = <i>nħ</i> (với <i>n</i> = 1, 2, 3...). "
        "Như vậy, các quỹ đạo dừng bền vững của Bohr thực chất chính là các trạng thái <i>sóng dừng</i> (Standing Wave) của sóng electron "
        "giam cầm trong trường xuyên tâm Coulomb của hạt nhân.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù phổ biến là đồng nhất sóng de Broglie với sóng điện từ. "
        "Cần nhấn mạnh: Sóng de Broglie không mang điện tích dao động, không bức xạ năng lượng điện từ khi chuyển động có gia tốc, "
        "mà là sóng biên độ xác suất cơ học lượng tử (sẽ được hình thức hóa qua hàm sóng <i>Ψ</i> của Schrödinger)."
    )
    story.append(he.make_paragraph(cer_db, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.2.4: NHIỄU XẠ TIA X VÀ ĐỊNH LUẬT PHẢN XẠ BRAGG
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.2.4: Nhiễu xạ tia X và Định luật phản xạ Bragg", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g4_p1 = (
        "Năm 1913, hai cha con nhà vật lý người Anh William Henry Bragg và William Lawrence Bragg đã thiết lập phương pháp tán xạ tia X trên mạng tinh thể "
        "và công bố định luật nhiễu xạ Bragg kinh điển (đoạt giải Nobel Vật lý năm 1915). "
        "Trong chất rắn tinh thể, các nguyên tử hoặc ion được sắp xếp tuần hoàn trật tự ba chiều nghiêm ngặt, tạo thành họ các mặt phẳng nguyên tử song song "
        "(gọi là các mặt phẳng Bragg) cách đều nhau một khoảng cách liên mặt mạng <i>d</i>. "
        "Khi chiếu một chùm sóng phẳng (tia X hoặc sóng hạt vi mô) tới bề mặt tinh thể, mỗi nguyên tử đóng vai trò là một tâm tán xạ phát sóng cầu thứ cấp. "
        "Sự giao thoa giữa các chùm sóng phản xạ từ các mặt phẳng nguyên tử kế tiếp nhau sẽ tạo nên các cực đại nhiễu xạ sắc nét trên màn đo."
    )
    story.append(he.make_paragraph(g4_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc phản xạ Bragg
    img_bragg_1 = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_05_Nhieu_Xa_Tia_X_Mat_Phang_Bragg.png")
    cap_bragg_1 = "Hình 2.2.4a: Sơ đồ hình học tán xạ tia X trên các mặt phẳng nguyên tử tinh thể song song và hiệu quang lộ giữa hai tia kế tiếp."
    story.append(he.embed_figure_with_caption(img_bragg_1, cap_bragg_1, kind="orig", styles=styles))

    bragg_ocr_1 = "Họ mặt phẳng tinh thể Bragg song song cách nhau một khoảng cách liên mạng d xác định."
    bragg_ocr_2 = "Góc trượt Bragg theta hợp bởi chùm tia tới và mặt phẳng nguyên tử (chú ý khác biệt với góc tới thông thường hợp với pháp tuyến)."
    bragg_ocr_3 = "Đoạn đường đi chênh lệch của tia phản xạ lớp dưới so với lớp trên: đoạn AB + BC = 2d*sin(theta)."
    bragg_ocr_4 = "Điều kiện giao thoa tăng cường: hiệu quang lộ đúng bằng một số nguyên lần bước sóng n*lambda."
    bragg_ocr_5 = "Chùm tia phản xạ tăng cường kết hợp tạo nên đỉnh cực đại quang phổ nhiễu xạ trên đầu dò detector."
    story.append(he.make_paragraph(bragg_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(bragg_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(bragg_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(bragg_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(bragg_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    img_bragg_2 = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_06_Giao_Thoa_Song_Bragg_Tinh_The.png")
    cap_bragg_2 = "Hình 2.2.4b: Giao thoa sóng phản xạ Bragg: phân tích điều kiện đồng pha của các đỉnh sóng khi phản xạ trên nhiều lớp nguyên tử."
    story.append(he.embed_figure_with_caption(img_bragg_2, cap_bragg_2, kind="orig", styles=styles))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g4_p2 = (
        "<b>Hạt nhân vật lý — Định luật nhiễu xạ Bragg:</b> Định luật Bragg quy định điều kiện chính xác để các sóng phản xạ từ các mặt tinh thể "
        "kế tiếp nhau giao thoa tăng cường (Constructive Interference). Để các sóng này cùng pha khi thoát ra khỏi tinh thể, "
        "hiệu đường đi quang học giữa hai tia phản xạ liên tiếp bắt buộc phải bằng một số nguyên lần bước sóng:"
    )
    story.append(he.make_paragraph(g4_p2, styles["Body"]))

    eq_bragg = r"2d\sin\theta = n\lambda \quad (n = 1, 2, 3, \dots)"
    nom_bragg = [
        ("Khoảng cách liên mặt mạng", "<i>d</i>", "nm", "Khoảng cách vuông góc giữa hai mặt phẳng nguyên tử song song kế tiếp"),
        ("Góc trượt Bragg (Glancing angle)", "<i>θ</i>", "độ", "Góc hợp bởi chùm tia tới (hoặc tia phản xạ) với mặt phẳng mạng nguyên tử"),
        ("Bậc cực đại nhiễu xạ", "<i>n</i>", "số nguyên", "Bậc phản xạ (n = 1: cực đại bậc nhất, n = 2: cực đại bậc hai, ...)"),
        ("Bước sóng chùm tới", "<i>λ</i>", "nm", "Bước sóng của bức xạ tia X hoặc sóng vật chất de Broglie của electron")
    ]
    story.append(he.build_target_equation_block(eq_bragg, nom_bragg, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    br_step1_txt = (
        "Phân tích hình học hiệu đường đi quang học. Xét hai tia sáng song song (1) và (2) cùng chiếu tới tinh thể dưới góc trượt <i>θ</i>. "
        "Tia (1) phản xạ tại nguyên tử <i>A</i> trên mặt mạng thứ nhất. Tia (2) đâm xuyên sâu hơn và phản xạ tại nguyên tử <i>B</i> trên mặt mạng thứ hai. "
        "Hạ các đường vuông góc từ <i>A</i> xuống tia tới (2) tại <i>H</i><sub>1</sub> và xuống tia phản xạ (2) tại <i>H</i><sub>2</sub>:"
    )
    br_step1_eq = r"\Delta L = H_1 B + B H_2 = d\sin\theta + d\sin\theta = 2d\sin\theta"
    story.append(he.build_intermediate_equation(br_step1_txt, br_step1_eq, styles=styles, is_expanded_from_slide=True))

    br_step2_txt = (
        "Thiết lập điều kiện giao thoa tăng cường cực đại. Độ lệch pha giữa hai sóng phản xạ là Δ<i>φ</i> = <i>k</i>·Δ<i>L</i> với số sóng <i>k</i>. "
        "Để hai sóng đồng pha hoàn toàn (Δ<i>φ</i> = 2<i>nπ</i>), hiệu quang lộ bắt buộc phải bằng bội số nguyên lần bước sóng:"
    )
    br_step2_eq = r"\Delta\phi = \frac{2\pi}{\lambda} (2d\sin\theta) = 2n\pi \implies 2d\sin\theta = n\lambda \quad (n \in \mathbb{N}^*)"
    story.append(he.build_intermediate_equation(br_step2_txt, br_step2_eq, styles=styles, is_expanded_from_slide=True))

    br_step3_txt = (
        "Liên hệ giữa khoảng cách liên mạng <i>d</i> và hằng số mạng tinh thể <i>a</i> đối với mạng lập phương đơn giản, tâm khối (BCC) hoặc tâm diện (FCC) "
        "theo chỉ số Miller (<i>h</i> <i>k</i> <i>l</i>):"
    )
    br_step3_eq = r"d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}} \implies 2\left(\frac{a}{\sqrt{h^2 + k^2 + l^2}}\right)\sin\theta = n\lambda"
    story.append(he.build_intermediate_equation(br_step3_txt, br_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g4_p4 = (
        "<b>Điều kiện biên tồn tại cực đại phản xạ:</b><br/>"
        "• <i>Giới hạn bước sóng tối đa:</i> Vì sin <i>θ</i> ≤ 1, điều kiện để tồn tại cực đại bậc <i>n</i> là: <i>λ</i> ≤ 2<i>d·n</i><sup>−1</sup>. "
        "Đối với cực đại bậc nhất (<i>n</i> = 1), bước sóng tới bắt buộc phải thỏa mãn <i>λ</i> ≤ 2<i>d</i>. "
        "Trong chất rắn, khoảng cách mạng <i>d</i> thông thường từ 0.1 nm đến 0.3 nm, do đó bước sóng tối đa có thể nhiễu xạ là <i>λ</i><sub>max</sub> ≈ 0.6 nm.<br/>"
        "• <i>Tại sao ánh sáng nhìn thấy không nhiễu xạ:</i> Ánh sáng khả kiến có bước sóng 400–700 nm, lớn hơn 2<i>d</i> cả nghìn lần. "
        "Do đó giá trị sin <i>θ</i> đòi hỏi vượt quá 1 (vô nghiệm), ánh sáng khả kiến hoàn toàn không thể bị nhiễu xạ trên mạng tinh thể nguyên tử.<br/>"
        "• <i>Ứng dụng nhiễu xạ tia X (XRD):</i> Khi sử dụng bước sóng chuẩn đã biết trước (ví dụ Cu K<i>α</i> với <i>λ</i> = 0.15406 nm) "
        "và đo chính xác các góc phản xạ <i>θ</i>, định luật Bragg cho phép xác định chính xác cấu trúc mạng tinh thể, hằng số mạng và độ định hướng màng mỏng nano."
    )
    story.append(he.make_paragraph(g4_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_br = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Phản xạ Bragg trên tinh thể chất rắn khác biệt bản chất so với hiện tượng phản xạ quang học thông thường trên gương phẳng.<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Phản xạ quang học trên gương phẳng xảy ra ở mọi góc tới <i>θ</i> bất kỳ. Ngược lại, phản xạ Bragg "
        "chỉ xuất hiện tại các góc rời rạc nghiêm ngặt thỏa mãn phương trình 2<i>d</i> sin <i>θ</i> = <i>nλ</i>; tại các góc lệch chỉ 0.1°, "
        "cường độ phản xạ suy giảm gần như triệt tiêu về 0.<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Gương phẳng phản xạ ở bề mặt giới hạn hai môi trường. Phản xạ Bragg là hiện tượng tán xạ thể tích "
        "từ hàng trăm đến hàng nghìn lớp mặt phẳng nguyên tử nằm sâu trong lòng khối. Nếu điều kiện Bragg không thỏa mãn chính xác, sóng phản xạ từ các lớp sâu "
        "sẽ lệch pha triệt tiêu lẫn nhau (Destructive Interference), làm triệt tiêu hoàn toàn cường độ sóng tổng hợp thoát ra ngoài.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Điểm mù dễ mắc phải là nhầm lẫn góc trượt Bragg <i>θ</i> với góc tới quy ước trong quang hình học. "
        "Trong quang học Snell, góc tới <i>i</i> hợp với <i>pháp tuyến</i> mặt gương (<i>i</i> = 90° − <i>θ</i>). Nếu người học vô ý thay góc tới pháp tuyến vào công thức 2<i>d</i> sin <i>i</i> "
        "thì toàn bộ tính toán khoảng cách mạng và bước sóng sẽ sai lệch hoàn toàn."
    )
    story.append(he.make_paragraph(cer_br, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # LUẬN ĐIỂM 2.2.5: THÍ NGHIỆM DAVISSON - GERMER: BẰNG CHỨNG THỰC NGHIỆM TRỰC TIẾP CỦA SÓNG ELECTRON
    # =========================================================================
    story.append(he.make_paragraph("Luận điểm 2.2.5: Thí nghiệm Davisson - Germer: Bằng chứng thực nghiệm trực tiếp của sóng electron", styles["H2"]))
    story.append(Spacer(1, 4))

    # Giai đoạn 1: Giới thiệu khái niệm & Trực quan hóa mở đầu
    story.append(he.make_paragraph("Giai đoạn 1: Giới thiệu khái niệm &amp; Trực quan hóa mở đầu", styles["H3"]))
    g5_p1 = (
        "Năm 1927, tại phòng thí nghiệm Bell Telephone Laboratories (Hoa Kỳ), Clinton Davisson và Lester Germer đã công bố kết quả thực nghiệm "
        "tán xạ chùm electron trên đơn tinh thể Niken. Cùng năm đó tại Scotland, George Paget Thomson đã độc lập chứng minh hiện tượng nhiễu xạ electron "
        "khi truyền qua màng kim loại đa tinh thể mỏng. Hai thí nghiệm mang tính bước ngoặt này đã cung cấp bằng chứng thực nghiệm trực tiếp và không thể tranh cãi "
        "về bản chất sóng của electron, mang lại giải Nobel Vật lý năm 1937 cho Davisson và Thomson (một điều kỳ thú lịch sử: J.J. Thomson đoạt giải Nobel năm 1906 "
        "vì chứng minh electron là hạt, còn con trai ông G.P. Thomson đoạt giải Nobel năm 1937 vì chứng minh electron là sóng!)."
    )
    story.append(he.make_paragraph(g5_p1, styles["Body"]))
    story.append(Spacer(1, 4))

    # Nhúng ảnh gốc sơ đồ Davisson Germer và Thomson
    img_dg_exp = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_07_So_Do_Davisson_Germer.png")
    cap_dg_exp = "Hình 2.2.5a: Sơ đồ súng phóng điện tử, buồng chân không và đầu dò detector xoay quanh đơn tinh thể Niken trong thí nghiệm Davisson - Germer."
    story.append(he.embed_figure_with_caption(img_dg_exp, cap_dg_exp, kind="orig", styles=styles))

    dg_ocr_1 = "Súng phóng điện tử với dây tóc nung vonfram phát xạ nhiệt điện tử và các điện cực gia tốc chuẩn trực thế U."
    dg_ocr_2 = "Đơn tinh thể Niken tinh khiết được nung luyện đặc biệt để hình thành các miền tinh thể đơn hướng đồng nhất."
    dg_ocr_3 = "Đầu dò Faraday cup kết nối với điện kế cực nhạy thu gom electron tán xạ, quay được từ góc 20 độ đến 90 độ."
    dg_ocr_4 = "Toàn bộ hệ thống đặt trong buồng chân không siêu cao nhằm tránh va chạm tán xạ của electron với phân tử không khí."
    dg_ocr_5 = "Chùm electron bắn vuông góc vào bề mặt phẳng tinh thể Ni (111) và bị tán xạ đàn hồi theo góc phi."
    story.append(he.make_paragraph(dg_ocr_1, styles["Body"], ocr_idx=1))
    story.append(he.make_paragraph(dg_ocr_2, styles["Body"], ocr_idx=2))
    story.append(he.make_paragraph(dg_ocr_3, styles["Body"], ocr_idx=3))
    story.append(he.make_paragraph(dg_ocr_4, styles["Body"], ocr_idx=4))
    story.append(he.make_paragraph(dg_ocr_5, styles["Body"], ocr_idx=5))
    story.append(Spacer(1, 6))

    img_thomson = os.path.join(kho_anh, "[Goc]_Muc_2.2_Hinh_08_Ket_Qua_Nhieu_Xa_Electron_Ni.png")
    cap_thomson = "Hình 2.2.5b: Kết quả ảnh thực nghiệm nhiễu xạ điện tử: vòng tròn đồng tâm Debye - Scherrer của G.P. Thomson khẳng định tính chất sóng vật chất."
    story.append(he.embed_figure_with_caption(img_thomson, cap_thomson, kind="orig", styles=styles))

    # Nhúng đồ thị mô phỏng cực đại Davisson Germer
    img_dg_sim = os.path.join(kho_anh, "[Mo_Phong]_Muc_2.2_Cuc_Dai_Nhieu_Xa_Davisson_Germer.png")
    cap_dg_sim = "Hình 2.2.5c: Đồ thị mô phỏng giải tích MATLAB cực đại tán xạ Davisson - Germer: phân bố góc phi tại U = 54 V và đặc tuyến cộng hưởng theo điện thế gia tốc U."
    story.append(he.embed_figure_with_caption(img_dg_sim, cap_dg_sim, kind="sim", styles=styles))

    # Giai đoạn 2: Ví dụ tối giản & Hạt nhân vật lý
    story.append(he.make_paragraph("Giai đoạn 2: Ví dụ tối giản &amp; Hạt nhân vật lý", styles["H3"]))
    g5_p2 = (
        "<b>Hạt nhân vật lý — Khảo sát định lượng tại điểm cực đại U = 54 V:</b> Trong thí nghiệm với tinh thể Niken, khi quét điện thế gia tốc "
        "từ 40 V đến 68 V, Davisson và Germer phát hiện một đỉnh nhọn cực đại xuất hiện nổi bật tại điện thế <i>U</i> = 54 V và góc tán xạ <i>φ</i> = 50°. "
        "Sự xuất hiện của đỉnh cường độ cục bộ này chỉ có thể giải thích được nếu coi electron là một sóng giao thoa tăng cường theo định luật Bragg."
    )
    story.append(he.make_paragraph(g5_p2, styles["Body"]))

    eq_dg = r"\lambda = D \sin\phi = 2d \sin\theta = \frac{h}{\sqrt{2 m_0 e U}}"
    nom_dg = [
        ("Bước sóng electron xác định bằng thực nghiệm", "<i>λ</i>", "nm", "Bước sóng đo đạc qua công thức giao thoa cách tử bề mặt Niken"),
        ("Khoảng cách liên hàng nguyên tử bề mặt", "<i>D</i>", "nm", "Khoảng cách giữa các hàng nguyên tử trên mặt phẳng (111) của Ni: 0.215 nm"),
        ("Góc tán xạ electron", "<i>φ</i>", "độ", "Góc giữa chùm electron tới vuông góc và chùm electron phản xạ (đỉnh nhọn tại 50°)"),
        ("Khoảng cách mặt mạng Bragg tương đương", "<i>d</i> = <i>D</i> sin(0.5<i>φ</i>)", "nm", "Khoảng cách giữa các mặt phản xạ nghiêng trong khối: 0.091 nm"),
        ("Góc trượt Bragg tương đương", "<i>θ</i> = 90° − 0.5<i>φ</i>", "độ", "Góc trượt Bragg tương ứng: 65° tại góc tán xạ 50°")
    ]
    story.append(he.build_target_equation_block(eq_dg, nom_dg, styles=styles))
    story.append(Spacer(1, 6))

    # Giai đoạn 3: Thực hành có hướng dẫn & Chuỗi nhân quả dẫn xuất
    story.append(he.make_paragraph("Giai đoạn 3: Thực hành có hướng dẫn &amp; Chuỗi nhân quả dẫn xuất", styles["H3"]))
    
    dg_step1_txt = (
        "Bước 1: Tính bước sóng lý thuyết de Broglie của chùm electron gia tốc qua hiệu điện thế <i>U</i> = 54 V bằng công thức vi mô:"
    )
    dg_step1_eq = r"\lambda_{\mathrm{theory}} = \frac{h}{\sqrt{2 m_0 e U}} = \frac{1{,}226}{\sqrt{54}}\ \mathrm{nm} \approx 0{,}1668\ \mathrm{nm} = 1{,}668\ \mathrm{\AA}"
    story.append(he.build_intermediate_equation(dg_step1_txt, dg_step1_eq, styles=styles, is_expanded_from_slide=True))

    dg_step2_txt = (
        "Bước 2: Tính bước sóng thực nghiệm thông qua hiện tượng nhiễu xạ trên các hàng nguyên tử bề mặt. Bề mặt tinh thể Niken hoạt động như "
        "một cách tử phản xạ một chiều với chu kỳ cách tử <i>D</i> = 0.215 nm (đo được độc lập qua nhiễu xạ tia X). Với chùm tia tới vuông góc mặt cách tử, "
        "điều kiện cực đại bậc nhất (<i>n</i> = 1) tại góc tán xạ <i>φ</i> = 50° là:"
    )
    dg_step2_eq = r"\lambda_{\mathrm{exp}} = D \sin\phi = (0{,}215\ \mathrm{nm}) \times \sin(50^\circ) = 0{,}215 \times 0{,}7660 \approx 0{,}1647\ \mathrm{nm} = 1{,}647\ \mathrm{\AA}"
    story.append(he.build_intermediate_equation(dg_step2_txt, dg_step2_eq, styles=styles, is_expanded_from_slide=True))

    dg_step3_txt = (
        "Bước 3: Đối chiếu với định luật phản xạ Bragg thể tích. Xét họ mặt phẳng nguyên tử nghiêng góc 0.5<i>φ</i> so với bề mặt. "
        "Góc trượt Bragg là <i>θ</i> = 90° − 0.5<i>φ</i> = 90° − 25° = 65°. Khoảng cách giữa các mặt mạng nghiêng là <i>d</i> = <i>D</i> sin(0.5<i>φ</i>) = 0.215 × sin(25°) = 0.0909 nm. "
        "Áp dụng định luật Bragg 2<i>d</i> sin <i>θ</i> = <i>λ</i>:"
    )
    dg_step3_eq = r"\lambda_{\mathrm{Bragg}} = 2d \sin\theta = 2 \times (0{,}0909\ \mathrm{nm}) \times \sin(65^\circ) = 0{,}1818 \times 0{,}9063 \approx 0{,}1648\ \mathrm{nm} = 1{,}648\ \mathrm{\AA}"
    story.append(he.build_intermediate_equation(dg_step3_txt, dg_step3_eq, styles=styles, is_expanded_from_slide=True))

    # Giai đoạn 4: Biến thể mở rộng & Quét tham số tiệm cận
    story.append(he.make_paragraph("Giai đoạn 4: Biến thể mở rộng &amp; Quét tham số tiệm cận", styles["H3"]))
    g5_p4 = (
        "<b>Đánh giá sai số và sự nhất quán hoàn hảo:</b><br/>"
        "• Sai số tương đối giữa bước sóng lý thuyết de Broglie (0.1668 nm) và bước sóng đo đạc thực nghiệm từ góc cực đại tán xạ (0.1648 nm) "
        "chỉ là: |0.1668 − 0.1648| / 0.1668 ≈ 1.2%! Sự sai lệch nhỏ bé này hoàn toàn nằm trong phạm vi sai số thực nghiệm của góc đo và hằng số mạng.<br/>"
        "• <i>Thí nghiệm G.P. Thomson:</i> Thomson sử dụng chùm electron năng lượng cao (~10–50 keV) bắn xuyên qua màng mỏng kim loại đa tinh thể (vàng, bạch kim, nhôm). "
        "Vì tinh thể trong màng mỏng định hướng ngẫu nhiên theo mọi phương không gian, hình ảnh giao thoa thu được trên tấm kính ảnh là các vòng tròn đồng tâm sắc nét "
        "(hình ảnh nhiễu xạ bột Debye - Scherrer). Bán kính của các vòng tròn tỷ lệ nghịch với căn bậc hai của điện thế gia tốc √<i>U</i>, "
        "khẳng định tuyệt đối bước sóng <i>λ</i> của chùm electron tỷ lệ nghịch với căn bậc hai của điện thế <i>U</i>."
    )
    story.append(he.make_paragraph(g5_p4, styles["Body"]))
    story.append(Spacer(1, 6))

    # Giai đoạn 5: Thử thách CER
    story.append(he.make_paragraph("Giai đoạn 5: Thử thách tự đánh giá định dạng lập luận CER", styles["H3"]))
    cer_dg = (
        "<b>Thử thách chẩn đoán kỹ thuật CER:</b><br/>"
        "• <b>[Khẳng định (Claim)]:</b> Thí nghiệm Davisson - Germer đã loại trừ hoàn toàn khả năng giải thích hiện tượng cực đại tán xạ "
        "bằng mô hình hạt cổ điển (ví dụ mô hình va chạm quả cầu cứng dạng hạt vi mô).<br/>"
        "• <b>[Bằng chứng định lượng (Evidence)]:</b> Nếu electron là các hạt cơ học cổ điển va chạm với các nguyên tử trên bề mặt gồ ghề, "
        "chúng sẽ bị tán xạ phân tán ngẫu nhiên về mọi phía. Cường độ chùm phản xạ phải biến thiên êm dịu, đơn điệu và liên tục theo góc <i>φ</i> "
        "(không có bất kỳ lý do cơ học nào để cường độ tăng đột ngột gấp nhiều lần tại đúng 50° và sụt giảm ngay lập tức ở 45° và 55°).<br/>"
        "• <b>[Lập luận vi mô (Reasoning)]:</b> Sự xuất hiện của đỉnh cường độ cực đại sắc nét tại một góc rời rạc xác định chỉ có thể xảy ra khi có "
        "hiện tượng <i>giao thoa tăng cường</i> giữa các sóng thành phần có pha kết hợp. Hiện tượng giao thoa là thuộc tính độc quyền của sóng "
        "(nơi các đỉnh sóng gặp nhau và cộng hưởng biên độ). Điều này chứng minh không thể chối cãi rằng mỗi electron chuyển động mang bản chất sóng.<br/>"
        "• <b>[Phản biện &amp; Điểm mù (Counter-argument &amp; Pitfall)]:</b> Chi tiết lịch sử mang tính định mệnh: Ban đầu, mẫu Niken của Davisson là đa tinh thể "
        "và họ không quan sát thấy bất kỳ cực đại nào. Trong một tai nạn nổ bình chân không, khối Niken bị oxy hóa ở nhiệt độ cao. Davisson và Germer "
        "đã phải nung mẫu trong lò nhiệt độ cao nhiều giờ để khử oxit. Quá trình ủ nhiệt kéo dài vô tình đã làm các vi tinh thể nhỏ kết tinh lại thành "
        "các miền đơn tinh thể khổng lồ! Nếu không có sự cố nung đơn tinh thể này, tính chất sóng của electron đã không thể bộc lộ rõ rệt."
    )
    story.append(he.make_paragraph(cer_dg, styles["Body"]))
    story.append(Spacer(1, 14))

    # =========================================================================
    # TỔNG KẾT MỤC 2.2 & BẢN ĐỒ ĐIỀU HƯỚNG MỤC 2.3
    # =========================================================================
    story.append(he.make_paragraph("Tổng kết Mục 2.2 &amp; Bản đồ Điều hướng Mục 2.3 tiếp theo", styles["H2"]))
    summary_text = (
        "<b>Ma trận tổng hợp kiến thức cốt lõi Mục 2.2:</b><br/>"
        "1. <i>Hiệu ứng quang điện:</i> Khẳng định bản chất hạt của bức xạ điện từ; photon mang năng lượng gián đoạn <i>E</i> = <i>hν</i>; "
        "phương trình Einstein bảo toàn năng lượng <i>hν</i> = <i>A</i><sub>exit</sub> + <i>eU</i><sub>h</sub> giải thích trọn vẹn giới hạn quang điện và tính tức thời.<br/>"
        "2. <i>Tán xạ Compton:</i> Minh chứng trực tiếp về động lượng của photon <i>p</i> = <i>h</i>·<i>λ</i><sup>−1</sup>; va chạm đàn hồi tương đối tính 2 chiều dẫn xuất độ dịch "
        "bước sóng phổ quát Δ<i>λ</i> = <i>λ</i><sub>C</sub>(1 − cos <i>θ</i>) với bước sóng Compton <i>λ</i><sub>C</sub> = 2.426 pm.<br/>"
        "3. <i>Giả thiết de Broglie:</i> Đối xứng hóa thiên nhiên; mọi hạt vật chất đều gắn liền sóng liên kết <i>λ</i> = <i>h</i>·<i>p</i><sup>−1</sup>; "
        "hệ thức kỹ thuật electron <i>λ</i> ≈ 12.26·(√<i>U</i>)<sup>−1</sup> (Å) định hình nguyên lý kính hiển vi điện tử TEM/SEM.<br/>"
        "4. <i>Nhiễu xạ Bragg:</i> Giao thoa tăng cường từ các mặt phẳng tinh thể song song 2<i>d</i> sin <i>θ</i> = <i>nλ</i>; điều kiện bước sóng <i>λ</i> ≤ 2<i>d</i> "
        "biến tinh thể chất rắn thành cách tử tự nhiên cho tia X và sóng electron.<br/>"
        "5. <i>Thí nghiệm Davisson - Germer &amp; G.P. Thomson:</i> Xác nhận thực nghiệm hoàn hảo bản chất sóng của electron trên đơn tinh thể Ni tại <i>U</i> = 54 V, "
        "<i>φ</i> = 50° với sai số dưới 1.2%, khép lại kỷ nguyên cổ điển và mở toang cánh cửa cơ học lượng tử.<br/><br/>"
        "<b>Mỏ neo điều hướng Mục 2.3 tiếp theo:</b><br/>"
        "Mục 2.3 sẽ giải mã câu hỏi nền tảng: Nếu hạt là một sóng, thì bản chất toán học của sóng đó là gì? "
        "Chúng ta sẽ nghiên cứu <i>Hàm sóng phẳng de Broglie dạng phức, Tiên đề xác suất Max Born, Cấu trúc Bó sóng (Wave Packet), "
        "Nguyên lý bất định Heisenberg và Phương trình vi phân Schrödinger</i>."
    )
    story.append(he.make_paragraph(summary_text, styles["Body"]))
    story.append(Spacer(1, 10))

    # 3. Biên dịch tài liệu
    print("Bắt đầu gọi doc.build(story)...")
    doc.build(story)
    print("Biên dịch thành công Mục 2.2!")

    # 4. Kiểm tra chất lượng và dung lượng
    compliance = he.assert_monograph_compliance(target_pdf, min_pages=5)
    print("Kết quả kiểm toán chất lượng (Compliance) Mục 2.2:", compliance)

    return compliance

if __name__ == "__main__":
    build_pdf()

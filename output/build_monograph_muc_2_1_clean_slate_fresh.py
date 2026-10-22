import os
import sys
import tempfile
import shutil

sys.stdout.reconfigure(encoding="utf-8")

from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.colors import HexColor

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\monograph-pdf-publisher\scripts")
import hust_pdf_engine as hpe

# ---------------------------------------------------------------------------
# ĐƯỜNG DẪN TỆP NGUỒN VÀ ĐÍCH TRÊN GOOGLE DRIVE G:\
# ---------------------------------------------------------------------------
drive_base = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý"
img_dir = os.path.join(drive_base, "Kho_Hinh_Anh")
pdf_dir = os.path.join(drive_base, "Bai_Giang_Dong_Goi")
os.makedirs(pdf_dir, exist_ok=True)

target_pdf_path = os.path.join(pdf_dir, "Chuyen_Khao_Laser_Diode_Muc_2.1.pdf")

# Hình ảnh thành phần
fig_goc_2_1 = os.path.join(img_dir, "[Goc]_Figure_2.1_Gian_do_dai_nang_luong_diode_di_the_kep_DH.png")
fig_goc_2_2 = os.path.join(img_dir, "[Goc]_Figure_2.2_Mo_hinh_ho_chua_hat_tai_duoi_nguong.png")
fig_sim_1 = os.path.join(img_dir, "[Mo_Phong]_Muc_2.1_Cau_Truc_Dai_Nang_Luong_Va_Mode_Quang_DH.png")
fig_sim_2 = os.path.join(img_dir, "[Mo_Phong]_Muc_2.1_Dong_Luc_Hoc_Tai_Hop_ABC_Va_Hieu_Suat_Buc_Xa.png")

styles = hpe.get_hust_styles()
styles["BodyText"] = styles["Body"]

flowables = []

# ===========================================================================
# TIÊU ĐỀ CHUYÊN KHẢO MỤC 2.1 (H1)
# ===========================================================================
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("Mục 2.1: Tiếp cận hiện tượng học đối với Laser Diode"),
        styles["H1"],
    )
)
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs(
            "<i>(A Phenomenological Approach to Diode Lasers — Coldren &amp; Corzine, Chương 2, trang 28–30)</i>"
        ),
        styles["Caption"],
    )
)
flowables.append(Spacer(1, 10))

# ===========================================================================
# LUẬN ĐIỂM VI MÔ MPT 2.1.1 (H2)
# ===========================================================================
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs(
            "Luận điểm 2.1.1: Tiếp giáp dị thể kép và mô hình phương trình tốc độ hạt tải hiện tượng học trong vùng tích cực laser diode"
        ),
        styles["H2"],
    )
)
flowables.append(Spacer(1, 6))

# ---------------------------------------------------------------------------
# KHỐI 1: TRỰC QUAN HÓA & NGHỊCH LÝ KHỞI ĐẦU (VISUAL ANCHOR & PARADOX)
# ---------------------------------------------------------------------------
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("Khối 1: Trực quan hóa &amp; Nghịch lý khởi đầu"),
        styles["H3"],
    )
)

# Causal Micro-block 1: Dị thể kép và giam giữ hạt tải
flowables.append(
    hpe.make_paragraph(
        "Cấu trúc laser bán dẫn hiện đại được thiết lập dựa trên tiếp giáp dị thể kép (Double Heterostructure - DH), "
        "trong đó một lớp tích cực vật liệu dải hẹp được kẹp chặt giữa hai lớp bọc có độ rộng vùng cấm lớn hơn.<br/>"
        "↳ Tiếp giáp dị thể kép (Double Heterostructure - DH): Cấu trúc phân lớp bán dẫn tạo vách thế năng giam giữ hạt tải và dẫn sóng quang học song song.<br/>"
        "Độ gián đoạn của dải dẫn <i>&Delta;E<sub>c</sub></i> và dải hóa trị <i>&Delta;E<sub>v</sub></i> thiết lập các hàng rào thế năng vững chắc, "
        "ngăn chặn triệt để sự khuếch tán thất thoát của electron và lỗ trống ra khỏi thể tích hoạt tính.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 6))

# Embed Hình gốc 2.1
flowables.append(
    hpe.embed_figure_with_caption(
        fig_goc_2_1,
        "Hình 2.1: Giản đồ dải năng lượng của diode tiếp giáp dị thể kép (DH) dưới điều kiện phân cực thuận (Coldren &amp; Corzine). "
        "Ba mắt xích vật lý: (a) Vách thế giam giữ điện tử <i>&Delta;E<sub>c</sub></i> và lỗ trống <i>&Delta;E<sub>v</sub></i>; "
        "(b) Vùng tích cực dải hẹp duy trì nồng độ hạt tải tiêm vượt mức cân bằng nhiệt; "
        "(c) Tái hợp bức xạ lưỡng phân tử phát xạ photon năng lượng xấp xỉ <i>E<sub>g</sub></i>.",
        kind="orig",
        styles=styles,
    )
)

# Causal Micro-block 2: Giam giữ mode quang học
flowables.append(
    hpe.make_paragraph(
        "Vùng tích cực không chỉ có vai trò giam giữ thế năng cơ học lượng tử của hạt tải, mà còn đóng vai trò là lõi của ống dẫn sóng điện môi phẳng "
        "do có chiết suất quang học cao hơn đáng kể so với hai lớp bọc dải rộng.<br/>"
        "↳ Chiết suất quang học (Refractive Index - <i>n</i>): Thông số điều khiển vận tốc pha và bẻ cong phân bố trường điện từ của mode dẫn sóng.<br/>"
        "Sự chênh lệch chiết suất này bẫy trọn vẹn mode quang cơ bản TE<sub>00</sub> lan truyền dọc theo trục cộng hưởng, tối ưu hóa hệ số giam giữ quang học &Gamma;.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 6))

# Embed Hình mô phỏng 1 (Structural Simulation)
flowables.append(
    hpe.embed_figure_with_caption(
        fig_sim_1,
        "Hình mô phỏng 2.1 (a): Cấu trúc dải năng lượng <i>E<sub>c</sub>(z)</i>, <i>E<sub>v</sub>(z)</i> và phân bố cường độ mode quang TE<sub>00</sub> trong dị thể kép GaAs – AlGaAs. "
        "Ba mắt xích kiểm chứng: (a) Độ gián đoạn dải dẫn <i>&Delta;E<sub>c</sub></i> &approx; 0,224 eV và dải hóa trị <i>&Delta;E<sub>v</sub></i> &approx; 0,150 eV; "
        "(b) Bề rộng vùng tích cực <i>d</i> = 200 nm giam giữ mật độ hạt tải cao; "
        "(c) Mode sóng quang học chồng lấn mạnh mẽ lên vùng tích cực với hệ số giam giữ &Gamma; &approx; 0,35.",
        kind="sim",
        styles=styles,
    )
)

# Causal Micro-block 3: Nghịch lý homojunction
flowables.append(
    hpe.make_paragraph(
        "Nghịch lý công nghệ khởi đầu: Tại sao các tiếp giáp đồng thể (Homojunction) <i>p</i>–<i>n</i> thông thường không thể hoạt động liên tục ở nhiệt độ phòng 300 K? "
        "Trong tiếp giáp đồng thể, các hạt tải thiểu số khuếch tán tự do ra vùng rộng hàng chục micromet dọc theo hai phía tiếp giáp, "
        "dẫn đến mật độ dòng ngưỡng yêu cầu để đảo mật độ vượt quá 50 kA&middot;cm<sup>-2</sup> và gây quá nhiệt phá hủy linh kiện. "
        "Tiếp giáp dị thể kép DH giải quyết triệt để nút thắt này bằng cách nén toàn bộ dòng tiêm vào một thể tích hoạt tính nano siêu nhỏ, "
        "hạ dòng ngưỡng xuống dưới 1 kA&middot;cm<sup>-2</sup> để duy trì phát xạ kích thích ổn định.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 10))

# ---------------------------------------------------------------------------
# KHỐI 2: CỐT LÕI FEYNMAN (FEYNMAN CORE)
# ---------------------------------------------------------------------------
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("Khối 2: Cốt lõi Feynman"),
        styles["H3"],
    )
)

flowables.append(
    hpe.make_paragraph(
        "Trực quan hóa Feynman 3 nhịp: Hãy hình dung vùng tích cực của laser diode như một hồ chứa nước kín có thể tích cố định <i>V</i>. "
        "Dòng điện tiêm <i>I</i> đóng vai trò là dòng nước bơm liên tục vào đỉnh hồ với hiệu suất van tiêm <i>&eta;<sub>i</sub></i>.<br/>"
        "↳ Hiệu suất tiêm nội (Internal Injection Efficiency - <i>&eta;<sub>i</sub></i>): Tỷ lệ phần trăm dòng điện ngoài thực sự đi vào tái hợp tại vùng tích cực.<br/>"
        "Mực nước dâng lên đại diện cho mật độ hạt tải <i>N</i>, và hồ chứa này có ba vòi xả đáy cạnh tranh khốc liệt:",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 4))

flowables.append(
    hpe.make_paragraph(
        "1. Vòi xả rãnh cặn Shockley-Read-Hall (SRH <i>AN</i>): Nước rò rỉ qua các vết nứt và khuyết tật mạng tinh thể, tiêu tán năng lượng thành phonon dao động mạng mà không sinh ra photon hữu ích.<br/>"
        "2. Dòng xả chính có ích (Bức xạ <i>BN</i><sup>2</sup>): Dòng nước sạch phun qua van tạo ánh sáng, trong đó một điện tử tái hợp trực tiếp với một lỗ trống để giải phóng một photon tự phát.<br/>"
        "3. Vòi xả xoáy va đập (Auger <i>CN</i><sup>3</sup>): Tại mật độ hạt tải cao, sự va chạm ba hạt truyền toàn bộ động năng cho một hạt thứ ba bay lên dải cao rồi phát nhiệt, làm sụt giảm nghiêm trọng hiệu suất lượng tử.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 6))

# Embed Hình gốc 2.2
flowables.append(
    hpe.embed_figure_with_caption(
        fig_goc_2_2,
        "Hình 2.2: Mô hình hồ chứa hạt tải dưới ngưỡng trong vùng tích cực laser diode (Coldren &amp; Corzine). "
        "Ba mắt xích thủy động lực học: (a) Tốc độ sinh hạt tải do dòng tiêm ngoài <i>&eta;<sub>i</sub> I / (q V)</i>; "
        "(b) Hồ chứa mật độ hạt tải <i>N</i> trong thể tích tích cực <i>V = d &middot; w &middot; L</i>; "
        "(c) Ba kênh tái hợp đáy hồ <i>R(N) = A N + B N<sup>2</sup> + C N<sup>3</sup></i> cạnh tranh tiêu tán hạt tải.",
        kind="orig",
        styles=styles,
    )
)

flowables.append(
    hpe.make_paragraph(
        "Phương trình vi phân tốc độ hạt tải bảo toàn điện tích trong vùng tích cực được thiết lập bằng cân bằng dòng vào và dòng ra vi mô:",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 4))

# HỆ THỨC CỘT TRỤ KHỐI 2 (LEVEL-3 PILLAR EQUATION)
eq_pillar_latex = r"\frac{\mathrm{d}N}{\mathrm{d}t} = \frac{\eta_i I}{q V} - R(N) = \frac{\eta_i I}{q V} - \left( A N + B N^2 + C N^3 \right)"

nomenclature_rows = [
    (
        "Mật độ hạt tải",
        "<i>N</i>",
        "cm<sup>-3</sup>",
        "Nồng độ điện tử và lỗ trống tự do giam giữ trong thể tích tích cực",
    ),
    (
        "Hiệu suất tiêm nội",
        "<i>&eta;<sub>i</sub></i>",
        "1",
        "Tỷ lệ hạt tải tiêm vào tái hợp trong vùng tích cực thay vì rò rỉ",
    ),
    (
        "Dòng điện bơm ngoài",
        "<i>I</i>",
        "A (mA)",
        "Cường độ dòng điện phân cực thuận cung cấp từ nguồn điều khiển",
    ),
    (
        "Điện tích nguyên tố",
        "<i>q</i>",
        "C",
        "Hằng số điện tích cơ bản của electron (1,602 176 634 &times; 10<sup>-19</sup> C)",
    ),
    (
        "Thể tích vùng tích cực",
        "<i>V</i>",
        "cm<sup>3</sup>",
        "Thể tích hình học khoang hoạt tính: tích số <i>V = d &middot; w &middot; L</i>",
    ),
    (
        "Hệ số tái hợp SRH",
        "<i>A</i>",
        "s<sup>-1</sup>",
        "Tốc độ bẫy hạt tải phi bức xạ qua tâm sai hỏng mạng tinh thể",
    ),
    (
        "Hệ số tái hợp bức xạ",
        "<i>B</i>",
        "cm<sup>3</sup>&middot;s<sup>-1</sup>",
        "Xác suất tái hợp trực tiếp tự phát giữa electron và lỗ trống tạo photon",
    ),
    (
        "Hệ số tái hợp Auger",
        "<i>C</i>",
        "cm<sup>6</sup>&middot;s<sup>-1</sup>",
        "Xác suất tán xạ ba hạt truyền năng lượng tái hợp cho hạt thứ ba dưới dạng nhiệt",
    ),
]

flowables.append(
    hpe.build_target_equation_block(
        eq_pillar_latex,
        nomenclature_rows,
        styles=styles,
    )
)
flowables.append(Spacer(1, 10))

# ---------------------------------------------------------------------------
# KHỐI 3: CHUỖI SUY LUẬN NHÂN QUẢ (CAUSAL FLOWCHAIN)
# ---------------------------------------------------------------------------
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("Khối 3: Chuỗi suy luận nhân quả"),
        styles["H3"],
    )
)

flowables.append(
    hpe.make_paragraph(
        "Bước 1: Thiết lập định luật bảo toàn hạt tải trong vi phân thể tích hoạt tính. "
        "Số lượng hạt tải tích tụ trong thể tích <i>V</i> tại mỗi thời điểm <i>t</i> là hiệu số giữa số electron tiêm vào qua tiếp giáp và số electron bị triệt tiêu qua các kênh tái hợp. "
        "Tốc độ sinh hạt tải trên một đơn vị thể tích được biểu diễn tường minh qua mật độ dòng điện:",
        styles["Body"],
    )
)

flowables.append(
    hpe.build_intermediate_equation(
        "Tốc độ sinh hạt tải thể tích tỷ lệ thuận với dòng bơm và tỷ lệ nghịch với thể tích hình học:",
        r"G_{\mathrm{gen}} = \frac{\eta_i I}{q V} = \frac{\eta_i J}{q d}",
        styles=styles,
        ocr_idx=1,
    )
)

flowables.append(
    hpe.make_paragraph(
        "Bước 2: Phân tách và tường minh thời gian sống vi mô của hạt tải. "
        "Thời gian sống hạt tải toàn phần <i>&tau;(N)</i> được định nghĩa là tỷ số giữa mật độ hạt tải hiện có và tổng tốc độ tái hợp:",
        styles["Body"],
    )
)

flowables.append(
    hpe.build_intermediate_equation(
        "Thời gian sống hạt tải toàn phần nghịch đảo với tổng tốc độ các kênh tái hợp:",
        r"\frac{1}{\tau(N)} = \frac{R(N)}{N} = A + B N + C N^2",
        styles=styles,
        ocr_idx=2,
    )
)

flowables.append(
    hpe.make_paragraph(
        "Bước 3: Dẫn xuất thời gian sống vi phân dưới kích thích tín hiệu nhỏ. "
        "Khi điều chế laser bằng tín hiệu xoay chiều biên độ nhỏ, tốc độ đáp ứng của nồng độ hạt tải phụ thuộc vào đạo hàm vi phân của tốc độ tái hợp theo mật độ hạt tải:",
        styles["Body"],
    )
)

flowables.append(
    hpe.build_intermediate_equation(
        "Đạo hàm vi phân xác định thời gian sống tín hiệu nhỏ:",
        r"\frac{1}{\tau_{\Delta}(N)} = \frac{\mathrm{d}R}{\mathrm{d}N} = A + 2 B N + 3 C N^2",
        styles=styles,
        is_expanded_from_slide=True,
    )
)

flowables.append(
    hpe.make_paragraph(
        "Bước 4: Trạng thái dừng dưới ngưỡng kích thích. "
        "Tại chế độ kích thích một chiều không đổi trước khi đạt ngưỡng phát laser, mật độ hạt tải duy trì không đổi theo thời gian, "
        "dẫn đến đạo hàm thời gian triệt tiêu: d<i>N</i>/d<i>t</i> = 0. Khi đó toàn bộ dòng tiêm ngoài cân bằng chính xác với tổng tổn hao tái hợp:",
        styles["Body"],
    )
)

flowables.append(
    hpe.build_intermediate_equation(
        "Cân bằng dòng dừng dưới ngưỡng liên kết trực tiếp dòng điều khiển với mật độ hạt tải:",
        r"I_{\mathrm{steady}} = \frac{q V}{\eta_i} \left( A N + B N^2 + C N^3 \right)",
        styles=styles,
        ocr_idx=3,
    )
)
flowables.append(Spacer(1, 10))

# ---------------------------------------------------------------------------
# KHỐI 4: THỬ NGHIỆM TIỆM CẬN & CHỐT CHẶN TRỰC GIÁC (ASYMPTOTIC SANITY CHECK)
# ---------------------------------------------------------------------------
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("Khối 4: Thử nghiệm tiệm cận &amp; Chốt chặn trực giác"),
        styles["H3"],
    )
)

flowables.append(
    hpe.make_paragraph(
        "Hiệu suất lượng tử bức xạ nội <i>&eta;<sub>rad</sub>(N)</i> là đại lượng cốt lõi định lượng tỷ lệ hạt tải chuyển hóa thành ánh sáng tự phát so với tổng lượng hạt tải bị tiêu tán:",
        styles["Body"],
    )
)

flowables.append(
    hpe.build_intermediate_equation(
        "Hiệu suất lượng tử bức xạ nội là hàm phụ thuộc phi tuyến vào mật độ hạt tải:",
        r"\eta_{\mathrm{rad}}(N) = \frac{R_{\mathrm{rad}}(N)}{R(N)} = \frac{B N^2}{A N + B N^2 + C N^3} = \frac{B N}{A + B N + C N^2}",
        styles=styles,
    )
)

flowables.append(
    hpe.make_paragraph(
        "Kiểm tra tiệm cận mật độ thấp (<i>N</i> &ll; <i>N</i><sub>opt</sub>): Khi dòng tiêm rất nhỏ, số lượng hạt tải ít khiến kênh SRH qua bẫy chiếm ưu thế tuyệt đối. "
        "Số hạng <i>A</i> trong mẫu số áp đảo hoàn toàn <i>BN</i> và <i>CN</i><sup>2</sup>, khiến hiệu suất bức xạ suy biến tuyến tính theo mật độ: "
        "<i>&eta;<sub>rad</sub></i> &approx; <i>BN / A</i> &rarr; 0. Tại vùng này, diode tiêu tốn năng lượng chủ yếu để nuôi các bẫy khuyết tật mạng mà hầu như không phát quang.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 4))

flowables.append(
    hpe.make_paragraph(
        "Kiểm tra tiệm cận mật độ cao (<i>N</i> &gg; <i>N</i><sub>opt</sub>): Khi bơm dòng cực mạnh, mật độ hạt tải tăng vọt khiến kênh va đập Auger bùng nổ theo lũy thừa bậc ba <i>CN</i><sup>3</sup>. "
        "Số hạng <i>CN</i><sup>2</sup> trong mẫu số vượt trội, làm hiệu suất bức xạ sụt giảm nghịch đảo: <i>&eta;<sub>rad</sub></i> &approx; <i>B / (CN)</i> &rarr; 0. "
        "Hiện tượng này giải thích trực tiếp cơ chế suy giảm hiệu suất (Efficiency Droop) và phát nhiệt dữ dội của diode quang ở mật độ dòng lớn.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 4))

flowables.append(
    hpe.build_intermediate_equation(
        "Điểm cực trị xác định mật độ hạt tải tối ưu và hiệu suất cực đại:",
        r"\frac{\mathrm{d}\eta_{\mathrm{rad}}}{\mathrm{d}N} = 0 \Longrightarrow N_{\mathrm{opt}} = \sqrt{\frac{A}{C}}, \quad \eta_{\max} = \frac{B}{2 \sqrt{A C} + B}",
        styles=styles,
        is_expanded_from_slide=True,
    )
)
flowables.append(Spacer(1, 6))

# Embed Hình mô phỏng 2 (Performance & Trade-off Sweep)
flowables.append(
    hpe.embed_figure_with_caption(
        fig_sim_2,
        "Hình mô phỏng 2.1 (b): Động lực học tái hợp vi mô <i>A, B, C</i> và hiệu suất lượng tử bức xạ nội <i>&eta;</i><sub>rad</sub>(<i>N</i>) trong GaAs ở 300 K. "
        "Hai đồ thị đối chuẩn: (a) Đồ thị Log-Log phân tách ba miền thống trị của SRH <i>AN</i>, bức xạ <i>BN</i><sup>2</sup> và Auger <i>CN</i><sup>3</sup>; "
        "(b) Đồ thị bán logarit định vị đỉnh hiệu suất cực đại <i>&eta;</i><sub>max</sub> &approx; 47,8% tại mật độ tối ưu <i>N</i><sub>opt</sub> &approx; 1,83 &times; 10<sup>18</sup> cm<sup>-3</sup>.",
        kind="sim",
        styles=styles,
    )
)

# DETACHED PARAMETER CARD (Bảng tham số vật liệu rời)
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("<b>Bảng thẻ tham số động học vi mô (Detached Parameter Card) — GaAs ở 300 K</b>"),
        styles["Caption"],
    )
)

param_headers = [
    Paragraph(hpe.wrap_math_glyphs("Tham số vật liệu"), styles["TableHeader"]),
    Paragraph(hpe.wrap_math_glyphs("Ký hiệu"), styles["TableHeader"]),
    Paragraph(hpe.wrap_math_glyphs("Giá trị chuẩn"), styles["TableHeader"]),
    Paragraph(hpe.wrap_math_glyphs("Đơn vị"), styles["TableHeader"]),
    Paragraph(hpe.wrap_math_glyphs("Ý nghĩa vật lý"), styles["TableHeader"]),
]
param_rows = [
    [
        Paragraph(hpe.wrap_math_glyphs("Hệ số bẫy SRH"), styles["TableCell"]),
        Paragraph(hpe.wrap_math_glyphs("<i>A</i>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("1,0 &times; 10<sup>8</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("s<sup>-1</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("Tái hợp phi bức xạ qua khuyết tật sâu"), styles["TableCell"]),
    ],
    [
        Paragraph(hpe.wrap_math_glyphs("Hệ số bức xạ tự phát"), styles["TableCell"]),
        Paragraph(hpe.wrap_math_glyphs("<i>B</i>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("1,0 &times; 10<sup>-10</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("cm<sup>3</sup>&middot;s<sup>-1</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("Phát xạ photon trực tiếp giữa hai dải"), styles["TableCell"]),
    ],
    [
        Paragraph(hpe.wrap_math_glyphs("Hệ số va đập Auger"), styles["TableCell"]),
        Paragraph(hpe.wrap_math_glyphs("<i>C</i>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("3,0 &times; 10<sup>-29</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("cm<sup>6</sup>&middot;s<sup>-1</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("Tổn hao ba hạt truyền nhiệt phonon"), styles["TableCell"]),
    ],
    [
        Paragraph(hpe.wrap_math_glyphs("Mật độ tối ưu"), styles["TableCell"]),
        Paragraph(hpe.wrap_math_glyphs("<i>N</i><sub>opt</sub>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("1,83 &times; 10<sup>18</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("cm<sup>-3</sup>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("Cân bằng hoàn hảo giữa SRH và Auger"), styles["TableCell"]),
    ],
    [
        Paragraph(hpe.wrap_math_glyphs("Hiệu suất cực đại"), styles["TableCell"]),
        Paragraph(hpe.wrap_math_glyphs("<i>&eta;</i><sub>max</sub>"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("47,8"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("%"), styles["TableCellCenter"]),
        Paragraph(hpe.wrap_math_glyphs("Hiệu suất lượng tử nội cao nhất có thể đạt"), styles["TableCell"]),
    ],
]

param_table = Table(
    [param_headers] + param_rows,
    colWidths=[105.0, 50.0, 95.0, 70.0, hpe.PRINTABLE_WIDTH - 320.0],
    repeatRows=1,
)
param_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), hpe.COLOR_TABLE_HEADER_BG),
            ("GRID", (0, 0), (-1, -1), 0.5, hpe.COLOR_BORDER_GRAY),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ]
    )
)
flowables.append(param_table)
flowables.append(Spacer(1, 10))

# ---------------------------------------------------------------------------
# KHỐI 5: THỬ THÁCH PHẢN XẠ & CHẨN ĐOÁN LỖI (CER DIAGNOSTIC CHALLENGE)
# ---------------------------------------------------------------------------
flowables.append(
    Paragraph(
        hpe.wrap_math_glyphs("Khối 5: Thử thách phản xạ &amp; Chẩn đoán lỗi"),
        styles["H3"],
    )
)

flowables.append(
    hpe.make_paragraph(
        "Tình huống chẩn đoán thực tế tại phòng thí nghiệm: Một kỹ sư quang điện tử tiến hành khảo sát đặc tuyến dòng – công suất quang của một diode laser GaAs/AlGaAs mới chế tạo ở 300 K. "
        "Khi bơm dòng điện xung <i>I</i> = 15 mA (dưới ngưỡng phát laser), công suất phát xạ tự phát thu được trên đầu dò suy giảm bất thường 40% so với mô hình thiết kế lý thuyết, "
        "đồng thời cảm biến hồng ngoại ghi nhận nhiệt độ phiến tăng vọt. Kỹ sư vội vã kết luận: 'Lỗi hoàn toàn do suy thoái lớp tiếp xúc kim loại Ohmic làm sụt giảm hiệu suất tiêm hạt tải <i>&eta;<sub>i</sub></i>'.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 4))

flowables.append(
    hpe.make_paragraph(
        "Yêu cầu đánh giá theo quy chuẩn CER (Claim – Evidence – Reasoning):<br/>"
        "1. <b>Claim (Khẳng định):</b> Kết luận quy kết nguyên nhân cho điện trở tiếp xúc Ohmic và <i>&eta;<sub>i</sub></i> của kỹ sư có thỏa đáng về mặt bản chất vật lý bán dẫn không?<br/>"
        "2. <b>Evidence (Bằng chứng):</b> Phép đo thời gian sống vi phân tín hiệu nhỏ <i>&tau;</i><sub>&Delta;</sub> và đo phổ phát xạ tự phát ở các mức dòng khác nhau sẽ cung cấp những bằng chứng thực nghiệm nào để phân biệt giữa suy giảm <i>&eta;<sub>i</sub></i> và sự kích hoạt của các tâm khuyết tật sâu SRH hoặc tổn hao nhiệt Auger?<br/>"
        "3. <b>Reasoning (Lập luận nguyên lý đầu):</b> Dựa trên phương trình tốc độ hạt tải và mô hình hồ chứa ba vòi rò rỉ, hãy xây dựng chuỗi lập luận logic giải thích tại sao hiện tượng sụt giảm công suất quang đi kèm với phát nhiệt mạnh là dấu hiệu đặc trưng không thể chối cãi của quá trình va đập Auger hoặc rò rỉ nhiệt hạt tải qua vách dị thể <i>&Delta;E<sub>c</sub></i>.",
        styles["Body"],
    )
)
flowables.append(Spacer(1, 14))

# ===========================================================================
# BIÊN DỊCH VÀ KIỂM CHỨNG TOÀN TRÌNH
# ===========================================================================
print("Building monograph PDF via BookmarkDocTemplate...")
doc = hpe.BookmarkDocTemplate(target_pdf_path)
doc.build(flowables, canvasmaker=hpe.NumberedBookmarkCanvas)

print(f"Monograph compiled successfully: {target_pdf_path}")
print(f"File size: {os.path.getsize(target_pdf_path)/1024:.1f} KB")

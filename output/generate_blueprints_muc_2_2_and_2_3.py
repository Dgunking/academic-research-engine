# -*- coding: utf-8 -*-
"""
Generate Blueprint JSON for Muc 2.2 and Muc 2.3 (Cơ sở vật lý và công nghệ nano)
Adhering to Pydantic contract and HUST 5-stage pedagogical schema.
"""

import os
import sys
import json
import pydantic
from typing import List, Dict, Any

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

data_dir = r"d:\antigravity\academic-research-engine\data"
os.makedirs(data_dir, exist_ok=True)

class VisualAssetSpec(pydantic.BaseModel):
    image_file_path: str
    interaction_id: str
    aspect_ratio: str
    brand_palette_compliant: bool
    pedagogical_caption: str

class MicroPointTopic(pydantic.BaseModel):
    mpt_id: str
    concept_introduction: str
    visual_anchor: VisualAssetSpec
    minimal_working_example: str
    pillar_equation_latex: str
    nomenclature_table: List[Dict[str, str]]
    guided_practice_steps: List[str]
    variations_and_asymptotic_sweeps: List[str]
    student_challenges_cer: List[str]

class LessonDeliverable(pydantic.BaseModel):
    lesson_title: str
    section_id: str
    source_document_citations: List[str]
    micro_point_topics: List[MicroPointTopic]
    total_pages_estimate: int

# =============================================================================
# BLUEPRINT MUC 2.2
# =============================================================================
bp_2_2 = LessonDeliverable(
    lesson_title="Chương 2: Bản chất lượng tử của thế giới nano - Mục 2.2: Lưỡng tính sóng - hạt của bức xạ và vật chất",
    section_id="Mục 2.2",
    source_document_citations=[
        "Bài 2-Quantum nature.pdf (Slide 13 đến 19), Bộ môn Vật liệu Điện tử - Viện Vật lý Kỹ thuật HUST",
        "Charles P. Poole Jr., Frank J. Owens, Introduction to Nanotechnology, Wiley-Interscience, 2003",
        "Edward L. Wolf, Nanophysics and Nanotechnology, Wiley-VCH, 2006",
        "Arthur Beiser, Concepts of Modern Physics, 6th Edition, McGraw-Hill, 2003"
    ],
    total_pages_estimate=12,
    micro_point_topics=[
        # MPT 2.2.1
        MicroPointTopic(
            mpt_id="Luận điểm 2.2.1",
            concept_introduction="Lưỡng tính sóng - hạt của bức xạ điện từ & Hiệu ứng quang điện: Sự sụp đổ của điện từ học cổ điển Maxwell trước hiện tượng quang điện ngoài, giả thuyết lượng tử ánh sáng của Einstein (1905) và phương trình quang điện bảo toàn năng lượng.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Goc]_Muc_2.2_Hinh_01_So_Do_Thi_Nghiem_Quang_Dien.png",
                interaction_id="IMG_2.2.1_ORIG_PHOTOELECTRIC",
                aspect_ratio="1:1",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.2.1: Sơ đồ nguyên lý thí nghiệm hiệu ứng quang điện ngoài và mạch đo thế hãm Uh."
            ),
            minimal_working_example="Chiếu bức xạ đơn sắc bước sóng lambda tới bề mặt kim loại kiềm trong tế bào quang điện chân không, đo dòng quang điện bão hòa I_bh và hiệu điện thế hãm triệt tiêu dòng quang điện.",
            pillar_equation_latex=r"h\nu = A_{\mathrm{exit}} + E_{k,\mathrm{max}} = e\Phi + \frac{1}{2}m_0 v_{\mathrm{max}}^2 = e\Phi + e U_h",
            nomenclature_table=[
                {"name": "Năng lượng photon tới", "symbol": "h\\nu", "unit": "eV", "meaning": "Gói năng lượng gián đoạn của lượng tử ánh sáng tới bề mặt kim loại"},
                {"name": "Công thoát điện tử", "symbol": "A_{\\mathrm{exit}} = e\\Phi", "unit": "eV", "meaning": "Năng lượng tối thiểu cần cung cấp để giải phóng electron khỏi liên kết mạng tinh thể"},
                {"name": "Động năng ban đầu cực đại", "symbol": "E_{k,\\mathrm{max}}", "unit": "eV", "meaning": "Động năng lớn nhất của quang electron ngay sau khi bứt ra khỏi bề mặt catot"},
                {"name": "Hiệu điện thế hãm", "symbol": "U_h", "unit": "V", "meaning": "Điện thế ngược đặt giữa anot và catot để triệt tiêu hoàn toàn dòng quang điện"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Năng lượng photon tới được hấp thụ nguyên vẹn theo cơ chế tương tác đơn hạt (1 photon truyền toàn bộ năng lượng cho 1 electron).",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi phương trình Einstein xác định tần số giới hạn quang điện: h\nu_0 = A_{\mathrm{exit}} \implies \lambda_0 = hc / A_{\mathrm{exit}}.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập hệ thức điện thế hãm tuyến tính theo tần số: e U_h = h\nu - A_{\mathrm{exit}} \implies U_h = (h/e)\nu - \Phi."
            ],
            variations_and_asymptotic_sweeps=[
                "Khi cường độ ánh sáng I tăng nhưng tần số nu < nu_0: Tuyệt đối không có quang electron nào bứt ra bất kể thời gian chiếu sáng kéo dài bao lâu.",
                "Khi tần số nu > nu_0: Dòng điện bão hòa I_bh tỷ lệ thuận với thông lượng photon tới, trong khi điện thế hãm U_h chỉ phụ thuộc tuyến tính vào tần số nu."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao thuyết điện từ sóng cổ điển dự đoán thời gian tích lũy năng lượng để bứt electron lên tới vài giờ, trong khi thực nghiệm đo được trễ dưới 10^-9 s?"
            ]
        ),
        # MPT 2.2.2
        MicroPointTopic(
            mpt_id="Luận điểm 2.2.2",
            concept_introduction="Hiệu ứng tán xạ Compton & Dẫn xuất định lượng bước sóng dịch chuyển: Bằng chứng trực tiếp không thể chối cãi về động lượng của photon thông qua tán xạ đàn hồi giữa photon tia X và electron tự do theo thuyết tương đối hẹp (1923).",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.2_Pho_Tan_Xa_Compton_Cac_Goc.png",
                interaction_id="IMG_2.2.2_SIM_COMPTON_SPECTRUM",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.2.2: Đồ thị mô phỏng giải tích MATLAB phổ tán xạ Compton theo góc tán xạ theta, minh họa sự phân tách vạch không đổi lambda_0 và vạch dịch chuyển lambda'."
            ),
            minimal_working_example="Va chạm đàn hồi 2 chiều giữa photon tia X có năng lượng h nu và động lượng h/lambda với electron ban đầu đứng yên (năng lượng nghỉ m_0 c^2).",
            pillar_equation_latex=r"\Delta\lambda = \lambda' - \lambda_0 = \frac{h}{m_0 c}(1 - \cos\theta) = \lambda_C (1 - \cos\theta)",
            nomenclature_table=[
                {"name": "Độ dịch bước sóng Compton", "symbol": "\\Delta\\lambda = \\lambda' - \\lambda_0", "unit": "pm", "meaning": "Độ tăng bước sóng của photon sau khi tán xạ đàn hồi qua góc theta"},
                {"name": "Bước sóng Compton của electron", "symbol": "\\lambda_C = \\frac{h}{m_0 c}", "unit": "pm", "meaning": "Hằng số phổ quát đặc trưng: 2.42631023867 pm (0.02426 Angstrom)"},
                {"name": "Góc tán xạ của photon", "symbol": "\\theta", "unit": "độ", "meaning": "Góc lệch phương giữa chùm photon tán xạ và phương tới ban đầu"},
                {"name": "Khối lượng nghỉ của electron", "symbol": "m_0", "unit": "kg", "meaning": "Hằng số CODATA 2022: 9.1093837e-31 kg"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập định luật bảo toàn năng lượng tương đối tính toàn phần: h\nu_1 + m_0 c^2 = h\nu_2 + \sqrt{p_e^2 c^2 + m_0^2 c^4}.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập định luật bảo toàn véctơ động lượng: \vec{p}_1 = \vec{p}_2 + \vec{p}_e \implies p_e^2 = p_1^2 + p_2^2 - 2 p_1 p_2 \cos\theta.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Bình phương hai vế phương trình năng lượng, triệt tiêu p_e^2 c^2 và nhóm số hạng suy ra hệ thức kinh điển: \lambda' - \lambda_0 = \frac{h}{m_0 c}(1 - \cos\theta)."
            ],
            variations_and_asymptotic_sweeps=[
                "Tại góc tán xạ theta = 0 độ: Delta lambda = 0 (tán xạ thẳng về phía trước, photon không truyền động lượng cho electron).",
                "Tại góc tán xạ theta = 90 độ: Delta lambda = lambda_C = 2.426 pm.",
                "Tại góc tán xạ theta = 180 độ: Delta lambda = 2 lambda_C = 4.853 pm (tán xạ ngược cực đại, electron giật lùi với động năng lớn nhất)."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao trong phổ tán xạ Compton luôn tồn tại một vạch không dịch chuyển bước sóng lambda_0 song song với vạch dịch chuyển lambda'?"
            ]
        ),
        # MPT 2.2.3
        MicroPointTopic(
            mpt_id="Luận điểm 2.2.3",
            concept_introduction="Giả thiết sóng vật chất de Broglie & Ý nghĩa cơ bản: Bước nhảy lượng tử vĩ đại của Louis de Broglie (1924) mở rộng tính lưỡng tính sóng - hạt từ bức xạ điện từ sang toàn bộ các thực thể vật chất có khối lượng (electron, proton, nguyên tử).",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.2_Buoc_Song_De_Broglie_Theo_Dien_The.png",
                interaction_id="IMG_2.2.3_SIM_DE_BROGLIE_WAVELENGTH",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.2.3: Đồ thị mô phỏng bước sóng de Broglie của electron theo điện thế gia tốc U từ 1 V đến 1 MV, so sánh mô hình cổ điển và tương đối tính."
            ),
            minimal_working_example="Tính bước sóng de Broglie của electron gia tốc qua điện thế U = 54 V trong thí nghiệm Davisson - Germer và electron 100 keV trong kính hiển vi điện tử truyền qua TEM.",
            pillar_equation_latex=r"\lambda = \frac{h}{p} = \frac{h}{m v} = \frac{h}{\sqrt{2 m_0 E_k}} = \frac{h}{\sqrt{2 m_0 e U}} \approx \frac{1{,}226}{\sqrt{U(\mathrm{V})}}\ \mathrm{nm}",
            nomenclature_table=[
                {"name": "Bước sóng de Broglie", "symbol": "\\lambda", "unit": "nm", "meaning": "Bước sóng liên kết của sóng vật chất mô tả hành vi giao thoa và nhiễu xạ của hạt"},
                {"name": "Động lượng của hạt", "symbol": "p = mv", "unit": "kg·m/s", "meaning": "Đại lượng đặc trưng cho tính chất hạt cơ học vi mô"},
                {"name": "Điện thế gia tốc chùm electron", "symbol": "U", "unit": "V", "meaning": "Hiệu điện thế tĩnh điện dùng để cung cấp động năng eU cho hạt mang điện"},
                {"name": "Hằng số Planck", "symbol": "h", "unit": "J·s", "meaning": "Hằng số phổ quát lượng tử CODATA 2022: 6.62607015e-34 J·s"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Xuất phát từ hệ thức năng lượng photon E = h\nu = pc \implies p = h/\lambda. Đối xứng hóa sang vật chất: \lambda = h/p.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu diễn động lượng electron không tương đối tính theo động năng: E_k = p^2 / (2m_0) \implies p = \sqrt{2 m_0 E_k} = \sqrt{2 m_0 e U}.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay số các hằng số chuẩn CODATA: \lambda = \frac{6.626\times 10^{-34}}{\sqrt{2\times 9.109\times 10^{-31}\times 1.602\times 10^{-19}}}\frac{1}{\sqrt{U}} = \frac{1.226\times 10^{-9}}{\sqrt{U}}\ \mathrm{m} = \frac{12.26}{\sqrt{U}}\ \mathrm{\AA}."
            ],
            variations_and_asymptotic_sweeps=[
                "Ở thang vĩ mô (quả bóng m = 0.1 kg bay với tốc độ 10 m/s): Bước sóng lambda ~ 10^-34 m hoàn toàn không thể quan sát được hiện tượng sóng.",
                "Ở thang vi mô (electron U = 54 V): Bước sóng lambda = 0.167 nm đúng bằng thang đo khoảng cách giữa các mặt phẳng nguyên tử trong tinh thể."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao mắt người và các dụng cụ đo vĩ mô không bao giờ quan sát được tính chất sóng của các vật thể chuyển động thường ngày?"
            ]
        ),
        # MPT 2.2.4
        MicroPointTopic(
            mpt_id="Luận điểm 2.2.4",
            concept_introduction="Nhiễu xạ tia X và Định luật phản xạ Bragg: Cơ sở giao thoa sóng trên cách mạng tinh thể tuần hoàn ba chiều, nguyên lý giao thoa tăng cường của tia phản xạ từ các mặt phẳng Bragg song song.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Goc]_Muc_2.2_Hinh_05_Nhieu_Xa_Tia_X_Mat_Phang_Bragg.png",
                interaction_id="IMG_2.2.4_ORIG_BRAGG_DIFFRACTION",
                aspect_ratio="16:9",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.2.4: Sơ đồ tán xạ sóng trên các mặt phẳng nguyên tử song song và hiệu đường đi quang học theo định luật Bragg."
            ),
            minimal_working_example="Tia X đơn sắc bước sóng lambda tới mặt mạng tinh thể có khoảng cách mạng d dưới góc trượt theta (góc giữa tia tới và mặt phẳng tinh thể).",
            pillar_equation_latex=r"2d\sin\theta = n\lambda \quad (n = 1, 2, 3, \dots)",
            nomenclature_table=[
                {"name": "Khoảng cách giữa hai mặt mạng tinh thể", "symbol": "d", "unit": "nm", "meaning": "Khoảng cách vuông góc giữa hai mặt phẳng Bragg song song kế tiếp"},
                {"name": "Góc trượt Bragg", "symbol": "\\theta", "unit": "độ", "meaning": "Góc hợp bởi chùm tia tới (hoặc tia phản xạ) với mặt phẳng nguyên tử tinh thể"},
                {"name": "Bậc nhiễu xạ", "symbol": "n", "unit": "không thứ nguyên", "meaning": "Số nguyên biểu thị số bước sóng chênh lệch giữa hai tia kế tiếp"},
                {"name": "Bước sóng sóng tới", "symbol": "\\lambda", "unit": "nm", "meaning": "Bước sóng của bức xạ điện từ tia X hoặc sóng vật chất electron"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Xét hai tia sáng song song phản xạ trên hai mặt phẳng nguyên tử kế tiếp nhau cách nhau khoảng cách d.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hình học quang học cho thấy hiệu quang lộ giữa hai tia liên tiếp là \Delta L = d\sin\theta + d\sin\theta = 2d\sin\theta.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điều kiện cực đại giao thoa tăng cường là hiệu quang lộ bằng số nguyên lần bước sóng: 2d\sin\theta = n\lambda."
            ],
            variations_and_asymptotic_sweeps=[
                "Điều kiện tồn tại cực đại phản xạ: sin theta = n lambda / (2d) <= 1, đòi hỏi bước sóng lambda <= 2d (ánh sáng khả kiến có lambda ~ 500 nm không thể nhiễu xạ trên tinh thể có d ~ 0.2 nm).",
                "Khi biết trước bước sóng lambda và đo góc cực đại theta: Xác định chính xác cấu trúc tinh thể và khoảng cách liên mạng d."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao không thể sử dụng ánh sáng nhìn thấy để nghiên cứu cấu trúc tinh thể chất rắn bằng phương pháp tán xạ Bragg?"
            ]
        ),
        # MPT 2.2.5
        MicroPointTopic(
            mpt_id="Luận điểm 2.2.5",
            concept_introduction="Thí nghiệm Davisson - Germer: Bằng chứng thực nghiệm trực tiếp của sóng electron: Cột mốc lịch sử năm 1927 tại Bell Labs xác nhận bản chất sóng của electron qua nhiễu xạ trên đơn tinh thể Niken.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.2_Cuc_Dai_Nhieu_Xa_Davisson_Germer.png",
                interaction_id="IMG_2.2.5_SIM_DAVISSON_GERMER",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.2.5: Đồ thị mô phỏng cực đại phản xạ Davisson - Germer tại U = 54 V và góc tán xạ phi = 50 độ trên tinh thể Niken."
            ),
            minimal_working_example="Bắn chùm electron gia tốc bởi U = 54 V vào bề mặt đơn tinh thể Niken (khoảng cách nguyên tử D = 0.215 nm), đo cường độ tán xạ theo góc phi.",
            pillar_equation_latex=r"\lambda = D \sin\phi = 2d \sin\theta = \frac{h}{\sqrt{2 m_0 e U}}",
            nomenclature_table=[
                {"name": "Khoảng cách giữa các hàng nguyên tử bề mặt", "symbol": "D", "unit": "nm", "meaning": "Khoảng cách liên nguyên tử trên bề mặt tinh thể Ni (0.215 nm)"},
                {"name": "Góc tán xạ electron", "symbol": "\\phi", "unit": "độ", "meaning": "Góc giữa chùm electron tới vuông góc và chùm electron phản xạ (50 độ)"},
                {"name": "Góc trượt Bragg tương đương", "symbol": "\\theta = 90^\\circ - \\phi/2", "unit": "độ", "meaning": "Góc trượt tương ứng trên các mặt mạng Bragg (65 độ)"},
                {"name": "Khoảng cách mặt Bragg tương ứng", "symbol": "d = D\\sin(\\phi/2)", "unit": "nm", "meaning": "Khoảng cách giữa các mặt phản xạ tinh thể (0.091 nm)"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tính bước sóng lý thuyết de Broglie tại U = 54 V: \lambda_{\mathrm{theory}} = 12.26 / \sqrt{54} = 1.668\ \mathrm{\AA} = 0.1668\ \mathrm{nm}.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tính bước sóng thực nghiệm từ định luật cách mạng bề mặt: \lambda_{\mathrm{exp}} = D\sin\phi = 0.215\times \sin(50^\circ) = 0.1647\ \mathrm{nm}.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đối chiếu với định luật Bragg khối: \theta = 90^\circ - 25^\circ = 65^\circ, d = 0.091\ \mathrm{nm} \implies \lambda = 2d\sin\theta = 2(0.091)\sin(65^\circ) = 0.165\ \mathrm{nm}. Độ sai lệch dưới 1% chứng minh hoàn hảo bản chất sóng."
            ],
            variations_and_asymptotic_sweeps=[
                "Ở các điện áp khác (U < 44 V hoặc U > 68 V): Đỉnh cực đại giao thoa bị triệt tiêu do không thỏa mãn đồng thời điều kiện giao thoa tăng cường.",
                "Thí nghiệm G.P. Thomson (1927): Bắn electron qua màng mỏng đa tinh thể tạo các vòng tròn đồng tâm nhiễu xạ Debye-Scherrer."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao sự cố nổ bình chân không làm mẫu Niken bị oxy hóa và phải nung lại nhiệt độ cao vô tình lại là chìa khóa quyết định dẫn tới thành công của Davisson và Germer?"
            ]
        )
    ]
)

# =============================================================================
# BLUEPRINT MUC 2.3
# =============================================================================
bp_2_3 = LessonDeliverable(
    lesson_title="Chương 2: Bản chất lượng tử của thế giới nano - Mục 2.3: Hàm sóng, bó sóng và nguyên lý bất định Heisenberg",
    section_id="Mục 2.3",
    source_document_citations=[
        "Bài 2-Quantum nature.pdf (Slide 20 đến 27), Bộ môn Vật liệu Điện tử - Viện Vật lý Kỹ thuật HUST",
        "David J. Griffiths, Darrell F. Schroeter, Introduction to Quantum Mechanics, 3rd Edition, Cambridge University Press, 2018",
        "Charles P. Poole Jr., Frank J. Owens, Introduction to Nanotechnology, Wiley-Interscience, 2003",
        "Edward L. Wolf, Nanophysics and Nanotechnology, Wiley-VCH, 2006"
    ],
    total_pages_estimate=12,
    micro_point_topics=[
        # MPT 2.3.1
        MicroPointTopic(
            mpt_id="Luận điểm 2.3.1",
            concept_introduction="Hàm sóng phẳng de Broglie dạng phức & Ý nghĩa vật lý: Mô tả trạng thái chuyển động của vi hạt tự do bằng hàm sóng điều hòa phức, sự liên kết giữa các đại lượng cơ học vi mô (E, p) với các đại lượng sóng (omega, k).",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Goc]_Muc_2.3_Hinh_01_Giao_Thoa_Van_Sang_Toi_Photon.png",
                interaction_id="IMG_2.3.1_ORIG_INTERFERENCE_PHOTON",
                aspect_ratio="4:3",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.3.1: Ảnh thực nghiệm giao thoa vân sáng tối của photon/electron tích lũy theo thời gian trên màn chắn."
            ),
            minimal_working_example="Hàm sóng phẳng đơn sắc lan truyền theo phương x mô tả hạt tự do có động lượng p_x xác định và năng lượng E không đổi.",
            pillar_equation_latex=r"\Psi(\vec{r}, t) = A \exp\left( i(\vec{k}\cdot\vec{r} - \omega t) \right) = A \exp\left( \frac{i}{\hbar}(\vec{p}\cdot\vec{r} - E t) \right)",
            nomenclature_table=[
                {"name": "Hàm sóng trạng thái vi mô", "symbol": "\\Psi(\\vec{r}, t)", "unit": "m^{-3/2}", "meaning": "Hàm giải tích phức chứa đựng toàn bộ thông tin vật lý của hệ vi mô"},
                {"name": "Véctơ sóng", "symbol": "\\vec{k}", "unit": "rad/m", "meaning": "Véctơ chỉ phương truyền sóng, có độ lớn k = 2\\pi / \\lambda = p / \\hbar"},
                {"name": "Tần số góc của sóng", "symbol": "\\omega", "unit": "rad/s", "meaning": "Tần số biến thiên pha thời gian: \\omega = 2\\pi\\nu = E / \\hbar"},
                {"name": "Biên độ hàm sóng", "symbol": "A", "unit": "m^{-3/2}", "meaning": "Hệ số chuẩn hóa không gian của hàm sóng"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu diễn hàm sóng phẳng dạng lượng giác thực: D(x, t) = A\cos(\omega t - kx + \alpha).",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Áp dụng công thức Euler mở rộng sang trường phức: \exp(i\phi) = \cos\phi + i\sin\phi \implies \Psi(x, t) = A\exp(-i(\omega t - kx)).",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay thế các hệ thức Einstein - de Broglie E = \hbar\omega và \vec{p} = \hbar\vec{k} để thu được phương trình hàm sóng vi hạt tự do."
            ],
            variations_and_asymptotic_sweeps=[
                "Hàm sóng phẳng lan truyền hoàn toàn không định xứ trong không gian: Mật độ xác suất |Psi|^2 = |A|^2 là hằng số trên toàn bộ không gian vô hạn.",
                "Pha của sóng: Phi(x, t) = kx - omega*t; mặt đồng pha là mặt phẳng vuông góc với véctơ k."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao hàm sóng lượng tử bắt buộc phải là một hàm phức (Complex Function) mà không thể thuần túy là một hàm thực như sóng cơ học hay sóng điện từ?"
            ]
        ),
        # MPT 2.3.2
        MicroPointTopic(
            mpt_id="Luận điểm 2.3.2",
            concept_introduction="Tiên đề xác suất Max Born & Điều kiện chuẩn hóa hàm sóng: Bản chất thống kê của cơ học lượng tử, giải thích ý nghĩa vật lý của hàm sóng phức qua bình phương môđun mật độ xác suất định xứ vi hạt.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.3_Mat_Do_Xac_Suat_Born_Va_Ham_Song.png",
                interaction_id="IMG_2.3.2_SIM_BORN_PROBABILITY",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.3.2: Đồ thị mô phỏng tiên đề xác suất Max Born: sự liên hệ giữa phần thực, phần ảo của hàm sóng và mật độ xác suất |Psi|^2 cùng hiện tượng giao thoa hai khe lượng tử."
            ),
            minimal_working_example="Tích phân chuẩn hóa mật độ xác suất trong toàn bộ không gian đối với hạt chuyển động định xứ (bằng 100% tìm thấy hạt trong vũ trụ).",
            pillar_equation_latex=r"dP = |\Psi(\vec{r}, t)|^2 dV = \Psi^*(\vec{r}, t)\Psi(\vec{r}, t) dV \quad \text{và} \quad \int_{-\infty}^{\infty} |\Psi(\vec{r}, t)|^2 dV = 1",
            nomenclature_table=[
                {"name": "Xác suất tìm thấy hạt trong phần tử thể tích", "symbol": "dP", "unit": "không thứ nguyên", "meaning": "Xác suất định xứ hạt vi mô trong lân cận thể tích dV"},
                {"name": "Mật độ xác suất vị trí", "symbol": "|\\Psi(\\vec{r}, t)|^2", "unit": "m^{-3}", "meaning": "Bình phương độ lớn hàm sóng, đại lượng thực dương đo lường xác suất trên đơn vị thể tích"},
                {"name": "Hàm sóng liên hợp phức", "symbol": "\\Psi^*", "unit": "m^{-3/2}", "meaning": "Số phức liên hợp của hàm sóng Psi"},
                {"name": "Điều kiện chuẩn hóa toàn phần", "symbol": "\\int |\\Psi|^2 dV = 1", "unit": "không thứ nguyên", "meaning": "Đảm bảo tính bảo toàn xác suất toàn cục của hệ lượng tử"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phân tích tương tự quang học sóng: cường độ bức xạ I = \epsilon_0 c \mathcal{E}^2 tỷ lệ với thông lượng photon N \implies N \propto \mathcal{E}^2.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mở rộng sang sóng vật chất: vai trò của trường điện từ \mathcal{E} được thay thế bằng hàm sóng \Psi.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Định nghĩa tiên đề Max Born (1926): Mật độ xác suất tìm thấy hạt tại điểm (\vec{r}, t) tỷ lệ thuận với |\Psi(\vec{r}, t)|^2."
            ],
            variations_and_asymptotic_sweeps=[
                "Điều kiện hàm sóng chuẩn mực (Well-behaved wave function): Bắt buộc phải liên tục, đơn trị, có đạo hàm riêng liên tục và khả tích bình phương (Square-integrable).",
                "Giao thoa hai khe: |\Psi_1 + \Psi_2|^2 = |\Psi_1|^2 + |\Psi_2|^2 + 2\mathrm{Re}[\Psi_1^* \Psi_2] tạo nên các vân giao thoa xác suất kỳ diệu."
            ],
            student_challenges_cer=[
                "Thử thách CER: Khi thực hiện thí nghiệm hai khe với chùm electron bắn từng hạt đơn lẻ cực kỳ thưa thớt, tại sao sau thời gian dài vẫn thu được hình ảnh vân giao thoa trên màn chắn?"
            ]
        ),
        # MPT 2.3.3
        MicroPointTopic(
            mpt_id="Luận điểm 2.3.3",
            concept_introduction="Khái niệm Bó sóng (Wave Packet), Chồng chập sóng & Vận tốc nhóm: Sự định xứ không gian của hạt vi mô thông qua tổ hợp tuyến tính các sóng phẳng Fourier, sự khác biệt bản chất giữa vận tốc pha và vận tốc nhóm của sóng de Broglie.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.3_Cau_Truc_Bo_Song_Va_Van_Toc_Nhom.png",
                interaction_id="IMG_2.3.3_SIM_WAVE_PACKET",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.3.3: Đồ thị mô phỏng giải tích bó sóng Gaussian lan truyền trong không gian: minh họa đường bao biên độ, sự lan truyền với vận tốc nhóm vg và vận tốc pha vp."
            ),
            minimal_working_example="Tích phân chồng chập Fourier của phổ sóng liên tục A(k) quanh số sóng trung tâm k_0 với độ rộng Delta k.",
            pillar_equation_latex=r"v_g = \frac{d\omega}{dk} = \frac{d(\hbar\omega)}{d(\hbar k)} = \frac{dE}{dp} = \frac{d}{dp}\left(\frac{p^2}{2m}\right) = \frac{p}{m} = v_{\mathrm{hạt}}",
            nomenclature_table=[
                {"name": "Vận tốc nhóm của bó sóng", "symbol": "v_g", "unit": "m/s", "meaning": "Tốc độ lan truyền của tâm bó sóng và năng lượng, trùng khớp với vận tốc hạt cổ điển"},
                {"name": "Vận tốc pha của sóng", "symbol": "v_p = \\omega / k", "unit": "m/s", "meaning": "Tốc độ lan truyền của các mặt đồng pha bên trong bó sóng (đối với hạt phi tương đối tính v_p = v/2)"},
                {"name": "Phổ biên độ Fourier", "symbol": "A(k)", "unit": "m^{1/2}", "meaning": "Hàm trọng số phân bố biên độ các thành phần sóng phẳng đơn sắc"},
                {"name": "Độ rộng phổ số sóng", "symbol": "\\Delta k", "unit": "rad/m", "meaning": "Dải tần số không gian tham gia cấu tạo nên bó sóng định xứ"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu diễn bó sóng bằng tích phân Fourier: \psi(x, t) = \int_{k_0-\Delta k}^{k_0+\Delta k} A(k)\exp(i(kx - \omega(k)t)) dk.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khai triển chuỗi Taylor tần số góc quanh k_0: \omega(k) \approx \omega(k_0) + \left.\frac{d\omega}{dk}\right|_{k_0} (k - k_0).",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tách biểu thức thành tích của sóng mang nhanh và đường bao biên độ chuyển động với vận tốc v_g = d\omega/dk."
            ],
            variations_and_asymptotic_sweeps=[
                "Hạt phi tương đối tính: E = p^2/(2m) \implies v_p = E/p = v/2, trong khi v_g = p/m = v (vận tốc nhóm gấp đôi vận tốc pha).",
                "Hiện tượng tán sắc sóng (Dispersion): Bó sóng lan truyền trong môi trường tự do sẽ dần bị giãn rộng đường bao theo thời gian."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao vận tốc pha của sóng de Broglie đối với hạt tương đối tính v_p = c^2 / v lại lớn hơn tốc độ ánh sáng c nhưng hoàn toàn không vi phạm thuyết tương đối?"
            ]
        ),
        # MPT 2.3.4
        MicroPointTopic(
            mpt_id="Luận điểm 2.3.4",
            concept_introduction="Nguyên lý bất định Heisenberg & Hệ quả giam cầm năng lượng: Quy luật phổ quát của cơ học lượng tử thiết lập ranh giới nhận thức không thể vượt qua giữa các cặp biến số liên hợp (tọa độ - xung lượng, năng lượng - thời gian) và hệ quả giam cầm lượng tử trong thế giới nano.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.3_Nguyen_Ly_Bat_Dinh_Heisenberg.png",
                interaction_id="IMG_2.3.4_SIM_HEISENBERG_CONFINEMENT",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.3.4: Đồ thị mô phỏng nguyên lý bất định Heisenberg: mối quan hệ tương hỗ Delta x - Delta p và năng lượng giam cầm lượng tử E_conf bùng nổ khi kích thước nano L < 5 nm."
            ),
            minimal_working_example="Ước tính động năng điểm không (Zero-point energy) của electron bị giam cầm trong hộp thế nano kích thước L = 1 nm.",
            pillar_equation_latex=r"\Delta x \cdot \Delta p_x \ge \frac{\hbar}{2} = \frac{h}{4\pi} \quad \text{và} \quad \Delta E \cdot \Delta t \ge \frac{\hbar}{2}",
            nomenclature_table=[
                {"name": "Độ bất định tọa độ không gian", "symbol": "\\Delta x", "unit": "nm", "meaning": "Độ lệch chuẩn vị trí định xứ của hạt trong không gian thực"},
                {"name": "Độ bất định động lượng", "symbol": "\\Delta p_x", "unit": "kg·m/s", "meaning": "Độ lệch chuẩn thành phần động lượng tương ứng theo trục x"},
                {"name": "Hằng số Planck rút gọn", "symbol": "\\hbar = h / (2\\pi)", "unit": "J·s", "meaning": "Hằng số lượng tử vi mô CODATA 2022: 1.054571817e-34 J·s"},
                {"name": "Năng lượng giam cầm tối thiểu", "symbol": "E_{\\mathrm{conf}}", "unit": "eV", "meaning": "Động năng cực tiểu bắt buộc phải có do sự bất định động lượng trong không gian hẹp"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biểu diễn tính chất Fourier của bó sóng: tích độ rộng không gian \Delta x và độ rộng số sóng \Delta k luôn thỏa mãn \Delta x \Delta k \ge 1/2.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Nhân cả hai vế với hằng số Planck rút gọn \hbar: \Delta x (\hbar \Delta k) \ge \hbar / 2 \implies \Delta x \Delta p_x \ge \hbar / 2.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Dẫn xuất năng lượng giam cầm trong cấu trúc nano kích thước L (\Delta x \approx L/2): E_k \ge (\Delta p)^2 / (2m^*) \approx \hbar^2 / (8 m^* (\Delta x)^2) \approx \hbar^2 / (2 m^* L^2)."
            ],
            variations_and_asymptotic_sweeps=[
                "Khi kích thước cấu trúc nano co nhỏ (L < 5 nm): Năng lượng giam cầm E_conf vượt trội hoàn toàn năng lượng dao động nhiệt k_B T ở 300 K, biến đổi dải năng lượng vật liệu.",
                "Hệ thức bất định năng lượng - thời gian: Giải thích độ rộng vạch quang phổ tự nhiên của mức năng lượng có thời gian sống hữu hạn: Delta E = hbar / tau."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao electron trong nguyên tử không thể rơi vào hạt nhân mang điện tích dương để làm sụp đổ nguyên tử theo lực hút tĩnh điện Coulomb?"
            ]
        ),
        # MPT 2.3.5
        MicroPointTopic(
            mpt_id="Luận điểm 2.3.5",
            concept_introduction="Phương trình Schrödinger cơ bản của cơ học lượng tử: Phương trình động lực học nền tảng của vật lý lượng tử (Erwin Schrödinger, 1926), toán tử vi phân Hamiltonian và sự phân tách trạng thái dừng độc lập thời gian.",
            visual_anchor=VisualAssetSpec(
                image_file_path=r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh\[Mo_Phong]_Muc_2.3_Mat_Do_Xac_Suat_Born_Va_Ham_Song.png",
                interaction_id="IMG_2.3.5_SCHRODINGER_EQUATION",
                aspect_ratio="6.5:4.2",
                brand_palette_compliant=True,
                pedagogical_caption="Hình 2.3.5: Cấu trúc toán tử vi phân trong phương trình Schrödinger và sự chuyển tiếp sang các trạng thái dừng năng lượng riêng."
            ),
            minimal_working_example="Thiết lập phương trình Schrödinger một chiều cho vi hạt chuyển động tự do và vi hạt chịu tác dụng của trường thế V(x).",
            pillar_equation_latex=r"i\hbar \frac{\partial \Psi}{\partial t} = \hat{H}\Psi = \left( -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r}, t) \right)\Psi \quad \text{và} \quad -\frac{\hbar^2}{2m}\nabla^2 \psi + V(\vec{r})\psi = E\psi",
            nomenclature_table=[
                {"name": "Toán tử Hamiltonian toàn phần", "symbol": "\\hat{H}", "unit": "J hoặc eV", "meaning": "Toán tử năng lượng toàn phần gồm toán tử động năng và toán tử thế năng"},
                {"name": "Toán tử vi phân Laplace", "symbol": "\\nabla^2 = \\Delta", "unit": "m^{-2}", "meaning": "Toán tử đạo hàm không gian bậc hai: d^2/dx^2 + d^2/dy^2 + d^2/dz^2"},
                {"name": "Trường thế năng ngoại đặt", "symbol": "V(\\vec{r}, t)", "unit": "J hoặc eV", "meaning": "Trường lực tương tác tác dụng lên hạt vi mô (Coulomb, giếng thế, rào thế)"},
                {"name": "Giá trị riêng năng lượng", "symbol": "E", "unit": "eV", "meaning": "Mức năng lượng gián đoạn của trạng thái dừng lượng tử"}
            ],
            guided_practice_steps=[
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Xây dựng toán tử động lượng vi phân từ hàm sóng phẳng: \hat{p}_x = -i\hbar \frac{\partial}{\partial x} \implies \hat{E}_k = \frac{\hat{p}^2}{2m} = -\frac{\hbar^2}{2m}\nabla^2.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Xây dựng toán tử năng lượng toàn phần theo thời gian: \hat{E} = i\hbar \frac{\partial}{\partial t}.",
                r"↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tách biến đối với trường thế dừng V(\vec{r}): \Psi(\vec{r}, t) = \psi(\vec{r})\exp(-iEt/\hbar), khử thừa số thời gian thu được phương trình Schrödinger độc lập thời gian."
            ],
            variations_and_asymptotic_sweeps=[
                "Trạng thái dừng (Stationary States): Mật độ xác suất |Psi(\vec{r}, t)|^2 = |\psi(\vec{r})|^2 hoàn toàn độc lập với thời gian.",
                "Nguyên lý xếp chồng trạng thái: Tổ hợp tuyến tính các nghiệm riêng trạng thái dừng cũng là một nghiệm của phương trình Schrödinger phụ thuộc thời gian."
            ],
            student_challenges_cer=[
                "Thử thách CER: Tại sao phương trình Schrödinger chỉ chứa đạo hàm bậc nhất theo thời gian dt mà lại chứa đạo hàm bậc hai theo không gian dx^2?"
            ]
        )
    ]
)

# Ghi tệp JSON
p_2_2 = os.path.join(data_dir, "BLUEPRINT_MUC_2.2_NANO.json")
with open(p_2_2, "w", encoding="utf-8") as f:
    json.dump(bp_2_2.model_dump(), f, ensure_ascii=False, indent=2)
print(f"Saved Blueprint Muc 2.2: {p_2_2}")

p_2_3 = os.path.join(data_dir, "BLUEPRINT_MUC_2.3_NANO.json")
with open(p_2_3, "w", encoding="utf-8") as f:
    json.dump(bp_2_3.model_dump(), f, ensure_ascii=False, indent=2)
print(f"Saved Blueprint Muc 2.3: {p_2_3}")

print("Both Blueprints generated and validated successfully with Pydantic!")

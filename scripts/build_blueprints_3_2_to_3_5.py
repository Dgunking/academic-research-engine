# -*- coding: utf-8 -*-
import json
import os

DATA_DIR = r"d:\antigravity\academic-research-engine\data"
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# BLUEPRINT 3.2
# ---------------------------------------------------------------------------
bp_3_2 = {
  "lesson_title": "Chương 3: Đặc trưng của vật liệu khi kích thước giảm - Mục 3.2: Nhiệt động học vi mô, động học chất lưu Stokes và chuyển động khuếch tán Brown",
  "section_id": "Mục 3.2",
  "source_document_citations": [
    "Bài 3-Properties.pdf (Slide 22 đến 28), Bộ môn Vật liệu Điện tử - Viện Vật lý Kỹ thuật HUST",
    "Edward L. Wolf, Nanophysics and Nanotechnology, Wiley-VCH, 2006 (Chapter 3)",
    "Charles P. Poole Jr., Frank J. Owens, Introduction to Nanotechnology, John Wiley & Sons, 2003"
  ],
  "total_pages_estimate": 20,
  "micro_point_topics": [
    {
      "mpt_id": "Luận điểm 3.2.1",
      "concept_introduction": "Truyền nhiệt vi mô qua cầu dẫn nhiệt nano: Thiết lập phương trình cân bằng nhiệt lượng dQ/dt = k_T A (T - T_0)/L = C_V dT/dt và nghiệm phân rã hàm mũ nhiệt độ.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.2_Hinh_01_Trao_Doi_Nhiet_Va_Hang_So_Thoi_Gian_Tau.png",
        "interaction_id": "IMG_3.2.1_ORIG_HEAT",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.2.1: Sơ đồ truyền nhiệt vi mô qua cầu nano và sự suy giảm hàm mũ nhiệt độ (Slide 22 HUST)."
      },
      "minimal_working_example": "Xác định hằng số thời gian nhiệt tau_th của cầu dẫn nhiệt Silicon có L = 1 um, tiết diện A = 100 nm x 100 nm nối với hạt nano Silicon.",
      "pillar_equation_latex": "\\frac{\\mathrm{d}Q}{\\mathrm{d}t} = \\frac{k_T A}{L}(T - T_0) = C_V \\frac{\\mathrm{d}T}{\\mathrm{d}t} \\implies T(t) - T_0 = \\Delta T_0 \\mathrm{e}^{-\\frac{t}{\\tau_{\\mathrm{th}}}}, \\quad \\tau_{\\mathrm{th}} = \\frac{L C_V}{k_T A}",
      "nomenclature_table": [
        {"name": "Hằng số thời gian nhiệt", "symbol": "\\tau_{\\mathrm{th}}", "unit": "s", "meaning": "Thời gian để độ chênh lệch nhiệt độ suy giảm e lần"},
        {"name": "Nhiệt dung toàn phần", "symbol": "C_V", "unit": "J/K", "meaning": "Nhiệt dung đẳng tích của khối nano C_V = c_v V = c_v rho L^3"},
        {"name": "Độ dẫn nhiệt của vật liệu", "symbol": "k_T", "unit": "W/(m K)", "meaning": "Hệ số truyền nhiệt dẫn xuất Fourier của cầu nối nano"},
        {"name": "Diện tích tiết diện cầu dẫn", "symbol": "A", "unit": "m^2", "meaning": "Diện tích tiếp xúc truyền dẫn nhiệt lượng"},
        {"name": "Chiều dài cầu dẫn nhiệt", "symbol": "L", "unit": "m", "meaning": "Khoảng cách truyền nhiệt từ hạt nano tới bể nhiệt tản"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thiết lập phương trình vi phân truyền dẫn nhiệt: C_V \\frac{\\mathrm{d}T}{\\mathrm{d}t} = -\\frac{k_T A}{L}(T - T_0).",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phân ly biến số và tích phân từ t = 0 đến t: \\int_{\\Delta T_0}^{\\Delta T} \\frac{\\mathrm{d}(\\Delta T)}{\\Delta T} = -\\frac{k_T A}{L C_V} \\int_0^t \\mathrm{d}t.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Suy ra nghiệm suy giảm hàm mũ: \\Delta T(t) = \\Delta T_0 \\exp(-t / \\tau_{th}) với \\tau_{th} = \\frac{L C_V}{k_T A}."
      ],
      "variations_and_asymptotic_sweeps": [
        "Khảo sát tỉ lệ kích thước: Do C_V propto L^3 và A propto L^2, ta có tau_th propto L * L^3 / L^2 = L^2. Khi kích thước L giảm 1000 lần (từ 1 mm xuống 1 um), thời gian hồi phục nhiệt tau_th giảm 10^6 lần (từ 1 ms xuống 1 ns), tạo khả năng tản nhiệt siêu tốc ở thang nano."
      ],
      "student_challenges_cer": [
        "Thử thách CER 3.2.1: Tính hằng số thời gian nhiệt tau_th cho một hạt nano Vàng đường kính D = 20 nm tản nhiệt vào môi trường nước xung quanh và giải thích tại sao hạt nano Vàng có thể nguội đi gần như tức thời sau khi bị kích thích laser xung femtosecond."
      ]
    },
    {
      "mpt_id": "Luận điểm 3.2.2",
      "concept_introduction": "Định luật tỉ lệ nhiệt L^2 và đồng nhất nhiệt độ ở thang nano: Phân tích độ chênh lệch nhiệt độ nội tại dT propto L và sự triệt tiêu gradient nhiệt bên trong cấu trúc nano đơn lẻ.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.2_Hinh_02_Dinh_Luat_Ti_Le_Nhiet_Va_Tan_Nhiet_Nano.png",
        "interaction_id": "IMG_3.2.2_ORIG_THERMAL_SCALING",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.2.2: Định luật tỉ lệ nhiệt tau_th propto L^2 và cơ chế đồng nhất nhiệt độ (Slide 23 HUST)."
      },
      "minimal_working_example": "Chứng minh số Biot Bi = h L / k_T << 0.1 đối với hạt nano dẫn đến trạng thái nhiệt đồng nhất tuyệt đối bên trong hạt.",
      "pillar_equation_latex": "\\Delta T \\propto L, \\quad \\tau_{\\mathrm{th}} \\propto L^2, \\quad \\mathrm{Bi} = \\frac{h L}{k_T} \\to 0",
      "nomenclature_table": [
        {"name": "Số Biot không thứ nguyên", "symbol": "Bi", "unit": "không thứ nguyên", "meaning": "Tỉ số giữa trở nhiệt truyền dẫn bên trong và trở nhiệt đối lưu bề mặt"},
        {"name": "Hệ số trao đổi nhiệt đối lưu", "symbol": "h", "unit": "W/(m^2 K)", "meaning": "Hệ số truyền nhiệt giữa bề mặt hạt và môi trường chất lưu xung quanh"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chênh lệch nhiệt độ giữa tâm hạt và bề mặt: \\Delta T_{int} \\approx \\frac{q L^2}{6 k_T} với mật độ phát nhiệt q = Q / V propto L^0.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi L -> 0, \\Delta T_{int} propto L^2 -> 0, dẫn tới nhiệt độ nội tại hoàn toàn đồng nhất."
      ],
      "variations_and_asymptotic_sweeps": ["Hệ quả: Các hạt nano không bao giờ duy trì được gradient nhiệt nội tại."],
      "student_challenges_cer": ["Thử thách CER 3.2.2: Đánh giá số Biot của chấm lượng tử CdSe bán kính 3 nm."]
    },
    {
      "mpt_id": "Luận điểm 3.2.3",
      "concept_introduction": "Động học chất lưu nhớt ở số Reynolds thấp và lực cản Stokes: Lực cản F_Stokes = 6 pi eta R v và tốc độ rơi giới hạn cân bằng trọng lực.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.2_Hinh_03_Luc_Can_Nhot_Stokes_Va_Van_Toc_Roi.png",
        "interaction_id": "IMG_3.2.3_ORIG_STOKES",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.2.3: Lực cản nhớt Stokes và tốc độ rơi giới hạn cân bằng trọng lực (Slide 24 HUST)."
      },
      "minimal_working_example": "Tính tốc độ rơi giới hạn của hạt vi mô R = 10 um trong nước (v = 23 mm/s) theo Slide 25 HUST.",
      "pillar_equation_latex": "F_{\\mathrm{Stokes}} = 6\\pi \\eta R v, \\quad v_{\\mathrm{term}} = \\frac{2(\\rho - \\rho_f) g R^2}{9\\eta}",
      "nomenclature_table": [
        {"name": "Độ nhớt động lực học của nước", "symbol": "\\eta", "unit": "Pa s", "meaning": "Độ nhớt của nước tại 300 K (1.002 x 10^-3 Pa s)"},
        {"name": "Bán kính hình học của hạt", "symbol": "R", "unit": "m", "meaning": "Bán kính hình cầu của hạt vi mô hoặc nano"},
        {"name": "Tốc độ rơi giới hạn cân bằng", "symbol": "v_{\\mathrm{term}}", "unit": "m/s", "meaning": "Tốc độ khi lực cản nhớt cân bằng lực trọng trường nổi"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Cân bằng lực trọng trường hiệu dụng và lực cản Stokes: \\frac{4}{3}\\pi R^3 (\\rho - \\rho_f) g = 6\\pi \\eta R v.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Giải tìm vận tốc rơi giới hạn: v_{term} = \\frac{2(\\rho - \\rho_f) g R^2}{9\\eta}."
      ],
      "variations_and_asymptotic_sweeps": ["Tốc độ rơi tỉ lệ thuận với R^2: Giảm R 1000 lần thì tốc độ rơi giảm 10^6 lần."],
      "student_challenges_cer": ["Thử thách CER 3.2.3: Tính vận tốc rơi của hạt nano R = 15 nm theo Slide 26 HUST."]
    },
    {
      "mpt_id": "Luận điểm 3.2.4",
      "concept_introduction": "Sụp đổ cơ học Newton trước khuếch tán nhiệt Brown: So sánh tốc độ lắng vi mô (23 mm/s) vs nano (13 nm/s), hệ thức Einstein-Smoluchowski và chiều dài khuếch tán x_rms.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.2_Hinh_04_Sup_Do_Co_Hoc_Newton_O_Thang_Nano.png",
        "interaction_id": "IMG_3.2.4_ORIG_BROWNIAN",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.2.4: Sự áp đảo của chuyển động nhiệt Brown so với lắng trọng trường ở thang nano (Slide 25–27 HUST)."
      },
      "minimal_working_example": "Tính hệ số khuếch tán D và chiều dài khuếch tán x_rms trong 1 giây của hạt nano R = 15 nm (Slide 27 HUST).",
      "pillar_equation_latex": "D = \\frac{k_B T}{6\\pi\\eta R}, \\quad \\langle x^2 \\rangle = 2 D t, \\quad x_{\\mathrm{rms}} = \\sqrt{2 D t}",
      "nomenclature_table": [
        {"name": "Hệ số khuếch tán Einstein", "symbol": "D", "unit": "m^2/s", "meaning": "Đại lượng đo tốc độ lan truyền ngẫu nhiên do dao động nhiệt"},
        {"name": "Chiều dài khuếch tán căn quân phương", "symbol": "x_{\\mathrm{rms}}", "unit": "m", "meaning": "Khoảng dịch chuyển trung bình của hạt sau thời gian t"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay số R = 15 nm, T = 300 K: D = (1.38 x 10^-23 * 300) / (6 * pi * 1.002 x 10^-3 * 15 x 10^-9) = 1.46 x 10^-11 m^2/s.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Sau t = 1 s, chiều dài khuếch tán x_rms = sqrt(2 * 1.46 x 10^-11 * 1) = 5.4 x 10^-6 m = 5.4 um, lớn hơn quãng đường rơi trọng trường (13 nm) tới 415 lần!"
      ],
      "variations_and_asymptotic_sweeps": ["Hệ quả: Các hạt nano lơ lửng vĩnh cửu trong dung dịch keo mà không bị sa lắng."],
      "student_challenges_cer": ["Thử thách CER 3.2.4: Chứng minh giới hạn kích thước hạt nano để khuếch tán Brown chi phối hoàn toàn trọng trường."]
    },
    {
      "mpt_id": "Luận điểm 3.2.5",
      "concept_introduction": "Hiện tượng ma sát siêu trơn (Superlubricity) ở thang phân tử: Khảo sát cấu trúc Graphite và Ống nano carbon (CNT) trượt không ma sát do không tương thích mạng tinh thể (Incommensurate contact).",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.2_Hinh_06_Hien_Tuong_Sieu_Tron_Graphite_Va_CNT.png",
        "interaction_id": "IMG_3.2.5_ORIG_SUPERLUBRICITY",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.2.5: Hiện tượng ma sát siêu trơn ở giao diện Graphite và Carbon Nanotubes (Slide 28 HUST)."
      },
      "minimal_working_example": "Mô hình Frenkel-Kontorova giải thích sự triệt tiêu lực cản tĩnh khi hai mặt phẳng tinh thể lệch góc quay theta.",
      "pillar_equation_latex": "F_{\\mathrm{friction}} \\propto \\sum_i \\sin\\left(\\frac{2\\pi x_i}{a}\\right) \\to 0 \\quad (\\text{Incommensurate State})",
      "nomenclature_table": [
        {"name": "Lực ma sát tĩnh vi mô", "symbol": "F_{\\mathrm{friction}}", "unit": "N", "meaning": "Tổng lực cản thế năng tuần hoàn giữa hai bề mặt tiếp xúc nguyên tử"},
        {"name": "Góc xoay lệch mạng", "symbol": "\\theta", "unit": "độ", "meaning": "Góc lệch giữa các vector mạng tinh thể của hai lớp trượt"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi hai mạng tương thích (commensurate), các nguyên tử rơi đồng loạt vào đáy thế năng, tạo lực cản cực đại.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi xoay lệch góc theta (incommensurate), một nửa số nguyên tử chịu lực đẩy trong khi nửa kia chịu lực hút, tổng lực thế năng triệt tiêu về 0, ma sát biến mất."
      ],
      "variations_and_asymptotic_sweeps": ["Ứng dụng: Chế tạo ổ bi nano và công tắc cơ lượng tử không bị mài mòn."],
      "student_challenges_cer": ["Thử thách CER 3.2.5: Phân tích tại sao ma sát siêu trơn chỉ tồn tại ở thang nano mà biến mất ở thang vĩ mô."]
    }
  ]
}

with open(os.path.join(DATA_DIR, "BLUEPRINT_MUC_3.2_NANO.json"), "w", encoding="utf-8") as f:
    json.dump(bp_3_2, f, ensure_ascii=False, indent=2)
print("BLUEPRINT_MUC_3.2_NANO.json created.")

# ---------------------------------------------------------------------------
# BLUEPRINT 3.3
# ---------------------------------------------------------------------------
bp_3_3 = {
  "lesson_title": "Chương 3: Đặc trưng của vật liệu khi kích thước giảm - Mục 3.3: Mật độ trạng thái điện tử (DOS), ống nano carbon và hiện tượng giam hãm phonon",
  "section_id": "Mục 3.3",
  "source_document_citations": [
    "Bài 3-Properties.pdf (Slide 29 đến 37), Bộ môn Vật liệu Điện tử - Viện Vật lý Kỹ thuật HUST",
    "Edward L. Wolf, Nanophysics and Nanotechnology, Wiley-VCH, 2006 (Chapter 3)",
    "Charles P. Poole Jr., Frank J. Owens, Introduction to Nanotechnology, John Wiley & Sons, 2003"
  ],
  "total_pages_estimate": 21,
  "micro_point_topics": [
    {
      "mpt_id": "Luận điểm 3.3.1",
      "concept_introduction": "Hình thái học đa dạng của cấu trúc nano (Morphology): Các dạng tinh thể ZnO (nanowires, nanorods, nanobelts, nanoflowers) và phân loại chiều không gian 0D, 1D, 2D, 3D.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.3_Hinh_02_Hinh_Thai_Hoc_Morphology_Vat_Lieu_ZnO.png",
        "interaction_id": "IMG_3.3.1_ORIG_MORPHOLOGY",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.3.1: Đa dạng hình thái học tinh thể nano ZnO và phân loại số chiều (Slide 29–30 HUST)."
      },
      "minimal_working_example": "Mối liên hệ giữa định hướng tinh thể Wurtzite của ZnO và hướng phát triển dây nano dọc trục c [0001].",
      "pillar_equation_latex": "d = 0, 1, 2, 3 \\implies \\text{Quantum Dot (0D), Wire (1D), Well (2D), Bulk (3D)}",
      "nomenclature_table": [
        {"name": "Số chiều giam giữ lượng tử", "symbol": "d", "unit": "nguyên", "meaning": "Số chiều mà hạt tải tự do chuyển động trong vật liệu"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Phân loại hệ lượng tử theo kích thước tương đối so với bước sóng de Broglie."
      ],
      "variations_and_asymptotic_sweeps": ["Sự chuyển đổi từ dải năng lượng liên tục sang các mức gián đoạn khi giảm chiều."],
      "student_challenges_cer": ["Thử thách CER 3.3.1: Phân tích cơ chế tạo hình bông hoa nanoflowers của ZnO."]
    },
    {
      "mpt_id": "Luận điểm 3.3.2",
      "concept_introduction": "Mật độ trạng thái điện tử (DOS) theo số chiều: Dẫn xuất toàn văn hàm DOS cho Bulk 3D (căn bậc hai), Quantum Well 2D (hàm bậc thang Heaviside), Quantum Wire 1D (nghịch đảo căn bậc hai - điểm kỳ dị Van Hove), Quantum Dot 0D (hàm delta Dirac).",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.3_Hinh_04_Bieu_Do_DOS_Theo_Chieu_Khong_Gian_3D_2D_1D_0D.png",
        "interaction_id": "IMG_3.3.2_ORIG_DOS",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.3.2: Biểu đồ mật độ trạng thái điện tử DOS theo số chiều 3D, 2D, 1D, 0D (Slide 31–32 HUST)."
      },
      "minimal_working_example": "Dẫn xuất hàm DOS 1D: g_{1D}(E) = (1/pi hbar) * sqrt(m / (2(E - E_n))) thể hiện điểm kỳ dị Van Hove tại E -> E_n.",
      "pillar_equation_latex": "g_{3\\mathrm{D}} \\propto \\sqrt{E}, \\quad g_{2\\mathrm{D}} \\propto \\sum_n \\Theta(E - E_n), \\quad g_{1\\mathrm{D}} \\propto \\sum_{n,m} \\frac{1}{\\sqrt{E - E_{n,m}}}, \\quad g_{0\\mathrm{D}} \\propto \\sum_i \\delta(E - E_i)",
      "nomenclature_table": [
        {"name": "Hàm mật độ trạng thái điện tử", "symbol": "g(E)", "unit": "eV^-1 m^-d", "meaning": "Số trạng thái điện tử trên một đơn vị năng lượng và thể tích d-chiều"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Tích phân không gian k theo số chiều d và chuyển đổi dN = g(E) dE.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Chứng minh điểm kỳ dị Van Hove trong hệ 1D khi đạo hàm dE/dk = 0."
      ],
      "variations_and_asymptotic_sweeps": ["Ý nghĩa: Tăng cường hấp thụ quang học và hệ số phát xạ kích thích tại điểm kỳ dị Van Hove."],
      "student_challenges_cer": ["Thử thách CER 3.3.2: So sánh độ sắc nét vạch phát xạ của laser giếng lượng tử 2D vs chấm lượng tử 0D."]
    },
    {
      "mpt_id": "Luận điểm 3.3.3",
      "concept_introduction": "Ống nano carbon (CNT): Vector chiral C_h = n a_1 + m a_2, góc chiral theta, phân loại cấu trúc Armchair, Zigzag, Chiral và quy tắc kim loại (n - m = 3q) vs bán dẫn.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.3_Hinh_05_Vector_Chiral_Va_Cau_Truc_Ong_Than_CNT.png",
        "interaction_id": "IMG_3.3.3_ORIG_CNT",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.3.3: Vector chiral C_h và các kiểu cuộn ống nano carbon CNT (Slide 33–34 HUST)."
      },
      "minimal_working_example": "Xác định tính chất kim loại hay bán dẫn của CNT (10, 0), (10, 10), (10, 5) và tính vùng cấm E_g = 2 gamma_0 a_cc / d_t.",
      "pillar_equation_latex": "\\mathbf{C}_h = n \\mathbf{a}_1 + m \\mathbf{a}_2, \\quad d_t = \\frac{a}{\\pi}\\sqrt{n^2 + n m + m^2}, \\quad n - m = 3q \\implies \\text{Kim loại}",
      "nomenclature_table": [
        {"name": "Đường kính ống nano carbon", "symbol": "d_t", "unit": "nm", "meaning": "Đường kính hình học của ống đơn vách SWCNT"},
        {"name": "Năng lượng tích phân nhảy", "symbol": "\\gamma_0", "unit": "eV", "meaning": "Tích phân nhảy xen phủ orbital pi của liên kết C-C (~2.9 eV)"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Cuộn mặt phẳng Graphene 2D với điều kiện biên tuần hoàn k . C_h = 2 pi j.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điểm Dirac K rơi vào đường cho phép khi và chỉ khi n - m chia hết cho 3."
      ],
      "variations_and_asymptotic_sweeps": ["1/3 số ống CNT là kim loại, 2/3 là bán dẫn với độ rộng vùng cấm tỉ lệ nghịch với đường kính E_g propto 1/d_t."],
      "student_challenges_cer": ["Thử thách CER 3.3.3: Tính đường kính và vùng cấm của SWCNT (10, 0)."]
    },
    {
      "mpt_id": "Luận điểm 3.3.4",
      "concept_introduction": "Hiện tượng giam hãm phonon (Phonon Confinement Effect): Phổ tán xạ Raman của hạt nano tinh thể CeO2 và TiO2, mô hình Campbell - Fauchet, sự dịch đỉnh và mở rộng bất đối xứng của vạch phổ Raman.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.4_Hinh_01_Pho_Tan_Xa_Raman_Giam_Giu_Phonon.png",
        "interaction_id": "IMG_3.3.4_ORIG_RAMAN",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.3.4: Hiện tượng giam hãm phonon và dịch đỉnh tán xạ Raman trong hạt nano CeO2 (Slide 35–36 HUST)."
      },
      "minimal_working_example": "Mô hình Richter-Campbell-Fauchet tích hợp vector sóng q từ 0 đến 1/L phá vỡ quy tắc chọn lọc q = 0.",
      "pillar_equation_latex": "I(\\omega) \\propto \\int \\frac{|C(0, \\mathbf{q})|^2}{[\\omega - \\omega(\\mathbf{q})]^2 + (\\Gamma_0/2)^2} \\mathrm{d}^3 q",
      "nomenclature_table": [
        {"name": "Độ dịch đỉnh Raman", "symbol": "\\Delta \\omega", "unit": "cm^-1", "meaning": "Độ lệch số sóng của đỉnh tán xạ Raman do giảm kích thước hạt"},
        {"name": "Độ rộng bán phần vạch phổ", "symbol": "\\Gamma", "unit": "cm^-1", "meaning": "Bề rộng nửa độ cao FWHM phản ánh thời gian sống của phonon"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Do giam giữ không gian Delta x ~ L, nguyên lý bất định Delta q ~ 1/L cho phép các phonon q > 0 tham gia tán xạ Raman.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Vì nhánh phonon quang học có độ dốc âm d omega / dq < 0, sự đóng góp của q > 0 làm dịch chuyển đỉnh Raman về phía tần số thấp (redshift) và mở rộng vạch phổ."
      ],
      "variations_and_asymptotic_sweeps": ["Sử dụng độ dịch phổ Raman làm phương pháp quang học không phá hủy để đo kích thước hạt nano."],
      "student_challenges_cer": ["Thử thách CER 3.3.4: Ước lượng kích thước hạt CeO2 khi đỉnh Raman 465 cm^-1 dịch về 460 cm^-1."]
    },
    {
      "mpt_id": "Luận điểm 3.3.5",
      "concept_introduction": "Tính chất từ và chuyển pha phụ thuộc kích thước: Sự suy giảm nhiệt độ Curie chuyển pha sắt từ - thuận từ và sắt điện trong gốm nano PbTiO3, hiệu ứng siêu thuận từ (Superparamagnetism) và giới hạn Néel-Brown.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.4_Hinh_03_Chuyen_Pha_Sat_Tu_Thuan_Tu_PbTiO3.png",
        "interaction_id": "IMG_3.3.5_ORIG_MAGNETIC",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.3.5: Đường cong từ trễ và chuyển pha siêu thuận từ ở hạt nano PbTiO3 và Fe3O4 (Slide 37 HUST)."
      },
      "minimal_working_example": "Thời gian hồi phục Néel tau = tau_0 exp(K V / k_B T) và sự biến mất của lực kháng từ H_c = 0 dưới nhiệt độ chặn T_B.",
      "pillar_equation_latex": "\\tau = \\tau_0 \\exp\\left(\\frac{K V}{k_B T}\\right), \\quad T_B = \\frac{K V}{k_B \\ln(t_m / \\tau_0)}",
      "nomenclature_table": [
        {"name": "Hằng số bất đẳng hướng từ", "symbol": "K", "unit": "J/m^3", "meaning": "Mật độ năng lượng từ tinh thể định hướng trục dễ từ hóa"},
        {"name": "Nhiệt độ chặn (Blocking Temperature)", "symbol": "T_B", "unit": "K", "meaning": "Nhiệt độ chuyển pha giữa trạng thái sắt từ bền và siêu thuận từ"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi thể tích hạt V nhỏ sao cho rào năng lượng K V ~ k_B T, năng lượng nhiệt làm lật ngẫu nhiên mômen từ của toàn bộ hạt.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Đường cong từ trễ co lại thành đường đơn trị không có diện tích trễ (H_c = 0, M_r = 0)."
      ],
      "variations_and_asymptotic_sweeps": ["Ứng dụng: Dẫn thuốc từ tính hạt nano Fe3O4 và chất tăng tương phản MRI không bị tắc mạch máu."],
      "student_challenges_cer": ["Thử thách CER 3.3.5: Tính kích thước tới hạn siêu thuận từ của hạt Fe3O4 ở 300 K."]
    }
  ]
}

with open(os.path.join(DATA_DIR, "BLUEPRINT_MUC_3.3_NANO.json"), "w", encoding="utf-8") as f:
    json.dump(bp_3_3, f, ensure_ascii=False, indent=2)
print("BLUEPRINT_MUC_3.3_NANO.json created.")

# ---------------------------------------------------------------------------
# BLUEPRINT 3.4
# ---------------------------------------------------------------------------
bp_3_4 = {
  "lesson_title": "Chương 3: Đặc trưng của vật liệu khi kích thước giảm - Mục 3.4: Hiệu ứng bề mặt, năng lượng bề mặt và các ứng dụng xúc tác - cảm biến nano",
  "section_id": "Mục 3.4",
  "source_document_citations": [
    "Bài 3-Properties.pdf (Slide 38 đến 43), Bộ môn Vật liệu Điện tử - Viện Vật lý Kỹ thuật HUST",
    "Edward L. Wolf, Nanophysics and Nanotechnology, Wiley-VCH, 2006 (Chapter 3)",
    "Charles P. Poole Jr., Frank J. Owens, Introduction to Nanotechnology, John Wiley & Sons, 2003"
  ],
  "total_pages_estimate": 18,
  "micro_point_topics": [
    {
      "mpt_id": "Luận điểm 3.4.1",
      "concept_introduction": "Bùng nổ diện tích bề mặt riêng và tỉ số diện tích trên thể tích S/V = 3/R: Phân tích sự gia tăng đột biến của phần trăm nguyên tử nằm ở bề mặt khi kích thước hạt giảm.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_01_Phan_Chia_Dien_Tich_Be_Mat.png",
        "interaction_id": "IMG_3.4.1_ORIG_SURFACE_AREA",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.4.1: Sự bùng nổ diện tích bề mặt khi phân chia một khối vật liệu thành các hạt nano (Slide 38 HUST)."
      },
      "minimal_working_example": "Tính tỉ lệ diện tích bề mặt S/V cho hạt hình cầu bán kính R và khối lập phương cạnh a.",
      "pillar_equation_latex": "\\frac{S}{V} = \\frac{3}{R} = \\frac{6}{D}, \\quad F_{\\mathrm{surf}} = 1 - \\left(1 - \\frac{2\\delta}{D}\\right)^3",
      "nomenclature_table": [
        {"name": "Tỉ số diện tích trên thể tích", "symbol": "S/V", "unit": "m^-1", "meaning": "Diện tích bề mặt khả dụng trên một đơn vị thể tích vật liệu"},
        {"name": "Độ dày lớp đơn nguyên tử bề mặt", "symbol": "\\delta", "unit": "nm", "meaning": "Khoảng cách liên nguyên tử đặc trưng (~0.3 nm)"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hạt cầu thể tích V = (4/3) pi R^3, diện tích S = 4 pi R^2 => S / V = 3 / R.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hạt D = 2 nm có tới 65% nguyên tử nằm ở bề mặt."
      ],
      "variations_and_asymptotic_sweeps": ["Bề mặt biến từ yếu tố biên không đáng kể ở vĩ mô thành yếu tố chi phối tuyệt đối ở thang nano."],
      "student_challenges_cer": ["Thử thách CER 3.4.1: Tính diện tích bề mặt của 1 gram hạt nano vàng đường kính 5 nm."]
    },
    {
      "mpt_id": "Luận điểm 3.4.2",
      "concept_introduction": "Trực quan hóa diện tích bề mặt qua góc nhìn phô mai Pháp (French cheese perspective): Phân chia khối lập phương từ 1 m xuống 1 mm rồi xuống 1 nm làm tăng diện tích từ 6 m^2 lên 6000 km^2.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_02_Bang_Tang_Dien_Tich_Lap_Phuong.png",
        "interaction_id": "IMG_3.4.2_ORIG_CHEESE",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.4.2: Bảng phân chia khối lập phương và góc nhìn phô mai Pháp (Slide 39–40 HUST)."
      },
      "minimal_working_example": "Chứng minh diện tích tổng cộng S_total = N * 6 a^2 = (V / a^3) * 6 a^2 = 6 V / a tỉ lệ nghịch với cạnh a.",
      "pillar_equation_latex": "S_{\\mathrm{total}} = \\frac{6 V_0}{a}, \\quad a = 1\\text{ m} \\to S = 6\\text{ m}^2; \\quad a = 1\\text{ nm} \\to S = 6000\\text{ km}^2",
      "nomenclature_table": [
        {"name": "Thể tích ban đầu cố định", "symbol": "V_0", "unit": "m^3", "meaning": "Thể tích khối vật liệu vĩ mô (1 m^3)"},
        {"name": "Kích thước cạnh khối lập phương con", "symbol": "a", "unit": "m", "meaning": "Kích thước hạt sau khi bẻ gãy phân chia"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Số khối con N = V_0 / a^3 = 1 / (10^-9)^3 = 10^27 khối.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Diện tích một khối s_1 = 6 a^2 = 6 * 10^-18 m^2. Tổng diện tích S = 10^27 * 6 * 10^-18 = 6 * 10^9 m^2 = 6000 km^2 (lớn hơn gấp đôi diện tích Hà Nội)."
      ],
      "variations_and_asymptotic_sweeps": ["Sự bùng nổ diện tích bề mặt giải thích khả năng hấp phụ và phản ứng hóa học cực mạnh."],
      "student_challenges_cer": ["Thử thách CER 3.4.2: So sánh diện tích bề mặt của 1 lon nước ngọt được tán thành các hạt nano 2 nm."]
    },
    {
      "mpt_id": "Luận điểm 3.4.3",
      "concept_introduction": "Năng lượng bề mặt và độ bất ổn định nhiệt động học: Liên kết chưa bão hòa (dangling bonds), hiện tượng tụ tập hạt nano (Agglomeration) và chín muồi Ostwald (Ostwald ripening).",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_03_Ket_Tu_Giam_Nang_Luong_Be_Mat.png",
        "interaction_id": "IMG_3.4.3_ORIG_AGGLOMERATION",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.4.3: Cơ chế giảm năng lượng tự do bề mặt qua hiện tượng kết tụ hạt nano (Slide 41 HUST)."
      },
      "minimal_working_example": "Tính biến thiên năng lượng tự do Gibbs khi hai khối lập phương cạnh L kết tụ thành một khối chữ nhật: Delta G = -2 gamma L^2 < 0.",
      "pillar_equation_latex": "\\Delta G_{\\mathrm{agglom}} = -2 \\gamma L^2 < 0, \\quad c(r) = c_\\infty \\exp\\left(\\frac{2\\gamma V_m}{r R_g T}\\right) \\quad (\\text{Gibbs-Thomson})",
      "nomenclature_table": [
        {"name": "Năng lượng bề mặt tự do", "symbol": "\\gamma", "unit": "J/m^2", "meaning": "Năng lượng cần thiết để tạo ra một đơn vị diện tích bề mặt mới"},
        {"name": "Độ hòa tan cân bằng của hạt bán kính r", "symbol": "c(r)", "unit": "mol/m^3", "meaning": "Độ hòa tan tăng cao ở các hạt có bán kính cong nhỏ theo phương trình Gibbs-Thomson"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Hai hạt lập phương có tổng diện tích 2 * 6 L^2 = 12 L^2.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi kết tụ, diện tích tiếp xúc biến mất 2 L^2, diện tích còn lại 10 L^2, giải phóng năng lượng Delta G = -2 gamma L^2."
      ],
      "variations_and_asymptotic_sweeps": ["Chín muồi Ostwald: Các hạt nhỏ tan ra và bồi đắp vào các hạt lớn để giảm tổng diện tích."],
      "student_challenges_cer": ["Thử thách CER 3.4.3: Thiết kế chất hoạt động bề mặt (Surfactant) để ngăn chặn hạt nano kết tụ."]
    },
    {
      "mpt_id": "Luận điểm 3.4.4",
      "concept_introduction": "Ứng dụng xúc tác nano (Nanocatalysis): Tâm hoạt tính bề mặt (active sites), năng lượng hoạt hóa giảm và hiệu quả kinh tế cắt giảm kim loại quý (Pt, Pd, Au).",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_04_Co_Che_Xuc_Tac_Nano.png",
        "interaction_id": "IMG_3.4.4_ORIG_CATALYSIS",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.4.4: Sơ đồ nguyên lý xúc tác hạt nano và giảm khối lượng kim loại quý (Slide 42 HUST)."
      },
      "minimal_working_example": "Đánh giá tốc độ phản ứng Arrhenius k = A exp(-E_a / k_B T) khi hạt nano xúc tác làm giảm năng lượng hoạt hóa E_a.",
      "pillar_equation_latex": "k_{\\mathrm{cat}} = A \\exp\\left(-\\frac{E_{a,\\mathrm{cat}}}{k_B T}\\right), \\quad E_{a,\\mathrm{cat}} < E_{a,0}",
      "nomenclature_table": [
        {"name": "Năng lượng hoạt hóa phản ứng", "symbol": "E_a", "unit": "eV", "meaning": "Rào cản thế năng tối thiểu để các phân tử phản ứng va chạm hiệu quả"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Các nguyên tử ở góc và cạnh của hạt nano có số phối trí thấp (undercoordinated atoms), tạo mật độ electron cục bộ cao đóng vai trò tâm hoạt tính xúc tác mạnh mẽ."
      ],
      "variations_and_asymptotic_sweeps": ["Xúc tác nano Pt trong pin nhiên liệu hydro cắt giảm 80% lượng bạch kim cần dùng."],
      "student_challenges_cer": ["Thử thách CER 3.4.4: Phân tích tại sao Vàng vĩ mô trơ hóa học nhưng hạt nano Vàng 3 nm lại là chất xúc tác cực nhạy cho phản ứng oxy hóa CO."]
    },
    {
      "mpt_id": "Luận điểm 3.4.5",
      "concept_introduction": "Ứng dụng cảm biến nano (Nanosensors): Độ nhạy cực đại, giới hạn phát hiện (LOD) tới mức đơn phân tử theo cơ chế chìa khóa - ổ khóa (Lock and Key).",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_05_Co_Che_Cam_Bien_Lock_Key.png",
        "interaction_id": "IMG_3.4.5_ORIG_SENSOR",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.4.5: Cơ chế nhận diện cảm biến sinh hóa nano theo mô hình Ổ khóa - Chìa khóa (Slide 43 HUST)."
      },
      "minimal_working_example": "Độ biến thiên điện trở Delta R / R_0 tỉ lệ thuận với tỉ số S/V khi khí độc bám dính vào bề mặt dây nano SnO2.",
      "pillar_equation_latex": "\\frac{\\Delta R}{R_0} \\propto \\left(\\frac{S}{V}\\right) \\cdot \\Delta N_{\\mathrm{ads}} \\propto \\frac{1}{D} \\cdot \\theta_{\\mathrm{gas}}",
      "nomenclature_table": [
        {"name": "Độ nhạy cảm biến tương đối", "symbol": "\\Delta R / R_0", "unit": "không thứ nguyên", "meaning": "Tỉ số biến thiên điện trở trên điện trở ban đầu khi có khí mục tiêu"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Bề dày lớp nghèo điện tử Debye lambda_D ~ 3-5 nm. Khi đường kính dây nano D ~ 2 lambda_D, toàn bộ tiết diện dây nano bị điều biến, tạo độ nhạy vô hạn."
      ],
      "variations_and_asymptotic_sweeps": ["Cảm biến dây nano có thể phát hiện khí độc ppm/ppb."],
      "student_challenges_cer": ["Thử thách CER 3.4.5: Giải thích tại sao cảm biến màng mỏng vĩ mô kém nhạy hơn cảm biến dây nano 1000 lần."]
    }
  ]
}

with open(os.path.join(DATA_DIR, "BLUEPRINT_MUC_3.4_NANO.json"), "w", encoding="utf-8") as f:
    json.dump(bp_3_4, f, ensure_ascii=False, indent=2)
print("BLUEPRINT_MUC_3.4_NANO.json created.")

# ---------------------------------------------------------------------------
# BLUEPRINT 3.5
# ---------------------------------------------------------------------------
bp_3_5 = {
  "lesson_title": "Chương 3: Đặc trưng của vật liệu khi kích thước giảm - Mục 3.5: Tính chất điện quang, cộng hưởng plasmon bề mặt (LSPR) và chấm lượng tử bán dẫn",
  "section_id": "Mục 3.5",
  "source_document_citations": [
    "Bài 3-Properties.pdf (Slide 44 đến 48), Bộ môn Vật liệu Điện tử - Viện Vật lý Kỹ thuật HUST",
    "Edward L. Wolf, Nanophysics and Nanotechnology, Wiley-VCH, 2006 (Chapter 3)",
    "Charles P. Poole Jr., Frank J. Owens, Introduction to Nanotechnology, John Wiley & Sons, 2003"
  ],
  "total_pages_estimate": 19,
  "micro_point_topics": [
    {
      "mpt_id": "Luận điểm 3.5.1",
      "concept_introduction": "Hiệu ứng giam hãm lượng tử và chuyển pha Kim loại - Bán dẫn (Hiệu ứng Kubo): Sự gián đoạn hóa mức năng lượng delta = E_F / N khi kích thước giảm làm mở ra vùng cấm năng lượng hữu hạn ở hạt nano kim loại.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_06_Giam_Giu_Mo_Vung_Cam_Kim_Loai.png",
        "interaction_id": "IMG_3.5.1_ORIG_KUBO",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.5.1: Sự mở vùng cấm năng lượng hữu hạn và chuyển pha kim loại - bán dẫn (Slide 44 HUST)."
      },
      "minimal_working_example": "Khoảng cách mức năng lượng Kubo delta = 4 E_F / (3 N). Khi delta > k_B T, hạt kim loại mất tính dẫn điện kim loại và trở thành chất bán dẫn.",
      "pillar_equation_latex": "\\delta_{\\mathrm{Kubo}} = \\frac{4 E_F}{3 N} = \\frac{4 E_F}{3 \\rho_n V} \\propto \\frac{1}{R^3}",
      "nomenclature_table": [
        {"name": "Khoảng cách mức Kubo", "symbol": "\\delta_{\\mathrm{Kubo}}", "unit": "eV", "meaning": "Khoảng cách năng lượng trung bình giữa các mức lượng tử lân cận trong hạt nano"},
        {"name": "Số lượng electron tự do trong hạt", "symbol": "N", "unit": "nguyên", "meaning": "Tổng số electron dẫn tỉ lệ thuận với thể tích hạt N propto R^3"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Ở kim loại vĩ mô, N ~ 10^23 => delta ~ 10^-22 eV << k_B T, dải năng lượng là liên tục.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Ở hạt nano R = 1 nm, N ~ 100 => delta ~ 0.1 eV >> k_B T (ở 300 K k_B T = 0.026 eV), làm đóng băng chuyển động nhiệt electron, hạt trở thành cách điện/bán dẫn."
      ],
      "variations_and_asymptotic_sweeps": ["Chuyển pha phụ thuộc kích thước và nhiệt độ."],
      "student_challenges_cer": ["Thử thách CER 3.5.1: Tính nhiệt độ Kubo T_Kubo cho hạt nano nhôm bán kính 1.5 nm."]
    },
    {
      "mpt_id": "Luận điểm 3.5.2",
      "concept_introduction": "Hiện tượng khóa Coulomb (Coulomb Blockade) & Transistor đơn electron (SET): Năng lượng nạp tĩnh điện E_c = e^2 / (2C) vượt trội năng lượng nhiệt k_B T ngăn cản từng electron đơn lẻ chui qua đảo lượng tử.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\Mo_Phong_Muc_3.5_Do_Thi_02_Coulomb_Blockade_SET.png",
        "interaction_id": "IMG_3.5.2_SIM_SET",
        "aspect_ratio": "6.5:4.2",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.5.2: Đặc tuyến I-V khóa Coulomb và dao động dẫn truyền Coulomb trong SET (Mô phỏng ZT-GVLE)."
      },
      "minimal_working_example": "Điều kiện quan sát khóa Coulomb: E_c = e^2 / (2C) >> k_B T và điện trở rào xuyên hầm R_T >> h / e^2 = 25.8 kOhm.",
      "pillar_equation_latex": "E_c = \\frac{e^2}{2 C} \\gg k_B T, \\quad R_T \\gg \\frac{h}{e^2} \\approx 25.8\\ \\mathrm{k}\\Omega, \\quad \\Delta V_g = \\frac{e}{C_g}",
      "nomenclature_table": [
        {"name": "Năng lượng nạp Coulomb", "symbol": "E_c", "unit": "eV hoặc J", "meaning": "Năng lượng tĩnh điện cần thiết để nạp thêm một electron vào đảo dẫn"},
        {"name": "Điện dung tổng cộng của đảo", "symbol": "C", "unit": "F", "meaning": "Tổng điện dung tiếp giáp nguồn, máng và cổng C = C_s + C_d + C_g"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Để hoạt động ở nhiệt độ phòng 300 K (k_B T = 26 meV), yêu cầu E_c >= 260 meV => C <= e^2 / (2 * 260 meV) ~ 0.3 aF (attofarad).",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Điện dung của hạt cầu C = 4 pi epsilon_0 epsilon_r R <= 0.3 aF đòi hỏi bán kính R <= 1.5 nm."
      ],
      "variations_and_asymptotic_sweeps": ["Chu kỳ dao động dẫn truyền Coulomb theo điện áp cổng Delta V_g = e / C_g."],
      "student_challenges_cer": ["Thử thách CER 3.5.2: Thiết kế transistor đơn electron hoạt động ở 300 K."]
    },
    {
      "mpt_id": "Luận điểm 3.5.3",
      "concept_introduction": "Tương tác quang học toàn phần và cân bằng quang thông: Bảo toàn năng lượng chùm sáng tới I_0 = T + A + R + S và sự áp đảo của tán xạ Rayleigh (S propto R^6 / lambda^4) khi kích thước hạt giảm.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_07_Tuong_Tac_Quang_Tan_Xa_Hat_Keo.png",
        "interaction_id": "IMG_3.5.3_ORIG_LIGHT_BALANCE",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.5.3: Cân bằng quang thông I = T + A + R + S trong hệ keo nano (Slide 45 HUST)."
      },
      "minimal_working_example": "Định luật tán xạ Rayleigh: Tiết diện tán xạ sigma_sca propto R^6 / lambda^4 so với tiết diện hấp thụ sigma_abs propto R^3 / lambda.",
      "pillar_equation_latex": "I_0 = T + A + R + S, \\quad \\sigma_{\\mathrm{sca}} = \\frac{8\\pi}{3} k^4 R^6 \\left|\\frac{m^2 - 1}{m^2 + 2}\\right|^2 \\propto \\frac{R^6}{\\lambda^4}",
      "nomenclature_table": [
        {"name": "Tiết diện tán xạ Rayleigh", "symbol": "\\sigma_{\\mathrm{sca}}", "unit": "m^2", "meaning": "Xác suất tán xạ ánh sáng của hạt có kích thước nhỏ hơn nhiều bước sóng R << lambda"},
        {"name": "Chiết suất tương đối", "symbol": "m = n_{\\mathrm{particle}} / n_{\\mathrm{medium}}", "unit": "không thứ nguyên", "meaning": "Tỉ số chiết suất của hạt nano so với môi trường phân tán"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Ở hạt rất nhỏ R <= 10 nm, hấp thụ tỉ lệ R^3 chiếm ưu thế áp đảo so với tán xạ tỉ lệ R^6 (hạt chủ yếu hấp thụ).",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Khi hạt lớn lên R >= 50 nm, tán xạ R^6 tăng vọt và chi phối độ đục của dung dịch."
      ],
      "variations_and_asymptotic_sweeps": ["Giải thích màu xanh của bầu trời và màu đỏ hoàng hôn theo định luật Rayleigh lambda^-4."],
      "student_challenges_cer": ["Thử thách CER 3.5.3: So sánh tỉ số tán xạ / hấp thụ của hạt vàng 10 nm vs 80 nm."]
    },
    {
      "mpt_id": "Luận điểm 3.5.4",
      "concept_introduction": "Cộng hưởng Plasmon Bề mặt Cục bộ (LSPR): Dao động tập thể của electron tự do trong hạt nano kim loại, điều kiện cộng hưởng Fröhlich Re(epsilon_m) = -2 epsilon_d, và màu sắc keo Au/Ag.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_08_Cong_Huong_Plasmon_LSPR.png",
        "interaction_id": "IMG_3.5.4_ORIG_LSPR",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.5.4: Hiện tượng cộng hưởng plasmon bề mặt cục bộ LSPR và màu sắc keo vàng đỏ rực rỡ (Slide 46 HUST)."
      },
      "minimal_working_example": "Tính bước sóng LSPR của hạt Vàng (520 nm) và Bạc (410 nm) trong nước theo lý thuyết Mie.",
      "pillar_equation_latex": "\\sigma_{\\mathrm{ext}} = 9\\frac{\\omega}{c}\\varepsilon_m^{3/2} V \\frac{\\varepsilon_2(\\omega)}{[\\varepsilon_1(\\omega) + 2\\varepsilon_m]^2 + \\varepsilon_2(\\omega)^2}, \\quad \\varepsilon_1(\\omega_{\\mathrm{LSPR}}) = -2\\varepsilon_m",
      "nomenclature_table": [
        {"name": "Hằng số điện môi của hạt nano", "symbol": "\\varepsilon(\\omega) = \\varepsilon_1 + i \\varepsilon_2", "unit": "không thứ nguyên", "meaning": "Hàm điện môi Drude-Sommerfeld của kim loại quý"},
        {"name": "Hằng số điện môi môi trường", "symbol": "\\varepsilon_m = n_m^2", "unit": "không thứ nguyên", "meaning": "Chiết suất bình phương của dung môi (nước n_m = 1.33 => epsilon_m = 1.77)"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Mô hình Drude epsilon_1(omega) = 1 - omega_p^2 / omega^2. Thay vào điều kiện Fröhlich 1 - omega_p^2 / omega^2 = -2 epsilon_m.",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Suy ra tần số cộng hưởng LSPR: omega_LSPR = omega_p / sqrt(1 + 2 epsilon_m). Khi chiết suất môi trường n_m tăng, omega_LSPR giảm (dịch đỏ bước sóng lambda_LSPR tăng)."
      ],
      "variations_and_asymptotic_sweeps": ["Ứng dụng làm cảm biến sinh học LSPR siêu nhạy đo sự gắn kết phân tử ADN."],
      "student_challenges_cer": ["Thử thách CER 3.5.4: Tính độ dịch bước sóng LSPR khi kháng thể gắn lên hạt nano vàng."]
    },
    {
      "mpt_id": "Luận điểm 3.5.5",
      "concept_introduction": "Chấm lượng tử bán dẫn (Quantum Dots): Mô hình Brus giải thích mở rộng vùng cấm E_g(R), năng lượng giam giữ động năng tỉ lệ 1/R^2, thế hút Coulomb tỉ lệ -1/R, và điều khiển màu sắc phát xạ huỳnh quang.",
      "visual_anchor": {
        "image_file_path": "G:\\My Drive\\NotebookLM - Academic Knowledge Base\\Cơ sở vật lý và công nghệ nano\\Kho_Hinh_Anh\\[Goc]_Muc_3.5_Hinh_09_Phat_Xa_Cham_Luong_Tu.png",
        "interaction_id": "IMG_3.5.5_ORIG_QD",
        "aspect_ratio": "16:9",
        "brand_palette_compliant": True,
        "pedagogical_caption": "Hình 3.5.5: Phổ phát xạ huỳnh quang đơn sắc điều khiển theo kích thước chấm lượng tử CdSe (Slide 47 HUST)."
      },
      "minimal_working_example": "Phương trình Brus tính vùng cấm E_g(R) của chấm lượng tử CdSe với E_{g,bulk} = 1.74 eV, bán kính R từ 1.5 nm đến 4 nm.",
      "pillar_equation_latex": "E_g(R) = E_{g,\\mathrm{bulk}} + \\frac{\\hbar^2 \\pi^2}{2 m_{eh}^* R^2} - \\frac{1.786 e^2}{4\\pi \\varepsilon_r \\varepsilon_0 R}, \\quad \\frac{1}{m_{eh}^*} = \\frac{1}{m_e^*} + \\frac{1}{m_h^*}",
      "nomenclature_table": [
        {"name": "Độ rộng vùng cấm hiệu dụng", "symbol": "E_g(R)", "unit": "eV", "meaning": "Khoảng cách năng lượng giữa trạng thái kích thích đáy dải dẫn và đỉnh dải hóa trị"},
        {"name": "Khối lượng rút gọn exciton", "symbol": "m_{eh}^*", "unit": "kg", "meaning": "Khối lượng hiệu dụng tương đương của cặp điện tử - lỗ trống"}
      ],
      "guided_practice_steps": [
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thành phần giam giữ lượng tử hbar^2 pi^2 / (2 m^* R^2) tỉ lệ 1/R^2 chiếm ưu thế tuyệt đối ở bán kính nhỏ, làm năng lượng phát xạ dịch mạnh về phía xanh (Blue Shift).",
        "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Thay số cho CdSe: Hạt R = 1.5 nm phát xạ xanh lam (lambda = 480 nm, 2.58 eV), hạt R = 4 nm phát xạ đỏ rực rỡ (lambda = 620 nm, 2.0 eV)."
      ],
      "variations_and_asymptotic_sweeps": ["Ứng dụng: Màn hình hiển thị QLED chấm lượng tử gam màu siêu rộng và đánh dấu tế bào ung thư."],
      "student_challenges_cer": ["Thử thách CER 3.5.5: Tính bán kính chấm lượng tử CdSe để phát ra ánh sáng vàng 580 nm."]
    }
  ]
}

with open(os.path.join(DATA_DIR, "BLUEPRINT_MUC_3.5_NANO.json"), "w", encoding="utf-8") as f:
    json.dump(bp_3_5, f, ensure_ascii=False, indent=2)
print("BLUEPRINT_MUC_3.5_NANO.json created.")

print("All blueprints 3.2, 3.3, 3.4, 3.5 created successfully!")

# -*- coding: utf-8 -*-
r"""
Script đóng gói toàn bộ tài nguyên cần thiết cho Gemini Spark Custom Gem.
Tạo thư mục \GEMINI_SPARK_DEPLOYMENT_PACKAGE\
"""

import os
import sys
import shutil
import zipfile
import re

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r""
SPARK_SKILLS_DIR = r"\teacher skills gemini spark\individual_skill_zips"
OUTPUT_DIR = r"\GEMINI_SPARK_DEPLOYMENT_PACKAGE"

DIR_01 = os.path.join(OUTPUT_DIR, "01_GEM_SYSTEM_INSTRUCTIONS")
DIR_02 = os.path.join(OUTPUT_DIR, "02_KNOWLEDGE_DOCUMENTS")
DIR_03 = os.path.join(OUTPUT_DIR, "03_SKILL_ZIP_PACKAGES")
DIR_04 = os.path.join(OUTPUT_DIR, "04_DEPLOYMENT_GUIDE")

for d in [DIR_01, DIR_02, DIR_03, DIR_04]:
    os.makedirs(d, exist_ok=True)

# 1. 01_GEM_SYSTEM_INSTRUCTIONS/GEMINI_SPARK_SYSTEM_INSTRUCTIONS.txt
src_prompt = os.path.join(BASE_DIR, "PROMPT_GEMINI_SPARK_STANDALONE.md")
with open(src_prompt, "r", encoding="utf-8") as f:
    prompt_content = f.read()

dest_txt = os.path.join(DIR_01, "GEMINI_SPARK_SYSTEM_INSTRUCTIONS.txt")
with open(dest_txt, "w", encoding="utf-8") as f:
    f.write(prompt_content)

print(f"[OK] Đã tạo System Instructions ({len(prompt_content)} ký tự): {dest_txt}")

# 2. 02_KNOWLEDGE_DOCUMENTS/
# File 01: Bán dẫn & CODATA
file_01_content = """# CƠ SỞ DỮ LIỆU VẬT LIỆU BÁN DẪN & HẰNG SỐ VẬT LÝ CODATA (300 K)

Tài liệu tham chiếu chuẩn mực cho Gemini Spark phục vụ tính toán, phân tích giải tích và đối thoại chuyên sâu cùng Lead Researcher ().

---

## I. HẰNG SỐ VẬT LÝ CĂN BẢN (CODATA 2022)

| Tên hằng số | Ký hiệu | Giá trị số | Đơn vị SI |
| :--- | :---: | :---: | :--- |
| Điện tích nguyên tố | $q$ | $1{,}602176634 \times 10^{-19}$ | $\\text{C}$ |
| Hằng số Planck rút gọn | $\\hbar$ | $1{,}054571817 \times 10^{-34}$ | $\\text{J}\\cdot\\text{s}$ |
| Hằng số Planck | $h$ | $6{,}62607015 \times 10^{-34}$ | $\\text{J}\\cdot\\text{s}$ |
| Khối lượng nghỉ electron | $m_0$ | $9{,}1093837 \times 10^{-31}$ | $\\text{kg}$ |
| Hằng số Boltzmann | $k_B$ | $1{,}380649 \times 10^{-23}$ | $\\text{J}/\\text{K}$ |
| Hằng số Boltzmann (năng lượng) | $k_B$ | $8{,}617333262 \times 10^{-5}$ | $\\text{eV}/\\text{K}$ |
| Độ điện thẩm chân không | $\\varepsilon_0$ | $8{,}8541878128 \times 10^{-12}$ | $\\text{F}/\\text{m}$ |
| Vận tốc ánh sáng chân không | $c$ | $2{,}99792458 \times 10^8$ | $\\text{m}/\\text{s}$ |
| Năng lượng nhiệt ở 300 K | $k_B T$ | $0{,}02585$ | $\\text{eV}$ ($25{,}85\\text{ meV}$) |

---

## II. THÔNG SỐ VẬT LIỆU BÁN DẪN Ở NHIỆT ĐỘ PHÒNG (300 K)

| Bán dẫn | Loại vùng cấm | $E_g\\text{ (eV)}$ | Bước sóng $\\lambda_g\\text{ (}\\mu\\text{m)}$ | $m_e^*/m_0$ | $m_{hh}^*/m_0$ | $\\varepsilon_r$ | Chiết suất $n_r$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **GaAs** | Trực tiếp | $1{,}424$ | $0{,}871$ | $0{,}067$ | $0{,}450$ | $12{,}9$ | $3{,}65$ |
| **InP** | Trực tiếp | $1{,}344$ | $0{,}923$ | $0{,}077$ | $0{,}600$ | $12{,}5$ | $3{,}17$ |
| **GaN** | Trực tiếp | $3{,}420$ | $0{,}363$ | $0{,}200$ | $0{,}800$ | $8{,}9$ | $2{,}40$ |
| **Si** | Gián tiếp | $1{,}120$ | $1{,}107$ | $1{,}080$ | $0{,}560$ | $11{,}7$ | $3{,}42$ |
| **Ge** | Gián tiếp | $0{,}660$ | $1{,}879$ | $0{,}550$ | $0{,}370$ | $16{,}0$ | $4{,}00$ |

### 1. Hợp kim ba nguyên tử $\\text{Al}_x\\text{Ga}_{1-x}\\text{As}$ (300 K):
- Vùng cấm trực tiếp ($x \\le 0{,}45$):
  $$E_g^\\Gamma(x) = 1{,}424 + 1{,}247x\\text{ [eV]}$$
- Vùng cấm gián tiếp ($x > 0{,}45$):
  $$E_g^X(x) = 1{,}900 + 0{,}125x + 0{,}143x^2\\text{ [eV]}$$

### 2. Sự phụ thuộc nhiệt độ của vùng cấm (Mô hình Varshni):
$$E_g(T) = E_g(0) - \\frac{\\alpha T^2}{T + \\beta}$$
- **GaAs:** $\\alpha = 5{,}405 \\times 10^{-4}\\text{ eV/K}$, $\\beta = 204\\text{ K}$, $E_g(0) = 1{,}519\\text{ eV}$.
- **InP:** $\\alpha = 4{,}900 \\times 10^{-4}\\text{ eV/K}$, $\\beta = 327\\text{ K}$, $E_g(0) = 1{,}424\\text{ eV}$.
- **Si:** $\\alpha = 4{,}730 \\times 10^{-4}\\text{ eV/K}$, $\\beta = 636\\text{ K}$, $E_g(0) = 1{,}170\\text{ eV}$.
"""

with open(os.path.join(DIR_02, "01_Co_So_Du_Lieu_Ban_Dan_Va_Hang_So_CODATA_300K.md"), "w", encoding="utf-8") as f:
    f.write(file_01_content)

# File 02: Danh pháp song ngữ ATCC
file_02_content = """# CHUẨN DANH PHÁP THUẬT NGỮ SONG NGỮ ATCC (ANH - VIỆT)

Tuân thủ nghiêm ngặt quy tắc Nghị định 30/2020/NĐ-CP (viết thường danh từ chung giữa câu, sentence case cho tiêu đề), định dạng APA 7 và đơn vị đo lường Luật 04.

---

## I. BẢNG ĐỐI CHIẾU THUẬT NGỮ CỐT LÕI (QUANG ĐIỆN TỬ & BÁN DẪN)

| Thuật ngữ tiếng Việt chuẩn | English Term | Ký hiệu | Bản chất vi mô & Ý nghĩa vật lý |
| :--- | :--- | :---: | :--- |
| Dải dẫn / Vùng dẫn | Conduction band | $E_c$ | Vùng năng lượng chứa các electron tự do tham gia dẫn điện |
| Dải hóa trị / Vùng hóa trị | Valence band | $E_v$ | Vùng năng lượng điền đầy electron liên kết, tạo lỗ trống khi electron nhảy lên vùng dẫn |
| Vùng cấm | Energy bandgap | $E_g$ | Khoảng cách năng lượng giữa đáy vùng dẫn và đỉnh vùng hóa trị |
| Mức Fermi chuẩn | Quasi-Fermi level | $E_{Fc}, E_{Fv}$ | Thế hóa học của electron và lỗ trống khi bị kích thích khỏi trạng thái cân bằng nhiệt |
| Nghịch đảo độ tích lũy | Population inversion | $N_2 > N_1$ | Trạng thái mật độ hạt tải ở mức cao vượt trội mức thấp ($E_{Fc} - E_{Fv} > h\\nu$) |
| Phát xạ tự phát | Spontaneous emission | $R_{\\text{sp}}$ | Electron tái hợp ngẫu nhiên không pha kết hợp, sinh photon không định hướng |
| Phát xạ kích thích | Stimulated emission | $R_{\\text{st}}$ | Photon tới kích thích electron tái hợp, sinh photon thứ hai cùng tần số, pha và hướng |
| Dòng ngưỡng | Threshold current | $I_{\\text{th}}$ | Dòng điện bơm tối thiểu để độ lợi quang học cân bằng tổng suy hao hốc cộng hưởng |
| Hiệu suất lượng tử vi phân | Differential quantum efficiency | $\\eta_d$ | Tỉ số giữa số photon phát xạ tăng thêm và số hạt tải bơm vào trên dòng ngưỡng |
| Giếng lượng tử | Quantum well | QW | Cấu trúc bán dẫn siêu mỏng làm giam hãm chuyển động hạt tải theo một chiều không gian |
| Hệ số giam hãm trường quang | Optical confinement factor | $\\Gamma$ | Tỉ lệ năng lượng của mode quang học chồng lấn với vùng hoạt tính |
| Gương phản xạ Bragg phân tán | Distributed Bragg reflector | DBR | Cấu trúc đa lớp chiết suất xen kẽ $\\lambda/4$ tạo độ phản xạ cao qua giao thoa tăng cường |

---

## II. QUY TẮC HIỂN THỊ TRONG VĂN BẢN & ĐỒ THỊ
1. **Định dạng văn bản:** Luôn xuất hiện dạng `thuật ngữ tiếng Việt (english term)` ở lần đầu và giữ ngữ nghĩa chuẩn xác.
2. **Quy tắc viết hoa:** Cấm viết hoa danh từ chung giữa câu (ví dụ: viết *"vùng cấm quang học"*, không viết *"Vùng Cấm Quang Học"*).
3. **Quy tắc viết số:** Dùng dấu phẩy `,` cho số thập phân (`1,424 eV`), khoảng số dùng en-dash `–` (`5–10 nm`).
"""

with open(os.path.join(DIR_02, "02_Chuan_Danh_Phap_Thuat_Ngu_ATCC_Song_Ngu.md"), "w", encoding="utf-8") as f:
    f.write(file_02_content)

# File 03: Cẩm nang Sư phạm Feynman & MALAE & 5 Mắt xích OCR
file_03_content = """# CẨM NANG SƯ PHẠM FEYNMAN, THUẬT TOÁN MALAE VÀ 5 MẮT XÍCH OCR

Tài liệu định chuẩn phương pháp luận sư phạm cho Gemini Spark trong mọi phản hồi học thuật với Lead Researcher.

---

## 1. NGUYÊN LÝ SƯ PHẠM FEYNMAN (UFME ENGINE)
- **Cơ chế:** Giải thích mọi hiện tượng từ các định luật cơ bản nhất (bảo toàn năng lượng, xung lượng tinh thể, đối xứng dải năng lượng, phân bố Fermi-Dirac).
- **Chuỗi nhân quả vi mô (Micro-causal Flowchains $\\le 65$ từ/khối):**
  `[Tác nhân bơm/kích thích] ──> [Tương tác vi mô] ──> [Biến đổi nồng độ/trường] ──> [Đáp ứng vĩ mô]`
- **Kiêng kỵ tuyệt đối:** Cấm dùng ẩn dụ cơ học thô sơ (như nước chảy qua ống, xe chạy trên đường) để giải thích bán dẫn lượng tử. Phải dùng trực giác không gian dải năng lượng ($E\\text{–}z$, $E\\text{–}k$).

---

## 2. THUẬT TOÁN MALAE — GIẢI PHẪU PHƯƠNG TRÌNH 3 CẤP ĐỘ
Khi người học hỏi về bất kỳ công thức toán học nào:
- **Cấp 1 — Trực giác Vật lý (Physical Intuition):** Ý nghĩa bảo toàn, nguồn gốc định luật.
- **Cấp 2 — Bảng Định danh Biến số Chuẩn ISO 80000-2:**
  Bảng 4 cột: `Tên đại lượng` | `Ký hiệu` | `Đơn vị SI` | `Ý nghĩa vi mô & Vai trò động học`.
  *(Quy tắc Zero-Slash-Fractions: Mọi công thức chứa phân số phải dùng phân số gạch ngang $\\frac{a}{b}$).*
- **Cấp 3 — Giới hạn Tiệm cận & Tính Đối xứng:**
  Khảo sát khi biến số tiến tới 0 hoặc vô cùng ($T \\to 0\\text{ K}$, $\\omega \\to \\infty$), kiểm tra tính đối xứng chẵn lẻ.

---

## 3. THUẬT TOÁN 6 — GIẢI TRÌNH HÌNH ẢNH THEO 5 MẮT XÍCH OCR
1. **Mắt xích 1 (Bối cảnh học thuật):** Vị trí và mục đích của hình vẽ trong bài giảng.
2. **Mắt xích 2 (Cơ chế lực vi mô):** Đường truyền photon, thế giam hãm thế lượng tử, tương tác hạt tải.
3. **Mắt xích 3 (Mô hình toán học):** Phương trình giải tích trực tiếp của các đường cong đồ thị.
4. **Mắt xích 4 (Điểm uốn & Ngưỡng tới hạn):** Dòng ngưỡng $I_{\\text{th}}$, độ dốc dI/dV, tần số cắt.
5. **Mắt xích 5 (Ứng dụng chế tạo & Lab thực tế):** Hệ quả đối với việc thiết kế cấu trúc laser diode hay màng mỏng quang học.

---

## 4. CHẤM BÀI CER & CƠ CHẾ SILENT DROP
- **Claim:** Nhận định kỹ thuật có dứt khoát, đi thẳng vào trọng tâm không?
- **Evidence:** Có viện dẫn phương trình, số liệu 300 K hoặc dữ kiện Lab cụ thể không?
- **Reasoning:** Logic bắc cầu nguyên nhân - hệ quả có liền mạch không, có bị ngộ nhận không?
- **Silent Drop:** AI không nhận xét chung chung "bạn làm tốt lắm". Chỉ thẳng vào điểm mù bằng nguyên lý đầu và kết thúc bằng một câu hỏi đối trọng ngắn gọn.
"""

with open(os.path.join(DIR_02, "03_Cam_Nang_Su_Pham_Feynman_MALAE_Va_5_Mat_Xich_OCR.md"), "w", encoding="utf-8") as f:
    f.write(file_03_content)

# File 04: Python Sandbox Plotting Template
file_04_content = r"""# -*- coding: utf-8 -*-
\"\"\"
Kịch bản mẫu vẽ đồ thị giải tích tự chứa chuẩn ZT-GVLE cho Gemini Spark Python Sandbox.
\"\"\"

import numpy as np
import matplotlib.pyplot as plt

# 1. Khởi tạo canvas tỷ lệ vàng chuẩn
fig, ax = plt.subplots(figsize=(6.5, 4.3), dpi=300)

# 2. Khóa cứng bảng màu chuẩn MATLAB
COLOR_BLUE = "#0072BD"
COLOR_ORANGE = "#D95319"
COLOR_DARK = "#222222"

# 3. Tính toán giải tích (Ví dụ: So sánh Lượng tử vs Cổ điển)
xi = np.linspace(-4.5, 4.5, 500)
psi0_sq = (1.0 / np.sqrt(np.pi)) * np.exp(-xi**2)

# 4. Vẽ đường cong
ax.plot(xi, psi0_sq, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Lượng tử trạng thái cơ bản } n = 0$")

# 5. Định dạng trục chuẩn Mathtext (Luật 14: Zero-Slash-Fractions)
ax.set_xlabel(r"$\text{Tọa độ không thứ nguyên, } \xi = \sqrt{\frac{m \cdot \omega}{\hbar}} \cdot x$", fontsize=10.5, fontweight="bold")
ax.set_ylabel(r"$\text{Mật độ xác suất tìm hạt, } |\psi_0(\xi)|^2$", fontsize=10.5, fontweight="bold")
ax.set_title(r"$\text{Mật độ xác suất dao động tử điều hòa lượng tử trạng thái cơ bản}$", fontsize=11.0, fontweight="bold", pad=28)

# 6. Thuật toán 13 ZT-GVLE: Legend đưa hoàn toàn ra ngoài trục (giải phóng 100% lòng đồ thị)
ax.legend(bbox_to_anchor=(0.5, 1.02), loc="lower center", ncol=1, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.5)

# 7. Triple Buffer Envelope: Chú thích cách xa đường cong, font >= 9.5 pt
ax.annotate(
    r"$\text{Cực đại tại } \xi = 0 \text{ (Đối lập cổ điển)}$",
    xy=(0.0, 0.56),
    xytext=(0.4, 0.45),
    arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
    fontsize=9.5,
    bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec="#CED4DA", alpha=0.95)
)

plt.tight_layout()
plt.show()
"""

with open(os.path.join(DIR_02, "04_Kich_Ban_Ve_Do_Thi_Sandbox_Chuan_ZT_GVLE.py"), "w", encoding="utf-8") as f:
    f.write(file_04_content)

print(f"[OK] Đã tạo 4 tệp Knowledge Documents trong {DIR_02}")

# 3. 03_SKILL_ZIP_PACKAGES/
needed_skills = [
    "academic-terminology-guardian.zip",
    "engineering-instructor.zip",
    "physics-diagram-studio.zip",
    "user-insights-profiler.zip",
    "semiconductor-photonics-lab.zip"
]

for skill_zip in needed_skills:
    src_zip = os.path.join(SPARK_SKILLS_DIR, skill_zip)
    dest_zip = os.path.join(DIR_03, skill_zip)
    if os.path.exists(src_zip):
        shutil.copy2(src_zip, dest_zip)
        print(f"[OK] Đã sao chép kỹ năng có sẵn: {skill_zip}")
    else:
        # Nếu chưa có zip cho semiconductor-photonics-lab, ta zip trực tiếp từ source
        skill_src_dir = os.path.join(BASE_DIR, ".agents", "skills", skill_zip.replace(".zip", ""))
        if os.path.exists(skill_src_dir):
            with zipfile.ZipFile(dest_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(skill_src_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, skill_src_dir)
                        zipf.write(file_path, arcname)
            print(f"[OK] Đã đóng gói tự động kỹ năng: {skill_zip}")

# 4. 04_DEPLOYMENT_GUIDE/HUONG_DAN_CAU_HINH_GEMINI_SPARK.md
guide_content = """# HƯỚNG DẪN THIẾT LẬP GEMINI SPARK CUSTOM GEM (TỪNG BƯỚC)

Tài liệu hướng dẫn Lead Researcher cấu hình và triển khai hệ thống học tập 1-1 trên Gemini Spark (Web & Mobile).

---

## BƯỚC 1: KHỞI TẠO GEM MỚI TRÊN GEMINI
1. Truy cập [gemini.google.com/gems](https://gemini.google.com/gems) trên trình duyệt hoặc mở ứng dụng Gemini trên điện thoại/máy tính bảng.
2. Bấm vào nút **New Gem** (+ Tạo Gem mới).
3. Đặt thông tin cơ bản:
   - **Name (Tên Gem):** `HUST Academic Instructor & Feynman Mentor` (hoặc `Cố Vấn Học Thuật HUST`)
   - **Description (Mô tả):** `Chuyên gia giảng dạy Quang điện tử, Bán dẫn & Nano theo nguyên lý Feynman và đồng hành đọc chuyên khảo PDF cùng Lead Researcher.`

---

## BƯỚC 2: CẤU HÌNH INSTRUCTIONS (HƯỚNG DẪN HỆ THỐNG)
1. Mở tệp: `\\GEMINI_SPARK_DEPLOYMENT_PACKAGE\\01_GEM_SYSTEM_INSTRUCTIONS\\GEMINI_SPARK_SYSTEM_INSTRUCTIONS.txt`
2. Chọn toàn bộ nội dung (`Ctrl + A`) và Sao chép (`Ctrl + C`).
3. Dán (`Ctrl + V`) vào ô **Instructions** của Custom Gem.
4. Kiểm tra độ dài: Văn bản khoảng 17.000 ký tự (nằm hoàn toàn trong giới hạn cho phép của Gemini Gems).

---

## BƯỚC 3: NẠP TRI THỨC (KNOWLEDGE BASE)
Tại phần **Knowledge** của Gem:
1. **Cách 1 (Khuyên dùng - Nạp tệp trực tiếp):** Tải lên các tệp trong thư mục:
   `\\GEMINI_SPARK_DEPLOYMENT_PACKAGE\\02_KNOWLEDGE_DOCUMENTS\\`
   - `01_Co_So_Du_Lieu_Ban_Dan_Va_Hang_So_CODATA_300K.md`
   - `02_Chuan_Danh_Phap_Thuat_Ngu_ATCC_Song_Ngu.md`
   - `03_Cam_Nang_Su_Pham_Feynman_MALAE_Va_5_Mat_Xich_OCR.md`
2. **Cách 2 (Kết nối Google Drive):**
   - Bấm vào biểu tượng Drive và chọn thư mục: `NotebookLM - Academic Knowledge Base` để Gem có thể truy xuất trực tiếp các tệp chuyên khảo PDF và hình ảnh do Antigravity biên soạn.

---

## BƯỚC 4: LƯU & KIỂM THỬ THỰC TẾ
1. Bấm **Save** (Lưu) để hoàn tất.
2. **Kiểm thử Chế độ 1 (Lệnh /learn ~2s):**
   Gõ:
   ```text
   /learn Mục 3.1 Chương 3 Cơ sở vật lý và công nghệ nano
   ```
   *Kỳ vọng:* AI phản hồi trong ~2 giây, chỉ xuất duy nhất Bộ ba Mỏ neo Điều hướng (Link Docs, Link PDF, Link Ảnh), không in văn bản dài ra chat.
3. **Kiểm thử Chế độ 2 (Đối thoại 1-1 Feynman):**
   Mở tệp PDF chuyên khảo trên máy tính bảng và hỏi:
   ```text
   Tại sao trong công thức dao động tử điều hòa lượng tử lại xuất hiện hằng số năng lượng điểm không 1/2 hbar omega?
   ```
   *Kỳ vọng:* AI mổ xẻ nguyên lý đầu bằng hệ thức bất định Heisenberg, chuỗi nhân quả $\\le 65$ từ/khối, giải phẫu MALAE và đưa ra câu hỏi phản biện Silent Drop.
"""

with open(os.path.join(DIR_04, "HUONG_DAN_CAU_HINH_GEMINI_SPARK.md"), "w", encoding="utf-8") as f:
    f.write(guide_content)

print(f"[OK] Đã tạo hướng dẫn cấu hình chi tiết trong {DIR_04}")

# 5. Đóng gói toàn bộ thành GEMINI_SPARK_MASTER_BUNDLE.zip
master_zip_path = os.path.join(OUTPUT_DIR, "GEMINI_SPARK_MASTER_BUNDLE.zip")
with zipfile.ZipFile(master_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path == master_zip_path:
                continue
            arcname = os.path.relpath(file_path, OUTPUT_DIR)
            zipf.write(file_path, arcname)

print(f"[OK] Đã đóng gói thành công Master Bundle: {master_zip_path}")
print("--- HOÀN TẤT ĐÓNG GÓI CHO GEMINI SPARK ---")

---
name: physics-diagram-studio
description: Chuyên vẽ đồ thị giải tích MATLAB R2014b+, quản lý cơ sở dữ liệu vật liệu bán dẫn SEMICONDUCTORS_300K và kịch bản Python tự chứa trên Google Antigravity.
---
# Physics Diagram Studio (MATLAB Analytical Plotting Engine)

Kỹ năng chuyên sâu phục vụ trực quan hóa học thuật, đồ thị mô phỏng giải tích và giản đồ dải năng lượng bán dẫn theo chuẩn MATLAB R2014b+ trên môi trường Google Antigravity Native Engine (Local OS / PowerShell / Python 3.12).

*Hợp đồng Đầu vào / Đầu ra:* Nhận thông số mô phỏng và cơ chế vi mô từ `engineering-instructor`, áp dụng chuẩn danh pháp/Sentence case/SI từ `academic-terminology-guardian`; xuất tệp ảnh PNG $\ge 300\text{ DPI}$ trực tiếp qua **Python 3.12 Host CLI của Antigravity**, bàn giao cho `monograph-pdf-publisher` nhúng vào PDF.

---

## 1. Cơ Sở Dữ Liệu Vật Liệu Bán Dẫn 300 K & Hằng Số CODATA

### 1.1. Hằng số Vật lý Căn bản (CODATA)
- Điện tích nguyên tố: $q = 1,602176634 \times 10^{-19}\text{ C}$
- Hằng số Planck rút gọn: $\hbar = 1,054571817 \times 10^{-34}\text{ J}\cdot\text{s}$; $h = 6,62607015 \times 10^{-34}\text{ J}\cdot\text{s}$
- Khối lượng electron tự do: $m_0 = 9,1093837 \times 10^{-31}\text{ kg}$
- Hằng số Boltzmann: $k_B = 1,380649 \times 10^{-23}\text{ J/K}$ ($k_B T \approx 0,02585\text{ eV}$ ở $300\text{ K}$)
- Độ điện thẩm chân không: $\varepsilon_0 = 8,8541878128 \times 10^{-12}\text{ F/m}$; Vận tốc ánh sáng: $c = 2,99792458 \times 10^8\text{ m/s}$

### 1.2. Bảng Thông số Bán dẫn 300 K (`SEMICONDUCTORS_300K`)
| Vật liệu | $E_g\text{ [eV]}$ | $m_e^*/m_0$ | $m_{hh}^*/m_0$ | $\varepsilon_r$ | Varshni $\alpha\text{ [eV/K]}$ | Varshni $\beta\text{ [K]}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GaAs** | 1,424 | 0,067 | 0,45 | 12,9 | $5,405 \times 10^{-4}$ | 204,0 |
| **InP** | 1,344 | 0,077 | 0,60 | 12,5 | $4,900 \times 10^{-4}$ | 327,0 |
| **GaN** | 3,420 | 0,200 | 0,80 | 8,9 | $9,090 \times 10^{-4}$ | 830,0 |
| **Si** | 1,120 | 1,080 | 0,56 | 11,7 | $4,730 \times 10^{-4}$ | 636,0 |
| **Ge** | 0,660 | 0,550 | 0,37 | 16,0 | $4,770 \times 10^{-4}$ | 235,0 |

- **Hợp kim $\text{Al}_x\text{Ga}_{1-x}\text{As}$ ở 300 K:**
  * Vùng cấm trực tiếp ($x \le 0,45$): $E_g^\Gamma(x) = 1,424 + 1,247x\text{ [eV]}$
  * Vùng cấm gián tiếp ($x > 0,45$): $E_g^X(x) = 1,900 + 0,125x + 0,143x^2\text{ [eV]}$

---

## 2. Kiến Trúc Phân Tầng Thị Giác Đa Nhiệm (Hybrid Dual-Simulation)

100% hình ảnh đồ thị giải tích số trong bài giảng được tổ chức theo 2 cấp độ chuyên biệt theo Thuật toán 7:

1. **Mô phỏng Loại 1 — Mô hình Cấu trúc & Dải năng lượng (Structural Simulation):**
   - *Vị trí tích hợp:* Đặt tại Giai đoạn 1 hoặc Giai đoạn 2 (Mỏ neo thị giác & Hạt nhân vật lý).
   - *Mục tiêu:* Trực quan hóa cấu trúc vi mô định lượng: giải tích số dải năng lượng $E_c(z), E_v(z)$, phân bố thế năng lượng tử, phân bố hạt tải tự do, và phân bố mode quang học cơ bản $\text{TE}_{00}/\text{TM}_{00}$.
   - *Panel đối chuẩn:* Khi có ảnh gốc giáo trình, ưu tiên ghép panel đối chuẩn: `(a) Sơ đồ/ảnh gốc giáo trình [Goc] — (b) Đồ thị mô phỏng giải tích [Mo_Phong]`. Làm điểm tựa trực giác cho chuỗi 2–3 câu nhân quả vi mô.

2. **Mô phỏng Loại 2 — Đặc tuyến Hoạt động & Quét Đánh đổi (Performance & Trade-off Sweep):**
   - *Vị trí tích hợp:* Đặt tại Giai đoạn 4 (Phân tích biến thể & Khảo sát tiệm cận).
   - *Mục tiêu:* Thực chứng phòng thí nghiệm & đánh đổi thiết kế: khảo sát cực hạn tiệm cận ($T \to 0$ vs. $300\text{ K}$, $\omega \to 0$ vs. $\infty$), đặc tuyến hoạt động $I\text{–}V$, $L\text{–}I\text{–}V$ thực tế có điện trở vi phân $R_s$, dòng ngưỡng $I_{\text{th}}$, và quét mảng tham số công nghệ (nhiệt độ $T$, bề rộng giếng $L_z$).
   - *Thẻ Tham số Bóc tách (Detached Parameter Card):* Bắt buộc nhúng ngay dưới đồ thị Loại 2 theo dạng inline badge:  
     `↳ [Vật liệu]: ... | [Thông số quét]: ... | [Hệ quả Lab & Sai số]: R² = ..., ...`.

---

## 3. Quy Chuẩn Đồ Họa MATLAB R2014b+ & Triple Buffer Envelope

- **Hình học chuẩn khi vẽ:** `figsize=(6.5, 4.2)` inches, xuất ảnh `dpi=300`, `bbox_inches='tight'`.
- **Bảng màu 6 đường chuẩn MATLAB Hex:**
  * Đường chính (Line 1): `#0072BD` (Xanh lam đậm) — `linewidth=2.0`
  * Đường đối chiếu 1 (Line 2): `#D95319` (Cam đỏ) — `linewidth=2.0`
  * Đường đối chiếu 2 (Line 3): `#EDB120` (Vàng nghệ) — `linewidth=2.0`
  * Đường đối chiếu 3 (Line 4): `#7E2F8E` (Tím) — `linewidth=2.0`
  * Đường tiệm cận / Mức chuẩn: `#77AC30` (Xanh lục) hoặc `#7F7F7F` (Xám) — `linewidth=1.2, linestyle='--'`
- **Spines & Ticks:** 4 cạnh khung bao `#1F1F1F` đóng hộp, vạch chia (ticks) hướng vào trong (`direction='in'`) ở cả 4 cạnh. Lưới tọa độ: `linestyle='--'`, `linewidth=0.6`, `color='#E0E0E0'`.
- **Typography font serif:** Tiêu đề 12,5–13,0 pt in đậm; Nhãn trục 11,5–12,0 pt (`Tên đại lượng $Ký hiệu$ [Đơn vị SI]`); Ticks 9,5–10,0 pt; Legend & Callout 10,0–10,5 pt (nền trắng ngà `#F8F9FA`, viền `#CED4DA`).
- **Thuật toán Chống Đè Chữ & Bộ Ba Vùng Giới Hạn Vô Hình (Triple Buffer Envelope):**
  * $\delta_{\text{geom}} \ge 8\%$: Khoảng cách từ mép hộp chú thích đến **TẤT CẢ các đường nét vẽ trên đồ thị** tối thiểu 8% biên độ trục. Phạm vi bảo vệ áp dụng bình đẳng cho: đường dữ liệu thực tế, **đường nét đứt tiệm cận (Asymptotic Lines)**, đường bao hình (Envelopes), đường đối chiếu lý thuyết, và các vạch ranh giới (`axvline`, `axhline`). **Tuyệt đối cấm hộp chú thích cắt qua, đè lên hoặc che khuất bất kỳ phần nào của đường nét đứt tiệm cận hay đường cong vật lý.**
  * $\delta_{\text{box}} \ge 6\text{ pt}$: Khoảng cách cách ly giữa các hộp chú thích (Callouts) với nhau và giữa hộp chú thích với hộp Legend tối thiểu 6 pt (~0,02–0,03 normalized), tuyệt đối không chạm đè hoặc giao cắt.
  * $\delta_{\text{spine}} \ge 5\%$: Khoảng cách từ hộp chữ đến 4 đường viền bao trục tối thiểu 5% để không bao giờ bị cắt mép hoặc chạm vào khung trục.
  * **Kỷ luật Độ rộng Hộp Chú Thích (Callout Line Wrapping):** Tại các vùng có đường cong dốc hoặc đường tiệm cận đi xiên, độ dài mỗi dòng chữ trong Callout tối đa 20–25 ký tự, ngắt dòng 2–3 nhịp súc tích (ví dụ: `Vùng $r \le R$:\n$E(r) \propto r$`) để giữ bề rộng hộp nhỏ gọn, triệt tiêu nguy cơ mép phải hộp phình rộng đè vào đường nét đứt tiệm cận.
  * **Chiến lược Hành lang Trống (Corridor Strategy):** Tận dụng tối đa các khoảng thở tự nhiên (như hành lang giữa đường tiệm cận suy giảm $1/r, 1/r^2$ và Legend phía trên) để bố trí Callout, kết hợp khóa mỏ neo `ha='left', va='bottom'`.
  * **Quy tắc Nới Trục Tự Động:** Nếu không đủ khoảng trống trên hình, kịch bản tự động nới rộng biên độ trục y thêm 20–35% (`y_span = y_max - y_min; ax.set_ylim(y_min, y_max + 0.30 * y_span)`) để tạo vùng đệm an toàn cho Callout và Legend; **tuyệt đối không thu nhỏ cỡ chữ (giữ cố định $\ge 10.0\text{ pt}$)**.
  * **Quy Chuẩn Phân Số Trên Hình Vẽ (Luật 14):** 100% công thức toán trong Callout, Legend, title, xlabel, ylabel bắt buộc hiển thị dạng phân số gạch ngang chuẩn LaTeX $\frac{a}{b}$ (`\frac{a}{b}`), triệt tiêu hoàn toàn dấu gạch chéo `/`.
  * **Quy trình Tiền kiểm Bắt buộc (Mandatory Pre-Flight Geometry Assertion):** 100% kịch bản kết xuất đồ thị bắt buộc phải chạy hàm kiểm định hình học định lượng `assert_triple_buffer_geometry(fig, ax)` từ `matlab_plot_engine.py` (kiểm tra toàn diện cỡ chữ $\ge 10.0\text{ pt}$, 3 vùng đệm Triple Buffer, và quét cạn Luật 14 Zero-Slash-Fractions). Nghiêm cấm lưu tệp ảnh `.png` hoặc bàn giao chuyên khảo khi chưa đạt `PASS 100%`.

---

## 4. Khung Mã Python Tự Chứa Cho Gemini Spark (Self-Contained Lean Script)

Khi Gemini Spark cần vẽ đồ thị mô phỏng hoặc giản đồ dải năng lượng trong Code Execution sandbox, **sử dụng trực tiếp khung mã tự chứa dưới đây** mà không cần import thư viện ngoài:

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageChops

# 1. HÀM TỰ CẮT VIỀN TRẮNG SLIDE BÀI GIẢNG (AUTO-CROP)
def auto_crop_slide_image(input_path: str, output_path: str, pad: int = 10):
    """Tự động xén sạch viền trắng thừa từ ảnh chụp slide với phần đệm an toàn pad=10 px."""
    try:
        im = Image.open(input_path)
        bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
        diff = ImageChops.difference(im, bg)
        bbox = diff.getbbox()
        if bbox:
            w, h = im.size
            crop_box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
            im.crop(crop_box).save(output_path)
            return output_path
    except Exception as e:
        print(f"Bỏ qua crop: {e}")
    return input_path

# 2. KHỞI TẠO CANVAS & CẤU HÌNH KHUNG VIỀN CHUẨN MATLAB R2014b+ (Spines & Inward Ticks)
fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)

for spine in ax.spines.values():
    spine.set_color('#1F1F1F')
    spine.set_linewidth(1.0)
ax.tick_params(direction='in', length=4.0, width=0.8, top=True, right=True, labelsize=10.0)
ax.grid(True, linestyle='--', linewidth=0.6, color='#E0E0E0', alpha=0.7)

# 3. TÍNH TOÁN DỮ LIỆU VẬT LÝ (Ví dụ: Phổ phát quang tự phát của GaAs ở 300 K)
E = np.linspace(1.38, 1.55, 300)  # Năng lượng photon [eV]
Eg = 1.424                        # Vùng cấm GaAs ở 300 K
kT = 0.02585                      # [eV]
I_sp = np.where(E >= Eg, np.sqrt(np.maximum(0, E - Eg)) * np.exp(-(E - Eg) / kT), 0)
I_sp = I_sp / np.max(I_sp)

# 4. VẼ ĐƯỜNG CONG DỮ LIỆU BẰNG BẢNG MÀU CHUẨN MATLAB
ax.plot(E, I_sp, color='#0072BD', linewidth=2.0, label='Phổ phát xạ tự phát (300 K)')
ax.axvline(x=Eg, color='#77AC30', linestyle='--', linewidth=1.2, label=r'$E_g = 1{,}424\ \mathrm{eV}$')

# 5. THUẬT TOÁN CHỐNG ĐÈ CHỮ: NỚI TRỤC Y TỰ ĐỘNG (Tạo khoảng đệm an toàn >= 20% span)
y_min, y_max = np.min(I_sp), np.max(I_sp)
y_span = y_max - y_min
ax.set_ylim(y_min - 0.05 * y_span, y_max + 0.20 * y_span)

# 6. ĐẶT LEGEND VÀ CALLOUT AN TOÀN (Khóa cứng font >= 10.0 pt, không đè lên đường cong)
ax.legend(loc='upper right', fontsize=10.0, framealpha=0.92, facecolor='#F8F9FA', edgecolor='#CED4DA')

peak_idx = np.argmax(I_sp)
ax.annotate(
    "Đỉnh phổ phát xạ\n" r"$h\nu_{\mathrm{peak}} \approx E_g + \frac{1}{2}k_B T$",
    xy=(E[peak_idx], I_sp[peak_idx]),
    xytext=(0.58, 0.72),
    textcoords="axes fraction",
    fontsize=10.0,
    fontname="DejaVu Serif",
    arrowprops=dict(arrowstyle="->", lw=1.0, color="#1F1F1F", shrinkB=3),
    bbox=dict(boxstyle="square,pad=0.35", facecolor="#F8F9FA", edgecolor="#CED4DA", lw=0.8)
)

# 7. ĐỊNH DẠNG NHÃN TRỤC CHUẨN SENTENCE CASE & SI (CẤM PHÂN SỐ GẠCH CHÉO '/')
ax.set_title('Phổ phát quang tự phát của GaAs ở 300 K', fontsize=12.5, fontname='DejaVu Serif', fontweight='bold', pad=10)
ax.set_xlabel(r'Năng lượng photon $h\nu$ [eV]', fontsize=11.5, fontname='DejaVu Serif')
ax.set_ylabel(r'Cường độ phát xạ chuẩn hóa [a.u.]', fontsize=11.5, fontname='DejaVu Serif')

# Xuất ảnh độ phân giải cao
plt.savefig('Mo_Phong_Pho_Phat_Quang_GaAs.png', dpi=300, bbox_inches='tight', facecolor='white')
```

---

## 5. Quy Chuẩn Thuật Toán Bóc Tách Ảnh Gốc RVAE 2.0 & Đồ Họa Phân Tầng HDSE

### 5.1. Thuật Toán Bóc Tách & Chuẩn Hóa Hình Ảnh Gốc (RVAE Engine 2.0 — Thuật Toán 3)
Quản trị việc trích xuất ảnh slide bài giảng theo 4 phân hệ cốt lõi:
1. **Luồng 2A (Bottom-Up Vector & DOM):** Sử dụng PyMuPDF truy xuất trực tiếp luồng lệnh vẽ `page.get_drawings()` và đối tượng `image` để bóc tách các sơ đồ nguyên khối (monolithic diagrams) và công thức vector mà không làm suy giảm chất lượng điểm ảnh.
2. **Luồng 2B (Top-Down Visual DLA):** Chạy mô hình phân tích bố cục tài liệu (Document Layout Analysis - DocLayout-YOLO / RT-DETR) ở 2 mức phân giải: $150\text{ DPI}$ để định vị ranh giới toàn trang và $300\text{ DPI}$ để xác định chính xác bounding boxes của hình vẽ, đồ thị, sơ đồ dải năng lượng.
3. **Phân hệ Định vị Hợp nhất D-SAFE (Deterministic Spatial & Anchor Fusion Engine):** Hợp nhất kết quả từ Luồng 2A và Luồng 2B bằng thuật toán Non-Maximum Suppression (NMS) có trọng số không gian, ngưỡng Spatial IoU $\ge 0.65$. Khớp nối tiêu đề hình qua đối sánh khoảng cách Manhattan $\Delta y \le 25\text{ pt}$.
4. **Phân hệ Cắt & Tối ưu Hóa MPDS & AODE:**
   - `MPDS` (Multi-Pass Deduction & Slicing): Cắt ảnh tự động với khoảng đệm an toàn padding $8\text{–}12\text{ px}$.
   - `AODE` (Asset Optimization & Delivery Engine): Kiểm soát dung lượng PNG $\le 300\text{ KB}$, độ phân giải $\ge 300\text{ DPI}$, đặt tên chuẩn hóa `[Goc]_*.png`, lưu trữ trực tiếp vào `Kho_Hinh_Anh/` trên Google Drive `G:\`.

### 5.2. Thuật Toán Bố Cục Đồ Họa Phân Tầng & Triple Buffer Envelope (HDSE Engine — Thuật Toán 7)
1. **Phân Tầng Thị Giác Kép (Hybrid Dual-Simulation):**
   - *Mô phỏng Loại 1 (Structural Simulation — [Mo_Phong]_...png):* Giản đồ cấu trúc vi mô, phân bố mode quang học TE/TM, dải năng lượng lượng tử ($E\text{–}z$, $E\text{–}k$), phân bố trường điện từ.
   - *Mô phỏng Loại 2 (Performance & Trade-off Sweep — [Mo_Phong]_...png):* Đường cong đặc tuyến hoạt động ($I\text{–}V$, $L\text{–}I\text{–}V$ có $R_s, I_{\text{th}}$), quét tham số công nghệ (nhiệt độ $T$, bề rộng giếng $L_z$) và khảo sát tiệm cận cực hạn.
2. **3 Vùng Đệm Bất Khả Xâm Phạm (Triple Buffer Envelope):**
   - $\delta_{\text{geom}} \ge 8\%$: Khoảng cách Euclidean chuẩn hóa tới 100% các đường cong và tiệm cận nét đứt trong axes.
   - $\delta_{\text{spine}} \ge 5\%$: Khoảng đệm an toàn tới 4 cạnh khung `#1F1F1F`.
   - $\delta_{\text{box}} \ge 6\text{ pt}$: Khoảng đệm giữa các hộp chữ Callout và Legend.
   - Cỡ chữ nhãn và Callout $\ge 10.0\text{ pt}$. Tự động nới trục y $20\text{–}35\%$ khi thiếu không gian, nghiêm cấm co nhỏ cỡ chữ.
   - Bắt buộc chạy `assert_triple_buffer_geometry(fig, ax)` đạt chuẩn PASS trước khi lưu ảnh.

### 5.3. Thuật Toán Khóa Cứng Hình Học Đồ Thị & Bố Trí Nhãn Tối Ưu (ZT-GVLE Engine — Thuật Toán 13)
Giải pháp triệt để ngăn chặn méo mó tỷ lệ, đè chữ và sai lệch hình học khi nhúng vào ReportLab:
1. **A4 Canvas Width Lock ( \le 7.0\text{ in}$):** Khóa cứng chiều rộng canvas đồ thị tối đa 7.0 inches để tương thích hoàn hảo với khổ A4 (8.27 in) trừ đi 2 lề ReportLab (40 pt mỗi bên = 1.11 in, vùng in 515.27 pt = 7.16 in). Tuyệt đối nghiêm cấm mở rộng canvas theo phương ngang kiểu igsize=(12, 5) khi cần vẽ 2 đồ thị; bắt buộc chuyển sang bố cục xếp chồng dọc 1 cột (1-column vertical stacking, ví dụ igsize=(6.5, 8.0)) hoặc phân tách thành 2 tệp ảnh độc lập igsize=(6.5, 4.2).
2. **Dense Raster Pixel Obstacle Cloud:** Trích xuất ma trận điểm ảnh vật cản với bước nhảy $\Delta s \le 2.5\text{ px}$ từ toàn bộ đường cong dữ liệu, vạch ngưỡng và đường tiệm cận nét đứt, biến chúng thành tập hợp chướng ngại vật định lượng.
3. **Continuous Elliptical Equi-Clearance Label Placement:** Tối ưu hóa vị trí nhãn và hộp Callout bằng hàm khoảng cách elip đẳng cự, bảo đảm khoảng đệm an toàn tới mọi điểm ảnh vật cản, loại bỏ hoàn toàn hiện tượng nhãn đè lên đường cong hoặc che khuất đường tiệm cận.
4. **Detached Parameter Card:** Thẻ tham số vật lý và thông số linh kiện được bóc tách thành một dải huy hiệu độc lập bên ngoài hoặc ngay dưới axes, không nhồi nhét vào bên trong đồ thị gây quá tải diện tích hiển thị.
5. **Cryptographic Sidecar Manifest (.manifest.json):** Mỗi tệp ảnh [Mo_Phong]_...png khi xuất xưởng bắt buộc đi kèm một tệp manifest JSON chứa mã băm SHA-256 của ảnh và các thông số hình học đã kiểm chứng (kích thước, font size $\ge 10\text{ pt}$, các khoảng đệm $\delta_{\text{geom}} \ge 8\%$, $\delta_{\text{spine}} \ge 5\%$, $\delta_{\text{box}} \ge 6\text{ pt}$, và kiểm toán Luật 14 Zero-Slash-Fractions). Phân hệ chế bản ReportLab sẽ xác thực manifest này trước khi nhúng ảnh vào PDF.
6. **Mã thực thi chuẩn:** Được triển khai và khóa cứng trong physics_viz_lock.py tại thư mục gốc.

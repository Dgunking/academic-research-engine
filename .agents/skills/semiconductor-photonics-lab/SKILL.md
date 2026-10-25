---
name: semiconductor-photonics-lab
description: Tra cứu cơ sở dữ liệu vật liệu bán dẫn 300 K (GaAs, InP, GaN, Si, Ge, AlGaAs), hằng số CODATA và thiết lập chuẩn đồ họa MATLAB R2014b+ cho Lab Quang điện tử HUST.
---
# Semiconductor & Photonics Lab Core (HUST Physics)

Kỹ năng chuyên trách quản lý cơ sở dữ liệu vật liệu bán dẫn 300 K, hằng số vật lý căn bản CODATA, và các module hỗ trợ trực quan hóa đồ họa giải tích MATLAB R2014b+ phục vụ nghiên cứu và chế bản tại Khoa Vật lý Kỹ thuật, ĐHBK Hà Nội.

*Hợp đồng Đầu vào / Đầu ra:* Cung cấp thông số vật liệu và hằng số chuẩn hóa cho `engineering-instructor` và `physics-diagram-studio`; hỗ trợ khởi tạo nhanh canvas chuẩn MATLAB R2014b+ với khung 4 cạnh và inward ticks.

---

## 1. Cơ Sở Dữ Liệu Vật Liệu Bán Dẫn 300 K & Hằng Số CODATA

Tệp script: `.agents/skills/semiconductor-photonics-lab/scripts/materials_db.py`

### 1.1. Hằng Số Vật Lý Căn Bản (CODATA 2018/2022)
- Điện tích nguyên tố: $q = 1{,}602176634 \times 10^{-19}\text{ C}$
- Hằng số Planck rút gọn: $\hbar = 1{,}054571817 \times 10^{-34}\text{ J}\cdot\text{s}$
- Hằng số Planck: $h = 6{,}62607015 \times 10^{-34}\text{ J}\cdot\text{s}$
- Khối lượng electron tự do: $m_0 = 9{,}1093837 \times 10^{-31}\text{ kg}$
- Hằng số Boltzmann: $k_B = 1{,}380649 \times 10^{-23}\text{ J/K}$ ($k_B T \approx 0{,}02585\text{ eV}$ ở $300\text{ K}$)
- Độ điện thẩm chân không: $\varepsilon_0 = 8{,}8541878128 \times 10^{-12}\text{ F/m}$
- Vận tốc ánh sáng: $c = 2{,}99792458 \times 10^8\text{ m/s}$

### 1.2. Bảng Thông Số Bán Dẫn Ở 300 K (`SEMICONDUCTORS_300K`)
- **GaAs:** $E_g = 1{,}424\text{ eV}$ (trực tiếp), $m_e^* = 0{,}067 m_0$, $m_{hh}^* = 0{,}45 m_0$, $\varepsilon_r = 12{,}9$, $n_r = 3{,}65$.
- **InP:** $E_g = 1{,}344\text{ eV}$ (trực tiếp), $m_e^* = 0{,}077 m_0$, $m_{hh}^* = 0{,}60 m_0$, $\varepsilon_r = 12{,}5$, $n_r = 3{,}17$.
- **GaN:** $E_g = 3{,}420\text{ eV}$ (trực tiếp), $m_e^* = 0{,}200 m_0$, $m_{hh}^* = 0{,}80 m_0$, $\varepsilon_r = 8{,}9$, $n_r = 2{,}40$.
- **Si:** $E_g = 1{,}120\text{ eV}$ (gián tiếp), $m_e^* = 1{,}080 m_0$, $m_{hh}^* = 0{,}56 m_0$, $\varepsilon_r = 11{,}7$, $n_r = 3{,}42$.
- **Ge:** $E_g = 0{,}660\text{ eV}$ (gián tiếp), $m_e^* = 0{,}550 m_0$, $m_{hh}^* = 0{,}37 m_0$, $\varepsilon_r = 16{,}0$, $n_r = 4{,}00$.
- **Hợp kim $\text{Al}_x\text{Ga}_{1-x}\text{As}$ (300 K):**
  - Vùng cấm trực tiếp ($x \le 0{,}45$): $E_g^\Gamma(x) = 1{,}424 + 1{,}247x\text{ [eV]}$
  - Vùng cấm gián tiếp ($x > 0{,}45$): $E_g^X(x) = 1{,}900 + 0{,}125x + 0{,}143x^2\text{ [eV]}$

---

## 2. Chuẩn Đồ Họa MATLAB R2014b+ Engine

Tệp script: `.agents/skills/semiconductor-photonics-lab/scripts/matlab_style.py`

### 2.1. Quy Chuẩn Khung Canvas & Bảng Màu
- Canvas: `figsize=(6.5, 4.2)`, `dpi=300`.
- 4 cạnh khung bao `#1F1F1F` đóng hộp, vạch chia hướng vào trong (*inward ticks*).
- 6 mã màu chuẩn MATLAB:
  - Line 1 (Chính): `#0072BD` (Xanh lam đậm)
  - Line 2 (Đối chiếu 1): `#D95319` (Cam đỏ)
  - Line 3 (Đối chiếu 2): `#EDB120` (Vàng nghệ)
  - Line 4 (Đối chiếu 3): `#7E2F8E` (Tím)
  - Đường tiệm cận: `#77AC30` (Xanh lục nét đứt) hoặc `#7F7F7F` (Xám)
- Triple Buffer Envelope: $\delta_{\text{geom}} \ge 8\%$, $\delta_{\text{box}} \ge 6\text{ pt}$, $\delta_{\text{spine}} \ge 5\%$.

### 2.2. Hướng Dẫn Sử Dụng Nhanh
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))

from materials_db import CODATA, SEMICONDUCTORS_300K, get_energy_gap
from matlab_style import setup_matlab_figure, add_callout, MATLAB_COLORS

fig, ax = setup_matlab_figure()
# Tiến hành tính toán và vẽ đặc tuyến
```

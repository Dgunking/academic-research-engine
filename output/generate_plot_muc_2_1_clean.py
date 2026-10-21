# -*- coding: utf-8 -*-
"""
Clean-Slate Simulation Plot Generator for Muc 2.1 Laser Diode
Compliant with MATLAB R2014b+ & Triple Buffer Envelope (HUST Standards)
Rule 14: Zero-Slash-Fractions in formulas via \\frac{a}{b}
Rule 13: Fonts >= 10.0 pt, 4 spines #1F1F1F, inward ticks, size <= 300 KB
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
from scipy.integrate import odeint

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image as PILImage

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\physics-diagram-studio\scripts")
import matlab_plot_engine as mpe

DRIVE_IMG_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý\Kho_Hinh_Anh"
TARGET_IMG = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Dong_Luc_Hoc_Bat_Tat_Xung_Laser_Diode_Relaxation_Oscillation.png")

# 1. THAM SỐ VẬT LÝ BÁN DẪN 300 K (InGaAsP/InP Laser Diode λ = 1.55 μm)
q = 1.602176634e-19   # C
c = 2.99792458e8      # m/s
n_g = 3.6             # Chiết suất nhóm
v_g = c / n_g         # Vận tốc nhóm ~ 8.33e7 m/s
d = 0.1e-6            # Bề dày vùng tích cực (m)
w = 2.0e-6            # Độ rộng sọc laser (m)
L = 300.0e-6          # Chiều dài hốc cộng hưởng (m)
V = d * w * L         # Thể tích vùng tích cực (m^3)
Gamma = 0.05          # Hệ số giam giữ quang học
tau_p = 2.0e-12       # Thời gian sống photon (2 ps)
a_diff = 2.5e-20      # Tiết diện độ lợi vi phân dg/dN (m^2)
N_tr = 1.0e24         # Mật độ hạt tải trong suốt (1.0e18 cm^-3 = 1.0e24 m^-3)

# Tổn hao và độ lợi ngưỡng
g_th = 1.0 / (Gamma * v_g * tau_p)  # m^-1
N_th = N_tr + g_th / a_diff          # Mật độ hạt tải ngưỡng (m^-3)

# Tái hợp phi tuyến R(N) = A*N + B*N^2 + C*N^3
A_srh = 1.0e8       # s^-1 (SRH)
B_rad = 1.0e-16     # m^3/s (Bức xạ tự phát)
C_aug = 3.0e-41     # m^6/s (Auger)
beta_sp = 1.0e-4    # Hệ số ghép bức xạ tự phát vào mode laser
eta_i = 0.85        # Hiệu suất lượng tử nội

def R_carrier(N):
    return A_srh * N + B_rad * (N**2) + C_aug * (N**3)

# Dòng ngưỡng lý thuyết I_th
I_th = (q * V / eta_i) * R_carrier(N_th)

# 2. GIẢI HỆ PHƯƠNG TRÌNH VI PHÂN TỐC ĐỘ (RATE EQUATIONS)
def rate_equations(y, t, I_bias):
    N, S = y
    g = a_diff * (N - N_tr) if N > N_tr else 0.0
    R_total = R_carrier(N)
    
    dN_dt = (eta_i * I_bias) / (q * V) - R_total - v_g * g * S
    dS_dt = Gamma * v_g * g * S - S / tau_p + Gamma * beta_sp * B_rad * (N**2)
    return [dN_dt, dS_dt]

# Thời gian mô phỏng xung bật: 0 đến 3.0 ns
t_span = np.linspace(0, 3.0e-9, 2000) # s
y0 = [0.0, 1.0e10] # Khởi đầu không hạt tải, photon nền nhiệt nhỏ
I_pulse = 2.0 * I_th # Dòng bơm gấp đôi dòng ngưỡng

sol = odeint(rate_equations, y0, t_span, args=(I_pulse,))
N_t = sol[:, 0]
S_t = sol[:, 1]

# Mật độ photon dừng trên ngưỡng S_0
S_steady = (Gamma * tau_p * (eta_i * (I_pulse - I_th) / (q * V)))
if S_steady <= 0:
    S_steady = 1.0e18

# Chuẩn hóa
t_ns = t_span * 1e9
N_norm = N_t / N_th
S_norm = S_t / S_steady

# 3. ĐẶC TUYẾN DỪNG THEO DÒNG TIÊM I / I_th
I_range = np.linspace(0.1 * I_th, 3.5 * I_th, 400)
N_ss = []
P_out_mw = []
h_nu = (6.62607015e-34 * 2.99792458e8) / 1.55e-6 # Năng lượng photon ~ 1.28e-19 J
eta_d = eta_i * 0.7 # Giả định hiệu suất vi phân ngoài ~ 0.60

for I_val in I_range:
    if I_val < I_th:
        N_val = N_th * np.sqrt(I_val / I_th)
        P_val = 0.01 * (I_val / I_th) # mW
    else:
        N_val = N_th
        P_val = eta_d * (h_nu / q) * (I_val - I_th) * 1e3 # mW
    N_ss.append(N_val / N_th)
    P_out_mw.append(P_val)

N_ss = np.array(N_ss)
P_out_mw = np.array(P_out_mw)

# 4. THIẾT LẬP ĐỒ THỊ MATLAB R2014b+ CHUẨN
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "axes.edgecolor": "#1F1F1F",
    "axes.linewidth": 1.0,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 4.8), dpi=300)
fig.patch.set_facecolor("#FFFFFF")

for ax in (ax1, ax2):
    ax.set_facecolor("#FFFFFF")
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("#1F1F1F")
        spine.set_linewidth(1.0)
    ax.tick_params(axis="both", which="both", direction="in", top=True, bottom=True, left=True, right=True,
                   length=4.5, width=0.8, labelsize=10.0, colors="#1F1F1F")
    ax.grid(True, linestyle="--", linewidth=0.5, color="#E0E0E0", alpha=0.7)

# --- PANEL (a): DAO ĐỘNG HỒI PHỤC DẬP DẦN ---
line_n = ax1.plot(t_ns, N_norm, color="#0072BD", lw=1.8, label=r"Mật độ hạt tải $\frac{N(t)}{N_{\mathrm{th}}}$")
line_s = ax1.plot(t_ns, S_norm, color="#D95319", lw=1.8, label=r"Mật độ photon $\frac{S(t)}{S_0}$")
line_eq = ax1.axhline(1.0, color="#77AC30", ls="--", lw=1.2, label=r"Mức cân bằng dừng ($1{,}0$)")

ax1.set_xlim(0.0, 3.0)
ax1.set_ylim(-0.1, 2.6)
ax1.set_xlabel(r"Thời gian $t$ [$\mathrm{ns}$]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
ax1.set_ylabel(r"Biên độ chuẩn hóa [Không thứ nguyên]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
ax1.set_title(r"(a) Dao động hồi phục dập dần ($I = 2 I_{\mathrm{th}}$)", fontsize=11.5, fontweight="bold", fontname="DejaVu Serif", color="#1F1F1F", pad=8)
ax1.legend(loc="upper right", bbox_to_anchor=(0.94, 0.94), fontsize=10.0, framealpha=0.95, edgecolor="#CED4DA")

ax1.annotate(r"$\bullet$ Đỉnh vượt lố photon" "\n"
             r"$\bullet$ Tần số $\omega_R \propto \sqrt{S_0}$" "\n"
             r"$\bullet$ Dập dần về dừng",
             xy=(0.65, 1.85), xytext=(1.6, 0.25),
             arrowprops=dict(arrowstyle="->", lw=0.9, color="#1F1F1F"),
             fontsize=10.0, fontname="DejaVu Serif",
             bbox=dict(boxstyle="square,pad=0.3", fc="#F8F9FA", ec="#CED4DA", lw=0.6))

# --- PANEL (b): ĐẶC TUYẾN DỪNG & KẸP HẠT TẢI ---
I_ratio = I_range / I_th
ax2_twin = ax2.twinx()
ax2_twin.tick_params(axis="y", which="both", direction="in", length=4.5, width=0.8, labelsize=10.0, colors="#D95319")

line1 = ax2.plot(I_ratio, N_ss, color="#0072BD", lw=1.8, label=r"Hạt tải dừng $\frac{N}{N_{\mathrm{th}}}$")
line2 = ax2_twin.plot(I_ratio, P_out_mw, color="#D95319", lw=1.8, label=r"Công suất phát $P_{\mathrm{out}}$")
line3 = ax2.axvline(1.0, color="#7E2F8E", ls=":", lw=1.3, label=r"Ngưỡng laser ($I = I_{\mathrm{th}}$)")

ax2.set_xlim(0.0, 3.5)
ax2.set_ylim(-0.1, 1.8)
ax2_twin.set_ylim(-2.0, 38.0)

ax2.set_xlabel(r"Tỷ số dòng tiêm $\frac{I}{I_{\mathrm{th}}}$ [Không thứ nguyên]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
ax2.set_ylabel(r"Mật độ hạt tải kẹp $\frac{N}{N_{\mathrm{th}}}$", fontsize=10.5, fontname="DejaVu Serif", color="#0072BD")
ax2_twin.set_ylabel(r"Công suất quang phát $P_{\mathrm{out}}$ [$\mathrm{mW}$]", fontsize=10.5, fontname="DejaVu Serif", color="#D95319")
ax2.set_title(r"(b) Kẹp hạt tải ngưỡng và đặc tuyến $P\text{–}I$", fontsize=11.5, fontweight="bold", fontname="DejaVu Serif", color="#1F1F1F", pad=8)

lines = line1 + line2 + [line3]
labels = [l.get_label() for l in lines]
ax2.legend(lines, labels, loc="upper left", bbox_to_anchor=(0.06, 0.94), fontsize=10.0, framealpha=0.95, edgecolor="#CED4DA")

ax2.annotate(r"Kẹp hạt tải:" "\n"
             r"$N = N_{\mathrm{th}}$" "\n"
             r"($I > I_{\mathrm{th}}$)",
             xy=(2.0, 1.0), xytext=(1.8, 0.3),
             arrowprops=dict(arrowstyle="->", lw=0.9, color="#1F1F1F"),
             fontsize=10.0, fontname="DejaVu Serif",
             bbox=dict(boxstyle="square,pad=0.3", fc="#F8F9FA", ec="#CED4DA", lw=0.6))

from matplotlib.backends.backend_agg import FigureCanvasAgg
FigureCanvasAgg(fig)
plt.tight_layout()

# Hard Gate Assertion: Triple Buffer Geometry on both panels
res_ax1 = mpe.assert_triple_buffer_geometry(fig, ax1)
res_ax2 = mpe.assert_triple_buffer_geometry(fig, ax2)
if res_ax1["status"] != "PASS" or res_ax2["status"] != "PASS":
    raise AssertionError(f"Triple Buffer Gate failed: ax1={res_ax1['status']}, ax2={res_ax2['status']}")

# LƯU VÀO FILE TẠM & THAY THẾ NGUYÊN TỬ
temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_muc_2_1.png")
fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
plt.close(fig)

with PILImage.open(temp_img) as im:
    im_quant = im.convert("RGB").quantize(colors=256, method=PILImage.Quantize.MEDIANCUT)
    im_quant.save(temp_img, format="PNG", dpi=(300, 300), optimize=True, compress_level=9)

import shutil
shutil.copyfile(temp_img, TARGET_IMG)
try:
    os.remove(temp_img)
except Exception:
    pass

size_kb = os.path.getsize(TARGET_IMG) / 1024.0
print(f"SUCCESS: Generated simulation plot at {TARGET_IMG}")
print(f"File size: {size_kb:.1f} KB (<= 300 KB Cap: {'PASS' if size_kb <= 300 else 'FAIL'})")

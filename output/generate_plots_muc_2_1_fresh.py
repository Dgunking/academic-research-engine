import os
import sys
sys.stdout.reconfigure(encoding="utf-8")
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from PIL import Image

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\physics-diagram-studio\scripts")
import matlab_plot_engine as mpe

drive_img_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý\Kho_Hinh_Anh"
os.makedirs(drive_img_dir, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. MÔ PHỎNG LOẠI 1 (STRUCTURAL SIMULATION):
# Giản đồ dải năng lượng Ec(z), Ev(z) và mode quang học TE00 của dị thể kép DH GaAs – Al0.3Ga0.7As
# ---------------------------------------------------------------------------
print("Generating Simulation Plot Type 1 (Structural)...")
fig1, ax1 = mpe.setup_matlab_axes(figsize=(6.8, 4.4), dpi=300)
FigureCanvasAgg(fig1)

z = np.linspace(-0.6, 0.6, 500)  # [um]
d_act = 0.2  # bề rộng vùng tích cực 200 nm

# Delta Ec = 0.6 * Delta Eg, Delta Ev = 0.4 * Delta Eg
# GaAs: Eg = 1.424 eV. Al0.3Ga0.7As: Eg = 1.424 + 1.247*0.3 = 1.798 eV
delta_Eg = 1.798 - 1.424
delta_Ec = 0.60 * delta_Eg  # 0.224 eV
delta_Ev = 0.40 * delta_Eg  # 0.150 eV

# Khung dải dẫn Ec và dải hóa trị Ev (eV)
Ec = np.where(np.abs(z) <= d_act / 2, 0.0, delta_Ec)
Ev = np.where(np.abs(z) <= d_act / 2, -1.424, -1.424 - delta_Ev)

# Phân bố cường độ trường quang mode cơ bản TE00
w_spot = 0.20  # spot size [um]
optical_mode = np.exp(-2 * (z / w_spot) ** 2)
optical_mode_scaled = -1.424 + delta_Ec + optical_mode * 0.45

# Vẽ dải dẫn và dải hóa trị
ax1.plot(z, Ec, color="#0072BD", lw=2.2, label=r"Dải dẫn $E_c(z)$")
ax1.plot(z, Ev, color="#D95319", lw=2.2, label=r"Dải hóa trị $E_v(z)$")

# Vẽ mode quang học TE00
ax1.plot(z, optical_mode_scaled, color="#7E2F8E", lw=2.0, ls="-.", label=r"Mode quang $\mathrm{TE}_{00}$")

# Ranh giới dị thể kép dạng đoạn thẳng
ax1.plot([-d_act / 2, -d_act / 2], [-1.65, 0.35], color="#77AC30", lw=1.2, ls="--")
ax1.plot([d_act / 2, d_act / 2], [-1.65, 0.35], color="#77AC30", lw=1.2, ls="--")

# Vùng tích cực tô màu nhẹ
ax1.axvspan(-d_act / 2, d_act / 2, color="#F0F7FF", alpha=0.6, label="Vùng tích cực (GaAs)")

# Giới hạn trục & nhãn
ax1.set_xlim(-0.55, 0.55)
ax1.set_ylim(-2.0, 1.8)

mpe.style_axes_labels(
    ax1,
    xlabel=r"Tọa độ không gian dọc trục phân lớp $z$ [$\mathrm{\mu m}$]",
    ylabel=r"Thế năng điện tử & dải năng lượng $E$ [$\mathrm{eV}$]",
    title=r"Cấu trúc dải năng lượng & giam giữ mode quang trong dị thể kép GaAs – AlGaAs",
)

# Thêm Callouts theo Corridor Strategy
ann0 = mpe.add_callout_annotation(
    ax1,
    text=r"Vách giam giữ" "\n" r"$\Delta E_c \approx 0{,}224\ \mathrm{eV}$",
    xy=(-d_act / 2, delta_Ec),
    xytext=(0.08, 0.82),
    fontsize=10.0,
)

ann1 = mpe.add_callout_annotation(
    ax1,
    text=r"Phát xạ photon" "\n" r"$h\nu \approx 1{,}424\ \mathrm{eV}$",
    xy=(0.0, -0.71),
    xytext=(0.42, 0.82),
    fontsize=10.0,
)

leg1 = mpe.add_matlab_legend(ax1, loc="upper right", bbox_to_anchor=(0.94, 0.94), fontsize=10.0)

# Tối ưu hóa Triple Buffer Occupancy Grid
mpe.optimize_annotations_triple_buffer(
    fig1,
    ax1,
    lines_data=[(z, Ec), (z, Ev), (z, optical_mode_scaled)],
)

# Pre-flight Geometry check
mpe.assert_triple_buffer_geometry(
    fig1,
    ax1,
    lines_data=[(z, Ec), (z, Ev), (z, optical_mode_scaled)],
)

plot1_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.1_Cau_Truc_Dai_Nang_Luong_Va_Mode_Quang_DH.png")
fig1.savefig(plot1_path, dpi=300, bbox_inches="tight")
plt.close(fig1)

im1 = Image.open(plot1_path)
im1.save(plot1_path, format="PNG", dpi=(300, 300), optimize=True, compress_level=9)
print(f"Plot 1 saved successfully: {plot1_path} ({os.path.getsize(plot1_path)/1024:.1f} KB)")


# ---------------------------------------------------------------------------
# 2. MÔ PHỎNG LOẠI 2 (PERFORMANCE & TRADE-OFF SWEEP):
# Động lực học các kênh tái hợp vi mô (SRH AN, Bức xạ BN^2, Auger CN^3) & Hiệu suất lượng tử nội
# ---------------------------------------------------------------------------
print("Generating Simulation Plot Type 2 (Performance & Trade-off)...")
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.serif": ["DejaVu Serif"],
        "mathtext.fontset": "dejavuserif",
        "axes.edgecolor": "#1F1F1F",
        "axes.linewidth": 1.0,
    }
)
fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(12.0, 4.4), dpi=300)
FigureCanvasAgg(fig2)

for ax in (ax2a, ax2b):
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("#1F1F1F")
        spine.set_linewidth(1.0)
    ax.tick_params(
        axis="both", which="both", direction="in", top=True, bottom=True, left=True, right=True,
        length=4.5, width=0.8, labelsize=10.0, colors="#1F1F1F"
    )
    ax.grid(True, linestyle="--", linewidth=0.6, color="#E0E0E0", alpha=0.7)

# Tham số vật liệu GaAs ở 300 K
A = 1.0e8       # s^-1 (SRH recombination)
B = 1.0e-10     # cm^3/s (Radiative recombination)
C = 3.0e-29     # cm^6/s (Auger recombination)

N = np.logspace(16, 19, 400)  # cm^-3
R_srh = A * N
R_rad = B * (N ** 2)
R_aug = C * (N ** 3)
R_tot = R_srh + R_rad + R_aug

eta_rad = R_rad / R_tot
N_opt = np.sqrt(A / C)  # mật độ đạt hiệu suất cực đại
eta_max = (B * N_opt) / (A + B * N_opt + C * (N_opt ** 2))

# Subplot 2a: Tốc độ các kênh tái hợp vi mô (Log-Log)
ax2a.loglog(N, R_srh, color="#7E2F8E", lw=1.8, ls="--", label=r"SRH $A N$ (phi bức xạ)")
ax2a.loglog(N, R_rad, color="#0072BD", lw=2.2, label=r"Bức xạ $B N^2$ (hữu ích)")
ax2a.loglog(N, R_aug, color="#D95319", lw=1.8, ls="-.", label=r"Auger $C N^3$ (tổn hao)")
ax2a.loglog(N, R_tot, color="#1F1F1F", lw=2.0, label=r"Tổng $R(N)$")

ax2a.set_xlim(1e16, 1e19)
ax2a.set_ylim(1e23, 1e31)

mpe.style_axes_labels(
    ax2a,
    xlabel=r"Mật độ hạt tải $N$ [$\mathrm{cm}^{-3}$]",
    ylabel=r"Tốc độ tái hợp $R$ [$\mathrm{cm}^{-3}\cdot\mathrm{s}^{-1}$]",
    title=r"(a) Động lực học các kênh tái hợp vi mô $A, B, C$",
)

mpe.add_matlab_legend(ax2a, loc="upper left", bbox_to_anchor=(0.06, 0.94), fontsize=10.0)

# Subplot 2b: Hiệu suất lượng tử nội eta_rad vs N (Semi-log X)
ax2b.semilogx(N, eta_rad, color="#0072BD", lw=2.4, label=r"Hiệu suất $\eta_{\mathrm{rad}}$")
ax2b.plot([N_opt, N_opt], [0.0, eta_max], color="#77AC30", lw=1.3, ls="--", label=r"Mật độ $N_{\mathrm{opt}}$")
ax2b.plot([1e16, N_opt], [eta_max, eta_max], color="#EDB120", lw=1.2, ls=":", label=r"Đỉnh $\eta_{\max}$")

ax2b.set_xlim(1e16, 1e19)
ax2b.set_ylim(0.0, 0.85)

mpe.style_axes_labels(
    ax2b,
    xlabel=r"Mật độ hạt tải $N$ [$\mathrm{cm}^{-3}$]",
    ylabel=r"Hiệu suất lượng tử bức xạ nội $\eta_{\mathrm{rad}}$",
    title=r"(b) Hiệu suất lượng tử nội & suy biến do Auger",
)

ann2b = mpe.add_callout_annotation(
    ax2b,
    text=r"Đỉnh cực đại" "\n" r"tại $N_{\mathrm{opt}}$",
    xy=(N_opt, eta_max),
    xytext=(0.42, 0.82),
    fontsize=10.0,
)

leg2b = mpe.add_matlab_legend(ax2b, loc="upper left", bbox_to_anchor=(0.06, 0.94), fontsize=10.0)

# Pre-flight assertions
mpe.assert_triple_buffer_geometry(
    fig2,
    ax2a,
    lines_data=[(N, R_tot), (N, R_srh), (N, R_rad), (N, R_aug)],
)

mpe.optimize_annotations_triple_buffer(
    fig2,
    ax2b,
    lines_data=[(N, eta_rad)],
)

mpe.assert_triple_buffer_geometry(
    fig2,
    ax2b,
    lines_data=[(N, eta_rad)],
)

plot2_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.1_Dong_Luc_Hoc_Tai_Hop_ABC_Va_Hieu_Suat_Buc_Xa.png")
fig2.savefig(plot2_path, dpi=300, bbox_inches="tight")
plt.close(fig2)

im2 = Image.open(plot2_path)
im2.save(plot2_path, format="PNG", dpi=(300, 300), optimize=True, compress_level=9)
print(f"Plot 2 saved successfully: {plot2_path} ({os.path.getsize(plot2_path)/1024:.1f} KB)")

print("ALL SIMULATION PLOTS GENERATED AND PASSED TRIPLE BUFFER ENVELOPE CHECKS 100%!")

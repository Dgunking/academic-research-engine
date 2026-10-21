# -*- coding: utf-8 -*-
"""
Clean-Slate Simulation Generator for Chapter 2 Laser Diode - Muc 2.1
Generates:
  1. [Mo_Phong]_Dong_Luc_Hoc_Tai_Hop_ABC_Va_Hieu_Suat_Buc_Xa_LED.png (MPT 2.1.1)
  2. [Mo_Phong]_Dong_Luc_Hoc_Bat_Tat_Xung_Laser_Diode_Relaxation_Oscillation.png (MPT 2.1.3)
Rules:
  - Strict compliance with MATLAB R2014b+ styling and Triple Buffer Envelope (Rule 13)
  - Zero-Slash-Fractions in math via \\frac{a}{b} (Rule 14)
  - Pre-flight assertion checks: assert_triple_buffer_geometry PASS 100% (Rule 15)
  - File size <= 300 KB each (Rule III.C.5)
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
from scipy.integrate import odeint

import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from PIL import Image as PILImage

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\physics-diagram-studio\scripts")
import matlab_plot_engine as mpe

DRIVE_IMG_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý\Kho_Hinh_Anh"
os.makedirs(DRIVE_IMG_DIR, exist_ok=True)

# Common styling
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "axes.edgecolor": "#1F1F1F",
    "axes.linewidth": 1.0,
})

def save_and_optimize(fig, target_path):
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_export.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("RGB").quantize(colors=256, method=PILImage.Quantize.MEDIANCUT)
        im_quant.save(temp_img, format="PNG", dpi=(300, 300), optimize=True, compress_level=9)
    
    import shutil
    shutil.copyfile(temp_img, target_path)
    try:
        os.remove(temp_img)
    except Exception:
        pass
    
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"SUCCESS: Exported {os.path.basename(target_path)} -> {size_kb:.1f} KB")
    if size_kb > 300.0:
        raise ValueError(f"Image {target_path} size {size_kb:.1f} KB exceeds 300 KB limit!")
    return size_kb

# =============================================================================
# FIGURE 1: TÁI HỢP ABC VÀ HIỆU SUẤT BỨC XẠ LED (MPT 2.1.1)
# =============================================================================
def generate_fig1_abc_recombination():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Dong_Luc_Hoc_Tai_Hop_ABC_Va_Hieu_Suat_Buc_Xa_LED.png")
    
    A = 1.0e8       # s^-1 (SRH)
    B = 1.0e-10     # cm^3/s (Bức xạ tự phát)
    C = 3.0e-29     # cm^6/s (Auger)
    
    N = np.logspace(16, 19, 400) # cm^-3
    R_srh = A * N
    R_rad = B * (N**2)
    R_aug = C * (N**3)
    R_tot = R_srh + R_rad + R_aug
    
    eta_rad = R_rad / R_tot
    N_opt = np.sqrt(A / C)
    eta_max = (B * N_opt) / (A + B * N_opt + C * (N_opt**2))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 4.8), dpi=300)
    FigureCanvasAgg(fig)
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
    
    # --- PANEL (a): TỐC ĐỘ TÁI HỢP VI MÔ ---
    ax1.loglog(N, R_srh, color="#7E2F8E", lw=1.6, ls="--", label=r"SRH $A N$")
    ax1.loglog(N, R_rad, color="#0072BD", lw=1.8, label=r"Bức xạ $B N^2$")
    ax1.loglog(N, R_aug, color="#D95319", lw=1.6, ls="-.", label=r"Auger $C N^3$")
    ax1.loglog(N, R_tot, color="#1F1F1F", lw=2.0, label=r"Tổng $R(N)$")
    
    ax1.set_xlim(1e16, 1e19)
    ax1.set_ylim(1e16, 1e33)
    ax1.set_xlabel(r"Mật độ hạt tải $N$ [$\mathrm{cm}^{-3}$]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
    ax1.set_ylabel(r"Tốc độ tái hợp $R$ [$\mathrm{cm}^{-3}\cdot\mathrm{s}^{-1}$]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
    ax1.set_title(r"(a) Các kênh tái hợp hạt tải vi mô ($A, B, C$)", fontsize=11.5, fontweight="bold", fontname="DejaVu Serif", color="#1F1F1F", pad=8)
    ax1.legend(loc="upper left", bbox_to_anchor=(0.06, 0.94), ncol=2, fontsize=10.0, framealpha=0.95, edgecolor="#CED4DA")
    
    ax1.annotate(r"$\bullet$ Miền SRH: $R \propto N$" "\n"
                 r"$\bullet$ Miền bức xạ: $R \propto N^2$" "\n"
                 r"$\bullet$ Miền Auger: $R \propto N^3$",
                 xy=(2e18, 3e27), xytext=(0.38, 0.08), textcoords="axes fraction",
                 arrowprops=dict(arrowstyle="->", lw=0.9, color="#1F1F1F"),
                 fontsize=10.0, fontname="DejaVu Serif",
                 bbox=dict(boxstyle="square,pad=0.3", fc="#F8F9FA", ec="#CED4DA", lw=0.6))
    
    # --- PANEL (b): HIỆU SUẤT LƯỢNG TỬ NỘI BỨC XẠ & DROOP ---
    ax2.semilogx(N, eta_rad * 100.0, color="#0072BD", lw=2.0, label=r"Hiệu suất $\eta_{\mathrm{rad}}(N)$")
    ax2.axvline(N_opt, color="#D95319", ls=":", lw=1.4, label=rf"Đỉnh $N = {N_opt*1e-18:.2f}\times 10^{{18}}\text{{ cm}}^{{-3}}$")
    ax2.plot([N_opt], [eta_max * 100.0], marker="o", color="#D95319", markersize=6)
    
    ax2.set_xlim(1e16, 1e19)
    ax2.set_ylim(-5.0, 95.0)
    ax2.set_xlabel(r"Mật độ hạt tải $N$ [$\mathrm{cm}^{-3}$]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
    ax2.set_ylabel(r"Hiệu suất lượng tử nội $\eta_{\mathrm{rad}}$ [$\%$]", fontsize=10.5, fontname="DejaVu Serif", color="#1F1F1F")
    ax2.set_title(r"(b) Hiệu suất phát xạ tự phát và suy hao Droop", fontsize=11.5, fontweight="bold", fontname="DejaVu Serif", color="#1F1F1F", pad=8)
    ax2.legend(loc="upper right", bbox_to_anchor=(0.95, 0.94), fontsize=10.0, framealpha=0.95, edgecolor="#CED4DA")
    
    ax2.annotate(r"Đỉnh cực đại:" "\n"
                 rf"$\eta_{{\mathrm{{rad, max}}}} \approx {eta_max*100.0:.1f}\%$" "\n"
                 r"Suy giảm do Auger",
                 xy=(N_opt, eta_max * 100.0), xytext=(0.08, 0.40), textcoords="axes fraction",
                 arrowprops=dict(arrowstyle="->", lw=0.9, color="#1F1F1F"),
                 fontsize=10.0, fontname="DejaVu Serif",
                 bbox=dict(boxstyle="square,pad=0.3", fc="#F8F9FA", ec="#CED4DA", lw=0.6))
    
    plt.tight_layout()
    
    # Assertions
    res1 = mpe.assert_triple_buffer_geometry(fig, ax1)
    res2 = mpe.assert_triple_buffer_geometry(fig, ax2)
    if res1["status"] != "PASS" or res2["status"] != "PASS":
        raise AssertionError(f"Fig1 Triple Buffer Gate failed: ax1={res1['status']}, ax2={res2['status']}")
        
    save_and_optimize(fig, target_path)

# =============================================================================
# FIGURE 2: DAO ĐỘNG HỒI PHỤC VÀ ĐẶC TUYẾN DỪNG P-I (MPT 2.1.3)
# =============================================================================
def generate_fig2_relaxation_and_steady_state():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Dong_Luc_Hoc_Bat_Tat_Xung_Laser_Diode_Relaxation_Oscillation.png")
    
    q = 1.602176634e-19
    c = 2.99792458e8
    n_g = 3.6
    v_g = c / n_g
    d = 0.1e-6
    w = 2.0e-6
    L = 300.0e-6
    V = d * w * L
    Gamma = 0.05
    tau_p = 2.0e-12
    a_diff = 2.5e-20
    N_tr = 1.0e24
    
    g_th = 1.0 / (Gamma * v_g * tau_p)
    N_th = N_tr + g_th / a_diff
    
    A_srh = 1.0e8
    B_rad = 1.0e-16
    C_aug = 3.0e-41
    beta_sp = 1.0e-4
    eta_i = 0.85
    
    def R_carrier(N):
        return A_srh * N + B_rad * (N**2) + C_aug * (N**3)
    
    I_th = (q * V / eta_i) * R_carrier(N_th)
    
    def rate_eqs(y, t, I_bias):
        N, S = y
        g = a_diff * (N - N_tr) if N > N_tr else 0.0
        dN = (eta_i * I_bias) / (q * V) - R_carrier(N) - v_g * g * S
        dS = Gamma * v_g * g * S - S / tau_p + Gamma * beta_sp * B_rad * (N**2)
        return [dN, dS]
    
    t_span = np.linspace(0, 3.0e-9, 2000)
    y0 = [0.0, 1.0e10]
    I_pulse = 2.0 * I_th
    sol = odeint(rate_eqs, y0, t_span, args=(I_pulse,))
    N_t = sol[:, 0]
    S_t = sol[:, 1]
    
    S_steady = (Gamma * tau_p * (eta_i * (I_pulse - I_th) / (q * V)))
    if S_steady <= 0:
        S_steady = 1.0e18
    
    t_ns = t_span * 1e9
    N_norm = N_t / N_th
    S_norm = S_t / S_steady
    
    # Đặc tuyến dừng
    I_range = np.linspace(0.1 * I_th, 3.5 * I_th, 400)
    N_ss = []
    P_out_mw = []
    h_nu = (6.62607015e-34 * 2.99792458e8) / 1.55e-6
    eta_d = eta_i * 0.70
    
    for I_val in I_range:
        if I_val < I_th:
            N_val = N_th * np.sqrt(I_val / I_th)
            P_val = 0.01 * (I_val / I_th)
        else:
            N_val = N_th
            P_val = eta_d * (h_nu / q) * (I_val - I_th) * 1e3
        N_ss.append(N_val / N_th)
        P_out_mw.append(P_val)
        
    N_ss = np.array(N_ss)
    P_out_mw = np.array(P_out_mw)
    I_ratio = I_range / I_th
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 4.8), dpi=300)
    FigureCanvasAgg(fig)
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
    ax1.plot(t_ns, N_norm, color="#0072BD", lw=1.8, label=r"Mật độ hạt tải $\frac{N(t)}{N_{\mathrm{th}}}$")
    ax1.plot(t_ns, S_norm, color="#D95319", lw=1.8, label=r"Mật độ photon $\frac{S(t)}{S_0}$")
    ax1.axhline(1.0, color="#77AC30", ls="--", lw=1.2, label=r"Mức cân bằng dừng ($1{,}0$)")
    
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
    
    plt.tight_layout()
    
    # Assertions
    res1 = mpe.assert_triple_buffer_geometry(fig, ax1)
    res2 = mpe.assert_triple_buffer_geometry(fig, ax2)
    if res1["status"] != "PASS" or res2["status"] != "PASS":
        raise AssertionError(f"Fig2 Triple Buffer Gate failed: ax1={res1['status']}, ax2={res2['status']}")
        
    save_and_optimize(fig, target_path)

if __name__ == "__main__":
    print("Generating Figure 1: ABC Recombination & LED Droop...")
    generate_fig1_abc_recombination()
    print("Generating Figure 2: Relaxation Oscillation & P-I Clamping...")
    generate_fig2_relaxation_and_steady_state()
    print("ALL SIMULATION PLOTS GENERATED SUCCESSFULLY.")

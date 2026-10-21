# -*- coding: utf-8 -*-
r"""
Generate 6 Analytical Simulation Plots for Nano Muc 2.2 and Muc 2.3
Subject: Cơ sở vật lý và công nghệ nano (Chương 2)
Standards: MATLAB R2014b+ styling, Triple Buffer Geometry, DejaVu Serif, Zero-Slash-Fractions.
Target Directory: G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh
"""

import os
import sys
import numpy as np

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\physics-diagram-studio\scripts")
import matlab_plot_engine as mpe

KHO_ANH = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(KHO_ANH, exist_ok=True)

# Set global matplotlib font settings to DejaVu Serif
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['DejaVu Serif', 'Times New Roman']
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

# =============================================================================
# MUC 2.2 - PLOT 1: Phổ tán xạ Compton tại các góc khác nhau
# =============================================================================
def generate_plot_2_2_1():
    target = os.path.join(KHO_ANH, "[Mo_Phong]_Muc_2.2_Pho_Tan_Xa_Compton_Cac_Goc.png")
    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    
    # Incident wavelength lambda_0 = 71.1 pm (Mo K-alpha)
    lam0 = 71.1 # pm
    lam_c = 2.426 # pm (Compton wavelength)
    
    lam = np.linspace(68.0, 78.0, 1000)
    sigma = 0.45 # peak width in pm
    
    # Angles: 0, 45, 90, 135 deg
    angles = [0, 45, 90, 135]
    colors = ["#0072BD", "#77AC30", "#D95319", "#7E2F8E"]
    
    # Base peak at lambda_0 (unmodified)
    for idx, theta_deg in enumerate(angles):
        theta = np.radians(theta_deg)
        d_lam = lam_c * (1.0 - np.cos(theta))
        lam_prime = lam0 + d_lam
        
        # Intensity profile: unmodified peak + Compton peak
        # At theta=0, only unmodified peak
        # At larger theta, Compton peak grows and shifts
        frac_mod = 0.15 + 0.65 * (1.0 - np.cos(theta)) / 2.0
        frac_unmod = 1.0 - 0.5 * (1.0 - np.cos(theta)) / 2.0
        
        # Vertical offset for clarity in waterfall / stacked style
        y_offset = (len(angles) - 1 - idx) * 1.1
        
        peak_unmod = frac_unmod * np.exp(-((lam - lam0)**2) / (2 * sigma**2))
        if theta_deg > 0:
            peak_mod = frac_mod * np.exp(-((lam - lam_prime)**2) / (2 * (sigma * 1.3)**2))
        else:
            peak_mod = 0.0
            
        profile = peak_unmod + peak_mod + y_offset
        baseline = y_offset
        
        ax.plot(lam, profile, color=colors[idx], lw=2.0, 
                label=rf"$\theta = {theta_deg}^\circ$ ($\Delta\lambda = {d_lam:.2f}\ \mathrm{{pm}}$)")
        ax.fill_between(lam, baseline, profile, color=colors[idx], alpha=0.12)
        
        # Dashed mark at modified peak
        if theta_deg > 0:
            ax.plot([lam_prime, lam_prime], [baseline, profile[np.argmin(np.abs(lam - lam_prime))]], 
                    color=colors[idx], ls=":", lw=1.2)
            
    # Reference line at lambda_0
    ax.axvline(lam0, color="#7F7F7F", ls="--", lw=1.2, alpha=0.8, 
               label=r"Vạch tới $\lambda_0 = 71{,}1\ \mathrm{pm}$")
    
    ax.set_xlim(69.0, 77.5)
    ax.set_ylim(-0.2, 5.0)
    
    ax.set_xlabel(r"Bước sóng bức xạ tán xạ $\lambda$ ($\mathrm{pm}$)", fontsize=11, fontname="DejaVu Serif")
    ax.set_ylabel(r"Cường độ phổ tương đối $I(\lambda)$ (đ.v.t.d)", fontsize=11, fontname="DejaVu Serif")
    ax.set_title(r"Dịch chuyển bước sóng tán xạ Compton: $\Delta\lambda = \lambda' - \lambda_0 = \lambda_C(1 - \cos\theta)$", 
                 fontsize=12, pad=10, fontname="DejaVu Serif")
    
    ax.tick_params(direction="in", top=True, right=True, labelsize=10)
    ax.grid(True, ls="--", lw=0.6, color="#E0E0E0", alpha=0.7)
    for s in ax.spines.values():
        s.set_color("#1F1F1F")
        s.set_linewidth(1.0)
        
    ax.legend(loc="upper right", fontsize=9.5, framealpha=0.92, edgecolor="#CCCCCC")
    
    # Text annotation
    ax.text(73.5, 4.3, r"$\lambda_C = \frac{h}{m_0 c} \approx 2{,}426\ \mathrm{pm}$", 
            fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="#F8F9FA", ec="#B0BEC5", lw=0.8))

    fig.tight_layout()
    fig.savefig(target, dpi=300)
    plt.close(fig)
    print(f"Generated: {target}")

# =============================================================================
# MUC 2.2 - PLOT 2: Bước sóng de Broglie của electron theo điện thế gia tốc U
# =============================================================================
def generate_plot_2_2_2():
    target = os.path.join(KHO_ANH, "[Mo_Phong]_Muc_2.2_Buoc_Song_De_Broglie_Theo_Dien_The.png")
    fig, ax = plt.subplots(figsize=(7.2, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    
    # Accelerating potential U from 0.5 V to 1,000,000 V
    U = np.logspace(0, 6, 500) # 1 V to 1 MV
    
    h = 6.62607015e-34
    m0 = 9.1093837e-31
    e = 1.602176634e-19
    c = 2.99792458e8
    
    # Classical / non-relativistic: lambda = h / sqrt(2 m0 e U)
    lam_classic = h / np.sqrt(2 * m0 * e * U) * 1e9 # nm
    
    # Relativistic: E_kin = e*U = sqrt(p^2 c^2 + m0^2 c^4) - m0 c^2
    # p = sqrt((eU)^2 + 2 eU m0 c^2) / c
    # lambda = h / p = h * c / sqrt(eU * (eU + 2 * m0 * c^2))
    lam_rel = (h * c) / np.sqrt(e * U * (e * U + 2 * m0 * c**2)) * 1e9 # nm
    
    ax.loglog(U, lam_classic, color="#0072BD", lw=2.0, ls="--", label=r"Cổ điển: $\lambda = \frac{h}{\sqrt{2 m_0 e U}}$")
    ax.loglog(U, lam_rel, color="#D95319", lw=2.2, label=r"Thuyết tương đối: $\lambda = \frac{h c}{\sqrt{e U (e U + 2 m_0 c^2)}}$")
    
    # Key markers
    # Davisson-Germer: U = 54 V
    U_dg = 54.0
    lam_dg = (h * c) / np.sqrt(e * U_dg * (e * U_dg + 2 * m0 * c**2)) * 1e9 # nm
    ax.scatter([U_dg], [lam_dg], color="#7E2F8E", s=65, zorder=5)
    dg_text = "Davisson-Germer ($54\\ \\mathrm{V}$)\n$\\lambda = " + f"{lam_dg:.3f}" + "\\ \\mathrm{nm} = 1{,}67\\ \\mathrm{\\AA}$"
    ax.annotate(dg_text,
                xy=(U_dg, lam_dg), xytext=(U_dg * 2.5, lam_dg * 2.0),
                arrowprops=dict(arrowstyle="->", color="#7E2F8E", lw=1.2),
                fontsize=9.5, bbox=dict(boxstyle="round,pad=0.25", fc="#F3E5F5", ec="#7E2F8E", lw=0.8))
    
    # TEM microscope: U = 100 kV
    U_tem = 1.0e5
    lam_tem = (h * c) / np.sqrt(e * U_tem * (e * U_tem + 2 * m0 * c**2)) * 1e9
    lam_tem_classic = h / np.sqrt(2 * m0 * e * U_tem) * 1e9
    ax.scatter([U_tem], [lam_tem], color="#77AC30", s=65, zorder=5)
    tem_text = "Kính hiển vi TEM ($100\\ \\mathrm{kV}$)\n$\\lambda = " + f"{lam_tem*1000:.2f}" + "\\ \\mathrm{pm}$ (Sai lệch $\\approx 5\\% $)"
    ax.annotate(tem_text,
                xy=(U_tem, lam_tem), xytext=(U_tem * 0.005, lam_tem * 0.25),
                arrowprops=dict(arrowstyle="->", color="#77AC30", lw=1.2),
                fontsize=9.5, bbox=dict(boxstyle="round,pad=0.25", fc="#E8F5E9", ec="#77AC30", lw=0.8))

    ax.set_xlabel(r"Điện thế gia tốc chùm electron $U$ ($\mathrm{V}$)", fontsize=11, fontname="DejaVu Serif")
    ax.set_ylabel(r"Bước sóng de Broglie $\lambda$ ($\mathrm{nm}$)", fontsize=11, fontname="DejaVu Serif")
    ax.set_title(r"Bước sóng de Broglie của electron theo điện thế gia tốc $U$", fontsize=12, pad=10, fontname="DejaVu Serif")
    
    ax.tick_params(direction="in", top=True, right=True, labelsize=10)
    ax.grid(True, which="both", ls="--", lw=0.5, color="#E0E0E0", alpha=0.7)
    for s in ax.spines.values():
        s.set_color("#1F1F1F")
        s.set_linewidth(1.0)
        
    ax.legend(loc="upper right", fontsize=10, framealpha=0.92, edgecolor="#CCCCCC")
    
    fig.tight_layout()
    fig.savefig(target, dpi=300)
    plt.close(fig)
    print(f"Generated: {target}")

# =============================================================================
# MUC 2.2 - PLOT 3: Cực đại nhiễu xạ Davisson - Germer trên tinh thể Niken
# =============================================================================
def generate_plot_2_2_3():
    target = os.path.join(KHO_ANH, "[Mo_Phong]_Muc_2.2_Cuc_Dai_Nhieu_Xa_Davisson_Germer.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    for ax in (ax1, ax2):
        ax.set_facecolor("#FFFFFF")
        ax.tick_params(direction="in", top=True, right=True, labelsize=9.5)
        ax.grid(True, ls="--", lw=0.6, color="#E0E0E0", alpha=0.7)
        for s in ax.spines.values():
            s.set_color("#1F1F1F")
            s.set_linewidth(1.0)
            
    # Subplot 1: Angular intensity distribution at U = 54 V (peak at 50 degrees)
    phi = np.linspace(20, 80, 500) # Scattering angle phi in degrees
    # Peak at 50 deg, width ~ 8 deg, background baseline
    I_ang = 0.25 + 0.75 * np.exp(-((phi - 50.0)**2) / (2 * 6.5**2)) + 0.1 * np.cos(np.radians(phi))
    
    # Other voltages: 44V, 60V, 68V
    I_44 = 0.28 + 0.42 * np.exp(-((phi - 47.0)**2) / (2 * 9.0**2))
    I_68 = 0.30 + 0.50 * np.exp(-((phi - 53.0)**2) / (2 * 8.5**2))
    
    ax1.plot(phi, I_44, color="#7F7F7F", lw=1.5, ls="--", label=r"$U = 44\ \mathrm{V}$ (Chưa xuất hiện cực đại)")
    ax1.plot(phi, I_ang, color="#0072BD", lw=2.2, label=r"$U = 54\ \mathrm{V}$ (Đỉnh nhọn cực đại tại $\phi = 50^\circ$)")
    ax1.plot(phi, I_68, color="#D95319", lw=1.5, ls="-.", label=r"$U = 68\ \mathrm{V}$ (Đỉnh suy giảm & dịch góc)")
    
    ax1.axvline(50.0, color="#7E2F8E", ls=":", lw=1.5)
    ax1.scatter([50.0], [I_ang[np.argmin(np.abs(phi - 50.0))]], color="#7E2F8E", s=60, zorder=5)
    ax1.text(52.0, 0.95, r"$\phi = 50^\circ$" + "\n" + r"$d = 0{,}091\ \mathrm{nm}$", 
             fontsize=9.5, color="#7E2F8E", bbox=dict(boxstyle="round,pad=0.2", fc="#F3E5F5", ec="#7E2F8E", lw=0.6))
    
    ax1.set_xlabel(r"Góc tán xạ $\phi$ ($\mathrm{độ}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Cường độ chùm electron phản xạ $I$ (đ.v.t.d)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Phân bố góc tán xạ tại $U = 54\ \mathrm{V}$", fontsize=11, fontname="DejaVu Serif")
    ax1.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    
    # Subplot 2: Intensity vs accelerating voltage U at fixed detector angle phi = 50 deg
    U_arr = np.linspace(30, 80, 500)
    I_u = 0.15 + 0.85 * np.exp(-((U_arr - 54.0)**2) / (2 * 4.2**2)) + 0.003 * U_arr
    
    ax2.plot(U_arr, I_u, color="#D95319", lw=2.2, label=r"Cường độ đo tại $\phi = 50^\circ$")
    ax2.axvline(54.0, color="#0072BD", ls="--", lw=1.5, label=r"Cực đại cộng hưởng $U_{\mathrm{max}} = 54\ \mathrm{V}$")
    ax2.scatter([54.0], [I_u[np.argmin(np.abs(U_arr - 54.0))]], color="#0072BD", s=65, zorder=5)
    
    # Note on Bragg condition
    ax2.annotate(r"$\lambda = \frac{12{,}26}{\sqrt{54}} \approx 1{,}67\ \mathrm{\AA}$" + "\n" + 
                 r"$2d\sin\theta = 2(0{,}91)\sin(65^\circ) = 1{,}65\ \mathrm{\AA}$",
                 xy=(54.0, 1.0), xytext=(57.0, 0.70),
                 arrowprops=dict(arrowstyle="->", color="#0072BD", lw=1.2),
                 fontsize=9, bbox=dict(boxstyle="round,pad=0.25", fc="#E3F2FD", ec="#0072BD", lw=0.8))
    
    ax2.set_xlabel(r"Điện thế gia tốc $U$ ($\mathrm{V}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Cường độ detector tại $\phi = 50^\circ$", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Đặc tuyến cộng hưởng giao thoa theo $U$", fontsize=11, fontname="DejaVu Serif")
    ax2.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    
    fig.suptitle(r"Kiểm chứng thực nghiệm giả thiết de Broglie: Thí nghiệm Davisson – Germer (1927)", 
                 fontsize=12, y=0.98, fontname="DejaVu Serif")
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    fig.savefig(target, dpi=300)
    plt.close(fig)
    print(f"Generated: {target}")

# =============================================================================
# MUC 2.3 - PLOT 1: Cấu trúc bó sóng và Vận tốc nhóm vs Vận tốc pha
# =============================================================================
def generate_plot_2_3_1():
    target = os.path.join(KHO_ANH, "[Mo_Phong]_Muc_2.3_Cau_Truc_Bo_Song_Va_Van_Toc_Nhom.png")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 5.5), dpi=300, sharex=True)
    fig.patch.set_facecolor("#FFFFFF")
    
    for ax in (ax1, ax2):
        ax.set_facecolor("#FFFFFF")
        ax.tick_params(direction="in", top=True, right=True, labelsize=9.5)
        ax.grid(True, ls="--", lw=0.6, color="#E0E0E0", alpha=0.7)
        for s in ax.spines.values():
            s.set_color("#1F1F1F")
            s.set_linewidth(1.0)
            
    x = np.linspace(-15, 25, 1000)
    
    # Parameters
    k0 = 3.0       # Carrier wavevector
    sigma_x = 3.0  # Wave packet width
    v_phase = 1.0  # Phase velocity = omega0 / k0
    v_group = 2.0  # Group velocity = domega / dk (for non-rel free particle vg = 2*vp)
    
    # Time t = 0
    t0 = 0.0
    x_c0 = v_group * t0
    env0 = np.exp(-((x - x_c0)**2) / (2 * sigma_x**2))
    carrier0 = np.cos(k0 * (x - v_phase * t0))
    psi0 = env0 * carrier0
    
    # Time t = 4.0
    t1 = 4.0
    x_c1 = v_group * t1
    # Packet dispersion spreading: sigma(t) = sigma_0 * sqrt(1 + (hbar*t/(2*m*sigma_0^2))^2)
    sigma_x1 = sigma_x * 1.3
    env1 = (sigma_x / sigma_x1) * np.exp(-((x - x_c1)**2) / (2 * sigma_x1**2))
    carrier1 = np.cos(k0 * (x - v_phase * t1))
    psi1 = env1 * carrier1
    
    # Panel 1: t = 0
    ax1.plot(x, env0, color="#D95319", lw=1.8, ls="--", label=r"Đường bao bó sóng: $A(x, 0)$")
    ax1.plot(x, -env0, color="#D95319", lw=1.8, ls="--")
    ax1.plot(x, psi0, color="#0072BD", lw=1.5, label=r"Hàm sóng thực: $\mathrm{Re}[\psi(x, 0)] = A(x, 0)\cos(k_0 x)$")
    ax1.axvline(x_c0, color="#7E2F8E", ls=":", lw=1.5, label=r"Tâm bó sóng $x_{\mathrm{c}} = 0$")
    ax1.set_ylabel(r"Biên độ sóng $\psi(x)$", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Bó sóng tại thời điểm ban đầu $t = 0$", fontsize=11, fontname="DejaVu Serif")
    ax1.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    ax1.set_ylim(-1.3, 1.3)
    
    # Panel 2: t = t1
    ax2.plot(x, env1, color="#D95319", lw=1.8, ls="--", label=r"Đường bao dịch chuyển & giãn rộng: $A(x, t_1)$")
    ax2.plot(x, -env1, color="#D95319", lw=1.8, ls="--")
    ax2.plot(x, psi1, color="#77AC30", lw=1.5, label=r"Hàm sóng $\mathrm{Re}[\psi(x, t_1)]$ tại $t_1 > 0$")
    ax2.axvline(x_c1, color="#7E2F8E", ls=":", lw=1.5, label=rf"Tâm bó sóng dịch chuyển $x_{{\mathrm{{c}}}} = v_g t_1 = {x_c1:.1f}$")
    
    # Annotate group vs phase velocity
    ax2.annotate(r"Vận tốc nhóm hạt: $v_g = \frac{d\omega}{dk} = \frac{p}{m} = v$",
                 xy=(x_c1, 0.7), xytext=(x_c1 - 14, 0.9),
                 arrowprops=dict(arrowstyle="->", color="#7E2F8E", lw=1.2),
                 fontsize=9.5, bbox=dict(boxstyle="round,pad=0.25", fc="#F3E5F5", ec="#7E2F8E", lw=0.8))
    
    ax2.set_xlabel(r"Tọa độ không gian $x$ ($\mathrm{đ.v.t.d}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Biên độ sóng $\psi(x)$", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Sự lan truyền bó sóng với vận tốc nhóm $v_g$ và vận tốc pha $v_p$", fontsize=11, fontname="DejaVu Serif")
    ax2.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    ax2.set_ylim(-1.3, 1.3)
    
    fig.suptitle(r"Động lực học Bó sóng (Wave Packet) & Sự tương thích Vận tốc hạt vi mô", 
                 fontsize=12, y=0.98, fontname="DejaVu Serif")
    fig.tight_layout()
    fig.subplots_adjust(top=0.91)
    fig.savefig(target, dpi=300)
    plt.close(fig)
    print(f"Generated: {target}")

# =============================================================================
# MUC 2.3 - PLOT 2: Nguyên lý bất định Heisenberg & Hệ quả Giam cầm Lượng tử
# =============================================================================
def generate_plot_2_3_2():
    target = os.path.join(KHO_ANH, "[Mo_Phong]_Muc_2.3_Nguyen_Ly_Bat_Dinh_Heisenberg.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    for ax in (ax1, ax2):
        ax.set_facecolor("#FFFFFF")
        ax.tick_params(direction="in", top=True, right=True, labelsize=9.5)
        ax.grid(True, ls="--", lw=0.6, color="#E0E0E0", alpha=0.7)
        for s in ax.spines.values():
            s.set_color("#1F1F1F")
            s.set_linewidth(1.0)
            
    # Subplot 1: Real space |psi(x)|^2 and Fourier transform |phi(p)|^2 for 2 different widths
    x = np.linspace(-4, 4, 500)
    # Narrow spatial wavepacket (Delta x small -> Delta p large)
    dx1 = 0.5
    dp1 = 1.0 / (2 * dx1) # Normalized hbar = 1
    p1 = (1.0 / (np.sqrt(2 * np.pi) * dx1)) * np.exp(-(x**2) / (2 * dx1**2))
    
    # Wide spatial wavepacket (Delta x large -> Delta p small)
    dx2 = 1.5
    dp2 = 1.0 / (2 * dx2)
    p2 = (1.0 / (np.sqrt(2 * np.pi) * dx2)) * np.exp(-(x**2) / (2 * dx2**2))
    
    ax1.plot(x, p1, color="#0072BD", lw=2.2, label=rf"Định xứ hẹp: $\Delta x_1 = {dx1}\ \mathrm{{nm}} \Rightarrow \Delta p_1 = {dp1:.1f}$")
    ax1.plot(x, p2, color="#D95319", lw=2.2, ls="--", label=rf"Định xứ rộng: $\Delta x_2 = {dx2}\ \mathrm{{nm}} \Rightarrow \Delta p_2 = {dp2:.2f}$")
    
    ax1.set_xlabel(r"Tọa độ không gian $x$ ($\mathrm{nm}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Mật độ xác suất $|\psi(x)|^2$ ($\mathrm{nm}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Đánh đổi không gian thực & xung lượng: $\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$", 
                  fontsize=11, fontname="DejaVu Serif")
    ax1.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    
    # Subplot 2: Quantum confinement energy E_conf vs nanostructure size L
    L_nm = np.linspace(1.0, 20.0, 500) # Nanometer scale
    # E_conf = (hbar*pi)^2 / (2 * m_eff * L^2)
    # Let's use GaAs: m_eff = 0.067 * m0
    hbar = 1.054571817e-34
    m0 = 9.1093837e-31
    q = 1.602176634e-19
    me_gaas = 0.067 * m0
    me_si = 0.26 * m0 # transverse
    
    E_gaas = (hbar * np.pi)**2 / (2 * me_gaas * (L_nm * 1e-9)**2) / q # eV
    E_si = (hbar * np.pi)**2 / (2 * me_si * (L_nm * 1e-9)**2) / q # eV
    # Uncertainty minimum energy estimate: E_min = hbar^2 / (8 m (Delta x)^2) with Delta x = L/2
    E_uncert = (hbar)**2 / (2 * me_gaas * (L_nm * 1e-9 / 2.0)**2) / q
    
    ax2.plot(L_nm, E_gaas, color="#0072BD", lw=2.2, label=r"Hạt trong hộp GaAs: $E_{\mathrm{conf}} \propto \frac{1}{L^2}$ ($m^* = 0{,}067 m_0$)")
    ax2.plot(L_nm, E_si, color="#77AC30", lw=2.0, ls="--", label=r"Hạt trong hộp Si ($m^* = 0{,}26 m_0$)")
    ax2.plot(L_nm, E_uncert, color="#D95319", lw=1.6, ls=":", label=r"Cận dưới Heisenberg: $E_{\mathrm{min}} \approx \frac{\hbar^2}{2 m^* (\Delta x)^2}$")
    
    ax2.set_xlim(1.0, 15.0)
    ax2.set_ylim(0.0, 1.2)
    ax2.set_xlabel(r"Kích thước cấu trúc nano $L$ ($\mathrm{nm}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Năng lượng giam cầm lượng tử $E_{\mathrm{conf}}$ ($\mathrm{eV}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Hệ quả giam cầm lượng tử trong cấu trúc nano", fontsize=11, fontname="DejaVu Serif")
    ax2.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    
    # Callout at L = 3 nm
    ax2.annotate(r"Bùng nổ năng lượng khi $L < 5\ \mathrm{nm}$" + "\n" + r"$E_{\mathrm{conf}} > k_B T_{300\mathrm{K}} \approx 26\ \mathrm{meV}$",
                 xy=(3.0, E_gaas[np.argmin(np.abs(L_nm - 3.0))]), xytext=(5.0, 0.8),
                 arrowprops=dict(arrowstyle="->", color="#0072BD", lw=1.2),
                 fontsize=9, bbox=dict(boxstyle="round,pad=0.25", fc="#E3F2FD", ec="#0072BD", lw=0.8))

    fig.suptitle(r"Nguyên lý Bất định Heisenberg: Bản chất Vi mô & Hiệu ứng Giam cầm Không gian Nano", 
                 fontsize=12, y=0.98, fontname="DejaVu Serif")
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    fig.savefig(target, dpi=300)
    plt.close(fig)
    print(f"Generated: {target}")

# =============================================================================
# MUC 2.3 - PLOT 3: Tiên đề xác suất Max Born & Bản chất Hàm sóng phức
# =============================================================================
def generate_plot_2_3_3():
    target = os.path.join(KHO_ANH, "[Mo_Phong]_Muc_2.3_Mat_Do_Xac_Suat_Born_Va_Ham_Song.png")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    for ax in (ax1, ax2):
        ax.set_facecolor("#FFFFFF")
        ax.tick_params(direction="in", top=True, right=True, labelsize=9.5)
        ax.grid(True, ls="--", lw=0.6, color="#E0E0E0", alpha=0.7)
        for s in ax.spines.values():
            s.set_color("#1F1F1F")
            s.set_linewidth(1.0)
            
    # Subplot 1: Complex wave function: Re[psi], Im[psi], envelope |psi|, and probability density |psi|^2
    x = np.linspace(-6, 6, 600)
    sigma = 2.0
    k0 = 2.5
    env = np.exp(-(x**2) / (2 * sigma**2)) / (np.pi * sigma**2)**0.25
    psi_re = env * np.cos(k0 * x)
    psi_im = env * np.sin(k0 * x)
    prob_density = env**2 # Normalised |psi|^2
    
    ax1.plot(x, psi_re, color="#0072BD", lw=1.6, label=r"Phần thực: $\mathrm{Re}[\psi(x)]$")
    ax1.plot(x, psi_im, color="#7E2F8E", lw=1.4, ls="--", label=r"Phần ảo: $\mathrm{Im}[\psi(x)]$")
    ax1.plot(x, env, color="#7F7F7F", lw=1.2, ls=":", label=r"Đường bao: $|\psi(x)|$")
    ax1.plot(x, prob_density, color="#D95319", lw=2.4, label=r"Mật độ xác suất Born: $P(x) = |\psi(x)|^2$")
    ax1.fill_between(x, 0, prob_density, color="#D95319", alpha=0.15)
    
    ax1.set_xlabel(r"Tọa độ không gian $x$ ($\mathrm{nm}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Biên độ & Mật độ xác suất", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Hàm sóng phức $\psi(x)$ & Mật độ xác suất $|\psi|^2$", fontsize=11, fontname="DejaVu Serif")
    ax1.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    
    # Subplot 2: Quantum interference in double-slit: P_total = |psi1 + psi2|^2 vs classical P1 + P2
    y_screen = np.linspace(-5, 5, 600)
    d_slit = 1.6 # slit separation
    w_slit = 0.8
    # psi1 and psi2 from two slits
    psi1 = np.exp(-((y_screen - d_slit/2)**2) / (2 * w_slit**2)) * np.exp(1j * 3.0 * y_screen)
    psi2 = np.exp(-((y_screen + d_slit/2)**2) / (2 * w_slit**2)) * np.exp(-1j * 3.0 * y_screen)
    
    p_classical = np.abs(psi1)**2 + np.abs(psi2)**2
    p_quantum = np.abs(psi1 + psi2)**2
    
    ax2.plot(y_screen, p_classical, color="#7F7F7F", lw=1.8, ls="--", 
             label=r"Cộng xác suất cổ điển: $P_1 + P_2$ (Không giao thoa)")
    ax2.plot(y_screen, p_quantum, color="#0072BD", lw=2.2, 
             label=r"Cộng biên độ lượng tử: $|\psi_1 + \psi_2|^2$ (Có giao thoa)")
    ax2.fill_between(y_screen, 0, p_quantum, color="#0072BD", alpha=0.15)
    
    # Highlight interference term
    ax2.text(0.0, 2.7, r"Số hạng giao thoa: $2\mathrm{Re}[\psi_1^* \psi_2] = 2|\psi_1||\psi_2|\cos(\Delta\theta)$", 
             fontsize=9.5, ha="center", bbox=dict(boxstyle="round,pad=0.25", fc="#FFF9C4", ec="#FBC02D", lw=0.8))
    
    ax2.set_xlabel(r"Vị trí trên màn chắn $y$ ($\mathrm{\mu m}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Cường độ / Xác suất tìm thấy hạt", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Giao thoa lượng tử hai khe: Tiên đề Max Born", fontsize=11, fontname="DejaVu Serif")
    ax2.legend(loc="upper right", fontsize=8.5, framealpha=0.92)
    
    fig.suptitle(r"Tiên đề Xác suất Max Born: Bản chất Thống kê của Sóng Vật chất de Broglie", 
                 fontsize=12, y=0.98, fontname="DejaVu Serif")
    fig.tight_layout()
    fig.subplots_adjust(top=0.88)
    fig.savefig(target, dpi=300)
    plt.close(fig)
    print(f"Generated: {target}")

if __name__ == "__main__":
    print("Generating simulation plots for Muc 2.2...")
    generate_plot_2_2_1()
    generate_plot_2_2_2()
    generate_plot_2_2_3()
    print("Generating simulation plots for Muc 2.3...")
    generate_plot_2_3_1()
    generate_plot_2_3_2()
    generate_plot_2_3_3()
    print("All 6 simulation plots generated successfully!")

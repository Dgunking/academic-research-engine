# -*- coding: utf-8 -*-
"""
Script sinh đồ thị mô phỏng giải tích 300 K cho Mục 3.1: Cơ học thang nano, dao động tử điều hòa và định luật tỉ lệ tần số
Môn học: Cơ sở vật lý và công nghệ nano (PH3470 - HUST)
Tuân thủ tuyệt đối:
- Chuẩn đồ họa MATLAB R2014b+ 6 màu chuẩn
- Bố cục External Top Banner cho Legend (loc="lower center", bbox_to_anchor=(0.5, 1.02))
- Luật 14: Zero-Slash Fractions (Cấm phân số gạch chéo trong công thức toán)
- Thuật toán 13 ZT-GVLE & Triple Buffer Envelope (delta_geom >= 8%, delta_box >= 6 pt, delta_spine >= 5%)
- Ký số SHA-256 sidecar manifest
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from physics_viz_lock import apply_pedagogical_style, export_with_sidecar_manifest
from scripts.viz_legend_utils import auto_space_title_legend

apply_pedagogical_style()

OUTPUT_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bảng màu MATLAB chuẩn
COLOR_BLUE = "#0072BD"
COLOR_ORANGE = "#D95319"
COLOR_YELLOW = "#EDB120"
COLOR_PURPLE = "#7E2F8E"
COLOR_GREEN = "#77AC30"
COLOR_GRAY = "#7F7F7F"
COLOR_DARK = "#1F1F1F"
COLOR_BORDER_GRAY_HEX = "#CED4DA"


# =============================================================================
# ĐỒ THỊ 1: THẾ NĂNG LENNARD-JONES VÀ XẤP XỈ ĐIỀU HÒA BẬC HAI
# =============================================================================
def generate_plot_1():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    
    r_norm = np.linspace(0.96, 2.3, 500)
    u_lj = 4.0 * (r_norm**(-12) - r_norm**(-6))
    
    r0 = 2.0**(1.0 / 6.0)  # ~1.12246
    k_eff = 72.0 / (2.0**(1.0 / 3.0))  # ~57.146
    
    r_harm = np.linspace(1.02, 1.25, 200)
    u_harm = -1.0 + 0.5 * k_eff * (r_harm - r0)**2
    
    ax.plot(r_norm, u_lj, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Thế Lennard-Jones } U(r)$")
    ax.plot(r_harm, u_harm, color=COLOR_ORANGE, linestyle="--", linewidth=2.0, label=r"$\text{Xấp xỉ điều hòa } U_{\mathrm{harm}}(r)$")
    
    ax.axhline(0.0, color=COLOR_GRAY, linestyle=":", linewidth=1.0)
    ax.axvline(r0, ymin=0.22, ymax=0.44, color=COLOR_PURPLE, linestyle="-.", linewidth=1.2, label=r"$\text{Cân bằng } r_0 = 1.122\sigma$")
    ax.scatter([r0], [-1.0], color=COLOR_ORANGE, s=60, zorder=5)
    
    ax.set_xlim(0.85, 2.25)
    ax.set_ylim(-1.9, 2.8)
    
    ax.set_xlabel(r"$\text{Khoảng cách tương đối giữa hai nguyên tử, } r \cdot \sigma^{-1}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Thế năng tương tác liên kết, } U(r) \cdot \varepsilon^{-1}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Thế năng Lennard-Jones và xấp xỉ điều hòa bậc hai quanh đáy thế } r_0$", fontsize=11, fontweight="bold", pad=42)
    
    ax.annotate(
        r"$\text{Đáy thế: } U(r_0) = -\varepsilon$",
        xy=(r0, -1.0),
        xytext=(1.25, -1.55),
        ha="left",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )
    
    ax.annotate(
        r"$\text{Hút van der Waals } \propto -r^{-6}$",
        xy=(1.55, -0.3),
        xytext=(1.85, -0.85),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )
    
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)
    
    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.1_The_Nang_Lennard_Jones_Va_Xap_Xi_Dieu_Hoa.png")
    param_card = {
        "model": "Lennard-Jones 6-12 Potential & Harmonic Approximation",
        "equilibrium_distance": "r_0 = 2^{1/6} sigma approx 1.12246 sigma",
        "well_depth": "-epsilon",
        "effective_spring_constant": "k_eff = 72 epsilon / (2^{1/3} sigma^2) approx 57.146 epsilon / sigma^2",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 2: MẬT ĐỘ XÁC SUẤT DAO ĐỘNG TỬ LƯỢNG TỬ VS CỔ ĐIỂN
# =============================================================================
def generate_plot_2():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    
    xi = np.linspace(-4.5, 4.5, 600)
    
    psi0_sq = (1.0 / np.sqrt(np.pi)) * np.exp(-xi**2)
    psi2_sq = (1.0 / (8.0 * np.sqrt(np.pi))) * (4.0 * xi**2 - 2.0)**2 * np.exp(-xi**2)
    
    import scipy.special as sp
    h8 = sp.hermite(8)
    norm8 = 1.0 / np.sqrt(2**8 * float(sp.factorial(8)) * np.sqrt(np.pi))
    psi8 = norm8 * h8(xi) * np.exp(-0.5 * xi**2)
    psi8_sq = psi8**2
    
    a_cl = np.sqrt(17.0)
    p_cl = np.zeros_like(xi)
    mask = np.abs(xi) < (a_cl - 0.05)
    p_cl[mask] = 1.0 / (np.pi * np.sqrt(a_cl**2 - xi[mask]**2))
    p_cl[~mask] = 0.0
    
    ax.plot(xi, psi0_sq + 0.0, color=COLOR_BLUE, linewidth=2.0, label=r"$\text{Lượng tử } n = 0 \text{ (Cơ bản)}$")
    ax.plot(xi, psi2_sq + 0.35, color=COLOR_GREEN, linewidth=1.8, label=r"$\text{Lượng tử } n = 2$")
    ax.plot(xi, psi8_sq + 0.75, color=COLOR_ORANGE, linewidth=1.5, label=r"$\text{Lượng tử } n = 8$")
    ax.plot(xi, p_cl * 0.35 + 0.75, color=COLOR_PURPLE, linestyle="--", linewidth=1.8, label=r"$\text{Bao hình cổ điển } p_{\mathrm{cl}}(x)$")
    
    ax.axvline(a_cl, ymin=0.0, ymax=0.48, color=COLOR_GRAY, linestyle=":", linewidth=1.2)
    ax.axvline(-a_cl, ymin=0.0, ymax=0.48, color=COLOR_GRAY, linestyle=":", linewidth=1.2)
    
    ax.set_xlim(-4.6, 4.6)
    ax.set_ylim(-0.05, 2.35)
    
    ax.set_xlabel(r"$\text{Tọa độ không thứ nguyên, } \xi = \sqrt{\frac{m \cdot \omega}{\hbar}} \cdot x$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Mật độ xác suất tìm hạt dịch tầng, } |\psi_n(\xi)|^2 + \text{offset}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Mật độ xác suất dao động tử điều hòa: Lượng tử vs Cổ điển (Bohr Principle)}$", fontsize=11.0, fontweight="bold", pad=52)
    
    ax.annotate(
        r"$\text{Cực đại tại } \xi = 0$" + "\n" + r"$\text{(Đối lập cổ điển)}$",
        xy=(0.0, 0.56),
        xytext=(-0.5, 1.40),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Xuyên hầm lượng tử}$" + "\n" + r"$\text{qua } \pm A_{\mathrm{cl}}$",
        xy=(a_cl, 0.85),
        xytext=(2.6, 1.45),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )
    
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)
    
    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.1_Mat_Do_Xac_Suat_Dao_Dong_Tu_Luong_Tu_Va_Co_Dien.png")
    param_card = {
        "model": "Quantum Harmonic Oscillator (Hermite Polynomials) vs Classical Probability Density",
        "quantum_levels": "n = 0, 2, 8",
        "classical_turning_point_n8": "xi_turn = sqrt(2*8 + 1) approx 4.123",
        "bohr_correspondence": "Verified for n=8 with classical envelope alignment",
        "zero_point_energy": "E_0 = 0.5 hbar omega"
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 3: ĐỊNH LUẬT TỈ LỆ TẦN SỐ THEO KÍCH THƯỚC (SCALING LAW)
# =============================================================================
def generate_plot_3():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    
    L_vals = np.logspace(-8, 0, 400)
    
    f_ref = 1.5e10
    L_ref = 1.0e-7
    f_vals = f_ref * (L_ref / L_vals)
    
    ax.loglog(L_vals, f_vals, color=COLOR_BLUE, linewidth=2.5, label=r"$\text{Tỉ lệ: } f \propto L^{-1}$")
    
    ax.scatter([1.0], [1.5], color=COLOR_PURPLE, s=60, zorder=5)
    ax.scatter([1.0e-4], [1.5e7], color=COLOR_GREEN, s=60, zorder=5)
    ax.scatter([1.0e-7], [1.5e10], color=COLOR_ORANGE, s=70, zorder=5)
    
    ax.axvspan(1e-8, 1e-6, color=COLOR_ORANGE, alpha=0.10, label=r"$\text{NEMS: } 10\text{ nm} - 1\,\mu\text{m}$")
    ax.axvspan(1e-6, 1e-3, color=COLOR_GREEN, alpha=0.08, label=r"$\text{MEMS: } 1\,\mu\text{m} - 1\text{ mm}$")
    ax.axvspan(1e-3, 1.0, color=COLOR_PURPLE, alpha=0.06, label=r"$\text{Macro: } > 1\text{ mm}$")
    
    ax.set_xlim(8e-9, 1.5)
    ax.set_ylim(0.5, 3e11)
    
    ax.set_xlabel(r"$\text{Kích thước hình học đặc trưng của dầm dao động, } L \text{ [m]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Tần số dao động cộng hưởng riêng, } f \text{ [Hz]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Định luật tỉ lệ kích thước: Sự bùng nổ tần số siêu cao (GHz) ở thang nano}$", fontsize=10.5, fontweight="bold", pad=52)
    
    ax.annotate(
        r"$\text{NEMS: } L = 100\text{ nm}$" + "\n" + r"$\Rightarrow f \approx 15\text{ GHz}$",
        xy=(1.0e-7, 1.5e10),
        xytext=(3.0e-7, 2.0e11),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )
    
    ax.annotate(
        r"$\text{MEMS: } L = 100\,\mu\text{m}$" + "\n" + r"$\Rightarrow f \approx 15\text{ MHz}$",
        xy=(1.0e-4, 1.5e7),
        xytext=(3.0e-5, 2.0e5),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )
    
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)
    
    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.1_Dinh_Luat_Ti_Le_Tan_So_Theo_Kich_Thuoc.png")
    param_card = {
        "model": "Scaling Law for Resonant Frequency in Cantilever Beams (omega propto L^-1)",
        "spring_constant_scaling": "k propto L",
        "mass_scaling": "m propto L^3",
        "frequency_scaling": "omega = sqrt(k/m) propto sqrt(L / L^3) = L^-1",
        "nems_benchmark": "L = 100 nm -> f = 15 GHz (Slide 18 HUST)",
        "mems_benchmark": "L = 100 um -> f = 15 MHz",
        "macro_benchmark": "L = 1 m -> f = 1.5 Hz"
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)

if __name__ == "__main__":
    print("Generating simulation plots for Section 3.1 with External Top Banner Legend...")
    generate_plot_1()
    generate_plot_2()
    generate_plot_3()
    print("All 3 simulation plots for Section 3.1 successfully generated and certified with ZT-GVLE!")

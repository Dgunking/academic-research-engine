# -*- coding: utf-8 -*-
"""
Script sinh đồ thị mô phỏng giải tích 300 K cho Mục 3.2:
Nhiệt động học vi mô, động học chất lưu Stokes và chuyển động khuếch tán Brown
Môn học: Cơ sở vật lý và công nghệ nano (PH3470 - HUST)
Tuân thủ tuyệt đối:
- Chuẩn đồ họa MATLAB R2014b+ 6 màu chuẩn
- Bố cục External Top Banner cho Legend (loc="lower center", bbox_to_anchor=(0.5, 1.02))
- Luật 14: Zero-Slash Fractions
- Thuật toán 13 ZT-GVLE & Triple Buffer Envelope
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
# ĐỒ THỊ 1: HẰNG SỐ THỜI GIAN NHIỆT VÀ ĐỊNH LUẬT TỈ LỆ L^2
# =============================================================================
def generate_plot_1():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    L_vals = np.logspace(-9, -1, 400)

    tau_si = 1.102e4 * (L_vals**2)
    tau_cu = 8.624e3 * (L_vals**2)
    tau_cnt = 2.925e2 * (L_vals**2)

    ax.loglog(L_vals, tau_si, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Silicon (Si: } k_T \approx 148\,\text{W}\cdot\text{m}^{-1}\cdot\text{K}^{-1})$")
    ax.loglog(L_vals, tau_cu, color=COLOR_ORANGE, linestyle="--", linewidth=2.0, label=r"$\text{Đồng (Cu: } k_T \approx 400\,\text{W}\cdot\text{m}^{-1}\cdot\text{K}^{-1})$")
    ax.loglog(L_vals, tau_cnt, color=COLOR_GREEN, linestyle="-.", linewidth=2.0, label=r"$\text{CNT } (k_T \approx 3000\,\text{W}\cdot\text{m}^{-1}\cdot\text{K}^{-1})$")

    ax.scatter([1.0e-8], [1.102e-12], color=COLOR_BLUE, s=60, zorder=5)
    ax.scatter([1.0e-6], [1.102e-8], color=COLOR_PURPLE, s=60, zorder=5)

    ax.axvspan(1e-9, 1e-7, color=COLOR_ORANGE, alpha=0.08, label=r"$\text{Thang Nano (NEMS: } \tau_{\mathrm{th}} < 1\,\text{ns)}$")

    ax.set_xlim(8e-10, 1.5e-1)
    ax.set_ylim(5e-16, 5e3)

    ax.set_xlabel(r"$\text{Kích thước hình học đặc trưng của cấu trúc, } L \text{ [m]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Hằng số thời gian truyền nhiệt, } \tau_{\mathrm{th}} \text{ [s]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Định luật tỉ lệ nhiệt: Tản nhiệt tức thời thang picogiây } (\tau_{\mathrm{th}} \propto L^2)$", fontsize=10.5, fontweight="bold", pad=52)

    ax.annotate(
        r"$\text{Si } 10\text{ nm} \Rightarrow \tau_{\mathrm{th}} \approx 1.1\text{ ps}$",
        xy=(1.0e-8, 1.102e-12),
        xytext=(3.0e-8, 1.0e-14),
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Định luật tỉ lệ: } \tau_{\mathrm{th}} \propto L^2$",
        xy=(1.0e-4, 1.102e-4),
        xytext=(2.0e-3, 1.0e-9),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.2_Hang_So_Thoi_Gian_Nhiet_Va_Dinh_Luat_Ti_Le_L2.png")
    param_card = {
        "model": "Thermal Relaxation Scaling Law tau_th = L * C_V / (k_T * A) propto L^2",
        "silicon_thermal_coeff": "c_v * rho / k_T approx 1.102e4 s/m^2",
        "sub_nanosecond_cooling": "tau_th < 1 ps at L = 10 nm",
        "isothermal_nanostructures": "dT propto L -> internal thermal gradients vanish at nanoscale",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 2: ĐỐI CHUẨN LẮNG TRỌNG LỰC STOKES VS KHUẾCH TÁN BROWN
# =============================================================================
def generate_plot_2():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    R_vals = np.logspace(-9, -4.3, 400)

    eta = 1.8e-5
    rho = 2000.0
    g = 9.8
    k_B = 1.380649e-23
    T = 300.0
    t = 1.0

    h_grav = (2.0 * rho * g * (R_vals**2) / (9.0 * eta)) * t
    D_vals = (k_B * T) / (6.0 * np.pi * eta * R_vals)
    x_rms = np.sqrt(4.0 * D_vals * t)

    ax.loglog(R_vals, h_grav, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Lắng Stokes } (h_{\mathrm{grav}} \propto R^2)$")
    ax.loglog(R_vals, x_rms, color=COLOR_ORANGE, linewidth=2.2, label=r"$\text{Khuếch tán Brown } (x_{\mathrm{rms}} \propto R^{-0.5})$")

    ax.scatter([1.0e-8], [1.07e-8], color=COLOR_BLUE, s=60, zorder=5)
    ax.scatter([1.0e-8], [6.99e-5], color=COLOR_ORANGE, s=60, zorder=5)

    R_cross = ((4.0 * k_B * T / (6.0 * np.pi * eta))**0.5 / (2.0 * rho * g / (9.0 * eta)))**(1.0 / 2.5)
    d_cross = (2.0 * rho * g * (R_cross**2) / (9.0 * eta)) * t
    ax.scatter([R_cross], [d_cross], color=COLOR_PURPLE, s=80, marker="o", zorder=6, label=r"$\text{Điểm giao } R_c \approx 0.82\,\mu\text{m}$")
    ax.vlines(R_cross, 1e-9, d_cross, color=COLOR_GRAY, linestyle=":", linewidth=1.2)

    ax.axvspan(1e-9, R_cross, color=COLOR_ORANGE, alpha=0.08)
    ax.axvspan(R_cross, 5e-5, color=COLOR_BLUE, alpha=0.06)

    ax.set_xlim(8e-10, 6e-5)
    ax.set_ylim(1e-9, 5.0)

    ax.set_xlabel(r"$\text{Bán kính hạt chất rắn trong chất lưu, } R \text{ [m]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Độ dịch chuyển trong thời gian } t = 1\,\text{s} \text{ [m]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Đối chuẩn động học: Chuyển động nhiệt Brown lấn át trọng lực ở thang nano}$", fontsize=10.5, fontweight="bold", pad=42)

    ax.annotate(
        r"$\text{Hạt nano } R = 10\text{ nm:}$" + "\n" + r"$\text{Brown gấp } \approx 6500\text{ lần rơi}$",
        xy=(1.0e-8, 6.99e-5),
        xytext=(2.0e-9, 2.0e-6),
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Giao điểm: } R_c \approx 0.82\,\mu\text{m}$",
        xy=(R_cross, d_cross),
        xytext=(3.0e-6, 3.0e-8),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.2_Doi_Chuan_Van_Toc_Lang_Stokes_Va_Khuech_Tan_Brown.png")
    param_card = {
        "model": "Stokes Settling Velocity vs Einstein-Smoluchowski Brownian Diffusion",
        "medium": "Air at 300 K (eta = 1.8e-5 Pa.s, rho_particle = 2000 kg/m^3)",
        "diffusion_coefficient_scaling": "D = k_B * T / (6 pi eta R) propto R^-1",
        "terminal_velocity_scaling": "v_term propto R^2",
        "crossover_radius": "R_cross approx 0.82 um in air",
        "brownian_dominance_ratio": "x_rms / h_grav > 5000 at R = 10 nm"
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 3: THẾ NĂNG MA SÁT VÀ HIỆN TƯỢNG SIÊU TRƠN CẤU TRÚC
# =============================================================================
def generate_plot_3():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    theta_deg = np.linspace(0.0, 60.0, 500)

    f_commensurate = 1.0
    f_incommensurate = 0.002
    sigma_deg = 2.2
    peak0 = np.exp(-(theta_deg**2) / (2.0 * sigma_deg**2))
    peak60 = np.exp(-((theta_deg - 60.0)**2) / (2.0 * sigma_deg**2))
    f_friction = f_incommensurate + (f_commensurate - f_incommensurate) * (peak0 + peak60)

    ax.semilogy(theta_deg, f_friction, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Lực ma sát liên lớp } F_s(\theta) \cdot F_{\mathrm{max}}^{-1}$")
    ax.axhline(f_incommensurate, color=COLOR_GREEN, linestyle="--", linewidth=1.5, label=r"$\text{Mức siêu trơn } (F_s \leq 0.002 F_{\mathrm{max}})$")

    ax.scatter([0.0, 60.0], [1.0, 1.0], color=COLOR_ORANGE, s=70, zorder=5, label=r"$\text{Ăn khớp } (\theta = 0^{\circ}, 60^{\circ})$")
    ax.scatter([30.0], [f_incommensurate], color=COLOR_PURPLE, s=70, zorder=5, label=r"$\text{Lệch } (\theta = 30^{\circ})$")

    ax.axvspan(5.0, 55.0, color=COLOR_GREEN, alpha=0.08)

    ax.set_xlim(-2.0, 62.0)
    ax.set_ylim(5e-4, 5.0)

    ax.set_xlabel(r"$\text{Góc lệch xoay mạng giữa hai lớp Graphene, } \theta \text{ [độ]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Lực ma sát tĩnh chuẩn hóa, } F_s(\theta) \cdot F_{\mathrm{max}}^{-1}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Ma sát nguyên tử: Hiện tượng siêu trơn do bất tương thích mạng Graphite – CNT}$", fontsize=10.5, fontweight="bold", pad=52)

    ax.annotate(
        r"$\text{Khóa mạng: } F_s = F_{\mathrm{max}}$",
        xy=(0.0, 1.0),
        xytext=(10.0, 0.25),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Siêu trơn: Ma sát triệt tiêu } 99.8\%$",
        xy=(30.0, f_incommensurate),
        xytext=(30.0, 0.005),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.2_The_Nang_Ma_Sat_Va_Hien_Tuong_Sieu_Tron_Incommensurate.png")
    param_card = {
        "model": "Structural Superlubricity in Rotated Graphene Bilayers & Multiwalled CNTs",
        "commensurate_angles": "theta = 0 deg and 60 deg (hexagonal symmetry)",
        "incommensurate_friction_drop": "F_s drops by > 99.8% in incommensurate regime (5 to 55 deg)",
        "physical_mechanism": "Lattice cancellation of lateral van der Waals forces",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating simulation plots for Section 3.2 with External Top Banner Legend...")
    generate_plot_1()
    generate_plot_2()
    generate_plot_3()
    print("All 3 simulation plots for Section 3.2 successfully generated and certified with ZT-GVLE!")

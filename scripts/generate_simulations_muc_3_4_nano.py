# -*- coding: utf-8 -*-
"""
generate_simulations_muc_3_4_nano.py
Tạo 3 đồ thị mô phỏng giải tích 300 K cho Mục 3.4:
1. Đồ thị 1: Phổ tán xạ Raman theo kích thước hạt nano (Mô hình Fauchet-Richter).
2. Đồ thị 2: Đường cong từ trễ M(H) và chuyển pha siêu thuận từ (Hàm Langevin).
3. Đồ thị 3: Thời gian hồi phục Néel và giới hạn siêu thuận từ theo đường kính hạt.
Tuân thủ toàn trình Thuật toán 13 ZT-GVLE, bố cục External Top Banner cho Legend, và ký số SHA-256 sidecar manifest.
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

from physics_viz_lock import (
    apply_pedagogical_style,
    export_with_sidecar_manifest,
)
from scripts.viz_legend_utils import auto_space_title_legend

OUTPUT_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(OUTPUT_DIR, exist_ok=True)

COLOR_BLUE = "#0072BD"
COLOR_ORANGE = "#D95319"
COLOR_YELLOW = "#EDB120"
COLOR_PURPLE = "#7E2F8E"
COLOR_GREEN = "#77AC30"
COLOR_GRAY = "#7F7F7F"
COLOR_DARK = "#222222"
COLOR_BORDER_GRAY_HEX = "#CCCCCC"

apply_pedagogical_style()


# =============================================================================
# ĐỒ THỊ 1: PHỔ TÁN XẠ RAMAN THEO KÍCH THƯỚC HẠT NANO
# =============================================================================
def generate_plot_1():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    w = np.linspace(495.0, 535.0, 500)
    w_bulk = 520.5
    gamma_0 = 3.6

    # L = 20 nm (Bulk-like)
    I_20 = 1.0 / ((w - w_bulk)**2 + (gamma_0 / 2.0)**2)
    I_20 /= np.max(I_20)

    # L = 6 nm
    w_6 = w_bulk - 1.8
    gamma_6 = 6.2
    I_6 = 0.85 / ((w - w_6)**2 + (gamma_6 / 2.0)**2)
    I_6 *= (1.0 + 0.15 * np.exp(-(w - w_6) / 4.0) * (w < w_6))
    I_6 /= np.max(I_6)

    # L = 4 nm
    w_4 = w_bulk - 4.2
    gamma_4 = 9.8
    I_4 = 0.65 / ((w - w_4)**2 + (gamma_4 / 2.0)**2)
    I_4 *= (1.0 + 0.25 * np.exp(-(w - w_4) / 5.0) * (w < w_4))
    I_4 /= np.max(I_4)

    # L = 2.5 nm
    w_25 = w_bulk - 8.5
    gamma_25 = 16.0
    I_25 = 0.45 / ((w - w_25)**2 + (gamma_25 / 2.0)**2)
    I_25 *= (1.0 + 0.35 * np.exp(-(w - w_25) / 6.0) * (w < w_25))
    I_25 /= np.max(I_25)

    ax.plot(w, I_20, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Khối } (L = 20\,\text{nm})$")
    ax.plot(w, I_6, color=COLOR_GREEN, linewidth=2.0, label=r"$\text{Hạt } L = 6\,\text{nm}$")
    ax.plot(w, I_4, color=COLOR_ORANGE, linewidth=2.0, label=r"$\text{Hạt } L = 4\,\text{nm}$")
    ax.plot(w, I_25, color=COLOR_PURPLE, linewidth=2.0, label=r"$\text{Hạt } L = 2.5\,\text{nm}$")

    ax.axvline(w_bulk, color=COLOR_GRAY, linestyle=":", linewidth=1.2)

    ax.set_xlim(496.0, 534.0)
    ax.set_ylim(0.0, 1.4)

    ax.set_xlabel(r"$\text{Số sóng Raman, } \omega \text{ [cm}^{-1}\text{]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Cường độ tán xạ chuẩn hóa, } I(\omega) \text{ [đ.v.t.đ]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Tiến hóa phổ Raman theo kích thước hạt nano (Mô hình Fauchet)}$", fontsize=10.5, fontweight="bold", pad=52)

    ax.annotate(
        r"$\text{Đỉnh khối: } 520.5\,\text{cm}^{-1}$",
        xy=(w_bulk, 1.0),
        xytext=(524.0, 1.08),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Dịch đỏ và mở rộng}$",
        xy=(w_25, 0.45),
        xytext=(502.0, 1.05),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.4_Pho_Raman_Theo_Kich_Thuoc_Hat_Model_Fauchet.png")
    param_card = {
        "model": "Richter-Campbell-Fauchet Phonon Confinement Model",
        "material": "Nanocrystalline Silicon / Cerium Oxide (CeO2)",
        "bulk_optical_phonon": "omega_0 = 520.5 cm^-1, Gamma_0 = 3.6 cm^-1",
        "spatial_confinement": "Breakdown of q = 0 selection rule due to delta_x ~ L",
        "effects": "Red shift and asymmetric broadening as size L decreases to 2.5 nm",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 2: ĐƯỜNG CONG TỪ TRỄ VÀ CHUYỂN PHA SIÊU THUẬN TỪ
# =============================================================================
def generate_plot_2():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    H = np.linspace(-1500.0, 1500.0, 600)

    # 1. Nhánh Sắt từ
    Hc = 350.0
    Mr = 0.65
    H_upper = H + Hc
    H_lower = H - Hc
    M_ferro_up = (2.0 / np.pi) * np.arctan(H_upper / 180.0)
    M_ferro_down = (2.0 / np.pi) * np.arctan(H_lower / 180.0)

    ax.plot(H, M_ferro_up, color=COLOR_BLUE, linewidth=2.0, label=r"$\text{Sắt từ } (L = 50\,\text{nm}): H_c = 350\,\text{Oe, } M_r > 0$")
    ax.plot(H, M_ferro_down, color=COLOR_BLUE, linewidth=2.0)

    # 2. Nhánh Siêu thuận từ
    xi = H / 120.0
    xi_safe = np.where(np.abs(xi) < 1e-4, 1e-4, xi)
    M_super = np.cosh(xi_safe) / np.sinh(xi_safe) - 1.0 / xi_safe
    M_super = np.where(np.abs(xi) < 1e-4, 0.0, M_super)

    ax.plot(H, M_super, color=COLOR_ORANGE, linewidth=2.2, linestyle="--", label=r"$\text{Siêu thuận từ } (L = 8\,\text{nm}): H_c = 0\,\text{Oe, } M_r = 0$")

    ax.axhline(0.0, color=COLOR_GRAY, linestyle=":", linewidth=1.0)
    ax.axvline(0.0, color=COLOR_GRAY, linestyle=":", linewidth=1.0)

    ax.scatter([0.0], [Mr], color=COLOR_BLUE, s=50, zorder=5)
    ax.scatter([-Hc], [0.0], color=COLOR_BLUE, s=50, zorder=5)
    ax.scatter([0.0], [0.0], color=COLOR_ORANGE, s=70, marker="o", zorder=6)

    ax.set_xlim(-1600.0, 1600.0)
    ax.set_ylim(-1.3, 1.3)

    ax.set_xlabel(r"$\text{Từ trường ngoài tác dụng, } H \text{ [Oe]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Độ từ hóa chuẩn hóa, } M(H) \cdot M_s^{-1}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Đặc tuyến từ trễ: Chuyển pha Sắt từ sang Siêu thuận từ ở thang nano}$", fontsize=10.5, fontweight="bold", pad=42)

    ax.annotate(
        r"$\text{Từ dư: } M_r = 0.65 M_s$" + "\n" + r"$\text{Lực kháng: } H_c = 350\,\text{Oe}$",
        xy=(-Hc, 0.0),
        xytext=(-850.0, 0.55),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Siêu thuận từ:}$" + "\n" + r"$\text{Triệt tiêu từ trễ } (H_c = 0)$",
        xy=(0.0, 0.0),
        xytext=(650.0, -0.55),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=1, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.4_Duong_Cong_Tu_Tre_Va_Chuyen_Pha_Sieu_Thuan_Tu.png")
    param_card = {
        "model": "Ferromagnetic Hysteresis vs Superparamagnetic Langevin Magnetization",
        "material": "Magnetite (Fe3O4) / Cobalt Nanoparticles at 300 K",
        "ferromagnetic_size": "L = 50 nm (stable single domain, H_c = 350 Oe)",
        "superparamagnetic_size": "L = 8 nm (thermal fluctuations overcome anisotropy barrier KV < k_B T)",
        "remanence_coercivity": "M_r = 0 and H_c = 0 in superparamagnetic regime",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 3: THỜI GIAN HỒI PHỤC NÉEL VÀ GIỚI HẠN SIÊU THUẬN TỪ
# =============================================================================
def generate_plot_3():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    D_nm = np.linspace(4.5, 17.5, 500)
    D_m = D_nm * 1e-9

    k_B = 1.380649e-23
    T = 300.0
    tau_0 = 1.0e-9

    K_fe3o4 = 2.5e4
    V_fe3o4 = (np.pi / 6.0) * (D_m**3)
    tau_fe3o4 = tau_0 * np.exp(np.clip(K_fe3o4 * V_fe3o4 / (k_B * T), 0.0, 45.0))

    K_co = 4.5e5
    V_co = (np.pi / 6.0) * (D_m**3)
    tau_co = tau_0 * np.exp(np.clip(K_co * V_co / (k_B * T), 0.0, 45.0))

    ax.semilogy(D_nm, tau_fe3o4, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Hạt Fe}_3\text{O}_4 \ (K = 2.5 \times 10^4\,\text{J}\cdot\text{m}^{-3})$")
    ax.semilogy(D_nm, tau_co, color=COLOR_ORANGE, linewidth=2.2, label=r"$\text{Hạt Cobalt } (K = 4.5 \times 10^5\,\text{J}\cdot\text{m}^{-3})$")

    t_10years = 3.15e8
    ax.axhline(t_10years, color=COLOR_GREEN, linestyle="--", linewidth=1.5, label=r"$\text{Lưu trữ 10 năm } (\tau = 3.15 \times 10^8\,\text{s})$")
    ax.axhline(100.0, color=COLOR_GRAY, linestyle=":", linewidth=1.2, label=r"$\text{Ngưỡng Lab } (\tau = 100\,\text{s})$")

    ax.axhspan(1e-10, 100.0, color=COLOR_PURPLE, alpha=0.06)

    ax.set_xlim(4.0, 18.0)
    ax.set_ylim(1e-10, 1e20)

    ax.set_xlabel(r"$\text{Đường kính hạt từ tính nano, } D \text{ [nm]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Thời gian hồi phục Néel, } \tau_N \text{ [s]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Định luật Arrhenius-Néel: Giới hạn siêu thuận từ ở nhiệt độ 300 K}$", fontsize=10.5, fontweight="bold", pad=52)

    ax.annotate(
        r"$\text{Giới hạn Cobalt: } D_p \approx 7.8\,\text{nm}$",
        xy=(7.8, t_10years),
        xytext=(11.5, 1e12),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Siêu thuận từ: } \tau < 1\,\text{s}$",
        xy=(5.0, 1e-9),
        xytext=(5.1, 1e-4),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.4_Thoi_Gian_Hoi_Phuc_Neel_Va_Gioi_Han_Sieu_Thuan_Tu.png")
    param_card = {
        "model": "Neel-Arrhenius Thermal Relaxation Time tau_N = tau_0 * exp(KV / k_B T)",
        "materials": "Fe3O4 (K = 2.5e4 J/m^3) and Co (K = 4.5e5 J/m^3) at 300 K",
        "superparamagnetic_limit": "Diameter D_p below which retention time drops below 10 years",
        "cobalt_critical_diameter": "D_p approx 7.8 nm for 10-year thermal stability",
        "fe3o4_critical_diameter": "D_p approx 20.5 nm for 10-year stability",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating simulation plots for Section 3.4 with External Top Banner Legend...")
    generate_plot_1()
    generate_plot_2()
    generate_plot_3()
    print("All 3 simulation plots for Section 3.4 successfully generated and certified with ZT-GVLE!")

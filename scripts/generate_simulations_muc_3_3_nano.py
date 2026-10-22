# -*- coding: utf-8 -*-
"""
generate_simulations_muc_3_3_nano.py
Tạo 3 đồ thị mô phỏng giải tích 300 K cho Mục 3.3:
1. Đồ thị 1: Đối chuẩn giải tích Mật độ trạng thái điện tử (DOS) 3D, 2D, 1D, 0D.
2. Đồ thị 2: Mô hình Brus - Độ dịch chuyển xanh của khe năng lượng theo bán kính chấm lượng tử.
3. Đồ thị 3: Phân loại vector chiral (n, m) và khe năng lượng của ống than nano CNT.
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
# ĐỒ THỊ 1: MẬT ĐỘ TRẠNG THÁI ĐIỆN TỬ (DOS) TRONG 3D, 2D, 1D, 0D
# =============================================================================
def generate_plot_1():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    E = np.linspace(0.001, 5.0, 600)

    # 1. 3D Bulk: g_3D(E) propto sqrt(E)
    g_3d = 0.8 * np.sqrt(E)
    ax.plot(E, g_3d, color=COLOR_BLUE, linewidth=2.0, label=r"$\text{Khối 3D } (g \propto E^{0.5})$")

    # 2. 2D Quantum Well: g_2D(E) propto sum_n theta(E - E_n)
    levels_2d = [1.0, 2.3, 3.8]
    g_2d = np.zeros_like(E)
    step_val = 0.55
    for en in levels_2d:
        g_2d += step_val * (E >= en)
    ax.step(E, g_2d, where="post", color=COLOR_ORANGE, linewidth=2.0, label=r"$\text{Giếng 2D } (g \propto \sum \theta)$")

    # 3. 1D Quantum Wire: g_1D(E) propto sum (E - E_nm)^(-0.5)
    levels_1d = [1.5, 3.2]
    g_1d = np.zeros_like(E)
    for en in levels_1d:
        mask = E > en
        term = np.zeros_like(E)
        term[mask] = 0.45 / np.sqrt(np.maximum(1e-4, E[mask] - en))
        term = np.clip(term, 0.0, 2.2)
        g_1d += term
    ax.plot(E, g_1d, color=COLOR_PURPLE, linewidth=2.0, label=r"$\text{Dây 1D } (g \propto \Delta E^{-0.5})$")

    # 4. 0D Quantum Dot: g_0D(E) propto sum delta(E - E_i)
    levels_0d = [0.8, 1.8, 2.9, 4.2]
    for i, en in enumerate(levels_0d):
        lbl = r"$\text{Chấm 0D } (g \propto \sum \delta)$" if i == 0 else None
        ax.vlines(en, 0.0, 2.3, color=COLOR_GREEN, linewidth=2.5, linestyle="-", label=lbl)
        ax.scatter([en], [2.3], color=COLOR_GREEN, s=40, zorder=5)

    ax.set_xlim(0.0, 5.2)
    ax.set_ylim(0.0, 3.2)

    ax.set_xlabel(r"$\text{Năng lượng hạt tải, } E \text{ [eV]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Mật độ trạng thái chuẩn hóa, } g(E) \text{ [đ.v.t.đ]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Mật độ trạng thái điện tử (DOS) theo chiều không gian 3D, 2D, 1D, 0D}$", fontsize=10.5, fontweight="bold", pad=52)

    ax.annotate(
        r"$\text{Đỉnh Van Hove 1D}$",
        xy=(1.52, 2.1),
        xytext=(2.2, 2.6),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Bậc thang 2D}$",
        xy=(1.05, 0.55),
        xytext=(1.4, 0.15),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.3_So_Sanh_Mat_Do_Trang_Thai_DOS_3D_2D_1D_0D.png")
    param_card = {
        "model": "Electronic Density of States across Dimensions (3D, 2D, 1D, 0D)",
        "3d_bulk": "g(E) propto E^0.5 (continuous parabolic)",
        "2d_quantum_well": "g(E) propto sum theta(E - E_n) (Heaviside step function)",
        "1d_quantum_wire": "g(E) propto sum (E - E_nm)^-0.5 (Van Hove singularities)",
        "0d_quantum_dot": "g(E) propto sum delta(E - E_i) (atomic-like delta peaks)",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 2: MÔ HÌNH BRUS - KHE NĂNG LƯỢNG QUANG THEO BÁN KÍNH CHẤM LƯỢNG TỬ
# =============================================================================
def generate_plot_2():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    R_nm = np.linspace(1.2, 8.0, 400)
    R_m = R_nm * 1e-9

    hbar = 1.054571817e-34
    e_charge = 1.602176634e-19
    eps_0 = 8.8541878128e-12
    m_0 = 9.1093837015e-31

    Eg_bulk = 1.74
    m_e = 0.13 * m_0
    m_h = 0.45 * m_0
    mu = (m_e * m_h) / (m_e + m_h)
    eps_r = 10.0

    E_conf_eV = ((hbar**2 * np.pi**2) / (2.0 * mu * R_m**2)) / e_charge
    E_coul_eV = ((1.786 * e_charge) / (4.0 * np.pi * eps_0 * eps_r * R_m))
    Eg_eff = Eg_bulk + E_conf_eV - E_coul_eV

    ax.plot(R_nm, Eg_eff, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{Mô hình Brus: } E_g(R) = E_{g,\mathrm{bulk}} + \Delta E_{\mathrm{conf}} - \Delta E_{\mathrm{Coul}}$")
    ax.axhline(Eg_bulk, color=COLOR_GRAY, linestyle="--", linewidth=1.5, label=r"$\text{Khối CdSe: } E_{g,\mathrm{bulk}} = 1.74\,\text{eV}$")

    R_sample = 2.0
    Eg_sample = Eg_bulk + (((hbar**2 * np.pi**2) / (2.0 * mu * (R_sample*1e-9)**2)) / e_charge) - ((1.786 * e_charge) / (4.0 * np.pi * eps_0 * eps_r * (R_sample*1e-9)))
    ax.scatter([R_sample], [Eg_sample], color=COLOR_ORANGE, s=70, zorder=5)

    ax.set_xlim(1.0, 8.2)
    ax.set_ylim(1.5, 4.2)

    ax.set_xlabel(r"$\text{Bán kính hạt chấm lượng tử, } R \text{ [nm]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Khe năng lượng quang hiệu dụng, } E_g \text{ [eV]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Độ dịch chuyển xanh khe năng lượng theo mô hình Brus (CdSe at 300 K)}$", fontsize=10.5, fontweight="bold", pad=42)

    ax.annotate(
        r"$\text{Giam giữ mạnh: } R = 2\text{ nm} \Rightarrow E_g \approx 2.45\text{ eV}$",
        xy=(R_sample, Eg_sample),
        xytext=(3.8, 2.8),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Tiệm cận khối: } R \to \infty \Rightarrow E_g \to 1.74\text{ eV}$",
        xy=(7.0, 1.8),
        xytext=(5.5, 2.1),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=1, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.3_Khe_Nang_Luong_Theo_Ban_Kinh_Cham_Luong_Tu_Model_Brus.png")
    param_card = {
        "model": "Brus Effective Mass Model for Quantum Dots",
        "material": "Cadmium Selenide (CdSe) at 300 K",
        "bulk_bandgap_eV": 1.74,
        "electron_effective_mass": "0.13 m_0",
        "hole_effective_mass": "0.45 m_0",
        "dielectric_constant": 10.0,
        "confinement_energy_scaling": "Delta E propto R^-2 (dominant for R < 3 nm)",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


# =============================================================================
# ĐỒ THỊ 3: KHE NĂNG LƯỢNG VÀ VECTOR CHIRAL (n, m) CỦA ỐNG THAN NANO CNT
# =============================================================================
def generate_plot_3():
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    d_t = np.linspace(0.6, 2.5, 400)
    E_g_semiconducting = 0.824 / d_t

    ax.plot(d_t, E_g_semiconducting, color=COLOR_BLUE, linewidth=2.2, label=r"$\text{CNT bán dẫn: } E_g(d_t) \approx 0.824\,\text{eV}\cdot\text{nm} \cdot d_t^{-1}$")
    ax.axhline(0.0, color=COLOR_ORANGE, linewidth=2.5, label=r"$\text{CNT kim loại: } E_g = 0\,\text{eV}$")

    ax.scatter([0.783], [1.05], color=COLOR_BLUE, s=70, zorder=5, label=r"$\text{Ống (10, 0) Zigzag } (1.05\,\text{eV})$")
    ax.scatter([0.939], [0.0], color=COLOR_ORANGE, s=70, zorder=5, label=r"$\text{Ống (12, 0) Zigzag } (0\,\text{eV})$")

    ax.set_xlim(0.5, 2.6)
    ax.set_ylim(-0.1, 2.0)

    ax.set_xlabel(r"$\text{Đường kính ống than nano, } d_t \text{ [nm]}$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Khe năng lượng dải cấm, } E_g \text{ [eV]}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Đặc tính điện của Carbon Nanotubes theo vector chiral } (n, m)$", fontsize=10.5, fontweight="bold", pad=52)

    ax.annotate(
        r"$\text{Quy tắc: } (n - m)\ \mathrm{mod}\ 3 = 0 \Rightarrow \text{Kim loại}$",
        xy=(1.5, 0.0),
        xytext=(1.5, 0.35),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.annotate(
        r"$\text{Nghịch biến: } E_g \propto d_t^{-1}$",
        xy=(1.0, 0.824),
        xytext=(1.6, 1.25),
        ha="center",
        arrowprops=dict(arrowstyle="->", color=COLOR_DARK, lw=1.2),
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFFFFF", ec=COLOR_BORDER_GRAY_HEX, alpha=0.95)
    )

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    out_path = os.path.join(OUTPUT_DIR, "[Mo_Phong]_Muc_3.3_Phan_Loai_Vector_Chiral_Va_Khe_Nang_Luong_CNT.png")
    param_card = {
        "model": "Carbon Nanotube (CNT) Bandgap Dispersion vs Chiral Vector (n, m)",
        "metallic_condition": "(n - m) mod 3 == 0 (zero bandgap metallic conduction)",
        "semiconducting_condition": "(n - m) mod 3 != 0 (finite bandgap Eg propto 1/d_t)",
        "carbon_carbon_bond": "a_cc = 0.142 nm, gamma_0 = 2.9 eV",
        "diameter_formula": "d_t = (a / pi) * sqrt(n^2 + nm + m^2)",
        "operating_temperature_k": 300.0
    }
    export_with_sidecar_manifest(fig, out_path, parameter_card=param_card)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating simulation plots for Section 3.3 with External Top Banner Legend...")
    generate_plot_1()
    generate_plot_2()
    generate_plot_3()
    print("All 3 simulation plots for Section 3.3 successfully generated and certified with ZT-GVLE!")

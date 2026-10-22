# -*- coding: utf-8 -*-
"""
generate_simulations_muc_2_3_laser.py
Sinh đồ thị mô phỏng giải tích 300 K cho Mục 2.3: Phát xạ tự phát và vận hành linh kiện LED.
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(r"d:\antigravity\academic-research-engine")
sys.path.append(r"d:\antigravity\academic-research-engine\scripts")
from physics_viz_lock import (
    apply_pedagogical_style,
    export_with_sidecar_manifest,
    assert_triple_buffer_geometry,
)
from viz_legend_utils import auto_space_title_legend

drive_img_dir = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Laser Diode - Cấu trúc và Nguyên lý\Kho_Hinh_Anh"
os.makedirs(drive_img_dir, exist_ok=True)

apply_pedagogical_style()

COLOR_BLUE = "#0072BD"
COLOR_ORANGE = "#D95319"
COLOR_YELLOW = "#EDB120"
COLOR_PURPLE = "#7E2F8E"
COLOR_GREEN = "#77AC30"
COLOR_DARK = "#1F1F1F"

# ---------------------------------------------------------------------------
# 1. PLOT 2.3a: HIỆU SUẤT TRÍCH XUẤT ÁNH SÁNG & GÓC TỚI HẠN THEO CHIẾT SUẤT
# ---------------------------------------------------------------------------
def generate_plot_2_3a():
    print("--- Generating Plot 2.3a: [Mo_Phong]_Muc_2.3_Hieu_Suat_Trich_Xuat_Quang_LED.png ---")
    fig, ax1 = plt.subplots(figsize=(6.8, 4.4))

    n_semi = np.linspace(2.2, 4.2, 300)
    # Góc tới hạn: theta_c = arcsin(1 / n)
    theta_c_deg = np.rad2deg(np.arcsin(1.0 / n_semi))

    # Góc khối nón thoát: Omega_c = 2 * pi * (1 - cos(theta_c))
    # Hiệu suất trích xuất qua 1 mặt phẳng (bỏ qua phản xạ Fresnel mặt trước):
    # eta_ex = (1 - cos(theta_c)) / 2 approx 1 / (4 * n_semi^2)
    eta_ex_exact = (1.0 - np.cos(np.deg2rad(theta_c_deg))) / 2.0 * 100.0 # %
    eta_ex_approx = (1.0 / (4.0 * (n_semi ** 2))) * 100.0 # %

    ax1.plot(n_semi, eta_ex_exact, color=COLOR_BLUE, lw=2.4, label=r"$\text{Hiệu suất trích xuất chính xác } \eta_{\mathrm{ex}}\ [\%]$")
    ax1.plot(n_semi, eta_ex_approx, color=COLOR_ORANGE, lw=1.8, ls="--", label=r"$\text{Xấp xỉ góc hẹp } (4 n_r^2)^{-1}\ [\%]$")

    # Mốc GaAs (n = 3.65)
    n_gaas = 3.65
    eta_gaas = (1.0 - np.cos(np.arcsin(1.0 / n_gaas))) / 2.0 * 100.0
    ax1.plot([n_gaas, n_gaas], [0.0, eta_gaas], color=COLOR_GREEN, lw=1.4, ls=":")
    ax1.plot(n_gaas, eta_gaas, 'o', color=COLOR_GREEN, markersize=6, label=r"$\text{GaAs } (n = 3{,}65,\ \eta_{\mathrm{ex}} \approx 1{,}92\%)$")

    ax1.set_xlim(2.2, 4.2)
    ax1.set_ylim(0.0, 6.0)

    ax1.set_xlabel(r"$\text{Chiết suất bán dẫn } n_r$", fontsize=10.5, fontweight="bold")
    ax1.set_ylabel(r"$\text{Hiệu suất trích xuất ánh sáng } \eta_{\mathrm{ex}}\ [\%]$", fontsize=10.5, fontweight="bold")
    ax1.set_title(r"$\text{Hiệu suất trích xuất ánh sáng } \eta_{\mathrm{ex}}\text{ & giới hạn nón thoát Snell trong LED}$", fontsize=11, fontweight="bold", pad=42)

    ax1.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=2,
        frameon=True,
        edgecolor=COLOR_DARK,
        fancybox=False,
        framealpha=0.95,
        fontsize=9.0,
    )

    auto_space_title_legend(fig, ax1, min_gap_pt=20.0)
    assert_triple_buffer_geometry(fig)

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.3_Hieu_Suat_Trich_Xuat_Quang_LED.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Bán dẫn III–V (GaAs, InP, GaN)",
            "sweep_parameters": "Chiết suất <i>n<sub>r</sub></i> = 2,2 đến 4,2; góc tới hạn <i>θ<sub>c</sub></i> = 13,8° đến 27,0°",
            "lab_metrics": "GaAs (<i>n</i> = 3,65) chỉ trích xuất được 1,92% photon qua mặt phân giới phẳng không lớp phủ"
        }
    )
    plt.close(fig)
    print(f"Plot 2.3a PASS: {plot_path}")


# ---------------------------------------------------------------------------
# 2. PLOT 2.3b: PHỔ PHÁT XẠ TỰ PHÁT & ĐỘ RỘNG FWHM
# ---------------------------------------------------------------------------
def generate_plot_2_3b():
    print("--- Generating Plot 2.3b: [Mo_Phong]_Muc_2.3_Pho_Phat_Xa_Tu_Phat_GaAs.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Năng lượng photon E quanh Eg = 1.424 eV ở 300 K
    Eg = 1.424 # eV
    kBT = 0.02585 # eV
    E = np.linspace(1.40, 1.55, 400) # eV

    # Tốc độ phát xạ tự phát R_sp(E) ~ sqrt(E - Eg) * exp(-(E - Eg) / kBT) khi E >= Eg
    dE = E - Eg
    R_sp = np.zeros_like(E)
    valid = dE >= 0.0
    R_sp[valid] = np.sqrt(dE[valid]) * np.exp(-dE[valid] / kBT)
    # Chuẩn hóa đỉnh cực đại về 1.0
    R_sp = R_sp / np.max(R_sp)

    # Đỉnh tại dE = kBT / 2 = 0.0129 eV -> E_peak = Eg + 0.0129 = 1.437 eV
    E_peak = Eg + 0.5 * kBT

    # Chuyển đổi sang bước sóng lambda = hc / E (nm)
    hc_eV_nm = 1239.841984
    wavelength = hc_eV_nm / E

    ax.plot(E, R_sp, color=COLOR_BLUE, lw=2.4, label=r"$\text{Phổ phát xạ tự phát } R_{\mathrm{sp}}(E)\text{ ở } 300\ \mathrm{K}$")
    ax.axvline(Eg, color=COLOR_ORANGE, ls="--", lw=1.5, label=r"$\text{Độ rộng vùng cấm } E_g = 1{,}424\ \mathrm{eV}$")
    ax.plot([E_peak, E_peak], [0.0, 1.0], color=COLOR_GREEN, ls=":", lw=1.5, label=r"$\text{Đỉnh phổ } E_{\mathrm{peak}} = E_g + \frac{1}{2}k_B T \approx 1{,}437\ \mathrm{eV}$")

    ax.set_xlim(1.41, 1.54)
    ax.set_ylim(0.0, 1.15)

    ax.set_xlabel(r"$\text{Năng lượng photon } E = h\nu\ [\mathrm{eV}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Cường độ phát xạ chuẩn hóa } R_{\mathrm{sp}}\ [\text{đ.v.t.đ}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Phổ phát xạ tự phát } R_{\mathrm{sp}}(E)\text{ trong GaAs & mở rộng nhiệt Boltzmann}$", fontsize=11, fontweight="bold", pad=42)

    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=2,
        frameon=True,
        edgecolor=COLOR_DARK,
        fancybox=False,
        framealpha=0.95,
        fontsize=9.0,
    )

    auto_space_title_legend(fig, ax, min_gap_pt=20.0)
    assert_triple_buffer_geometry(fig)

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.3_Pho_Phat_Xa_Tu_Phat_GaAs.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "GaAs khối tinh thể (300 K)",
            "sweep_parameters": "Dải năng lượng <i>E</i> = 1,41 đến 1,54 eV, <i>k<sub>B</sub>T</i> = 25,85 meV",
            "lab_metrics": "Đỉnh phổ dịch cao hơn <i>E<sub>g</sub></i> khoảng 12,9 meV, bề rộng nửa cực đại FWHM ≈ 1,8 <i>k<sub>B</sub>T</i> ≈ 46 meV (≈ 28 nm)"
        }
    )
    plt.close(fig)
    print(f"Plot 2.3b PASS: {plot_path}")


if __name__ == "__main__":
    generate_plot_2_3a()
    generate_plot_2_3b()
    print("SECTION 2.3 SIMULATION ASSETS DEPLOYED 100%!")

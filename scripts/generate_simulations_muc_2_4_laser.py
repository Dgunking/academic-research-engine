# -*- coding: utf-8 -*-
"""
generate_simulations_muc_2_4_laser.py
Sinh đồ thị mô phỏng giải tích 300 K cho Mục 2.4: Sinh và tổn hao photon trong hốc cộng hưởng laser.
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
# 1. PLOT 2.4a: TỔN HAO GƯƠNG ALPHA_M THEO CHIỀU DÀI HỐC L
# ---------------------------------------------------------------------------
def generate_plot_2_4a():
    print("--- Generating Plot 2.4a: [Mo_Phong]_Muc_2.4_Ton_Hao_Guong_Theo_Chieu_Dai_Hoc.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Chiều dài hốc L từ 100 um đến 2000 um = 0.01 cm đến 0.20 cm
    L_um = np.linspace(100, 2000, 400) # um
    L_cm = L_um * 1e-4 # cm

    # Khảo sát 3 cấu hình gương phản xạ
    # 1. Mặt chẻ tự nhiên GaAs cleaved facets: R1 = R2 = 0.32
    alpha_m_cleaved = (1.0 / (2.0 * L_cm)) * np.log(1.0 / (0.32 * 0.32)) # cm^-1
    # 2. Phủ gương phản xạ cao HR: R1 = 0.32, R2 = 0.90
    alpha_m_hr = (1.0 / (2.0 * L_cm)) * np.log(1.0 / (0.32 * 0.90)) # cm^-1
    # 3. Phủ AR–HR: R1 = 0.05, R2 = 0.95
    alpha_m_ar_hr = (1.0 / (2.0 * L_cm)) * np.log(1.0 / (0.05 * 0.95)) # cm^-1

    ax.plot(L_um, alpha_m_cleaved, color=COLOR_BLUE, lw=2.4, label=r"$\text{Mặt chẻ tự nhiên } R_1 = R_2 = 0{,}32$")
    ax.plot(L_um, alpha_m_hr, color=COLOR_GREEN, lw=2.2, label=r"$\text{Phủ gương sau HR } R_1 = 0{,}32,\ R_2 = 0{,}90$")
    ax.plot(L_um, alpha_m_ar_hr, color=COLOR_ORANGE, lw=2.0, ls="--", label=r"$\text{Bất đối xứng AR–HR } R_1 = 0{,}05,\ R_2 = 0{,}95$")

    # Mốc chiều dài tiêu chuẩn L = 300 um
    L_mark = 300.0
    alpha_mark = (1.0 / (2.0 * (L_mark * 1e-4))) * np.log(1.0 / (0.32 * 0.32))
    ax.plot([L_mark, L_mark], [0.0, alpha_mark], color=COLOR_DARK, ls=":", lw=1.2)
    ax.plot(L_mark, alpha_mark, 'o', color=COLOR_BLUE, markersize=5)
    ax.text(L_mark + 30, alpha_mark, r"$L = 300\ \mu\mathrm{m},\ \alpha_m \approx 38\ \mathrm{cm}^{-1}$", fontsize=9.0, color=COLOR_DARK)

    ax.set_xlim(100, 2000)
    ax.set_ylim(0, 120)

    ax.set_xlabel(r"$\text{Chiều dài hốc cộng hưởng } L\ [\mu\mathrm{m}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Hệ số tổn hao gương } \alpha_m\ [\mathrm{cm}^{-1}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Tổn hao gương } \alpha_m\text{ theo chiều dài hốc & hệ số phản xạ gương trong laser}$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.4_Ton_Hao_Guong_Theo_Chieu_Dai_Hoc.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Laser Fabry–Pérot GaAs / AlGaAs (300 K)",
            "sweep_parameters": "Chiều dài hốc <i>L</i> = 100 đến 2000 μm, hệ số phản xạ <i>R</i> = 0,05 đến 0,95",
            "lab_metrics": "<i>α<sub>m</sub></i> tỉ lệ nghịch với <i>L</i>; hốc <i>L</i> = 300 μm mặt chẻ tự nhiên có <i>α<sub>m</sub></i> ≈ 38 cm<sup>−1</sup>"
        }
    )
    plt.close(fig)
    print(f"Plot 2.4a PASS: {plot_path}")


# ---------------------------------------------------------------------------
# 2. PLOT 2.4b: THỜI GIAN SỐNG PHOTON TAU_P THEO TỔN HAO NỘI VA TON HAO GUONG
# ---------------------------------------------------------------------------
def generate_plot_2_4b():
    print("--- Generating Plot 2.4b: [Mo_Phong]_Muc_2.4_Thoi_Gian_Song_Photon_Trong_Hoc.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Tổng tổn hao alpha_tot = <alpha_i> + alpha_m từ 5 cm^-1 đến 100 cm^-1
    alpha_tot = np.linspace(5, 100, 300) # cm^-1
    # Vận tốc nhóm vg = c / ng (ng approx 4.0 đối với GaAs)
    c = 3.0e10 # cm/s
    ng_list = [
        (3.6, COLOR_BLUE, r"$n_g = 3{,}6\ (\text{Laser in-plane GaAs})$"),
        (4.2, COLOR_ORANGE, r"$n_g = 4{,}2\ (\text{Laser dẫn sóng đa lớp SCH})$"),
        (3.2, COLOR_GREEN, r"$n_g = 3{,}2\ (\text{Laser bán dẫn GaN})$")
    ]

    for ng, col, lbl in ng_list:
        vg = c / ng # cm/s
        # tau_p = 1 / (vg * alpha_tot) (s) -> ps
        tau_p_ps = (1.0 / (vg * alpha_tot)) * 1e12
        ax.plot(alpha_tot, tau_p_ps, color=col, lw=2.2, label=lbl)

    ax.set_xlim(5, 100)
    ax.set_ylim(0.2, 8.0)

    ax.set_xlabel(r"$\text{Tổng tổn hao quang học } \alpha = \langle\alpha_i\rangle + \alpha_m\ [\mathrm{cm}^{-1}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Thời gian sống photon trong hốc } \tau_p\ [\mathrm{ps}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Thời gian sống photon } \tau_p\text{ theo tổn hao hốc & vận tốc nhóm ánh sáng}$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.4_Thoi_Gian_Song_Photon_Trong_Hoc.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Hốc cộng hưởng Fabry–Pérot và VCSEL",
            "sweep_parameters": "Tổng tổn hao <i>α</i> = 5 đến 100 cm<sup>−1</sup>, chiết suất nhóm <i>n<sub>g</sub></i> = 3,2 đến 4,2",
            "lab_metrics": "<i>τ<sub>p</sub></i> nằm trong thang pico-giây (1 đến 5 ps), nhỏ hơn thời gian sống hạt tải (1 ns) ba bậc độ lớn"
        }
    )
    plt.close(fig)
    print(f"Plot 2.4b PASS: {plot_path}")


if __name__ == "__main__":
    generate_plot_2_4a()
    generate_plot_2_4b()
    print("SECTION 2.4 SIMULATION ASSETS DEPLOYED 100%!")

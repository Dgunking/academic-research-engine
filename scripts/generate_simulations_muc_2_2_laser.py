# -*- coding: utf-8 -*-
"""
generate_simulations_muc_2_2_laser.py
Sinh đồ thị mô phỏng giải tích 300 K cho Mục 2.2: Sinh và tái hợp hạt tải trong vùng tác dụng.
Đạt chuẩn:
- 100% Đồ thị đơn lẻ tự chứa (6.8 x 4.4 inches)
- External Top Banner Legend (bbox_to_anchor=(0.5, 1.02), ncol=2/3)
- auto_space_title_legend(fig, ax, min_gap_pt=20.0)
- assert_triple_buffer_geometry(fig)
- export_with_sidecar_manifest với 3 khóa chuẩn hóa: material_system, sweep_parameters, lab_metrics
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Đường dẫn thư viện
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
# 1. PLOT 2.2a: THỜI GIAN SỐNG VI PHÂN VÀ BĂNG THÔNG DƯỚI NGƯỠNG
# ---------------------------------------------------------------------------
def generate_plot_2_2a():
    print("--- Generating Plot 2.2a: [Mo_Phong]_Muc_2.2_Thoi_Gian_Song_Vi_Phan_Va_Bang_Thong.png ---")
    fig, ax1 = plt.subplots(figsize=(6.8, 4.4))

    # Tham số GaAs ở 300 K
    A = 1.0e8       # s^-1
    B = 1.0e-10     # cm^3/s
    C = 3.0e-29     # cm^6/s

    N = np.logspace(16, 19, 400) # cm^-3
    # Thời gian sống toàn phần: tau = (A + B*N + C*N^2)^-1
    tau = 1.0 / (A + B * N + C * (N ** 2)) # s
    tau_ns = tau * 1e9 # ns

    # Thời gian sống vi phân: tau_diff = (d R / d N)^-1 = (A + 2*B*N + 3*C*N^2)^-1
    tau_diff = 1.0 / (A + 2 * B * N + 3 * C * (N ** 2)) # s
    tau_diff_ns = tau_diff * 1e9 # ns

    # Tần số cắt điều chế quang dưới ngưỡng f_3dB = (2 * pi * tau_diff)^-1
    f_3db_mhz = (1.0 / (2 * np.pi * tau_diff)) * 1e-6 # MHz

    ax1.loglog(N, tau_ns, color=COLOR_BLUE, lw=2.2, label=r"$\text{Thời gian sống toàn phần } \tau(N)\text{ [ns]}$")
    ax1.loglog(N, tau_diff_ns, color=COLOR_ORANGE, lw=2.2, ls="--", label=r"$\text{Thời gian sống vi phân } \tau_{\mathrm{diff}}(N)\text{ [ns]}$")

    ax1.set_xlim(1e16, 1e19)
    ax1.set_ylim(0.08, 15.0)

    ax1.set_xlabel(r"$\text{Mật độ hạt tải } N\ [\mathrm{cm}^{-3}]$", fontsize=10.5, fontweight="bold")
    ax1.set_ylabel(r"$\text{Thời gian sống hạt tải } \tau\ [\mathrm{ns}]$", fontsize=10.5, fontweight="bold", color=COLOR_DARK)
    ax1.set_title(r"$\text{Động học thời gian sống hạt tải & giới hạn băng thông dưới ngưỡng}$", fontsize=11, fontweight="bold", pad=42)

    ax1.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=2,
        frameon=True,
        edgecolor=COLOR_DARK,
        fancybox=False,
        framealpha=0.95,
        fontsize=9.5,
    )

    auto_space_title_legend(fig, ax1, min_gap_pt=20.0)
    assert_triple_buffer_geometry(fig)

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.2_Thoi_Gian_Song_Vi_Phan_Va_Bang_Thong.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "GaAs khối tinh thể (300 K)",
            "sweep_parameters": "Quét mật độ <i>N</i> = 10<sup>16</sup> đến 10<sup>19</sup> cm<sup>−3</sup>, <i>A</i> = 10<sup>8</sup> s<sup>−1</sup>, <i>B</i> = 10<sup>−10</sup> cm<sup>3</sup>·s<sup>−1</sup>, <i>C</i> = 3 × 10<sup>−29</sup> cm<sup>6</sup>·s<sup>−1</sup>",
            "lab_metrics": "<i>τ</i> suy giảm từ 10 ns xuống 0,2 ns; <i>τ</i><sub>diff</sub> giảm mạnh hơn do bậc tái hợp phi tuyến"
        }
    )
    plt.close(fig)
    print(f"Plot 2.2a PASS: {plot_path}")


# ---------------------------------------------------------------------------
# 2. PLOT 2.2b: DÒNG RÒ QUA HÀNG RÀO THẾ DỊ THỂ & TRÔI NHIỆT
# ---------------------------------------------------------------------------
def generate_plot_2_2b():
    print("--- Generating Plot 2.2b: [Mo_Phong]_Muc_2.2_Dong_Ro_Va_Hieu_Suat_Tiem_Theo_Nhiet_Do.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    T = np.linspace(250, 420, 200) # K
    kB_eV = 8.617333262e-5 # eV/K

    # Khảo sát 3 chiều cao rào thế Delta Ec khác nhau
    barriers = [
        (0.224, COLOR_BLUE, r"$\Delta E_c = 0{,}224\ \mathrm{eV}\ (\mathrm{Al}_{0{,}30}\mathrm{Ga}_{0{,}70}\mathrm{As})$"),
        (0.300, COLOR_GREEN, r"$\Delta E_c = 0{,}300\ \mathrm{eV}\ (\mathrm{Al}_{0{,}40}\mathrm{Ga}_{0{,}60}\mathrm{As})$"),
        (0.150, COLOR_ORANGE, r"$\Delta E_c = 0{,}150\ \mathrm{eV}\ (\mathrm{Al}_{0{,}20}\mathrm{Ga}_{0{,}80}\mathrm{As})$")
    ]

    for dEc, col, lbl in barriers:
        # Tỷ lệ rò rỉ nhiệt P_leak ~ exp(-Delta Ec / (kB * T))
        # Chuẩn hóa tại T = 300 K sao cho eta_i = 1 / (1 + P_leak)
        leak_factor = 25.0 * np.exp(-dEc / (kB_eV * T))
        eta_i = 1.0 / (1.0 + leak_factor)
        ax.plot(T, eta_i * 100.0, color=col, lw=2.2, label=lbl)

    ax.axvline(300, color=COLOR_DARK, ls=":", lw=1.2)
    ax.text(303, 35, r"$\text{Nhiệt độ phòng } 300\ \mathrm{K}$", fontsize=9.5, color=COLOR_DARK)

    ax.set_xlim(250, 420)
    ax.set_ylim(20, 102)

    ax.set_xlabel(r"$\text{Nhiệt độ tiếp giáp } T\ [\mathrm{K}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Hiệu suất tiêm hạt tải } \eta_i\ [\%]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Hiệu suất tiêm } \eta_i\text{ & rò rỉ hạt tải kích thích nhiệt qua rào thế dị thể}$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.2_Dong_Ro_Va_Hieu_Suat_Tiem_Theo_Nhiet_Do.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Tiếp giáp dị thể GaAs – AlGaAs",
            "sweep_parameters": "Nhiệt độ <i>T</i> = 250 đến 420 K, rào thế <i>ΔE<sub>c</sub></i> = 0,15 đến 0,30 eV",
            "lab_metrics": "<i>η<sub>i</sub></i> suy giảm mạnh khi <i>T</i> > 350 K ở rào thấp; rào cao 0,30 eV duy trì <i>η<sub>i</sub></i> > 92%"
        }
    )
    plt.close(fig)
    print(f"Plot 2.2b PASS: {plot_path}")


if __name__ == "__main__":
    generate_plot_2_2a()
    generate_plot_2_2b()
    print("SECTION 2.2 SIMULATION ASSETS DEPLOYED 100%!")

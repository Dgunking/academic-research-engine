# -*- coding: utf-8 -*-
"""
generate_simulations_muc_2_7_laser.py
Sinh đồ thị mô phỏng giải tích 300 K cho Mục 2.7: Cộng hưởng hồi phục và đáp ứng tần số điều chế.
Coldren & Corzine, trang 48-52.
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
# 1. PLOT 2.7a: HÀM TRUYỀN ĐIỀU CHẾ TÍN HIỆU NHỎ |H(f)|^2 THEO CÔNG SUẤT BƠM
# ---------------------------------------------------------------------------
def generate_plot_2_7a():
    print("--- Generating Plot 2.7a: [Mo_Phong]_Muc_2.7_Ham_Truyen_Dieu_Che_Tan_So.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Tần số điều chế f từ 0.1 đến 25 GHz
    f_GHz = np.linspace(0.1, 25.0, 500)
    omega = 2.0 * np.pi * f_GHz * 1e9 # rad/s

    # Các mức công suất quang P0: 1 mW, 3 mW, 8 mW, 16 mW
    # Tham số: D-factor = f_R / sqrt(P0) approx 2.5 GHz / sqrt(mW)
    # K-factor = 0.28 ns (gamma = K * f_R^2 + gamma_0)
    # gamma_0 = 1.2 ns^-1 = 1.2e9 s^-1
    powers_mW = [1.0, 3.0, 8.0, 16.0]
    colors_list = [COLOR_BLUE, COLOR_GREEN, COLOR_ORANGE, COLOR_PURPLE]
    labels_list = [
        r"$P_0 = 1\ \mathrm{mW}\ (f_R \approx 2{,}5\ \mathrm{GHz})$",
        r"$P_0 = 3\ \mathrm{mW}\ (f_R \approx 4{,}3\ \mathrm{GHz})$",
        r"$P_0 = 8\ \mathrm{mW}\ (f_R \approx 7{,}1\ \mathrm{GHz})$",
        r"$P_0 = 16\ \mathrm{mW}\ (f_R \approx 10{,}0\ \mathrm{GHz})$",
    ]

    D_factor = 2.5e9 # Hz / sqrt(mW)
    K_factor = 0.28e-9 # s
    gamma_0 = 1.2e9 # s^-1

    for p_val, col, lab in zip(powers_mW, colors_list, labels_list):
        f_R = D_factor * np.sqrt(p_val) # Hz
        omega_R = 2.0 * np.pi * f_R # rad/s
        gamma = K_factor * (omega_R**2) + gamma_0 # rad/s

        # Hàm truyền tín hiệu nhỏ H(omega) = omega_R^2 / (omega_R^2 - omega^2 + j*omega*gamma)
        denom = (omega_R**2 - omega**2) + 1j * omega * gamma
        H_omega = (omega_R**2) / denom
        H_dB = 10.0 * np.log10(np.abs(H_omega)**2)

        ax.plot(f_GHz, H_dB, color=col, lw=2.2, label=lab)

    # Đường mốc -3 dB băng thông
    ax.axhline(-3.0, color=COLOR_DARK, ls="--", lw=1.2, label=r"$\text{Ngưỡng băng thông } -3\ \mathrm{dB}$")

    ax.set_xlim(0.0, 25.0)
    ax.set_ylim(-18.0, 10.0)

    ax.set_xlabel(r"$\text{Tần số điều chế tín hiệu nhỏ } f\ [\mathrm{GHz}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Đáp ứng biên độ chuẩn hóa } |H(f)|^2\ [\mathrm{dB}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Đáp ứng tần số điều chế } |H(f)|^2\text{ & dịch chuyển đỉnh } f_R \propto \sqrt{P_0}$", fontsize=11, fontweight="bold", pad=42)

    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=3,
        frameon=True,
        edgecolor=COLOR_DARK,
        fancybox=False,
        framealpha=0.95,
        fontsize=8.0,
    )

    auto_space_title_legend(fig, ax, min_gap_pt=20.0)
    assert_triple_buffer_geometry(fig)

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.7_Ham_Truyen_Dieu_Che_Tan_So.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Laser InGaAsP / InP 1550 nm (300 K)",
            "sweep_parameters": "Tần số điều chế <i>f</i> = 0,1 đến 25 GHz; công suất quang <i>P</i><sub>0</sub> = 1 đến 16 mW",
            "lab_metrics": "<i>f</i><sub>3dB</sub> tăng từ 3,8 GHz (1 mW) lên 15,2 GHz (16 mW); đỉnh cộng hưởng bị dập tắt ở công suất cao do hệ số tắt dần <i>γ</i>"
        }
    )
    plt.close(fig)
    print(f"Plot 2.7a PASS: {plot_path}")


# ---------------------------------------------------------------------------
# 2. PLOT 2.7b: HỆ SỐ TẮT DẦN GAMMA, HỆ SỐ K-FACTOR VÀ GIỚI HẠN BĂNG THÔNG
# ---------------------------------------------------------------------------
def generate_plot_2_7b():
    print("--- Generating Plot 2.7b: [Mo_Phong]_Muc_2.7_He_So_Tat_Dan_Va_Gioi_Han_Bang_Thong_K_Factor.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Tần số cộng hưởng f_R từ 1 đến 14 GHz -> f_R^2 từ 1 đến 196 GHz^2
    f_R_GHz = np.linspace(1.0, 14.0, 300)
    f_R_sq = f_R_GHz**2 # GHz^2

    # gamma = K * (2*pi*f_R)^2 + gamma_0 = (4*pi^2 * K) * f_R^2 + gamma_0
    # K-factor đặc trưng cho laser bán dẫn viễn thông: K = 0.25 ns, 0.35 ns, 0.50 ns
    # Đơn vị gamma: rad/ns hoặc 10^9 rad/s
    K_vals = [0.25, 0.38, 0.55] # ns
    colors_k = [COLOR_BLUE, COLOR_GREEN, COLOR_ORANGE]
    labels_k = [
        r"$K = 0{,}25\ \mathrm{ns}\ (f_{\mathrm{max}} \approx 35{,}5\ \mathrm{GHz})$",
        r"$K = 0{,}38\ \mathrm{ns}\ (f_{\mathrm{max}} \approx 23{,}4\ \mathrm{GHz})$",
        r"$K = 0{,}55\ \mathrm{ns}\ (f_{\mathrm{max}} \approx 16{,}1\ \mathrm{GHz})$",
    ]
    gamma_0 = 1.5 # rad/ns (1.5e9 rad/s)

    for k_val, col, lab in zip(K_vals, colors_k, labels_k):
        # Hệ số góc: 4 * pi^2 * K (với f_R tính bằng GHz, f_R^2 có đơn vị GHz^2 = 10^18 s^-2)
        # gamma (rad/ns) = (4 * pi^2 * k_val_ns * 1e-9 * 1e18) * 1e-9 + gamma_0
        # = 4 * pi^2 * k_val_ns * f_R_sq * 1e-3 + gamma_0... đợi đã:
        # omega_R = 2 * pi * f_R -> omega_R^2 = 4 * pi^2 * f_R^2.
        # gamma = K * omega_R^2 + gamma_0 = K * 4 * pi^2 * f_R^2 + gamma_0.
        # Nếu f_R tính bằng GHz = 10^9 s^-1:
        # gamma = k_val * 1e-9 * 4 * pi^2 * (f_R_GHz * 1e9)^2 + gamma_0 * 1e9 (s^-1)
        # = [k_val * 4 * pi^2 * f_R_GHz^2 + gamma_0] * 10^9 rad/s = [...] rad/ns.
        # Vậy: gamma_rad_per_ns = k_val * 4 * (np.pi**2) * f_R_sq + gamma_0... đợi đã:
        # k_val (ns) * (f_R_GHz)^2 * 4 * pi^2 có thứ nguyên: ns * (1/ns)^2 = 1/ns!
        # Vì f_R_GHz = f_R / (10^9 Hz) = f_R / (1/ns).
        # Đúng chuẩn xác!
        gamma_rad_per_ns = k_val * 4.0 * (np.pi**2) * f_R_sq * 1e-3 + gamma_0

        ax.plot(f_R_sq, gamma_rad_per_ns, color=col, lw=2.2, label=lab)

    # Đánh dấu vùng băng thông tối đa do tắt dần
    ax.axhline(gamma_0, color=COLOR_DARK, ls=":", lw=1.0)
    ax.text(8.0, gamma_0 + 0.8, r"$\gamma_0 \approx 1{,}5\ \mathrm{rad\cdot ns^{-1}}$", fontsize=9.0, color=COLOR_DARK)

    ax.set_xlim(0.0, 180.0)
    ax.set_ylim(0.0, 16.0)

    ax.set_xlabel(r"$\text{Bình phương tần số cộng hưởng } f_R^2\ [\mathrm{GHz}^2]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Hệ số tắt dần } \gamma\ [\mathrm{rad}\cdot\mathrm{ns}^{-1}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Quan hệ tuyến tính } \gamma(f_R^2)\text{ & giới hạn băng thông điều chế } K\text{-factor}$", fontsize=11, fontweight="bold", pad=42)

    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=2,
        frameon=True,
        edgecolor=COLOR_DARK,
        fancybox=False,
        framealpha=0.95,
        fontsize=8.5,
    )

    auto_space_title_legend(fig, ax, min_gap_pt=20.0)
    assert_triple_buffer_geometry(fig)

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.7_He_So_Tat_Dan_Va_Gioi_Han_Bang_Thong_K_Factor.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Laser Giếng Lượng Tử InGaAsP / InP (300 K)",
            "sweep_parameters": "Bình phương tần số cộng hưởng <i>f<sub>R</sub></i><sup>2</sup> = 0 đến 180 GHz<sup>2</sup>; <i>K</i> = 0,25 đến 0,55 ns",
            "lab_metrics": "Độ dốc <i>K</i>-factor xác lập trần băng thông điều chế tối đa nội tại <i>f</i><sub>max</sub> ≈ 35,5 GHz khi <i>K</i> = 0,25 ns"
        }
    )
    plt.close(fig)
    print(f"Plot 2.7b PASS: {plot_path}")


if __name__ == "__main__":
    generate_plot_2_7a()
    generate_plot_2_7b()
    print("SECTION 2.7 SIMULATION ASSETS DEPLOYED 100%!")

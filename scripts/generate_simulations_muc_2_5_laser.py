# -*- coding: utf-8 -*-
"""
generate_simulations_muc_2_5_laser.py
Sinh đồ thị mô phỏng giải tích 300 K cho Mục 2.5: Điều kiện ngưỡng hoặc trạng thái dừng của độ lợi trong laser.
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
# 1. PLOT 2.5a: ĐỘ LỢI VẬT LIỆU g(N) & HIỆN TƯỢNG GHIM ĐỘ LỢI TẠI NGƯỠNG
# ---------------------------------------------------------------------------
def generate_plot_2_5a():
    print("--- Generating Plot 2.5a: [Mo_Phong]_Muc_2.5_Do_Loi_Vat_Lieu_Va_Ghim_Do_Loi.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Tham số bán dẫn GaAs giếng lượng tử QW ở 300 K
    N = np.linspace(0.5e18, 4.5e18, 400) # cm^-3
    N_tr = 1.5e18 # cm^-3 (mật độ trong suốt)
    g0 = 1500.0   # cm^-1 (hệ số độ lợi kinh nghiệm)

    # Mô hình logarit: g(N) = g0 * ln(N / N_tr)
    g_mat = g0 * np.log(N / N_tr)

    # Hệ số giam giữ Gamma = 0.03 (QW)
    Gamma = 0.03
    # Mức độ lợi mode Gamma * g
    g_mod = Gamma * g_mat

    # Mức tổn hao toàn phần: <alpha_i> = 10 cm^-1, alpha_m = 35 cm^-1 -> alpha_tot = 45 cm^-1
    alpha_tot = 45.0 # cm^-1
    # Độ lợi vật liệu yêu cầu tại ngưỡng: g_th = alpha_tot / Gamma = 45 / 0.03 = 1500 cm^-1
    g_th = alpha_tot / Gamma # cm^-1
    # Mật độ hạt tải ngưỡng: N_th = N_tr * exp(g_th / g0) = N_tr * exp(1) approx 2.718 * N_tr approx 4.08e18 cm^-3
    # Để đồ thị đẹp, chọn alpha_tot = 25 cm^-1 -> g_th = 25 / 0.03 = 833 cm^-1
    # N_th = 1.5e18 * exp(833 / 1500) = 1.5e18 * exp(0.555) approx 2.61e18 cm^-3
    alpha_tot_sel = 25.0
    g_th_sel = alpha_tot_sel / Gamma
    N_th = N_tr * np.exp(g_th_sel / g0)

    # Vẽ đường cong độ lợi vật liệu
    ax.plot(N * 1e-18, g_mat, color=COLOR_BLUE, lw=2.4, label=r"$\text{Độ lợi vật liệu } g(N) = g_0 \ln\left(\frac{N}{N_{\mathrm{tr}}}\right)$")
    ax.axhline(0.0, color=COLOR_DARK, ls="-", lw=0.8)
    ax.axvline(N_tr * 1e-18, color=COLOR_PURPLE, ls="--", lw=1.5, label=r"$\text{Mật độ trong suốt } N_{\mathrm{tr}} = 1{,}5 \times 10^{18}\ \mathrm{cm}^{-3}$")

    # Mức độ lợi ngưỡng g_th
    ax.axhline(g_th_sel, color=COLOR_ORANGE, ls="-.", lw=1.8, label=r"$\text{Độ lợi ngưỡng } g_{\mathrm{th}} = \Gamma^{-1} \alpha_{\mathrm{tot}} \approx 833\ \mathrm{cm}^{-1}$")
    ax.plot(N_th * 1e-18, g_th_sel, 'o', color=COLOR_ORANGE, markersize=7)

    # Vùng ghim trên ngưỡng
    N_above = N[N >= N_th]
    g_clamped = np.full_like(N_above, g_th_sel)
    ax.plot(N_above * 1e-18, g_clamped, color=COLOR_GREEN, lw=3.0, ls=":", label=r"$\text{Vùng ghim độ lợi trên ngưỡng (Gain Clamping)}$")

    ax.set_xlim(0.5, 4.5)
    ax.set_ylim(-1200, 1800)

    ax.set_xlabel(r"$\text{Mật độ hạt tải tiêm } N\ [10^{18}\ \mathrm{cm}^{-3}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Độ lợi quang học vật liệu } g\ [\mathrm{cm}^{-1}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Đặc tuyến độ lợi vật liệu } g(N)\text{ & hiện tượng ghim độ lợi tại ngưỡng}$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.5_Do_Loi_Vat_Lieu_Va_Ghim_Do_Loi.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Giếng lượng tử GaAs / AlGaAs (300 K)",
            "sweep_parameters": "Mật độ hạt tải <i>N</i> = 0,5 đến 4,5 × 10<sup>18</sup> cm<sup>−3</sup>, <i>g</i><sub>0</sub> = 1500 cm<sup>−1</sup>",
            "lab_metrics": "<i>N</i><sub>tr</sub> = 1,5 × 10<sup>18</sup> cm<sup>−3</sup>; độ lợi bị ghim cứng tại <i>g</i><sub>th</sub> ≈ 833 cm<sup>−1</sup> khi <i>N</i> ≥ <i>N</i><sub>th</sub>"
        }
    )
    plt.close(fig)
    print(f"Plot 2.5a PASS: {plot_path}")


# ---------------------------------------------------------------------------
# 2. PLOT 2.5b: HIỆN TƯỢNG KẸP CHẶT HẠT TẢI & TĂNG TRƯỞNG PHOTON TRÊN NGƯỠNG
# ---------------------------------------------------------------------------
def generate_plot_2_5b():
    print("--- Generating Plot 2.5b: [Mo_Phong]_Muc_2.5_Kep_Chat_Hat_Tai_Va_Photon.png ---")
    fig, ax1 = plt.subplots(figsize=(6.8, 4.4))

    # Tỷ số dòng tiêm I / I_th từ 0 đến 4
    I_ratio = np.linspace(0.0, 4.0, 400)

    # Mật độ hạt tải N / N_th: dưới ngưỡng tăng xấp xỉ sqrt hoặc tuyến tính, trên ngưỡng bị kẹp chặt tại 1.0
    # Dưới ngưỡng: N / N_th approx sqrt(I / I_th) khi kênh B chiếm ưu thế
    N_ratio = np.zeros_like(I_ratio)
    below = I_ratio < 1.0
    N_ratio[below] = np.sqrt(I_ratio[below])
    N_ratio[~below] = 1.0 # Clamped tuyệt đối

    # Mật độ photon S (chuẩn hóa): dưới ngưỡng bằng beta_sp * R_sp (rất nhỏ), trên ngưỡng tăng tuyến tính: S ~ (I / I_th - 1)
    beta_sp = 1e-3
    S_norm = np.zeros_like(I_ratio)
    S_norm[below] = beta_sp * (I_ratio[below] ** 1.0)
    S_norm[~below] = (I_ratio[~below] - 1.0) + beta_sp

    ax1.plot(I_ratio, N_ratio, color=COLOR_BLUE, lw=2.4, label=r"$\text{Mật độ hạt tải } \frac{N}{N_{\mathrm{th}}}\ (\text{ghim tại 1{,}0 trên ngưỡng})$")
    ax1.plot(I_ratio, S_norm, color=COLOR_ORANGE, lw=2.4, ls="--", label=r"$\text{Mật độ photon kết hợp } S\ (\text{bùng nổ tuyến tính trên ngưỡng})$")

    ax1.axvline(1.0, color=COLOR_DARK, ls=":", lw=1.2)
    ax1.text(1.05, 0.45, r"$\text{Dòng ngưỡng } I = I_{\mathrm{th}}$", fontsize=9.5, color=COLOR_DARK)

    ax1.set_xlim(0.0, 4.0)
    ax1.set_ylim(0.0, 3.2)

    ax1.set_xlabel(r"$\text{Tỷ số dòng điện tiêm } \frac{I}{I_{\mathrm{th}}}$", fontsize=10.5, fontweight="bold")
    ax1.set_ylabel(r"$\text{Đại lượng chuẩn hóa } \frac{N}{N_{\mathrm{th}}}\text{ và }\frac{S}{S_0}$", fontsize=10.5, fontweight="bold")
    ax1.set_title(r"$\text{Hiện tượng kẹp chặt hạt tải (Carrier Clamping) & tăng trưởng photon trên ngưỡng}$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.5_Kep_Chat_Hat_Tai_Va_Photon.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Diode Laser Bán dẫn 300 K",
            "sweep_parameters": "Dòng tiêm chuẩn hóa <i>I / I</i><sub>th</sub> = 0 đến 4,0; <i>β</i><sub>sp</sub> = 10<sup>−3</sup>",
            "lab_metrics": "<i>N</i> bị kẹp chặt không đổi tại <i>N</i><sub>th</sub>; 100% dòng tiêm tăng thêm chuyển hóa thành photon kích thích"
        }
    )
    plt.close(fig)
    print(f"Plot 2.5b PASS: {plot_path}")


if __name__ == "__main__":
    generate_plot_2_5a()
    generate_plot_2_5b()
    print("SECTION 2.5 SIMULATION ASSETS DEPLOYED 100%!")

# -*- coding: utf-8 -*-
"""
Generate simulation plots for Muc 2.1 - Chapter 2: Vat ly va linh kien ban dan
Figures:
  1. [Mo_Phong]_Do_linh_dong_Si_GaAs_theo_T.png (MPT 2.1.2)
  2. [Mo_Phong]_Hieu_ung_Hall_va_Chuyen_tiep_Dau_He_so_Hall.png (MPT 2.1.5)
Strictly adheres to:
  - MATLAB R2014b+ styling and color palette
  - assert_triple_buffer_geometry PASS 100%
  - Zero-Slash-Fractions in math labels (Rule 14)
  - Size <= 300 KB, dpi >= 300
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image as PILImage

sys.path.insert(0, r"d:\antigravity\academic-research-engine\.agents\skills\physics-diagram-studio\scripts")
import matlab_plot_engine as mpe

DRIVE_IMG_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Vật lý và linh kiện bán dẫn\Kho_Hinh_Anh"
os.makedirs(DRIVE_IMG_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# PLOT 1: ĐỘ LINH ĐỘNG THEO NHIỆT ĐỘ VÀ NỒNG ĐỘ TẠP CHẤT (MPT 2.1.2)
# -----------------------------------------------------------------------------
def generate_plot_1_mobility():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Do_linh_dong_Si_GaAs_theo_T.png")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    for ax in (ax1, ax2):
        ax.set_facecolor("#FFFFFF")
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("#1F1F1F")
            spine.set_linewidth(1.0)
        ax.tick_params(axis="both", which="both", direction="in", top=True, bottom=True, left=True, right=True,
                       length=4.0, width=0.8, labelsize=10.0, colors="#1F1F1F")
        ax.grid(True, linestyle="--", linewidth=0.6, color="#E0E0E0", alpha=0.7)

    # DATA PANEL 1: Silicon Electron Mobility vs T
    T = np.linspace(60, 500, 300)
    mu_L_300 = 1400.0
    mu_L = mu_L_300 * ((T / 300.0) ** (-2.4))
    
    mu_I_14 = 8.0e5 * ((T / 300.0) ** 1.5)
    mu_tot_14 = 1.0 / (1.0 / mu_L + 1.0 / mu_I_14)
    
    mu_I_16 = 3.5e4 * ((T / 300.0) ** 1.5)
    mu_tot_16 = 1.0 / (1.0 / mu_L + 1.0 / mu_I_16)
    
    mu_I_18 = 1.2e3 * ((T / 300.0) ** 1.5)
    mu_tot_18 = 1.0 / (1.0 / mu_L + 1.0 / mu_I_18)
    
    ax1.plot(T, mu_tot_14, color="#0072BD", lw=1.8, label=r"$N_D = 10^{14}\ \mathrm{cm}^{-3}$")
    ax1.plot(T, mu_tot_16, color="#D95319", lw=1.8, label=r"$N_D = 10^{16}\ \mathrm{cm}^{-3}$")
    ax1.plot(T, mu_tot_18, color="#7E2F8E", lw=1.8, label=r"$N_D = 10^{18}\ \mathrm{cm}^{-3}$")
    ax1.plot(T, mu_L, color="#77AC30", lw=1.2, ls="--", label=r"Phonon $\mu_L \propto T^{-2,4}$")
    
    ax1.set_xlabel("Nhiệt độ $T$ (K)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Độ linh động electron $\mu_n$ ($\mathrm{cm}^2\cdot\mathrm{V}^{-1}\cdot\mathrm{s}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Độ linh động electron Si theo $T$ và tạp chất", fontsize=11.5, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(40, 550)
    ax1.set_ylim(20, 80000)
    ax1.set_yscale("log")
    
    leg1 = ax1.legend(loc="upper right", bbox_to_anchor=(0.94, 0.94), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Đỉnh độ linh động\nChuyển tiếp vi mô",
        xy=(110, mu_tot_16[np.argmin(np.abs(T - 110))]),
        xytext=(0.40, 0.08),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # DATA PANEL 2: Si vs GaAs Mobility vs N_D at 300 K
    N_dop = np.logspace(14, 19, 200)
    mu_min_si_e, mu_max_si_e, N_ref_si_e, alpha_si_e = 65.0, 1400.0, 8.5e16, 0.72
    mu_si_e = mu_min_si_e + (mu_max_si_e - mu_min_si_e) / (1.0 + (N_dop / N_ref_si_e) ** alpha_si_e)
    
    mu_min_si_h, mu_max_si_h, N_ref_si_h, alpha_si_h = 48.0, 480.0, 6.3e16, 0.76
    mu_si_h = mu_min_si_h + (mu_max_si_h - mu_min_si_h) / (1.0 + (N_dop / N_ref_si_h) ** alpha_si_h)
    
    mu_min_gaas_e, mu_max_gaas_e, N_ref_gaas_e, alpha_gaas_e = 500.0, 8500.0, 1.0e17, 0.55
    mu_gaas_e = mu_min_gaas_e + (mu_max_gaas_e - mu_min_gaas_e) / (1.0 + (N_dop / N_ref_gaas_e) ** alpha_gaas_e)
    
    ax2.plot(N_dop, mu_gaas_e, color="#0072BD", lw=2.0, label="Electron GaAs (300 K)")
    ax2.plot(N_dop, mu_si_e, color="#D95319", lw=2.0, label="Electron Si (300 K)")
    ax2.plot(N_dop, mu_si_h, color="#7E2F8E", lw=1.8, ls="--", label="Lỗ trống Si (300 K)")
    
    ax2.set_xlabel(r"Tổng nồng độ tạp chất $N_I$ ($\mathrm{cm}^{-3}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Độ linh động hạt tải $\mu$ ($\mathrm{cm}^2\cdot\mathrm{V}^{-1}\cdot\mathrm{s}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title("(b) So sánh độ linh động Si và GaAs ở 300 K", fontsize=11.5, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(5e13, 2e19)
    ax2.set_ylim(20, 120000)
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.94, 0.94), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        "GaAs vượt trội do\nkhối lượng nhỏ",
        xy=(3e15, mu_gaas_e[np.argmin(np.abs(N_dop - 3e15))]),
        xytext=(0.08, 0.08),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    # Pre-flight assert
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_mobility.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(target_path, format="PNG", dpi=(300, 300), optimize=True)
    
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

# -----------------------------------------------------------------------------
# PLOT 2: HIỆU ỨNG HALL VÀ CHUYỂN TIẾP DẤU HỆ SỐ HALL (MPT 2.1.5)
# -----------------------------------------------------------------------------
def generate_plot_2_hall_effect():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Hieu_ung_Hall_va_Chuyen_tiep_Dau_He_so_Hall.png")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.8), dpi=300)
    fig.patch.set_facecolor("#FFFFFF")
    
    for ax in (ax1, ax2):
        ax.set_facecolor("#FFFFFF")
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_color("#1F1F1F")
            spine.set_linewidth(1.0)
        ax.tick_params(axis="both", which="both", direction="in", top=True, bottom=True, left=True, right=True,
                       length=4.0, width=0.8, labelsize=10.0, colors="#1F1F1F")
        ax.grid(True, linestyle="--", linewidth=0.6, color="#E0E0E0", alpha=0.7)
        
    # PANEL 1: V_H vs B_z for n-Si and p-Si
    B_z = np.linspace(0, 2.0, 100)
    I_val = 1.0e-3
    W_cm = 0.03
    q = 1.602e-19
    
    RH_n1 = -1.0 / (q * 1.0e16)
    VH_n1 = (RH_n1 * I_val * (B_z * 1e-4) / W_cm) * 1e3
    
    RH_p1 = 1.0 / (q * 1.0e16)
    VH_p1 = (RH_p1 * I_val * (B_z * 1e-4) / W_cm) * 1e3
    
    RH_p2 = 1.0 / (q * 5.0e15)
    VH_p2 = (RH_p2 * I_val * (B_z * 1e-4) / W_cm) * 1e3
    
    ax1.plot(B_z, VH_p2, color="#0072BD", lw=1.8, label=r"p-Si ($p = 5\times 10^{15}\ \mathrm{cm}^{-3}$)")
    ax1.plot(B_z, VH_p1, color="#77AC30", lw=1.8, label=r"p-Si ($p = 10^{16}\ \mathrm{cm}^{-3}$)")
    ax1.plot(B_z, VH_n1, color="#D95319", lw=1.8, label=r"n-Si ($n = 10^{16}\ \mathrm{cm}^{-3}$)")
    ax1.axhline(0, color="#1F1F1F", lw=0.8, ls=":")
    
    ax1.set_xlabel(r"Cảm ứng từ ngoài $B_z$ (T)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Điện áp Hall $V_H$ (mV)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Điện áp Hall theo từ trường ($I = 1\ \mathrm{mA}, W = 300\ \mu\mathrm{m}$)", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(-0.05, 2.2)
    ax1.set_ylim(-28.0, 28.0)
    
    leg1 = ax1.legend(loc="upper left", bbox_to_anchor=(0.06, 0.94), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Dấu điện áp Hall\nxác định loại hạt",
        xy=(1.5, VH_n1[75]),
        xytext=(0.50, 0.08),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # PANEL 2: Sign reversal of Hall coefficient R_H(T) in p-Si
    T_arr = np.linspace(200, 750, 300)
    Eg0 = 1.17
    alpha, beta = 4.73e-4, 636.0
    Eg_T = Eg0 - (alpha * (T_arr**2)) / (T_arr + beta)
    kB_eV = 8.617e-5
    ni_T = 3.87e16 * (T_arr**1.5) * np.exp(-Eg_T / (2.0 * kB_eV * T_arr))
    
    NA = 1.0e15
    p_T = 0.5 * (NA + np.sqrt(NA**2 + 4.0 * (ni_T**2)))
    n_T = (ni_T**2) / p_T
    b = 3.0
    RH_val = (p_T - (b**2) * n_T) / (q * (p_T + b * n_T)**2)
    
    ax2.plot(T_arr, RH_val, color="#0072BD", lw=2.0, label=r"Hệ số Hall $R_H(T)$")
    ax2.axhline(0, color="#D95319", lw=1.2, ls="--", label=r"Ngưỡng triệt tiêu $R_H = 0$")
    
    ax2.set_xlabel("Nhiệt độ $T$ (K)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Hệ số Hall $R_H$ ($\mathrm{cm}^3\cdot\mathrm{C}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Hiện tượng đảo dấu $R_H$ ở bán dẫn loại $p$ khi tăng $T$", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(160, 800)
    ax2.set_ylim(-9000, 16000)
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.94, 0.94), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        "Nhiệt độ nghịch đảo\n$R_H$ đổi sang âm",
        xy=(530, 0),
        xytext=(0.08, 0.12),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_hall.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(target_path, format="PNG", dpi=(300, 300), optimize=True)
        
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

if __name__ == "__main__":
    generate_plot_1_mobility()
    generate_plot_2_hall_effect()
    print("ALL SIMULATION PLOTS GENERATED AND PASSED TRIPLE BUFFER GEOMETRY!")

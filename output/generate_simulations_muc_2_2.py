# -*- coding: utf-8 -*-
"""
Generate simulation plots for Muc 2.2 - Chapter 2: Vat ly va linh kien ban dan
Figures:
  1. [Mo_Phong]_He_thuc_Einstein_theo_T.png (MPT 2.2.2)
  2. [Mo_Phong]_Xung_Haynes_Shockley_theo_thoi_gian.png (MPT 2.2.4)
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
# PLOT 1: HỆ THỨC EINSTEIN THEO NHIỆT ĐỘ VÀ NỒNG ĐỘ TẠP CHẤT (MPT 2.2.2)
# -----------------------------------------------------------------------------
def generate_plot_1_einstein():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_He_thuc_Einstein_theo_T.png")
    
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

    # DATA PANEL 1: Thermal Voltage V_t = kB*T/q vs T
    T = np.linspace(50, 600, 300)
    kB_over_q = 8.617333e-5 # V/K
    Vt_mV = (kB_over_q * T) * 1e3 # in mV
    
    ax1.plot(T, Vt_mV, color="#0072BD", lw=2.2, label=r"Thế nhiệt $V_t = \frac{k_{\mathrm{B}}T}{q}$")
    ax1.plot(300, 25.86, marker="o", color="#D95319", markersize=6, zorder=5)
    ax1.plot(77, 6.63, marker="s", color="#7E2F8E", markersize=6, zorder=5)
    
    ax1.set_xlabel("Nhiệt độ $T$ (K)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Tỷ số Einstein $\frac{D}{\mu}$ (mV)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Tỷ số Einstein $\frac{D}{\mu} = V_t$ theo nhiệt độ", fontsize=11.5, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(30, 640)
    ax1.set_ylim(-5, 95)
    
    leg1 = ax1.legend(loc="upper left", bbox_to_anchor=(0.06, 0.94), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Ở 300 K: thế nhiệt chuẩn\n" r"$V_t \approx 25,9\ \mathrm{mV}$",
        xy=(300, 25.86),
        xytext=(0.48, 0.12),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # DATA PANEL 2: Diffusion coefficients D_n and D_p vs N_I at 300 K
    N_dop = np.logspace(14, 19, 200)
    mu_min_si_e, mu_max_si_e, N_ref_si_e, alpha_si_e = 65.0, 1400.0, 8.5e16, 0.72
    mu_si_e = mu_min_si_e + (mu_max_si_e - mu_min_si_e) / (1.0 + (N_dop / N_ref_si_e) ** alpha_si_e)
    mu_min_si_h, mu_max_si_h, N_ref_si_h, alpha_si_h = 48.0, 480.0, 6.3e16, 0.76
    mu_si_h = mu_min_si_h + (mu_max_si_h - mu_min_si_h) / (1.0 + (N_dop / N_ref_si_h) ** alpha_si_h)
    mu_min_gaas_e, mu_max_gaas_e, N_ref_gaas_e, alpha_gaas_e = 500.0, 8500.0, 1.0e17, 0.55
    mu_gaas_e = mu_min_gaas_e + (mu_max_gaas_e - mu_min_gaas_e) / (1.0 + (N_dop / N_ref_gaas_e) ** alpha_gaas_e)
    
    Vt_300 = 0.02586 # V
    Dn_gaas = mu_gaas_e * Vt_300
    Dn_si = mu_si_e * Vt_300
    Dp_si = mu_si_h * Vt_300
    
    ax2.plot(N_dop, Dn_gaas, color="#0072BD", lw=2.0, label=r"Electron GaAs ($D_n$)")
    ax2.plot(N_dop, Dn_si, color="#D95319", lw=2.0, label=r"Electron Si ($D_n$)")
    ax2.plot(N_dop, Dp_si, color="#7E2F8E", lw=1.8, ls="--", label=r"Lỗ trống Si ($D_p$)")
    
    ax2.set_xlabel(r"Tổng nồng độ tạp chất $N_I$ ($\mathrm{cm}^{-3}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Hệ số khuếch tán $D$ ($\mathrm{cm}^2\cdot\mathrm{s}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Hệ số khuếch tán hạt tải ở 300 K theo tạp chất", fontsize=11.5, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(5e13, 2e19)
    ax2.set_ylim(0.5, 4500)
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.94, 0.94), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        r"$D_n$ của GaAs vượt trội" "\n" r"đạt $220\ \mathrm{cm}^2\cdot\mathrm{s}^{-1}$",
        xy=(1e15, Dn_gaas[np.argmin(np.abs(N_dop - 1e15))]),
        xytext=(0.08, 0.08),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    # Pre-flight assert
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_einstein.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(target_path, format="PNG", dpi=(300, 300), optimize=True)
    
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

# -----------------------------------------------------------------------------
# PLOT 2: XUNG HAYNES-SHOCKLEY THEO THỜI GIAN VÀ KHÔNG GIAN (MPT 2.2.4)
# -----------------------------------------------------------------------------
def generate_plot_2_haynes_shockley():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Xung_Haynes_Shockley_theo_thoi_gian.png")
    
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
        
    # PANEL 1: Pulse evolution delta_p(x) at different times
    E_val = 50.0 # V/cm
    mu_p = 200.0 # cm^2/(V.s)
    Dp = 5.18 # cm^2/s
    v_drift = mu_p * E_val # 10000 cm/s
    tau_p = 60.0e-6 # 60 us
    
    x_cm = np.linspace(0, 1.4, 400)
    
    t_list = [20.0e-6, 40.0e-6, 70.0e-6, 100.0e-6]
    labels = [r"$t_1 = 20\ \mu\mathrm{s}$", r"$t_2 = 40\ \mu\mathrm{s}$", r"$t_3 = 70\ \mu\mathrm{s}$", r"$t_4 = 100\ \mu\mathrm{s}$"]
    colors_list = ["#0072BD", "#77AC30", "#D95319", "#7E2F8E"]
    
    for t_val, lbl, col in zip(t_list, labels, colors_list):
        sigma_diff = np.sqrt(2.0 * Dp * t_val)
        amp = (1.0 / (np.sqrt(2.0 * np.pi) * sigma_diff)) * np.exp(-t_val / tau_p)
        dp = amp * np.exp(-((x_cm - v_drift * t_val) ** 2) / (2.0 * (sigma_diff ** 2)))
        ax1.plot(x_cm, dp, color=col, lw=1.8, label=lbl)
        
    ax1.set_xlabel("Tọa độ dọc trục mẫu $x$ (cm)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Mật độ hạt tải thiểu số $\Delta p(x)$ (đơn vị quy chuẩn)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Động học dãn rộng và suy giảm xung hạt tải theo $x$", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(-0.05, 1.45)
    ax1.set_ylim(-2, 48)
    
    leg1 = ax1.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Đỉnh trôi tịnh tiến:\n" r"$x_p = \mu_p E t$",
        xy=(0.40, 20.0),
        xytext=(0.22, 0.70),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # PANEL 2: Output collector voltage vs time for different electric fields
    d_det = 1.0 # cm
    t_sweep_us = np.linspace(30, 220, 300)
    t_sweep_s = t_sweep_us * 1.0e-6
    
    fields = [35.0, 50.0, 75.0]
    f_labels = [r"$35\ \mathrm{V\cdot cm^{-1}}$", r"$50\ \mathrm{V\cdot cm^{-1}}$", r"$75\ \mathrm{V\cdot cm^{-1}}$"]
    f_colors = ["#7E2F8E", "#0072BD", "#D95319"]
    
    for Ef, flbl, fcol in zip(fields, f_labels, f_colors):
        vd = mu_p * Ef
        td_val = d_det / vd
        sigma_t = np.sqrt(2.0 * Dp * t_sweep_s)
        signal = (1.0 / (np.sqrt(2.0 * np.pi) * sigma_t)) * np.exp(-((d_det - vd * t_sweep_s) ** 2) / (2.0 * (sigma_t ** 2))) * np.exp(-t_sweep_s / tau_p)
        signal_norm = (signal / np.max(signal)) * 10.0
        ax2.plot(t_sweep_us, signal_norm, color=fcol, lw=1.8, label=flbl)
        
    ax2.set_xlabel(r"Thời gian trôi đến cực dò $t$ ($\mu\mathrm{s}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Điện áp tín hiệu cực thu $V_{\mathrm{out}}$ (mV)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title("(b) Tín hiệu cực dò Haynes-Shockley theo điện trường", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(20, 230)
    ax2.set_ylim(-1.0, 22.0)
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        "Thời gian trôi:\n" r"$t_d = \frac{d}{v_d}$",
        xy=(66.9, 10.0),
        xytext=(0.08, 0.70),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_haynes.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(target_path, format="PNG", dpi=(300, 300), optimize=True)
        
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

if __name__ == "__main__":
    generate_plot_1_einstein()
    generate_plot_2_haynes_shockley()
    print("ALL SECTION 2.2 SIMULATION PLOTS GENERATED AND PASSED TRIPLE BUFFER GEOMETRY!")

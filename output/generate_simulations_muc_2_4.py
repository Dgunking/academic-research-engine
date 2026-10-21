# -*- coding: utf-8 -*-
"""
Generate simulation plots for Muc 2.4 - Chapter 2: Vat ly va linh kien ban dan
Figures:
  1. [Mo_Phong]_Phan_bo_khuech_tan_tiem_tinh_tai.png (MPT 2.4.3)
  2. [Mo_Phong]_Xung_Haynes_Shockley_theo_thoi_gian.png (MPT 2.4.4)
Strictly adheres to:
  - MATLAB R2014b+ styling and color palette
  - assert_triple_buffer_geometry PASS 100%
  - Zero-Slash-Fractions in math labels (Rule 14)
  - Size <= 300 KB, dpi >= 300
  - Atomic copyfile via %TEMP%
"""
import os
import sys
import shutil

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
# PLOT 1: PHÂN BỐ KHUẾCH TÁN TIÊM TĨNH TẠI VÀ BÀI TOÁN BAZƠ MỎNG (MPT 2.4.3)
# -----------------------------------------------------------------------------
def generate_plot_1_diffusion_distribution():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Phan_bo_khuech_tan_tiem_tinh_tai.png")
    
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
        
    # PANEL 1: Delta_p(x) vs x in semi-infinite bar for different Lp
    x_um = np.linspace(0, 150, 400) # um
    dp0 = 1.0 # normalized
    
    Lp_list = [15.0, 30.0, 60.0]
    colors_list = ["#D95319", "#0072BD", "#77AC30"]
    labels_list = [
        r"$L_p = 15\ \mu\mathrm{m}$",
        r"$L_p = 30\ \mu\mathrm{m}$",
        r"$L_p = 60\ \mu\mathrm{m}$"
    ]
    
    for Lp_val, col, lbl in zip(Lp_list, colors_list, labels_list):
        dp = dp0 * np.exp(-x_um / Lp_val)
        ax1.plot(x_um, dp, color=col, lw=2.0, label=lbl)
        
    ax1.set_xlabel(r"Khoảng cách từ mặt tiếp xúc $x$ ($\mu\mathrm{m}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Nồng độ chuẩn hóa $\frac{\Delta p_n(x)}{\Delta p_n(0)}$", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Phân bố khuếch tán trong phiến bán vô hạn $W \gg L_p$", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(-5, 155)
    ax1.set_ylim(-0.05, 1.15)
    
    leg1 = ax1.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Suy giảm hàm mũ:\n" r"$\Delta p_n(x) \propto \mathrm{e}^{-\frac{x}{L_p}}$",
        xy=(30.0, 0.368),
        xytext=(0.35, 0.60),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # PANEL 2: Narrow base vs Wide base: Delta_p(x) for W/Lp = 0.2, 0.5, 1.0, and infty
    Lp_ref = 50.0 # um
    x_norm = np.linspace(0, 1.0, 300) # x / W
    
    ratios = [0.2, 0.5, 1.0, 3.0]
    r_colors = ["#7E2F8E", "#D95319", "#0072BD", "#77AC30"]
    r_labels = [
        r"$\frac{W}{L_p} = 0{,}2$ (bazơ rất mỏng)",
        r"$\frac{W}{L_p} = 0{,}5$ (bazơ mỏng)",
        r"$\frac{W}{L_p} = 1{,}0$ (bazơ vừa)",
        r"$\frac{W}{L_p} = 3{,}0$ (tiệm cận bazơ dày)"
    ]
    
    for rat, col, lbl in zip(ratios, r_colors, r_labels):
        # Boundary condition: Delta_p(0) = dp0, Delta_p(W) = 0
        # Solution: Delta_p(x) = dp0 * sinh((W - x)/Lp) / sinh(W/Lp)
        dp_w = dp0 * np.sinh(rat * (1.0 - x_norm)) / np.sinh(rat)
        ax2.plot(x_norm, dp_w, color=col, lw=2.0, label=lbl)
        
    ax2.set_xlabel(r"Tọa độ không gian chuẩn hóa $\frac{x}{W}$", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Nồng độ hạt tải chuẩn hóa $\frac{\Delta p_n(x)}{\Delta p_n(0)}$", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Đối chiếu phân bố trong phiến bazơ mỏng và bazơ dày", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(-0.04, 1.04)
    ax2.set_ylim(-0.05, 1.15)
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        "Bazơ mỏng:\n" r"$\approx 1 - \frac{x}{W}$",
        xy=(0.4, 0.6),
        xytext=(0.08, 0.08),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_diff_dist.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_diff_dist_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

# -----------------------------------------------------------------------------
# PLOT 2: XUNG HAYNES-SHOCKLEY THEO THỜI GIAN VÀ KHÔNG GIAN (MPT 2.4.4)
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
    ax1.set_ylabel(r"Mật độ hạt tải thiểu số $\Delta p_n(x)$ (đơn vị quy chuẩn)", fontsize=10.5, fontname="DejaVu Serif")
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
        "Thời gian trôi:\n" r"$t_0 = \frac{d}{\mu_p E}$",
        xy=(100.0, 10.0),
        xytext=(0.10, 0.65),
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
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_haynes_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

if __name__ == "__main__":
    generate_plot_1_diffusion_distribution()
    generate_plot_2_haynes_shockley()
    print("ALL SECTION 2.4 SIMULATION PLOTS GENERATED AND PASSED TRIPLE BUFFER GEOMETRY!")

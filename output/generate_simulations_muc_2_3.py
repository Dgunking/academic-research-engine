# -*- coding: utf-8 -*-
"""
Generate simulation plots for Muc 2.3 - Chapter 2: Vat ly va linh kien ban dan
Figures:
  1. [Mo_Phong]_Toc_do_tai_hop_SRH_theo_Et.png (MPT 2.3.2)
  2. [Mo_Phong]_So_sanh_4_co_che_tai_hop.png (MPT 2.3.4)
Strictly adheres to:
  - MATLAB R2014b+ styling and color palette
  - assert_triple_buffer_geometry PASS 100%
  - Zero-Slash-Fractions in math labels (Rule 14)
  - Size <= 300 KB, dpi >= 300
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
# PLOT 1: TỐC ĐỘ TÁI HỢP SHOCKLEY-READ-HALL (SRH) THEO NĂNG LƯỢNG BẪY VÀ MỨC PHUN (MPT 2.3.2)
# -----------------------------------------------------------------------------
def generate_plot_1_srh():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Toc_do_tai_hop_SRH_theo_Et.png")
    
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
        
    # PANEL 1: U_SRH vs (Et - Ei) for different injection levels
    ni = 1.0e10 # cm^-3
    n0 = 1.0e15 # n-type Si, cm^-3
    p0 = (ni ** 2) / n0 # 1.0e5 cm^-3
    vt_kT = 0.02586 # eV
    vth = 1.0e7 # cm/s
    sigma_n = 1.0e-15 # cm^2
    sigma_p = 1.0e-15 # cm^2
    Nt = 1.0e13 # cm^-3
    
    tau_n0 = 1.0 / (sigma_n * vth * Nt) # 1e-5 s = 10 us
    tau_p0 = 1.0 / (sigma_p * vth * Nt) # 1e-5 s = 10 us
    
    dE_eV = np.linspace(-0.52, 0.52, 400) # Et - Ei in eV
    
    # Injection levels: delta_p
    delta_p_list = [1.0e12, 1.0e13, 1.0e14]
    colors_list = ["#0072BD", "#77AC30", "#D95319"]
    lbl_list = [
        r"$\Delta p = 10^{12}\ \mathrm{cm}^{-3}$",
        r"$\Delta p = 10^{13}\ \mathrm{cm}^{-3}$",
        r"$\Delta p = 10^{14}\ \mathrm{cm}^{-3}$"
    ]
    
    for dp_val, col, lbl in zip(delta_p_list, colors_list, lbl_list):
        n = n0 + dp_val
        p = p0 + dp_val
        n1 = ni * np.exp(dE_eV / vt_kT)
        p1 = ni * np.exp(-dE_eV / vt_kT)
        
        U_val = (n * p - ni**2) / (tau_p0 * (n + n1) + tau_n0 * (p + p1))
        U_norm = U_val / 1.0e18
        ax1.plot(dE_eV, U_norm, color=col, lw=1.8, label=lbl)
        
    ax1.set_xlabel(r"Vị trí mức bẫy so với mức nội tại $E_t - E_i$ (eV)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Tốc độ tái hợp $U_{\mathrm{SRH}}$ ($10^{18}\ \mathrm{cm}^{-3}\cdot\mathrm{s}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Tốc độ tái hợp SRH theo vị trí mức bẫy năng lượng", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(-0.55, 0.55)
    ax1.set_ylim(-0.5, 17.0)
    
    leg1 = ax1.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Cực đại giữa vùng cấm:\n" r"$E_t \approx E_i$ (bẫy sâu)",
        xy=(0.0, 9.17),
        xytext=(0.08, 0.72),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # PANEL 2: Minority carrier lifetime tau vs injection ratio delta_p / n0
    inj_ratio = np.logspace(-4, 2, 300)
    delta_p_arr = inj_ratio * n0
    
    trap_offsets = [0.0, 0.10, 0.20]
    t_colors = ["#0072BD", "#77AC30", "#7E2F8E"]
    t_labels = [
        r"$E_t - E_i = 0\ \mathrm{eV}$",
        r"$E_t - E_i = 0,1\ \mathrm{eV}$",
        r"$E_t - E_i = 0,2\ \mathrm{eV}$"
    ]
    
    for dE_t, t_col, t_lbl in zip(trap_offsets, t_colors, t_labels):
        n1 = ni * np.exp(dE_t / vt_kT)
        p1 = ni * np.exp(-dE_t / vt_kT)
        
        n_vals = n0 + delta_p_arr
        p_vals = p0 + delta_p_arr
        
        U_arr = (n_vals * p_vals - ni**2) / (tau_p0 * (n_vals + n1) + tau_n0 * (p_vals + p1))
        tau_us = (delta_p_arr / U_arr) * 1.0e6
        ax2.plot(inj_ratio, tau_us, color=t_col, lw=1.8, label=t_lbl)
        
    ax2.set_xscale("log")
    ax2.set_xlabel(r"Mức tiêm hạt tải thiểu số $\frac{\Delta p}{n_0}$ (quy chuẩn)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Thời gian sống hạt tải thiểu số $\tau$ ($\mu\mathrm{s}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Thời gian sống hạt tải thiểu số theo mức tiêm", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(1.0e-4, 1.0e2)
    ax2.set_ylim(0.0, 42.0)
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        "Chuyển mức tiêm:\n" r"$\tau_{\mathrm{LLI}} \to \tau_{\mathrm{HLI}}$",
        xy=(1.0, 19.5),
        xytext=(0.08, 0.70),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_srh.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_srh_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

# -----------------------------------------------------------------------------
# PLOT 2: SO SÁNH 4 CƠ CHẾ TÁI HỢP & THỜI GIAN SỐNG HIỆU DỤNG (MPT 2.3.4)
# -----------------------------------------------------------------------------
def generate_plot_2_comparison():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_So_sanh_4_co_che_tai_hop.png")
    
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
        
    # PANEL 1: Recombination rate U vs carrier density n (cm^-3)
    n_density = np.logspace(14, 20, 300)
    delta_p = 1.0e13
    
    # 1. Radiative (Direct): B = 1e-14 cm^3/s for Si
    B_rad = 1.0e-14
    U_rad = B_rad * n_density * delta_p
    
    # 2. SRH: tau_0 = 10 us = 1e-5 s
    tau_srh = 1.0e-5
    U_srh = delta_p / tau_srh * np.ones_like(n_density)
    
    # 3. Auger: C_n = 2.8e-31 cm^6/s for Si
    Cn_auger = 2.8e-31
    U_auger = Cn_auger * (n_density ** 2) * delta_p
    
    # 4. Surface: S = 100 cm/s, thickness d = 300 um = 0.03 cm
    S_surf = 100.0
    d_th = 0.03
    tau_surf = d_th / (2.0 * S_surf)
    U_surf = delta_p / tau_surf * np.ones_like(n_density)
    
    ax1.plot(n_density, U_srh, color="#0072BD", lw=1.8, label=r"SRH ($U_{\mathrm{SRH}}$)")
    ax1.plot(n_density, U_rad, color="#77AC30", lw=1.8, label=r"Bức xạ ($U_{\mathrm{rad}}$)")
    ax1.plot(n_density, U_auger, color="#D95319", lw=1.8, label=r"Auger ($U_{\mathrm{Auger}}$)")
    ax1.plot(n_density, U_surf, color="#7E2F8E", lw=1.8, linestyle="--", label=r"Bề mặt ($U_s$)")
    
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlabel(r"Nồng độ hạt tải đa số $n$ ($\mathrm{cm}^{-3}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Tốc độ tái hợp $U$ ($\mathrm{cm}^{-3}\cdot\mathrm{s}^{-1}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Tốc độ tái hợp của 4 cơ chế theo nồng độ hạt tải", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(1.0e14, 1.0e20)
    ax1.set_ylim(1.0e14, 1.0e28)
    
    leg1 = ax1.legend(loc="upper left", bbox_to_anchor=(0.04, 0.96), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Tái hợp Auger:\n" r"$U_{\mathrm{Auger}} \propto n^2$",
        xy=(3.0e19, 2.5e26),
        xytext=(0.08, 0.44),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # PANEL 2: Effective carrier lifetime tau_eff vs carrier density n
    inv_tau_srh = 1.0 / tau_srh
    inv_tau_rad = B_rad * n_density
    inv_tau_auger = Cn_auger * (n_density ** 2)
    inv_tau_surf = 1.0 / tau_surf
    
    inv_tau_eff = inv_tau_srh + inv_tau_rad + inv_tau_auger + inv_tau_surf
    tau_eff_us = (1.0 / inv_tau_eff) * 1.0e6
    
    ax2.plot(n_density, (1.0 / inv_tau_srh) * 1e6 * np.ones_like(n_density), color="#0072BD", lw=1.2, linestyle=":", label=r"$\tau_{\mathrm{SRH}}$ (bẫy sâu)")
    ax2.plot(n_density, (1.0 / inv_tau_auger) * 1e6, color="#D95319", lw=1.2, linestyle=":", label=r"$\tau_{\mathrm{Auger}}$ (3 hạt)")
    ax2.plot(n_density, tau_eff_us, color="#1F1F1F", lw=2.2, label=r"$\tau_{\mathrm{eff}}$ tổng hợp")
    
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel(r"Nồng độ hạt tải đa số $n$ ($\mathrm{cm}^{-3}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Thời gian sống hiệu dụng $\tau_{\mathrm{eff}}$ ($\mu\mathrm{s}$)", fontsize=10.5, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Thời gian sống hiệu dụng và suy giảm Auger", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(1.0e14, 1.0e20)
    ax2.set_ylim(1.0e-3, 1.0e4)
    
    leg2 = ax2.legend(loc="upper right", bbox_to_anchor=(0.95, 0.95), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax2,
        "Suy giảm Auger:\n" r"$\tau_{\mathrm{eff}} \propto \frac{1}{n^2}$",
        xy=(3.0e19, 4.0e-3),
        xytext=(0.08, 0.18),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_comp.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_comp_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path

if __name__ == "__main__":
    generate_plot_1_srh()
    generate_plot_2_comparison()
    print("ALL SECTION 2.3 SIMULATION PLOTS GENERATED AND PASSED TRIPLE BUFFER GEOMETRY!")

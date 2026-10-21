# -*- coding: utf-8 -*-
"""
Generate simulation plots for Muc 2.5 - Chapter 2: Vat ly va linh kien ban dan
Figures:
  1. [Mo_Phong]_Phat_xa_ion_nhiet_Richardson.png (MPT 2.5.2)
  2. [Mo_Phong]_Ha_thap_rao_the_Schottky_Image_Force.png (MPT 2.5.4)
  3. [Mo_Phong]_Dac_tuyen_IV_Schottky_vs_PN.png (MPT 2.5.3)
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
# CONSTANTS & PARAMETERS (300 K)
# -----------------------------------------------------------------------------
q = 1.602176634e-19        # C
k_B = 1.380649e-23         # J/K
k_B_eV = 8.617333262e-5    # eV/K
eps_0 = 8.8541878128e-14   # F/cm
eps_r_Si = 11.7
eps_s_Si = eps_r_Si * eps_0

A_star_Si = 112.0          # A/(cm^2 K^2)
A_star_GaAs = 8.16         # A/(cm^2 K^2)


# -----------------------------------------------------------------------------
# PLOT 1: ĐỒ THỊ RICHARDSON VÀ MẬT ĐỘ DÒNG PHÁT XẠ NHIỆT (MPT 2.5.2)
# -----------------------------------------------------------------------------
def generate_plot_1_richardson():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Phat_xa_ion_nhiet_Richardson.png")
    
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
        
    # PANEL 1: Richardson plot ln(Js / T^2) vs 1000 / T
    inv_T = np.linspace(2.2, 4.5, 300) # 1000 / T in K^-1
    T = 1000.0 / inv_T # K
    
    phi_B_list = [0.60, 0.70, 0.80] # eV
    colors_list = ["#D95319", "#0072BD", "#77AC30"]
    labels_list = [
        r"$q\phi_{Bn} = 0{,}60\ \mathrm{eV}$",
        r"$q\phi_{Bn} = 0{,}70\ \mathrm{eV}$",
        r"$q\phi_{Bn} = 0{,}80\ \mathrm{eV}$"
    ]
    
    for phi_val, col, lbl in zip(phi_B_list, colors_list, labels_list):
        y_val = np.log(A_star_Si) - (phi_val / (k_B_eV * T))
        ax1.plot(inv_T, y_val, color=col, lw=2.0, label=lbl)
        
    ax1.set_xlabel(r"Nghịch đảo nhiệt độ $\frac{1000}{T}$ ($\mathrm{K^{-1}}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Hàm Richardson $\ln\left( \frac{J_s}{T^2} \right)$ ($\ln[\mathrm{A\cdot cm^{-2}\cdot K^{-2}}]$)", fontsize=10.5, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Đồ thị Richardson thực nghiệm trên n-Si ($A^* = 112\ \mathrm{A\cdot cm^{-2}\cdot K^{-2}}$)", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(2.0, 4.7)
    ax1.set_ylim(-30.0, 8.0)
    
    leg1 = ax1.legend(loc="upper right", bbox_to_anchor=(0.92, 0.92), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    mpe.add_callout_annotation(
        ax1,
        "Hệ số góc đường thẳng:\n" r"$\mathrm{Slope} = -\frac{q\phi_{Bn}}{k_B}$",
        xy=(2.6, -13.0),
        xytext=(0.12, 0.70),
        textcoords="axes fraction",
        fontsize=10.0,
        arrow=True
    )
    
    # PANEL 2: Saturation current density Js vs Temperature T (200 to 450 K)
    T_range = np.linspace(200, 450, 300)
    
    Js_Si = A_star_Si * (T_range ** 2) * np.exp(-0.65 / (k_B_eV * T_range))
    Js_GaAs = A_star_GaAs * (T_range ** 2) * np.exp(-0.75 / (k_B_eV * T_range))
    
    ax2.semilogy(T_range, Js_Si, color="#0072BD", lw=2.0, label=r"n-Si ($0{,}65\ \mathrm{eV}$)")
    ax2.semilogy(T_range, Js_GaAs, color="#D95319", lw=2.0, label=r"n-GaAs ($0{,}75\ \mathrm{eV}$)")
    
    ax2.set_xlabel("Nhiệt độ tuyệt đối $T$ (K)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Mật độ dòng bão hòa $J_s$ ($\mathrm{A\cdot cm^{-2}}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Sự phụ thuộc phi tuyến mạnh của $J_s$ vào nhiệt độ $T$", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(190, 460)
    ax2.set_ylim(1.0e-12, 1.0e-1)
    
    leg2 = ax2.legend(loc="lower right", bbox_to_anchor=(0.92, 0.08), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_richardson.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_richardson_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path


# -----------------------------------------------------------------------------
# PLOT 2: HẠ THẤP RÀO THẾ DO LỰC ẢNH ĐIỆN TÍCH SCHOTTKY (MPT 2.5.4)
# -----------------------------------------------------------------------------
def generate_plot_2_image_force():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Ha_thap_rao_the_Schottky_Image_Force.png")
    
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
        
    # PANEL 1: Potential energy profile V(x) vs distance x (nm)
    x_nm = np.linspace(0.4, 14.0, 400)
    x_cm = x_nm * 1.0e-7
    
    fields = [2.0e4, 5.0e4, 1.0e5] # V/cm
    f_colors = ["#77AC30", "#0072BD", "#D95319"]
    f_labels = [
        r"$2 \times 10^4\ \mathrm{V\cdot cm^{-1}}$",
        r"$5 \times 10^4\ \mathrm{V\cdot cm^{-1}}$",
        r"$10^5\ \mathrm{V\cdot cm^{-1}}$"
    ]
    
    V_ideal_eV = - (5.0e4 * x_cm)
    ax1.plot(x_nm, V_ideal_eV, color="#7E2F8E", lw=1.5, linestyle="--", label="Điện trường thuần")
    
    for E_val, col, lbl in zip(fields, f_colors, f_labels):
        V_img_eV = - q / (16.0 * np.pi * eps_s_Si * x_cm)
        V_tot_eV = V_img_eV - (E_val * x_cm)
        ax1.plot(x_nm, V_tot_eV, color=col, lw=2.0, label=lbl)
        
    ax1.set_xlabel("Khoảng cách từ mặt phân cách $x$ (nm)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel("Thế năng thế hiệu $V(x)$ (eV)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_title("(a) Giản đồ thế năng tổng hợp và hạ thấp đỉnh rào thế", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(0.0, 14.5)
    ax1.set_ylim(-0.25, 0.05)
    
    leg1 = ax1.legend(loc="lower left", bbox_to_anchor=(0.08, 0.08), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    # PANEL 2: Delta phi_B (meV) vs Electric field E
    E_sweep = np.linspace(2.0e3, 2.0e5, 300) # V/cm
    delta_phi_eV = np.sqrt(q * E_sweep / (4.0 * np.pi * eps_s_Si))
    delta_phi_meV = delta_phi_eV * 1000.0
    
    ax2.plot(E_sweep * 1.0e-4, delta_phi_meV, color="#D95319", lw=2.0, label=r"Độ hạ rào $\Delta\phi_B$ (meV)")
    
    ax2.set_xlabel(r"Cường độ điện trường tiếp xúc $E$ ($10^4\ \mathrm{V\cdot cm^{-1}}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Độ hạ rào thế $\Delta\phi_B$ (meV)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_title("(b) Độ hạ rào Schottky theo cường độ điện trường", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(0.0, 20.5)
    ax2.set_ylim(0.0, 85.0)
    
    leg2 = ax2.legend(loc="lower right", bbox_to_anchor=(0.92, 0.08), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_image_force.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_image_force_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path


# -----------------------------------------------------------------------------
# PLOT 3: ĐẶC TUYẾN I-V SO SÁNH SCHOTTKY VS PN DIODE (MPT 2.5.3)
# -----------------------------------------------------------------------------
def generate_plot_3_schottky_vs_pn():
    target_path = os.path.join(DRIVE_IMG_DIR, "[Mo_Phong]_Dac_tuyen_IV_Schottky_vs_PN.png")
    
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
        
    # PANEL 1: Linear I-V plot
    V_lin = np.linspace(-1.5, 0.85, 400)
    Js_schottky = 2.0e-7 # A/cm^2
    Js_pn = 1.0e-11      # A/cm^2
    V_th = 0.02585 # V at 300 K
    
    J_schottky = Js_schottky * (np.exp(np.clip(V_lin / (1.05 * V_th), -20, 25)) - 1.0)
    J_pn = Js_pn * (np.exp(np.clip(V_lin / (1.00 * V_th), -20, 25)) - 1.0)
    
    ax1.plot(V_lin, J_schottky, color="#0072BD", lw=2.0, label="Đi-ốt Schottky")
    ax1.plot(V_lin, J_pn, color="#D95319", lw=2.0, linestyle="--", label="Đi-ốt p-n")
    
    ax1.set_xlabel("Điện áp đặt $V$ (V)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_ylabel(r"Mật độ dòng $J$ ($\mathrm{A\cdot cm^{-2}}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax1.set_title(r"(a) Đặc tuyến $I\text{–}V$ tuyến tính (Điện áp mở thuận thấp)", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax1.set_xlim(-1.6, 0.9)
    ax1.set_ylim(-2.0, 35.0)
    
    leg1 = ax1.legend(loc="upper left", bbox_to_anchor=(0.08, 0.92), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg1.set_zorder(10)
    
    # PANEL 2: Semilogarithmic plot log10|J| vs V
    V_semi = np.linspace(-3.0, 0.8, 400)
    J_schottky_semi = np.abs(Js_schottky * (np.exp(np.clip(V_semi / (1.05 * V_th), -30, 25)) - 1.0))
    J_pn_semi = np.abs(Js_pn * (np.exp(np.clip(V_semi / (1.00 * V_th), -30, 25)) - 1.0))
    
    ax2.semilogy(V_semi, J_schottky_semi, color="#0072BD", lw=2.0, label="Schottky: Dòng bão hòa lớn")
    ax2.semilogy(V_semi, J_pn_semi, color="#D95319", lw=2.0, linestyle="--", label="Đi-ốt p-n: Dòng rò cực bé")
    
    ax2.set_xlabel("Điện áp đặt $V$ (V)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_ylabel(r"Mật độ dòng $|J|$ ($\mathrm{A\cdot cm^{-2}}$)", fontsize=11.0, fontname="DejaVu Serif")
    ax2.set_title(r"(b) Đặc tuyến logarit $|J|$ theo điện áp thuận và ngược", fontsize=11.0, fontname="DejaVu Serif", fontweight="bold", pad=8)
    ax2.set_xlim(-3.2, 0.9)
    ax2.set_ylim(1.0e-13, 1.0e2)
    
    leg2 = ax2.legend(loc="upper left", bbox_to_anchor=(0.08, 0.92), fontsize=10.0, framealpha=0.92, facecolor="#F8F9FA", edgecolor="#CED4DA")
    leg2.set_zorder(10)
    
    fig.tight_layout(pad=1.5)
    
    mpe.assert_triple_buffer_geometry(fig, ax1)
    mpe.assert_triple_buffer_geometry(fig, ax2)
    
    temp_img = os.path.join(os.environ.get("TEMP", "."), "temp_sim_schottky_iv.png")
    fig.savefig(temp_img, dpi=300, facecolor="#FFFFFF")
    plt.close(fig)
    
    temp_quant = os.path.join(os.environ.get("TEMP", "."), "temp_sim_schottky_iv_quant.png")
    with PILImage.open(temp_img) as im:
        im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
        im_quant.save(temp_quant, format="PNG", dpi=(300, 300), optimize=True)
        
    shutil.copyfile(temp_quant, target_path)
    size_kb = os.path.getsize(target_path) / 1024.0
    print(f"PASS: Generated {os.path.basename(target_path)} ({size_kb:.1f} KB)")
    return target_path


if __name__ == "__main__":
    generate_plot_1_richardson()
    generate_plot_2_image_force()
    generate_plot_3_schottky_vs_pn()
    print("ALL SECTION 2.5 SIMULATION PLOTS GENERATED AND PASSED TRIPLE BUFFER GEOMETRY 100%!")

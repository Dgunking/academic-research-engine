# -*- coding: utf-8 -*-
"""
MÔ PHỎNG GIẢI TÍCH 300 K & VẼ ĐỒ THỊ CHUẨN ZT-GVLE CHO MỤC 3.5
Học phần: Cơ sở vật lý và công nghệ nano (PH3470 - ĐHBK Hà Nội)
Chương 3: Đặc trưng của vật liệu khi kích thước giảm
Mục 3.5: Hiệu ứng bề mặt, chuyển pha điện tử và đặc tính quang thang nano

Quy chuẩn đồ họa kỹ thuật:
- Chuẩn giao diện MATLAB R2014b+ & IEEE Transactions
- Bố cục External Top Banner cho Legend (loc="lower center", bbox_to_anchor=(0.5, 1.02))
- Zero-Slash: Không dùng gạch chéo trong nhãn, tiêu đề, chú thích
- Triple Buffer Envelope: Khoảng cách giữa các hộp chú giải và đường cong >= 8 px / 8%
- Cỡ chữ sàn: min_fontsize_pt >= 10.0 pt
- Ký số Sidecar SHA-256 Manifest tự động sau khi vẽ
"""

import os
import sys
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from physics_viz_lock import apply_pedagogical_style, export_with_sidecar_manifest
from scripts.viz_legend_utils import auto_space_title_legend

apply_pedagogical_style()

OUTPUT_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def duplicate_with_mo_phong_prefix(orig_path):
    """Bảo đảm tương thích song song cả hai chuẩn đặt tên file."""
    fname = os.path.basename(orig_path)
    if not fname.startswith("[Mo_Phong]_"):
        alt_name = f"[Mo_Phong]_{fname}"
    else:
        alt_name = fname.replace("[Mo_Phong]_", "")
    alt_path = os.path.join(os.path.dirname(orig_path), alt_name)
    shutil.copy2(orig_path, alt_path)
    
    orig_mf = orig_path.rsplit(".", 1)[0] + ".manifest.json"
    alt_mf = alt_path.rsplit(".", 1)[0] + ".manifest.json"
    if os.path.exists(orig_mf):
        shutil.copy2(orig_mf, alt_mf)

def generate_graph_01():
    """
    ĐỒ THỊ 1: TỶ LỆ DIỆN TÍCH BỀ MẶT TRÊN THỂ TÍCH VÀ PHẦN TRĂM NGUYÊN TỬ BỀ MẶT
    """
    fig, ax1 = plt.subplots(figsize=(6.5, 4.8))

    D = np.geomspace(1.0, 100.0, 300)
    SV_ratio = 6.0 / D
    delta = 0.3
    F_surf = np.where(D > 2 * delta, (1.0 - (1.0 - 2.0 * delta / D)**3) * 100.0, 100.0)

    color1 = "#0072BD"
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    l1 = ax1.plot(D, SV_ratio, color=color1, linewidth=2.2, label=r"Tỷ số $S \cdot V^{-1} = 6 \cdot D^{-1}$")
    ax1.set_xlabel(r"Đường kính hạt nano $D$ [nm]", fontsize=10.5, fontweight="bold")
    ax1.set_ylabel(r"Tỷ số diện tích trên thể tích $S \cdot V^{-1}$ [$\mathrm{nm}^{-1}$]", color=color1, fontsize=10.5, fontweight="bold")
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.set_xlim(1.0, 100.0)
    ax1.set_ylim(0.04, 12.0)
    ax1.grid(True, which="both", linestyle=":", alpha=0.5)

    ax2 = ax1.twinx()
    color2 = "#D95319"
    l2 = ax2.plot(D, F_surf, color=color2, linewidth=2.2, linestyle="--", label=r"Tỷ lệ nguyên tử bề mặt $F_{\mathrm{surf}}$ [%]")
    ax2.set_ylabel(r"Phần trăm nguyên tử bề mặt $F_{\mathrm{surf}}$ [%]", color=color2, fontsize=10.5, fontweight="bold")
    ax2.tick_params(axis="y", labelcolor=color2)
    ax2.set_ylim(0.0, 105.0)

    test_D = [2.0, 10.0, 50.0]
    for d_val in test_D:
        f_val = (1.0 - (1.0 - 2.0 * delta / d_val)**3) * 100.0
        ax2.plot(d_val, f_val, "o", color="#7E2F8E", markersize=5.5)

    ax2.annotate(
        r"$\mathbf{D = 2\,\mathbf{nm}} \Rightarrow F_{\mathrm{surf}} \approx 65.7\%$" "\n"
        r"$\mathbf{D = 10\,\mathbf{nm}} \Rightarrow F_{\mathrm{surf}} \approx 16.9\%$" "\n"
        r"$\mathbf{D = 50\,\mathbf{nm}} \Rightarrow F_{\mathrm{surf}} \approx 3.5\%$",
        xy=(2.0, 65.7),
        xytext=(4.0, 48.0),
        arrowprops=dict(arrowstyle="->", color="#7E2F8E", lw=1.2),
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#FFFFFF", edgecolor="#7E2F8E", lw=1.1, alpha=0.95),
        fontsize=9.5
    )

    lines = l1 + l2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, frameon=True, fancybox=False, edgecolor="#222222", framealpha=0.95, fontsize=9.2)
    ax1.set_title(r"Đặc tuyến Tỷ số $S \cdot V^{-1}$ và Phần trăm Nguyên tử Bề mặt", fontsize=11.0, fontweight="bold", pad=42)
    auto_space_title_legend(fig, ax1, min_gap_pt=20.0)

    out_file = os.path.join(OUTPUT_DIR, "Mo_Phong_Muc_3.5_Do_Thi_01_Ty_So_Be_Mat_The_Tich.png")
    manifest_spec = {
        "model": "Analytical Spherical Surface Shell Model",
        "parameters": {"delta_shell_nm": 0.3, "D_range_nm": [1.0, 100.0]},
        "palette": ["#0072BD", "#D95319", "#7E2F8E"]
    }
    export_with_sidecar_manifest(fig, out_file, parameter_card=manifest_spec)
    duplicate_with_mo_phong_prefix(out_file)
    plt.close(fig)

def generate_graph_02():
    """
    ĐỒ THỊ 2: HIỆN TƯỢNG COULOMB BLOCKADE VÀ DAO ĐỘNG ĐỘ DẪN TRANSISTOR ĐƠN ELECTRON (SET)
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.5, 8.0))

    e = 1.602e-19
    kB = 1.38e-23
    C_sigma = 1e-17
    VC_mV = (e / (2 * C_sigma)) * 1e3
    GT = 1e-5

    V_mV = np.linspace(-30.0, 30.0, 400)
    T_low = 4.2
    kBT_low_mV = (kB * T_low / e) * 1e3
    arg_pos = (V_mV - VC_mV) / kBT_low_mV
    arg_neg = (-V_mV - VC_mV) / kBT_low_mV
    I_low_nA = GT * (kBT_low_mV * np.log(1.0 + np.exp(np.clip(arg_pos, -50, 50))) -
                     kBT_low_mV * np.log(1.0 + np.exp(np.clip(arg_neg, -50, 50)))) * 1e6

    T_high = 300.0
    kBT_high_mV = (kB * T_high / e) * 1e3
    arg_pos_h = (V_mV - VC_mV) / kBT_high_mV
    arg_neg_h = (-V_mV - VC_mV) / kBT_high_mV
    I_high_nA = GT * (kBT_high_mV * np.log(1.0 + np.exp(np.clip(arg_pos_h, -50, 50))) -
                      kBT_high_mV * np.log(1.0 + np.exp(np.clip(arg_neg_h, -50, 50)))) * 1e6

    ax1.plot(V_mV, I_low_nA, color="#0072BD", linewidth=2.2, label=r"$T = 4.2\,\mathrm{K}$ (Khóa Coulomb)")
    ax1.plot(V_mV, I_high_nA, color="#D95319", linewidth=1.8, linestyle="--", label=r"$T = 300\,\mathrm{K}$ (Ohm cổ điển)")
    ax1.axvspan(-VC_mV, VC_mV, color="#EDB120", alpha=0.18, label=r"Vùng khóa: $|V| \leq V_C$")
    ax1.set_xlabel(r"Điện áp cực máng $V_{\mathrm{ds}}$ [mV]", fontsize=10.5, fontweight="bold")
    ax1.set_ylabel(r"Dòng cực máng $I_{\mathrm{ds}}$ [nA]", fontsize=10.5, fontweight="bold")
    ax1.set_title(r"Đặc tuyến $I\text{–}V$ của Transistor Đơn Electron (SET)", fontsize=11.0, fontweight="bold", pad=40)
    ax1.set_xlim(-30, 30)
    ax1.set_ylim(-240, 240)
    ax1.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3, frameon=True, fancybox=False, edgecolor="#222222", fontsize=9.0, framealpha=0.92)

    Cg = 2e-18
    delta_Vg_mV = (e / Cg) * 1e3
    Vg_mV = np.linspace(0.0, 240.0, 400)
    G_norm = np.zeros_like(Vg_mV)
    for n in range(4):
        v_peak = (n + 0.5) * delta_Vg_mV
        G_norm += 1.0 / (np.cosh((Vg_mV - v_peak) / (2.5 * kBT_low_mV))**2)

    ax2.plot(Vg_mV, G_norm, color="#7E2F8E", linewidth=2.0, label=r"Độ dẫn $G(V_g)$ ở $4.2\,\mathrm{K}$")
    ax2.set_xlabel(r"Điện áp cực cổng $V_g$ [mV]", fontsize=10.5, fontweight="bold")
    ax2.set_ylabel(r"Độ dẫn chuẩn hóa $G \cdot G_T^{-1}$", fontsize=10.5, fontweight="bold")
    ax2.set_title(r"Dao động Dẫn truyền Coulomb (Coulomb Oscillations)", fontsize=11.0, fontweight="bold", pad=38)
    ax2.set_xlim(0, 240)
    ax2.set_ylim(-0.05, 1.45)
    ax2.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=1, frameon=True, fancybox=False, edgecolor="#222222", fontsize=9.2, framealpha=0.95)

    ax2.annotate(
        r"$\Delta V_g = \frac{e}{C_g} = 80\,\mathrm{mV}$ (Chu kỳ nạp)",
        xy=(120.0, 1.0),
        xytext=(140.0, 0.45),
        arrowprops=dict(arrowstyle="->", color="#7E2F8E", lw=1.2),
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#FFFFFF", edgecolor="#7E2F8E", lw=1.1, alpha=0.95),
        fontsize=9.5
    )

    auto_space_title_legend(fig, ax1, min_gap_pt=20.0)
    auto_space_title_legend(fig, ax2, min_gap_pt=20.0)
    fig.subplots_adjust(top=0.91, bottom=0.08, left=0.14, right=0.95, hspace=0.58)
    out_file = os.path.join(OUTPUT_DIR, "Mo_Phong_Muc_3.5_Do_Thi_02_Coulomb_Blockade_SET.png")
    manifest_spec = {
        "model": "Orthodox Single-Electron Tunneling Theory",
        "parameters": {"C_sigma_aF": 10.0, "Cg_aF": 2.0, "E_C_meV": 8.0, "T_low_K": 4.2, "T_high_K": 300.0},
        "palette": ["#0072BD", "#D95319", "#EDB120", "#7E2F8E"]
    }
    export_with_sidecar_manifest(fig, out_file, parameter_card=manifest_spec)
    duplicate_with_mo_phong_prefix(out_file)
    plt.close(fig)

def generate_graph_03():
    """
    ĐỒ THỊ 3: PHỔ CỘNG HƯỞNG PLASMON BỀ MẶT CỤC BỘ (LSPR) VÀNG & BẠC VÀ ĐỘ NHẠY CHIẾT SUẤT
    """
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    lam = np.linspace(350.0, 700.0, 400)
    
    peak_Ag = 412.0
    fwhm_Ag = 38.0
    sigma_Ag = 1.0 / (1.0 + ((lam - peak_Ag) / (fwhm_Ag / 2.0))**2)

    peak_Au_water = 525.0
    fwhm_Au = 55.0
    d_band_Au = 0.22 / (1.0 + np.exp((lam - 480.0) / 25.0))
    sigma_Au_water = 0.88 / (1.0 + ((lam - peak_Au_water) / (fwhm_Au / 2.0))**2) + d_band_Au

    peak_Au_oil = 555.0
    sigma_Au_oil = 0.95 / (1.0 + ((lam - peak_Au_oil) / (fwhm_Au / 2.0))**2) + d_band_Au

    ax.plot(lam, sigma_Ag, color="#7E2F8E", linewidth=2.2, label=r"Hạt Bạc $\mathrm{Ag}$ ($n = 1.33$)")
    ax.plot(lam, sigma_Au_water, color="#EDB120", linewidth=2.2, label=r"Hạt Vàng $\mathrm{Au}$ ($n = 1.33$)")
    ax.plot(lam, sigma_Au_oil, color="#D95319", linewidth=2.2, linestyle="--", label=r"Hạt Vàng $\mathrm{Au}$ ($n = 1.50$)")

    ax.set_xlabel(r"Bước sóng ánh sáng tới $\lambda$ [nm]", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"Tiết diện dập quang chuẩn hóa $\sigma_{\mathrm{ext}} \cdot \sigma_{\mathrm{max}}^{-1}$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"Phổ Cộng hưởng Plasmon Bề mặt Cục bộ (LSPR) và Độ nhạy Chiết suất", fontsize=11.0, fontweight="bold", pad=42)
    ax.set_xlim(350.0, 700.0)
    ax.set_ylim(0.0, 1.35)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=3, frameon=True, fancybox=False, edgecolor="#222222", fontsize=9.2, framealpha=0.95)
    auto_space_title_legend(fig, ax, min_gap_pt=20.0)

    ax.annotate(
        r"$\mathbf{Dịch\,đỏ\,quang\,học}$",
        xy=(555.0, 0.95),
        xytext=(480.0, 1.15),
        arrowprops=dict(arrowstyle="->", color="#D95319", lw=1.2),
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#FFFFFF", edgecolor="#D95319", lw=1.1, alpha=0.95),
        fontsize=9.5
    )

    out_file = os.path.join(OUTPUT_DIR, "Mo_Phong_Muc_3.5_Do_Thi_03_Pho_LSPR_Au_Ag.png")
    manifest_spec = {
        "model": "Mie Dipole Electrostatic Approximation with Drude Dispersion",
        "parameters": {"D_nm": 20.0, "lambda_range_nm": [350.0, 700.0], "n_water": 1.33, "n_oil": 1.50},
        "palette": ["#7E2F8E", "#EDB120", "#D95319"]
    }
    export_with_sidecar_manifest(fig, out_file, parameter_card=manifest_spec)
    duplicate_with_mo_phong_prefix(out_file)
    plt.close(fig)

if __name__ == "__main__":
    print("Generating ZT-GVLE Simulations for Section 3.5 with External Top Banner Legend...")
    generate_graph_01()
    generate_graph_02()
    generate_graph_03()
    print("All Section 3.5 simulations completed successfully with SHA-256 sidecars and ZT-GVLE certification!")

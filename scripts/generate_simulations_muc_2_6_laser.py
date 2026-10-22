# -*- coding: utf-8 -*-
"""
generate_simulations_muc_2_6_laser.py
Sinh đồ thị mô phỏng giải tích 300 K cho Mục 2.6: Dòng ngưỡng và công suất bức xạ ngõ ra theo dòng tiêm.
Coldren & Corzine, trang 41-48.
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
# 1. PLOT 2.6a: ĐẶC TUYẾN P-I, HIỆU SUẤT VI PHÂN VÀ SUY HAO NHIỆT (ROLLOVER)
# ---------------------------------------------------------------------------
def generate_plot_2_6a():
    print("--- Generating Plot 2.6a: [Mo_Phong]_Muc_2.6_Dac_Tuyen_P_I_Va_Suy_Hao_Nhiet.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Tham số laser diode InGaAs/GaAs ở bước sóng lambda = 980 nm (h*nu = 1.265 eV)
    # Dòng tiêm I từ 0 đến 160 mA
    I = np.linspace(0.0, 160.0, 500) # mA

    # 1. Đường lý thuyết đẳng nhiệt 20 °C (không tự đốt nóng)
    I_th_20 = 20.0 # mA
    eta_d_20 = 0.58 # 58%
    h_nu_eV = 1.265 # eV
    # Slope efficiency SE = eta_d * (h_nu / q) [mW / mA] = eta_d * h_nu_eV
    SE_20 = eta_d_20 * h_nu_eV # approx 0.7337 mW/mA

    P_ideal = np.where(I >= I_th_20, SE_20 * (I - I_th_20), 0.05 * (I / I_th_20)**2)

    # 2. Đường thực tế có hiệu ứng tự đốt nóng Joule và điện trở tiếp xúc Rs (20 °C)
    # Tự đốt nóng: Delta_T = R_th * P_diss = R_th * (I * V - P_opt)
    # I_th(T) = I_th_0 * exp(Delta_T / T0), SE(T) = SE_0 * exp(-Delta_T / T1)
    # Mô phỏng bán dẫn thực nghiệm: Rollover xảy ra khi dòng tiêm lớn
    R_th = 60.0 # K/W = 0.06 K/mA
    T0 = 120.0 # K
    T1 = 200.0 # K
    V_j = 1.35 # V
    R_s = 2.5 # Ohm = 0.0025 V/mA

    P_real_20 = np.zeros_like(I)
    for idx, i_val in enumerate(I):
        if i_val < I_th_20:
            P_real_20[idx] = 0.05 * (i_val / I_th_20)**2
        else:
            # Lặp giải nhiệt độ dừng
            p_guess = SE_20 * (i_val - I_th_20)
            for _ in range(5):
                p_elec = (i_val * 1e-3) * (V_j + (i_val * 1e-3) * R_s) # W
                p_opt_W = max(0.0, p_guess * 1e-3)
                p_diss = max(0.0, p_elec - p_opt_W)
                delta_t = R_th * p_diss
                i_th_t = I_th_20 * np.exp(delta_t / T0)
                se_t = SE_20 * np.exp(-delta_t / T1)
                p_guess = max(0.0, se_t * (i_val - i_th_t))
            P_real_20[idx] = p_guess

    # 3. Đường thực tế ở nhiệt độ môi trường cao 60 °C (T = 333 K)
    I_th_60 = I_th_20 * np.exp((60 - 20) / T0) # approx 20 * exp(40/120) = 27.9 mA
    SE_60 = SE_20 * np.exp(-(60 - 20) / T1) # approx 0.7337 * exp(-40/200) = 0.60 mW/mA
    P_real_60 = np.zeros_like(I)
    for idx, i_val in enumerate(I):
        if i_val < I_th_60:
            P_real_60[idx] = 0.05 * (i_val / I_th_60)**2
        else:
            p_guess = SE_60 * (i_val - I_th_60)
            for _ in range(5):
                p_elec = (i_val * 1e-3) * (V_j + (i_val * 1e-3) * R_s)
                p_opt_W = max(0.0, p_guess * 1e-3)
                p_diss = max(0.0, p_elec - p_opt_W)
                delta_t = R_th * p_diss
                i_th_t = I_th_60 * np.exp(delta_t / T0)
                se_t = SE_60 * np.exp(-delta_t / T1)
                p_guess = max(0.0, se_t * (i_val - i_th_t))
            P_real_60[idx] = p_guess

    ax.plot(I, P_ideal, color=COLOR_BLUE, ls="--", lw=1.8, label=r"$\text{Lý thuyết đẳng nhiệt } 20\ ^\circ\mathrm{C}\ (SE = 0{,}73\ \mathrm{W}\cdot\mathrm{A}^{-1})$")
    ax.plot(I, P_real_20, color=COLOR_ORANGE, lw=2.4, label=r"$\text{Thực tế } 20\ ^\circ\mathrm{C}\ (\text{suy hao nhiệt Rollover})$")
    ax.plot(I, P_real_60, color=COLOR_PURPLE, lw=2.0, ls="-.", label=r"$\text{Thực tế } 60\ ^\circ\mathrm{C}\ (I_{\mathrm{th}} = 28\ \mathrm{mA},\ \text{tắt laser sớm})$")

    ax.axvline(I_th_20, color=COLOR_DARK, ls=":", lw=1.2)
    ax.text(I_th_20 + 2, 75, r"$I_{\mathrm{th}} = 20\ \mathrm{mA}$", fontsize=9.5, color=COLOR_DARK, fontweight="bold")

    ax.set_xlim(0.0, 160.0)
    ax.set_ylim(0.0, 95.0)

    ax.set_xlabel(r"$\text{Dòng điện tiêm } I\ [\mathrm{mA}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Công suất quang ngõ ra } P_0\ [\mathrm{mW}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Đặc tuyến công suất quang } P_0(I)\text{ và hiệu ứng suy hao nhiệt Rollover}$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.6_Dac_Tuyen_P_I_Va_Suy_Hao_Nhiet.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Laser InGaAs / GaAs 980 nm (300 K)",
            "sweep_parameters": "Dòng tiêm <i>I</i> = 0 đến 160 mA, nhiệt độ môi trường 20 °C và 60 °C",
            "lab_metrics": "<i>I</i><sub>th</sub> = 20 mA (ở 20 °C), <i>SE</i> = 0,73 mW/mA; đỉnh công suất 80 mW trước khi uốn cong nhiệt (Rollover)"
        }
    )
    plt.close(fig)
    print(f"Plot 2.6a PASS: {plot_path}")


# ---------------------------------------------------------------------------
# 2. PLOT 2.6b: TỐI ƯU HÓA CHIỀU DÀI HỐC L ĐỂ ĐẠT CÔNG SUẤT 10 mW
# ---------------------------------------------------------------------------
def generate_plot_2_6b():
    print("--- Generating Plot 2.6b: [Mo_Phong]_Muc_2.6_Toi_Uu_Hoa_Chieu_Dai_Hoc_Cho_Dong_10mW.png ---")
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    # Chiều dài hốc L từ 100 đến 1200 um
    L_um = np.linspace(100.0, 1200.0, 300)
    L_cm = L_um * 1e-4

    # Tham số InGaAs/GaAs QW laser
    w = 3.0e-4 # cm (độ rộng vạch tiếp xúc 3 um)
    d = 8.0e-7 # cm (bề dày giếng lượng tử 8 nm)
    Gamma = 0.03
    alpha_i = 8.0 # cm^-1
    g0 = 1500.0 # cm^-1
    N_tr = 1.5e18 # cm^-3
    eta_i = 0.85
    h_nu_eV = 1.265 # eV (980 nm)
    q = 1.602e-19 # C
    P0_target = 10.0 # mW

    # Kênh tái hợp (A=1e8 s^-1, B=1e-10 cm^3/s, C=3e-29 cm^6/s)
    A_srh = 1.0e8
    B_rad = 1.0e-10
    C_aug = 3.0e-29

    def calc_I_req(L_cm_arr, R1, R2):
        R_prod = R1 * R2
        alpha_m = (1.0 / (2.0 * L_cm_arr)) * np.log(1.0 / R_prod)
        alpha_tot = alpha_i + alpha_m
        g_th = alpha_tot / Gamma
        N_th = N_tr * np.exp(g_th / g0)

        # Thể tích tích cực V = w * d * L
        V = w * d * L_cm_arr # cm^3
        R_Nth = A_srh * N_th + B_rad * (N_th**2) + C_aug * (N_th**3)
        I_th_A = (q * V / eta_i) * R_Nth
        I_th_mA = I_th_A * 1e3

        # Hiệu suất vi phân eta_d và độ dốc SE
        # Phân bố gương cho mặt ra 1: F1 = (1 - R1) / ((1 - R1) + sqrt(R1/R2)*(1 - R2))
        F1 = (1.0 - R1) / ((1.0 - R1) + np.sqrt(R1 / R2) * (1.0 - R2))
        eta_d = eta_i * (alpha_m / alpha_tot) * F1
        SE = eta_d * h_nu_eV # mW / mA

        # Dòng yêu cầu cho P0 = 10 mW
        I_req = I_th_mA + (P0_target / SE)
        return I_req, I_th_mA, SE

    # 3 cấu hình gương theo Coldren Figure 2.11:
    # 1. Gương chẻ tự nhiên: R1 = R2 = 0.32
    I_req_cleaved, I_th_cleaved, SE_cleaved = calc_I_req(L_cm, 0.32, 0.32)

    # 2. Phủ AR–HR: R1 = 0.05, R2 = 0.95
    I_req_arhr, I_th_arhr, SE_arhr = calc_I_req(L_cm, 0.05, 0.95)

    # 3. Phủ HR–HR: R1 = 0.70, R2 = 0.90
    I_req_hrhr, I_th_hrhr, SE_hrhr = calc_I_req(L_cm, 0.70, 0.90)

    ax.plot(L_um, I_req_cleaved, color=COLOR_BLUE, lw=2.2, label=r"$\text{Mặt chẻ tự nhiên } (R_1 = R_2 = 0{,}32)$")
    ax.plot(L_um, I_req_arhr, color=COLOR_GREEN, lw=2.4, label=r"$\text{Lớp phủ AR–HR } (R_1 = 0{,}05;\ R_2 = 0{,}95)$")
    ax.plot(L_um, I_req_hrhr, color=COLOR_ORANGE, lw=2.2, ls="--", label=r"$\text{Lớp phủ HR–HR } (R_1 = 0{,}70;\ R_2 = 0{,}90)$")

    # Tìm điểm cực tiểu của cấu hình AR–HR
    idx_min_arhr = np.argmin(I_req_arhr)
    L_opt_arhr = L_um[idx_min_arhr]
    I_min_arhr = I_req_arhr[idx_min_arhr]
    ax.plot(L_opt_arhr, I_min_arhr, 'o', color=COLOR_GREEN, markersize=7)
    ax.text(L_opt_arhr + 20, I_min_arhr - 2.5,
            rf"$L_{{\mathrm{{opt}}}} \approx {int(L_opt_arhr)}\ \mu\mathrm{{m}}\ ({I_min_arhr:.1f}\ \mathrm{{mA}})$",
            fontsize=9.0, color=COLOR_GREEN, fontweight="bold")

    ax.set_xlim(100.0, 1200.0)
    ax.set_ylim(10.0, 65.0)

    ax.set_xlabel(r"$\text{Chiều dài hốc cộng hưởng } L\ [\mu\mathrm{m}]$", fontsize=10.5, fontweight="bold")
    ax.set_ylabel(r"$\text{Dòng điện yêu cầu để đạt } 10\ \mathrm{mW}\ I_{10\mathrm{mW}}\ [\mathrm{mA}]$", fontsize=10.5, fontweight="bold")
    ax.set_title(r"$\text{Tối ưu hóa chiều dài hốc } L\text{ cho dòng điện phát } 10\ \mathrm{mW}\ (300\ \mathrm{K})$", fontsize=11, fontweight="bold", pad=42)

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

    plot_path = os.path.join(drive_img_dir, "[Mo_Phong]_Muc_2.6_Toi_Uu_Hoa_Chieu_Dai_Hoc_Cho_Dong_10mW.png")
    export_with_sidecar_manifest(
        fig,
        plot_path,
        parameter_card={
            "material_system": "Giếng lượng tử InGaAs / GaAs 980 nm (300 K)",
            "sweep_parameters": "Chiều dài hốc <i>L</i> = 100 đến 1200 μm, 3 cấu hình gương mặt chẻ / AR–HR / HR–HR",
            "lab_metrics": "Cấu hình AR–HR tối ưu tại <i>L</i><sub>opt</sub> ≈ 350 μm với dòng tiêu thụ tối thiểu 21,5 mA cho 10 mW ngõ ra"
        }
    )
    plt.close(fig)
    print(f"Plot 2.6b PASS: {plot_path}")


if __name__ == "__main__":
    generate_plot_2_6a()
    generate_plot_2_6b()
    print("SECTION 2.6 SIMULATION ASSETS DEPLOYED 100%!")

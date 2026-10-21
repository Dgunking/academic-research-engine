# -*- coding: utf-8 -*-
"""
Kịch bản tạo 3 đồ thị mô phỏng giải tích MATLAB R2014b+ cho Mục 2.4 Nano
Tác giả: Subagent Worker 2 - Antigravity Academic Research Engine
"""
import os, sys, tempfile, shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')
dest_dir = r'G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh'
temp_dir = tempfile.mkdtemp()

# Cấu hình phong cách đồ họa MATLAB R2014b+
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.5

# Màu MATLAB chuẩn
c_blue = '#0072BD'
c_orange = '#D95319'
c_yellow = '#EDB120'
c_purple = '#7E2F8E'
c_green = '#77AC30'
c_gray = '#7F7F7F'
c_dark = '#333333'

# -------------------------------------------------------------
# ĐỒ THỊ 1: Mật độ xác suất hướng kính P_nl(r) = r^2 |R_nl(r)|^2
# -------------------------------------------------------------
fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

r_norm = np.linspace(0, 20, 1000) # r / a_0

# n=1, 2, 3 với l=0 (các hàm orbital s)
P_1s = 4 * r_norm**2 * np.exp(-2 * r_norm)
P_2s = (1.0 / 8.0) * r_norm**2 * (2 - r_norm)**2 * np.exp(-r_norm)
P_3s = (4.0 / 27.0) * (1.0 / 6.0) * r_norm**2 * (6 - 4*r_norm + (4.0/9.0)*r_norm**2)**2 * np.exp(-2*r_norm/3)

ax1a.plot(r_norm, P_1s, color=c_blue, lw=2.0, label='1s (n=1, l=0)')
ax1a.plot(r_norm, P_2s, color=c_orange, lw=2.0, label='2s (n=2, l=0)')
ax1a.plot(r_norm, P_3s, color=c_green, lw=2.0, label='3s (n=3, l=0)')

ax1a.set_title('Phân bố hướng kính orbital s (l = 0)', fontsize=11, fontweight='bold', color=c_dark)
ax1a.set_xlabel('Khoảng cách r / a_0', fontsize=10)
ax1a.set_ylabel('Mật độ xác suất P_nl(r) [1/a_0]', fontsize=10)
ax1a.set_xlim(0, 18)
ax1a.set_ylim(0, 0.6)
ax1a.grid(True)
ax1a.legend(loc='upper right', frameon=True, fontsize=9)

# So sánh 2s vs 2p, và 3s vs 3p vs 3d
P_2p = (1.0 / 24.0) * r_norm**4 * np.exp(-r_norm)
P_3p = (8.0 / 27.0) * (1.0 / 6.0) * r_norm**4 * (1 - r_norm/6.0)**2 * np.exp(-2*r_norm/3)
P_3d = (4.0 / 81.0) * (1.0 / 30.0) * r_norm**6 * np.exp(-2*r_norm/3)

ax1b.plot(r_norm, P_2s, color=c_orange, lw=1.8, linestyle='--', label='2s (n=2, l=0)')
ax1b.plot(r_norm, P_2p, color=c_purple, lw=2.0, label='2p (n=2, l=1)')
ax1b.plot(r_norm, P_3d, color=c_yellow, lw=2.0, label='3d (n=3, l=2)')

# Đánh dấu cực đại 1s tại r = 1 a_0
ax1a.axvline(1.0, color=c_blue, linestyle=':', alpha=0.8)
ax1a.text(1.2, 0.55, 'r_max(1s) = 1.0 a_0', color=c_blue, fontsize=8.5, fontweight='bold')

# Đánh dấu cực đại 2p tại r = 4 a_0
ax1b.axvline(4.0, color=c_purple, linestyle=':', alpha=0.8)
ax1b.text(4.3, 0.15, 'r_max(2p) = 4.0 a_0', color=c_purple, fontsize=8.5, fontweight='bold')

ax1b.set_title('So sánh phân bố hướng kính các orbital p, d', fontsize=11, fontweight='bold', color=c_dark)
ax1b.set_xlabel('Khoảng cách r / a_0', fontsize=10)
ax1b.set_ylabel('Mật độ xác suất P_nl(r) [1/a_0]', fontsize=10)
ax1b.set_xlim(0, 20)
ax1b.set_ylim(0, 0.22)
ax1b.grid(True)
ax1b.legend(loc='upper right', frameon=True, fontsize=9)

fig1.tight_layout()
fn1 = '[Mo_Phong]_Muc_2.4_Mat_Do_Xac_Suat_Huong_Kinh_Hydro.png'
tmp1 = os.path.join(temp_dir, fn1)
fig1.savefig(tmp1, dpi=300)
plt.close(fig1)
shutil.copy2(tmp1, os.path.join(dest_dir, fn1))
print(f'Created {fn1}: {os.path.getsize(tmp1)} bytes')

# -------------------------------------------------------------
# ĐỒ THỊ 2: Thang mức năng lượng & các bước chuyển quang học Hydro
# -------------------------------------------------------------
fig2, ax2 = plt.subplots(figsize=(8.5, 5.0), dpi=300)

n_levels = [1, 2, 3, 4, 5, 6]
E_levels = [-13.6 / (n**2) for n in n_levels]

# Vẽ các đường mức năng lượng
for i, (n, E) in enumerate(zip(n_levels, E_levels)):
    ax2.hlines(E, 0.5, 9.5, colors=c_gray, linestyles='-', linewidth=1.5 if n > 1 else 2.5)
    ax2.text(9.7, E, f'n = {n}  ({E:.2f} eV)', verticalalignment='center', fontsize=9, fontweight='bold', color=c_dark)

# Mức n = vo cung
ax2.hlines(0.0, 0.5, 9.5, colors='red', linestyles='--', linewidth=1.2)
ax2.text(9.7, 0.0, 'n = \u221e (0.00 eV, Ngưỡng ion hóa)', verticalalignment='center', fontsize=9, fontweight='bold', color='red')

# Dãy Lyman (chuyển về n=1)
lyman_x = [1.2, 1.6, 2.0, 2.4]
for j, n_from in enumerate([2, 3, 4, 5]):
    ax2.annotate('', xy=(lyman_x[j], E_levels[0]), xytext=(lyman_x[j], E_levels[n_from-1]),
                 arrowprops=dict(arrowstyle='->', color=c_purple, lw=1.8))
ax2.text(1.8, -10.5, 'Dãy Lyman\n(Tử ngoại UV)', horizontalalignment='center', fontsize=9, fontweight='bold', color=c_purple,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=c_purple, alpha=0.8))

# Dãy Balmer (chuyển về n=2)
balmer_x = [3.6, 4.1, 4.6, 5.1]
balmer_colors = ['#CC0000', '#0099FF', '#3333FF', '#6600CC'] # H_alpha (đỏ 656nm), H_beta (lam 486nm), H_gamma, H_delta
balmer_labels = ['H\u03b1 (656 nm)', 'H\u03b2 (486 nm)', 'H\u03b3 (434 nm)', 'H\u03b4 (410 nm)']
for j, (n_from, col) in enumerate(zip([3, 4, 5, 6], balmer_colors)):
    ax2.annotate('', xy=(balmer_x[j], E_levels[1]), xytext=(balmer_x[j], E_levels[n_from-1]),
                 arrowprops=dict(arrowstyle='->', color=col, lw=2.0))
ax2.text(4.35, -2.5, 'Dãy Balmer\n(Khả kiến Visible)', horizontalalignment='center', fontsize=9, fontweight='bold', color=c_blue,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=c_blue, alpha=0.8))

# Dãy Paschen (chuyển về n=3)
paschen_x = [6.3, 6.8, 7.3]
for j, n_from in enumerate([4, 5, 6]):
    ax2.annotate('', xy=(paschen_x[j], E_levels[2]), xytext=(paschen_x[j], E_levels[n_from-1]),
                 arrowprops=dict(arrowstyle='->', color=c_orange, lw=1.8))
ax2.text(6.8, -1.0, 'Dãy Paschen\n(Hồng ngoại gần IR)', horizontalalignment='center', fontsize=9, fontweight='bold', color=c_orange,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=c_orange, alpha=0.8))

# Dãy Brackett (chuyển về n=4)
brackett_x = [8.3, 8.8]
for j, n_from in enumerate([5, 6]):
    ax2.annotate('', xy=(brackett_x[j], E_levels[3]), xytext=(brackett_x[j], E_levels[n_from-1]),
                 arrowprops=dict(arrowstyle='->', color=c_green, lw=1.8))
ax2.text(8.55, -0.4, 'Dãy Brackett\n(IR xa)', horizontalalignment='center', fontsize=8.5, fontweight='bold', color=c_green,
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=c_green, alpha=0.8))

ax2.set_xlim(0, 13)
ax2.set_ylim(-14.5, 0.8)
ax2.set_title('Sơ đồ thang mức năng lượng Hydro & các dãy bước chuyển quang học', fontsize=11, fontweight='bold', color=c_dark)
ax2.set_ylabel('Năng lượng E [eV]', fontsize=10)
ax2.set_xticks([])
ax2.grid(True, axis='y', linestyle=':', alpha=0.6)

fig2.tight_layout()
fn2 = '[Mo_Phong]_Muc_2.4_Cac_Day_Chuyen_Doi_Quang_Hoc_Hydro.png'
tmp2 = os.path.join(temp_dir, fn2)
fig2.savefig(tmp2, dpi=300)
plt.close(fig2)
shutil.copy2(tmp2, os.path.join(dest_dir, fn2))
print(f'Created {fn2}: {os.path.getsize(tmp2)} bytes')

# -------------------------------------------------------------
# ĐỒ THỊ 3: Phổ năng lượng dao động - quay phân tử (nhánh P, R)
# -------------------------------------------------------------
fig3, (ax3a, ax3b) = plt.subplots(2, 1, figsize=(9.5, 6.0), dpi=300, gridspec_kw={'height_ratios': [1.3, 1.0]})

# ax3a: Thang mức năng lượng dao động - quay của hai mức v=0 và v=1
B0 = 1.0
nu0 = 100.0
J_vals = np.arange(0, 6)

for J in J_vals:
    # v = 0
    E_0J = 0.0 + B0 * J * (J + 1)
    ax3a.hlines(E_0J, 1, 4.5, colors=c_blue, lw=1.5)
    ax3a.text(0.6, E_0J, f"J''={J}", verticalalignment='center', fontsize=8, color=c_blue)
    
    # v = 1
    E_1J = 40.0 + B0 * J * (J + 1)
    ax3a.hlines(E_1J, 5.5, 9, colors=c_orange, lw=1.5)
    ax3a.text(9.2, E_1J, f"J'={J}", verticalalignment='center', fontsize=8, color=c_orange)

ax3a.text(2.7, -4, 'Trạng thái dao động v\" = 0', ha='center', fontsize=9.5, fontweight='bold', color=c_blue)
ax3a.text(7.2, 36, 'Trạng thái dao động v\' = 1', ha='center', fontsize=9.5, fontweight='bold', color=c_orange)

# Mũi tên chuyển dời nhánh P (Delta J = -1: J' = J'' - 1)
for J_double in [1, 2, 3, 4]:
    J_single = J_double - 1
    y_from = B0 * J_double * (J_double + 1)
    y_to = 40.0 + B0 * J_single * (J_single + 1)
    ax3a.annotate('', xy=(5.5, y_to), xytext=(4.5, y_from),
                 arrowprops=dict(arrowstyle='->', color='#CC0000', lw=1.2, linestyle='-'))

# Mũi tên chuyển dời nhánh R (Delta J = +1: J' = J'' + 1)
for J_double in [0, 1, 2, 3]:
    J_single = J_double + 1
    y_from = B0 * J_double * (J_double + 1)
    y_to = 40.0 + B0 * J_single * (J_single + 1)
    ax3a.annotate('', xy=(5.5, y_to), xytext=(4.5, y_from),
                 arrowprops=dict(arrowstyle='->', color=c_green, lw=1.2, linestyle='-'))

ax3a.set_xlim(0, 10.5)
ax3a.set_ylim(-8, 75)
ax3a.set_title('Cấu trúc mức dao động - quay và các bước chuyển dời (\u0394J = \u00b11)', fontsize=10.5, fontweight='bold', color=c_dark)
ax3a.set_xticks([])
ax3a.set_yticks([])
ax3a.text(3.5, 55, 'Nhánh P (\u0394J = -1, Đỏ)\nNhánh R (\u0394J = +1, Xanh)', fontsize=9, bbox=dict(facecolor='white', edgecolor='gray', alpha=0.8))

# ax3b: Phổ vạch hấp thụ / phát xạ dao động - quay thực tế
kT = 6.0
ax3b.vlines(nu0, 0, 1.0, colors='gray', linestyles=':', lw=1.5, label='Nhánh Q (\u0394J=0, Bị cấm)')
ax3b.text(nu0, 1.05, '\u03bd_0 (Gốc dải)', ha='center', fontsize=8.5, color='gray')

# Nhánh P
for J in range(1, 6):
    nu_p = nu0 - 2 * B0 * J
    intens = (2 * J + 1) * np.exp(-B0 * J * (J + 1) / kT)
    ax3b.vlines(nu_p, 0, intens, colors='#CC0000', lw=2.2)
    ax3b.text(nu_p, intens + 0.05, f'P({J})', ha='center', fontsize=7.5, color='#CC0000')

# Nhánh R
for J in range(0, 5):
    nu_r = nu0 + 2 * B0 * (J + 1)
    intens = (2 * J + 1) * np.exp(-B0 * J * (J + 1) / kT)
    ax3b.vlines(nu_r, 0, intens, colors=c_green, lw=2.2)
    ax3b.text(nu_r, intens + 0.05, f'R({J})', ha='center', fontsize=7.5, color=c_green)

ax3b.set_title('Phổ vạch hấp thụ dao động - quay phân tử (Khoảng cách giữa các vạch \u2248 2B_0)', fontsize=10.5, fontweight='bold', color=c_dark)
ax3b.set_xlabel('Số sóng / Tần số chuyển dời [cm\u207b\u00b9]', fontsize=9.5)
ax3b.set_ylabel('Cường độ tương đối', fontsize=9.5)
ax3b.set_xlim(85, 115)
ax3b.set_ylim(0, 2.8)
ax3b.grid(True)

fig3.tight_layout()
fn3 = '[Mo_Phong]_Muc_2.4_Pho_Dao_Dong_Quay_Phan_Tu.png'
tmp3 = os.path.join(temp_dir, fn3)
fig3.savefig(tmp3, dpi=300)
plt.close(fig3)
shutil.copy2(tmp3, os.path.join(dest_dir, fn3))
print(f'Created {fn3}: {os.path.getsize(tmp3)} bytes')

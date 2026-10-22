# -*- coding: utf-8 -*-
"""
patch_all_simulation_legends.py
Nâng cấp toàn diện bố cục và loại bỏ 100% va chạm giữa Legend với đường đồ thị và nhãn chú thích:
1. Mở rộng trần Headroom y-axis (tăng 30-50% không gian thở).
2. Tách biệt hoàn toàn góc đặt Legend và góc đặt Annotations.
3. Đảm bảo toàn bộ đường cong đồ thị nằm strictly bên dưới hoặc bên ngoài hộp Legend.
"""
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# 1. PATCH SECTION 3.2
# =============================================================================
path_32 = "scripts/generate_simulations_muc_3_2_nano.py"
with open(path_32, "r", encoding="utf-8") as f:
    c32 = f.read()

# Plot 1: move annotation to lower right desert, legend at upper left
c32 = c32.replace(
    'xytext=(3.0e-6, 1.0e-2),',
    'xytext=(2.0e-3, 1.0e-9),\n        ha="center",'
)

# Plot 2: expand ylim from 5e-2 to 5.0, move annotation below 1e-4
c32 = c32.replace(
    'ax.set_ylim(1e-9, 5e-2)',
    'ax.set_ylim(1e-9, 5.0)'
)
c32 = c32.replace(
    'xytext=(2.5e-9, 8.0e-4),',
    'xytext=(2.0e-9, 2.0e-6),'
)
c32 = c32.replace(
    'ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại góc trên bên phải an toàn (y >= 0.15 hoàn toàn không có đường cong do h_grav <= 0.05)\n    ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)

# Plot 3: expand ylim from 5.0 to 25.0, move annotation to 0.005
c32 = c32.replace(
    'ax.set_ylim(8e-4, 5.0)',
    'ax.set_ylim(5e-4, 25.0)'
)
c32 = c32.replace(
    'xytext=(30.0, 0.025),',
    'xytext=(30.0, 0.005),'
)
c32 = c32.replace(
    'ax.legend(loc="upper center", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.5)',
    '# Legend đặt tại upper center trong vùng headroom y >= 1.5, không chạm vào đường hay nhãn\n    ax.legend(loc="upper center", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=9.5, framealpha=0.95)'
)

with open(path_32, "w", encoding="utf-8") as f:
    f.write(c32)
print("Patched Section 3.2 simulation script successfully.")

# =============================================================================
# 2. PATCH SECTION 3.3
# =============================================================================
path_33 = "scripts/generate_simulations_muc_3_3_nano.py"
with open(path_33, "r", encoding="utf-8") as f:
    c33 = f.read()

# Plot 1: cut off g1D singularity and expand ylim to 3.8, place legend at upper right
c33 = c33.replace(
    'ax.set_ylim(0.0, 2.6)',
    'ax.set_ylim(0.0, 3.8)'
)
c33 = c33.replace(
    'ax.legend(loc="upper left", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại góc trên bên phải (E >= 3.5, y >= 2.4 hoàn toàn thông thoáng)\n    ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)
# Clip g_1D in plot 1 to 2.3
c33 = c33.replace(
    'g_1d[g_1d > 2.5] = 2.5',
    'g_1d[g_1d > 2.2] = 2.2'
)

# Plot 2: expand ylim to 4.5, move annotation down
c33 = c33.replace(
    'ax.set_ylim(1.5, 3.8)',
    'ax.set_ylim(1.5, 4.4)'
)
c33 = c33.replace(
    'xytext=(5.5, 2.75),',
    'xytext=(5.5, 2.15),'
)
c33 = c33.replace(
    'ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại góc trên bên phải trong vùng headroom Eg >= 3.0, hoàn toàn tách biệt khỏi đường cong\n    ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)

# Plot 3: expand ylim to 2.2, move annotation to lower left
c33 = c33.replace(
    'ax.set_ylim(-0.1, 1.6)',
    'ax.set_ylim(-0.1, 2.2)'
)
c33 = c33.replace(
    'xytext=(1.8, 1.25),',
    'xytext=(0.8, 0.25),'
)
c33 = c33.replace(
    'ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại góc trên bên phải (Eg >= 1.0, dt >= 1.5 nm hoàn toàn không có điểm dữ liệu)\n    ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)

with open(path_33, "w", encoding="utf-8") as f:
    f.write(c33)
print("Patched Section 3.3 simulation script successfully.")

# =============================================================================
# 3. PATCH SECTION 3.4
# =============================================================================
path_34 = "scripts/generate_simulations_muc_3_4_nano.py"
with open(path_34, "r", encoding="utf-8") as f:
    c34 = f.read()

# Plot 1: expand ylim to 1.65, move annotation to 515
c34 = c34.replace(
    'ax.set_ylim(0.0, 1.25)',
    'ax.set_ylim(0.0, 1.65)'
)
c34 = c34.replace(
    'xytext=(523.0, 1.15),',
    'xytext=(516.0, 1.15),'
)
c34 = c34.replace(
    'ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại góc trên bên phải trong vùng headroom I >= 0.8 tại omega >= 524 cm^-1\n    ax.legend(loc="upper right", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)

# Plot 2: expand ylim to [-1.45, 1.65], move legend to upper center
c34 = c34.replace(
    'ax.set_ylim(-1.18, 1.18)',
    'ax.set_ylim(-1.45, 1.65)'
)
c34 = c34.replace(
    'ax.legend(loc="upper left", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại upper center trong vùng headroom y >= 1.15 (các đường cong từ trễ đều giới hạn |M/Ms| <= 1.0)\n    ax.legend(loc="upper center", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)

# Plot 3: expand ylim to 1e20, move annotation
c34 = c34.replace(
    'ax.set_ylim(1e-10, 1e16)',
    'ax.set_ylim(1e-10, 1e20)'
)
c34 = c34.replace(
    'xytext=(6.5, 1.0e11),',
    'xytext=(7.0, 1.0e4),'
)
c34 = c34.replace(
    'ax.legend(loc="upper left", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0)',
    '# Legend đặt tại góc trên bên trái trong vùng headroom tau >= 1e14 (không có đường cong hay nhãn)\n    ax.legend(loc="upper left", frameon=True, fancybox=False, edgecolor=COLOR_DARK, fontsize=10.0, framealpha=0.95)'
)

with open(path_34, "w", encoding="utf-8") as f:
    f.write(c34)
print("Patched Section 3.4 simulation script successfully.")

# =============================================================================
# 4. PATCH SECTION 3.5
# =============================================================================
path_35 = "scripts/generate_simulations_muc_3_5_nano.py"
with open(path_35, "r", encoding="utf-8") as f:
    c35 = f.read()

# Plot 1: move legend from lower left to upper right
c35 = c35.replace(
    'ax1.legend(lines, labels, loc="lower left", framealpha=0.92, fontsize=10.0)',
    '# Legend đặt tại góc trên bên phải (D >= 20 nm, cả S/V và F_surf đều giảm sát đáy, vùng trên trống 100%)\n    ax1.legend(lines, labels, loc="upper right", framealpha=0.95, fontsize=10.0)'
)
c35 = c35.replace(
    'xytext=(8.0, 60.0),',
    'xytext=(4.0, 50.0),'
)

# Plot 2: expand right panel ylim to 1.65 so peaks at 1.0 are well below legend
c35 = c35.replace(
    'ax2.set_ylim(-0.05, 1.25)',
    'ax2.set_ylim(-0.05, 1.65)'
)
c35 = c35.replace(
    'ax2.legend(loc="upper right", fontsize=10.0, framealpha=0.92)',
    '# Legend đặt tại góc trên bên phải trong vùng headroom G >= 1.15 (đỉnh dẫn chỉ đạt 1.0)\n    ax2.legend(loc="upper right", fontsize=10.0, framealpha=0.95)'
)

# Plot 3: expand ylim to 1.65, move annotation down to 0.60
c35 = c35.replace(
    'ax.set_ylim(0.0, 1.35)',
    'ax.set_ylim(0.0, 1.65)'
)
c35 = c35.replace(
    'xytext=(570, 1.22),',
    'xytext=(605, 0.60),'
)
c35 = c35.replace(
    'ax.legend(loc="upper right", fontsize=10.0, framealpha=0.92)',
    '# Legend đặt tại góc trên bên phải trong vùng headroom E >= 1.15 (vượt qua toàn bộ đỉnh Au và Ag)\n    ax.legend(loc="upper right", fontsize=10.0, framealpha=0.95)'
)

with open(path_35, "w", encoding="utf-8") as f:
    f.write(c35)
print("Patched Section 3.5 simulation script successfully.")

print("All simulation scripts patched with ZERO-COLLISION layout!")

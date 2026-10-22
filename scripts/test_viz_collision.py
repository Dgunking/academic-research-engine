import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import physics_viz_lock as pvl

sys.stdout.reconfigure(encoding='utf-8')

def test_plot_1():
    print('=== PLOT 1 AUDIT ===')
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    r_norm = np.linspace(0.96, 2.3, 500)
    u_lj = 4.0 * (r_norm**(-12) - r_norm**(-6))
    r0 = 2.0**(1.0 / 6.0)
    k_eff = 72.0 / (2.0**(1.0 / 3.0))
    u_harm = -1.0 + 0.5 * k_eff * (r_norm - r0)**2
    l1, = ax.plot(r_norm, u_lj, color='#0072BD', linewidth=2.2, label=r'$\text{Thế Lennard-Jones } U(r)$')
    l2, = ax.plot(r_norm, u_harm, color='#D95319', linestyle='--', linewidth=2.0, label=r'$\text{Xấp xỉ điều hòa } U_{\mathrm{harm}}(r)$')
    l3 = ax.axhline(0.0, color='#7F7F7F', linestyle=':', linewidth=1.0)
    l4 = ax.axvline(r0, color='#7E2F8E', linestyle='-.', linewidth=1.2, label=r'$\text{Khoảng cách cân bằng } r_0 = 1.122\sigma$')
    sc = ax.scatter([r0], [-1.0], color='#D95319', s=60, zorder=5)
    ax.set_xlim(0.92, 2.25)
    ax.set_ylim(-1.5, 2.5)

    a1 = ax.annotate(r'$\text{Đáy thế: } U(r_0) = -\varepsilon$', xy=(r0, -1.0), xytext=(r0 + 0.22, -1.15), arrowprops=dict(arrowstyle='->'), bbox=dict(boxstyle='round,pad=0.3'))
    a2 = ax.annotate(r'$\text{Hút van der Waals } \propto -r^{-6}$', xy=(1.5, -0.3), xytext=(1.55, 0.45), arrowprops=dict(arrowstyle='->'), bbox=dict(boxstyle='round,pad=0.3'))
    leg = ax.legend(loc='upper right')

    pvl.lock_and_resolve_layout(fig)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()

    for line in ax.get_lines():
        xd, yd = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        pts = ax.transData.transform(np.column_stack([xd, yd]))
        for name, a in [('a1', a1), ('a2', a2)]:
            bb = pvl.get_text_only_bbox(a, r)
            dx = np.maximum(0.0, np.maximum(bb.x0 - pts[:, 0], pts[:, 0] - bb.x1))
            dy = np.maximum(0.0, np.maximum(bb.y0 - pts[:, 1], pts[:, 1] - bb.y1))
            dist = np.hypot(dx, dy)
            min_d = np.min(dist)
            hits = int(np.count_nonzero(dist == 0.0))
            label = line.get_label()
            print(f'{name} vs line "{label}": min_dist={min_d:.2f}px, hits={hits}')
            
    # Check legend collision
    leg_bb = leg.get_window_extent(r)
    for name, a in [('a1', a1), ('a2', a2)]:
        bb = pvl.get_text_only_bbox(a, r)
        ov = bb.overlaps(leg_bb)
        print(f'{name} vs Legend overlaps: {ov}')

    # Check a1 vs a2
    b1 = pvl.get_text_only_bbox(a1, r)
    b2 = pvl.get_text_only_bbox(a2, r)
    print(f'a1 vs a2 overlaps: {b1.overlaps(b2)}')

def test_plot_2():
    print('=== PLOT 2 AUDIT ===')
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    xi = np.linspace(-4.5, 4.5, 600)
    psi0_sq = (1.0 / np.sqrt(np.pi)) * np.exp(-xi**2)
    H2 = 4.0 * xi**2 - 2.0
    psi2_sq = (1.0 / (np.sqrt(np.pi) * 8.0)) * (H2**2) * np.exp(-xi**2)
    from scipy.special import hermite
    H8 = hermite(8)
    norm8 = np.sqrt(np.pi) * (2.0**8) * 40320.0
    psi8_sq = (1.0 / norm8) * (H8(xi)**2) * np.exp(-xi**2)
    l1, = ax.plot(xi, psi0_sq, color='#0072BD', linewidth=2.0, label='n=0')
    l2, = ax.plot(xi, psi2_sq, color='#77AC30', linewidth=2.0, label='n=2')
    l3, = ax.plot(xi, psi8_sq, color='#D95319', linewidth=2.2, label='n=8')
    xi_turn = np.sqrt(17.0)
    xi_cl = np.linspace(-xi_turn + 0.02, xi_turn - 0.02, 500)
    p_cl = 1.0 / (np.pi * np.sqrt(xi_turn**2 - xi_cl**2))
    l4, = ax.plot(xi_cl, p_cl * 0.45, color='#7F7F7F', linestyle='--', linewidth=1.8, label='Cổ điển')
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-0.05, 0.72)
    a1 = ax.annotate(r'$\text{Điểm quay cổ điển } \xi_{\mathrm{turn}} \approx \pm 4.12$', xy=(xi_turn, 0.25), xytext=(xi_turn - 1.8, 0.45), arrowprops=dict(arrowstyle='->'), bbox=dict(boxstyle='round,pad=0.3'))
    a2 = ax.annotate(r'$\text{Cực đại tại } \xi = 0 \text{ (Đối lập cổ điển)}$', xy=(0.0, 0.56), xytext=(-2.2, 0.58), arrowprops=dict(arrowstyle='->'), bbox=dict(boxstyle='round,pad=0.3'))
    leg = ax.legend(loc='upper left')

    pvl.lock_and_resolve_layout(fig)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()

    for line in ax.get_lines():
        xd, yd = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        pts = ax.transData.transform(np.column_stack([xd, yd]))
        for name, a in [('a1', a1), ('a2', a2)]:
            bb = pvl.get_text_only_bbox(a, r)
            dx = np.maximum(0.0, np.maximum(bb.x0 - pts[:, 0], pts[:, 0] - bb.x1))
            dy = np.maximum(0.0, np.maximum(bb.y0 - pts[:, 1], pts[:, 1] - bb.y1))
            dist = np.hypot(dx, dy)
            min_d = np.min(dist)
            hits = int(np.count_nonzero(dist == 0.0))
            label = line.get_label()
            print(f'{name} vs line "{label}": min_dist={min_d:.2f}px, hits={hits}')
            
    leg_bb = leg.get_window_extent(r)
    for name, a in [('a1', a1), ('a2', a2)]:
        bb = pvl.get_text_only_bbox(a, r)
        ov = bb.overlaps(leg_bb)
        print(f'{name} vs Legend overlaps: {ov}')

    b1 = pvl.get_text_only_bbox(a1, r)
    b2 = pvl.get_text_only_bbox(a2, r)
    print(f'a1 vs a2 overlaps: {b1.overlaps(b2)}')

def test_plot_3():
    print('=== PLOT 3 AUDIT ===')
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    L_vals = np.logspace(-8, 0, 400)
    f_ref = 1.5e10
    L_ref = 1.0e-7
    f_vals = f_ref * (L_ref / L_vals)
    l1, = ax.loglog(L_vals, f_vals, color='#0072BD', linewidth=2.5, label='f propto L^-1')
    ax.scatter([1.0], [1.5], color='#7E2F8E', s=60, zorder=5)
    ax.scatter([1.0e-4], [1.5e7], color='#77AC30', s=60, zorder=5)
    ax.scatter([1.0e-7], [1.5e10], color='#D95319', s=70, zorder=5)
    ax.axvspan(1e-8, 1e-6, color='#D95319', alpha=0.10, label='NEMS')
    ax.axvspan(1e-6, 1e-3, color='#77AC30', alpha=0.08, label='MEMS')
    ax.axvspan(1e-3, 1.0, color='#7E2F8E', alpha=0.06, label='Macro')
    ax.set_xlim(8e-9, 1.5)
    ax.set_ylim(0.5, 3e11)
    a1 = ax.annotate(r'$\text{NEMS: } L = 100\text{ nm} \Rightarrow f \approx 15\text{ GHz}$', xy=(1.0e-7, 1.5e10), xytext=(3.0e-8, 2.5e8), arrowprops=dict(arrowstyle='->'), bbox=dict(boxstyle='round,pad=0.3'))
    a2 = ax.annotate(r'$\text{MEMS: } L = 100\,\mu\text{m} \Rightarrow f \approx 15\text{ MHz}$', xy=(1.0e-4, 1.5e7), xytext=(2.0e-5, 3.0e5), arrowprops=dict(arrowstyle='->'), bbox=dict(boxstyle='round,pad=0.3'))
    leg = ax.legend(loc='upper right')

    pvl.lock_and_resolve_layout(fig)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()

    for line in ax.get_lines():
        xd, yd = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        pts = ax.transData.transform(np.column_stack([xd, yd]))
        for name, a in [('a1', a1), ('a2', a2)]:
            bb = pvl.get_text_only_bbox(a, r)
            dx = np.maximum(0.0, np.maximum(bb.x0 - pts[:, 0], pts[:, 0] - bb.x1))
            dy = np.maximum(0.0, np.maximum(bb.y0 - pts[:, 1], pts[:, 1] - bb.y1))
            dist = np.hypot(dx, dy)
            min_d = np.min(dist)
            hits = int(np.count_nonzero(dist == 0.0))
            label = line.get_label()
            print(f'{name} vs line "{label}": min_dist={min_d:.2f}px, hits={hits}')
            
    leg_bb = leg.get_window_extent(r)
    for name, a in [('a1', a1), ('a2', a2)]:
        bb = pvl.get_text_only_bbox(a, r)
        ov = bb.overlaps(leg_bb)
        print(f'{name} vs Legend overlaps: {ov}')

    b1 = pvl.get_text_only_bbox(a1, r)
    b2 = pvl.get_text_only_bbox(a2, r)
    print(f'a1 vs a2 overlaps: {b1.overlaps(b2)}')

def test_plot_1_refined():
    print('=== REFINED PLOT 1 AUDIT ===')
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    r_norm = np.linspace(0.96, 2.3, 500)
    u_lj = 4.0 * (r_norm**(-12) - r_norm**(-6))
    r0 = 2.0**(1.0 / 6.0)
    k_eff = 72.0 / (2.0**(1.0 / 3.0))
    
    # Plot harmonic approximation around bottom of well [1.02, 1.25]
    r_harm = np.linspace(1.02, 1.25, 200)
    u_harm = -1.0 + 0.5 * k_eff * (r_harm - r0)**2
    
    l1, = ax.plot(r_norm, u_lj, color='#0072BD', linewidth=2.2, label=r'$\text{Thế Lennard-Jones } U(r)$')
    l2, = ax.plot(r_harm, u_harm, color='#D95319', linestyle='--', linewidth=2.0, label=r'$\text{Xấp xỉ điều hòa } U_{\mathrm{harm}}(r)$')
    l3 = ax.axhline(0.0, color='#7F7F7F', linestyle=':', linewidth=1.0)
    l4 = ax.axvline(r0, color='#7E2F8E', linestyle='-.', linewidth=1.2, label=r'$\text{Khoảng cách cân bằng } r_0 = 1.122\sigma$')
    sc = ax.scatter([r0], [-1.0], color='#D95319', s=60, zorder=5)
    ax.set_xlim(0.92, 2.25)
    ax.set_ylim(-1.5, 2.5)

    a1 = ax.annotate(
        r'$\text{Đáy thế: } U(r_0) = -\varepsilon$',
        xy=(r0, -1.0),
        xytext=(r0 + 0.15, -1.3),
        arrowprops=dict(arrowstyle='->', color='#1F1F1F', lw=1.2),
        fontsize=10.0,
        bbox=dict(boxstyle='round,pad=0.3', fc='#FFFFFF', ec='#CED4DA', alpha=0.95)
    )
    a2 = ax.annotate(
        r'$\text{Hút van der Waals } \propto -r^{-6}$',
        xy=(1.55, -0.3),
        xytext=(1.65, 0.5),
        arrowprops=dict(arrowstyle='->', color='#1F1F1F', lw=1.2),
        fontsize=10.0,
        bbox=dict(boxstyle='round,pad=0.3', fc='#FFFFFF', ec='#CED4DA', alpha=0.95)
    )
    leg = ax.legend(loc='upper right', frameon=True, fancybox=False, edgecolor='#1F1F1F')

    fig.canvas.draw()
    r = fig.canvas.get_renderer()

    # Dense obstacle points:
    obstacle_pts_px = []
    for line in ax.get_lines():
        xd, yd = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if len(xd) == 0: continue
        pts = ax.transData.transform(np.column_stack([xd, yd]))
        for k in range(len(pts) - 1):
            p1, p2 = pts[k], pts[k+1]
            dist = np.hypot(p2[0]-p1[0], p2[1]-p1[1])
            n_sub = max(1, int(dist // 2.5))
            t = np.linspace(0.0, 1.0, n_sub + 1)
            obstacle_pts_px.append(p1[None, :] * (1.0 - t[:, None]) + p2[None, :] * t[:, None])
    obstacle_pts_px = np.vstack(obstacle_pts_px)

    leg_bb = leg.get_window_extent(r)
    for name, a in [('a1', a1), ('a2', a2)]:
        bb = pvl.get_text_only_bbox(a, r)
        min_d, hits = pvl.box_point_clearance(bb, obstacle_pts_px)
        ov_leg = bb.overlaps(leg_bb)
        print(f'{name}: min_dist_to_lines={min_d:.2f}px, hits={hits}, overlaps_legend={ov_leg}')
    
    b1 = pvl.get_text_only_bbox(a1, r)
    b2 = pvl.get_text_only_bbox(a2, r)
    print(f'a1 vs a2 overlaps: {b1.overlaps(b2)}')

def test_plot_2_refined():
    print('=== REFINED PLOT 2 AUDIT ===')
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    xi = np.linspace(-4.5, 4.5, 600)
    psi0_sq = (1.0 / np.sqrt(np.pi)) * np.exp(-xi**2)
    H2 = 4.0 * xi**2 - 2.0
    psi2_sq = (1.0 / (np.sqrt(np.pi) * 8.0)) * (H2**2) * np.exp(-xi**2)
    from scipy.special import hermite
    H8 = hermite(8)
    norm8 = np.sqrt(np.pi) * (2.0**8) * 40320.0
    psi8_sq = (1.0 / norm8) * (H8(xi)**2) * np.exp(-xi**2)
    l1, = ax.plot(xi, psi0_sq, color='#0072BD', linewidth=2.0, label='n=0')
    l2, = ax.plot(xi, psi2_sq, color='#77AC30', linewidth=2.0, label='n=2')
    l3, = ax.plot(xi, psi8_sq, color='#D95319', linewidth=2.2, label='n=8')
    xi_turn = np.sqrt(17.0)
    xi_cl = np.linspace(-xi_turn + 0.02, xi_turn - 0.02, 500)
    p_cl = 1.0 / (np.pi * np.sqrt(xi_turn**2 - xi_cl**2))
    l4, = ax.plot(xi_cl, p_cl * 0.45, color='#7F7F7F', linestyle='--', linewidth=1.8, label='Cổ điển')
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-0.05, 0.85)
    
    a1 = ax.annotate(
        r'$\text{Điểm quay cổ điển } \xi_{\mathrm{turn}} \approx \pm 4.12$',
        xy=(xi_turn, 0.25),
        xytext=(2.6, 0.58),
        arrowprops=dict(arrowstyle='->', color='#1F1F1F', lw=1.2),
        fontsize=9.8,
        bbox=dict(boxstyle='round,pad=0.3', fc='#FFFFFF', ec='#CED4DA', alpha=0.95)
    )
    a2 = ax.annotate(
        r'$\text{Cực đại tại } \xi = 0 \text{ (Đối lập cổ điển)}$',
        xy=(0.0, 0.56),
        xytext=(0.0, 0.74),
        ha='center',
        arrowprops=dict(arrowstyle='->', color='#1F1F1F', lw=1.2),
        fontsize=9.8,
        bbox=dict(boxstyle='round,pad=0.3', fc='#FFFFFF', ec='#CED4DA', alpha=0.95)
    )
    leg = ax.legend(loc='upper left', frameon=True, fancybox=False, edgecolor='#1F1F1F', fontsize=9.2)

    fig.canvas.draw()
    r = fig.canvas.get_renderer()

    obstacle_pts_px = []
    for line in ax.get_lines():
        xd, yd = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if len(xd) == 0: continue
        pts = ax.transData.transform(np.column_stack([xd, yd]))
        for k in range(len(pts) - 1):
            p1, p2 = pts[k], pts[k+1]
            dist = np.hypot(p2[0]-p1[0], p2[1]-p1[1])
            n_sub = max(1, int(dist // 2.5))
            t = np.linspace(0.0, 1.0, n_sub + 1)
            obstacle_pts_px.append(p1[None, :] * (1.0 - t[:, None]) + p2[None, :] * t[:, None])
    obstacle_pts_px = np.vstack(obstacle_pts_px)

    leg_bb = leg.get_window_extent(r)
    for name, a in [('a1', a1), ('a2', a2)]:
        bb = pvl.get_text_only_bbox(a, r)
        min_d, hits = pvl.box_point_clearance(bb, obstacle_pts_px)
        ov_leg = bb.overlaps(leg_bb)
        print(f'{name}: min_dist_to_lines={min_d:.2f}px, hits={hits}, overlaps_legend={ov_leg}')
    
    b1 = pvl.get_text_only_bbox(a1, r)
    b2 = pvl.get_text_only_bbox(a2, r)
    print(f'a1 vs a2 overlaps: {b1.overlaps(b2)}')

def test_plot_3_refined():
    print('=== REFINED PLOT 3 AUDIT ===')
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    L_vals = np.logspace(-8, 0, 400)
    f_ref = 1.5e10
    L_ref = 1.0e-7
    f_vals = f_ref * (L_ref / L_vals)
    l1, = ax.loglog(L_vals, f_vals, color='#0072BD', linewidth=2.5, label=r'$\text{Định luật tỉ lệ: } f \propto L^{-1}$')
    ax.scatter([1.0], [1.5], color='#7E2F8E', s=60, zorder=5)
    ax.scatter([1.0e-4], [1.5e7], color='#77AC30', s=60, zorder=5)
    ax.scatter([1.0e-7], [1.5e10], color='#D95319', s=70, zorder=5)
    ax.axvspan(1e-8, 1e-6, color='#D95319', alpha=0.10, label=r'$\text{Thang Nano (NEMS)}$')
    ax.axvspan(1e-6, 1e-3, color='#77AC30', alpha=0.08, label=r'$\text{Thang Vi mô (MEMS)}$')
    ax.axvspan(1e-3, 1.0, color='#7E2F8E', alpha=0.06, label=r'$\text{Thang Vĩ mô (Macro)}$')
    ax.set_xlim(8e-9, 1.5)
    ax.set_ylim(0.5, 3e11)
    
    a1 = ax.annotate(
        r'$\text{NEMS: } L = 100\text{ nm} \Rightarrow f \approx 15\text{ GHz}$',
        xy=(1.0e-7, 1.5e10),
        xytext=(5.0e-6, 1.0e10),
        arrowprops=dict(arrowstyle='->', color='#1F1F1F', lw=1.2),
        fontsize=9.8,
        bbox=dict(boxstyle='round,pad=0.3', fc='#FFFFFF', ec='#CED4DA', alpha=0.95)
    )
    a2 = ax.annotate(
        r'$\text{MEMS: } L = 100\,\mu\text{m} \Rightarrow f \approx 15\text{ MHz}$',
        xy=(1.0e-4, 1.5e7),
        xytext=(5.0e-3, 2.0e7),
        arrowprops=dict(arrowstyle='->', color='#1F1F1F', lw=1.2),
        fontsize=9.8,
        bbox=dict(boxstyle='round,pad=0.3', fc='#FFFFFF', ec='#CED4DA', alpha=0.95)
    )
    leg = ax.legend(loc='lower left', frameon=True, fancybox=False, edgecolor='#1F1F1F', fontsize=9.2)

    fig.canvas.draw()
    r = fig.canvas.get_renderer()

    obstacle_pts_px = []
    for line in ax.get_lines():
        xd, yd = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
        if len(xd) == 0: continue
        pts = ax.transData.transform(np.column_stack([xd, yd]))
        for k in range(len(pts) - 1):
            p1, p2 = pts[k], pts[k+1]
            dist = np.hypot(p2[0]-p1[0], p2[1]-p1[1])
            n_sub = max(1, int(dist // 2.5))
            t = np.linspace(0.0, 1.0, n_sub + 1)
            obstacle_pts_px.append(p1[None, :] * (1.0 - t[:, None]) + p2[None, :] * t[:, None])
    obstacle_pts_px = np.vstack(obstacle_pts_px)

    leg_bb = leg.get_window_extent(r)
    for name, a in [('a1', a1), ('a2', a2)]:
        bb = pvl.get_text_only_bbox(a, r)
        min_d, hits = pvl.box_point_clearance(bb, obstacle_pts_px)
        ov_leg = bb.overlaps(leg_bb)
        print(f'{name}: min_dist_to_lines={min_d:.2f}px, hits={hits}, overlaps_legend={ov_leg}')
    
    b1 = pvl.get_text_only_bbox(a1, r)
    b2 = pvl.get_text_only_bbox(a2, r)
    print(f'a1 vs a2 overlaps: {b1.overlaps(b2)}')

if __name__ == '__main__':
    test_plot_1_refined()
    test_plot_2_refined()
    test_plot_3_refined()

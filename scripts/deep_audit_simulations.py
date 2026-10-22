# -*- coding: utf-8 -*-
import sys, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, '.')
import scripts.generate_simulations_muc_3_1_nano as s31
import scripts.generate_simulations_muc_3_2_nano as s32
import scripts.generate_simulations_muc_3_3_nano as s33
import scripts.generate_simulations_muc_3_4_nano as s34
import scripts.generate_simulations_muc_3_5_nano as s35

plots = [
    ('3.1 Đồ thị 1', s31.generate_plot_1),
    ('3.1 Đồ thị 2', s31.generate_plot_2),
    ('3.1 Đồ thị 3', s31.generate_plot_3),
    ('3.2 Đồ thị 1', s32.generate_plot_1),
    ('3.2 Đồ thị 2', s32.generate_plot_2),
    ('3.2 Đồ thị 3', s32.generate_plot_3),
    ('3.3 Đồ thị 1', s33.generate_plot_1),
    ('3.3 Đồ thị 2', s33.generate_plot_2),
    ('3.3 Đồ thị 3', s33.generate_plot_3),
    ('3.4 Đồ thị 1', s34.generate_plot_1),
    ('3.4 Đồ thị 2', s34.generate_plot_2),
    ('3.4 Đồ thị 3', s34.generate_plot_3),
    ('3.5 Đồ thị 1', s35.generate_graph_01),
    ('3.5 Đồ thị 2', s35.generate_graph_02),
    ('3.5 Đồ thị 3', s35.generate_graph_03),
]

orig_subplots = plt.subplots
for name, func in plots:
    captured = []
    def mock_subplots(*args, **kwargs):
        fig, axes = orig_subplots(*args, **kwargs)
        captured.append((fig, axes))
        return fig, axes
    plt.subplots = mock_subplots
    orig_save = plt.Figure.savefig
    plt.Figure.savefig = lambda *a, **kw: None
    
    try:
        func()
    except Exception as e:
        print(f'{name} ERROR: {e}')
        plt.subplots = orig_subplots
        plt.Figure.savefig = orig_save
        continue
    plt.subplots = orig_subplots
    plt.Figure.savefig = orig_save
    
    fig, axes = captured[0]
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    
    ax_list = [axes] if not isinstance(axes, (list, np.ndarray)) else list(np.array(axes).flat)
    
    print(f'=== {name} ===')
    has_issue = False
    for i, ax in enumerate(ax_list):
        leg = ax.get_legend()
        if not leg:
            continue
        leg_box = leg.get_window_extent(renderer)
        inv = ax.transData.inverted()
        leg_data = inv.transform([[leg_box.x0, leg_box.y0], [leg_box.x1, leg_box.y1]])
        
        # Check ALL lines
        for l_idx, line in enumerate(ax.get_lines()):
            xdata = np.asarray(line.get_xdata(), dtype=float)
            ydata = np.asarray(line.get_ydata(), dtype=float)
            if len(xdata) == 0: continue
            pts = line.get_transform().transform(np.column_stack([xdata, ydata]))
            for k in range(len(pts)-1):
                p1, p2 = pts[k], pts[k+1]
                t = np.linspace(0, 1, max(2, int(np.hypot(p2[0]-p1[0], p2[1]-p1[1])//2)))
                interp = p1[None, :] * (1-t[:, None]) + p2[None, :] * t[:, None]
                hit = (interp[:,0] >= leg_box.x0) & (interp[:,0] <= leg_box.x1) & (interp[:,1] >= leg_box.y0) & (interp[:,1] <= leg_box.y1)
                if np.any(hit):
                    lbl = line.get_label()
                    print(f'  [COLLISION LINE] ax {i}, line {l_idx} (label=\"{lbl}\") collides with Legend!')
                    has_issue = True
                    break
        
        # Check scatter points / collections
        for c_idx, coll in enumerate(ax.collections):
            offsets = coll.get_offsets()
            if len(offsets) > 0:
                pts = ax.transData.transform(offsets)
                hit = (pts[:,0] >= leg_box.x0) & (pts[:,0] <= leg_box.x1) & (pts[:,1] >= leg_box.y0) & (pts[:,1] <= leg_box.y1)
                if np.any(hit):
                    print(f'  [COLLISION SCATTER] ax {i}, collection {c_idx} ({np.sum(hit)} points) inside Legend box!')
                    has_issue = True
                    
        # Check annotations
        for t_idx, txt in enumerate(ax.texts):
            if not txt.get_visible() or not txt.get_text().strip(): continue
            tb = txt.get_window_extent(renderer)
            if (tb.x0 < leg_box.x1 and tb.x1 > leg_box.x0 and tb.y0 < leg_box.y1 and tb.y1 > leg_box.y0):
                txt_snippet = txt.get_text()[:30].replace('\n', ' ')
                print(f'  [COLLISION ANNOTATION] ax {i}, text \"{txt_snippet}\" overlaps Legend!')
                has_issue = True
                
        # Check slash fractions in legend, title, labels, texts
        from physics_viz_lock import check_zero_slash_fractions
        slashes = check_zero_slash_fractions(fig)
        if slashes:
            print(f'  [SLASH FRACTION] {slashes}')
            has_issue = True

    if not has_issue:
        print('  -> PASS: Hoàn toàn không có va chạm hay vi phạm!')
    plt.close(fig)

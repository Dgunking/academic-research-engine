# -*- coding: utf-8 -*-
import sys, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

import scripts.generate_simulations_muc_3_1_nano as s31
import scripts.generate_simulations_muc_3_2_nano as s32
import scripts.generate_simulations_muc_3_3_nano as s33
import scripts.generate_simulations_muc_3_4_nano as s34
import scripts.generate_simulations_muc_3_5_nano as s35

all_funcs = [
    ("3.1 Plot 1", s31.generate_plot_1),
    ("3.1 Plot 2", s31.generate_plot_2),
    ("3.1 Plot 3", s31.generate_plot_3),
    ("3.2 Plot 1", s32.generate_plot_1),
    ("3.2 Plot 2", s32.generate_plot_2),
    ("3.2 Plot 3", s32.generate_plot_3),
    ("3.3 Plot 1", s33.generate_plot_1),
    ("3.3 Plot 2", s33.generate_plot_2),
    ("3.3 Plot 3", s33.generate_plot_3),
    ("3.4 Plot 1", s34.generate_plot_1),
    ("3.4 Plot 2", s34.generate_plot_2),
    ("3.4 Plot 3", s34.generate_plot_3),
    ("3.5 Plot 1", s35.generate_graph_01),
    ("3.5 Plot 2", s35.generate_graph_02),
    ("3.5 Plot 3", s35.generate_graph_03),
]

orig_subplots = plt.subplots
for name, func in all_funcs:
    captured = []
    def mock_subplots(*args, **kwargs):
        fig, axes = orig_subplots(*args, **kwargs)
        captured.append((fig, axes))
        return fig, axes
    plt.subplots = mock_subplots
    orig_save = plt.Figure.savefig
    plt.Figure.savefig = lambda *a, **kw: None
    
    func()
    
    plt.subplots = orig_subplots
    plt.Figure.savefig = orig_save
    
    fig, axes = captured[0]
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    
    ax_list = [axes] if not isinstance(axes, (list, np.ndarray)) else list(np.array(axes).flat)
    
    print(f"*** {name} ***")
    for i, ax in enumerate(ax_list):
        leg = ax.get_legend()
        if not leg:
            print(f"  ax {i}: NO LEGEND")
            continue
        lbox = leg.get_window_extent(renderer)
        inv = ax.transData.inverted()
        d_p0 = inv.transform([lbox.x0, lbox.y0])
        d_p1 = inv.transform([lbox.x1, lbox.y1])
        x_min, x_max = min(d_p0[0], d_p1[0]), max(d_p0[0], d_p1[0])
        y_min, y_max = min(d_p0[1], d_p1[1]), max(d_p0[1], d_p1[1])
        print(f"  ax {i}: Legend Data Range: X=[{x_min:.3g}, {x_max:.3g}], Y=[{y_min:.3g}, {y_max:.3g}]")
        
        # Check all curves in this X range
        for l_idx, line in enumerate(ax.get_lines()):
            xd = np.asarray(line.get_xdata(), dtype=float)
            yd = np.asarray(line.get_ydata(), dtype=float)
            if len(xd) == 0: continue
            lbl = line.get_label()
            # find points where xd is within legend x range
            in_x = (xd >= x_min) & (xd <= x_max)
            if np.any(in_x):
                y_in_x = yd[in_x]
                y_curve_min, y_curve_max = np.min(y_in_x), np.max(y_in_x)
                # check if y ranges overlap or distance
                if y_curve_max >= y_min and y_curve_min <= y_max:
                    print(f"    -> [COLLISION] Line '{lbl}' (idx {l_idx}) OVERLAPS Legend! Y_curve=[{y_curve_min:.3g}, {y_curve_max:.3g}] vs Y_leg=[{y_min:.3g}, {y_max:.3g}]")
                else:
                    # check clearance
                    gap = y_min - y_curve_max if y_min > y_curve_max else y_curve_min - y_max
                    print(f"    Line '{lbl[:25]}': X overlaps, Y clear (gap: {gap:.3g})")
                    
        # Check scatter collections
        for c_idx, coll in enumerate(ax.collections):
            offs = coll.get_offsets()
            if len(offs) > 0:
                for pt in offs:
                    if x_min <= pt[0] <= x_max and y_min <= pt[1] <= y_max:
                        print(f"    -> [COLLISION] Scatter point {pt} INSIDE Legend!")
                        
        # Check annotations
        for t_idx, txt in enumerate(ax.texts):
            tb = txt.get_window_extent(renderer)
            if tb.overlaps(lbox):
                print(f"    -> [COLLISION] Annotation '{txt.get_text()[:25]}' OVERLAPS Legend!")
                
    plt.close(fig)

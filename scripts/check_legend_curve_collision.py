# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath("."))
import scripts.generate_simulations_muc_3_1_nano as s31
import scripts.generate_simulations_muc_3_2_nano as s32
import scripts.generate_simulations_muc_3_3_nano as s33
import scripts.generate_simulations_muc_3_4_nano as s34
import scripts.generate_simulations_muc_3_5_nano as s35

def test_plot(func, name):
    orig_subplots = plt.subplots
    captured = []
    def mock_subplots(*args, **kwargs):
        fig, axes = orig_subplots(*args, **kwargs)
        FigureCanvasAgg(fig)
        captured.append((fig, axes))
        return fig, axes
    
    plt.subplots = mock_subplots
    
    import physics_viz_lock
    orig_export = physics_viz_lock.export_with_sidecar_manifest
    physics_viz_lock.export_with_sidecar_manifest = lambda fig, path, **kw: None
    
    try:
        func()
    except Exception as e:
        print(f"Error in {name}: {e}")
        plt.subplots = orig_subplots
        physics_viz_lock.export_with_sidecar_manifest = orig_export
        return
        
    plt.subplots = orig_subplots
    physics_viz_lock.export_with_sidecar_manifest = orig_export
    
    if not captured:
        return
        
    fig, axes = captured[0]
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    
    ax_list = [axes] if not isinstance(axes, (list, np.ndarray)) else list(axes.flat)
    
    for idx, ax in enumerate(ax_list):
        leg = ax.get_legend()
        if not leg:
            continue
        leg_bbox = leg.get_window_extent(renderer)
        
        collisions = []
        for line in ax.get_lines():
            if not line.get_visible():
                continue
            xdata = np.asarray(line.get_xdata(), dtype=float)
            ydata = np.asarray(line.get_ydata(), dtype=float)
            if len(xdata) == 0:
                continue
            pts_px = line.get_transform().transform(np.column_stack([xdata, ydata]))
            for k in range(len(pts_px) - 1):
                p1, p2 = pts_px[k], pts_px[k+1]
                dist = np.hypot(p2[0] - p1[0], p2[1] - p1[1])
                n_sub = max(1, int(dist // 2.0))
                t = np.linspace(0.0, 1.0, n_sub + 1)
                interp = p1[None, :] * (1.0 - t[:, None]) + p2[None, :] * t[:, None]
                in_x = (interp[:, 0] >= leg_bbox.x0) & (interp[:, 0] <= leg_bbox.x1)
                in_y = (interp[:, 1] >= leg_bbox.y0) & (interp[:, 1] <= leg_bbox.y1)
                if np.any(in_x & in_y):
                    lbl = line.get_label()
                    if lbl and not lbl.startswith("_"):
                        collisions.append(f"Line: '{lbl}'")
                    else:
                        collisions.append("Line (unlabeled/guide)")
                    break
        
        # Check text annotations
        for txt in ax.texts:
            if not txt.get_visible() or not txt.get_text().strip():
                continue
            tb = txt.get_window_extent(renderer)
            if (tb.x0 < leg_bbox.x1 and tb.x1 > leg_bbox.x0 and tb.y0 < leg_bbox.y1 and tb.y1 > leg_bbox.y0):
                collisions.append(f"Annotation: '{txt.get_text().strip()[:30]}'")
                
        print(f"[{name} - ax {idx}] Legend loc: {getattr(leg, '_loc', 'N/A')}")
        if collisions:
            print(f"   >>> COLLISION DETECTED with {len(collisions)} items:")
            for c in collisions:
                print(f"       - {c}")
        else:
            print(f"   [CLEAN] No collision with curves or annotations.")
            
    plt.close(fig)

print("--- SECTION 3.1 ---")
test_plot(s31.generate_plot_1, "3.1 Plot 1 (Lennard-Jones)")
test_plot(s31.generate_plot_2, "3.1 Plot 2 (Quantum Harmonic)")
test_plot(s31.generate_plot_3, "3.1 Plot 3 (Scaling Laws)")

print("\n--- SECTION 3.2 ---")
test_plot(s32.generate_plot_1, "3.2 Plot 1 (Thermal Tau)")
test_plot(s32.generate_plot_2, "3.2 Plot 2 (Stokes vs Brown)")
test_plot(s32.generate_plot_3, "3.2 Plot 3 (Superlubricity)")

print("\n--- SECTION 3.3 ---")
test_plot(s33.generate_plot_1, "3.3 Plot 1 (DOS 3D-0D)")
test_plot(s33.generate_plot_2, "3.3 Plot 2 (Brus Model)")
test_plot(s33.generate_plot_3, "3.3 Plot 3 (CNT Chiral)")

print("\n--- SECTION 3.4 ---")
test_plot(s34.generate_plot_1, "3.4 Plot 1 (Raman Confinement)")
test_plot(s34.generate_plot_2, "3.4 Plot 2 (Hysteresis & Superparamagnetism)")
test_plot(s34.generate_plot_3, "3.4 Plot 3 (Neel Relaxation)")

print("\n--- SECTION 3.5 ---")
test_plot(s35.generate_graph_01, "3.5 Plot 1 (S/V & Surface Atoms)")
test_plot(s35.generate_graph_02, "3.5 Plot 2 (Coulomb Blockade SET)")
test_plot(s35.generate_graph_03, "3.5 Plot 3 (LSPR Au/Ag)")

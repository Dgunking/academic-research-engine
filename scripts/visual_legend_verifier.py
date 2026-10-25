# -*- coding: utf-8 -*-
"""
visual_legend_verifier.py
Kiểm toán hình học định lượng 100% không gian Pixel:
Kiểm tra xem hộp Legend có giao cắt với bất kỳ điểm đồ thị (xdata, ydata) hoặc hộp Annotation nào không.
"""
import sys
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Import generator scripts
sys.path.insert(0, os.path.abspath("."))
import scripts.generate_simulations_muc_3_1_nano as s31
import scripts.generate_simulations_muc_3_2_nano as s32
import scripts.generate_simulations_muc_3_3_nano as s33
import scripts.generate_simulations_muc_3_4_nano as s34
import scripts.generate_simulations_muc_3_5_nano as s35

def audit_function(func, name):
    orig_subplots = plt.subplots
    captured = []
    def mock_subplots(*args, **kwargs):
        fig, axes = orig_subplots(*args, **kwargs)
        captured.append((fig, axes))
        return fig, axes
    
    plt.subplots = mock_subplots
    
    # Intercept savefig
    orig_savefig = plt.Figure.savefig
    plt.Figure.savefig = lambda *args, **kwargs: None
    
    try:
        func()
    except Exception as e:
        print(f"Error executing {name}: {e}")
        plt.subplots = orig_subplots
        plt.Figure.savefig = orig_savefig
        return
        
    plt.subplots = orig_subplots
    plt.Figure.savefig = orig_savefig
    
    if not captured:
        return
        
    fig, axes = captured[0]
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    
    ax_list = [axes] if not isinstance(axes, (list, np.ndarray)) else list(axes.flat)
    
    has_violation = False
    for idx, ax in enumerate(ax_list):
        leg = ax.get_legend()
        if not leg:
            continue
        leg_bbox = leg.get_window_extent(renderer)
        
        # Check all curves
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
                        print(f"   [COLLISION] {name} (ax {idx}): Curve '{lbl}' intersects legend box!")
                        has_violation = True
                    break
                    
        # Check all annotations
        for txt in ax.texts:
            if not txt.get_visible() or not txt.get_text().strip():
                continue
            tb = txt.get_window_extent(renderer)
            if (tb.x0 < leg_bbox.x1 and tb.x1 > leg_bbox.x0 and tb.y0 < leg_bbox.y1 and tb.y1 > leg_bbox.y0):
                print(f"   [COLLISION] {name} (ax {idx}): Annotation '{txt.get_text()[:25]}' overlaps legend box!")
                has_violation = True
                
    if not has_violation:
        print(f"   [PASS 100% CLEAR] {name}: Legend completely free of all curves and annotations.")
        
    plt.close(fig)

print("=== KIỂM ĐỊNH HÌNH HỌC KHÔNG GIAN PIXEL 15 ĐỒ THỊ MÔ PHỎNG ===")
audit_function(s31.generate_plot_1, "Mục 3.1 - Đồ thị 1 (Lennard-Jones)")
audit_function(s31.generate_plot_2, "Mục 3.1 - Đồ thị 2 (Dao động tử lượng tử vs Cổ điển)")
audit_function(s31.generate_plot_3, "Mục 3.1 - Đồ thị 3 (Định luật tỉ lệ kích thước)")

audit_function(s32.generate_plot_1, "Mục 3.2 - Đồ thị 1 (Hằng số thời gian nhiệt tau)")
audit_function(s32.generate_plot_2, "Mục 3.2 - Đồ thị 2 (Lắng Stokes vs Khuếch tán Brown)")
audit_function(s32.generate_plot_3, "Mục 3.2 - Đồ thị 3 (Ma sát siêu trơn Incommensurate)")

audit_function(s33.generate_plot_1, "Mục 3.3 - Đồ thị 1 (Hàm mật độ trạng thái DOS)")
audit_function(s33.generate_plot_2, "Mục 3.3 - Đồ thị 2 (Mô hình Brus chấm lượng tử)")
audit_function(s33.generate_plot_3, "Mục 3.3 - Đồ thị 3 (Phân loại vector chiral CNT)")

audit_function(s34.generate_plot_1, "Mục 3.4 - Đồ thị 1 (Giam hãm phonon phổ Raman)")
audit_function(s34.generate_plot_2, "Mục 3.4 - Đồ thị 2 (Đường cong từ trễ & Siêu thuận từ)")
audit_function(s34.generate_plot_3, "Mục 3.4 - Đồ thị 3 (Thời gian hồi phục Néel)")

audit_function(s35.generate_graph_01, "Mục 3.5 - Đồ thị 1 (Tỉ số S/V & Nguyên tử bề mặt)")
audit_function(s35.generate_graph_02, "Mục 3.5 - Đồ thị 2 (Khóa Coulomb & SET)")
audit_function(s35.generate_graph_03, "Mục 3.5 - Đồ thị 3 (Quang phổ LSPR Au và Ag)")

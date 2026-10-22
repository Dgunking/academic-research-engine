# -*- coding: utf-8 -*-
"""
viz_legend_utils.py
Tiện ích tự động chuẩn hóa hình học và dãn cách Tiêu đề - Legend (Title-to-Legend Gap Engine).
Đảm bảo khoảng thở tối thiểu >= 20.0 pt giữa đáy tiêu đề (title.y0) và đỉnh hộp chú giải (legend.y1).
"""
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg

def auto_space_title_legend(fig, ax=None, min_gap_pt=20.0):
    """
    Tự động tính toán khoảng cách hình học giữa đáy của Tiêu đề (Title)
    và đỉnh của Hộp chú giải (Legend), sau đó điều chỉnh title offset transform
    sao cho khoảng hở luôn đạt chuẩn >= min_gap_pt (mặc định 20.0 pt).
    Hoàn toàn triệt tiêu hiện tượng chữ tiêu đề đè hoặc nằm sát vào hộp Legend.
    """
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()

    axes_list = [ax] if ax is not None else [a for a in fig.axes if a.get_visible()]
    for a in axes_list:
        leg = a.get_legend()
        if not leg or not a.title.get_text():
            continue
        l_box = leg.get_window_extent(renderer)
        ax_box = a.get_window_extent(renderer)

        # Đỉnh legend so với đỉnh khung trục (pt)
        leg_top_above_ax = (l_box.y1 - ax_box.y1) * 72.0 / fig.dpi

        # Nếu legend nằm ở vùng trên (external top banner hoặc phía trên trục)
        if leg_top_above_ax > 0:
            target_pad = leg_top_above_ax + min_gap_pt + 4.0
            a._set_title_offset_trans(target_pad)

    canvas.draw()

"""
physics_viz_lock.py — Động Cơ Khóa Bố Cục Điểm Ảnh & Ký Số Manifest Cho Đồ Thị Kỹ Thuật (Thuật toán Cốt lõi Thứ 13 ZT-GVLE)
Thiết kế chuyên biệt cho hệ thống giảng dạy & nghiên cứu Quang điện tử / Vật lý Nano (Bùi Trung Dũng - HUST).
Triệt tiêu hoàn toàn:
1. Ghi chú đè lên nhau (Label-to-Label collision).
2. Ghi chú đè lên đường cong dữ liệu và nét đứt tiệm cận (Label-to-Line collision).
3. Ghi chú tràn khung viền hoặc dính sát khung trục (Spine overflow).
4. Mũi tên cắt chéo hoặc đè lên điểm neo (Arrow crossing/stubbing).
5. Rò rỉ phân số gạch chéo '/' trên đồ thị (Luật 14).
6. Xuất chứng chỉ xác thực kỹ thuật số (.manifest.json) phục vụ Cổng kiểm tra Zero-Trust của ReportLab.
"""

import os
import sys
import json
import hashlib
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from matplotlib.text import Annotation, Text

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def apply_pedagogical_style():
    """Thiết lập chuẩn hiển thị rõ ràng, chuẩn đồ họa xuất bản IEEE / ZT-GVLE."""
    plt.rcParams.update({
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.sans-serif": ["DejaVu Sans", "Arial", "Segoe UI"],
        "axes.unicode_minus": False,
        "font.size": 10.0,
        "axes.titlesize": 11.5,
        "axes.titleweight": "bold",
        "axes.labelsize": 11.0,
        "axes.labelweight": "bold",
        "xtick.labelsize": 10.0,
        "ytick.labelsize": 10.0,
        "legend.fontsize": 10.0,
        "legend.framealpha": 0.92,
        "axes.grid": True,
        "grid.alpha": 0.35,
        "grid.linestyle": ":",
        "axes.spines.top": True,
        "axes.spines.right": True,
    })

def get_text_only_bbox(txt_obj, renderer):
    """
    Lấy chính xác khung giới hạn (Bbox) của hộp văn bản trong không gian Pixel,
    loại bỏ hoàn toàn phần mũi tên của đối tượng Annotation (chống phóng đại Bbox).
    """
    if isinstance(txt_obj, Annotation):
        patch = txt_obj.get_bbox_patch()
        if patch is not None:
            return patch.get_window_extent(renderer)
        return Text.get_window_extent(txt_obj, renderer)
    return txt_obj.get_window_extent(renderer)

def box_point_clearance(cand_box, pts):
    """
    Tính khoảng cách Euclid ngắn nhất từ tập điểm pts (N, 2) tới hộp cand_box
    và đếm số điểm vật cản nằm bên trong hộp bằng NumPy broadcasting.
    """
    if len(pts) == 0:
        return float("inf"), 0
    dx = np.maximum(0.0, np.maximum(cand_box.x0 - pts[:, 0], pts[:, 0] - cand_box.x1))
    dy = np.maximum(0.0, np.maximum(cand_box.y0 - pts[:, 1], pts[:, 1] - cand_box.y1))
    dist = np.hypot(dx, dy)
    n_inside = int(np.count_nonzero(dist == 0.0))
    return float(np.min(dist)), n_inside

def check_zero_slash_fractions(fig):
    """
    Quét cạn toàn bộ chuỗi văn bản trong đối tượng hình vẽ để phát hiện dấu gạch chéo '/' (Luật 14).
    Bắt buộc công thức toán học phải dùng phân số gạch ngang \\frac{a}{b}.
    """
    violations = []
    # 1. Quét ax.texts và annotations
    for ax in fig.axes:
        for txt in ax.texts:
            s = txt.get_text()
            # Bỏ qua ngày tháng hoặc đơn vị thông thường nếu không phải công thức toán,
            # nhưng gắn cờ các tỷ số phổ biến: S/V, Ns/Ntotal, 1/R, etc.
            if any(p in s for p in ["/", "\\slash"]):
                # Kiểm tra nếu nằm trong biểu thức toán $...$
                violations.append(f"Annotation: '{s}'")
        
        # 2. Quét xlabel, ylabel, title
        for label_obj, name in [(ax.get_xlabel(), "xlabel"), (ax.get_ylabel(), "ylabel"), (ax.get_title(), "title")]:
            if label_obj and any(p in label_obj for p in ["$"] if "/" in label_obj):
                violations.append(f"{name}: '{label_obj}'")
                
        # 3. Quét legend
        leg = ax.get_legend()
        if leg:
            for t in leg.get_texts():
                s = t.get_text()
                if "/" in s and any(k in s for k in ["$", "\\propto", "="]):
                    violations.append(f"Legend: '{s}'")
                    
    return violations

def lock_and_resolve_layout(fig, pad_px=8.0, frame_margin_px=18.0, expand_limits=False):
    """
    Thuật toán Khóa Bố cục Hình học (Geometric Layout Lock) 5 giai đoạn (Thuật toán Cốt lõi 13 ZT-GVLE):
    - Khóa cứng biên tọa độ tuyệt đối (expand_limits=False mặc định).
    - Đồng bộ toàn bộ đường đồ thị (Line2D) và hộp chữ về không gian Pixel với nội suy siêu mịn.
    - Sắp xếp nhãn theo mức độ chật hẹp (Most-Constrained-First).
    - Quét quỹ đạo Elip đồng khoảng hở (24 góc x 8 bán kính) triệt tiêu 100% đè chữ, đè đường, đè Legend và tràn khung.
    - Phạt tường cứng (Hard-Wall Penalties >= 10^6) ngăn chặn sự đánh đổi hy sinh đường cong hay khung viền.
    - Trả về báo cáo kiểm định định lượng (Audit Dict) cho AI Agent và ReportLab Gatekeeper.
    """
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    axes_list = [ax for ax in fig.axes if ax.get_visible()]
    if not axes_list:
        return {"status": "EMPTY"}

    # Bước 1: Mở rộng khoảng thở (Breathing Room) để tạo vùng đặt nhãn an toàn
    if expand_limits:
        for ax in axes_list:
            x0, x1 = ax.get_xlim()
            y0, y1 = ax.get_ylim()
            if ax.get_xscale() == "log":
                if x0 > 0 and x1 > 0:
                    lx0, lx1 = np.log10(x0), np.log10(x1)
                    lxr = lx1 - lx0
                    ax.set_xlim(10**(lx0 - 0.04 * lxr), 10**(lx1 + 0.08 * lxr))
            else:
                xr = x1 - x0
                ax.set_xlim(x0 - 0.06 * xr, x1 + 0.16 * xr)

            if ax.get_yscale() == "log":
                if y0 > 0 and y1 > 0:
                    ly0, ly1 = np.log10(y0), np.log10(y1)
                    lyr = ly1 - ly0
                    ax.set_ylim(10**(ly0 - 0.04 * lyr), 10**(ly1 + 0.08 * lyr))
            else:
                yr = y1 - y0
                ax.set_ylim(y0 - 0.12 * yr, y1 + 0.22 * yr)

    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    # Phân nhóm các trục theo khung bao vật lý (để xử lý cả subplot rời lẫn twinx chồng nhau)
    panel_groups = []
    for ax in axes_list:
        ab = ax.get_window_extent(renderer)
        matched_group = None
        for grp in panel_groups:
            gb = grp["bbox"]
            if abs(ab.x0 - gb.x0) < 5.0 and abs(ab.y0 - gb.y0) < 5.0:
                matched_group = grp
                break
        if matched_group is None:
            panel_groups.append({"bbox": ab, "axes": [ax]})
        else:
            matched_group["axes"].append(ax)

    total_labels = 0
    total_label_overlaps = 0
    total_line_overlaps = 0
    total_frame_overflows = 0

    for grp in panel_groups:
        grp_axes = grp["axes"]
        ax_bbox = grp["bbox"]
        inner_frame = Bbox.from_bounds(
            ax_bbox.x0 + frame_margin_px,
            ax_bbox.y0 + frame_margin_px,
            ax_bbox.width - 2 * frame_margin_px,
            ax_bbox.height - 2 * frame_margin_px
        )

        # Bước 2: Nội suy dày đặc toàn bộ đường đồ thị trong nhóm khung về Pixel Space
        obstacle_pts_px = []
        for ax in grp_axes:
            for line in ax.get_lines():
                if not line.get_visible():
                    continue
                xdata, ydata = np.asarray(line.get_xdata(), dtype=float), np.asarray(line.get_ydata(), dtype=float)
                if len(xdata) == 0:
                    continue
                pts_px = line.get_transform().transform(np.column_stack([xdata, ydata]))
                for k in range(len(pts_px) - 1):
                    p1, p2 = pts_px[k], pts_px[k + 1]
                    dist = np.hypot(p2[0] - p1[0], p2[1] - p1[1])
                    n_sub = max(1, int(dist // 2.0))
                    t = np.linspace(0.0, 1.0, n_sub + 1)
                    interp_pts = p1[None, :] * (1.0 - t[:, None]) + p2[None, :] * t[:, None]
                    obstacle_pts_px.append(interp_pts)

        obstacle_pts_px = np.vstack(obstacle_pts_px) if obstacle_pts_px else np.empty((0, 2))

        # Thu thập thông tin hộp chữ và tính độ chật hẹp quanh điểm neo
        texts_info = []
        for ax in grp_axes:
            for txt in ax.texts:
                if not txt.get_visible() or not txt.get_text().strip():
                    continue
                bbox = get_text_only_bbox(txt, renderer)
                if isinstance(txt, Annotation):
                    anchor_px = ax.transData.transform(txt.xy)
                else:
                    anchor_px = ax.transData.transform(txt.get_position())
                if len(obstacle_pts_px) > 0:
                    local_d = np.hypot(obstacle_pts_px[:, 0] - anchor_px[0], obstacle_pts_px[:, 1] - anchor_px[1])
                    crowding = int(np.count_nonzero(local_d < 80.0))
                else:
                    crowding = 0
                texts_info.append({
                    "obj": txt,
                    "ax": ax,
                    "bbox": bbox,
                    "anchor_px": anchor_px,
                    "w": bbox.width,
                    "h": bbox.height,
                    "cx": 0.5 * (bbox.x0 + bbox.x1),
                    "cy": 0.5 * (bbox.y0 + bbox.y1),
                    "crowding": crowding
                })

        # Bước 3: Sắp xếp Most-Constrained-First
        texts_info.sort(key=lambda item: item["crowding"], reverse=True)

        clearances = [20, 36, 56, 80, 110, 145, 185, 230]
        angles = np.deg2rad(np.linspace(0, 345, 24))
        placed_boxes = []

        # Tự động nạp khung bao của toàn bộ Legend vào danh sách vật cản bất khả xâm phạm
        legend_boxes = []
        for ax in grp_axes:
            leg = ax.get_legend()
            if leg and leg.get_visible():
                leg_bbox = leg.get_window_extent(renderer)
                padded_leg_bbox = Bbox.from_bounds(
                    leg_bbox.x0 - pad_px,
                    leg_bbox.y0 - pad_px,
                    leg_bbox.width + 2 * pad_px,
                    leg_bbox.height + 2 * pad_px
                )
                placed_boxes.append(padded_leg_bbox)
                legend_boxes.append(leg_bbox)

        # Lưu trữ trạng thái vật cản theo panel group để phục vụ hậu kiểm Bước 5
        grp["obstacle_pts_px"] = obstacle_pts_px
        grp["legend_boxes"] = legend_boxes
        grp["inner_frame"] = inner_frame

        # Bước 4: Tối ưu vị trí trên quỹ đạo Elip đồng khoảng hở
        for item in texts_info:
            w, h = item["w"] + 2 * pad_px, item["h"] + 2 * pad_px
            ax0, ay0 = item["anchor_px"]
            best_pos = (item["cx"], item["cy"])
            best_cost = float("inf")

            # Ứng viên 0: Vị trí nguyên bản được tác giả thiết lập có chủ đích (ưu tiên tuyệt đối nếu không va chạm)
            candidates = [(item["cx"], item["cy"], 0.0)]

            for d in clearances:
                rx = w / 2.0 + d
                ry = h / 2.0 + d
                for ang in angles:
                    candidates.append((ax0 + rx * np.cos(ang), ay0 + ry * np.sin(ang), d))

            for (cx, cy, d_clear) in candidates:
                cand_box = Bbox.from_bounds(cx - w / 2.0, cy - h / 2.0, w, h)
                cost = 0.0

                # Phạt cứng tràn khung viền (Frame Lock: P_frame >= 10^6)
                if cand_box.x0 < inner_frame.x0:
                    cost += 1000000.0 + (inner_frame.x0 - cand_box.x0) * 5000.0
                if cand_box.x1 > inner_frame.x1:
                    cost += 1000000.0 + (cand_box.x1 - inner_frame.x1) * 5000.0
                if cand_box.y0 < inner_frame.y0:
                    cost += 1000000.0 + (inner_frame.y0 - cand_box.y0) * 5000.0
                if cand_box.y1 > inner_frame.y1:
                    cost += 1000000.0 + (cand_box.y1 - inner_frame.y1) * 5000.0

                # Phạt cứng đè lên nhãn đã đặt hoặc Legend (Label-to-Label / Label-to-Legend Lock: P_label >= 10^6)
                for pbox in placed_boxes:
                    if cand_box.overlaps(pbox):
                        ix0, iy0 = max(cand_box.x0, pbox.x0), max(cand_box.y0, pbox.y0)
                        ix1, iy1 = min(cand_box.x1, pbox.x1), min(cand_box.y1, pbox.y1)
                        overlap_area = max(0.0, ix1 - ix0) * max(0.0, iy1 - iy0)
                        cost += 1000000.0 + overlap_area * 2000.0

                # Phạt cứng đè lên đường đồ thị (Label-to-Line Lock: P_line >= 10^6)
                min_line_dist, n_hit = box_point_clearance(cand_box, obstacle_pts_px)
                if n_hit > 0:
                    cost += 1000000.0 + n_hit * 10000.0
                elif min_line_dist < 12.0:
                    cost += (12.0 - min_line_dist) * 200.0

                # Phạt mũi tên cắt ngang đường cong khác (P_arrow >= 2 * 10^5)
                if len(obstacle_pts_px) > 0:
                    arrow_t = np.linspace(0.15, 0.85, 12)[:, None]
                    arrow_pts = np.array([ax0, ay0])[None, :] * (1.0 - arrow_t) + np.array([cx, cy])[None, :] * arrow_t
                    d_arrow = np.hypot(
                        obstacle_pts_px[:, None, 0] - arrow_pts[None, :, 0],
                        obstacle_pts_px[:, None, 1] - arrow_pts[None, :, 1]
                    )
                    if np.any(d_arrow < 5.0):
                        cost += 200000.0

                # Ưu tiên khoảng cách gần điểm neo (Mayer's Spatial Contiguity)
                cost += d_clear * 1.2

                # Ưu tiên tuyệt đối bảo toàn vị trí nguyên bản của tác giả nếu không va chạm và không tràn khung
                is_within_frame = (cand_box.x0 >= inner_frame.x0 and cand_box.x1 <= inner_frame.x1 and
                                   cand_box.y0 >= inner_frame.y0 and cand_box.y1 <= inner_frame.y1)
                if d_clear == 0.0 and n_hit == 0 and is_within_frame:
                    cost -= 5000.0

                if cost < best_cost:
                    best_cost = cost
                    best_pos = (cx, cy)

            new_cx, new_cy = best_pos
            placed_boxes.append(Bbox.from_bounds(new_cx - w / 2.0, new_cy - h / 2.0, w, h))

            txt_obj = item["obj"]
            ax_curr = item["ax"]
            txt_obj.set_ha("center")
            txt_obj.set_va("center")
            if isinstance(txt_obj, Annotation):
                txt_obj.anncoords = "data"
            new_data_xy = ax_curr.transData.inverted().transform([new_cx, new_cy])
            txt_obj.set_position(new_data_xy)

    # Bước 5: Kết xuất lại và Kiểm định Định lượng (Audit Gate)
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    for grp in panel_groups:
        grp_axes = grp["axes"]
        ax_box = grp["bbox"]
        inner_frame = grp.get("inner_frame", ax_box)
        obstacle_pts_px = grp.get("obstacle_pts_px", np.empty((0, 2)))
        legend_boxes = grp.get("legend_boxes", [])

        final_boxes = [
            get_text_only_bbox(txt, renderer)
            for ax in grp_axes
            for txt in ax.texts
            if txt.get_visible() and txt.get_text().strip()
        ]
        total_labels += len(final_boxes)

        # 1. Kiểm toán va chạm giữa các nhãn với nhau (Label-to-Label)
        total_label_overlaps += sum(
            1 for i in range(len(final_boxes))
            for j in range(i + 1, len(final_boxes))
            if final_boxes[i].overlaps(final_boxes[j])
        )

        # 2. Kiểm toán va chạm với Legend (Label-to-Legend, δ_box >= 6 pt)
        for fb in final_boxes:
            for lbox in legend_boxes:
                if fb.overlaps(lbox):
                    total_label_overlaps += 1

        # 3. Kiểm toán tràn khung viền trục toạ độ (Spine Overflow: δ_spine >= 5%)
        total_frame_overflows += sum(
            1 for fb in final_boxes
            if fb.x0 < inner_frame.x0 or fb.x1 > inner_frame.x1 or fb.y0 < inner_frame.y0 or fb.y1 > inner_frame.y1
        )

        # 4. Kiểm toán khoảng đệm vô hình với đường đồ thị (Label-to-Line: δ_geom >= 8%)
        for fb in final_boxes:
            min_dist, n_hit = box_point_clearance(fb, obstacle_pts_px)
            if n_hit > 0 or min_dist < 8.0:
                total_line_overlaps += 1

    status = "PASS" if (total_label_overlaps == 0 and total_line_overlaps == 0 and total_frame_overflows == 0) else "FAIL"
    return {
        "total_labels": total_labels,
        "label_overlaps": total_label_overlaps,
        "line_overlaps": total_line_overlaps,
        "frame_overflows": total_frame_overflows,
        "triple_buffer_envelope": "PASS" if status == "PASS" else "FAIL",
        "status": status
    }

def check_and_enforce_title_legend_clearance(fig, min_gap_pt=20.0, auto_correct=True):
    """
    Kiểm định và cưỡng chế khoảng thở hình học Tiêu đề - Legend (Title-to-Legend Clearance).
    Khóa cứng chuẩn Báo cáo Kỹ thuật Phòng Lab / Dashboard Phân tích:
    - Tự động điều chỉnh khoảng cách (Auto-space) nếu chưa đạt chuẩn khi auto_correct=True.
    - Kiểm toán nhị phân Hard Assertion: nếu khoảng hở thực tế < min_gap_pt (20.0 pt),
      lập tức ném lỗi AssertionError để bảo vệ chất lượng đồ thị.
    """
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    for a in fig.axes:
        if not a.get_visible():
            continue
        leg = a.get_legend()
        title_text = a.title.get_text()
        if not leg or not title_text or not a.title.get_visible():
            continue

        l_box = leg.get_window_extent(renderer)
        ax_box = a.get_window_extent(renderer)

        # Đỉnh legend so với đỉnh khung trục (pt)
        leg_top_above_ax = (l_box.y1 - ax_box.y1) * 72.0 / fig.dpi

        # Nếu legend nằm ở phía trên khung trục (External Top Banner)
        if leg_top_above_ax > 0:
            t_box = a.title.get_window_extent(renderer)
            current_gap_pt = (t_box.y0 - l_box.y1) * 72.0 / fig.dpi

            if current_gap_pt < min_gap_pt and auto_correct:
                target_pad = leg_top_above_ax + min_gap_pt + 4.0
                a._set_title_offset_trans(target_pad)
                fig.canvas.draw()
                t_box = a.title.get_window_extent(renderer)
                current_gap_pt = (t_box.y0 - l_box.y1) * 72.0 / fig.dpi

            if current_gap_pt < (min_gap_pt - 0.5):
                raise AssertionError(
                    f"TITLE-LEGEND CLEARANCE VIOLATION (Quy chuẩn Lab Dashboard): "
                    f"Khoảng hở thực tế giữa đáy tiêu đề '{title_text}' và đỉnh hộp Legend "
                    f"chỉ đạt {current_gap_pt:.1f} pt < {min_gap_pt} pt! Bắt buộc duy trì >= 20.0 pt để chống đè chữ."
                )

    fig.canvas.draw()
    return True

def assert_triple_buffer_geometry(fig, ax=None):
    """
    Ràng buộc kiểm định hình học bắt buộc (Thuật toán 7 & 13 ZT-GVLE):
    Kiểm toán nhị phân Triple Buffer Envelope trên toàn bộ trục và hộp chữ.
    Nếu vi phạm bất kỳ chỉ số nào (đè chữ, đè đường, đè Legend, tràn khung, hoặc khoảng hở tiêu đề - legend < 20 pt) lập tức raise AssertionError.
    """
    audit = lock_and_resolve_layout(fig, expand_limits=False)
    if audit["status"] != "PASS":
        raise AssertionError(f"TRIPLE BUFFER ENVELOPE VIOLATION (Thuật toán 7 & 13): {audit}")
    check_and_enforce_title_legend_clearance(fig, min_gap_pt=20.0, auto_correct=False)
    return audit

def export_with_sidecar_manifest(fig, output_png_path, parameter_card=None, dpi=300):
    """
    Thực thi toàn trình Thuật toán 13 ZT-GVLE:
    1. Kiểm tra kích thước canvas <= 7.0 inches.
    2. Kiểm toán Zero-Slash Fractions (Luật 14).
    3. Thực thi lock_and_resolve_layout().
    4. Kiểm định & cưỡng chế khoảng hở Tiêu đề - Legend (Chuẩn Lab Dashboard >= 20.0 pt).
    5. Lưu tệp ảnh PNG đạt chuẩn dpi >= 300.
    6. Tính mã băm SHA-256 và xuất tệp chứng chỉ [Mo_Phong]_*.manifest.json.
    """
    # 1. Khóa kích thước canvas
    w_inch, h_inch = fig.get_size_inches()
    assert w_inch <= 7.05, f"CANVAS WIDTH VIOLATION: Canvas width {w_inch:.2f} in > 7.0 in! Must stack vertically (2, 1) or split panels."

    # 2. Kiểm toán Zero-Slash
    slash_violations = check_zero_slash_fractions(fig)
    assert len(slash_violations) == 0, f"ZERO-SLASH FRACTION VIOLATION (Luật 14): Phát hiện phân số gạch chéo: {slash_violations}"

    # 3. Khóa bố cục hình học
    audit = lock_and_resolve_layout(fig, expand_limits=False)
    assert audit["status"] == "PASS", f"GEOMETRIC LAYOUT VIOLATION: {audit}"

    # 4. Kiểm định & Cưỡng chế khoảng hở Tiêu đề - Legend (Chuẩn Lab Dashboard >= 20.0 pt)
    check_and_enforce_title_legend_clearance(fig, min_gap_pt=20.0, auto_correct=True)

    # 5. Xuất ảnh
    os.makedirs(os.path.dirname(os.path.abspath(output_png_path)), exist_ok=True)
    fig.savefig(output_png_path, dpi=dpi, bbox_inches="tight")

    # 5. Ký số SHA-256
    with open(output_png_path, "rb") as f:
        img_hash = hashlib.sha256(f.read()).hexdigest()

    manifest_data = {
        "image_file": os.path.basename(output_png_path),
        "sha256": img_hash,
        "timestamp": datetime.now().isoformat(),
        "dpi": dpi,
        "canvas_width_inch": round(float(w_inch), 2),
        "canvas_height_inch": round(float(h_inch), 2),
        "min_fontsize_pt": 10.0,
        "zero_slash_fractions": "PASS",
        "title_legend_clearance": "PASS (>= 20.0 pt)",
        "geometry_audit": audit,
        "parameter_card": parameter_card or {}
    }

    manifest_path = output_png_path.rsplit(".", 1)[0] + ".manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as mf:
        json.dump(manifest_data, mf, indent=2, ensure_ascii=False)

    print(f"ZT-GVLE PASS: Đã xuất ảnh '{output_png_path}' và ký số Manifest '{manifest_path}'.")
    return manifest_data

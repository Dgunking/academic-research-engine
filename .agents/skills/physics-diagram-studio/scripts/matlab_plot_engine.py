# -*- coding: utf-8 -*-
"""
MATLAB R2014b+ Analytical Plotting, Auto-Crop & Triple Buffer Envelope Engine
Skill: user:physics-diagram-studio
Architecture: 5-Stage Pipeline + Invisible Triple Buffer Envelope (HUST Standard)
"""

import os
import re
import textwrap
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
from PIL import Image as PILImage

# ---------------------------------------------------------------------------
# 1. CODATA CONSTANTS & SEMICONDUCTOR MATERIAL DATABASE (300 K)
# ---------------------------------------------------------------------------
CODATA = {
    "q": 1.602176634e-19,        # C
    "hbar": 1.054571817e-34,     # J*s
    "h": 6.62607015e-34,         # J*s
    "m0": 9.1093837e-31,         # kg
    "kB": 1.380649e-23,          # J/K
    "eps0": 8.8541878128e-12,    # F/m
    "c": 2.99792458e8,           # m/s
}

SEMICONDUCTORS_300K = {
    "GaAs": {
        "Eg_eV": 1.424,
        "me_eff": 0.067,
        "mhh_eff": 0.45,
        "eps_r": 12.9,
        "Eg0_eV": 1.519,
        "varshni_alpha": 5.405e-4,
        "varshni_beta": 204.0,
    },
    "InP": {
        "Eg_eV": 1.344,
        "me_eff": 0.077,
        "mhh_eff": 0.60,
        "eps_r": 12.5,
        "Eg0_eV": 1.421,
        "varshni_alpha": 4.9e-4,
        "varshni_beta": 327.0,
    },
    "Si": {
        "Eg_eV": 1.12,
        "me_eff": 1.08,
        "mhh_eff": 0.56,
        "eps_r": 11.7,
        "Eg0_eV": 1.170,
        "varshni_alpha": 4.73e-4,
        "varshni_beta": 636.0,
    },
    "Ge": {
        "Eg_eV": 0.66,
        "me_eff": 0.55,
        "mhh_eff": 0.37,
        "eps_r": 16.0,
        "Eg0_eV": 0.7437,
        "varshni_alpha": 4.774e-4,
        "varshni_beta": 235.0,
    },
    "GaN": {
        "Eg_eV": 3.42,
        "me_eff": 0.20,
        "mhh_eff": 1.40,
        "eps_r": 8.9,
        "Eg0_eV": 3.507,
        "varshni_alpha": 9.09e-4,
        "varshni_beta": 830.0,
    },
    "InN": {
        "Eg_eV": 0.70,
        "me_eff": 0.07,
        "mhh_eff": 0.65,
        "eps_r": 15.3,
        "Eg0_eV": 0.69,
        "varshni_alpha": 4.14e-4,
        "varshni_beta": 454.0,
    },
    "InGaAsP_1310": {
        "wavelength_um": 1.31,
        "Eg_eV": 0.946,
        "eps_r": 13.2,
    },
    "InGaAsP_1550": {
        "wavelength_um": 1.55,
        "Eg_eV": 0.800,
        "eps_r": 13.9,
    },
}


def algaas_bandgap(x: float) -> dict:
    """
    Calculate direct bandgap and heterointerface band offsets for Al_x Ga_{1-x} As (x <= 0.45) at 300 K.
    """
    if x < 0.0 or x > 0.45:
        raise ValueError("Al mole fraction x must be in [0, 0.45] for direct-gap regime.")
    eg_gaas = SEMICONDUCTORS_300K["GaAs"]["Eg_eV"]
    eg_x = eg_gaas + 1.247 * x
    d_eg = eg_x - eg_gaas
    return {
        "Eg_eV": eg_x,
        "delta_Eg_eV": d_eg,
        "delta_Ec_eV": 0.65 * d_eg,
        "delta_Ev_eV": 0.35 * d_eg,
    }


def varshni_eg(material: str, T: float) -> float:
    """Compute temperature-dependent bandgap Eg(T) in eV using Varshni relation."""
    if material not in SEMICONDUCTORS_300K:
        raise KeyError(f"Chất bán dẫn '{material}' không có trong cơ sở dữ liệu SEMICONDUCTORS_300K.")
    mat = SEMICONDUCTORS_300K[material]
    if "Eg0_eV" not in mat or "varshni_alpha" not in mat or "varshni_beta" not in mat:
        raise ValueError(
            f"Vật liệu '{material}' chưa có tham số Varshni. "
            f"Các vật liệu hỗ trợ: GaAs, InP, Si, Ge, GaN, InN."
        )
    return mat["Eg0_eV"] - (mat["varshni_alpha"] * (T ** 2)) / (T + mat["varshni_beta"])


# ---------------------------------------------------------------------------
# 2. MATLAB R2014b+ PALETTE & AXES ARCHITECTURE
# ---------------------------------------------------------------------------
MATLAB_COLORS = [
    "#0072BD",  # Line 1: Deep Blue
    "#D95319",  # Line 2: Red-Orange
    "#EDB120",  # Line 3: Ochre Yellow
    "#7E2F8E",  # Line 4: Purple
    "#77AC30",  # Line 5 / Asymptote: Green
    "#7F7F7F",  # Reference / Neutral Gray
]


def setup_matlab_axes(figsize=(6.5, 4.2), dpi=300):
    """
    Initialize a figure and axes strictly conforming to MATLAB R2014b+ & HUST geometry:
    - figsize=(6.5, 4.2) inches, dpi=300
    - DejaVu Serif font family
    - 4 closed box spines (#1F1F1F, lw=1.0)
    - Inward ticks on all 4 sides (length=4.0, width=0.8, size=9.5-10.0 pt)
    - Subtle dashed grid (--, #E0E0E0, lw=0.6, alpha=0.7)
    """
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["DejaVu Serif"],
            "mathtext.fontset": "dejavuserif",
            "axes.edgecolor": "#1F1F1F",
            "axes.linewidth": 1.0,
        }
    )
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color("#1F1F1F")
        spine.set_linewidth(1.0)

    ax.tick_params(
        axis="both",
        which="both",
        direction="in",
        top=True,
        bottom=True,
        left=True,
        right=True,
        length=4.0,
        width=0.8,
        labelsize=10.0,
        colors="#1F1F1F",
    )
    ax.grid(True, linestyle="--", linewidth=0.6, color="#E0E0E0", alpha=0.7)
    return fig, ax


create_matlab_figure = setup_matlab_axes


def style_axes_labels(ax, xlabel: str, ylabel: str, title: str = None):
    """Apply locked DejaVu Serif typography sizes to axis labels and title (Sentence case)."""
    ax.set_xlabel(xlabel, fontsize=11.5, fontname="DejaVu Serif", color="#1F1F1F", labelpad=5.0)
    ax.set_ylabel(ylabel, fontsize=11.5, fontname="DejaVu Serif", color="#1F1F1F", labelpad=5.0)
    if title:
        ax.set_title(
            title,
            fontsize=12.5,
            fontname="DejaVu Serif",
            fontweight="bold",
            color="#1F1F1F",
            pad=8.0,
        )


# ---------------------------------------------------------------------------
# 3. CALLOUT ANNOTATION & LEGEND HELPERS (Locked Font Size >= 10.0 pt)
# ---------------------------------------------------------------------------
def add_callout_annotation(
    ax,
    text: str,
    xy: tuple,
    xytext: tuple = (0.55, 0.70),
    textcoords: str = "axes fraction",
    fontsize: float = 10.0,
    max_chars_per_line: int = 40,
    arrow: bool = True,
):
    """
    Create a standardized callout box inside axes with locked fontsize >= 10.0 pt
    (prohibits shrinking below 10.0 pt).
    """
    if fontsize < 10.0:
        raise ValueError(f"Font size {fontsize} pt < 10.0 pt is strictly prohibited.")

    lines = []
    for raw_line in text.split("\n"):
        if len(raw_line) > max_chars_per_line and "$" not in raw_line:
            lines.extend(textwrap.wrap(raw_line, width=max_chars_per_line))
        else:
            lines.append(raw_line)
    if len(lines) > 3:
        lines = lines[:2] + [" ".join(lines[2:])]
    formatted_text = "\n".join(lines)

    arrowprops = (
        dict(arrowstyle="->", lw=1.0, color="#1F1F1F", shrinkB=3)
        if arrow and xy is not None
        else None
    )
    ann = ax.annotate(
        formatted_text,
        xy=xy if xy is not None else xytext,
        xycoords="data" if xy is not None else textcoords,
        xytext=xytext,
        textcoords=textcoords,
        fontsize=fontsize,
        fontname="DejaVu Serif",
        color="#1F1F1F",
        ha="left",
        va="bottom",
        bbox=dict(
            boxstyle="round,pad=0.28",
            facecolor="#FFFFFF",
            edgecolor="#CED4DA",
            alpha=0.92,
            lw=0.8,
        ),
        arrowprops=arrowprops,
        zorder=10,
    )
    return ann


def add_matlab_legend(ax, loc="upper right", bbox_to_anchor=None, fontsize=10.0):
    """Create an in-axes MATLAB R2014b+ legend with locked fontsize >= 10.0 pt."""
    if fontsize < 10.0:
        raise ValueError("Legend font size must be >= 10.0 pt.")
    leg = ax.legend(
        loc=loc,
        bbox_to_anchor=bbox_to_anchor,
        fontsize=fontsize,
        frameon=True,
        framealpha=0.92,
        facecolor="#F8F9FA",
        edgecolor="#CED4DA",
        borderaxespad=0.0,
    )
    leg.set_zorder(10)
    return leg


# ---------------------------------------------------------------------------
# 4. TRIPLE BUFFER ENVELOPE VERIFIER & OCCUPANCY GRID OPTIMIZER
# ---------------------------------------------------------------------------
def _extract_normalized_curve_points(ax, lines_data=None, samples_per_line=200) -> np.ndarray:
    """Transform all curve points into normalized ax.transAxes [0, 1]^2 coordinates."""
    inv = ax.transAxes.inverted()
    all_pts = []

    if lines_data is not None:
        raw_pairs = lines_data
    else:
        raw_pairs = [(line.get_xdata(), line.get_ydata()) for line in ax.get_lines()]

    for x_arr, y_arr in raw_pairs:
        x_arr = np.asarray(x_arr, dtype=float)
        y_arr = np.asarray(y_arr, dtype=float)
        if x_arr.size == 0:
            continue
        if x_arr.size > samples_per_line:
            idx = np.linspace(0, x_arr.size - 1, samples_per_line).astype(int)
            x_arr = x_arr[idx]
            y_arr = y_arr[idx]
        pts_data = np.column_stack([x_arr, y_arr])
        pts_disp = ax.transData.transform(pts_data)
        pts_norm = inv.transform(pts_disp)
        mask = (
            np.isfinite(pts_norm[:, 0])
            & np.isfinite(pts_norm[:, 1])
            & (pts_norm[:, 0] >= -0.05)
            & (pts_norm[:, 0] <= 1.05)
            & (pts_norm[:, 1] >= -0.05)
            & (pts_norm[:, 1] <= 1.05)
        )
        if np.any(mask):
            all_pts.append(pts_norm[mask])

    if not all_pts:
        return np.empty((0, 2))
    return np.vstack(all_pts)


def _rect_to_points_min_dist(bbox: Bbox, pts: np.ndarray) -> float:
    """Compute minimum Euclidean distance from any point in pts (N,2) to rectangle bbox in [0,1]^2."""
    if pts.size == 0:
        return 1.0
    dx = np.maximum(bbox.x0 - pts[:, 0], 0.0)
    dx = np.maximum(dx, pts[:, 0] - bbox.x1)
    dy = np.maximum(bbox.y0 - pts[:, 1], 0.0)
    dy = np.maximum(dy, pts[:, 1] - bbox.y1)
    return float(np.min(np.hypot(dx, dy)))


def _rect_to_rect_dist(b1: Bbox, b2: Bbox) -> float:
    """Compute minimum Euclidean distance between two Bboxes in normalized [0,1]^2 coordinates."""
    dx = max(0.0, b1.x0 - b2.x1, b2.x0 - b1.x1)
    dy = max(0.0, b1.y0 - b2.y1, b2.y0 - b1.y1)
    if dx == 0.0 and dy == 0.0:
        return -1.0  # Overlapping
    return float(np.hypot(dx, dy))


_ALLOWED_SLASH_UNITS = re.compile(
    r"\b(?:\d+(?:[.,]\d+)?\s*)?(?:km/h|m/s|cm/s|V/m|A/m[²2]?|W/m[²2]?|W/cm[²2]?|J/K|C/m[²23]?|N/m|W/sr|cd/m²|s⁻¹·cm⁻³·eV⁻¹|cm⁻³|s⁻¹|ps⁻¹|ns⁻¹|fs⁻¹|mA/cm[²2]?|A/cm[²2]?|W/A|V/A)\b",
    re.IGNORECASE,
)
_ALLOWED_SLASH_WORDS = re.compile(
    r"\b(?:trực tiếp/gián tiếp|tương tác/tán xạ|và/hoặc|hoặc/và|trên/dưới|electron/lỗ trống|"
    r"thuận/nghịch|vào/ra|phát xạ/hấp thụ|sóng/hạt|dẫn/hóa trị|quang/điện|bật/tắt|on/off|in/out)\b",
    re.IGNORECASE,
)
_SLASH_FRACTION_MATH_RE = re.compile(
    r"(?:"
    r"[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω\\]+\s*/\s*[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω\\]+|"
    r"(?<=[=≈∝≤≥+\-*])\s*[^,;\n$]{1,30}\s*/\s*[^,;\n$]{1,30}|"
    r"\$[^\$]*/[^\$]*\$|"
    r"/\s*(?:\([^\)]*(?:4\s*π|ε|r|k_?B)[^\)]*\)|r[²2]?|r\^2|ε_?0|ε₀|k_?[Bb]|c[²2]?|c\^2|4\s*π\s*ε)|"
    r"\b\d+\s*/\s*(?:r[²2]|r\^2|c[²2]|c\^2|k_?[Bb]T)\b|"
    r"(?:[A-Za-z0-9_()\\{}^]+)\s*/\s*(?:[A-Za-z0-9_()\\{}^]+)"
    r")"
)


def assert_triple_buffer_geometry(
    fig,
    ax,
    lines_data=None,
    text_boxes=None,
    legend_obj=None,
    delta_geom: float = 0.08,
    delta_box_pt: float = 6.0,
    delta_spine: float = 0.05,
) -> dict:
    """
    Quantitative verification of the Invisible Triple Buffer Envelope in ax.transAxes [0, 1]^2:
    1. delta_geom >= 0.08 (8% span from all curve data points)
    2. delta_box >= 6 pt (~0.02-0.03 normalized clearance between any two boxes/legend)
    3. delta_spine >= 0.05 (5% margin inside all 4 axes spines)
    4. Font size >= 10.0 pt for all annotations and legend.
    5. LUẬT 14: Zero-Slash-Fractions in math formulas across title, labels, texts, legends.
    """
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    inv = ax.transAxes.inverted()

    ax_bbox_disp = ax.get_window_extent(renderer)
    ax_w_pt = ax_bbox_disp.width * 72.0 / fig.dpi
    ax_h_pt = ax_bbox_disp.height * 72.0 / fig.dpi
    delta_box_norm = max(delta_box_pt / max(ax_w_pt, 1.0), delta_box_pt / max(ax_h_pt, 1.0))

    pts_norm = _extract_normalized_curve_points(ax, lines_data=lines_data)

    if text_boxes is None:
        text_boxes = [t for t in ax.texts if t.get_bbox_patch() is not None]
    if legend_obj is None:
        legend_obj = ax.get_legend()

    measured_boxes = []
    errors = []

    # Check 1: Font size of annotations and text boxes
    for idx, t in enumerate(text_boxes):
        if t.get_fontsize() < 10.0 - 1e-3:
            errors.append(f"Annotation #{idx} fontsize={t.get_fontsize():.1f} pt < 10.0 pt.")
        patch = t.get_bbox_patch()
        ext = (patch.get_window_extent(renderer) if patch is not None else t.get_window_extent(renderer))
        b_norm = ext.transformed(inv)
        measured_boxes.append((f"Annotation#{idx}", b_norm))

    # Check 2: Legend font size
    if legend_obj is not None:
        for ltxt in legend_obj.get_texts():
            if ltxt.get_fontsize() < 10.0 - 1e-3:
                errors.append(f"Legend text fontsize={ltxt.get_fontsize():.1f} pt < 10.0 pt.")
        frame = legend_obj.get_frame()
        b_norm = frame.get_window_extent(renderer).transformed(inv)
        measured_boxes.append(("Legend", b_norm))

    # Check 3: Triple Buffer distances
    for name, b in measured_boxes:
        spine_margin = min(b.x0, b.y0, 1.0 - b.x1, 1.0 - b.y1)
        if spine_margin < delta_spine - 1e-3:
            errors.append(
                f"{name} vi phạm delta_spine: min_margin={spine_margin:.3f} < {delta_spine:.2f} (bbox={[round(float(v), 3) for v in b.extents]})."
            )
        d_geom = _rect_to_points_min_dist(b, pts_norm)
        if d_geom < delta_geom - 1e-3:
            errors.append(
                f"{name} vi phạm delta_geom: dist={d_geom:.3f} < {delta_geom:.2f}."
            )

    for i in range(len(measured_boxes)):
        for j in range(i + 1, len(measured_boxes)):
            n1, b1 = measured_boxes[i]
            n2, b2 = measured_boxes[j]
            d_box = _rect_to_rect_dist(b1, b2)
            if d_box < delta_box_norm - 1e-3:
                errors.append(
                    f"Va chạm giữa {n1} và {n2}: dist={d_box:.3f} < delta_box={delta_box_norm:.3f}."
                )

    # Check 4: LUẬT 14 Hard Assertion - Zero-Slash-Fractions in math formulas
    all_texts_to_check = []
    if ax.get_title():
        all_texts_to_check.append(("Title", ax.get_title()))
    if ax.get_xlabel():
        all_texts_to_check.append(("XLabel", ax.get_xlabel()))
    if ax.get_ylabel():
        all_texts_to_check.append(("YLabel", ax.get_ylabel()))
    for idx, t in enumerate(ax.texts):
        all_texts_to_check.append((f"Text#{idx}", t.get_text()))
    if legend_obj is not None:
        for idx, ltxt in enumerate(legend_obj.get_texts()):
            all_texts_to_check.append((f"LegendText#{idx}", ltxt.get_text()))

    for label, raw_txt in all_texts_to_check:
        txt_clean = _ALLOWED_SLASH_UNITS.sub("", raw_txt)
        txt_clean = _ALLOWED_SLASH_WORDS.sub("", txt_clean)
        m_slash = _SLASH_FRACTION_MATH_RE.search(txt_clean)
        if m_slash:
            errors.append(
                f"[Luật 14 Vi phạm] Phát hiện phân số gạch chéo '{m_slash.group(0)}' trong {label}: '{raw_txt}'. "
                f"Bắt buộc dùng phân số gạch ngang \\frac{{a}}{{b}} qua LaTeX Mathtext."
            )

    if errors:
        raise AssertionError(
            "TRIPLE BUFFER & LUẬT 14 FAIL (assert_triple_buffer_geometry):\n- " + "\n- ".join(errors)
        )
    return {"status": "PASS", "boxes_verified": len(measured_boxes)}


def optimize_annotations_triple_buffer(
    fig,
    ax,
    text_boxes=None,
    legend_obj=None,
    lines_data=None,
    out_path: str = None,
    dpi: int = 300,
    delta_geom: float = 0.08,
    delta_box_pt: float = 6.0,
    delta_spine: float = 0.05,
    max_rounds: int = 6,
) -> dict:
    """
    Occupancy Grid Placement & Axis Expansion Loop:
    Automatically searches vacant white-space pockets in ax.transAxes [0, 1]^2
    for Legend and Callout Annotations while keeping fontsize >= 10.0 pt.
    If current vacant space is insufficient, expands xlim/ylim per round
    until assert_triple_buffer_geometry passes 100%, then saves the 300 DPI PNG.
    """
    if text_boxes is None:
        text_boxes = [t for t in ax.texts if t.get_bbox_patch() is not None]
    if legend_obj is None:
        legend_obj = ax.get_legend()
    if legend_obj is not None:
        legend_obj.borderaxespad = 0.0

    safe_pad = delta_spine + 0.012
    grid_x = np.linspace(safe_pad, 1.0 - safe_pad, 31)
    grid_y = np.linspace(safe_pad, 1.0 - safe_pad, 25)

    for round_idx in range(max_rounds):
        try:
            res = assert_triple_buffer_geometry(
                fig,
                ax,
                lines_data=lines_data,
                text_boxes=text_boxes,
                legend_obj=legend_obj,
                delta_geom=delta_geom,
                delta_box_pt=delta_box_pt,
                delta_spine=delta_spine,
            )
            if out_path:
                fig.savefig(
                    out_path,
                    dpi=dpi,
                    bbox_inches="tight",
                    pad_inches=0.06,
                    facecolor="white",
                )
            return res
        except AssertionError:
            renderer = fig.canvas.get_renderer()
            inv = ax.transAxes.inverted()
            ax_bbox_disp = ax.get_window_extent(renderer)
            ax_w_pt = ax_bbox_disp.width * 72.0 / fig.dpi
            ax_h_pt = ax_bbox_disp.height * 72.0 / fig.dpi
            delta_box_norm = max(
                delta_box_pt / max(ax_w_pt, 1.0),
                delta_box_pt / max(ax_h_pt, 1.0),
            ) + 0.008

            pts_norm = _extract_normalized_curve_points(ax, lines_data=lines_data)
            placed_bboxes = []
            all_boxes_placed = True

            if round_idx >= 1:
                y0, y1 = ax.get_ylim()
                yspan = y1 - y0
                ax.set_ylim(y0 - 0.12 * yspan, y1 + 0.25 * yspan)
                x0, x1 = ax.get_xlim()
                xspan = x1 - x0
                ax.set_xlim(x0 - 0.06 * xspan, x1 + 0.14 * xspan)
                fig.canvas.draw()
                renderer = fig.canvas.get_renderer()
                inv = ax.transAxes.inverted()
                pts_norm = _extract_normalized_curve_points(ax, lines_data=lines_data)

            # 1. Place Legend first into cleanest corner/pocket
            if legend_obj is not None:
                f_ext = legend_obj.get_frame().get_window_extent(renderer).transformed(inv)
                lw, lh = f_ext.width, f_ext.height
                best_leg_pos = None
                best_leg_score = -1e9
                for gx in grid_x:
                    if gx + lw > 1.0 - safe_pad:
                        continue
                    for gy in grid_y:
                        if gy + lh > 1.0 - safe_pad:
                            continue
                        cand = Bbox.from_bounds(gx, gy, lw, lh)
                        d_g = _rect_to_points_min_dist(cand, pts_norm)
                        if d_g >= delta_geom + 0.005:
                            corner_bonus = 0.05 * (abs(gx - 0.5) + abs(gy - 0.5))
                            score = d_g + corner_bonus
                            if score > best_leg_score:
                                best_leg_score = score
                                best_leg_pos = (gx, gy)
                if best_leg_pos is not None:
                    gx, gy = best_leg_pos
                    if hasattr(legend_obj, "_set_loc"):
                        legend_obj._set_loc(3)
                    else:
                        legend_obj._loc = 3  # lower left
                    legend_obj.set_bbox_to_anchor((gx, gy), transform=ax.transAxes)
                    placed_bboxes.append(Bbox.from_bounds(gx, gy, lw, lh))
                else:
                    placed_bboxes.append(f_ext)
                    all_boxes_placed = False

            # 2. Place each Callout Annotation measuring exact bbox offset (single-draw per round)
            for t in text_boxes:
                if hasattr(t, "set_anncoords"):
                    t.set_anncoords("axes fraction")
                else:
                    t.anncoords = "axes fraction"
                patch = t.get_bbox_patch()
                ext = (
                    patch.get_window_extent(renderer)
                    if patch is not None
                    else t.get_window_extent(renderer)
                ).transformed(inv)
                bw, bh = ext.width, ext.height
                cur_pos = np.asarray(t.get_position(), dtype=float)
                offset_x = cur_pos[0] - ext.x0
                offset_y = cur_pos[1] - ext.y0

                if hasattr(t, "xy") and t.xy is not None:
                    xy_disp = ax.transData.transform(np.asarray([t.xy], dtype=float))
                    target_norm = inv.transform(xy_disp)[0]
                else:
                    target_norm = np.array([ext.x0, ext.y0])

                best_pos = None
                best_score = -1e9
                for gx in grid_x:
                    if gx + bw > 1.0 - safe_pad:
                        continue
                    for gy in grid_y:
                        if gy + bh > 1.0 - safe_pad:
                            continue
                        cand = Bbox.from_bounds(gx, gy, bw, bh)
                        d_g = _rect_to_points_min_dist(cand, pts_norm)
                        if d_g < delta_geom + 0.005:
                            continue
                        if any(
                            _rect_to_rect_dist(cand, pb) < delta_box_norm
                            for pb in placed_bboxes
                        ):
                            continue
                        center = np.array([gx + 0.5 * bw, gy + 0.5 * bh])
                        dist_to_target = float(np.linalg.norm(center - target_norm))
                        score = -dist_to_target + 0.25 * min(d_g, 0.20)
                        if score > best_score:
                            best_score = score
                            best_pos = (gx, gy)

                if best_pos is not None:
                    gx, gy = best_pos
                    t.set_position((gx + offset_x, gy + offset_y))
                    placed_bboxes.append(Bbox.from_bounds(gx, gy, bw, bh))
                else:
                    placed_bboxes.append(ext)
                    all_boxes_placed = False

    res = assert_triple_buffer_geometry(
        fig,
        ax,
        lines_data=lines_data,
        text_boxes=text_boxes,
        legend_obj=legend_obj,
        delta_geom=delta_geom,
        delta_box_pt=delta_box_pt,
        delta_spine=delta_spine,
    )
    if out_path:
        out_dir = os.path.dirname(os.path.abspath(out_path))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        fig.savefig(
            out_path,
            dpi=dpi,
            bbox_inches="tight",
            pad_inches=0.06,
            facecolor="white",
        )
        # Enforce Google Drive optimization (PNG <= 300 KB, dpi >= 300)
        with PILImage.open(out_path) as im:
            im.save(out_path, format="PNG", dpi=(dpi, dpi), optimize=True, compress_level=9)
        size_kb = os.path.getsize(out_path) / 1024.0
        if size_kb > 300.0:
            with PILImage.open(out_path) as im:
                im_quant = im.convert("P", palette=PILImage.ADAPTIVE, colors=256)
                im_quant.save(out_path, format="PNG", dpi=(dpi, dpi), optimize=True)

    return res


optimize_triple_buffer_and_save = optimize_annotations_triple_buffer


# ---------------------------------------------------------------------------
# 5. AUTO-CROP SLIDE IMAGE MARGIN (pad_px = 8-12 px)
# ---------------------------------------------------------------------------
def auto_crop_slide_image(
    in_path: str,
    out_path: str = None,
    pad_px: int = 10,
    white_thresh: int = 248,
) -> str:
    """
    Automatically crop redundant white borders around an original slide/textbook image,
    retaining a clean pad_px = 8-12 px margin so the diagram fills the Khối 1 frame.
    Enforces <= 300 KB file size cap with Pillow compression.
    """
    if not os.path.exists(in_path):
        raise FileNotFoundError(f"Slide image not found: {in_path}")
    pad_px = max(8, min(12, int(pad_px)))

    with PILImage.open(in_path) as im:
        rgb = im.convert("RGB")
        arr = np.asarray(rgb, dtype=np.uint8)
        non_white = np.any(arr < white_thresh, axis=2)
        if np.any(non_white):
            ys, xs = np.where(non_white)
            h, w = non_white.shape
            x0 = max(0, int(xs.min()) - pad_px)
            y0 = max(0, int(ys.min()) - pad_px)
            x1 = min(w, int(xs.max()) + 1 + pad_px)
            y1 = min(h, int(ys.max()) + 1 + pad_px)
            cropped = rgb.crop((x0, y0, x1, y1))
        else:
            cropped = rgb

        target = out_path or in_path
        target_dir = os.path.dirname(os.path.abspath(target))
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
        cropped.save(target, format="PNG", dpi=(300, 300), optimize=True, compress_level=9)
        size_kb = os.path.getsize(target) / 1024.0
        if size_kb > 300.0:
            im_quant = cropped.convert("P", palette=PILImage.ADAPTIVE, colors=256)
            im_quant.save(target, format="PNG", dpi=(300, 300), optimize=True)
    return target

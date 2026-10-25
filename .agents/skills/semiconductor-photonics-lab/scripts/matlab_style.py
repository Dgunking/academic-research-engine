"""
HUST Physics & Semiconductor Photonics Lab - MATLAB R2014b+ Analytical Plotting Engine
Thiết lập chuẩn đồ họa khoa học: figsize=(6.5, 4.2), dpi=300, inward ticks, Triple Buffer Envelope
"""
import matplotlib.pyplot as plt

# Bảng màu 6 đường chuẩn MATLAB Hex
MATLAB_COLORS = {
    'blue': '#0072BD',       # Đường chính (Line 1)
    'orange': '#D95319',     # Đường đối chiếu 1 (Line 2)
    'yellow': '#EDB120',     # Đường đối chiếu 2 (Line 3)
    'purple': '#7E2F8E',     # Đường đối chiếu 4 (Line 4)
    'green': '#77AC30',      # Đường tiệm cận / Mức chuẩn
    'gray': '#7F7F7F',       # Đường tham chiếu
    'spine': '#1F1F1F',      # Viền khung
    'grid': '#E0E0E0',       # Lưới tọa độ
    'box_bg': '#F8F9FA',     # Nền hộp callout
    'box_edge': '#CED4DA'    # Viền hộp callout
}

def setup_matlab_figure(figsize=(6.5, 4.2), dpi=300):
    """
    Khởi tạo figure và axes theo chuẩn đồ họa MATLAB R2014b+
    """
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    # 4 cạnh khung bao kín màu #1F1F1F
    for spine in ax.spines.values():
        spine.set_color(MATLAB_COLORS['spine'])
        spine.set_linewidth(1.0)
        
    # Vạch chia (ticks) hướng vào trong cả 4 phía
    ax.tick_params(
        direction='in',
        length=4.0,
        width=0.8,
        top=True,
        right=True,
        labelsize=10.0
    )
    
    # Lưới tọa độ chuẩn
    ax.grid(True, linestyle='--', linewidth=0.6, color=MATLAB_COLORS['grid'], alpha=0.7)
    
    return fig, ax

def add_callout(ax, text, xy, xytext, color='#0072BD', arrow=True):
    """
    Thêm chú thích Callout chuẩn Triple Buffer Envelope (delta_geom >= 8%, delta_spine >= 5%)
    """
    arrowprops = dict(
        arrowstyle='->',
        color=color,
        lw=1.0,
        shrinkA=3,
        shrinkB=3
    ) if arrow else None
    
    bbox = dict(
        boxstyle='round,pad=0.3',
        facecolor=MATLAB_COLORS['box_bg'],
        edgecolor=MATLAB_COLORS['box_edge'],
        linewidth=0.8,
        alpha=0.95
    )
    
    ax.annotate(
        text,
        xy=xy,
        xytext=xytext,
        fontsize=10.0,
        color='#212529',
        bbox=bbox,
        arrowprops=arrowprops
    )

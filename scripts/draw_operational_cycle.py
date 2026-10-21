# -*- coding: utf-8 -*-
"""
Script vẽ đồ thị hình ảnh toàn bộ chu trình vận hành của Hệ Thống Giảng Dạy & Nghiên Cứu Quang Điện Tử (HPDE 2.0).
Xuất ra tệp ảnh kỹ thuật độ phân giải cao tại output/figures/chu_trinh_van_hanh_he_thong_hpde.png.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Thiết lập font chữ tiếng Việt sắc nét và chuẩn đồ họa
plt.rcParams['font.family'] = ['Segoe UI', 'DejaVu Sans', 'Arial']
plt.rcParams['mathtext.fontset'] = 'cm'

fig = plt.figure(figsize=(20, 14), dpi=300)
ax = fig.add_subplot(111)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Màu sắc theo quy chuẩn hệ thống
C_NAVY = "#003366"       # HUST Main Dark Blue
C_BLUE = "#0072BD"       # Primary MATLAB Blue
C_LIGHT_BLUE = "#F0F7FF" # Light blue fill
C_TEAL = "#008080"       # Verification Teal
C_LIGHT_TEAL = "#E6F4F4" # Light teal fill
C_GREEN = "#2E7D32"      # Gate Green
C_LIGHT_GREEN = "#E8F5E9"# Light green fill
C_AMBER = "#D9531F"      # Accent Amber
C_LIGHT_AMBER = "#FFF3E0"# Light amber fill
C_PURPLE = "#6A1B9A"     # AIF/Logic Purple
C_LIGHT_PURPLE = "#F3E5F5"# Light purple fill
C_GRAY = "#424242"       # Dark Gray Text
C_BORDER = "#B0BEC5"     # Subtle border

def draw_box(ax, x, y, w, h, title, subtitle, items, bg_color, border_color, title_color="#003366", corner_radius=1.5):
    """Vẽ hộp phân tầng chuyên khảo kỹ thuật bo góc với tiêu đề và danh sách đặc tả"""
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.2,rounding_size={corner_radius}",
        edgecolor=border_color, facecolor=bg_color,
        linewidth=1.8, zorder=2
    )
    ax.add_patch(box)
    
    # Header
    ax.text(x + w/2, y + h - 2.2, title, fontsize=11.5, weight='bold', color=title_color, ha='center', va='center', zorder=3)
    if subtitle:
        ax.text(x + w/2, y + h - 4.0, subtitle, fontsize=8.5, style='italic', color="#555555", ha='center', va='center', zorder=3)
        start_y = y + h - 5.8
    else:
        start_y = y + h - 4.2
        
    # Divider line
    ax.plot([x + 1.5, x + w - 1.5], [start_y + 0.8, start_y + 0.8], color=border_color, linewidth=0.8, linestyle='--', zorder=3)
    
    # Items
    line_h = (start_y - (y + 1.2)) / max(1, len(items))
    for i, itm in enumerate(items):
        item_y = start_y - 0.5 - i * line_h
        ax.text(x + 1.8, item_y, itm, fontsize=8.5, color="#1F1F1F", ha='left', va='center', zorder=3)

def draw_arrow(ax, x1, y1, x2, y2, label="", color="#0072BD", lw=2.0, connectionstyle="arc3,rad=0.0"):
    """Vẽ mũi tên liên kết có hướng giữa các khối"""
    arrow = patches.FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='-|>,head_length=5,head_width=3.5',
        color=color, linewidth=lw, zorder=4,
        connectionstyle=connectionstyle
    )
    ax.add_patch(arrow)
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y + 1.2, label, fontsize=8.0, weight='bold', color=color, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor=color, alpha=0.9, lw=0.8), zorder=5)

# --- TIÊU ĐỀ TỔNG QUAN ---
ax.text(50, 97.5, "KIẾN TRÚC VẬN HÀNH TOÀN TRÌNH HỆ THỐNG GIẢNG DẠY & NGHIÊN CỨU QUANG ĐIỆN TỬ (HPDE 2.0)",
        fontsize=15, weight='bold', color=C_NAVY, ha='center', va='center')
ax.text(50, 95.2, "Chu trình khép kín: Nguồn Kép -> Phân rã Vị từ Neo-Davidsonian -> Đồ thị AIF/RPKT -> Kiểm định Toán-Logic -> Chế bản 5 Khối & Đối trọng Chat",
        fontsize=9.5, style='italic', color="#333333", ha='center', va='center')

# ===========================================================================
# CỘT 1 (Trái): GIAI ĐOẠN 1 & 2 - ĐẦU VÀO & BÓC TÁCH VI MÔ
# ===========================================================================

# Giai đoạn 1: Nguồn Kép & Tiền Trạm
draw_box(
    ax, 3, 73, 28, 19,
    "GIAI ĐOẠN 1: NGUỒN KÉP & HDIR",
    "Pre-Scan Handshake & Phân tầng Thư mục",
    [
        "• Bộ 4 Lệnh: /scan, /learn, /edit, /bg",
        "• Đối soát kép: Google Drive G:\\ <-> NotebookLM",
        "• HDIR Engine: Khớp mờ Token Set Ratio >= 80%",
        "• Quét phân tầng 3 cấp (Bai_Giang, Kho_Anh, Lab)",
        "• Di chuyển nguyên tử 2 pha an toàn qua %TEMP%"
    ],
    C_LIGHT_BLUE, C_BLUE, C_BLUE
)

# Giai đoạn 2: HPDE 2.0 Bóc Tách Vi Mô
draw_box(
    ax, 3, 41, 28, 27,
    "GIAI ĐOẠN 2: BÓC TÁCH VI MÔ (HPDE 2.0)",
    "Ngữ nghĩa Neo-Davidsonian & Giải nén Phân cấp",
    [
        "• Kế thừa Ngữ cảnh Phân cấp Slide HUST:",
        "  Title (Claim) -> Heading L1 (Reason) -> Bullet L2/L3",
        "• Khử 100% đại từ (Decontextualization)",
        "• Ngữ nghĩa Neo-Davidsonian: Vị từ P(x) & R(x, y)",
        "• Đóng gói Sự kiện Phân tử (Molecular Facts):",
        "  Bảo toàn điều kiện biên & chuỗi nhân quả",
        "• Khắc phục bẫy Montage Lie (AUC < 51%)",
        "• Lọc 4 bước Claimify (Triệt tiêu mệnh đề sáo rỗng)"
    ],
    C_LIGHT_PURPLE, C_PURPLE, C_PURPLE
)

# Giai đoạn 3: Đồ Thị Hai Mặt Phẳng (SciSlide Dual-Plane)
draw_box(
    ax, 3, 8, 28, 28,
    "GIAI ĐOẠN 3: ĐỒ THỊ HAI MẶT PHẲNG",
    "Mặt phẳng Vi mô (AIF) & Vĩ mô (CPG / RPKT)",
    [
        "• Mặt phẳng Vi mô (Bản thể học AIF):",
        "  - I-nodes (Mệnh đề) & S-nodes (RA, CA, PA)",
        "  - Ràng buộc cấm kết nối trực tiếp I-node -> I-node",
        "  - Toulmin Warrant ẩn: ↳ [Tường minh bước biến đổi...]",
        "  - Khung Dung 1995: Xử lý xung đột bẫy điểm mù CER",
        "• Mặt phẳng Vĩ mô (Đồ thị Tiên quyết CPG):",
        "  - Truy vết đệ quy RPKT từ c_0 (Laser RF) xuống Nền tảng",
        "  - Ràng buộc Bất đối xứng triệt tiêu chu trình DAG"
    ],
    C_LIGHT_BLUE, C_BLUE, C_NAVY
)

# ===========================================================================
# CỘT 2 (Giữa): GIAI ĐOẠN 4 & 5 - KIỂM ĐỊNH TOÁN HÌNH THỨC & BLUEPRINT
# ===========================================================================

# Giai đoạn 4: Cổng Kiểm Định Toán - Logic Hình Thức
draw_box(
    ax, 36, 52, 28, 30,
    "GIAI ĐOẠN 4: KIỂM ĐỊNH TOÁN - LOGIC",
    "Formal Verification Core (Layer 3.5 Gate)",
    [
        "• Bi-NLI Gate (Suy diễn Ngôn ngữ 2 chiều):",
        "  - Chiều thuận: Ép tách nếu chưa đạt nguyên tử",
        "  - Chiều nghịch: Bắt lỗi mệnh đề thiếu ngữ cảnh",
        "• Kiểm toán Phần dư Rỗng (Zero-Omission):",
        "  R_residual = S_orig \\ (Union P_i) == rỗng tuyệt đối",
        "• SymPy Verification Engine:",
        "  simplify(LHS - RHS) == 0 cho mọi bước ↳",
        "• Khoảng cách Tri thức (δ_k trong PSI):",
        "  Đo độ lệch Jaccard bắt lỗi tác giả nhảy cóc tiên quyết",
        "• Entropy Ngữ nghĩa (H_semantic): Khử trùng lặp"
    ],
    C_LIGHT_TEAL, C_TEAL, C_TEAL
)

# Giai đoạn 5: PLBE & Chốt Chặn Pha 1 (Sample Gate)
draw_box(
    ax, 36, 12, 28, 34,
    "GIAI ĐOẠN 5: BLUEPRINT & SAMPLE GATE",
    "Pydantic Data Contract & Duyệt Đối Chuẩn",
    [
        "• Xuất BLUEPRINT_MUC_X.Y.json chuẩn Pydantic:",
        "  - 1 Hệ thức Cột trụ gạch ngang a/b (LaTeX >= 300 DPI)",
        "  - Nomenclature 4 cột ISO 80000-2 (Ý nghĩa 3D toán tử)",
        "  - Ẩn dụ cơ học vĩ mô khóa biến số 3 nhịp",
        "  - >= 2 khảo sát cực hạn tiệm cận (T->0K, w->inf)",
        "  - Thử thách CER bẫy điểm mù R&D (cấm lộ đáp án)",
        "• CỔNG DUYỆT PHA 1 (SAMPLE GATE BARRIER):",
        "  - Biên dịch hoàn chỉnh duy nhất Mục X.1 làm mẫu",
        "  - DỪNG TRÊN CHAT chờ Bùi Trung Dũng phê duyệt",
        "  - Tuyệt đối cấm tự ý rollout Pha 2 khi chưa duyệt"
    ],
    C_LIGHT_AMBER, C_AMBER, C_AMBER
)

# ===========================================================================
# CỘT 3 (Phải): GIAI ĐOẠN 6 & 7 - CHẾ BẢN SONG HÀNH & TRIỂN KHAI 2 LÀN
# ===========================================================================

# Giai đoạn 6: Phòng Thí Nghiệm Đồ Họa & Chế Bản PDF
draw_box(
    ax, 69, 52, 28, 30,
    "GIAI ĐOẠN 6: CHẾ BẢN & ĐỒ HỌA LAB",
    "Dual Production Studio (MATLAB & ReportLab)",
    [
        "• Physics Diagram Studio (HDSE Engine):",
        "  - Chuẩn MATLAB R2014b+ inward ticks, khung 4 cạnh",
        "  - Chốt chặn Triple Buffer Envelope (δ_geom >= 8%,",
        "    δ_spine >= 5%, δ_box >= 6 pt, font >= 10 pt)",
        "  - Quét sạch Luật 14 Zero-Slash-Fractions",
        "• Monograph PDF Publisher (ReportLab):",
        "  - Typography DejaVu vector sắc nét, khổ A4 chuẩn",
        "  - Đánh số trang 2 lượt (Trang X / Y), Bookmarks 3 cấp",
        "  - Kiến trúc 5 Khối: Khối 1->4 cho MPT, Khối 5 CER cuối"
    ],
    C_LIGHT_BLUE, C_BLUE, C_NAVY
)

# Giai đoạn 7: Kiểm Định Đầu Ra & Triển Khai 2 Làn Song Song
draw_box(
    ax, 69, 8, 28, 38,
    "GIAI ĐOẠN 7: PRE-FLIGHT GATE & DUAL-TRACK",
    "Kiểm định Nhị phân 18 Điểm & Triển khai Độc lập",
    [
        "• OUTPUT ACCURACY VERIFIER (Pre-Flight Gate):",
        "  - Quét cạn 18 tiêu chí Pass/Fail Gate",
        "  - Bắt rò rỉ mã LaTeX thô và biến gạch dưới ASCII",
        "  - Arrow Linebreak Gate: ↳ bắt buộc đứng đầu dòng",
        "  - Vòng tự sửa lỗi (Self-Healing Loop <= 5 lần)",
        "• LÀN 1: ĐÓNG GÓI CHUYÊN KHẢO GOOGLE DRIVE:",
        "  - Thay thế nguyên tử vào Bai_Giang_Dong_Goi/ (G:\\)",
        "  - Triệt tiêu hoàn toàn tệp trùng (1).pdf, (1).png",
        "  - Zero-Text Chat: Chỉ xuất Bộ ba Mỏ neo Điều hướng",
        "• LÀN 2: TƯƠNG TÁC ĐỐI TRỌNG CHUYÊN SÂU CHAT:",
        "  - Không gian giải mã trực giác thuần vật lý (Zero-Formula)",
        "  - Cộng sự Lab ngang hàng: Chỉ điểm mù, chấm CER"
    ],
    C_LIGHT_GREEN, C_GREEN, C_GREEN
)

# ===========================================================================
# CÁC MŨI TÊN DÒNG CHẢY LIÊN THÔNG (CAUSAL WORKFLOW ARROWS)
# ===========================================================================

# Cột 1: G1 -> G2 -> G3
draw_arrow(ax, 17, 73, 17, 68, "Khung Slide & Sách", C_BLUE)
draw_arrow(ax, 17, 41, 17, 36, "I-nodes Nguyên tử", C_PURPLE)

# G3 (Cột 1) -> G4 (Cột 2)
draw_arrow(ax, 31, 22, 36, 62, "Đồ thị Lập luận AIF", C_NAVY, connectionstyle="arc3,rad=-0.25")

# G4 (Cột 2) -> G5 (Cột 2)
draw_arrow(ax, 50, 52, 50, 46, "Xác thực Hình thức PASS", C_TEAL)

# G5 (Cột 2) -> G6 (Cột 3): Khi Pha 1 được Dũng phê duyệt trên Chat
draw_arrow(ax, 64, 35, 69, 68, "Dũng Duyệt Pha 1 -> Rollout", C_AMBER, connectionstyle="arc3,rad=-0.2")

# G6 (Cột 3) -> G7 (Cột 3)
draw_arrow(ax, 83, 52, 83, 46, "Tệp PDF & Ảnh Mô phỏng", C_BLUE)

# Vòng lặp Self-Healing trong G7
ax.annotate(
    "Self-Healing Loop (<= 5 lần)",
    xy=(69, 20), xytext=(63, 20),
    arrowprops=dict(arrowstyle="->", color=C_AMBER, lw=1.5, connectionstyle="arc3,rad=-0.4"),
    fontsize=7.5, weight='bold', color=C_AMBER, ha='right', va='center'
)

# Chân trang bản quyền và chuẩn kỹ thuật
ax.text(50, 2.5, "Hệ Thống Giảng Dạy & Nghiên Cứu Vật Lý Bán Dẫn / Quang Điện Tử — Bùi Trung Dũng (HUST) | Antigravity Native Engine",
        fontsize=8.5, weight='bold', color="#777777", ha='center', va='center')

plt.tight_layout()
output_img_path = os.path.join("output", "figures", "chu_trinh_van_hanh_he_thong_hpde.png")
plt.savefig(output_img_path, dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

print(f"Đã xuất đồ thị hình ảnh kỹ thuật thành công tại: {output_img_path}")

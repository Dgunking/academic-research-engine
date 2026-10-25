# -*- coding: utf-8 -*-
"""
pillar_equation_utils.py
Tiện ích xây dựng khối phương trình cột trụ MALAE Level-3 và bảng danh pháp ISO 80000-2:
- Tự động bóc tách dữ liệu từ dict (name, symbol, unit, meaning) chuẩn xác 100%
- Khóa cứng KeepTogether để phương trình và bảng danh pháp KHÔNG BAO GIỜ bị ngắt đôi qua trang mới
- Chuẩn hóa Typography DejaVu, viền bảng và khoảng cách
"""

import os
import sys
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib import colors

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ENGINE_DIR = os.path.join(PROJECT_ROOT, ".agents", "skills", "monograph-pdf-publisher", "scripts")
if ENGINE_DIR not in sys.path:
    sys.path.insert(0, ENGINE_DIR)

import hust_pdf_engine as he


def build_pillar_equation_block(latex_eq: str, nom_data: list, styles: dict = None) -> KeepTogether:
    """
    Xây dựng khối phương trình cột trụ Cấp 3 kèm Bảng danh pháp ISO 80000-2 nguyên tử:
    - latex_eq: Chuỗi công thức LaTeX
    - nom_data: Danh sách các dict {'name': ..., 'symbol': ..., 'unit': ..., 'meaning': ...} hoặc tuple
    - styles: Bộ ReportLab ParagraphStyles chuẩn HUST
    """
    if styles is None:
        styles = he.get_hust_styles()

    img_path = he.render_latex_to_image(latex_eq, fontsize=14.0, dpi=300, bg_color="#F0F7FF", linespacing=2.2)
    eq_img = he._create_scaled_eq_image(img_path, max_width=he.PRINTABLE_WIDTH - 36.0)

    eq_box = Table([[eq_img]], colWidths=[he.PRINTABLE_WIDTH])
    eq_box.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), he.COLOR_BG_LEVEL3),
            ("LINEBEFORE", (0, 0), (0, -1), 2.0, he.COLOR_PRIMARY),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ("LEFTPADDING", (0, 0), (-1, -1), 16),
            ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ])
    )

    headers = [
        Paragraph(he.wrap_math_glyphs("Tên đại lượng"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("Ký hiệu ISO 80000-2"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("Đơn vị SI"), styles["TableHeader"]),
        Paragraph(he.wrap_math_glyphs("Ý nghĩa vật lý vi mô &amp; Hình học không gian"), styles["TableHeader"]),
    ]
    table_data = [headers]

    for row in nom_data:
        if isinstance(row, dict):
            name_val = row.get("name", "")
            sym_val = row.get("symbol", "")
            unit_val = row.get("unit", "")
            meaning_val = row.get("meaning", "")
        else:
            name_val, sym_val, unit_val, meaning_val = row

        table_data.append([
            Paragraph(he.wrap_math_glyphs(str(name_val)), styles["TableCell"]),
            Paragraph(he.wrap_math_glyphs(str(sym_val)), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(str(unit_val)), styles["TableCellCenter"]),
            Paragraph(he.wrap_math_glyphs(str(meaning_val)), styles["TableCell"]),
        ])

    col_widths = [115.0, 80.0, 65.0, he.PRINTABLE_WIDTH - 260.0]
    nom_table = Table(table_data, colWidths=col_widths, repeatRows=0, splitByRow=0)
    nom_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), he.COLOR_TABLE_HEADER_BG),
            ("GRID", (0, 0), (-1, -1), 0.5, he.COLOR_BORDER_GRAY),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ])
    )

    # Khóa cứng toàn bộ khối vào KeepTogether để không bao giờ bị cắt đôi qua 2 trang
    return KeepTogether([Spacer(1, 6), eq_box, Spacer(1, 6), nom_table, Spacer(1, 10)])

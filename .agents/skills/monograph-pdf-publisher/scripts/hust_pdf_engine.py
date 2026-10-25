# -*- coding: utf-8 -*-

"""

HUST Monograph PDF Typesetting & Pre-flight Linter Engine

Skill: user:monograph-pdf-publisher

Architecture: 5-Block Visual-First Core & Causal Flowchain (HUST Standard)

"""



import hashlib

import html

import os

import re
import sys
import tempfile
from typing import Any, Optional, Dict, List, Union

from concurrent.futures import ThreadPoolExecutor

from xml.sax.saxutils import escape



import matplotlib

matplotlib.use("Agg")

import matplotlib.font_manager as fm

import matplotlib.pyplot as plt

from PIL import Image as PILImage



from reportlab.lib import colors

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

from reportlab.lib.pagesizes import A4

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

from reportlab.pdfgen import canvas

from reportlab.platypus import (

    BaseDocTemplate,

    Frame,

    Image,

    KeepTogether,

    PageBreak,

    PageTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle,

)



# ---------------------------------------------------------------------------

# 1. CONSTANTS & STANDARDIZED LABELS (0-Token Boilerplate)

# ---------------------------------------------------------------------------

PAGE_WIDTH, PAGE_HEIGHT = A4

MARGIN_LR = 40.0

MARGIN_TB = 46.0

PRINTABLE_WIDTH = PAGE_WIDTH - 2.0 * MARGIN_LR  # 515.2756 pt

PRINTABLE_HEIGHT = PAGE_HEIGHT - 2.0 * MARGIN_TB



COLOR_PRIMARY = colors.HexColor("#0072BD")

COLOR_BODY = colors.HexColor("#212529")

COLOR_CAPTION = colors.HexColor("#495057")

COLOR_BG_LEVEL3 = colors.HexColor("#F0F7FF")

COLOR_BG_LEVEL2 = colors.HexColor("#F8F9FA")

COLOR_BORDER_GRAY = colors.HexColor("#CED4DA")

COLOR_TABLE_HEADER_BG = colors.HexColor("#E8F2FC")



MATH_GLYPHS = ("≫", "≪", "⇒", "→", "↳", "•", "≠", "≈", "≤", "≥", "∮", "∯", "∰", "ℓ", "≅", "⟪", "⟫")

_MATH_GLYPH_PATTERN = re.compile(

    r"(?<!<font face=\"DejaVuSans\">)(?<!<font face='DejaVuSans'>)(["

    + "".join(re.escape(g) for g in MATH_GLYPHS)

    + r"])(?!</font>)"

)



OCR_LINK_LABELS = {

    1: "↳ [Bản chất & Mục tiêu hình vẽ]:",

    2: "↳ [Giải mã Không gian & Hệ ký hiệu gốc]:",

    3: "↳ [Cơ chế Vật lý & Hành vi Tia/Hạt trên hình]:",

    4: "↳ [Quan hệ Hình học & Biến đổi Trung gian Chuẩn gốc]:",

    5: "↳ [Hệ thức Đích & Quy ước Dấu Đại số]:",

}



SLIDE_STEP_PREFIX = "↳ [Tường minh bước biến đổi trung gian từ slide gốc]:"



BLOCK_H3_TITLES = {
    1: "Khối 1: Khởi nguyên & Nỗi đau Công nghệ (Origin & Technological Bottleneck)",
    2: "Khối 2: Mỏ neo Thị giác & Mô hình hóa (Visual Anchor & Modeling)",
    3: "Khối 3: Góc Nhìn Đối Trọng & Thử Thách Chẩn Đoán CER (Orthogonal Perspective & Open CER Challenge)",
}

BLOCK_5_H2_TITLE = "Khối 3: Thử thách Chẩn đoán CER & Võ đài Phản biện Chat" 



def get_eq_cache_dir(namespace: str = None) -> str:
    """Trả về thư mục cache công thức toán độc lập cho từng tiến trình.
    
    Khi chạy song song qua /scan (Pha 2), mỗi Worker sở hữu một không gian độc lập
    qua tham số namespace, biến môi trường HUST_WORKER_NAMESPACE hoặc tự động suy luận
    từ tên script thực thi (__main__.__file__):
        %TEMP%/worker_{namespace}/hust_eq_cache/
    Triệt tiêu 100% xung đột đa tiến trình WinError 32 (Race Conditions).
    """
    ns = namespace or os.environ.get("HUST_WORKER_NAMESPACE", "").strip()
    if not ns:
        main_mod = sys.modules.get('__main__')
        main_file = getattr(main_mod, '__file__', '') if main_mod else ''
        if main_file:
            base = os.path.basename(main_file)
            m = re.search(r'(\d+[\._]\d+)', base)
            if m:
                ns = m.group(1).replace('_', '.')
    if ns:
        target_dir = os.path.join(tempfile.gettempdir(), f"worker_{ns}", "hust_eq_cache")
    else:
        target_dir = os.path.join(tempfile.gettempdir(), "hust_eq_cache")
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

EQ_CACHE_DIR = get_eq_cache_dir()





# ---------------------------------------------------------------------------

# 2. FONT REGISTRATION & STYLES (DejaVu Typography)

# ---------------------------------------------------------------------------

def register_dejavu_fonts(font_dir=None):

    """Register DejaVuSerif and DejaVuSans font families for ReportLab cross-platform."""

    font_paths = {

        "DejaVuSerif": fm.findfont("DejaVu Serif"),

        "DejaVuSerif-Bold": fm.findfont("DejaVu Serif:bold"),

        "DejaVuSerif-Italic": fm.findfont("DejaVu Serif:italic"),

        "DejaVuSerif-BoldItalic": fm.findfont("DejaVu Serif:bold:italic"),

        "DejaVuSans": fm.findfont("DejaVu Sans"),

        "DejaVuSans-Bold": fm.findfont("DejaVu Sans:bold"),

        "DejaVuSans-Oblique": fm.findfont("DejaVu Sans:italic"),

        "DejaVuSans-BoldOblique": fm.findfont("DejaVu Sans:bold:italic"),

    }

    

    # Nếu chỉ định font_dir tùy chọn

    if font_dir and os.path.exists(font_dir):

        file_map = {

            "DejaVuSerif": "DejaVuSerif.ttf",

            "DejaVuSerif-Bold": "DejaVuSerif-Bold.ttf",

            "DejaVuSerif-Italic": "DejaVuSerif-Italic.ttf",

            "DejaVuSerif-BoldItalic": "DejaVuSerif-BoldItalic.ttf",

            "DejaVuSans": "DejaVuSans.ttf",

            "DejaVuSans-Bold": "DejaVuSans-Bold.ttf",

            "DejaVuSans-Oblique": "DejaVuSans-Oblique.ttf",

            "DejaVuSans-BoldOblique": "DejaVuSans-BoldOblique.ttf",

        }

        for name, filename in file_map.items():

            candidate = os.path.join(font_dir, filename)

            if os.path.exists(candidate):

                font_paths[name] = candidate



    for name, path in font_paths.items():

        if path and os.path.exists(path):

            try:

                pdfmetrics.getFont(name)

            except KeyError:

                try:

                    pdfmetrics.registerFont(TTFont(name, path))

                except Exception as e:

                    pass



    pdfmetrics.registerFontFamily(

        "DejaVuSerif",

        normal="DejaVuSerif",

        bold="DejaVuSerif-Bold",

        italic="DejaVuSerif-Italic",

        boldItalic="DejaVuSerif-BoldItalic" if "DejaVuSerif-BoldItalic" in pdfmetrics._fonts else "DejaVuSerif-Bold",

    )

    pdfmetrics.registerFontFamily(

        "DejaVuSans",

        normal="DejaVuSans",

        bold="DejaVuSans-Bold",

        italic="DejaVuSans-Oblique" if "DejaVuSans-Oblique" in pdfmetrics._fonts else "DejaVuSans",

        boldItalic="DejaVuSans-BoldOblique" if "DejaVuSans-BoldOblique" in pdfmetrics._fonts else "DejaVuSans-Bold",

    )





def get_hust_styles():

    """Return pre-configured HUST ReportLab ParagraphStyles."""

    register_dejavu_fonts()

    base = getSampleStyleSheet()

    styles = {}



    styles["H1"] = ParagraphStyle(

        "H1HUST",

        parent=base["Normal"],

        fontName="DejaVuSans-Bold",

        fontSize=16.0,

        leading=22.0,

        textColor=COLOR_PRIMARY,

        spaceBefore=10.0,

        spaceAfter=8.0,

        keepWithNext=True,

    )

    styles["H2"] = ParagraphStyle(

        "H2HUST",

        parent=base["Normal"],

        fontName="DejaVuSans-Bold",

        fontSize=14.0,

        leading=19.0,

        textColor=COLOR_PRIMARY,

        spaceBefore=10.0,

        spaceAfter=6.0,

        keepWithNext=True,

    )

    styles["H3"] = ParagraphStyle(

        "H3HUST",

        parent=base["Normal"],

        fontName="DejaVuSans-Bold",

        fontSize=12.0,

        leading=16.0,

        textColor=COLOR_PRIMARY,

        spaceBefore=8.0,

        spaceAfter=4.0,

        keepWithNext=True,

    )

    styles["Body"] = ParagraphStyle(

        "BodyHUST",

        parent=base["Normal"],

        fontName="DejaVuSerif",

        fontSize=13.0,

        leading=18.0,

        textColor=COLOR_BODY,

        alignment=TA_JUSTIFY,

        spaceBefore=2.0,

        spaceAfter=5.0,

    )

    styles["Caption"] = ParagraphStyle(

        "CaptionHUST",

        parent=base["Normal"],

        fontName="DejaVuSerif-Italic",

        fontSize=10.5,

        leading=14.0,

        textColor=COLOR_CAPTION,

        alignment=TA_CENTER,

        spaceBefore=3.0,

        spaceAfter=8.0,

    )

    styles["TableHeader"] = ParagraphStyle(

        "TableHeaderHUST",

        parent=base["Normal"],

        fontName="DejaVuSans-Bold",

        fontSize=11.5,

        leading=15.0,

        textColor=COLOR_PRIMARY,

        alignment=TA_CENTER,

    )

    styles["TableCell"] = ParagraphStyle(

        "TableCellHUST",

        parent=base["Normal"],

        fontName="DejaVuSerif",

        fontSize=11.5,

        leading=15.5,

        textColor=COLOR_BODY,

        alignment=TA_LEFT,

    )

    styles["TableCellCenter"] = ParagraphStyle(

        "TableCellCenterHUST",

        parent= styles["TableCell"],

        alignment=TA_CENTER,

    )

    return styles





# ---------------------------------------------------------------------------

# 3. AUTOMATIC MATH GLYPH WRAPPING & PARAGRAPH HELPERS

# ---------------------------------------------------------------------------

_BARE_AMP_PATTERN = re.compile(r"&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)")





def _unescape_html_named_entities(text: str) -> str:

    """

    Convert named HTML entities (like &ndash;, &beta;, &nu;, &tau;, &mu;, &Delta;, &times;, &middot;)

    into real Unicode characters supported by DejaVu fonts, while preserving XML core entities

    (&amp;, &lt;, &gt;, &quot;, &apos;) and numeric character entities (&#...;).

    """

    def repl(m):

        entity = m.group(0)

        name = m.group(1)

        if name.lower() in ("lt", "gt", "amp", "quot", "apos"):

            return entity

        if name.startswith("#"):

            return entity

        return html.unescape(entity)

    return re.sub(r"&([a-zA-Z0-9#]+);", repl, text)





def wrap_math_glyphs(text: str) -> str:

    """

    Automatically wrap special math/arrow glyphs missing from DejaVuSerif

    in <font face="DejaVuSans">...</font> without double-wrapping, unescape HTML entities,

    and escape bare '&'.

    """

    if not text:

        return ""

    text_unescaped = _unescape_html_named_entities(str(text))

    safe_xml = _BARE_AMP_PATTERN.sub("&amp;", text_unescaped)

    return _MATH_GLYPH_PATTERN.sub(r'<font face="DejaVuSans">\1</font>', safe_xml)





def make_paragraph(

    text: str,

    style: ParagraphStyle,

    ocr_idx: int = None,

    is_expanded_from_slide: bool = False,

) -> Paragraph:

    """Create a ReportLab Paragraph with automatic wrap_math_glyphs & optional prefix."""

    prefix = ""

    if ocr_idx in OCR_LINK_LABELS:

        lbl = OCR_LINK_LABELS[ocr_idx]

        prefix = f"<b>{lbl}</b> "

    elif is_expanded_from_slide:

        prefix = f"<b>{SLIDE_STEP_PREFIX}</b> "

    full_text = wrap_math_glyphs(prefix + text)

    return Paragraph(full_text, style)





# ---------------------------------------------------------------------------

# 4. LATEX MATHTEXT 300 DPI RENDERER WITH SHA-256 CACHE

# ---------------------------------------------------------------------------

def clear_equation_cache(namespace: str = None):

    """Clear cached equation images (used on /edit Clean-Slate Recompilation)."""

    cache_dir = get_eq_cache_dir(namespace)

    if os.path.exists(cache_dir):

        for fname in os.listdir(cache_dir):

            fpath = os.path.join(cache_dir, fname)

            if os.path.isfile(fpath):

                try:

                    os.remove(fpath)

                except Exception:

                    pass





def _normalize_mathtext_latex(latex_str: str) -> str:

    """Normalize display math delimiters, short relational macros, and multi-line environments for DejaVu Serif mathtext."""

    s = latex_str.strip()

    if s.startswith("$$") and s.endswith("$$") and len(s) > 4:

        s = s[2:-2].strip()

    elif s.startswith(r"\[") and s.endswith(r"\]"):

        s = s[2:-2].strip()

    elif s.startswith(r"\(") and s.endswith(r"\)"):

        s = s[2:-2].strip()

    elif s.startswith("$") and s.endswith("$") and len(s) > 2:

        s = s[1:-1].strip()



    s = re.sub(r"\\ge(?![a-zA-Z])", r"\\geq", s)

    s = re.sub(r"\\le(?![a-zA-Z])", r"\\leq", s)

    s = re.sub(r"\\ne(?![a-zA-Z])", r"\\neq", s)

    s = re.sub(r"\\lvert(?![a-zA-Z])", "|", s)

    s = re.sub(r"\\rvert(?![a-zA-Z])", "|", s)

    s = re.sub(r"\\lVert(?![a-zA-Z])", r"\\|", s)

    s = re.sub(r"\\rVert(?![a-zA-Z])", r"\\|", s)

    s = re.sub(r"\\boxed\s*\{([^{}]*)\}", r"\1", s)

    s = re.sub(r"\\(?:bm|boldsymbol)(?![a-zA-Z])", r"\\mathbf", s)

    s = re.sub(r"\\operatorname(?![a-zA-Z])", r"\\mathrm", s)

    s = re.sub(r"\\implies(?![a-zA-Z])", r"\\Longrightarrow", s)

    s = re.sub(r"\\iff(?![a-zA-Z])", r"\\Longleftrightarrow", s)

    s = re.sub(r"\\gets(?![a-zA-Z])", r"\\leftarrow", s)

    s = re.sub(r"\\(?:tfrac|cfrac)(?![a-zA-Z])", r"\\frac", s)

    s = re.sub(r"\\grad(?![a-zA-Z])", r"\\nabla", s)

    s = re.sub(r"\\curl(?![a-zA-Z])", r"\\nabla \\times", s)

    s = re.sub(r"\\angstrom(?![a-zA-Z])", "Å", s)

    s = re.sub(r"\\vphantom\s*\{[^{}]*\}", "", s)



    def _repl_aligned(m):

        body = m.group(1).strip()

        rows = [r.replace("&", " ").strip() for r in re.split(r"\\\\(?:\[[^\]]*\])?", body) if r.strip()]

        return "\n".join(f"${r}$" for r in rows)



    s2 = re.sub(

        r"\\begin\{(?:aligned|align\*?|split|gathered)\}(.*?)\\end\{(?:aligned|align\*?|split|gathered)\}",

        _repl_aligned,

        s,

        flags=re.DOTALL,

    )

    if s2 != s:

        return s2



    m_cases = re.search(r"^(.*?)\\begin\{cases\}(.*?)\\end\{cases\}(.*?)$", s, flags=re.DOTALL)

    if m_cases:

        pre, body, post = m_cases.group(1).strip(), m_cases.group(2).strip(), m_cases.group(3).strip()

        rows = [r.strip() for r in re.split(r"\\\\(?:\[[^\]]*\])?", body) if r.strip()]

        formatted_rows = []

        for idx, r in enumerate(rows):

            parts = [p.strip() for p in r.split("&")]

            row_str = r", \quad ".join(parts)

            prefix = f"{pre} \\{{ " if (idx == 0 and pre) else (r"\quad " if pre else "")

            suffix = f" {post}" if (idx == len(rows) - 1 and post) else ""

            formatted_rows.append(f"${prefix}{row_str}{suffix}$")

        return "\n".join(formatted_rows)



    def _repl_matrix(m):

        mtype, body = m.group(1), m.group(2).strip()

        lbr, rbr = {"pmatrix": ("(", ")"), "bmatrix": ("[", "]"), "vmatrix": ("|", "|")}.get(mtype, ("(", ")"))

        rows = [r.strip() for r in re.split(r"\\\\", body) if r.strip()]

        row_exprs = [f"\\left{lbr} " + r" \;\; ".join(c.strip() for c in r.split("&")) + f" \\right{rbr}" for r in rows]

        return r" \; ; \; ".join(row_exprs)



    s3 = re.sub(r"\\begin\{(pmatrix|bmatrix|vmatrix|matrix)\}(.*?)\\end\{\1\}", _repl_matrix, s, flags=re.DOTALL)

    return f"${s3}$"





def _render_latex_via_pdflatex(

    raw_math: str,

    target_path: str,

    dpi: int = 300,

    bg_color: str = "#F8F9FA",

) -> str:

    """Fallback 300 DPI renderer via pdflatex + pypdfium2."""

    import subprocess

    import tempfile

    import numpy as _np

    import pypdfium2 as pdfium



    bg_hex = bg_color.lstrip("#")

    tex_doc = "\n".join([

        r"\documentclass[12pt]{article}",

        r"\usepackage{amsmath,amssymb,bm}",

        r"\usepackage[utf8]{inputenc}",

        r"\usepackage{xcolor}",

        f"\\definecolor{{bgcol}}{{HTML}}{{{bg_hex}}}",

        r"\definecolor{fgcol}{HTML}{212529}",

        r"\pagestyle{empty}",

        r"\begin{document}",

        r"\pagecolor{bgcol}\color{fgcol}",

        f"\\[ {raw_math} \\]",

        r"\end{document}",

    ])

    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:

        tex_path = os.path.join(tmpdir, "eq.tex")

        pdf_path = os.path.join(tmpdir, "eq.pdf")

        with open(tex_path, "w", encoding="utf-8") as f:

            f.write(tex_doc)

        subprocess.run(

            ["pdflatex", "-interaction=nonstopmode", "-output-directory", tmpdir, tex_path],

            stdout=subprocess.DEVNULL,

            stderr=subprocess.DEVNULL,

            check=True,

        )

        pdf = pdfium.PdfDocument(pdf_path)

        pil_im = pdf[0].render(scale=dpi / 72.0).to_pil().convert("RGB")

        arr = _np.asarray(pil_im)

        bg_rgb = tuple(int(bg_hex[i : i + 2], 16) for i in (0, 2, 4))

        diff = _np.any(_np.abs(arr.astype(int) - bg_rgb) > 6, axis=2)

        if _np.any(diff):

            ys, xs = _np.where(diff)

            pad = 18

            x0 = max(0, int(xs.min()) - pad)

            y0 = max(0, int(ys.min()) - pad)

            x1 = min(arr.shape[1], int(xs.max()) + 1 + pad)

            y1 = min(arr.shape[0], int(ys.max()) + 1 + pad)

            pil_im = pil_im.crop((x0, y0, x1, y1))

        pil_im.save(target_path, format="PNG", dpi=(dpi, dpi))

    return target_path





def render_latex_to_image(

    latex_str: str,

    out_path: str = None,

    fontsize: float = 13.5,

    dpi: int = 300,

    bg_color: str = "#F8F9FA",

    text_color: str = "#212529",

    linespacing: float = 2.2,

) -> str:

    """

    Render a LaTeX math expression to a crisp >= 300 DPI PNG image.

    Uses SHA-256 content hashing in /tmp/hust_eq_cache/ to avoid redundant renders,

    with automatic pdflatex fallback for multi-line environments (cases, pmatrix, aligned).

    """

    cache_dir = get_eq_cache_dir()

    clean_eq = _normalize_mathtext_latex(latex_str)



    key = f"{clean_eq}|{fontsize}|{dpi}|{bg_color}|{text_color}|{linespacing}"

    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:20]

    cached_path = out_path or os.path.join(cache_dir, f"eq_{digest}.png")



    if out_path is None and os.path.exists(cached_path) and os.path.getsize(cached_path) > 0:

        return cached_path



    fig = plt.figure(figsize=(0.1, 0.1), dpi=dpi)

    try:

        fig.patch.set_facecolor(bg_color)

        fig.patch.set_alpha(1.0)

        fig.text(

            0.0,

            0.0,

            clean_eq,

            fontsize=fontsize,

            color=text_color,

            va="center",

            ha="center",

            math_fontfamily="dejavuserif",

            linespacing=linespacing,

        )

        fig.savefig(

            cached_path,

            dpi=dpi,

            bbox_inches="tight",

            pad_inches=0.08,

            facecolor=bg_color,

            transparent=False,

        )

    except Exception:

        plt.close(fig)

        return _render_latex_via_pdflatex(latex_str.strip().strip('$'), cached_path, dpi=dpi, bg_color=bg_color)

    plt.close(fig)

    return cached_path





def batch_render_equations(eq_specs: list) -> list:

    """Render multiple equation specs concurrently."""

    with ThreadPoolExecutor(max_workers=4) as pool:

        return list(pool.map(lambda spec: render_latex_to_image(**spec), eq_specs))





def _create_scaled_eq_image(img_path: str, max_width: float = 470.0) -> Image:

    """Load a rendered 300 DPI equation PNG and convert pixels to points without distortion."""

    with PILImage.open(img_path) as im:

        px_w, px_h = im.size

    pt_w = px_w * 72.0 / 300.0

    pt_h = px_h * 72.0 / 300.0

    if pt_w > max_width:

        scale = max_width / pt_w

        pt_w *= scale

        pt_h *= scale

    img_flowable = Image(img_path, width=pt_w, height=pt_h)

    img_flowable.hAlign = "CENTER"

    return img_flowable





def build_intermediate_equation(

    explanation_text: str,

    latex_eq: str,

    styles: dict = None,

    is_expanded_from_slide: bool = False,

    ocr_idx: int = None,

) -> KeepTogether:

    """

    Build a Level-2 Causal Flowchain step (Khối 3):

    - Explanation Paragraph (automatically wrapped with math glyphs & optional slide/OCR prefix)

    - 300 DPI equation image centered on subtle #F8F9FA background

    - Wrapped in an individual-step KeepTogether to prevent >25% page whitespace.

    """

    if styles is None:

        styles = get_hust_styles()



    para = make_paragraph(

        explanation_text,

        styles["Body"],

        ocr_idx=ocr_idx,

        is_expanded_from_slide=is_expanded_from_slide,

    )

    img_path = render_latex_to_image(latex_eq, fontsize=13.0, dpi=300, bg_color="#F8F9FA")

    eq_img = _create_scaled_eq_image(img_path, max_width=PRINTABLE_WIDTH - 24.0)



    eq_table = Table([[eq_img]], colWidths=[PRINTABLE_WIDTH])

    eq_table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, -1), COLOR_BG_LEVEL2),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

                ("TOPPADDING", (0, 0), (-1, -1), 8),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

                ("LEFTPADDING", (0, 0), (-1, -1), 12),

                ("RIGHTPADDING", (0, 0), (-1, -1), 12),

            ]

        )

    )

    return KeepTogether([para, Spacer(1, 6), eq_table, Spacer(1, 10)])





def build_target_equation_block(

    latex_eq: str,

    nomenclature_rows: list,

    styles: dict = None,

) -> KeepTogether:

    """

    Build a Level-3 Pillar Equation Block (Khối 2 - Unique per MPT):

    - 300 DPI equation image on #F0F7FF background with 2 pt #0072BD vertical bar

      (top/bottom padding 10 pt, left/right padding 16 pt)

    - 4-column ISO 80000-2 Nomenclature table (Tên đại lượng | Ký hiệu ISO 80000-2 | Đơn vị SI | Ý nghĩa vật lý vi mô & Hình học không gian)

    - Bound together inside KeepTogether.

    """

    if styles is None:

        styles = get_hust_styles()



    img_path = render_latex_to_image(latex_eq, fontsize=14.0, dpi=300, bg_color="#F0F7FF", linespacing=2.2)

    eq_img = _create_scaled_eq_image(img_path, max_width=PRINTABLE_WIDTH - 36.0)



    eq_box = Table([[eq_img]], colWidths=[PRINTABLE_WIDTH])

    eq_box.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, -1), COLOR_BG_LEVEL3),

                ("LINEBEFORE", (0, 0), (0, -1), 2.0, COLOR_PRIMARY),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

                ("TOPPADDING", (0, 0), (-1, -1), 10),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

                ("LEFTPADDING", (0, 0), (-1, -1), 16),

                ("RIGHTPADDING", (0, 0), (-1, -1), 16),

            ]

        )

    )



    headers = [

        Paragraph(wrap_math_glyphs("Tên đại lượng"), styles["TableHeader"]),

        Paragraph(wrap_math_glyphs("Ký hiệu ISO 80000-2"), styles["TableHeader"]),

        Paragraph(wrap_math_glyphs("Đơn vị SI"), styles["TableHeader"]),

        Paragraph(

            wrap_math_glyphs("Ý nghĩa vật lý vi mô & Hình học không gian"),

            styles["TableHeader"],

        ),

    ]

    table_data = [headers]

    for row in nomenclature_rows:

        if isinstance(row, dict):
            name_col = row.get("name", "")
            sym_col = row.get("symbol", "")
            unit_col = row.get("unit", "")
            meaning_col = row.get("meaning", "")
        else:
            name_col, sym_col, unit_col, meaning_col = row

        table_data.append(

            [

                Paragraph(wrap_math_glyphs(str(name_col)), styles["TableCell"]),

                Paragraph(wrap_math_glyphs(str(sym_col)), styles["TableCellCenter"]),

                Paragraph(wrap_math_glyphs(str(unit_col)), styles["TableCellCenter"]),

                Paragraph(wrap_math_glyphs(str(meaning_col)), styles["TableCell"]),

            ]

        )



    col_widths = [115.0, 80.0, 65.0, PRINTABLE_WIDTH - 260.0]

    nom_table = Table(table_data, colWidths=col_widths, repeatRows=0, splitByRow=0)

    nom_table.setStyle(

        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), COLOR_TABLE_HEADER_BG),

                ("GRID", (0, 0), (-1, -1), 0.5, COLOR_BORDER_GRAY),

                ("VALIGN", (0, 0), (-1, -1), "TOP"),

                ("TOPPADDING", (0, 0), (-1, -1), 5),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),

                ("LEFTPADDING", (0, 0), (-1, -1), 6),

                ("RIGHTPADDING", (0, 0), (-1, -1), 6),

            ]

        )

    )

    return KeepTogether([Spacer(1, 6), eq_box, Spacer(1, 6), nom_table, Spacer(1, 10)])





build_level3_target_equation = build_target_equation_block

render_latex_block = build_intermediate_equation


def make_open_cer_box(
    challenge_data: Any,
    styles: dict = None,
    mpt_id: str = "",
) -> KeepTogether:
    """
    Tạo khối Flowable khung viền bo cho Thử thách Chẩn đoán R&D Mở (Open CER Challenge) ở Khối 3.

    RÀNG BUỘC BẤT BIẾN:
    - Hiển thị: Bối cảnh & Đề bài chẩn đoán, Định hướng Khẳng định (Claim Guide),
      Dữ kiện Thực nghiệm cần trích xuất (Evidence Guide), Tiêu chí Lập luận (Reasoning Guide),
      Cảnh báo bẫy ngộ nhận (Misconception Trap).
    - CẤM TUYỆT ĐỐI IN LỜI GIẢI / ĐÁP ÁN TRONG PDF.
    - Đề bài để mở tự do, có dòng nhắc Lead Researcher độc lập phản biện trên Chat.
    """
    if styles is None:
        styles = get_hust_styles()

    if isinstance(challenge_data, dict):
        diag_q = challenge_data.get("diagnostic_question") or challenge_data.get("challenge_prompt", "")
        context = challenge_data.get("challenge_context", "")
        claim = challenge_data.get("claim_guidance", "")
        evidence = challenge_data.get("evidence_required", "")
        reasoning = challenge_data.get("reasoning_rubric", "")
        misconception = challenge_data.get("misconception_trap") or challenge_data.get("misconception_warning", "")
    else:
        diag_q = getattr(challenge_data, "diagnostic_question", getattr(challenge_data, "challenge_prompt", ""))
        context = getattr(challenge_data, "challenge_context", "")
        claim = getattr(challenge_data, "claim_guidance", "")
        evidence = getattr(challenge_data, "evidence_required", "")
        reasoning = getattr(challenge_data, "reasoning_rubric", "")
        misconception = getattr(challenge_data, "misconception_trap", getattr(challenge_data, "misconception_warning", ""))

    content_cells = []

    # 1. Tiêu đề hộp
    title_suffix = f" — MPT {mpt_id}" if mpt_id else ""
    title_text = f"<b>THỬ THÁCH CHẨN ĐOÁN R&amp;D THỰC CHIẾN (OPEN CER CHALLENGE){title_suffix}</b>"
    content_cells.append(make_paragraph(title_text, styles.get("H3", styles["Body"])))

    # 2. Bối cảnh & Đề bài
    prompt_full = diag_q or context
    if prompt_full:
        content_cells.append(Spacer(1, 4))
        content_cells.append(make_paragraph(f"<b>Bối cảnh &amp; Đề bài Chẩn đoán:</b> <i>{prompt_full}</i>", styles["Body"]))

    # 3. Tiêu chí định hướng Claim - Evidence - Reasoning (KHÔNG IN LỜI GIẢI)
    cer_items = []
    if claim:
        cer_items.append(f"• <b>Định hướng Khẳng định (Claim Guide):</b> {claim}")
    if evidence:
        cer_items.append(f"• <b>Dữ kiện Cần Trích xuất (Evidence Guide):</b> {evidence}")
    if reasoning:
        cer_items.append(f"• <b>Tiêu chí Lập luận (Reasoning Guide):</b> {reasoning}")

    if cer_items:
        content_cells.append(Spacer(1, 4))
        content_cells.append(make_paragraph("<br/>".join(cer_items), styles["Body"]))

    # 4. Bẫy ngộ nhận kinh điển
    if misconception:
        content_cells.append(Spacer(1, 4))
        content_cells.append(make_paragraph(f"⚠️ <b>Bẫy ngộ nhận cần tránh:</b> {misconception}", styles["Body"]))

    # 5. Dòng lưu ý bản quyền tư duy
    note_text = (
        "<i>🔒 <b>Chốt chặn bảo mật tư duy:</b> Đề bài để mở tự do, cấm in lời giải trong tài liệu này. "
        "Lead Researcher hãy phân tích độc lập và trực tiếp tranh biện trên Chat Antigravity để AI chấm điểm phản biện.</i>"
    )
    content_cells.append(Spacer(1, 6))
    content_cells.append(make_paragraph(note_text, styles.get("Caption", styles["Body"])))

    # Đóng gói vào Table viền bo
    table_data = [[content_cells]]
    box_table = Table(table_data, colWidths=[PRINTABLE_WIDTH])
    box_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8F9FA")),
        ('BOX', (0, 0), (-1, -1), 1.0, colors.HexColor("#0072BD")),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return KeepTogether([Spacer(1, 6), box_table, Spacer(1, 10)])





# ---------------------------------------------------------------------------

# 5. GEOMETRY-SAFE FIGURE EMBEDDING (Anti-Shrink Guard)

# ---------------------------------------------------------------------------

def embed_figure_with_caption(

    img_path: str,

    caption_text: str,

    kind: str = "sim",

    styles: dict = None,

) -> KeepTogether:

    """

    Embed a simulation plot ('sim' -> [Mo_Phong]) or auto-cropped textbook figure ('orig' -> [Goc])

    with strict A4 geometry limits:

    - Simulation plot ('sim'): width 460-500 pt (default 480 pt), max height 340 pt.

    - Original slide figure ('orig'): landscape width 430-485 pt (max height 320 pt),

      square/portrait width 360-420 pt (max height 340 pt).

    - Strictly prohibits shrinking height <= 180 pt or width < 360 pt.

    """

    if styles is None:

        styles = get_hust_styles()

    if not os.path.exists(img_path):

        raise FileNotFoundError(f"Figure not found: {img_path}")



    with PILImage.open(img_path) as im:

        px_w, px_h = im.size

    aspect = px_h / float(px_w)



    if kind == "sim" or os.path.basename(img_path).startswith("[Mo_Phong]"):

        target_w = 480.0

        max_h = 340.0

        min_w = 460.0

    else:

        if aspect <= 0.82:  # landscape / wide schematic

            target_w = 465.0

            max_h = 320.0

            min_w = 430.0

        else:  # square / portrait

            target_w = 390.0

            max_h = 340.0

            min_w = 360.0



    target_h = target_w * aspect

    if target_h > max_h:

        target_h = max_h

        target_w = target_h / aspect



    if target_h <= 180.0 and target_w < 430.0:

        scale_up = min(485.0 / max(target_w, 1.0), 185.0 / max(target_h, 1.0))

        target_w *= scale_up

        target_h *= scale_up



    if target_h <= 180.0 and target_w < 360.0:

        raise ValueError(

            f"Anti-Shrink Guard Triggered: Embedded size {target_w:.1f}x{target_h:.1f} pt is too small for {img_path}."

        )



    img_flowable = Image(img_path, width=target_w, height=target_h)

    img_flowable.hAlign = "CENTER"

    cap_para = make_paragraph(caption_text, styles["Caption"])

    flowables = [Spacer(1, 4), img_flowable, Spacer(1, 4)]

    # Thuật toán 13 ZT-GVLE: Kiểm tra Zero-Trust Manifest & Nhúng Thẻ Tham số Bóc tách
    if os.path.basename(img_path).startswith("[Mo_Phong]"):
        import json
        manifest_path = img_path.rsplit(".", 1)[0] + ".manifest.json"
        if not os.path.exists(manifest_path):
            raise AssertionError(f"ZT-GVLE Missing Cryptographic Manifest for {img_path}: Expected {manifest_path}")
        with open(manifest_path, "r", encoding="utf-8") as mf:
            manifest_data = json.load(mf)
        with open(img_path, "rb") as im_f:
            actual_hash = hashlib.sha256(im_f.read()).hexdigest()
        if actual_hash != manifest_data.get("sha256"):
            raise AssertionError(f"ZT-GVLE Cryptographic Hash Mismatch for {img_path}: Actual {actual_hash} != Manifest {manifest_data.get('sha256')}")
        if manifest_data.get("geometry_audit", {}).get("status") != "PASS":
            raise AssertionError(f"ZT-GVLE Geometry Audit Fail for {img_path}: {manifest_data.get('geometry_audit')}")
            
            param_card = manifest_data.get("parameter_card")
            if param_card and any(param_card.values()):
                mat_sys = param_card.get("material_system")
                swp_par = param_card.get("sweep_parameters")
                lab_met = param_card.get("lab_metrics")
                if mat_sys and swp_par and lab_met and "N/A" not in (str(mat_sys), str(swp_par), str(lab_met)):
                    badge_text = (
                        f"<i>↳ [Hệ vật liệu]: {mat_sys} | "
                        f"[Thông số quét]: {swp_par} | "
                        f"[Hệ quả Lab]: {lab_met}</i>"
                    )
                    param_para = make_paragraph(badge_text, styles["BodyText"])
                    flowables.extend([param_para, Spacer(1, 4)])

    flowables.extend([cap_para, Spacer(1, 10)])

    return KeepTogether(flowables)





# ---------------------------------------------------------------------------

# 6. MULTI-LEVEL PDF BOOKMARKS & PAGE X / Y CANVAS

# ---------------------------------------------------------------------------

class NumberedBookmarkCanvas(canvas.Canvas):

    """Two-pass ReportLab Canvas rendering 'Trang X / Y' footer and preserving exact page bookmarks."""



    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self._saved_page_states = []

        self._page_bookmarks = []



    def record_page_bookmark(self, title: str, key: str, level: int):

        self._page_bookmarks.append((title, key, level))



    def showPage(self):

        self._saved_page_states.append(dict(self.__dict__))

        self._startPage()

        self._page_bookmarks = []



    def save(self):

        num_pages = len(self._saved_page_states)

        max_level = -1

        for page_idx, state in enumerate(self._saved_page_states, start=1):

            self.__dict__.update(state)

            self._pageNumber = page_idx

            for title, key, level in getattr(self, "_page_bookmarks", []):

                safe_level = min(level, max_level + 1)

                max_level = max(max_level, safe_level)

                self.bookmarkPage(key)

                self.addOutlineEntry(title, key, level=safe_level, closed=False)

            self._draw_page_number(num_pages)

            super().showPage()

        super().save()



    def _draw_page_number(self, page_count: int):

        self.saveState()

        self.setFont("DejaVuSerif", 9.5)

        self.setFillColor(COLOR_CAPTION)

        label = f"Trang {self._pageNumber} / {page_count}"

        self.drawRightString(PAGE_WIDTH - MARGIN_LR, 24.0, label)

        self.restoreState()





class BookmarkDocTemplate(BaseDocTemplate):

    """

    A4 Document Template (margins: L/R 40 pt, T/B 46 pt) that automatically

    captures H1, H2, and H3 Paragraphs into a 3-level PDF Bookmark tree.

    """



    def __init__(self, filename, **kwargs):

        self._target_filename = os.path.abspath(filename)

        self._temp_filename = os.path.join(

            tempfile.gettempdir(),

            f"hust_build_{os.getpid()}_{hashlib.md5(self._target_filename.encode('utf-8')).hexdigest()[:8]}.pdf",

        )

        kwargs.setdefault("pagesize", A4)

        kwargs.setdefault("leftMargin", MARGIN_LR)

        kwargs.setdefault("rightMargin", MARGIN_LR)

        kwargs.setdefault("topMargin", MARGIN_TB)

        kwargs.setdefault("bottomMargin", MARGIN_TB)

        super().__init__(self._temp_filename, **kwargs)



        frame = Frame(

            self.leftMargin,

            self.bottomMargin,

            self.width,

            self.height,

            id="normal_frame",

            leftPadding=0,

            rightPadding=0,

            topPadding=0,

            bottomPadding=0,

        )

        template = PageTemplate(id="MonographPage", frames=[frame])

        self.addPageTemplates([template])

        self._bookmark_counter = 0



    def afterFlowable(self, flowable):

        if isinstance(flowable, Paragraph):

            style_name = flowable.style.name

            level = None

            if style_name in ("H1HUST", "H1"):

                level = 0

            elif style_name in ("H2HUST", "H2"):

                level = 1

            elif style_name in ("H3HUST", "H3"):

                level = 2



            if level is not None:

                raw_text = re.sub(r"<[^>]+>", "", flowable.getPlainText()).strip()

                self._bookmark_counter += 1

                key = f"bm_{level}_{self._bookmark_counter}"

                if hasattr(self.canv, "record_page_bookmark"):

                    self.canv.record_page_bookmark(raw_text, key, level)

                else:

                    self.canv.bookmarkPage(key)

                    self.canv.addOutlineEntry(raw_text, key, level=level, closed=False)



    def build(self, flowables, canvasmaker=NumberedBookmarkCanvas):

        flowables_list = list(flowables)

        # BẮT BUỘC: Pre-flight Hard Assertion Gate quét cạn toàn văn trước khi build

        assert_monograph_text_compliance(flowables_list, require_5_blocks=True)



        target_dir = os.path.dirname(self._target_filename)

        if target_dir:

            os.makedirs(target_dir, exist_ok=True)

        if os.path.exists(self._target_filename):

            if not os.access(self._target_filename, os.W_OK):

                raise PermissionError(

                    f"Target file '{self._target_filename}' is locked or not writable. Check for active PDF viewers or Drive sync locks."

                )



        super().build(flowables_list, canvasmaker=canvasmaker)



        if not os.path.exists(self._temp_filename) or os.path.getsize(self._temp_filename) < 5120:

            raise RuntimeError(f"Monograph build failed or generated file is corrupt: {self._temp_filename}")



        size_mb = os.path.getsize(self._temp_filename) / (1024.0 * 1024.0)

        if size_mb > 5.0:

            raise ValueError(f"Monograph PDF size ({size_mb:.2f} MB) exceeds 5.0 MB limit.")



        try:

            os.replace(self._temp_filename, self._target_filename)

        except OSError:

            import shutil

            shutil.copy2(self._temp_filename, self._target_filename)

            try:

                os.remove(self._temp_filename)

            except OSError:

                pass

        self.filename = self._target_filename



        # BẮT BUỘC: Post-build Hard Assertion Gate kiểm tra tính toàn vẹn của tệp PDF xuất bản

        assert_monograph_compliance(self._target_filename)





# ---------------------------------------------------------------------------

# 7. PRE-FLIGHT LINTER (assert_monograph_compliance - 0 LLM Tokens)

# ---------------------------------------------------------------------------

_RAW_LATEX_RE = re.compile(

    r"\\(?:theta|alpha|beta|gamma|delta|Delta|omega|Omega|lambda|sigma|pi|mu|nu|tau|phi|Phi|psi|Psi|"

    r"eta|kappa|rho|chi|xi|zeta|Gamma|epsilon|varepsilon|sin|cos|tan|exp|ln|log|frac|dfrac|sqrt|nabla|"

    r"partial|infty|sum|int|prod|cdot|times|pm|mp|Rightarrow|Leftarrow|rightarrow|leftarrow|"

    r"leftrightarrow|approx|neq|leq|geq|ll|gg|mathrm|mathbf|mathcal|text|left|right|hat|vec|bar|"

    r"tilde|dot|ddot)\b"

)



_RAW_NAMED_ENTITY_RE = re.compile(

    r"&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)[a-zA-Z0-9]+;",

    re.IGNORECASE,

)



_RAW_UNDERSCORE_VAR_RE = re.compile(

    r"(?<![A-Za-z0-9_/\\])\b([A-Za-z]{1,3})_([A-Za-z0-9]+)\b(?![A-Za-z0-9_])"

)



_RAW_CARET_EXPONENT_RE = re.compile(

    r"(?<![A-Za-z0-9_.\[])\b([A-Za-z0-9]+)\^([-+]?[0-9]+)\b"

)



_SI_MISSING_SPACE_RE = re.compile(

    r"(?<![A-Za-z0-9_.\[])(\d+(?:[.,]\d+)?)(nm|um|μm|mm|cm|km|kg|mg|ms|us|μs|ns|ps|fs|Hz|kHz|MHz|GHz|THz|"

    r"eV|meV|keV|MeV|GeV|mA|uA|μA|kA|mV|kV|mW|kW|MW|GW|Pa|kPa|MPa|GPa|kΩ|MΩ|GΩ|mΩ|Ω|mT|μT|T|mH|μH|nH|H|"

    r"mC|μC|nC|pC|C|mF|μF|nF|pF|mol|cd|lm|lx|Wb|°C|oC|K|V|A|W|J|N|F|s|m)(?![A-Za-z0-9_])"

)

_ORBITAL_CONTEXT_RE = re.compile(

    r"(?:quỹ\s+đạo|trạng\s+thái|orbital|phân\s+lớp|lớp|lai\s+hóa|[1-7][spdf])",

    re.IGNORECASE,

)



_ALLOWED_SLASH_UNITS = re.compile(

    r"\b(?:\d+(?:[.,]\d+)?\s*)?(?:km/h|m/s|V/m|V/cm|A/m[²2]?|A/cm[²2]?|W/m[²2]?|W/cm[²2]?|J/K|C/m[²23]?|N/m|W/sr|cd/m²|s⁻¹·cm⁻³·eV⁻¹|cm[²2]/\(?V[·\.]?s\)?|cm[²2]/s)\b",

    re.IGNORECASE,

)

_ALLOWED_SLASH_WORDS = re.compile(

    r"\b(?:[tT]rực tiếp/[gG]ián tiếp|[tT]ương tác/[tT]án xạ|[vV]à/[hH]oặc|[hH]oặc/[vV]à|[tT]rên/[dD]ưới|"

    r"[eE]lectron/[lL]ỗ trống|[tT]huận/[nN]ghịch|[vV]ào/[rR]a|[pP]hát xạ/[hH]ấp thụ|[sS]óng/[hH]ạt|"

    r"[dD]ẫn/[hH]óa trị|[qQ]uang/[đĐ]iện|[A-Z][a-z0-9]+/[A-Z][a-z0-9]+)\b"

)

_SLASH_FRACTION_MATH_RE = re.compile(

    r"(?:"

    r"[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω]\s*/\s*[∂d]\s*[A-Za-z0-9_α-ωΑ-Ω]|"

    r"(?<=[=≈∝≤≥])\s*[^,;\n<>]{1,40}\s*/\s*[^,;\n<>]{1,40}|"

    r"/\s*(?:\([^\)]*(?:4\s*π|ε|r|k_?B)[^\)]*\)|r[²2]?|r\^2|ε_?0|ε₀|k_?[Bb]|c[²2]?|c\^2|4\s*π\s*ε)|"

    r"\b\d+\s*/\s*(?:r[²2]|r\^2|c[²2]|c\^2|k_?[Bb]T)\b|"

    r"\b\d+\s*/\s*\([^\)]+\)"

    r")"

)






_NESTED_SUP_SUB_RE = re.compile(
    r"<(sup|sub)[^>]*>(?:(?!</\1>).)*?<\1[^>]*>",
    re.IGNORECASE | re.DOTALL,
)

_RAW_CHEM_FORMULA_RE = re.compile(
    r"\b(?:g-C3N4|Ag3VO4|WO3|TiO2|BiVO4|Fe2O3|CH3OH|C2H5OH|H2O2|CO2|H2O|NO2|SO2)\b"
)

_RAW_BAND_VAR_RE = re.compile(
    r"\b(?:ECB|EVB|Eg)\b"
)


def _extract_flowable_texts(items) -> list:

    """Recursively extract clean text strings from strings, Paragraphs, KeepTogether, and Tables."""

    extracted = []

    if items is None:

        return extracted

    for item in items:

        if isinstance(item, str):

            extracted.append(item)

        elif isinstance(item, Paragraph):

            extracted.append(getattr(item, "text", str(item)))

        elif isinstance(item, KeepTogether):

            extracted.extend(_extract_flowable_texts(getattr(item, "_content", [])))

        elif isinstance(item, Table):

            for row in getattr(item, "_cellvalues", []):

                extracted.extend(_extract_flowable_texts(row))

        elif isinstance(item, (list, tuple)):

            extracted.extend(_extract_flowable_texts(item))

    return extracted





def assert_monograph_text_compliance(

    text_blocks: list,

    require_5_blocks: bool = True,

) -> dict:

    """

    Scan all text strings / Paragraphs for:

    1. Raw LaTeX backslash leaks (\theta, \frac, \nabla...)

    2. Missing whitespace before SI units (20nm, 300K, 37oC...)

    3. Unwrapped special math glyphs (⇒, ↳, →, ≈, ≤, ≥, ≫, ≪, ≠, •)

    4. Zero-Slash-Fractions in math formulas (cấm ρ / ε₀, 1/r², ∂ρ/∂t...)

    5. Presence of 5-Block headings (Khối 1 -> Khối 4 and Khối 5).

    Raises AssertionError with detailed diagnostics if any check fails.

    """

    errors = []

    clean_blocks = _extract_flowable_texts(text_blocks)

    combined_text = "\n".join(clean_blocks)



    has_flowable_para = any(not isinstance(x, str) for x in (text_blocks or []))

    for idx, s in enumerate(clean_blocks):

        m_latex = _RAW_LATEX_RE.search(s)

        if m_latex:

            errors.append(

                f"[Block {idx}] Rò rỉ lệnh LaTeX thô '{m_latex.group(0)}' trong văn bản: {s[:90]}..."

            )

        for m_si in _SI_MISSING_SPACE_RE.finditer(s):

            num_part, unit_part = m_si.group(1), m_si.group(2)

            if unit_part == "s" and num_part in ("1", "2", "3", "4", "5", "6", "7") and _ORBITAL_CONTEXT_RE.search(s):

                continue

            errors.append(

                f"[Block {idx}] Thiếu khoảng trắng chuẩn SI '{m_si.group(0)}' (phải viết '{num_part} {unit_part}'): {s[:90]}..."

            )

            break

        if has_flowable_para:

            m_glyph = _MATH_GLYPH_PATTERN.search(s)

            if m_glyph:

                errors.append(

                    f"[Block {idx}] Ký tự toán học '{m_glyph.group(1)}' chưa bọc wrap_math_glyphs (DejaVuSans): {s[:90]}..."

                )

        # Check 4: Zero-Slash-Fractions in math formulas

        s_clean = re.sub(r"<[^>]+>", "", s)

        s_clean = _ALLOWED_SLASH_UNITS.sub("", s_clean)

        s_clean = _ALLOWED_SLASH_WORDS.sub("", s_clean)

        s_clean = re.sub(r"https?://\S+", "", s_clean)

        m_slash = _SLASH_FRACTION_MATH_RE.search(s_clean)

        if m_slash:

            errors.append(

                f"[Block {idx}] Phát hiện phân số gạch chéo '{m_slash.group(0)}' trong công thức toán. "

                f"Bắt buộc dùng phân số gạch ngang \\frac{{a}}{{b}} qua LaTeX Mathtext: {s[:90]}..."

            )



        # Check 5: Raw ASCII underscore variables (E_c, N_th, I_th, V_j, v_g...)

        s_no_filename = re.sub(r"\[(?:Goc|Mo_Phong|OLD_[^\]]+)\]_[A-Za-z0-9_.-]+", "", s)

        s_no_filename = re.sub(r"\bFigure_[0-9_A-Za-z.-]+", "", s_no_filename)

        s_no_filename = re.sub(r"https?://\S+", "", s_no_filename)

        s_no_filename = re.sub(r"<[^>]+>", "", s_no_filename)

        m_var = _RAW_UNDERSCORE_VAR_RE.search(s_no_filename)

        if m_var:

            errors.append(

                f"[Block {idx}] Phát hiện biến số gạch dưới ASCII thô '{m_var.group(0)}' chưa được bọc HTML tags. "

                f"Bắt buộc format dạng '<i>{m_var.group(1)}</i><sub>{m_var.group(2)}</sub>': {s[:90]}..."

            )



        # Check 6: Raw caret exponent (BN^2, cm^-3, s^-1...)

        m_caret = _RAW_CARET_EXPONENT_RE.search(s_no_filename)

        if m_caret:

            errors.append(

                f"[Block {idx}] Phát hiện số mũ ASCII thô '{m_caret.group(0)}' chưa được bọc HTML tags. "

                f"Bắt buộc format dạng '<sup>{m_caret.group(2)}</sup>': {s[:90]}..."

            )



        # Check 7: Arrow glyph ↳ must be on a new line (preceded by <br/> or at block start)

        for m_arrow in re.finditer(r"↳", s):

            arrow_idx = m_arrow.start()

            prefix = s[:arrow_idx].rstrip()

            prefix_clean = re.sub(r"</?(?:b|i|font|span|strong|em)[^>]*>", "", prefix).rstrip()

            if prefix_clean:

                if not re.search(r"<br\s*/?>\s*(?:<[^>]+>\s*)*$", prefix, re.IGNORECASE):

                    snippet = s[max(0, arrow_idx - 30) : min(len(s), arrow_idx + 45)]

                    errors.append(

                        f"[Block {idx}] Phát hiện ký hiệu '↳' không được xuống dòng riêng biệt. "

                        f"Bắt buộc chèn thẻ '<br/>' trước '↳' để tách dòng độc lập theo quy chuẩn Micro-Block: ...{snippet}..."

                    )



        # Check 8: Zero-Raw-HTML-Entities Gate (Cấm tuyệt đối rò rỉ thực thể HTML thô)

        m_entity = _RAW_NAMED_ENTITY_RE.search(s)

        if m_entity:

            errors.append(

                f"[Block {idx}] Phát hiện thực thể HTML đặt tên thô '{m_entity.group(0)}' chưa được giải mã sang ký tự Unicode chuẩn (DejaVu Serif). "

                f"Bắt buộc dùng trực tiếp ký tự Unicode hoặc bọc qua wrap_math_glyphs: {s[:90]}..."

            )

        # Check 9: Zero-Placeholder-Tables Gate (Cấm rò rỉ keys dict ['name', 'symbol', 'unit', 'meaning'])
        if re.search(r"\bname\b.*\bsymbol\b.*\bunit\b.*\bmeaning\b", s, re.IGNORECASE) or (
            s.strip().lower() in ("name", "symbol", "unit", "meaning") and has_flowable_para
        ):
            errors.append(
                f"[Block {idx}] Phát hiện chuỗi placeholder keys 'name|symbol|unit|meaning' trong bảng danh pháp: {s[:90]}..."
            )

        # Check 10: Zero-NA-Badge Gate (Cấm rò rỉ thẻ tham số N/A)
        if "↳ [Hệ vật liệu]: N/A" in s or "[Thông số quét]: N/A" in s or "[Hệ quả Lab]: N/A" in s:
            errors.append(
                f"[Block {idx}] Phát hiện rò rỉ thẻ tham số mô phỏng '[Hệ vật liệu]: N/A': {s[:90]}..."
            )

        # Check 11: Nested Superscript / Subscript Tags Gate (Zero-Nested-Tags Gate)
        m_nested = _NESTED_SUP_SUB_RE.search(s)
        if m_nested:
            errors.append(
                f"[Block {idx}] Phát hiện thẻ lồng nhau '{m_nested.group(0)}' (ReportLab không hỗ trợ nested sup/sub). "
                f"Bắt buộc tách lớp hoặc chuyển sang diễn giải căn thức/số mũ đơn: {s[:90]}..."
            )

        # Check 12: Zero-Raw-Chemical-Formulas Gate (Cấm công thức hóa học chữ phẳng)
        m_chem = _RAW_CHEM_FORMULA_RE.search(s)
        if m_chem:
            errors.append(
                f"[Block {idx}] Phát hiện công thức hóa học chữ phẳng '{m_chem.group(0)}' thiếu thẻ <sub>. "
                f"Bắt buộc định dạng subscript chuẩn (ví dụ 'WO<sub>3</sub>', 'g-C<sub>3</sub>N<sub>4</sub>'): {s[:90]}..."
            )

        # Check 13: Zero-Raw-Band-Variables Gate (Cấm biến số dải năng lượng/vật lý chữ phẳng)
        m_band = _RAW_BAND_VAR_RE.search(s)
        if m_band:
            errors.append(
                f"[Block {idx}] Phát hiện biến số dải năng lượng chữ phẳng '{m_band.group(0)}' chưa bọc HTML tags. "
                f"Bắt buộc định dạng '<i>E</i><sub>CB</sub>', '<i>E</i><sub>VB</sub>', hoặc '<i>E<sub>g</sub></i>': {s[:90]}..."
            )



    if require_5_blocks:
        # HARD GATE: KHÓA CỨNG BẮT BUỘC DÒNG CHẢY NHẬN THỨC NGUYÊN LÝ ĐẦU 3 KHỐI
        # 1. Cấm tuyệt đối cấu trúc 5 giai đoạn di sản (Zero-Legacy-Stages Gate)
        legacy_stage_matches = re.findall(
            r"\b(?:Giai\s+đoạn|GIAI\s+ĐOẠN)\s+[1-5]\b", combined_text
        )
        if legacy_stage_matches:
            errors.append(
                f"VI PHẠM QUY CHUẨN SƯ PHẠM (Legacy Stages Deprecated): Phát hiện cấu trúc di sản {list(set(legacy_stage_matches))}. "
                "Cấu trúc 5 giai đoạn đã bị khai trừ hoàn toàn. Bắt buộc 100% chuyên khảo phải tuân thủ 'Dòng chảy Nhận thức Nguyên lý Đầu 3 Khối' "
                "(Khối 1: Teleology & Spatial Context, Khối 2: Mechanistic Blending & Derivation, Khối 3: Boundary Audit & Engineering Schema)."
            )

        # 2. Bắt buộc hiện diện đầy đủ cả 3 Khối trong toàn văn chuyên khảo
        for k in range(1, 4):
            tag1 = f"Khối {k}:"
            tag2 = f"KHỐI {k}:"
            tag3 = f"Khối {k}"
            tag4 = f"KHỐI {k}"
            if not any(t in combined_text for t in [tag1, tag2, tag3, tag4]):
                errors.append(
                    f"VI PHẠM DÒNG CHẢY 3 KHỐI: Thiếu tiêu đề 'Khối {k}:' trong chuyên khảo bài giảng."
                )

        # 3. Khóa cứng trọn vẹn 3 Khối trên TỪNG Luận điểm Vi mô (Per-MPT 3-Block Hard Gate)
        mpt_blocks = re.split(r"(?:Luận điểm\s+\d+\.\d+\.\d+)", combined_text)
        if len(mpt_blocks) > 1:
            for mpt_idx, mpt_chunk in enumerate(mpt_blocks[1:], start=1):
                missing_blocks = []
                for k in (1, 2, 3):  # Khóa cứng cả 3 Khối trong từng MPT
                    if not any(t in mpt_chunk for t in [f"Khối {k}:", f"KHỐI {k}:", f"Khối {k}", f"KHỐI {k}"]):
                        missing_blocks.append(f"Khối {k}")
                if missing_blocks:
                    errors.append(
                        f"VI PHẠM KHUNG SƯ PHẠM MPT (Luận điểm vi mô thứ {mpt_idx}): Thiếu {missing_blocks}. "
                        "Bắt buộc mỗi MPT phải có trọn vẹn Khối 1 (Teleology & Spatial), Khối 2 (Mechanistic Blending & Derivation) "
                        "và Khối 3 (Boundary Audit & Engineering Schema)."
                    )

        # Elastic Depth Gate: MPT Density & Anti-Compression (Bám sát cấu trúc thực tế tài liệu gốc)
        mpt_matches = re.findall(r"Luận điểm\s+\d+\.\d+\.\d+", combined_text)
        unique_mpts = sorted(list(set(mpt_matches)))
        if len(unique_mpts) < 1:
            errors.append(
                "VI PHẠM UNBOUNDED DEPTH: Không tìm thấy Luận điểm Vi mô (MPT) nào. "
                "Quy chuẩn chuyên khảo bắt buộc tối thiểu >= 1 MPT độc lập cho mỗi Mục X.Y bám sát cấu trúc tài liệu gốc."
            )

        # Kiểm tra Giải phẫu Động lực học & Tham số Vận hành (Bộ Tứ Câu Hỏi Kỹ Sư Trưởng) (Thuật toán 4, 5, 8, 12)
        # Hỗ trợ song song cả nhãn học thuật mới và nhãn cũ để đảm bảo 100% Zero-Regression
        engineer_questions_matches = re.findall(
            r"(?:Giải phẫu Động lực học|Bộ Tứ Câu Hỏi|Cơ chế vi mô cốt lõi|Thông số ta có thể chủ động điều khiển|Tín hiệu thực nghiệm quan sát được|Phạm vi hoạt động tối ưu|Cuộc giằng co vi mô|Cần gạt điều khiển|Đáp ứng vĩ mô|Vùng công tác hợp lệ|Phương trình cốt trụ|Mỏ neo TVD)",
            combined_text,
            re.IGNORECASE
        )
        if len(engineer_questions_matches) < len(unique_mpts):
            errors.append(
                f"THIẾU KHỐI GIẢI PHẪU ĐỘNG LỰC HỌC & THAM SỐ VẬN HÀNH: Số khối phát hiện ({len(engineer_questions_matches)}) "
                f"nhỏ hơn số MPT ({len(unique_mpts)}). Cấm dẫn xuất đại số râu ria; bắt buộc có đủ khối Giải phẫu Động lực học & Tham số Vận hành cho mỗi MPT."
            )





    if errors:

        raise AssertionError(

            "LINTER FAIL (assert_monograph_text_compliance):\n- " + "\n- ".join(errors)

        )

    return {"status": "PASS", "checked_blocks": len(text_blocks)}





def assert_monograph_compliance(

    pdf_path: str,

    text_blocks: list = None,

    require_5_blocks: bool = True,

    min_pages: int = 1,

) -> dict:

    """

    Full pre-flight verification of both text compliance and compiled PDF integrity.

    Enforces size caps, duplicate checks, and Elastic Depth page count.

    """

    if text_blocks is not None:

        assert_monograph_text_compliance(text_blocks, require_5_blocks=require_5_blocks)



    if not os.path.exists(pdf_path):

        raise AssertionError(f"LINTER FAIL: Tệp PDF không tồn tại tại {pdf_path}")

    size_kb = os.path.getsize(pdf_path) / 1024.0

    if size_kb < 5.0:

        raise AssertionError(f"LINTER FAIL: Tệp PDF quá nhỏ ({size_kb:.2f} KB), nghi ngờ rỗng.")

    if size_kb > 5120.0:

        raise AssertionError(f"LINTER FAIL: Tệp PDF ({size_kb / 1024.0:.2f} MB) vượt quá giới hạn dung lượng 5 MB.")



    base_name = os.path.basename(pdf_path)

    if re.search(r"\s\(\d+\)\.pdf$", base_name):

        raise AssertionError(

            f"LINTER FAIL: Phát hiện tệp trùng lặp Google Drive xung đột '{base_name}'. Phải dùng tên tệp nguyên tử."

        )



    # Elastic Depth Gate: Minimum Page Count (Co giãn tự nhiên theo khối lượng kiến thức, min >= 1 trang)

    page_count = 0

    try:

        import pymupdf

        doc = pymupdf.open(pdf_path)

        page_count = len(doc)

        doc.close()

    except Exception:

        try:

            import fitz

            doc = fitz.open(pdf_path)

            page_count = len(doc)

            doc.close()

        except Exception:

            pass



    if page_count > 0 and page_count < min_pages:

        raise AssertionError(

            f"LINTER FAIL (assert_monograph_compliance): Chuyên khảo chỉ có {page_count} trang (< {min_pages} trang). "

            f"Tệp PDF phải có tối thiểu >= {min_pages} trang A4 hợp lệ."

        )



    return {

        "status": "PASS",

        "pdf_path": pdf_path,

        "size_kb": round(size_kb, 2),

        "page_count": page_count,

    }


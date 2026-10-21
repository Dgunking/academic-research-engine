---
name: monograph-pdf-publisher
description: Chế bản chuyên khảo PDF bằng Python ReportLab theo chuẩn Typography DejaVu, công thức 3 cấp và kịch bản tự chứa trên Google Antigravity.
---
# Monograph PDF Publisher (ReportLab Typesetting Engine)

Kỹ năng chuyên trách chế bản, định dạng Typography và đóng gói tệp bài giảng chuyên khảo PDF hoàn chỉnh bằng thư viện Python `reportlab` theo Khung Sư phạm Lũy tiến 5 Giai đoạn (`Visual Anchor & Causal Flowchain`) trên môi trường Google Antigravity Native Engine (Local OS / PowerShell / Python 3.12).

*Hợp đồng Đầu vào / Đầu ra:* Nhận bản thảo toàn văn 5 Giai đoạn từ `engineering-instructor`, ảnh PNG $\ge 300\text{ DPI}$ từ `physics-diagram-studio`, chuẩn danh pháp từ `academic-terminology-guardian`; xuất tệp PDF chuyên khảo hoàn chỉnh trực tiếp qua **Python 3.12 Host CLI của Antigravity**.

---

## 1. Quy Chuẩn Typography & Bố Cục Trang In A4

### 1.1. Kiểu Chữ & Phân Cấp Tiêu Đề 5 Giai Đoạn (Sentence Case)
- **Thân bài (Body text):** Cỡ chữ 13 pt (leading 18 pt), màu `#212529`, căn đều hai bên (`TA_JUSTIFY`), sử dụng font TrueType Unicode `DejaVuSerif`.
- **Phân cấp tiêu đề (Màu `#0072BD` in đậm, chuẩn Sentence case theo Nghị định 30, font `DejaVuSans-Bold`):**
  * **H1 (16 pt, leading 21 pt):** Tiêu đề phân mục chuyên khảo (`Mục X.Y: [Tên phân mục]`).
  * **H2 (14 pt, leading 19 pt):** Tiêu đề Luận điểm Vi mô (`Luận điểm X.Y.k: [Tên luận điểm]`) và `Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Thử thách CER)`.
  * **H3 (12 pt, leading 16 pt):** Tiêu đề 4 giai đoạn thành phần (`Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu`, `Giai đoạn 2: Ví dụ tối giản và hạt nhân vật lý`, `Giai đoạn 3: Thực hành có hướng dẫn và dẫn xuất vi mô từng bước`, `Giai đoạn 4: Phân tích các biến thể và khảo sát tiệm cận kỹ thuật`).
- **Khoảng cách lề tài liệu A4:** Lề trái 40 pt, lề phải 40 pt, lề trên 46 pt, lề dưới 46 pt (vùng in khả dụng rộng 515,27 pt).

### 1.2. Phân Tầng Hiển Thị Công Thức 3 Cấp & Chuẩn Hóa Phân Số (Zero-Slash-Fractions)
- **Cấp 1 (Inline HTML trong văn bản thường):** Biểu thức ngắn không chứa phân thức. Biến số in nghiêng (`<i>x</i>`, `<i>t</i>`, `<i>E</i>`), hàm lượng giác/toán tử in đứng (`sin`, `cos`), vectơ in đậm (`<b>E</b>`, `<b>B</b>`). Cấm để rò rỉ mã LaTeX backslash thô (`\theta`, `\frac`) và cấm tuyệt đối rò rỉ thực thể HTML đặt tên thô (`&beta;`, `&nu;`, `&tau;`, `&mu;`, `&Delta;`, `&ndash;`, `&mdash;`, `&minus;`, `&middot;`, v.v.) trong văn bản hay bảng. 100% ký hiệu Hy Lạp và dấu nối bắt buộc dùng trực tiếp ký tự Unicode DejaVu (`β`, `ν`, `τ`, `μ`, `Δ`, `–`, `—`, `−`, `·`) hoặc hàm `wrap_math_glyphs` để tự động giải mã sang Unicode trước khi kết xuất. Ký hiệu `↳` (Inline Code Badge, dẫn xuất trung gian) bắt buộc phải nằm trên dòng độc lập riêng biệt (đứng ở đầu khối hoặc có thẻ `<br/>` đứng liền trước; cấm dính dòng). **TUYỆT ĐỐI CẤM VIẾT PHÂN SỐ GẠCH CHÉO `/` TRONG CÔNG THỨC TOÁN** (như `ρ / ε₀`, `∂ρ/∂t`, `1 / r²`, `(cos α dS) / r²`, `1 / c²`). Mọi công thức chứa phân số bắt buộc tách thành khối Cấp 2 hoặc Cấp 3 kết xuất bằng LaTeX Mathtext với phân thức gạch ngang chuẩn `\frac{a}{b}`.
- **Cấp 2 (Mắt xích trung gian trong `Causal Flowchain` tại Giai đoạn 3):** Sử dụng hàm `build_intermediate_equation(latex_eq, label_text)` kết xuất qua Mathtext 300 DPI, đặt trên nền `#F8F9FA` kèm nhãn mũi tên (`⇒`, `↳`). Bảng công thức có đệm ô `TOPPADDING=8, BOTTOMPADDING=8`, dãn cách hàng nội bộ `linespacing=2.2`, dùng `\\[8pt]` giữa các dòng phương trình, và Spacer dưới bảng `10 pt`. Bọc `KeepTogether` cho từng mắt xích đơn lẻ (chống khoảng trắng rỗng $> 25\%$).
- **Cấp 3 (Hệ thức Cột trụ độc lập tại Giai đoạn 2):** Sử dụng hàm `build_target_equation_block(latex_eq, nomenclature_rows)` đóng khung vạch dọc `2 pt` màu `#0072BD` trên nền `#F0F7FF` (đệm ô `10 pt`, dãn cách hàng nội bộ `linespacing=2.2`), bọc liền khối cùng **Bảng Nomenclature 4 cột chuẩn ISO 80000-2**: `Tên đại lượng | Ký hiệu ISO 80000-2 | Đơn vị SI | Ý nghĩa vật lý vi mô & Hình học không gian`. Đệm Spacer sau bảng là `12 pt`. Khối này chỉ xuất hiện duy nhất 1 lần cho mỗi MPT tại Giai đoạn 2.
- **Causal Flowchain Compiler theo Thuật toán 12 (`MALAE`):** Bắt buộc mọi quá trình vật lý hiển thị dạng chuỗi mũi tên định hướng $A \xrightarrow[\text{Biên}]{\text{Vi mô}} B \Longrightarrow C$; giới hạn cứng $\le 65\text{ từ/khối}$ liên tiếp nếu không có mũi tên hoặc công thức. 100% công thức toán học đi qua Giải phẫu Phương trình Liên dòng 3 Cấp (Tầng 1: Vai trò vật lý $\to$ Tầng 2: Bảng tham số vi mô chuẩn SI theo Luật 04 và HTML `<i>...</i>` $\to$ Tầng 3: Kiểm tra 2 giới hạn tiệm cận cực trị biên).

### 1.3. Nhúng Hình Ảnh, Xác Thực Sidecar Manifest & Độ Lấp Đầy Trang
- **Kích thước nhúng ảnh:** [Mo_Phong] rộng 460–500 pt; [Goc] ngang rộng 430–485 pt hoặc vuông/dọc rộng 360–420 pt. Cấm thu nhỏ chiều cao $\le 180\text{ pt}$.
- **Xác thực Sidecar Manifest Bắt buộc (Zero-Trust Manifest Verification Gate — Thuật toán 13):** Khi nhúng tệp ảnh [Mo_Phong]_...png, hàm embed_figure_with_caption() bắt buộc kiểm tra sự tồn tại của tệp sidecar manifest .manifest.json tương ứng, đối soát mã băm SHA-256 của ảnh, xác thực các tiêu chí hình học ( \le 7.0\text{ in}$, $\text{fontsize} \ge 10.0\text{ pt}$, $\delta_{\text{geom}} \ge 8\%$, $\delta_{\text{spine}} \ge 5\%$, $\delta_{\text{box}} \ge 6\text{ pt}$, zero slash fractions). Nếu thiếu manifest hoặc mã băm không khớp: từ chối nhúng và ném ngoại lệ dừng an toàn.
- **Độ lấp đầy trang:** Luồng chảy tự nhiên liên tục (Continuous Natural Flow), không chèn PageBreak() tùy tiện giữa các khối, độ lấp đầy trang $\ge 75\text{–}80\%$.

---

## 2. Khung Mã ReportLab Tự Chứa Cho Gemini Spark (Self-Contained Lean Template)

Khi Gemini Spark cần xuất bản tệp PDF chuyên khảo trong Code Execution sandbox, **sử dụng trực tiếp khung mã tự chứa dưới đây**. Mã nguồn tự động khai thác font Unicode DejaVu từ `matplotlib`, tạo canvas 2 lượt đánh số trang và Bookmark PDF 3 cấp mà không cần bất kỳ module ngoài nào:

```python
import os
import matplotlib.font_manager as fm
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, Flowable
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# 1. TỰ ĐỘNG TÌM & ĐĂNG KÝ FONT TRUETYPE UNICODE TỪ MATPLOTLIB (100% TIẾNG VIỆT & TOÁN HỌC)
serif_path = fm.findfont("DejaVu Serif")
sans_path = fm.findfont("DejaVu Sans")

pdfmetrics.registerFont(TTFont("DejaVuSerif", serif_path))
pdfmetrics.registerFont(TTFont("DejaVuSerif-Bold", fm.findfont("DejaVu Serif:bold") or serif_path))
pdfmetrics.registerFont(TTFont("DejaVuSerif-Italic", fm.findfont("DejaVu Serif:italic") or serif_path))
pdfmetrics.registerFont(TTFont("DejaVuSans", sans_path))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", fm.findfont("DejaVu Sans:bold") or sans_path))
pdfmetrics.registerFontFamily("DejaVuSerif", normal="DejaVuSerif", bold="DejaVuSerif-Bold", italic="DejaVuSerif-Italic")
pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans-Bold")

# 2. CANVAS 2 LƯỢT: ĐÁNH SỐ "TRANG X / Y" VÀ KHUNG FOOTER CHUẨN HUST
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        self.setFont("DejaVuSans", 9)
        self.setFillColor(HexColor("#495057"))
        page_str = f"Trang {self._pageNumber} / {total_pages}"
        self.drawRightString(A4[0] - 40, 25, page_str)
        self.drawString(40, 25, "Khoa Vật lý Kỹ thuật — ĐHBK Hà Nội (HUST)")
        self.setStrokeColor(HexColor("#CED4DA"))
        self.setLineWidth(0.5)
        self.line(40, 36, A4[0] - 40, 36)
        self.restoreState()

# 3. BOOKMARK ĐA TẦNG 3 CẤP CHO PDF (Level 0: H1, Level 1: H2, Level 2: H3)
class Bookmark(Flowable):
    def __init__(self, key: str, title: str, level: int = 0):
        super().__init__()
        self.key = key
        self.title = title
        self.level = level

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, level=self.level, closed=False)

def build_spark_pdf(filename="Bai_Giang_Chuyen_Khao_HUST.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4, leftMargin=40, rightMargin=40, topMargin=46, bottomMargin=46)
    styles = getSampleStyleSheet()

    body_style = ParagraphStyle('HUST_Body', parent=styles['Normal'], fontName='DejaVuSerif', fontSize=13, leading=18, textColor=HexColor('#212529'), alignment=TA_JUSTIFY)
    h1_style = ParagraphStyle('HUST_H1', fontName='DejaVuSans-Bold', fontSize=16, leading=21, textColor=HexColor('#0072BD'), spaceAfter=8)
    h2_style = ParagraphStyle('HUST_H2', fontName='DejaVuSans-Bold', fontSize=14, leading=19, textColor=HexColor('#0072BD'), spaceBefore=12, spaceAfter=6)
    h3_style = ParagraphStyle('HUST_H3', fontName='DejaVuSans-Bold', fontSize=12, leading=16, textColor=HexColor('#0072BD'), spaceBefore=8, spaceAfter=4)

    story = []

    # 1. Tiêu đề H1 phân mục kèm Bookmark Level 0
    story.append(Bookmark("muc_1_1", "Mục 1.1: Cấu trúc vùng năng lượng và phát xạ tự phát trong bán dẫn", level=0))
    story.append(Paragraph("Mục 1.1: Cấu trúc vùng năng lượng và phát xạ tự phát trong bán dẫn", h1_style))
    story.append(Spacer(1, 10))

    # 2. GIAI ĐOẠN 1: Giới thiệu khái niệm & Trực quan hóa mở đầu kèm Bookmark
    story.append(Bookmark("luan_diem_1_1_1", "Luận điểm 1.1.1: Quá trình tái hợp bức xạ qua vùng cấm trực tiếp", level=1))
    story.append(Paragraph("Luận điểm 1.1.1: Quá trình tái hợp bức xạ qua vùng cấm trực tiếp", h2_style))
    story.append(Bookmark("giai_doan_1", "Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu", level=2))
    story.append(Paragraph("Giai đoạn 1: Giới thiệu khái niệm và trực quan hóa mở đầu", h3_style))
    story.append(Paragraph("↳ <b>[Bản chất & Mục tiêu hình vẽ]:</b> Thiết lập quy luật phân bố phổ phát xạ tự phát của hạt tải trong bán dẫn vùng cấm trực tiếp GaAs.", body_style))
    story.append(Spacer(1, 8))

    return doc, story
```

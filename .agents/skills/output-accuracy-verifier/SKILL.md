---
name: output-accuracy-verifier
description: Trạm kiểm định chất lượng nhị phân 17 điểm (Pass/Fail Gate) và phản tỉnh tự sửa lỗi (Self-Healing Loop) kết hợp hệ thống 5 trạm chốt chặn DOHG 2.0 trên Google Antigravity.
---
# Output Accuracy Verifier (Pre-Flight Sanity Gate & DOHG 2.0)

Kỹ năng kiểm định chất lượng độc lập, đóng vai trò như một bộ lọc phản tỉnh (Self-Reflection Gate) kiểm soát toàn vẹn dữ liệu, tiêu chuẩn kỹ thuật và kỷ luật tài nguyên lưu trữ trước khi Antigravity xuất phản hồi hoặc bàn giao tệp cho Bùi Trung Dũng tại ĐHBK Hà Nội.

*Hợp đồng Đầu vào / Đầu ra:* Kiểm tra nhị phân 17 điểm (Pass/Fail Gate) trên toàn bộ bản thảo văn bản, mã Python, tệp đồ thị/PDF và tính toàn vẹn tài nguyên Google Drive; kích hoạt vòng lặp tự sửa lỗi (Self-Healing tối đa 5 lần) trong môi trường thực thi trước khi hoàn tất.

---

## 1. Bảng Checklist Kiểm Định Nhị Phân 17 Điểm (Pass/Fail Gate)

Mọi phản hồi chuyên môn, tệp PDF chuyên khảo và đồ thị mô phỏng bắt buộc đạt 100% cả 17 tiêu chí dưới đây theo Thuật toán 8:

| Mã | Nhóm kiểm định | Nội dung tiêu chí kiểm định (Pass/Fail Gate) |
| :--- | :--- | :--- |
| **01** | **Độ sâu Co giãn & Độ phủ 100% (Elastic Depth & Zero-Omission Gate)** | Bóc tách đầy đủ các Luận điểm Vi mô độc lập (`MPT`) theo tài liệu gốc (`1 Mục X.Y = 1 File PDF`). Dung lượng trang co giãn tự nhiên theo khối lượng kiến thức thực tế (Lõi lý thuyết $\ge 10\text{ trang}$, Tiểu mục ngắn $5\text{–}6\text{ trang}$, không ép đáy gây bơm chữ, không giới hạn trần Unbounded Depth). Kiểm toán nhị phân bảo đảm 100% phương trình, giả thiết, hình vẽ từ Slide & Sách được bẻ thành các Khối vi mô 2–3 câu; kiểm toán phần dư rỗng $\mathcal{R}_{\text{residual}} = \emptyset$; cấm tóm tắt hời hợt hay bỏ sót luận điểm. |
| **02** | **Khung Sư phạm Lũy tiến 5 Giai đoạn** | Triển khai tuần tự qua 5 giai đoạn sư phạm (`Giai đoạn 1: Giới thiệu khái niệm` $\to$ `Giai đoạn 2: Ví dụ tối giản` $\to$ `Giai đoạn 3: Thực hành có hướng dẫn` $\to$ `Giai đoạn 4: Phân tích biến thể`) cho từng MPT; hội tụ tại `Giai đoạn 5: Thử thách tự luyện & Dự đoán lỗi sai (Thử thách CER)` ở cuối bài. |
| **03** | **Ẩn dụ 3 Nhịp & ARegistry** | Ẩn dụ cơ học vĩ mô Khóa biến số 3 Nhịp áp dụng mô hình SME đăng ký vào `ARegistry` (`analogy_registry`) toàn chương để chống lặp lại (xuất hiện duy nhất 1 lần/MPT tại Giai đoạn 2 bằng văn bản, không vẽ ảnh); sạch 100% câu sáo rỗng. |
| **04** | **Đối soát Ký hiệu & Zero-Symbol-Drift** | Khớp 100% hệ ký hiệu trên trục, tên góc và mũi tên thực tế đọc từ OCR hình gốc theo Master Variable Dictionary của Thuật toán 2 (`HPDE 2.0`) và Từ điển Thuộc tính $G_{\text{attr}}$ của Thuật toán 10 (`ATCC`). |
| **05** | **Bố trí 5 Mắt xích OCR** | Mắt xích 1–3 đặt ngay dưới hình mở đầu tại Giai đoạn 1 kèm Nghịch lý mở đầu; Mắt xích 4–5 tích hợp trực tiếp vào dẫn xuất tại Giai đoạn 3. |
| **06** | **Quy ước Dấu Đại số & Hình học** | Khớp tuyệt đối giữa tam giác hình học giải tích và quy ước dấu âm/dương trong phương trình đại số tổng quát. |
| **07** | **Vùng áp dụng & Khảo sát Tiệm cận** | Giai đoạn 3 mở đầu bằng Vùng áp dụng và Điều kiện biên; Giai đoạn 4 khảo sát $\ge 2$ cực hạn đối lập ($T \to 0$ vs. $300\text{ K}$, $\omega \to 0$ vs. $\infty$) và liên kết thông số linh kiện ($I_{\text{th}}, \eta_d, \lambda, R_s$). |
| **08** | **Causal Flowchain & Dẫn xuất Tường minh** | Dẫn xuất từng bước theo `Causal Flowchain Compiler` $\le 65\text{ từ/khối}$, gắn nhãn `↳ [Tường minh bước biến đổi trung gian từ slide gốc]:` cho các bước mở rộng (tối thiểu 1 bước tường minh cho mỗi MPT, Zero-Skipped-Steps). |
| **09** | **Hệ thức Cột trụ & Bảng Nomenclature** | Hệ thức Cột trụ Cấp 3 đóng khung `#0072BD` trên nền `#F0F7FF` kèm Bảng Nomenclature 4 cột ISO 80000-2 duy nhất tại Giai đoạn 2. |
| **10** | **Chế độ Vận hành Song song** | Đúng 2 chế độ: Hỏi đáp học thuật trả lời trực tiếp trên Chat; chế bản đóng gói PDF chạy qua Python Code Execution host. |
| **11** | **Zero-Text Chat Rule** | Khi chạy `/learn`: Khung Chat chỉ xuất duy nhất Bộ ba Mỏ neo Điều hướng (~2s), không in bài giảng dài làm loãng context. |
| **12** | **Clean-Slate /edit** | Khi gọi `/edit`: Mặc định làm lại toàn bộ nội dung và tạo lại ảnh mới 100% từ đầu (xóa cache tạm `%TEMP%/hust_eq_cache/`, tính toán lại, biên dịch mới); trừ khi người học viết rõ đích danh nội dung cần chỉnh sửa cục bộ. |
| **13** | **Kiểm định Đồ họa MATLAB (HDSE)** | Đồ thị MATLAB: Khung 4 cạnh `#1F1F1F`, inward ticks, cỡ chữ $\ge 10.0\text{ pt}$, đạt chuẩn Triple Buffer Envelope ($\delta_{\text{geom}} \ge 8\%$ cho 100% đường nét kể cả nét đứt tiệm cận, $\delta_{\text{box}} \ge 6\text{ pt}$, $\delta_{\text{spine}} \ge 5\%$). Quét cạn Luật 14 Zero-Slash-Fractions trên toàn bộ nhãn/trục/legend. Bắt buộc vượt qua `assert_triple_buffer_geometry(fig, ax)`. PNG $\le 300\text{ KB}$, DPI $\ge 300$. |
| **14** | **Kiểm định Chế bản PDF (Pre-Flight Gates)** | Khổ A4, margins 40/46 pt, styles H1–H3 Sentence case, nhúng ảnh chuẩn hình học. Dung lượng PDF $\le 5\text{ MB}$, vector DejaVu sắc nét, bookmarks 3 cấp (`H1 → H2 → H3`). Đạt kiểm định `assert_monograph_text_compliance` (sạch mã LaTeX thô, sạch biến ASCII thô, `↳` xuống dòng độc lập, sạch thực thể HTML thô) và `assert_monograph_compliance`. |
| **15** | **Ngôn ngữ Khoa học & Danh pháp (ATCC)** | Chuẩn Sentence case (Nghị định 30), số APA 7, đơn vị SI (Luật Đo lường 04). 100% thuật ngữ Trạng thái 1 giữ định dạng `tiếng Việt (english term)` trong PDF; thuật ngữ Trạng thái 2 rà soát tối thiểu 10 nguồn tài liệu chuẩn và đối chiếu chéo ít nhất 3 lần trước khi đưa vào hàng đợi nạp NotebookLM. |
| **16** | **Kỷ luật Tài nguyên Drive (%TEMP% Isolation)** | Sạch 100% tệp tạm/cache trên `G:\`; ghi đè nguyên tử `os.replace` không sinh hậu tố ` (1).pdf` hay ` (1).png`; đúng cây thư mục Whitelist `G:\My Drive\NotebookLM - Academic Knowledge Base\<Tên_Học_Phần>\`. |
| **17** | **Khóa cứng Pha 1 (Sample Gate Protocol)** | Tuyệt đối cấm tự động kích hoạt Pha 2 (Autonomous Batch Rollout) khi người học chưa duyệt tường minh mẫu Pha 1 trên Chat; cấm tự ý cam kết chất lượng hàng loạt khi chưa qua đối chuẩn thực nghiệm. |

---

## 2. Cơ Chế Phản Tỉnh Tự Sửa Lỗi (Self-Healing Loop)
- **Tự động rà soát trước khi xuất xưởng:** Trước khi hiển thị kết quả cho người học hoặc đẩy tệp sang Google Drive, Antigravity tự đối soát qua 17 tiêu chí trên.
- **Nếu phát hiện lỗi (Reject & Fix):** 
  * Lỗi hình thức, LaTeX thô, cỡ chữ, dung lượng tệp: Sửa lại tham số định dạng và tối ưu hóa qua Pillow/ReportLab trong môi trường Python 3.12 host.
  * Lỗi đè nét tiệm cận / vi phạm Triple Buffer Envelope ($\delta_{\text{geom}} < 8\%$, $\delta_{\text{spine}} < 5\%$, $\delta_{\text{box}} < 6\text{ pt}$): Tinh gọn độ dài dòng Callout ($\le 20\text{–}25$ ký tự/dòng), chuyển Callout sang hành lang trống (Corridor Strategy), hoặc nới trục y thêm 20–35% và tái kiểm định bằng `assert_triple_buffer_geometry(fig, ax)`.
  * Lỗi bản chất vật lý, thiếu bước biến đổi, thiếu Nomenclature: Bổ sung trực tiếp mắt xích nhân quả trước khi xuất kết quả.
  * Lỗi phân số gạch chéo, công thức nén sát: Thay thế bằng phân số gạch ngang $\frac{a}{b}$ qua Mathtext, dãn `linespacing=2.2`, bổ sung `\\[8pt]` và Spacers $\ge 8\text{–}12\text{ pt}$.
  * Lỗi tài nguyên Drive, phát sinh file lock hoặc tệp trùng ` (1).pdf`: Dọn dẹp cache `%TEMP%`, kiểm tra quyền ghi tệp và dùng phương thức thay thế nguyên tử `os.replace`.
  * Tối đa 5 lần tự sửa ngầm. Nếu sau 5 lần vẫn bế tắc: Dừng an toàn và báo cáo chi tiết điểm nghẽn kỹ thuật cho Dũng.

---

## 3. Hệ Thống 5 Trạm Chốt Chặn Đầu Ra Xác Định (DOHG 2.0 Hard Assertion Stations)

Mọi tệp xuất bản bắt buộc vượt qua 5 trạm chốt chặn bằng mã thực thi nhị phân khách quan ngoại vi:

1. **Trạm 1: Static AST & Typography Pre-Flight Linter:**
   - Regex L1: Cấm 100% rò rỉ mã LaTeX thô trong thẻ XML `Paragraph` (`\frac`, `\eta`, `\tau`, `\omega`...). Bắt buộc định dạng thẻ HTML (`<i>`, `<sub>`, `<sup>`).
   - Regex L2: Khóa cứng Luật 14 — Cấm tuyệt đối phân số gạch chéo `/` trong công thức và nhãn/trục đồ thị. Bắt buộc hiển thị phân số gạch ngang chuẩn $\frac{a}{b}$ qua ảnh Mathtext $\ge 300\text{ DPI}$.
   - Regex L3: Cấm biến mã nguồn ASCII `E_c(z)`, `N_th`, `I_th`. Bắt buộc chuẩn hóa typography `<i>E<sub>c</sub></i>(<i>z</i>)`, `<i>N</i><sub>th</sub>`.
   - Regex L4 (Arrow Linebreak Gate): Ký hiệu dẫn xuất `↳` bắt buộc đứng đầu khối hoặc có `<br/>` đứng liền trước; cấm dính dòng với câu văn trước.
   - Regex L5 (Zero-Raw-HTML-Entities Gate): Quét cạn `_RAW_NAMED_ENTITY_RE` cấm thực thể HTML đặt tên thô (`&beta;`, `&nu;`, `&tau;`, `&Delta;`, `&ndash;`, `&minus;`...).

2. **Trạm 2: Geometry Collision & Cryptographic Manifest Detector (HDSE & ZT-GVLE / ssert_triple_buffer_geometry):**
   - Đo pixel thực tế trên Canvas: $\delta_{\text{geom}} \ge 8\%$ cách tuyệt đối cả đường cong và **toàn bộ nét đứt tiệm cận** ({\text{th}}, g_{\text{th}}$).
   - $\delta_{\text{spine}} \ge 5\%$, $\delta_{\text{box}} \ge 6\text{ pt}$, Fontsize $\ge 10.0\text{ pt}$ cho 100% nhãn trục, annotation và legend. Khung 4 cạnh #1F1F1F, inward ticks, 6 màu chuẩn HUST Lab. Quét cạn Luật 14 cấm phân số gạch chéo trên title, xlabel, ylabel, texts, legend.
   - Kiểm tra A4 Canvas Width Lock ( \le 7.0\text{ in}$), đám mây điểm ảnh vật cản $\Delta s \le 2.5\text{ px}$, nhãn elip đẳng cự và xác thực tính toàn vẹn của mã băm SHA-256 qua tệp Cryptographic Sidecar Manifest (.manifest.json).

3. **Trạm 3: Post-Build Binary & Figure Coverage Gate (PyMuPDF / itz):**
   - Kiểm toán dung lượng co giãn: ssert len(doc) >= Blueprint.estimated_pages.
   - Kiểm toán độ phủ hình ảnh gốc và mô phỏng: $\mathbf{F}_{\text{blueprint}} \subseteq \mathbf{F}_{\text{rendered\_pdf}}$ (Zero-Omission for Images). Thiếu dù chỉ 1 hình gốc $\implies$ Ném ngay AssertionError.
   - Xác thực Zero-Trust Manifest: Bắt buộc 100% ảnh [Mo_Phong] nhúng trong PDF đã được giải mã và kiểm chứng khớp mã băm SHA-256 từ .manifest.json.
   - Kiểm toán bước tường minh: Đếm đủ số đoạn '↳ [Tường minh bước biến đổi trung gian từ slide gốc]:' theo số MPT. Đủ chú giải 3 Mắt xích dưới mỗi hình.
4. **Trạm 4: Formal CAS & Epistemic Calibration Gate (SymPy + Bi-NLI):**
   - Xác thực đại số hình thức bằng **SymPy**: `sympy.simplify(Expr_trung_gian - Expr_dich) == 0` cho các bước biến đổi `↳` từ slide gốc, triệt tiêu 100% ảo giác toán học.
   - Kiểm tra tương đương ngữ nghĩa hai chiều $\text{Bi-NLI} \ge 0.85$.
   - Đối chuẩn hằng số bán dẫn 300 K với `materials_db.py` (sai số $\le 1.0\%$). Kích hoạt `Calib-Abstain` dừng an toàn khi $SE(x) > \tau$.

5. **Trạm 5: Atomic Sandbox Gate & Resource Isolation:**
   - Kiểm tra `os.access(..., os.W_OK)`, ghi đè nguyên tử `os.replace` từ `%TEMP%` sang `G:\` triệt tiêu tệp trùng ` (1).pdf`.
   - Quét cạn và dọn sạch 100% tệp rác `.tmp`, `.aux`, `.log` trong `%TEMP%`.

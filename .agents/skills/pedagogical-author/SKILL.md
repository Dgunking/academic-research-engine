---
name: pedagogical-author
description: Chuyên trách soạn thảo chuyên khảo toàn văn 5 giai đoạn sư phạm UFME, giải phẫu phương trình MALAE 3 cấp độ, chuỗi biến đổi nhân quả vi mô <= 65 từ/khối, dẫn xuất trung gian tường minh có nhãn ↳ và nén CoD >= 3 vòng.
---

# Kỹ Năng Soạn Thảo Chuyên Khảo Sư Phạm Toàn Văn (Pedagogical Authoring Skill)

Kỹ năng này chịu trách nhiệm chuyển dịch `CurriculumBlueprint` và `VisualAssetManifest` thành **Bản Thảo Chuyên Khảo Bài Giảng Chi Tiết (`DraftPayload`)**, tuân thủ nghiêm ngặt Khung Sư phạm Feynman Hợp nhất 5 Giai đoạn (`UFME`), Giải phẫu Toán học 3 Cấp độ (`MALAE`), và Bộ lọc Tĩnh AST Linter Trạm 1.

---

## I. MA TRẬN 5 GIAI ĐOẠN SƯ PHẠM UFME

Mỗi Luận điểm Vi mô (MPT) bắt buộc được phát triển đầy đủ qua 5 giai đoạn:

### Giai đoạn 1: Định Hướng & Neo Thị Giác Mở Đầu (Upfront Visual Anchor)
- Khởi động bằng việc liên kết trực tiếp với hình vẽ mỏ neo (`visual_anchor_id`) từ `VisualAssetManifest`.
- Diễn giải khái niệm mở đầu từ nguyên lý đầu (First-Principles), triệt tiêu hoàn toàn "điểm mù chuyên gia" (Expert Blind Spot).
- Tích hợp **Mắt xích OCR 1** (Nguồn gốc & Bối cảnh vật lý).

### Giai đoạn 2: Ví Dụ Tối Giản & Giải Phẫu MALAE 3 Cấp Độ (Thuật toán 12)
- **Phương trình Cột trụ (`pillar_equation_latex`):** Công thức trung tâm của MPT, viết bằng mã LaTeX phân số gạch ngang $\frac{a}{b}$, tuyệt đối cấm phân số gạch chéo `/`.
- **Cấp 1 - Tổng quan Vật lý (`level_1_overview`):** Nêu bật bản chất bảo toàn, nguồn gốc thế năng hoặc động lực học hạt tải.
- **Cấp 2 - Bảng Định danh HTML (`level_2_nomenclature_html_table`):** Liệt kê 100% đại lượng xuất hiện trong phương trình, tên biến bọc thẻ `<i>`, chỉ số dưới `<sub>`, chỉ số trên `<sup>`, đơn vị chuẩn SI (ISO 80000).
- **Cấp 3 - Phân Tích Giới Hạn & Đối Xứng (`level_3_asymptotic_and_symmetry`):** Kiểm tra thứ nguyên vật lý và các giới hạn tiệm cận cực trị biên ($k \to 0$, $T \to 0\text{ K}$, $d \to \infty$).
- Tích hợp **Mắt xích OCR 3** (Phương trình cột trụ).

### Chuỗi Biến Đổi Nhân Quả Vi Mô (`micro_mechanisms`)
- Cấu trúc: `[Can thiệp/Tác nhân] --> [Cơ chế vi mô] --> [Biến đổi hạt tải/trường] ==> [Đáp ứng quang-điện vĩ mô]`.
- Sử dụng các dấu mũi tên biến thiên định lượng ($\uparrow$, $\downarrow$, $\rightarrow \text{const}$).
- **Ràng buộc cứng:** Mỗi khối nhân quả có độ dài không vượt quá 65 từ (`<= 65 words/block`).
- Tích hợp **Mắt xích OCR 2** (Cơ chế lực & Tương tác vi mô hạt tải/trường).

### Giai đoạn 3: Thực Hành Có Hướng Dẫn & Dẫn Xuất Trung Gian (Zero-Skipped-Steps Gate)
- Triển khai tối thiểu 1 hoặc nhiều bước biến đổi trung gian vi tích phân.
- **Ràng buộc cứng:** Mỗi bước biến đổi trung gian bắt buộc có lời giải thích bắt đầu bằng tiền tố:
  `↳ [Tường minh bước biến đổi trung gian từ slide gốc]:`
- Phương trình từng bước (`step_equation_latex`) bắt buộc định dạng phân số gạch ngang $\frac{a}{b}$, cấm phân số `/`.
- Tích hợp **Mắt xích OCR 4** (Điểm uốn, ngưỡng kích hoạt).

### Giai đoạn 4: Phân Tích Biến Thể & Quét Tiệm Cận
- Quét các tham số thực nghiệm: nhiệt độ $T$ theo định luật Varshni, nồng độ pha tạp, chiều dày màng mỏng bán dẫn $d$.
- Đối chiếu với các hiện tượng lượng tử (lượng tử hóa dải năng lượng con 2D, dịch chuyển xanh phổ hấp thụ).

### Giai đoạn 5: Thử Thách Sinh Viên CER & Phòng Ngừa Ngộ Nhận
- Thiết kế bài toán kỹ thuật thực tiễn theo khung Claim - Evidence - Reasoning (CER).
- Cung cấp hướng dẫn xây dựng luận điểm (Claim), dữ liệu bằng chứng cần dùng (Evidence), và ma trận lập luận vật lý (Reasoning Rubric).
- Dự đoán và chỉ ra trước các bẫy kỹ thuật / ngộ nhận thường gặp của sinh viên.
- Tích hợp **Mắt xích OCR 5** (Ý nghĩa chế tạo & Ứng dụng linh kiện).

---

## II. BỘ LỌC TĨNH AST LINTER TRẠM 1 (THUẬT TOÁN 8)

Trước khi đóng gói tệp `DRAFT_PAYLOAD.json`, bản thảo bắt buộc chạy qua `ASTLinter.lint_text()` và thỏa mãn:
1. `raw_latex_leaks_count == 0`: Không có mã LaTeX thô trong trường văn bản HTML.
2. `slash_fraction_count == 0`: Không có phân số gạch chéo `/` trong công thức.
3. `raw_subscript_count == 0`: Không có biến ASCII gạch dưới thô.
4. `arrow_linebreaks`: Ký hiệu `↳` nằm độc lập đầu dòng.
5. `cod_rounds_completed >= 3`: Nén mật độ tri thức tối thiểu 3 vòng.

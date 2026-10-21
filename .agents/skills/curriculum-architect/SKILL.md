---
name: curriculum-architect
description: Hướng dẫn phân rã học liệu đa tầng (Chương -> Mục -> MPT), dựng đồ thị DAG tri thức phi chu trình theo giải thuật Kahn, khóa danh pháp song ngữ ATCC và xuất bản Hợp đồng Dữ liệu CurriculumBlueprint (BLUEPRINT_MUC_X.Y.json) cho hệ thống bài giảng HUST.
---

# Kỹ Năng Phân Rã Học Liệu & Dựng Khung Bài Giảng (Curriculum & Structural Architect Skill)

Kỹ năng này chuyên trách chuyển hóa kho tài liệu nguồn kép (Slide bài giảng HUST & Sách giáo trình chuyên khảo) thành **Bản Thiết kế Đề cương & Đồ thị Tri thức Chuẩn hóa (Curriculum Blueprint)**, bảo đảm tính toàn vẹn học thuật (Zero-Omission) và phi chu trình tuyệt đối (Acyclic DAG).

---

## I. QUY TRÌNH 5 BƯỚC PHÂN RÃ HỌC LIỆU CHUẨN MỰC

```
[Nguồn kép: Slide HUST + Sách GT]
               │
               ▼
   [Bước 1: Pre-Scan Handshake] ──(Thiếu tài liệu)──> [DỪNG AN TOÀN (Hard Stop)]
               │ (Đủ tài liệu)
               ▼
  [Bước 2: Phân rã Neo-Davidsonian & CNF]
               │
               ▼
  [Bước 3: Dựng DAG Tri thức & Giải thuật Kahn] ──(Phát hiện chu trình)──> [GREEDYCYCLEBREAK] (Tối đa 5 lần)
               │ (Acyclic = True)
               ▼
  [Bước 4: Thiết kế MPT & Ánh xạ Visual Anchor]
               │
               ▼
  [Bước 5: Khóa Danh pháp Song ngữ ATCC & Xuất CurriculumBlueprint]
```

### Bước 1: Khảo sát Nguồn kép & Pre-Scan Handshake (Thuật toán 1 DICG 2.0)
- Quét kho học liệu tại `G:\My Drive\NotebookLM - Academic Knowledge Base\<Tên_Học_Phần>\`.
- Kiểm tra sự hiện diện của tệp Slide và Giáo trình tương ứng với chương học.
- Xác thực ngưỡng Token Set Ratio $\ge 80\%$.

### Bước 2: Phân đoạn Nguyên tử hóa & Lọc CNF (Thuật toán 2 HPDE 2.0)
- Áp dụng ngữ nghĩa học Neo-Davidsonian bóc tách từng phát biểu thành mệnh đề nguyên tử.
- Khử phụ thuộc ngữ cảnh triệt để (Full Decontextualization):
  * Thay thế 100% đại từ nhân xưng và đại từ chỉ định bằng danh từ định danh đầy đủ.
  * Tách rời thông tin mô tả thực thể thành mệnh đề độc lập.
- Điều kiện CNF: Mỗi mệnh đề chỉ chứa một khẳng định đơn nghĩa, không sót liên từ đẳng lập nội bộ.

### Bước 3: Dựng Đồ thị Tri thức DAG & Kiểm toán Kahn (Thuật toán 2 & 4)
- Định nghĩa từng nút `KnowledgeDAGNode`:
  * Mã định danh `node_id` duy nhất (ví dụ: `NODE_2_1_1`).
  * Bậc nhận thức Bloom: `Nhớ`, `Hiểu`, `Vận dụng`, `Phân tích`, `Đánh giá`, `Sáng tạo`.
  * Định luật nền tảng năm 1–3 làm gốc (`first_principles_root`).
- Thiết lập các cạnh phụ thuộc `KnowledgeDAGEdge`:
  * `prerequisite`: Tiền đề bắt buộc phải hiểu trước.
  * `causal`: Quan hệ nhân quả vật lý trực tiếp.
  * `generalization`: Mở rộng từ trường hợp riêng sang tổng quát.
  * `boundary_limit`: Điều kiện biên triệt tiêu hoặc chuyển pha.
- **Khóa kiểm toán phi chu trình bằng Giải thuật Kahn:**
  * Tính bán bậc vào (in-degree) cho mọi nút.
  * Duyệt hàng đợi nút có bậc vào bằng 0.
  * Nếu phát hiện chu trình kín ($visited < total$), kích hoạt cơ chế `GREEDYCYCLEBREAK` cắt bỏ cạnh phụ thuộc yếu nhất, thử lại tối đa 5 lần.

### Bước 4: Thiết kế Luận điểm Vi mô (MPT) & Visual Requirements (Thuật toán 4 PLBE)
- Mỗi MPT là một đơn vị sư phạm nguyên tử tương ứng với một mục tiêu nhận thức cụ thể.
- Xác định phương trình giải tích trọng tâm (`target_equations`).
- Khởi tạo yêu cầu hình ảnh mỏ neo (`VisualRequirement`):
  * `MATLAB_SIMULATION`: Cần mô phỏng số liệu vật liệu 300 K (GaAs, InP, GaN...).
  * `DSAFE_CROP`: Cần trích xuất ảnh gốc từ slide hoặc sách với độ phân giải $\ge 300\text{ DPI}$.
  * `SCHEMATIC_DIAGRAM`: Sơ đồ nguyên lý/khối vector.

### Bước 5: Khóa Danh pháp ATCC & Đóng gói Hợp đồng Dữ liệu (Thuật toán 10)
- Rà soát toàn bộ thuật ngữ chuyên ngành qua `TerminologyGuardian`:
  * Tiêu chuẩn hóa danh pháp song ngữ: `tiếng Việt (english term)`.
  * Khóa danh từ mượn nguyên ngữ (không in nghiêng): `laser`, `diode`, `electron`, `photon`...
  * Kiểm soát viết hoa theo Nghị định 30 (Sentence case cho H1–H3).
  * Viết số theo APA 7 và đơn vị SI Luật Đo lường 04 (bắt buộc khoảng cách: $300\text{ K}$, $1.55\text{ }\mu\text{m}$).
- Đóng gói toàn bộ vào schema Pydantic `CurriculumBlueprint`.
- Lưu trữ tệp Hợp đồng: `BLUEPRINT_MUC_X.Y.json`.

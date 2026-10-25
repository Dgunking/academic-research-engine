---
name: quality-gatekeeper
description: Động cơ thẩm định chất lượng nhị phân 18 điểm (Pass/Fail Gate & Gate 18 TVD), kiểm chứng đại số hình thức SymPy CAS, kiểm toán mật mã SHA-256 sidecar manifest, chế bản chuyên khảo ReportLab DejaVu PDF với khung Open CER Box (Zero-Solution trong PDF) và thay thế nguyên tử %TEMP% Isolation trên Google Antigravity.
---

# Quality Gatekeeper & Monograph Publisher Engine (Agent 4 Skill)

Kỹ năng điều phối kiểm định chất lượng toàn diện và chế bản chuyên khảo PDF cho hệ thống bài giảng & nghiên cứu Quang điện tử HUST.

## I. Quy Trình 5 Trạm Chốt Chặn Đầu Ra Xác Định (DOHG 2.0)

1. **Trạm 1: Static AST & Typography Linter**
   - Nạp `DraftPayload` và chạy qua `common.ASTLinter.lint_payload()`.
   - Kiểm tra các điều kiện cứng:
     1. `raw_latex_leaks_count == 0`
     2. `slash_fraction_count == 0`
     3. `raw_subscript_count == 0`
     4. `arrow_inline_count == 0`
     5. `raw_html_entity_count == 0`
     6. `merged_stages_count == 0`
     7. `old_blocks_count == 0`
     8. `nested_tag_errors_count == 0`
     9. `raw_chemical_errors_count == 0`
     10. `raw_band_variable_errors_count == 0`
     11. `unwarranted_claims_count == 0` (Zero-Unwarranted Claims Gate: Đánh FAIL nếu Khối 2 đưa ra kết luận kỹ thuật mà thiếu giải mã vi mô Warrant 1 hoặc phép thử tương quan độ lớn Warrant 2)

2. **Trạm 2: Geometry Collision & Cryptographic Sidecar Manifest**
   - Xác thực sự hiện diện và toàn vẹn của tệp ảnh: đọc bytes và so sánh `sha256(bytes) == asset.sha256_hash`.
   - Nạp file sidecar `[image_stem].manifest.json` và kiểm tra:
     * `envelope_clearance_percent >= 8.0%`
     * `min_font_size_pt >= 10.0 pt`
     * `zero_slash_fractions == "PASS"`
     * `canvas_width_inch <= 7.0 in`

3. **Trạm 3: Formal CAS SymPy Verification & Materials DB Audit**
   - Với các bước biến đổi trung gian có bản chất đại số giải tích (`DERIVATION_ALGEBRAIC`):
     * Gọi `SymPyCASEngine.verify_algebraic_identity(step_lhs, step_rhs)` hoặc xác thực chuỗi `verify_derivation_chain`.
     * Yêu cầu: `sp.simplify(diff) == 0`.
   - Đối soát thông số vật liệu 300 K qua `SemiconductorDatabase.MATERIALS_300K`:
     * Độ lệch tương đối $\le 1.0\%$.
   - Kiểm toán phần dư rỗng: `SymPyCASEngine.check_zero_omission_residual(source_entities, payload_text) == True`.

4. **Trạm 4: Typography DejaVu Preflight & Structural Layout**
   - Giải phẫu Kỹ Sư Trưởng: Bắt buộc có đủ Giải phẫu Động lực học & Tham số Vận hành và dịch ký hiệu thành thực thể sống. Khai trừ bảng Nomenclature 4 cột tĩnh.
   - Định dạng đơn vị SI: Khoảng trắng chuẩn giữa số và đơn vị (`300 K`, `1.424 eV`).
   - Cấu trúc Dòng chảy Nhận thức 3 Khối Mới: Khóa cứng Khối 1 (Khởi nguyên & Nỗi đau Công nghệ), Khối 2 (Mỏ neo Thị giác & Mô hình hóa), Khối 3 (Góc Nhìn Đối Trọng & Thử Thách Chẩn Đoán CER) theo UFME mới.
   - Mắt xích Chuyển tiếp: Có mặt đầy đủ câu hỏi gợi mở chuyển giao giữa Khối 1 $\to$ Khối 2 và Khối 2 $\to$ Khối 3.

5. **Trạm 5: ReportLab DocTemplate Compilation & Atomic Sandbox**
   - Sử dụng `BookmarkDocTemplate` và `NumberedBookmarkCanvas` từ `hust_pdf_engine.py`.
   - Lắp ráp luồng phần tử Flowables:
     * H1: Tên phân mục
     * H2: Từng Luận điểm vi mô (`Luận điểm X.Y.k`)
     * H3: Khối 1, Khối 2, Khối 3
     * Flowable `make_open_cer_box`: Khung Thử thách Chẩn đoán R&D Mở viền bo `#0072BD`, **CẤM TUYỆT ĐỐI IN LỜI GIẢI / ĐÁP ÁN TRONG PDF**; để trống khung cho người học suy nghĩ và tranh biện trực tiếp trên Chat.
   - Bọc `KeepTogether` cho từng bước dẫn xuất trung gian đơn lẻ và khung `make_open_cer_box`.
   - Dựng PDF tại `%TEMP%` trước (`%TEMP% Isolation Policy`).
   - Hậu kiểm nhị phân bằng PyMuPDF (`pymupdf.open()`):
     * Kiểm tra `len(doc) >= estimated_pages`
     * Kiểm tra cấu trúc bookmarks 3 cấp (`doc.get_toc()`)
     * Kiểm tra dung lượng tệp $\le 5.0\text{ MB}$
   - Thay thế nguyên tử `os.replace` vào đích xuất bản (cục bộ hoặc Google Drive `G:\`).
   - Quét dọn toàn bộ tệp tạm trong `%TEMP%`.
   - **Trạm 6: Xuất bản Hồ sơ Kiểm toán Word (.docx) & Đồng bộ Cloud ID**:
     * Tự động kích hoạt scripts.docx_audit_generator.py sau khi chuyên khảo PDF được xuất bản thành công.
     * Trích xuất tự động mã Cloud File ID từ SQLite DriveFS (metadata_sqlite_db) ở chế độ Read-Only (0 ms latency).
     * Khóa cứng cú pháp liên kết khớp 100% regex spark-visual-cockpit-v2.0.0/content.js (Link PDF Tab Phải và Link Ảnh Tab Trái).
     * Thay thế nguyên tử os.replace tệp Ho_So_Kiem_Toan_Chuong_[X]_[Ten_Hoc_Phan].docx lên cấp thư mục gốc trên Google Google Drive.

## II. Bảng Kiểm 18 Điểm Nhị Phân & Vòng Lặp Tự Sửa Lỗi Kỷ Luật Kỹ Thuật

### 1. Bảng 18 Tiêu chí Nhị phân (Pass/Fail Gate)
1. `GATE_01`: Elastic Depth & Zero-Omission Gate (Bao phủ 100% slide/giáo trình, Unbounded Depth)
2. `GATE_02`: Dòng chảy Nhận thức 3 Khối chuẩn mực (Khối 1 -> Khối 2 -> Khối 3)
3. `GATE_03`: Hình tượng hóa trực giác ARegistry (duy nhất 1 lần/MPT tại Khối 1)
4. `GATE_04`: Zero-Symbol-Drift (Khớp 100% ký hiệu trục, góc với OCR và Master Variable Dictionary)
5. `GATE_05`: Bố trí 5 Mắt xích OCR xuyên suốt 3 Khối
6. `GATE_06`: Quy ước Dấu Đại số & Hình học nhất quán
7. `GATE_07`: Quét biến thiên tiệm cận & Khảo sát đa biến
8. `GATE_08`: Dẫn xuất trung gian tường minh (Zero-Skipped-Steps, không phân số gạch chéo `/`)
9. `GATE_09`: Phương trình cột trụ & Bảng Giải phẫu Động lực học MALAE Cấp 3
10. `GATE_10`: Giải phẫu MALAE 3 Cấp độ hoàn chỉnh
11. `GATE_11`: Kỷ luật không chat tự do khi chạy /learn hoặc đóng gói
12. `GATE_12`: Clean-Slate Recompilation (Tái tạo toàn diện, không vá chắp vá)
13. `GATE_13`: Khung Open CER Box (Zero-Solution trong PDF)
14. `GATE_14`: Chế bản PDF ReportLab DejaVu & PyMuPDF (Bookmark 3 cấp, Trang X / Y)
15. `GATE_15`: Chuẩn hóa danh pháp song ngữ ATCC & SI
16. `GATE_16`: Quản trị tài nguyên Google Drive sạch sẽ, không sinh file rác ` (1).pdf`
17. `GATE_17`: Khóa cứng Sample Gate Pha 1 (Chờ người học duyệt trước khi Rollout Pha 2)
18. `GATE_18`: Thẩm vấn Bằng chứng Thực nghiệm TVD Engine (Sidecar manifest `*.tvd.json` & Regex caption)

### 2. Quy trình Tự Phản Tỉnh Theo Kỷ Luật Kỹ Thuật (@ENGINEERING_DISCIPLINE_WORKFLOW.md)
Mọi can thiệp sửa lỗi của Agent trong quá trình Self-Healing bắt buộc tuân thủ 3 Pha:
- **Pha 1 (Vá lỗi):** Bắt buộc viết script kiểm thử độc lập tái hiện lỗi (kết quả FAIL) trước khi chạm vào mã nguồn. Sửa mã tối thiểu (Atomic Fix) và xác nhận test chuyển sang PASS 100%. Cấm sửa mò (Zero-Shotgun-Debugging).
- **Pha 2 (Tái cấu trúc):** Khóa chặt Data Contract Invariant (chữ ký hàm, kiểu dữ liệu, schema Pydantic). Thực thi ghi đè nguyên tử an toàn qua `%TEMP%` và `os.replace`.
- **Pha 3 (Mở rộng):** Thiết kế Spec trước, đóng gói module hóa độc lập, viết acceptance test trước khi sinh code.
- **5 Tiêu chí tự đối soát trước phản hồi (Ponytail Checklist):**
  1. Đã có test độc lập chứng minh lỗi chưa?
  2. Data Contract có được bảo toàn 100% không?
  3. Module có bị viết monolithic dồn đống không?
  4. Test suite trên host OS đạt PASS 100% chưa?
  5. Văn phong có tuân thủ Ponytail Mode (gãy gọn, zero văn mẫu) không?

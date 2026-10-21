---
name: quality-gatekeeper
description: Động cơ thẩm định chất lượng nhị phân 17 điểm, kiểm chứng đại số hình thức SymPy CAS, kiểm toán mật mã SHA-256 sidecar manifest, chế bản chuyên khảo ReportLab DejaVu PDF và thay thế nguyên tử %TEMP% Isolation trên Google Antigravity.
---

# Quality Gatekeeper & Monograph Publisher Engine (Agent 4 Skill)

Kỹ năng điều phối kiểm định chất lượng toàn diện và chế bản chuyên khảo PDF cho hệ thống bài giảng & nghiên cứu Quang điện tử HUST.

## I. Quy Trình 5 Trạm Chốt Chặn Đầu Ra Xác Định (DOHG 2.0)

1. **Trạm 1: Static AST & Typography Linter**
   - Nạp `DraftPayload` và chạy qua `common.ASTLinter.lint_payload()`.
   - Kiểm tra 7 điều kiện cứng:
     1. `raw_latex_leaks_count == 0`
     2. `slash_fraction_count == 0`
     3. `raw_subscript_count == 0`
     4. `arrow_inline_count == 0`
     5. `raw_html_entity_count == 0`
     6. `merged_stages_count == 0`
     7. `old_blocks_count == 0`

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
   - Bảng Nomenclature: Kiểm tra đủ 4 trường `name_vi`, `symbol_html`, `standard_unit_si`, `physical_role`.
   - Định dạng đơn vị SI: Khoảng trắng chuẩn giữa số và đơn vị (`300 K`, `1.424 eV`).
   - Cấu trúc 5 Giai đoạn sư phạm lũy tiến: Khóa cứng `Giai đoạn 1:` đến `Giai đoạn 4:` trong từng MPT và `Giai đoạn 5:` ở cuối mục.

5. **Trạm 5: ReportLab DocTemplate Compilation & Atomic Sandbox**
   - Sử dụng `BookmarkDocTemplate` và `NumberedBookmarkCanvas` từ `hust_pdf_engine.py`.
   - Lắp ráp luồng phần tử Flowables:
     * H1: Tên phân mục
     * H2: Từng Luận điểm vi mô (`Luận điểm X.Y.k`)
     * H3: Giai đoạn 1..4
     * H2: Giai đoạn 5 (Thử thách CER)
   - Bọc `KeepTogether` cho từng bước dẫn xuất trung gian đơn lẻ (preserving document breathing room).
   - Dựng PDF tại `%TEMP%` trước (`%TEMP% Isolation Policy`).
   - Hậu kiểm nhị phân bằng PyMuPDF (`pymupdf.open()`):
     * Kiểm tra `len(doc) >= estimated_pages`
     * Kiểm tra cấu trúc bookmarks 3 cấp (`doc.get_toc()`)
     * Kiểm tra dung lượng tệp $\le 5.0\text{ MB}$
   - Thay thế nguyên tử `os.replace` vào đích xuất bản (cục bộ hoặc Google Drive `G:\`).
   - Quét dọn toàn bộ tệp tạm trong `%TEMP%`.

## II. Bảng Kiểm 17 Điểm Nhị Phân & Vòng Lặp Tự Sửa Lỗi (Self-Healing Loop)
- Đánh giá 17 tiêu chí nhị phân `GATE_1` đến `GATE_17`.
- Quản lý số lần thử tự sửa `attempt_count` (tối đa 5 lần).
- Xuất bản Hợp đồng Dữ liệu `AuditReport` (`AUDIT_REPORT.json`).

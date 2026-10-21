# -*- coding: utf-8 -*-
"""
scripts/dry_run_phase_4.py — Kịch bản Dry-run Kiểm định Độc lập Pha 4: Quality Gatekeeper (Agent 4)
Antigravity 2.0 - Standalone Autonomous Subagent Verification.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).

Kiểm chứng 7 miền kỹ thuật:
- Miền 1: Hợp đồng Pydantic AuditReport & Tính nghiêm ngặt extra="forbid" (Thuật toán 8)
- Miền 2: Trạm 1 Static AST & Typography Linter (Luật 14, 15, Zero-Raw-LaTeX, Zero-Slash-Fractions)
- Miền 3: Trạm 2 Cryptographic Sidecar Manifest & Triple Buffer Geometry (Thuật toán 7, 13)
- Miền 4: Trạm 3 Formal SymPy CAS Verification & Đối chuẩn Bán dẫn 300 K (Thuật toán 6, 8)
- Miền 5: Trạm 4 Typography DejaVu Preflight & Bảng Nomenclature 4 cột ISO 80000-2 (Thuật toán 10, 12)
- Miền 6: Trạm 5 Chế bản ReportLab DejaVu PDF, Canvas 2 lượt Trang X / Y & Bookmark 3 cấp (Thuật toán 9, 14)
- Miền 7: Bảng kiểm 17 Điểm Nhị phân (17/17 PASS), Thay thế Nguyên tử & Báo cáo Giám định Toàn diện
"""

import sys
import os
import json
import time

# Cấu hình UTF-8 cho Windows Terminal
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pymupdf
from agents.quality_gatekeeper.gatekeeper import QualityGatekeeper
from schemas.audit import AuditReport


def log_section(title: str):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def verify_domain_1_audit_contracts(gatekeeper: QualityGatekeeper):
    log_section("[MIỀN 1] HỢP ĐỒNG PYDANTIC AUDITREPORT & TÍNH NGHIÊM NGẶT EXTRA='FORBID'")
    print("[*] Kiểm tra tính toàn vẹn và khớp nối giữa các hợp đồng dữ liệu:")
    print(f"    - Blueprint Section ID: MUC_{gatekeeper.blueprint.chapter_index}_{gatekeeper.blueprint.section_index}")
    print(f"    - Manifest Section ID: {gatekeeper.manifest.section_id}")
    print(f"    - Draft Payload Section ID: {gatekeeper.draft_payload.section_id}")
    print(f"    - Tiêu đề phân mục: {gatekeeper.draft_payload.section_title}")
    print(f"    - Số lượng MPTs bóc tách: {len(gatekeeper.draft_payload.mpt_payloads)}")

    assert gatekeeper.manifest.section_id == gatekeeper.draft_payload.section_id, "[-] Bất đồng bộ section_id!"
    print("    [+] Hợp đồng dữ liệu đa tầng liên kết nhất quán: ĐẠT CHUẨN 100%.")


def verify_domain_2_station_1_linter(gatekeeper: QualityGatekeeper):
    log_section("[MIỀN 2] TRẠM 1: STATIC AST & TYPOGRAPHY PRE-FLIGHT LINTER (THUẬT TOÁN 8)")
    st1 = gatekeeper.run_dohg_station_1_linter()
    print(f"[*] Kết quả Trạm 1: {'PASS (100% Hợp quy)' if st1.passed else 'FAIL'}")
    print(f"    - Chi tiết: {st1.details}")

    assert st1.passed, f"[-] Trạm 1 Static Linter thất bại: {st1.details}"
    assert st1.error_traces is None, "[-] Trạm 1 có vết lỗi kỹ thuật!"
    print("    [+] Trạm 1 Static AST Linter: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_3_station_2_manifest_audit(gatekeeper: QualityGatekeeper):
    log_section("[MIỀN 3] TRẠM 2: GEOMETRY COLLISION & CRYPTOGRAPHIC MANIFEST (THUẬT TOÁN 7, 13)")
    st2 = gatekeeper.run_dohg_station_2_manifest_audit()
    print(f"[*] Kết quả Trạm 2: {'PASS (100% Hợp quy)' if st2.passed else 'FAIL'}")
    print(f"    - Chi tiết: {st2.details}")

    assert st2.passed, f"[-] Trạm 2 Manifest & Geometry Audit thất bại: {st2.details}"
    assert st2.error_traces is None, "[-] Trạm 2 có vết lỗi kỹ thuật!"
    print("    [+] Trạm 2 Sidecar Manifest & Triple Buffer Gate: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_4_station_3_sympy_cas(gatekeeper: QualityGatekeeper):
    log_section("[MIỀN 4] TRẠM 3: FORMAL CAS SYMPY & EPISTEMIC CALIBRATION (THUẬT TOÁN 6, 8)")
    st3 = gatekeeper.run_dohg_station_3_sympy_cas()
    print(f"[*] Kết quả Trạm 3: {'PASS (100% Hợp quy)' if st3.passed else 'FAIL'}")
    print(f"    - Chi tiết: {st3.details}")

    assert st3.passed, f"[-] Trạm 3 Formal CAS SymPy thất bại: {st3.details}"
    assert st3.error_traces is None, "[-] Trạm 3 có vết lỗi kỹ thuật!"
    print("    [+] Trạm 3 Formal CAS & Epistemic Calibration: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_5_station_4_typography_preflight(gatekeeper: QualityGatekeeper):
    log_section("[MIỀN 5] TRẠM 4: TYPOGRAPHY DEJAVU PREFLIGHT & NOMENCLATURE (THUẬT TOÁN 10, 12)")
    st4 = gatekeeper.run_dohg_station_4_typographic_preflight()
    print(f"[*] Kết quả Trạm 4: {'PASS (100% Hợp quy)' if st4.passed else 'FAIL'}")
    print(f"    - Chi tiết: {st4.details}")

    assert st4.passed, f"[-] Trạm 4 Typography Preflight thất bại: {st4.details}"
    assert st4.error_traces is None, "[-] Trạm 4 có vết lỗi kỹ thuật!"
    print("    [+] Trạm 4 Typography Preflight & ISO 80000-2 Table: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_6_station_5_pdf_compilation(report: AuditReport):
    log_section("[MIỀN 6] TRẠM 5: CHẾ BẢN REPORTLAB PDF, CANVASES & PYMUPDF (THUẬT TOÁN 9, 14)")
    st5 = report.dohg_2_0_results.station_5_reportlab_compilation
    pm = report.publication_metadata
    print(f"[*] Kết quả Trạm 5: {'PASS (100% Hợp quy)' if st5.passed else 'FAIL'}")
    print(f"    - Chi tiết: {st5.details}")
    print(f"[*] Thông tin xuất bản PDF:")
    print(f"    - Đường dẫn: {pm.final_drive_path}")
    print(f"    - Dung lượng: {pm.file_size_bytes / 1024:.2f} KB ({pm.file_size_bytes} bytes)")
    print(f"    - Mã băm SHA-256: {pm.sha256_checksum}")
    print(f"    - Canvas hai lượt: {pm.two_pass_total_pages}")
    print(f"    - Xác thực cây Bookmarks 3 cấp: {'ĐẠT CHUẨN' if pm.pdf_bookmarks_levels_verified else 'CHƯA ĐẠT'}")

    assert st5.passed, f"[-] Trạm 5 PDF Compilation thất bại: {st5.details}"
    assert pm is not None, "[-] PublicationMetadata bị rỗng!"
    assert pm.atomic_replace_success, "[-] Ghi đè nguyên tử thất bại!"

    # Mở tệp kiểm tra bằng PyMuPDF
    doc = pymupdf.open(pm.final_drive_path)
    total_pages = len(doc)
    toc = doc.get_toc()
    doc.close()

    print(f"[*] Kiểm toán nhị phân PyMuPDF:")
    print(f"    - Tổng số trang in: {total_pages} trang")
    print(f"    - Số lượng mục Bookmarks (TOC): {len(toc)} mục")
    for item in toc:
        indent = "    " * item[0]
        print(f"      {indent}↳ [Level {item[0]}] {item[1]} (Trang {item[2]})")

    assert total_pages >= 1, "[-] Số trang < 1!"
    assert len(toc) >= 3, "[-] Cây bookmark thiếu cấp độ!"
    print("    [+] Trạm 5 ReportLab DocTemplate & Two-Pass Canvas: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_7_binary_17_points_and_audit_report(report: AuditReport, report_path: str):
    log_section("[MIỀN 7] BẢNG KIỂM 17 ĐIỂM NHỊ PHÂN & HỢP ĐỒNG AUDIT_REPORT.JSON")
    b17 = report.binary_17_point_checklist
    print(f"[*] Điểm kiểm định chất lượng nhị phân: {b17.total_passed}/17 tiêu chí ĐẠT")
    for gate_key, passed in b17.checklist_status.items():
        print(f"    - [{'PASS' if passed else 'FAIL'}] {gate_key}")

    assert b17.total_passed == 17, f"[-] Chỉ đạt {b17.total_passed}/17 tiêu chí!"
    assert report.overall_verdict == "PASS_100_PERCENT", f"[-] Kết luận chung không phải PASS_100_PERCENT: {report.overall_verdict}"
    assert os.path.exists(report_path), f"[-] Không tìm thấy tệp kết xuất: {report_path}"

    # Kiểm tra Lossless Round-trip
    with open(report_path, "r", encoding="utf-8") as f:
        loaded_json = json.load(f)
    re_validated = AuditReport.model_validate(loaded_json)
    assert re_validated.section_id == report.section_id, "[-] Sai lệch section_id sau round-trip!"
    assert re_validated.overall_verdict == report.overall_verdict, "[-] Sai lệch verdict sau round-trip!"
    print("    [+] Lossless Round-trip Deserialization: ĐẠT CHUẨN 100%.")
    print("    [+] Bảng kiểm 17 điểm nhị phân & AuditReport: ĐẠT CHUẨN TUYỆT ĐỐI.")


def main():
    start_time = time.time()
    print("=" * 80)
    print("  KỊCH BẢN DRY-RUN KIỂM ĐỊNH ĐỘC LẬP PHA 4 (quality-gatekeeper)")
    print("  Hệ thống AI Agent Giảng dạy & Chuyên khảo Vật lý Bán dẫn HUST")
    print("  Phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội)")
    print("=" * 80)

    bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
    mf_path = os.path.join(PROJECT_ROOT, "output", "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json")
    draft_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")
    out_pdf_path = os.path.join(PROJECT_ROOT, "output", "pdf", "Chuyen_Khao_Laser_Diode_Muc_2_1_Phase4.pdf")
    out_report_path = os.path.join(PROJECT_ROOT, "output", "reports", "AUDIT_REPORT_MUC_2_1.json")

    print(f"[*] Nạp Blueprint: {bp_path}")
    print(f"[*] Nạp Manifest: {mf_path}")
    print(f"[*] Nạp Draft Payload: {draft_path}")

    gatekeeper = QualityGatekeeper()
    gatekeeper.load_inputs(bp_path, mf_path, draft_path)

    # Thực thi các miền kiểm chứng tiền biên dịch
    verify_domain_1_audit_contracts(gatekeeper)
    verify_domain_2_station_1_linter(gatekeeper)
    verify_domain_3_station_2_manifest_audit(gatekeeper)
    verify_domain_4_station_3_sympy_cas(gatekeeper)
    verify_domain_5_station_4_typography_preflight(gatekeeper)

    # Thực thi kiểm định toàn diện và chế bản PDF
    report = gatekeeper.execute_audit(
        output_pdf_path=out_pdf_path,
        output_report_path=out_report_path,
        max_attempts=5,
    )

    # Thực thi các miền kiểm chứng hậu biên dịch
    verify_domain_6_station_5_pdf_compilation(report)
    verify_domain_7_binary_17_points_and_audit_report(report, out_report_path)

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print("  TỔNG KẾT DRY-RUN PHA 4: TẤT CẢ 7 MIỀN KỸ THUẬT ĐẠT PASS 100%!")
    print(f"  Thời gian thực thi: {elapsed:.3f} giây | 0 ERRORS | 0 FAILURES")
    print(f"  Tệp PDF chuyên khảo: {out_pdf_path}")
    print(f"  Tệp Báo cáo kiểm định: {out_report_path}")
    print("=" * 80)


if __name__ == "__main__":
    main()

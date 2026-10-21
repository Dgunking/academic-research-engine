# -*- coding: utf-8 -*-
"""
agents/quality_gatekeeper/runner.py — CLI Runner Độc Lập Cho Quality Gatekeeper (Agent 4)
Antigravity 2.0 - Standalone CLI Execution.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).
"""

import os
import sys

# Cấu hình UTF-8 cho Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import argparse

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from agents.quality_gatekeeper.gatekeeper import QualityGatekeeper


def main():
    parser = argparse.ArgumentParser(
        description="Quality Gatekeeper CLI Runner — Kiểm định 17 điểm & Chế bản ReportLab PDF"
    )
    parser.add_argument(
        "--blueprint",
        type=str,
        default=os.path.join(PROJECT_ROOT, "output", "blueprints", "BLUEPRINT_MUC_2_1.json"),
        help="Đường dẫn tệp BLUEPRINT_MUC_X.Y.json",
    )
    parser.add_argument(
        "--manifest",
        type=str,
        default=os.path.join(PROJECT_ROOT, "output", "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json"),
        help="Đường dẫn tệp ASSET_MANIFEST_MUC_X.Y.json",
    )
    parser.add_argument(
        "--draft",
        "--payload",
        type=str,
        default=os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json"),
        help="Đường dẫn tệp DRAFT_PAYLOAD_MUC_X.Y.json",
    )
    parser.add_argument(
        "--output-pdf",
        type=str,
        default=os.path.join(PROJECT_ROOT, "output", "pdf", "Chuyen_Khao_Laser_Diode_Muc_2_1_Phase4.pdf"),
        help="Đường dẫn xuất tệp PDF chuyên khảo",
    )
    parser.add_argument(
        "--output-report",
        type=str,
        default=os.path.join(PROJECT_ROOT, "output", "reports", "AUDIT_REPORT_MUC_2_1.json"),
        help="Đường dẫn xuất tệp báo cáo AUDIT_REPORT.json",
    )
    parser.add_argument(
        "--drive-dir",
        type=str,
        default=None,
        help="Thư mục xuất bản đồng bộ trên Google Drive G:\\",
    )

    args = parser.parse_args()

    print("=" * 80)
    print("  QUALITY GATEKEEPER (AGENT 4) — STANDALONE CLI RUNNER")
    print("  Hệ thống AI Agent Giảng dạy & Chuyên khảo Vật lý Bán dẫn HUST")
    print("=" * 80)

    # Fallback to DRY_RUN files if standard files don't exist
    bp_path = args.blueprint
    if not os.path.exists(bp_path):
        dry_bp = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        if os.path.exists(dry_bp):
            bp_path = dry_bp

    mf_path = args.manifest
    if not os.path.exists(mf_path):
        dry_mf = os.path.join(PROJECT_ROOT, "output", "manifests", "DRY_RUN_ASSET_MANIFEST_2_1.json")
        if os.path.exists(dry_mf):
            mf_path = dry_mf

    draft_path = args.draft
    if not os.path.exists(draft_path):
        dry_draft = os.path.join(PROJECT_ROOT, "output", "payloads", "DRY_RUN_DRAFT_PAYLOAD_2_1.json")
        if os.path.exists(dry_draft):
            draft_path = dry_draft

    print(f"[*] Nạp Blueprint: {bp_path}")
    print(f"[*] Nạp Manifest: {mf_path}")
    print(f"[*] Nạp Draft Payload: {draft_path}")

    gatekeeper = QualityGatekeeper()
    gatekeeper.load_inputs(bp_path, mf_path, draft_path)

    report = gatekeeper.execute_audit(
        output_pdf_path=args.output_pdf,
        output_report_path=args.output_report,
        drive_destination_path=args.drive_dir,
    )

    print("\n" + "=" * 80)
    print("  KẾT QUẢ KIỂM ĐỊNH CHẤT LƯỢNG (AUDIT REPORT)")
    print("=" * 80)
    print(f"Phân mục: {report.section_id}")
    print(f"Kết luận chung (Overall Verdict): {report.overall_verdict}")
    print(f"Số lần thử nghiệm tự sửa: {report.self_healing_attempt_count}")
    print(f"Điểm kiểm tra 17 điểm: {report.binary_17_point_checklist.total_passed}/17 tiêu chí ĐẠT")
    print("\nTrạng thái 5 Trạm Chốt Chặn DOHG 2.0:")
    for st_field in ["station_1_static_linter", "station_2_boundary_re3_audit", "station_3_sympy_cas_verification", "station_4_typographic_preflight", "station_5_reportlab_compilation"]:
        st = getattr(report.dohg_2_0_results, st_field)
        status_txt = "PASS" if st.passed else "FAIL"
        print(f"  - [{status_txt}] {st.station_name}")
        if not st.passed and st.error_traces:
            for err in st.error_traces[:3]:
                print(f"      ↳ {err}")

    if report.publication_metadata:
        pm = report.publication_metadata
        print(f"\nThông tin xuất bản PDF:")
        print(f"  - Tệp đích: {pm.final_drive_path}")
        print(f"  - Dung lượng: {pm.file_size_bytes / 1024:.2f} KB")
        print(f"  - Mã băm SHA-256: {pm.sha256_checksum[:16]}...")
        print(f"  - Định dạng số trang: {pm.two_pass_total_pages}")
        print(f"  - Thay thế nguyên tử: {'THÀNH CÔNG' if pm.atomic_replace_success else 'THẤT BẠI'}")

    print("=" * 80)

    if report.overall_verdict == "PASS_100_PERCENT":
        print("[+] KIỂM ĐỊNH THÀNH CÔNG: ĐẠT PASS 100%.")
        sys.exit(0)
    else:
        print("[-] KIỂM ĐỊNH THẤT BẠI: HỦY XUẤT BẢN.")
        sys.exit(1)


if __name__ == "__main__":
    main()

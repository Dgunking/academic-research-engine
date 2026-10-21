# -*- coding: utf-8 -*-
"""
CLI Runner for Central Orchestration Kernel (Agent 5 - FSM & E2E Pipeline)
Giao diện dòng lệnh khởi chạy và điều phối tự động toàn diện:
python -m agents.orchestration_kernel.runner --chapter 2 --section MUC_2_1 --mode sample
"""

import os
import sys
import argparse
import json

# Đảm bảo mã hóa UTF-8 trên Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from agents.orchestration_kernel.kernel import (
    OrchestrationKernel,
    OrchestratorConfig,
    RunMode,
    SectionExecutionResult,
)
from agents.orchestration_kernel.fsm import FSMState
from agents.schemas.blueprint import CurriculumBlueprint
from agents.schemas.manifest import VisualAssetManifest
from agents.schemas.payload import DraftPayload


def parse_args():
    parser = argparse.ArgumentParser(
        description="Central Orchestration Kernel (Agent 5) - FSM & E2E Pipeline Controller"
    )
    parser.add_argument(
        "--course-name",
        type=str,
        default="Quang điện tử & Laser Diode",
        help="Tên học phần giảng dạy",
    )
    parser.add_argument(
        "--chapter",
        type=int,
        default=2,
        help="Số thứ tự chương cần quét (ví dụ: 2)",
    )
    parser.add_argument(
        "--section",
        type=str,
        default="MUC_2_1",
        help="Mã phân mục (ví dụ: MUC_2_1)",
    )
    parser.add_argument(
        "--title",
        type=str,
        default="Vật lý Bán dẫn & Laser Diode",
        help="Tiêu đề phân mục",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["sample", "rollout", "single"],
        default="sample",
        help="Chế độ vận hành (sample: dừng tại X.1; rollout: cuốn chiếu tự động; single: chạy 1 mục)",
    )
    parser.add_argument(
        "--approve-sample",
        action="store_true",
        help="Cờ phê duyệt phân mục mẫu X.1 của người học để mở cổng Pha 2 cuốn chiếu",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Chạy kịch bản kiểm thử giả lập hoặc sử dụng dữ liệu đối chuẩn sẵn có",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Thư mục xuất xưởng cục bộ",
    )
    parser.add_argument(
        "--drive-dir",
        type=str,
        default=None,
        help="Đường dẫn thư mục lưu trữ trên Google Drive G:\\",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=5,
        help="Ngưỡng tự sửa lỗi tối đa (mặc định 5 chu kỳ)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    mode_map = {
        "sample": RunMode.SAMPLE_GATE,
        "rollout": RunMode.AUTONOMOUS_ROLLOUT,
        "single": RunMode.SINGLE_SECTION,
    }
    run_mode = mode_map[args.mode]

    # Phân tích số thứ tự mục từ chuỗi MUC_X_Y
    sec_idx = 1
    parts = args.section.replace("MUC_", "").split("_")
    if len(parts) >= 2:
        try:
            sec_idx = int(parts[1])
        except ValueError:
            sec_idx = 1

    print("=" * 80)
    print("  BỘ TỔNG CHỈ HUY ĐIỀU PHỐI FSM TRUNG TÂM (ORCHESTRATION KERNEL)")
    print("  Hệ thống AI Agent Giảng dạy & Chuyên khảo Vật lý Bán dẫn HUST")
    print("  Chủ nhiệm Dự án: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội)")
    print("=" * 80)
    print(f"[*] Học phần   : {args.course_name}")
    print(f"[*] Chương     : Chương {args.chapter}")
    print(f"[*] Phân mục   : {args.section} - {args.title}")
    print(f"[*] Chế độ     : {run_mode.value}")
    print(f"[*] Phê duyệt  : {args.approve_sample}")
    print(f"[*] Thư mục ra : {args.output_dir}")
    print(f"[*] Google Drive: {args.drive_dir or 'Không kết nối (lưu trữ cục bộ)'}")
    print("-" * 80)

    config = OrchestratorConfig(
        course_name=args.course_name,
        chapter_index=args.chapter,
        output_dir=args.output_dir,
        drive_destination_dir=args.drive_dir,
        max_retries=args.max_retries,
    )

    kernel = OrchestrationKernel(config=config)

    # Nạp dữ liệu đối chuẩn sẵn có nếu chạy dry-run
    pre_blueprint = None
    pre_manifest = None
    pre_draft = None

    if args.dry_run:
        bp_path = os.path.join(args.output_dir, "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        mf_path = os.path.join(args.output_dir, "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json")
        dp_path = os.path.join(args.output_dir, "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")

        if os.path.exists(bp_path):
            with open(bp_path, "r", encoding="utf-8") as f:
                pre_blueprint = CurriculumBlueprint.model_validate_json(f.read())
            print(f"[+] Dry-Run: Đã nạp Blueprint đối chuẩn: {bp_path}")

        if os.path.exists(mf_path):
            with open(mf_path, "r", encoding="utf-8") as f:
                pre_manifest = VisualAssetManifest.model_validate_json(f.read())
            print(f"[+] Dry-Run: Đã nạp Asset Manifest đối chuẩn: {mf_path}")

        if os.path.exists(dp_path):
            with open(dp_path, "r", encoding="utf-8") as f:
                pre_draft = DraftPayload.model_validate_json(f.read())
            print(f"[+] Dry-Run: Đã nạp Draft Payload đối chuẩn: {dp_path}")

    # Thực thi quy trình cho phân mục
    result = kernel.run_section_pipeline(
        section_id=args.section,
        section_index=sec_idx,
        section_title=args.title,
        run_mode=run_mode,
        approved_sample=args.approve_sample,
        preloaded_blueprint=pre_blueprint,
        preloaded_manifest=pre_manifest,
        preloaded_draft=pre_draft,
    )

    print("\n" + "=" * 80)
    print("  KẾT QUẢ ĐIỀU PHỐI ORCHESTRATION KERNEL")
    print("=" * 80)
    print(f"[*] Phân mục       : {result.section_id}")
    print(f"[*] Trạng thái FSM : {result.final_state.value}")
    print(f"[*] Số lần lặp     : {result.attempt_count}")
    print(f"[*] Tệp PDF        : {result.pdf_path}")
    print(f"[*] Báo cáo Audit  : {result.report_path}")

    # Hiển thị Bộ ba Mỏ neo Điều hướng (~2s)
    if result.navigation_anchors:
        print("\n" + "-" * 80)
        print("  BỘ BA MỎ NEO ĐIỀU HƯỚNG (NAVIGATION ANCHORS)")
        print("-" * 80)
        print(result.navigation_anchors["anchor_1_concept"])
        print(result.navigation_anchors["anchor_2_equation"])
        print(result.navigation_anchors["anchor_3_deliverable"])
        print("-" * 80)

    # Đánh giá mã thoát hệ thống
    if result.status == "SUCCESS":
        print("\n[+] ĐIỀU PHỐI HOÀN TẤT: PASS 100% (Thoát mã 0)")
        sys.exit(0)
    elif result.status == "SAMPLE_GATE_WAIT":
        print("\n[!] DỪNG TẠI SAMPLE GATE PHA 1: Chờ Bùi Trung Dũng duyệt chất lượng (Thoát mã 2)")
        sys.exit(2)
    else:
        print(f"\n[x] THẤT BẠI: {result.status} (Thoát mã 1)")
        for trace in result.error_traces:
            print(f"    ↳ {trace}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Kịch bản Dry-Run Nghiệm Thu Độc Lập Pha 5: Central Orchestration Kernel & E2E Pipeline
Chủ nhiệm Đề tài & Duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội)

Kiểm toán thực chứng 6 Miền Kỹ thuật:
1. Máy trạng thái hữu hạn FSM & Ma trận chuyển dịch hợp lệ (Thuật toán 11).
2. Động cơ Tự phản tỉnh sửa lỗi Lai ghép Hybrid Self-Healing (1-3 Local, 4-5 Clean-Slate, >5 Fail-Safe).
3. Rào cản Phê duyệt Phân mục Mẫu Sample Gate Mục X.1 (Luật 10 & 16).
4. Thực thi chuỗi End-to-End toàn diện nối kết 4 Subagents từ đầu (Agent 1 -> 2 -> 3 -> 4).
5. Giao thức Quản trị Drive %TEMP% Isolation & Atomic Replace (Thuật toán 9).
6. Giao diện Dòng lệnh CLI Runner & Mã thoát hệ thống (Exit code 0, 1, 2).
"""

import sys
import os
import json
import time
import subprocess
import tempfile
import shutil

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

from agents.orchestration_kernel.fsm import FSMMachine, FSMState
from agents.orchestration_kernel.self_healing import (
    HybridSelfHealingEngine,
    HealingStrategy,
    TargetSubagent,
)
from agents.orchestration_kernel.kernel import (
    OrchestrationKernel,
    OrchestratorConfig,
    RunMode,
    atomic_replace,
)
from agents.schemas.blueprint import CurriculumBlueprint
from agents.schemas.manifest import VisualAssetManifest
from agents.schemas.payload import DraftPayload
from agents.schemas.audit import (
    AuditReport,
    DOHGStationsResult,
    StationResult,
    BinarySeventeenPointResult,
)


def log_section(title: str):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def verify_domain_1_fsm():
    log_section("[MIỀN 1] MÁY TRẠNG THÁI HỮU HẠN FSM & MA TRẬN CHUYỂN DỊCH (THUẬT TOÁN 11)")
    fsm = FSMMachine(initial_state=FSMState.IDLE)
    print(f"[*] Trạng thái khởi đầu: {fsm.current_state.value}")
    assert fsm.current_state == FSMState.IDLE

    # Kiểm tra chuỗi chuyển dịch đơn vị
    transitions = [
        (FSMState.EXTRACTING_BLUEPRINT, "Agent 1 trích xuất Blueprint"),
        (FSMState.GENERATING_ASSETS, "Agent 2 vẽ đồ thị"),
        (FSMState.AUTHORING_DRAFT, "Agent 3 soạn thảo bài giảng"),
        (FSMState.AUDITING_QUALITY, "Agent 4 kiểm toán 5 trạm"),
        (FSMState.COMPLETED, "Hoàn tất chuyên khảo"),
    ]

    for next_state, reason in transitions:
        assert fsm.can_transition(next_state)
        fsm.transition_to(next_state, reason)
        print(f"    ↳ Chuyển dịch hợp lệ: {fsm.current_state.value} ({reason})")

    # Kiểm tra bắt chặn chuyển dịch phi pháp
    fsm.reset_to_idle("Reset về IDLE để kiểm tra rào cản")
    assert not fsm.can_transition(FSMState.SAMPLE_GATE_WAIT)
    try:
        fsm.transition_to(FSMState.SAMPLE_GATE_WAIT, "Cố tình nhảy cóc")
        raise AssertionError("FSM không bắt được lỗi chuyển dịch bất hợp lệ!")
    except ValueError as e:
        print(f"[*] Kiểm thử bắt chặn rẽ nhánh trái phép: PASS -> '{str(e)[:70]}...'")

    print("[+] Miền 1 FSM Controller: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_2_hybrid_self_healing():
    log_section("[MIỀN 2] ĐỘNG CƠ TỰ SỬA LỖI LAI GHÉP HYBRID SELF-HEALING (VÒNG 1-5)")

    def make_mock_report(failed_station: int):
        stations = {
            "station_1_static_linter": StationResult(station_name="S1", passed=True, details="OK", error_traces=[]),
            "station_2_boundary_re3_audit": StationResult(station_name="S2", passed=True, details="OK", error_traces=[]),
            "station_3_sympy_cas_verification": StationResult(station_name="S3", passed=True, details="OK", error_traces=[]),
            "station_4_typographic_preflight": StationResult(station_name="S4", passed=True, details="OK", error_traces=[]),
            "station_5_reportlab_compilation": StationResult(station_name="S5", passed=True, details="OK", error_traces=[]),
        }
        if failed_station == 2:
            stations["station_2_boundary_re3_audit"] = StationResult(
                station_name="S2", passed=False, details="Envelope fail", error_traces=["Envelope < 8%"]
            )
        elif failed_station == 3:
            stations["station_3_sympy_cas_verification"] = StationResult(
                station_name="S3", passed=False, details="CAS fail", error_traces=["simplify != 0"]
            )

        checklist = {f"GATE_{i:02d}": True for i in range(1, 18)}
        return AuditReport(
            section_id="MUC_2_1",
            audit_timestamp="2026-10-21T00:00:00",
            overall_verdict="FAIL_RETRY_REQUIRED",
            self_healing_attempt_count=1,
            dohg_2_0_results=DOHGStationsResult(**stations),
            binary_17_point_checklist=BinarySeventeenPointResult(total_passed=16, checklist_status=checklist),
        )

    # 1. Vòng 1-3: Vi phẫu Trạm 2 -> Agent 2
    rep_s2 = make_mock_report(failed_station=2)
    strat_2, dir_2 = HybridSelfHealingEngine.analyze_audit_report(rep_s2, current_attempt=1)
    print(f"[*] Vòng 1 (Lỗi Trạm 2): Chiến lược = {strat_2.value} | Đích = {[s.value for s in dir_2.target_subagents]}")
    assert strat_2 == HealingStrategy.LOCAL_DISPATCH
    assert TargetSubagent.PHYSICS_GRAPHIC_ARTIST in dir_2.target_subagents

    # 2. Vòng 1-3: Vi phẫu Trạm 3 -> Agent 3
    rep_s3 = make_mock_report(failed_station=3)
    strat_3, dir_3 = HybridSelfHealingEngine.analyze_audit_report(rep_s3, current_attempt=2)
    print(f"[*] Vòng 2 (Lỗi Trạm 3): Chiến lược = {strat_3.value} | Đích = {[s.value for s in dir_3.target_subagents]}")
    assert strat_3 == HealingStrategy.LOCAL_DISPATCH
    assert TargetSubagent.PEDAGOGICAL_AUTHOR in dir_3.target_subagents

    # 3. Vòng 4-5: Clean-Slate Re-rollout
    strat_4, dir_4 = HybridSelfHealingEngine.analyze_audit_report(rep_s3, current_attempt=4)
    print(f"[*] Vòng 4 (Tái phát lỗi): Chiến lược = {strat_4.value} | Đích = {[s.value for s in dir_4.target_subagents]}")
    assert strat_4 == HealingStrategy.CLEAN_SLATE_RESET
    assert TargetSubagent.ALL in dir_4.target_subagents

    # 4. Vòng > 5: Fail-Safe Halt
    strat_6, dir_6 = HybridSelfHealingEngine.analyze_audit_report(rep_s3, current_attempt=6)
    print(f"[*] Vòng 6 (Vượt quá 5 chu kỳ): Chiến lược = {strat_6.value} -> CRITICAL_FAIL_SAFE")
    assert strat_6 == HealingStrategy.FAIL_SAFE_HALT

    print("[+] Miền 2 Hybrid Self-Healing Engine: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_3_sample_gate(temp_dir: str):
    log_section("[MIỀN 3] RÀO CẢN PHÊ DUYỆT PHÂN MỤC MẪU SAMPLE GATE (LUẬT 10 & 16)")
    config = OrchestratorConfig(course_name="Quang điện tử", chapter_index=2, output_dir=temp_dir)
    kernel = OrchestrationKernel(config=config)

    # Nạp các file đối chuẩn sẵn có để kiểm tra Sample Gate Barrier
    bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
    mf_path = os.path.join(PROJECT_ROOT, "output", "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json")
    dp_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")

    with open(bp_path, "r", encoding="utf-8") as f:
        bp = CurriculumBlueprint.model_validate_json(f.read())
    with open(mf_path, "r", encoding="utf-8") as f:
        mf = VisualAssetManifest.model_validate_json(f.read())
    with open(dp_path, "r", encoding="utf-8") as f:
        dp = DraftPayload.model_validate_json(f.read())

    # 1. Chạy khi chưa duyệt -> Phải dừng tại SAMPLE_GATE_WAIT
    res_wait = kernel.run_section_pipeline(
        section_id="MUC_2_1",
        section_index=1,
        section_title="Vật lý Bán dẫn & Laser Diode",
        run_mode=RunMode.SAMPLE_GATE,
        approved_sample=False,
        preloaded_blueprint=bp,
        preloaded_manifest=mf,
        preloaded_draft=dp,
    )
    print(f"[*] Kiểm thử Sample Gate chưa duyệt: Status = {res_wait.status} | FSM = {res_wait.final_state.value}")
    assert res_wait.status == "SAMPLE_GATE_WAIT"
    assert res_wait.final_state == FSMState.SAMPLE_GATE_WAIT

    print("[*] Hiển thị Bộ ba Mỏ neo Điều hướng (~2s) xuất ra Chat:")
    print(f"    {res_wait.navigation_anchors['anchor_1_concept']}")
    print(f"    {res_wait.navigation_anchors['anchor_2_equation']}")
    print(f"    {res_wait.navigation_anchors['anchor_3_deliverable']}")

    # 2. Chạy khi Bùi Trung Dũng đã duyệt -> Mở cổng COMPLETED
    res_ok = kernel.run_section_pipeline(
        section_id="MUC_2_1",
        section_index=1,
        section_title="Vật lý Bán dẫn & Laser Diode",
        run_mode=RunMode.SAMPLE_GATE,
        approved_sample=True,
        preloaded_blueprint=bp,
        preloaded_manifest=mf,
        preloaded_draft=dp,
    )
    print(f"[*] Kiểm thử Sample Gate đã duyệt: Status = {res_ok.status} | FSM = {res_ok.final_state.value}")
    assert res_ok.status == "SUCCESS"
    assert res_ok.final_state == FSMState.COMPLETED

    print("[+] Miền 3 Sample Gate Protocol: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_4_e2e_scratch(temp_dir: str):
    log_section("[MIỀN 4] THỰC THI END-TO-END CHUỖI 4 SUBAGENTS TỪ ĐẦU (ZERO TO HERO)")
    config = OrchestratorConfig(course_name="Quang học & Quang điện tử", chapter_index=2, output_dir=temp_dir)
    kernel = OrchestrationKernel(config=config)

    start_time = time.time()
    result = kernel.run_section_pipeline(
        section_id="MUC_2_1",
        section_index=1,
        section_title="Vật lý Bán dẫn & Laser Diode",
        run_mode=RunMode.SAMPLE_GATE,
        approved_sample=True,  # Duyệt hoàn tất để kiểm chứng xuất bản toàn chuỗi
    )
    duration = time.time() - start_time

    print(f"[*] Thời gian thực thi toàn chuỗi: {duration:.3f} giây")
    print(f"[*] Trạng thái hoàn thành       : {result.status} (FSM: {result.final_state.value})")
    print(f"[*] Blueprint sinh ra          : {result.blueprint_path} ({os.path.exists(result.blueprint_path)})")
    print(f"[*] Asset Manifest sinh ra     : {result.manifest_path} ({os.path.exists(result.manifest_path)})")
    print(f"[*] Draft Payload sinh ra      : {result.payload_path} ({os.path.exists(result.payload_path)})")
    print(f"[*] Audit Report sinh ra       : {result.report_path} ({os.path.exists(result.report_path)})")
    print(f"[*] Chuyên khảo PDF xuất bản   : {result.pdf_path} ({os.path.exists(result.pdf_path)})")

    assert result.status == "SUCCESS"
    assert os.path.exists(result.pdf_path)
    assert os.path.getsize(result.pdf_path) > 0

    print("[+] Miền 4 End-to-End Autonomous Pipeline: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_5_atomic_replace(temp_dir: str):
    log_section("[MIỀN 5] GIAO THỨC %TEMP% ISOLATION & ATOMIC REPLACE (THUẬT TOÁN 9)")
    src = os.path.join(temp_dir, "temp_render.pdf")
    dst = os.path.join(temp_dir, "final_deliverable.pdf")

    with open(src, "w", encoding="utf-8") as f:
        f.write("New PDF binary stream")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("Old existing file")

    atomic_replace(src, dst)
    with open(dst, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[*] Thay thế nguyên tử tệp đích thành công: nội dung = '{content}'")
    assert content == "New PDF binary stream"
    print("[+] Miền 5 Atomic Replace & Drive Safety: ĐẠT CHUẨN TUYỆT ĐỐI.")


def verify_domain_6_cli_runner(temp_dir: str):
    log_section("[MIỀN 6] GIAO DIỆN DÒNG LỆNH CLI RUNNER & MÃ THOÁT HỆ THỐNG")

    # 1. Chế độ sample chưa duyệt -> mã thoát 2
    cmd_sample = [
        sys.executable, "-m", "agents.orchestration_kernel.runner",
        "--chapter", "2",
        "--section", "MUC_2_1",
        "--mode", "sample",
        "--dry-run",
        "--output-dir", temp_dir,
    ]
    res_sample = subprocess.run(
        cmd_sample, capture_output=True, encoding="utf-8", errors="replace", cwd=PROJECT_ROOT
    )
    print(f"[*] CLI Runner (chưa duyệt) mã thoát: {res_sample.returncode} (Kỳ vọng: 2) -> PASS")
    assert res_sample.returncode == 2

    # 2. Chế độ sample đã duyệt -> mã thoát 0
    cmd_approve = [
        sys.executable, "-m", "agents.orchestration_kernel.runner",
        "--chapter", "2",
        "--section", "MUC_2_1",
        "--mode", "sample",
        "--approve-sample",
        "--dry-run",
        "--output-dir", temp_dir,
    ]
    res_approve = subprocess.run(
        cmd_approve, capture_output=True, encoding="utf-8", errors="replace", cwd=PROJECT_ROOT
    )
    print(f"[*] CLI Runner (đã duyệt) mã thoát  : {res_approve.returncode} (Kỳ vọng: 0) -> PASS")
    assert res_approve.returncode == 0

    print("[+] Miền 6 CLI Runner & Exit Codes: ĐẠT CHUẨN TUYỆT ĐỐI.")


def main():
    print("=" * 80)
    print("  KỊCH BẢN DRY-RUN KIỂM ĐỊNH ĐỘC LẬP PHA 5 (orchestration-kernel)")
    print("  Hệ thống AI Agent Giảng dạy & Chuyên khảo Vật lý Bán dẫn HUST")
    print("  Phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội)")
    print("=" * 80)

    temp_dir = tempfile.mkdtemp(prefix="dry_run_phase5_")
    t0 = time.time()
    try:
        verify_domain_1_fsm()
        verify_domain_2_hybrid_self_healing()
        verify_domain_3_sample_gate(temp_dir)
        verify_domain_4_e2e_scratch(temp_dir)
        verify_domain_5_atomic_replace(temp_dir)
        verify_domain_6_cli_runner(temp_dir)

        elapsed = time.time() - t0
        print("\n" + "=" * 80)
        print(f"  TỔNG KẾT DRY-RUN PHA 5: TẤT CẢ 6 MIỀN KỸ THUẬT ĐẠT PASS 100%!")
        print(f"  Thời gian thực thi: {elapsed:.3f} giây | 0 ERRORS | 0 FAILURES")
        print("  Central Orchestration Kernel & E2E Pipeline hoàn tất tích hợp thành công!")
        print("=" * 80)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()

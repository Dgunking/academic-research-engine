# -*- coding: utf-8 -*-
"""
Test Suite for Phase 5: Central Orchestration Kernel & E2E Pipeline
Kiểm thử toàn diện:
1. Máy trạng thái hữu hạn FSM (chuyển dịch hợp lệ, bắt chặn bất hợp lệ)
2. Động cơ Tự phản tỉnh sửa lỗi Lai ghép Hybrid Self-Healing (1-3 Local, 4-5 Clean-Slate, >5 Fail-Safe)
3. Rào cản Phê duyệt Phân mục Mẫu Sample Gate (Mục X.1)
4. Bộ ba Mỏ neo Điều hướng Navigation Anchors (~2s)
5. Giao thức Quản trị Drive %TEMP% Isolation & Atomic Replace
6. Thực thi chuỗi End-to-End toàn diện nối kết 4 Subagents
"""

import unittest
import os
import sys
import tempfile
import shutil

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from agents.orchestration_kernel.fsm import FSMMachine, FSMState, FSMTransition
from agents.orchestration_kernel.self_healing import (
    HybridSelfHealingEngine,
    HealingStrategy,
    TargetSubagent,
    HealingDirective,
)
from agents.orchestration_kernel.kernel import (
    OrchestrationKernel,
    OrchestratorConfig,
    RunMode,
    SectionExecutionResult,
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
    PublicationMetadata,
)


class TestPhase5OrchestrationKernel(unittest.TestCase):
    """Bộ kiểm thử đơn vị & tích hợp cho Central Orchestration Kernel (Agent 5)."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="agy_test_phase5_")
        self.config = OrchestratorConfig(
            course_name="Quang học & Quang điện tử",
            chapter_index=2,
            output_dir=self.test_dir,
            max_retries=5,
        )
        self.kernel = OrchestrationKernel(config=self.config)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir, ignore_errors=True)

    # -----------------------------------------------------------------------
    # TEST NHÓM 1: MÁY TRẠNG THÁI HỮU HẠN FSM
    # -----------------------------------------------------------------------
    def test_01_fsm_initialization_and_valid_transitions(self):
        """Kiểm tra khởi tạo FSM và chuỗi chuyển dịch trạng thái tuần tự hợp lệ."""
        fsm = FSMMachine(initial_state=FSMState.IDLE)
        self.assertEqual(fsm.current_state, FSMState.IDLE)

        # IDLE -> EXTRACTING_BLUEPRINT
        self.assertTrue(fsm.can_transition(FSMState.EXTRACTING_BLUEPRINT))
        fsm.transition_to(FSMState.EXTRACTING_BLUEPRINT, "Bắt đầu trích xuất Blueprint")
        self.assertEqual(fsm.current_state, FSMState.EXTRACTING_BLUEPRINT)

        # EXTRACTING_BLUEPRINT -> GENERATING_ASSETS
        self.assertTrue(fsm.can_transition(FSMState.GENERATING_ASSETS))
        fsm.transition_to(FSMState.GENERATING_ASSETS, "Sinh tài sản hình ảnh")
        self.assertEqual(fsm.current_state, FSMState.GENERATING_ASSETS)

        # GENERATING_ASSETS -> AUTHORING_DRAFT
        self.assertTrue(fsm.can_transition(FSMState.AUTHORING_DRAFT))
        fsm.transition_to(FSMState.AUTHORING_DRAFT, "Soạn thảo bản thảo 5 giai đoạn")
        self.assertEqual(fsm.current_state, FSMState.AUTHORING_DRAFT)

        # AUTHORING_DRAFT -> AUDITING_QUALITY
        self.assertTrue(fsm.can_transition(FSMState.AUDITING_QUALITY))
        fsm.transition_to(FSMState.AUDITING_QUALITY, "Kiểm toán 5 trạm DOHG 2.0")
        self.assertEqual(fsm.current_state, FSMState.AUDITING_QUALITY)

        # AUDITING_QUALITY -> COMPLETED
        self.assertTrue(fsm.can_transition(FSMState.COMPLETED))
        fsm.transition_to(FSMState.COMPLETED, "Hoàn tất xuất bản")
        self.assertEqual(fsm.current_state, FSMState.COMPLETED)

        # Kiểm tra nhật ký vết
        history = fsm.history
        self.assertGreaterEqual(len(history), 6)
        self.assertEqual(history[-1].to_state, FSMState.COMPLETED)

    def test_02_fsm_invalid_transition_raises_error(self):
        """Bắt chặn và ném ValueError khi chuyển dịch trạng thái bất hợp lệ."""
        fsm = FSMMachine(initial_state=FSMState.IDLE)
        # IDLE không thể nhảy cóc sang SAMPLE_GATE_WAIT, COMPLETED hoặc FAIL_SAFE_HALTED
        self.assertFalse(fsm.can_transition(FSMState.SAMPLE_GATE_WAIT))
        self.assertFalse(fsm.can_transition(FSMState.COMPLETED))
        self.assertFalse(fsm.can_transition(FSMState.FAIL_SAFE_HALTED))

        with self.assertRaises(ValueError) as ctx:
            fsm.transition_to(FSMState.COMPLETED, "Cố tình nhảy cóc")
        self.assertIn("LỖI CHUYỂN DỊCH FSM BẤT HỢP LỆ", str(ctx.exception))

    # -----------------------------------------------------------------------
    # TEST NHÓM 2: ĐỘNG CƠ TỰ SỬA LỖI LAI GHÉP HYBRID SELF-HEALING
    # -----------------------------------------------------------------------
    def _create_mock_audit_report(self, overall_verdict: str, failed_station_idx: int = 0):
        """Hàm trợ giúp tạo mock AuditReport."""
        stations = {
            "station_1_static_linter": StationResult(station_name="Station 1", passed=True, details="OK", error_traces=[]),
            "station_2_boundary_re3_audit": StationResult(station_name="Station 2", passed=True, details="OK", error_traces=[]),
            "station_3_sympy_cas_verification": StationResult(station_name="Station 3", passed=True, details="OK", error_traces=[]),
            "station_4_typographic_preflight": StationResult(station_name="Station 4", passed=True, details="OK", error_traces=[]),
            "station_5_reportlab_compilation": StationResult(station_name="Station 5", passed=True, details="OK", error_traces=[]),
        }

        if failed_station_idx == 1:
            stations["station_1_static_linter"] = StationResult(station_name="Station 1", passed=False, details="Linter fail", error_traces=["Raw LaTeX detected"])
        elif failed_station_idx == 2:
            stations["station_2_boundary_re3_audit"] = StationResult(station_name="Station 2", passed=False, details="Envelope fail", error_traces=["Triple buffer envelope < 8%"])
        elif failed_station_idx == 3:
            stations["station_3_sympy_cas_verification"] = StationResult(station_name="Station 3", passed=False, details="CAS fail", error_traces=["simplify != 0"])
        elif failed_station_idx == 4:
            stations["station_4_typographic_preflight"] = StationResult(station_name="Station 4", passed=False, details="Table fail", error_traces=["Table not 4 cols"])

        checklist = {
            "GATE_01_elastic_depth_zero_omission": True,
            "GATE_02_five_stage_pedagogy": True,
            "GATE_03_three_beat_analogy_aregistry": True,
            "GATE_04_zero_symbol_drift": True,
            "GATE_05_five_link_ocr_caption": True,
            "GATE_06_algebraic_geometric_sign": True,
            "GATE_07_asymptotic_sweeps_boundary": True,
            "GATE_08_causal_flowchain_explicit_derivation": True,
            "GATE_09_pillar_equation_nomenclature": True,
            "GATE_10_parallel_operation_modes": True,
            "GATE_11_zero_text_chat_rule": True,
            "GATE_12_clean_slate_edit": True,
            "GATE_13_matlab_hdse_triple_buffer": True,
            "GATE_14_pdf_preflight_compliance": True,
            "GATE_15_atcc_scientific_nomenclature": True,
            "GATE_16_temp_isolation_atomic_replace": True,
            "GATE_17_sample_gate_protocol": True,
        }

        return AuditReport(
            section_id="MUC_2_1",
            audit_timestamp="2026-10-21T00:00:00",
            overall_verdict=overall_verdict,
            self_healing_attempt_count=1,
            dohg_2_0_results=DOHGStationsResult(**stations),
            binary_17_point_checklist=BinarySeventeenPointResult(
                total_passed=17,
                checklist_status=checklist,
            ),
        )

    def test_03_hybrid_self_healing_pass_verdict(self):
        """Khi AuditReport đạt PASS 100%, không kích hoạt sửa lỗi."""
        report = self._create_mock_audit_report("PASS_100_PERCENT")
        strategy, directive = HybridSelfHealingEngine.analyze_audit_report(report, current_attempt=1)
        self.assertEqual(strategy, HealingStrategy.NONE)
        self.assertIsNone(directive)

    def test_04_hybrid_self_healing_local_dispatch_station_2(self):
        """Vòng 1-3: Khi Trạm 2 thất bại, phân luồng vi phẫu cục bộ tới Agent 2 (physics_graphic_artist)."""
        report = self._create_mock_audit_report("FAIL_RETRY_REQUIRED", failed_station_idx=2)
        strategy, directive = HybridSelfHealingEngine.analyze_audit_report(report, current_attempt=2)

        self.assertEqual(strategy, HealingStrategy.LOCAL_DISPATCH)
        self.assertIsNotNone(directive)
        self.assertIn(TargetSubagent.PHYSICS_GRAPHIC_ARTIST, directive.target_subagents)
        self.assertNotIn(TargetSubagent.PEDAGOGICAL_AUTHOR, directive.target_subagents)
        self.assertIn(2, directive.failed_stations)

    def test_05_hybrid_self_healing_local_dispatch_station_1_3_4(self):
        """Vòng 1-3: Khi Trạm 1/3/4 thất bại, phân luồng vi phẫu cục bộ tới Agent 3 (pedagogical_author)."""
        report = self._create_mock_audit_report("FAIL_RETRY_REQUIRED", failed_station_idx=3)
        strategy, directive = HybridSelfHealingEngine.analyze_audit_report(report, current_attempt=1)

        self.assertEqual(strategy, HealingStrategy.LOCAL_DISPATCH)
        self.assertIsNotNone(directive)
        self.assertIn(TargetSubagent.PEDAGOGICAL_AUTHOR, directive.target_subagents)
        self.assertNotIn(TargetSubagent.PHYSICS_GRAPHIC_ARTIST, directive.target_subagents)
        self.assertIn(3, directive.failed_stations)

    def test_06_hybrid_self_healing_clean_slate_attempts_4_5(self):
        """Vòng 4-5: Tự động chuyển chiến lược sang Clean-Slate Re-rollout toàn phần."""
        report = self._create_mock_audit_report("FAIL_RETRY_REQUIRED", failed_station_idx=1)
        strategy, directive = HybridSelfHealingEngine.analyze_audit_report(report, current_attempt=4)

        self.assertEqual(strategy, HealingStrategy.CLEAN_SLATE_RESET)
        self.assertIsNotNone(directive)
        self.assertIn(TargetSubagent.ALL, directive.target_subagents)
        self.assertIn("CLEAN-SLATE RE-ROLLOUT", directive.corrective_instructions)

    def test_07_hybrid_self_healing_fail_safe_halt_attempt_exceeded(self):
        """Vượt quá 5 lần thử: Kích hoạt chốt dừng an toàn CRITICAL_FAIL_SAFE."""
        report = self._create_mock_audit_report("FAIL_RETRY_REQUIRED", failed_station_idx=1)
        strategy, directive = HybridSelfHealingEngine.analyze_audit_report(report, current_attempt=6)

        self.assertEqual(strategy, HealingStrategy.FAIL_SAFE_HALT)
        self.assertIsNotNone(directive)
        self.assertIn("CRITICAL_FAIL_SAFE", directive.corrective_instructions)

    # -----------------------------------------------------------------------
    # TEST NHÓM 3: RÀO CẢN PHÊ DUYỆT PHÂN MỤC MẪU SAMPLE GATE (LUẬT 10 & 16)
    # -----------------------------------------------------------------------
    def test_08_sample_gate_barrier_locks_at_section_1(self):
        """Mục X.1 chạy ở chế độ SAMPLE_GATE khi chưa duyệt bắt buộc dừng tại SAMPLE_GATE_WAIT."""
        # Nạp các file đối chuẩn sẵn có từ thư mục output
        bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        mf_path = os.path.join(PROJECT_ROOT, "output", "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json")
        dp_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")

        if not (os.path.exists(bp_path) and os.path.exists(mf_path) and os.path.exists(dp_path)):
            self.skipTest("Thiếu file đối chuẩn để chạy thử nghiệm Sample Gate.")

        with open(bp_path, "r", encoding="utf-8") as f:
            bp = CurriculumBlueprint.model_validate_json(f.read())
        with open(mf_path, "r", encoding="utf-8") as f:
            mf = VisualAssetManifest.model_validate_json(f.read())
        with open(dp_path, "r", encoding="utf-8") as f:
            dp = DraftPayload.model_validate_json(f.read())

        result = self.kernel.run_section_pipeline(
            section_id="MUC_2_1",
            section_index=1,
            section_title="Vật lý Bán dẫn & Laser Diode",
            run_mode=RunMode.SAMPLE_GATE,
            approved_sample=False,  # Chưa phê duyệt
            preloaded_blueprint=bp,
            preloaded_manifest=mf,
            preloaded_draft=dp,
        )

        self.assertEqual(result.status, "SAMPLE_GATE_WAIT")
        self.assertEqual(result.final_state, FSMState.SAMPLE_GATE_WAIT)
        self.assertIsNotNone(result.navigation_anchors)
        self.assertIn("anchor_1_concept", result.navigation_anchors)
        self.assertIn("anchor_2_equation", result.navigation_anchors)
        self.assertIn("anchor_3_deliverable", result.navigation_anchors)

    def test_09_sample_gate_approval_opens_completion(self):
        """Khi Bùi Trung Dũng phê duyệt (approved_sample=True), phân mục mẫu X.1 hoàn tất COMPLETED."""
        bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        mf_path = os.path.join(PROJECT_ROOT, "output", "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json")
        dp_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")

        if not (os.path.exists(bp_path) and os.path.exists(mf_path) and os.path.exists(dp_path)):
            self.skipTest("Thiếu file đối chuẩn để chạy thử nghiệm Sample Gate Approval.")

        with open(bp_path, "r", encoding="utf-8") as f:
            bp = CurriculumBlueprint.model_validate_json(f.read())
        with open(mf_path, "r", encoding="utf-8") as f:
            mf = VisualAssetManifest.model_validate_json(f.read())
        with open(dp_path, "r", encoding="utf-8") as f:
            dp = DraftPayload.model_validate_json(f.read())

        result = self.kernel.run_section_pipeline(
            section_id="MUC_2_1",
            section_index=1,
            section_title="Vật lý Bán dẫn & Laser Diode",
            run_mode=RunMode.SAMPLE_GATE,
            approved_sample=True,  # ĐÃ PHÊ DUYỆT
            preloaded_blueprint=bp,
            preloaded_manifest=mf,
            preloaded_draft=dp,
        )

        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.final_state, FSMState.COMPLETED)
        self.assertTrue(os.path.exists(result.pdf_path))

    # -----------------------------------------------------------------------
    # TEST NHÓM 4: GIAO THỨC QUẢN TRỊ DRIVE %TEMP% VÀ ATOMIC REPLACE
    # -----------------------------------------------------------------------
    def test_10_atomic_replace_drive_safety(self):
        """Kiểm tra thay thế nguyên tử tệp nguồn sang tệp đích an toàn."""
        src_file = os.path.join(self.test_dir, "source.pdf")
        dst_file = os.path.join(self.test_dir, "destination.pdf")

        with open(src_file, "w", encoding="utf-8") as f:
            f.write("Initial Source Content")
        with open(dst_file, "w", encoding="utf-8") as f:
            f.write("Old Destination Content")

        atomic_replace(src_file, dst_file)

        self.assertTrue(os.path.exists(dst_file))
        with open(dst_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "Initial Source Content")

    def test_11_navigation_anchors_formatting(self):
        """Kiểm tra định dạng của Bộ ba Mỏ neo Điều hướng (~2s) xuất ra chat."""
        bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        dp_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")
        rep_path = os.path.join(PROJECT_ROOT, "output", "reports", "AUDIT_REPORT_MUC_2_1.json")

        if not (os.path.exists(bp_path) and os.path.exists(dp_path) and os.path.exists(rep_path)):
            self.skipTest("Thiếu dữ liệu để test format navigation anchors.")

        with open(bp_path, "r", encoding="utf-8") as f:
            bp = CurriculumBlueprint.model_validate_json(f.read())
        with open(dp_path, "r", encoding="utf-8") as f:
            dp = DraftPayload.model_validate_json(f.read())
        with open(rep_path, "r", encoding="utf-8") as f:
            rep = AuditReport.model_validate_json(f.read())

        anchors = self.kernel.format_navigation_anchors(
            bp, dp, "output/pdf/test.pdf", rep
        )

        self.assertIn("Mỏ neo 1", anchors["anchor_1_concept"])
        self.assertIn("Mỏ neo 2", anchors["anchor_2_equation"])
        self.assertIn("Mỏ neo 3", anchors["anchor_3_deliverable"])

    def test_12_full_e2e_pipeline_execution_from_scratch(self):
        """Thực thi toàn chuỗi 4 Subagent từ đầu (không dùng preloaded) đạt COMPLETED."""
        result = self.kernel.run_section_pipeline(
            section_id="MUC_2_1",
            section_index=1,
            section_title="Vật lý Bán dẫn & Laser Diode",
            run_mode=RunMode.SAMPLE_GATE,
            approved_sample=True,
        )

        self.assertEqual(result.status, "SUCCESS")
        self.assertEqual(result.final_state, FSMState.COMPLETED)
        self.assertTrue(os.path.exists(result.pdf_path))
        self.assertTrue(os.path.exists(result.report_path))
        self.assertTrue(os.path.exists(result.blueprint_path))
        self.assertTrue(os.path.exists(result.manifest_path))
        self.assertTrue(os.path.exists(result.payload_path))

    def test_13_runner_cli_dry_run_sample_gate(self):
        """Kiểm tra CLI Runner ở chế độ dry-run sample gate."""
        import subprocess

        cmd = [
            sys.executable,
            "-m",
            "agents.orchestration_kernel.runner",
            "--chapter",
            "2",
            "--section",
            "MUC_2_1",
            "--mode",
            "sample",
            "--dry-run",
            "--output-dir",
            self.test_dir,
        ]
        res = subprocess.run(
            cmd, capture_output=True, encoding="utf-8", errors="replace", cwd=PROJECT_ROOT
        )
        # Chế độ sample chưa approve trả về mã 2 (SAMPLE_GATE_WAIT)
        self.assertEqual(res.returncode, 2)
        self.assertIn("DỪNG TẠI SAMPLE GATE PHA 1", res.stdout)

    def test_14_runner_cli_dry_run_approved_sample(self):
        """Kiểm tra CLI Runner ở chế độ dry-run sample gate đã phê duyệt."""
        import subprocess

        cmd = [
            sys.executable,
            "-m",
            "agents.orchestration_kernel.runner",
            "--chapter",
            "2",
            "--section",
            "MUC_2_1",
            "--mode",
            "sample",
            "--approve-sample",
            "--dry-run",
            "--output-dir",
            self.test_dir,
        ]
        res = subprocess.run(
            cmd, capture_output=True, encoding="utf-8", errors="replace", cwd=PROJECT_ROOT
        )
        # Chế độ sample đã approve trả về mã 0 (SUCCESS)
        self.assertEqual(res.returncode, 0)
        self.assertIn("PASS 100%", res.stdout)


if __name__ == "__main__":
    unittest.main()

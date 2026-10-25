# -*- coding: utf-8 -*-
"""
Test Suite for Phase 2 Refactoring & Toulmin 4-Beat Causal Pipeline
Xác minh:
1. Lược đồ Pydantic mới ToulminFourBeatPipeline, ToulminFourBeatSpec.
2. Mở rộng MechanisticBlendingEquation với 4 trường:
   - visual_evidence (Nhịp 1 - Data)
   - micro_dynamics_warrant (Nhịp 2 - Warrant 1)
   - math_blending_scaling (Nhịp 3 - Warrant 2)
   - engineering_claim (Nhịp 4 - Claim)
3. Bảo toàn 100% tương thích ngược với payload cũ.
4. Logic kiểm toán ASTLinter.check_unwarranted_claims (Zero-Unwarranted Claims Gate).
"""

import unittest
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AGENTS_DIR = os.path.join(PROJECT_ROOT, ".agents")
for p in [AGENTS_DIR, PROJECT_ROOT]:
    if p not in sys.path:
        sys.path.insert(0, p)

from schemas.payload import (
    ToulminFourBeatPipeline,
    MechanisticBlendingEquation,
    TeleologySpatialContext,
    BoundaryAuditEngineeringSchema,
    MicroPointTopicPayload,
    DraftPayload,
    InternalASTLinterReport,
)
from schemas.blueprint import (
    ToulminFourBeatSpec,
    MicroPointTopicSpec,
)
from common.linter import ASTLinter


class TestToulminFourBeatPipeline(unittest.TestCase):
    """Bộ kiểm thử cho Chuỗi Suy Luận Nhân Quả 4 Nhịp Toulmin."""

    def test_01_schema_instantiation_full_four_beats(self):
        """Khởi tạo thành công đối tượng 4 Nhịp Toulmin."""
        pipeline = ToulminFourBeatPipeline(
            beat_1_visual_evidence="Điểm uốn Ith = 22.5 mA trên đồ thị L-I tại 300 K.",
            beat_2_micro_dynamics_warrant="Hiện tượng ghim mật độ hạt tải (Carrier Density Pinning) khi đạt ngưỡng.",
            beat_3_math_blending_scaling="Hệ thức Ith = q*V*Nth/tau; phép thử độ lớn cho thấy Ith tỷ lệ nghịch với thời gian sống tau.",
            beat_4_engineering_claim="Quyết định thiết kế R&D: Giảm thể tích tích cực V để hạ dòng ngưỡng."
        )
        self.assertIn("22.5 mA", pipeline.beat_1_visual_evidence)
        self.assertIn("Carrier Density Pinning", pipeline.beat_2_micro_dynamics_warrant)
        self.assertIn("Ith = q*V*Nth/tau", pipeline.beat_3_math_blending_scaling)
        self.assertIn("R&D", pipeline.beat_4_engineering_claim)

    def test_02_mechanistic_blending_equation_fields(self):
        """MechanisticBlendingEquation chứa đủ 4 trường và tương thích ngược."""
        block_2 = MechanisticBlendingEquation(
            first_principles_origin="Từ phương trình liên tục hạt tải và phương trình Poisson.",
            visual_evidence="Điểm gãy Ith = 22.5 mA.",
            micro_dynamics_warrant="Đảo mật độ quần thể và bão hòa độ lợi.",
            math_blending_scaling="Công thức Ith = q*V*Nth/tau; scaling ratio cho thấy giảm V 50% giảm Ith 50%.",
            engineering_claim="Giảm chiều rộng stripe xuống 2 um để hạ dòng ngưỡng hoạt động.",
            cognitive_handover_to_block_3="Khi vận hành ở nhiệt độ cao, rủi ro trôi nhiệt là gì?"
        )
        self.assertEqual(block_2.visual_evidence, "Điểm gãy Ith = 22.5 mA.")
        self.assertIn("Đảo mật độ", block_2.micro_dynamics_warrant)
        self.assertIn("scaling ratio", block_2.math_blending_scaling)
        self.assertIn("stripe", block_2.engineering_claim)
        self.assertIn("trôi nhiệt", block_2.cognitive_handover_to_block_3)

    def test_03_backward_compatibility_empty_beats(self):
        """Dữ liệu cũ thiếu 4 trường mới vẫn khởi tạo bình thường mà không báo lỗi."""
        legacy_block_2 = MechanisticBlendingEquation(
            first_principles_origin="Định luật bảo toàn điện tích.",
            causal_flowchain=["A -> B", "B -> C"],
        )
        self.assertIsNone(legacy_block_2.visual_evidence)
        self.assertIsNone(legacy_block_2.micro_dynamics_warrant)
        self.assertIsNone(legacy_block_2.math_blending_scaling)
        self.assertIsNone(legacy_block_2.engineering_claim)
        self.assertEqual(len(legacy_block_2.causal_flowchain), 2)

    def test_04_blueprint_spec_four_beats(self):
        """MicroPointTopicSpec trong Blueprint hỗ trợ ToulminFourBeatSpec."""
        spec_pipeline = ToulminFourBeatSpec(
            visual_evidence="Trích xuất Ith = 25 mA từ đồ thị L-I.",
            micro_dynamics_warrant="Cơ chế ghim mật độ hạt tải.",
            math_blending_scaling="Thử độ lớn tỷ số tau_rec.",
            engineering_claim="Tối ưu hốc cộng hưởng Fabry-Perot."
        )
        mpt_spec = MicroPointTopicSpec(
            mpt_id="MPT_2_1_1",
            title="Dòng ngưỡng Laser Diode",
            core_proposition="Dòng ngưỡng xác định thời điểm khuếch đại kích thích thắng tổn hao.",
            four_beat_pipeline=spec_pipeline
        )
        self.assertIsNotNone(mpt_spec.four_beat_pipeline)
        self.assertEqual(mpt_spec.four_beat_pipeline.visual_evidence, "Trích xuất Ith = 25 mA từ đồ thị L-I.")

    def test_05_linter_zero_unwarranted_claims_negative(self):
        """Linter bắt lỗi nhảy cóc từ Data sang Claim mà thiếu Warrant 1 hoặc Warrant 2."""
        incomplete_dict = {
            "visual_evidence": "Đồ thị L-I có điểm uốn tại 20 mA.",
            "engineering_claim": "Kết luận thiết kế linh kiện phải phủ gương 95%.",
            # Thiếu micro_dynamics_warrant và math_blending_scaling
        }
        findings = ASTLinter.check_unwarranted_claims(incomplete_dict)
        self.assertGreater(len(findings), 0)
        self.assertTrue(any("Warrant 1" in f for f in findings))
        self.assertTrue(any("Warrant 2" in f for f in findings))

    def test_06_linter_zero_unwarranted_claims_positive(self):
        """Linter PASS khi Khối 2 có đầy đủ 4 thành phần hợp lý."""
        complete_dict = {
            "visual_evidence": "Đồ thị L-I có điểm uốn tại 20 mA.",
            "micro_dynamics_warrant": "Cơ chế đảo mật độ quần thể vượt ngưỡng tổn hao buồng cộng hưởng.",
            "math_blending_scaling": "Hệ thức g_th = alpha_i + (1/2L)ln(1/R1R2), scaling cho thấy tăng L giảm g_th.",
            "engineering_claim": "Kết luận thiết kế linh kiện kéo dài hốc L = 500 um để hạ dòng ngưỡng."
        }
        findings = ASTLinter.check_unwarranted_claims(complete_dict)
        self.assertEqual(len(findings), 0)

    def test_07_author_build_mpt_payload_populates_four_beats(self):
        """UFMEEngine.build_mpt_payload tự động khởi tạo đủ 4 Nhịp Toulmin."""
        from agents.pedagogical_author.author import UFMEEngine
        spec = MicroPointTopicSpec(
            mpt_id="MPT_TEST_1",
            title="Kiểm thử 4 Nhịp Toulmin",
            core_proposition="Năng lượng photon tỷ lệ thuận với tần số dao động.",
            target_equations=["E = h \\cdot \\nu"]
        )
        payload = UFMEEngine.build_mpt_payload(spec, material_name="GaAs")
        mbe = payload.mechanistic_blending_equation
        self.assertIsNotNone(mbe.visual_evidence)
        self.assertIsNotNone(mbe.micro_dynamics_warrant)
        self.assertIsNotNone(mbe.math_blending_scaling)
        self.assertIsNotNone(mbe.engineering_claim)
        self.assertIsNotNone(mbe.four_beat_pipeline)
        self.assertEqual(mbe.four_beat_pipeline.beat_1_visual_evidence, mbe.visual_evidence)

    def test_08_gatekeeper_station_1_catches_unwarranted_claims(self):
        """QualityGatekeeper Trạm 1 đánh FAIL khi có unwarranted claim trong DraftPayload."""
        from agents.quality_gatekeeper.gatekeeper import QualityGatekeeper
        from agents.pedagogical_author.author import UFMEEngine

        spec = MicroPointTopicSpec(
            mpt_id="MPT_TEST_2",
            title="Kiểm thử Gatekeeper Station 1",
            core_proposition="Dòng ngưỡng phụ thuộc vào nhiệt độ.",
            target_equations=["I_{th}(T) = I_0 \\cdot e^{T / T_0}"]
        )
        valid_mpt = UFMEEngine.build_mpt_payload(spec, material_name="GaAs")

        linter_rep = InternalASTLinterReport(
            passed=True,
            raw_latex_leaks_count=0,
            slash_fraction_count=0,
            raw_subscript_count=0,
            unwarranted_claims_count=0
        )

        # 1. DraftPayload hợp lệ -> Station 1 PASS
        valid_payload = DraftPayload(
            section_id="MUC_TEST",
            section_title="Mục Kiểm Thử Hợp Lệ",
            cod_rounds_completed=3,
            linter_pre_check=linter_rep,
            mpt_payloads=[valid_mpt]
        )
        gk = QualityGatekeeper()
        gk.draft_payload = valid_payload
        res_pass = gk.run_dohg_station_1_linter()
        self.assertTrue(res_pass.passed, f"Expected PASS but got: {res_pass.details} {res_pass.error_traces}")

        # 2. Xóa Warrant 1 và Warrant 2 -> Station 1 FAIL
        broken_mbe = valid_mpt.mechanistic_blending_equation.model_copy(update={
            "micro_dynamics_warrant": None,
            "math_blending_scaling": None,
            "engineering_claim": "Khẳng định kỹ thuật mồ côi không có cơ sở."
        })
        broken_mpt = valid_mpt.model_copy(update={"mechanistic_blending_equation": broken_mbe})
        invalid_payload = DraftPayload(
            section_id="MUC_TEST_INVALID",
            section_title="Mục Kiểm Thử Vi Phạm",
            cod_rounds_completed=3,
            linter_pre_check=linter_rep,
            mpt_payloads=[broken_mpt]
        )
        gk.draft_payload = invalid_payload
        res_fail = gk.run_dohg_station_1_linter()
        self.assertFalse(res_fail.passed)
        self.assertTrue(any("Warrant 1" in e for e in res_fail.error_traces))
        self.assertTrue(any("Warrant 2" in e for e in res_fail.error_traces))


if __name__ == "__main__":
    unittest.main()

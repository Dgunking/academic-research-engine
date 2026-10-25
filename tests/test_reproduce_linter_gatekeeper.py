# -*- coding: utf-8 -*-
"""
Test tái hiện độc lập lỗi lệch giao diện Linter <-> Gatekeeper (Bước 1.1 / 2.1).
Hiện tượng: ASTLinter phát hiện vi phạm Typography mới (raw chemicals, band variables, nested tags)
nhưng Gatekeeper Station 1 không gom vào all_errors, dẫn đến thông báo vô lý 'FAIL: Phát hiện 0 vi phạm'
và đánh rớt trạm kiểm định.
"""

import os
import sys
import unittest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AGENTS_DIR = os.path.join(PROJECT_ROOT, ".agents")
for p in [PROJECT_ROOT, AGENTS_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

from schemas.payload import (
    DraftPayload,
    MicroPointTopicPayload,
    InternalASTLinterReport,
    TeleologySpatialContext,
    MechanisticBlendingEquation,
    BoundaryAuditEngineeringSchema,
)
from common.linter import ASTLinter
from agents.quality_gatekeeper.gatekeeper import QualityGatekeeper


class TestReproduceLinterGatekeeperMismatch(unittest.TestCase):
    def test_raw_chemicals_or_band_variables_error_trace_not_empty_on_failure(self):
        """Nếu Station 1 FAIL do vi phạm typography mới, error_traces không được rỗng và details không được ghi '0 vi phạm'."""
        gatekeeper = QualityGatekeeper()
        
        # Tạo payload chứa biến dải năng lượng thô Eg và hóa chất thô TiO2 trong plain_english_axiom
        mpt_payload = MicroPointTopicPayload(
            mpt_id="MPT_TEST",
            mpt_title="Tiêu đề thử nghiệm",
            teleology_and_spatial_context=TeleologySpatialContext(
                systemic_teleology_sbf="Thử nghiệm linh kiện quang điện tử",
                plain_english_axiom="Chất xúc tác TiO2 có độ rộng dải cấm Eg = 3.2 eV", # dính TiO2 và Eg thô
                spatial_topology_anchor="TiO2",
            ),
            mechanistic_blending_equation=MechanisticBlendingEquation(
                visual_evidence="Dải năng lượng",
                micro_dynamics_warrant="Tương tác hạt tải",
                math_blending_scaling="Bề rộng vùng cấm Eg = 1.424 eV", # dính biến Eg thô
                engineering_claim="Tần số phát xạ ổn định",
                guided_derivations=[],
            ),
            boundary_audit_and_engineering_schema=BoundaryAuditEngineeringSchema(
                adversarial_boundary_audit="Nhiệt độ 300 K",
                engineering_heuristic_schema="Quy tắc thực nghiệm",
                student_challenge_cer={},
            ),
        )
        
        draft = DraftPayload(
            section_id="MUC_TEST",
            section_title="Phân mục thử nghiệm",
            cod_rounds_completed=3,
            mpt_payloads=[mpt_payload],
            linter_pre_check=InternalASTLinterReport(
                passed=False,
                raw_latex_leaks_count=0,
                slash_fraction_count=0,
                raw_subscript_count=0,
                unwarranted_claims_count=0,
            ),
        )
        
        gatekeeper.draft_payload = draft
        res = gatekeeper.run_dohg_station_1_linter()
        
        # Nếu passed == False, thì error_traces bắt buộc không được None/rỗng và details không được chứa '0 vi phạm'
        if not res.passed:
            self.assertIsNotNone(res.error_traces, "Lỗi: error_traces là None khi passed == False!")
            self.assertGreater(len(res.error_traces), 0, "Lỗi: error_traces rỗng dù trạm báo FAIL!")
            self.assertNotIn("Phát hiện 0 vi phạm", res.details, "Lỗi: details thông báo 'Phát hiện 0 vi phạm' vô lý!")


if __name__ == "__main__":
    unittest.main()

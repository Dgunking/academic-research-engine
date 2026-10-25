# -*- coding: utf-8 -*-
"""
tests/test_phase_3.py — Bộ Kiểm Thử Đơn Vị Toàn Diện Cho Pha 3 (Agent 3 - pedagogical-author)
Chủ thể phê duyệt: Lead Researcher ().

Bao gồm 18 bài kiểm tra bao phủ 5 miền kỹ thuật:
- Kiểm tra hợp đồng Pydantic DraftPayload (ràng buộc extra="forbid", CoD >= 3)
- Kiểm tra động cơ UFME 5 Giai đoạn & MALAE 3 Cấp độ
- Kiểm tra giới hạn trần <= 65 từ của Causal Flowchain
- Kiểm tra tiền tố bắt buộc ↳ và luật Zero-Skipped-Steps
- Kiểm tra Trạm 1 AST Linter (Zero-Slash-Fractions, Zero-Raw-LaTeX, Zero-ASCII-Subscripts)
- Kiểm tra ma trận bao phủ 5 Mắt xích OCR (Zero-Omission)
- Kiểm tra CLI Runner độc lập
"""

import os
import sys
import json
import unittest
import subprocess

# Cấu hình UTF-8 cho Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pydantic
import agents
from agents.pedagogical_author.author import (
    PedagogicalAuthor,
    UFMEEngine,
    MALAEEngine,
    CausalFlowchainCompiler,
    sanitize_text_for_typography,
)
from schemas.blueprint import CurriculumBlueprint, MicroPointTopicSpec, VisualRequirement
from schemas.manifest import VisualAssetManifest, VisualAssetItem, OCRChainPedagogicalCaption
from schemas.payload import (
    DraftPayload,
    MicroPointTopicPayload,
    EquationDissectionMALAE,
    IntermediateDerivationStep,
    InternalASTLinterReport,
)
from common.linter import ASTLinter


class TestPhase3PedagogicalAuthor(unittest.TestCase):
    """Bộ kiểm thử đơn vị cho Agent 3 (pedagogical-author)."""

    @classmethod
    def setUpClass(cls):
        cls.bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        cls.mf_path = os.path.join(PROJECT_ROOT, "output", "manifests", "DRY_RUN_ASSET_MANIFEST_2_1.json")
        with open(cls.bp_path, "r", encoding="utf-8") as f:
            cls.blueprint = CurriculumBlueprint.model_validate(json.load(f))
        with open(cls.mf_path, "r", encoding="utf-8") as f:
            cls.manifest = VisualAssetManifest.model_validate(json.load(f))

    def setUp(self):
        self.author = PedagogicalAuthor(blueprint=self.blueprint, manifest=self.manifest)

    # -------------------------------------------------------------------------
    # 1. KIỂM THỬ HỢP ĐỒNG PYDANTIC (DRAFT PAYLOAD SCHEMAS)
    # -------------------------------------------------------------------------
    def test_01_schema_valid_draft_payload(self):
        """Xác thực đối tượng DraftPayload hợp lệ có thể serialize/deserialize hai chiều."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        self.assertIsInstance(payload, DraftPayload)
        self.assertEqual(payload.section_id, "MUC_2_1")
        self.assertGreaterEqual(payload.cod_rounds_completed, 3)

        # Roundtrip JSON
        json_str = payload.model_dump_json()
        reloaded = DraftPayload.model_validate_json(json_str)
        self.assertEqual(reloaded.section_id, payload.section_id)
        self.assertEqual(len(reloaded.mpt_payloads), len(payload.mpt_payloads))

    def test_02_schema_forbids_extra_fields(self):
        """Khóa cứng schema: Thuộc tính ngoài danh mục bị chặn bởi extra='forbid'."""
        dissection = EquationDissectionMALAE(
            pillar_equation_latex=r"E(k) = E_c + \frac{\hbar^2 \cdot k^2}{2 \cdot m^*_e}",
            level_1_overview="Tổng quan",
            level_2_nomenclature_html_table=[{"symbol_html": "<i>k</i>", "name_vi": "Vector sóng"}],
            level_3_asymptotic_and_symmetry="Tiệm cận k = 0"
        )
        step = IntermediateDerivationStep(
            step_index=1,
            explanation_vi="↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi",
            step_equation_latex=r"\frac{dE}{dk} = 0"
        )
        linter_rep = InternalASTLinterReport(
            passed=True,
            raw_latex_leaks_count=0,
            slash_fraction_count=0,
            raw_subscript_count=0
        )

        with self.assertRaises(pydantic.ValidationError):
            DraftPayload(
                section_id="MUC_2_1",
                section_title="Vật lý Bán dẫn",
                cod_rounds_completed=3,
                mpt_payloads=[],
                linter_pre_check=linter_rep,
                extra_unknown_field="Forbidden"  # Extra field
            )

    def test_03_cod_rounds_minimum_constraint(self):
        """Khóa cứng CoD: Số vòng nén Chain-of-Density bắt buộc >= 3."""
        linter_rep = InternalASTLinterReport(
            passed=True,
            raw_latex_leaks_count=0,
            slash_fraction_count=0,
            raw_subscript_count=0
        )
        with self.assertRaises(pydantic.ValidationError):
            DraftPayload(
                section_id="MUC_2_1",
                section_title="Tiêu đề",
                cod_rounds_completed=2,  # < 3
                mpt_payloads=[],
                linter_pre_check=linter_rep
            )

    # -------------------------------------------------------------------------
    # 2. KIỂM THỬ KHUNG SƯ PHẠM UFME 5 GIAI ĐOẠN
    # -------------------------------------------------------------------------
    def test_04_ufme_stage_1_upfront_visual_anchor(self):
        """Giai đoạn 1 liên kết upfront visual_anchor_id và giải thích không điểm mù."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        mpt = payload.mpt_payloads[0]
        self.assertIsNotNone(mpt.visual_anchor_id)
        self.assertIn("FIG_", mpt.visual_anchor_id)
        self.assertGreater(len(mpt.stage_1_orientation), 50)

    def test_05_ufme_stage_2_malae_dissection_structure(self):
        """Giai đoạn 2 chứa đủ 3 cấp độ MALAE: Tổng quan, Bảng HTML, và Giới hạn tiệm cận."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        mpt = payload.mpt_payloads[0]
        dissection = mpt.stage_2_dissection
        self.assertIsNotNone(dissection)
        self.assertIn(r"\frac", dissection.pillar_equation_latex)
        self.assertNotIn("/", dissection.pillar_equation_latex)
        self.assertGreater(len(dissection.level_1_overview), 30)
        self.assertGreater(len(dissection.level_3_asymptotic_and_symmetry), 30)

    def test_06_ufme_stage_2_nomenclature_html_tags(self):
        """Bảng danh pháp HTML bắt buộc bọc thẻ Typography <i>, <sub>, <sup>."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        table = payload.mpt_payloads[0].stage_2_dissection.level_2_nomenclature_html_table
        self.assertGreaterEqual(len(table), 3)
        for row in table:
            sym = row["symbol_html"]
            self.assertTrue(
                "<i>" in sym or "<sub>" in sym or "<sup>" in sym,
                f"Ký hiệu {sym} chưa được bọc thẻ Typography!"
            )
            # Không được chứa phân số gạch chéo trong đơn vị SI
            unit = row.get("standard_unit_si", "")
            self.assertNotIn("/", unit, f"Đơn vị {unit} chứa phân số gạch chéo!")

    def test_07_ufme_stage_3_guided_derivation_prefix(self):
        """Zero-Skipped-Steps: 100% bước biến đổi trung gian bắt buộc có tiền tố ↳."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        steps = payload.mpt_payloads[0].stage_3_guided_derivation
        self.assertGreaterEqual(len(steps), 1)
        for s in steps:
            self.assertTrue(
                s.explanation_vi.startswith(UFMEEngine.MANDATORY_DERIVATION_PREFIX),
                f"Bước {s.step_index} thiếu tiền tố ↳ chuẩn!"
            )
            self.assertIn(s.step_nature, ["EXACT_ALGEBRAIC", "PHYSICAL_APPROXIMATION"])

    def test_08_ufme_stage_3_zero_slash_fractions(self):
        """Luật 14: Công thức từng bước trong dẫn xuất tuyệt đối không chứa phân số gạch chéo /."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        steps = payload.mpt_payloads[0].stage_3_guided_derivation
        for s in steps:
            self.assertNotIn("/", s.step_equation_latex, f"Công thức {s.step_equation_latex} chứa '/'!")

    def test_09_ufme_stage_4_variation_sweeps(self):
        """Giai đoạn 4 chứa phân tích quét biến thể thực nghiệm và tiệm cận lượng tử."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        stage_4 = payload.mpt_payloads[0].stage_4_variation_sweeps
        self.assertIn("Varshni", stage_4)
        self.assertIn("300 K", stage_4)

    def test_10_ufme_stage_5_cer_structure(self):
        """Giai đoạn 5 cấu trúc chuẩn CER (Claim, Evidence, Reasoning, Misconception)."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        cer = payload.mpt_payloads[0].stage_5_student_challenge_cer
        for required_key in ["challenge_prompt", "claim_guidance", "evidence_required", "reasoning_rubric", "misconception_warning"]:
            self.assertIn(required_key, cer, f"Thiếu khóa CER: {required_key}")
            self.assertGreater(len(cer[required_key]), 20)

    # -------------------------------------------------------------------------
    # 3. KIỂM THỬ CAUSAL FLOWCHAIN COMPILER (<= 65 TỪ/KHỐI)
    # -------------------------------------------------------------------------
    def test_11_causal_flowchain_word_count_limit(self):
        """Khóa cứng độ dài: 100% khối nhân quả trong micro_mechanisms bắt buộc <= 65 từ."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        for mpt in payload.mpt_payloads:
            for idx, block in enumerate(mpt.micro_mechanisms):
                wc = len(block.strip().split())
                self.assertLessEqual(
                    wc, 65,
                    f"MPT {mpt.mpt_id} Khối {idx+1} vượt quá 65 từ ({wc} từ)!"
                )

    def test_12_causal_flowchain_compiler_compression(self):
        """CausalFlowchainCompiler tự động nén khối văn bản vượt quá 65 từ."""
        long_block = (
            "Thao tác: Kích thích hạt tải trong bán dẫn chúng ta có thể nhận thấy rằng điều này trực tiếp dẫn đến việc "
            "hấp thụ photon có năng lượng lớn hơn bề rộng vùng cấm như đã được phân tích ở phần trước từ các lập luận trên rút ra kết luận "
            "electron nhảy từ vùng hóa trị lên vùng dẫn để lại lỗ trống tự do và thực hiện khảo sát trên thực tế cho thấy nồng độ hạt tải "
            "không cân bằng tăng vọt xuất hiện dòng quang điện chạy qua mạch thu tín hiệu thực nghiệm chứng minh rằng điều này hoàn toàn chính xác."
        )
        self.assertFalse(CausalFlowchainCompiler.validate_block_word_count(long_block))
        compressed = CausalFlowchainCompiler.compress_block_to_limit(long_block, max_words=65)
        self.assertTrue(CausalFlowchainCompiler.validate_block_word_count(compressed))

    # -------------------------------------------------------------------------
    # 4. KIỂM THỬ TRẠM 1 AST LINTER & LUẬT 14, 15
    # -------------------------------------------------------------------------
    def test_13_ast_linter_raw_latex_leak_detection(self):
        """Trạm 1 AST Linter phát hiện chính xác rò rỉ mã lệnh LaTeX thô trong văn bản."""
        dirty_text = r"Theo công thức \frac{a}{b} và hằng số \hbar \mu ta tính được."
        findings = ASTLinter.check_raw_latex_leaks(dirty_text)
        self.assertGreater(len(findings), 0)

    def test_14_ast_linter_slash_fraction_detection(self):
        """Trạm 1 AST Linter phát hiện phân số gạch chéo / trái luật 14."""
        dirty_text = "Hệ số hấp thụ tính bằng α = 4πk / λ đối với bước sóng kích thích."
        findings = ASTLinter.check_slash_fractions(dirty_text)
        self.assertGreater(len(findings), 0)

    def test_15_ast_linter_ascii_subscripts_detection(self):
        """Trạm 1 AST Linter phát hiện biến số lập trình gạch dưới ASCII thô."""
        dirty_text = "Dòng ngưỡng phát xạ kích thích ký hiệu là I_th và nồng độ N_th."
        findings = ASTLinter.check_raw_ascii_subscripts(dirty_text)
        self.assertGreaterEqual(len(findings), 2)

    def test_16_clean_payload_passes_linter_pre_check(self):
        """Bản thảo được sinh tự động bởi PedagogicalAuthor vượt qua Trạm 1 AST Linter 100%."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        self.assertTrue(payload.linter_pre_check.passed)
        self.assertEqual(payload.linter_pre_check.raw_latex_leaks_count, 0)
        self.assertEqual(payload.linter_pre_check.slash_fraction_count, 0)
        self.assertEqual(payload.linter_pre_check.raw_subscript_count, 0)

    # -------------------------------------------------------------------------
    # 5. KIỂM THỬ MA TRẬN 5 MẮT XÍCH OCR & CLI RUNNER
    # -------------------------------------------------------------------------
    def test_17_five_link_ocr_synthesis_coverage(self):
        """Zero-Omission: 100% 5 Mắt xích OCR từ AssetManifest được tích hợp hữu cơ."""
        payload = self.author.draft_section_payload(cod_rounds=3)
        mpt = payload.mpt_payloads[0]
        asset = self.author.get_asset_for_mpt(mpt.mpt_id)
        coverage = self.author.verify_five_link_coverage(mpt, asset)
        for chain_key in ["chain_1_origin", "chain_2_physical_feature", "chain_3_mathematical_link", "chain_4_threshold_inflection", "chain_5_engineering_insight"]:
            self.assertTrue(coverage[chain_key], f"Mắt xích {chain_key} chưa được tích hợp!")

    def test_18_cli_runner_execution(self):
        """CLI Runner thực thi thành công từ dòng lệnh và trả về mã thoát 0."""
        cmd = [
            sys.executable,
            "-m",
            "agents.pedagogical_author.runner",
            "--blueprint", self.bp_path,
            "--manifest", self.mf_path,
            "--output", os.path.join(PROJECT_ROOT, "output", "payloads", "TEST_CLI_DRAFT_PAYLOAD.json"),
            "--cod-rounds", "3"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=PROJECT_ROOT)
        self.assertEqual(result.returncode, 0, f"CLI runner thất bại: {result.stderr}")
        self.assertIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()

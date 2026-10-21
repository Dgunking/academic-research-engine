# -*- coding: utf-8 -*-
"""
tests/test_phase_4.py — Bộ Kiểm Thử Đơn Vị Toàn Diện Cho Pha 4 (Agent 4 - quality-gatekeeper)
Antigravity 2.0 - Standalone Autonomous Quality Gatekeeper & Monograph Publisher.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).

Bao gồm 15 bài kiểm tra bao phủ 6 miền kỹ thuật:
- Miền 1: Hợp đồng Pydantic AuditReport & các mô hình con (ràng buộc extra="forbid", lossless round-trip)
- Miền 2: Trạm 1 Static AST & Typography Linter (Luật 14, 15, Zero-Raw-LaTeX, Zero-Slash-Fractions)
- Miền 3: Trạm 2 Cryptographic Sidecar Manifest & Triple Buffer Geometry Gate
- Miền 4: Trạm 3 Formal SymPy CAS Verification & Đối chuẩn Vật liệu 300 K
- Miền 5: Trạm 4 Typography DejaVu Preflight & Bảng Nomenclature 4 cột ISO 80000-2
- Miền 6: Trạm 5 Chế bản ReportLab PDF, Canvas 2 lượt Trang X / Y, Bookmark 3 cấp & Hậu kiểm PyMuPDF
- Miền 7: Bảng kiểm 17 điểm nhị phân, Vòng lặp tự sửa lỗi (Self-Healing Loop <= 5 lần) & CLI Runner
"""

import os
import sys
import json
import tempfile
import unittest
import subprocess
import hashlib
from typing import Dict, Any

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
import pymupdf
from agents.quality_gatekeeper.gatekeeper import QualityGatekeeper
from schemas.blueprint import CurriculumBlueprint
from schemas.manifest import VisualAssetManifest
from schemas.payload import DraftPayload
from schemas.audit import (
    StationResult,
    DOHGStationsResult,
    BinarySeventeenPointResult,
    PublicationMetadata,
    AuditReport,
)
from common.linter import ASTLinter
from common.cas import SymPyCASEngine
from common.materials import SemiconductorDatabase, CODATA_2022


class TestPhase4QualityGatekeeper(unittest.TestCase):
    """Bộ kiểm thử đơn vị độc lập toàn diện cho Pha 4 (quality-gatekeeper)."""

    @classmethod
    def setUpClass(cls):
        cls.blueprint_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        cls.manifest_path = os.path.join(PROJECT_ROOT, "output", "manifests", "BLUEPRINT_2_1_ASSET_MANIFEST.json")
        cls.draft_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRAFT_PAYLOAD_MUC_2_1.json")

        with open(cls.blueprint_path, "r", encoding="utf-8") as f:
            cls.blueprint_data = json.load(f)
        with open(cls.manifest_path, "r", encoding="utf-8") as f:
            cls.manifest_data = json.load(f)
        with open(cls.draft_path, "r", encoding="utf-8") as f:
            cls.draft_data = json.load(f)

    # --------------------------------------------------------------------------
    # MIỀN 1: HỢP ĐỒNG PYDANTIC AUDITREPORT & RÀNG BUỘC CHẶT CHẼ
    # --------------------------------------------------------------------------
    def test_01_audit_report_pydantic_schema_strictness(self):
        """Kiểm tra hợp đồng AuditReport: extra='forbid' và serialize/deserialize 2 chiều."""
        sample_station = StationResult(
            station_name="Trạm Kiểm Thử",
            passed=True,
            details="Chi tiết kiểm thử",
            error_traces=None,
        )
        self.assertTrue(sample_station.passed)

        # Kiểm tra extra="forbid"
        with self.assertRaises(pydantic.ValidationError):
            StationResult(
                station_name="Test",
                passed=True,
                details="Extra Field Test",
                unauthorized_extra_field="ILLEGAL",
            )

        dohg_res = DOHGStationsResult(
            station_1_static_linter=sample_station,
            station_2_boundary_re3_audit=sample_station,
            station_3_sympy_cas_verification=sample_station,
            station_4_typographic_preflight=sample_station,
            station_5_reportlab_compilation=sample_station,
        )
        checklist_status = {f"GATE_{i:02d}": True for i in range(1, 18)}
        b17 = BinarySeventeenPointResult(total_passed=17, checklist_status=checklist_status)

        pub_meta = PublicationMetadata(
            temp_build_path="C:/Temp/build.pdf",
            final_drive_path="output/pdf/sample.pdf",
            atomic_replace_success=True,
            file_size_bytes=102400,
            sha256_checksum="abcdef1234567890" * 4,
            two_pass_total_pages="Trang 1 / 5",
            pdf_bookmarks_levels_verified=True,
        )

        report = AuditReport(
            section_id="MUC_2_1",
            audit_timestamp="2026-10-21T19:00:00",
            overall_verdict="PASS_100_PERCENT",
            self_healing_attempt_count=1,
            dohg_2_0_results=dohg_res,
            binary_17_point_checklist=b17,
            publication_metadata=pub_meta,
        )

        # Lossless Round-trip
        json_str = report.model_dump_json()
        restored = AuditReport.model_validate_json(json_str)
        self.assertEqual(restored.section_id, report.section_id)
        self.assertEqual(restored.overall_verdict, "PASS_100_PERCENT")
        self.assertEqual(restored.binary_17_point_checklist.total_passed, 17)

    # --------------------------------------------------------------------------
    # MIỀN 2: TRẠM 1 STATIC AST & TYPOGRAPHY LINTER
    # --------------------------------------------------------------------------
    def test_02_station_1_clean_draft_pass(self):
        """Trạm 1: Đạt PASS 100% trên bản thảo thực tế sạch mã thô."""
        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

        st1 = gatekeeper.run_dohg_station_1_linter()
        self.assertTrue(st1.passed)
        self.assertIn("PASS 100%", st1.details)
        self.assertIsNone(st1.error_traces)

    def test_03_station_1_detects_raw_latex_and_slash_fractions(self):
        """Trạm 1: Bắt lỗi chính xác khi tiêm mã LaTeX thô hoặc phân số gạch chéo."""
        tampered_draft = json.loads(json.dumps(self.draft_data))
        # Tiêm mã LaTeX thô \frac vào văn bản xuôi
        tampered_draft["mpt_payloads"][0]["stage_1_orientation"] += " Tiêm rò rỉ \\frac{a}{b} vào văn bản."
        # Tiêm phân số gạch chéo
        tampered_draft["mpt_payloads"][0]["stage_4_variation_sweeps"] += " Vận tốc dE/dk không hợp lệ."

        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, tampered_draft)

        st1 = gatekeeper.run_dohg_station_1_linter()
        self.assertFalse(st1.passed)
        self.assertIsNotNone(st1.error_traces)
        trace_str = " ".join(st1.error_traces)
        self.assertTrue("LaTeX thô" in trace_str or "phân số gạch chéo" in trace_str)

    # --------------------------------------------------------------------------
    # MIỀN 3: TRẠM 2 MANIFEST & GEOMETRY AUDIT
    # --------------------------------------------------------------------------
    def test_04_station_2_manifest_sha256_pass(self):
        """Trạm 2: Đạt PASS 100% khi đối chiếu mã băm SHA-256 tệp ảnh thực tế."""
        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

        st2 = gatekeeper.run_dohg_station_2_manifest_audit()
        self.assertTrue(st2.passed)
        self.assertIn("PASS 100%", st2.details)

    def test_05_station_2_detects_tampered_sidecar_manifest(self):
        """Trạm 2: Bắt lỗi chính xác khi sidecar manifest bị sai lệch mã băm hoặc vi phạm hình học."""
        tampered_manifest = json.loads(json.dumps(self.manifest_data))
        # Thay đổi file path tới một tệp không tồn tại
        tampered_manifest["assets"][0]["file_path_local"] = "non_existent_figure_999.png"

        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, tampered_manifest, self.draft_data)

        st2 = gatekeeper.run_dohg_station_2_manifest_audit()
        self.assertFalse(st2.passed)
        self.assertIsNotNone(st2.error_traces)
        self.assertTrue(any("Không tìm thấy" in err for err in st2.error_traces))

    # --------------------------------------------------------------------------
    # MIỀN 4: TRẠM 3 FORMAL CAS & EPISTEMIC CALIBRATION
    # --------------------------------------------------------------------------
    def test_06_station_3_sympy_cas_and_materials_pass(self):
        """Trạm 3: Đạt PASS 100% khi xác thực đại số giải tích và đối chuẩn GaAs 300 K."""
        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

        st3 = gatekeeper.run_dohg_station_3_sympy_cas()
        self.assertTrue(st3.passed)
        self.assertIn("PASS 100%", st3.details)

    def test_07_station_3_detects_algebraic_contradiction(self):
        """Trạm 3: Bắt lỗi khi bước biến đổi trung gian giải tích có sai lệch toán học."""
        tampered_draft = json.loads(json.dumps(self.draft_data))
        # Sửa bước dẫn xuất thành biểu thức sai lệch đại số: x + 1 = x + 2
        tampered_draft["mpt_payloads"][0]["stage_3_guided_derivation"][0]["step_equation_latex"] = "E + 1 = E + 2"
        tampered_draft["mpt_payloads"][0]["stage_3_guided_derivation"][0]["step_nature"] = "EXACT_ALGEBRAIC"

        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, tampered_draft)

        st3 = gatekeeper.run_dohg_station_3_sympy_cas()
        self.assertFalse(st3.passed)
        self.assertIsNotNone(st3.error_traces)
        self.assertTrue(any("SymPy CAS Mismatch" in err for err in st3.error_traces))

    # --------------------------------------------------------------------------
    # MIỀN 5: TRẠM 4 TYPOGRAPHY DEJAVU PREFLIGHT & STRUCTURE
    # --------------------------------------------------------------------------
    def test_08_station_4_nomenclature_and_structure_pass(self):
        """Trạm 4: Đạt PASS 100% khi bảng Nomenclature đủ 4 cột ISO 80000-2 và đủ CER."""
        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

        st4 = gatekeeper.run_dohg_station_4_typographic_preflight()
        self.assertTrue(st4.passed)
        self.assertIn("PASS 100%", st4.details)

    def test_09_station_4_detects_missing_nomenclature_columns(self):
        """Trạm 4: Bắt lỗi khi bảng Nomenclature thiếu cột chuẩn ISO 80000-2."""
        tampered_draft = json.loads(json.dumps(self.draft_data))
        # Xóa cột physical_role trong Nomenclature table
        for row in tampered_draft["mpt_payloads"][0]["stage_2_dissection"]["level_2_nomenclature_html_table"]:
            if "physical_role" in row:
                del row["physical_role"]

        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, tampered_draft)

        st4 = gatekeeper.run_dohg_station_4_typographic_preflight()
        self.assertFalse(st4.passed)
        self.assertIsNotNone(st4.error_traces)
        self.assertTrue(any("thiếu 1 trong 4 cột ISO" in err for err in st4.error_traces))

    # --------------------------------------------------------------------------
    # MIỀN 6: TRẠM 5 CHẾ BẢN REPORTLAB PDF & HẬU KIỂM PYMUPDF
    # --------------------------------------------------------------------------
    def test_10_station_5_pdf_compilation_and_pymupdf_verification(self):
        """Trạm 5: Biên dịch PDF thành công, kiểm toán PyMuPDF và thay thế nguyên tử."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_pdf = os.path.join(tmp_dir, "test_monograph.pdf")
            gatekeeper = QualityGatekeeper()
            gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

            st5, pub_meta = gatekeeper.run_dohg_station_5_pdf_compilation(output_pdf_path=out_pdf)

            self.assertTrue(st5.passed)
            self.assertIsNotNone(pub_meta)
            self.assertTrue(os.path.exists(out_pdf))
            self.assertTrue(pub_meta.atomic_replace_success)
            self.assertGreater(pub_meta.file_size_bytes, 10000)

            # Kiểm toán nhị phân trực tiếp bằng PyMuPDF
            doc = pymupdf.open(out_pdf)
            self.assertGreaterEqual(len(doc), 1)

            # Kiểm tra cây bookmarks 3 cấp (H1 -> H2 -> H3)
            toc = doc.get_toc()
            self.assertGreaterEqual(len(toc), 3)
            levels = set(item[0] for item in toc)
            self.assertIn(1, levels)  # H1
            self.assertIn(2, levels)  # H2
            self.assertIn(3, levels)  # H3

            # Kiểm tra text trên các trang
            has_pedagogy_text = False
            for page in doc:
                text = page.get_text()
                if "Giai đoạn 1:" in text or "Luận điểm" in text:
                    has_pedagogy_text = True
                    break
            doc.close()
            self.assertTrue(has_pedagogy_text)

    # --------------------------------------------------------------------------
    # MIỀN 7: BẢNG KIỂM 17 ĐIỂM, SELF-HEALING LOOP & CLI RUNNER
    # --------------------------------------------------------------------------
    def test_11_binary_17_point_checklist_all_pass(self):
        """Bảng kiểm 17 điểm: Đạt tuyệt đối 17/17 tiêu chí khi các trạm DOHG đạt PASS."""
        gatekeeper = QualityGatekeeper()
        gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

        st1 = gatekeeper.run_dohg_station_1_linter()
        st2 = gatekeeper.run_dohg_station_2_manifest_audit()
        st3 = gatekeeper.run_dohg_station_3_sympy_cas()
        st4 = gatekeeper.run_dohg_station_4_typographic_preflight()

        with tempfile.TemporaryDirectory() as tmp_dir:
            out_pdf = os.path.join(tmp_dir, "test_b17.pdf")
            st5, pub_meta = gatekeeper.run_dohg_station_5_pdf_compilation(output_pdf_path=out_pdf)

            dohg_res = DOHGStationsResult(
                station_1_static_linter=st1,
                station_2_boundary_re3_audit=st2,
                station_3_sympy_cas_verification=st3,
                station_4_typographic_preflight=st4,
                station_5_reportlab_compilation=st5,
            )
            b17 = gatekeeper.evaluate_binary_17_checklist(dohg_res, pub_meta)
            self.assertEqual(b17.total_passed, 17)
            self.assertEqual(len(b17.checklist_status), 17)
            self.assertTrue(all(v is True for v in b17.checklist_status.values()))

    def test_12_full_audit_self_healing_and_report_export(self):
        """Kiểm tra quy trình execute_audit toàn trình, xuất AUDIT_REPORT.json nguyên tử."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_pdf = os.path.join(tmp_dir, "monograph_out.pdf")
            out_report = os.path.join(tmp_dir, "AUDIT_REPORT.json")

            gatekeeper = QualityGatekeeper()
            gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, self.draft_data)

            report = gatekeeper.execute_audit(
                output_pdf_path=out_pdf,
                output_report_path=out_report,
                max_attempts=3,
            )

            self.assertEqual(report.overall_verdict, "PASS_100_PERCENT")
            self.assertEqual(report.binary_17_point_checklist.total_passed, 17)
            self.assertTrue(os.path.exists(out_report))

            # Nạp lại và kiểm tra JSON đã lưu
            with open(out_report, "r", encoding="utf-8") as f:
                saved_json = json.load(f)
            restored_report = AuditReport.model_validate(saved_json)
            self.assertEqual(restored_report.section_id, "MUC_2_1")
            self.assertEqual(restored_report.overall_verdict, "PASS_100_PERCENT")

    def test_13_critical_halt_after_max_healing_attempts(self):
        """Tự sửa lỗi: Kích hoạt CRITICAL_HALT khi lỗi không thể khắc phục sau max_attempts."""
        tampered_draft = json.loads(json.dumps(self.draft_data))
        # Tiêm lỗi toán học không thể tự sửa
        tampered_draft["mpt_payloads"][0]["stage_3_guided_derivation"][0]["step_equation_latex"] = "1 + 1 = 3"
        tampered_draft["mpt_payloads"][0]["stage_3_guided_derivation"][0]["step_nature"] = "EXACT_ALGEBRAIC"

        with tempfile.TemporaryDirectory() as tmp_dir:
            out_pdf = os.path.join(tmp_dir, "monograph_fail.pdf")
            out_report = os.path.join(tmp_dir, "AUDIT_REPORT_FAIL.json")

            gatekeeper = QualityGatekeeper()
            gatekeeper.load_inputs(self.blueprint_data, self.manifest_data, tampered_draft)

            report = gatekeeper.execute_audit(
                output_pdf_path=out_pdf,
                output_report_path=out_report,
                max_attempts=2,
            )

            self.assertEqual(report.overall_verdict, "CRITICAL_HALT")
            self.assertEqual(report.self_healing_attempt_count, 2)
            self.assertFalse(report.dohg_2_0_results.station_3_sympy_cas_verification.passed)
            self.assertIsNone(report.publication_metadata)

    def test_14_cli_runner_execution(self):
        """Kiểm tra thực thi dòng lệnh của CLI Runner độc lập."""
        cmd = [
            sys.executable,
            "-m",
            "agents.quality_gatekeeper.runner",
            "--blueprint", self.blueprint_path,
            "--manifest", self.manifest_path,
            "--draft", self.draft_path,
        ]
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=PROJECT_ROOT,
        )
        self.assertEqual(res.returncode, 0)
        self.assertIn("QUALITY GATEKEEPER", res.stdout)
        self.assertIn("PASS 100%", res.stdout)


if __name__ == "__main__":
    unittest.main()

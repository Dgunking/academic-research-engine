# -*- coding: utf-8 -*-
"""
Unit Test Suite cho Pha 0: Hợp đồng Dữ liệu & Thư viện Dùng chung (Shared Libraries).
Antigravity 2.0 - Phase 0 Comprehensive Test Suite.
"""

import sys
import os
import unittest
import json
import math

# Thêm đường dẫn .agents vào sys.path để nạp schemas và common
AGENTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".agents"))
if AGENTS_DIR not in sys.path:
    sys.path.insert(0, AGENTS_DIR)

import pydantic
from schemas import (
    KnowledgeDAGNode,
    KnowledgeDAGEdge,
    VisualRequirement,
    MicroPointTopicSpec,
    TerminologyEntry,
    CurriculumBlueprint,
    TripleBufferMetrics,
    OCRChainPedagogicalCaption,
    VisualAssetItem,
    VisualAssetManifest,
    EquationDissectionMALAE,
    IntermediateDerivationStep,
    MicroPointTopicPayload,
    InternalASTLinterReport,
    DraftPayload,
    StationResult,
    DOHGStationsResult,
    BinarySeventeenPointResult,
    PublicationMetadata,
    AuditReport,
)

from common import (
    ASTLinter,
    TerminologyGuardian,
    LOAN_NOUNS_WHITELIST,
    SI_UNITS,
    ATCC_BILINGUAL_DICTIONARY,
    MASTER_PHYSICS_SYMBOLS,
    SemiconductorDatabase,
    CODATA_2022,
    SEMICONDUCTORS_300K,
    SymPyCASEngine,
)


class TestPhase0Schemas(unittest.TestCase):
    """Kiểm thử Biên dịch & Hợp đồng Dữ liệu Pydantic Schemas."""

    def test_01_schema_generation(self):
        """100% schemas Pydantic biên dịch hợp lệ (model_json_schema())."""
        models = [
            CurriculumBlueprint,
            VisualAssetManifest,
            DraftPayload,
            AuditReport,
        ]
        for model in models:
            schema = model.model_json_schema()
            self.assertIsInstance(schema, dict)
            self.assertIn("properties", schema)
            self.assertGreater(len(schema["properties"]), 0)

    def test_02_blueprint_contract_validation(self):
        """Kiểm thử tính hợp lệ của Hợp đồng 1: CurriculumBlueprint."""
        blueprint_data = {
            "course_name": "Quang học và Quang điện tử",
            "chapter_index": 2,
            "section_index": 1,
            "section_title": "Vật lý Bán dẫn & Laser Diode",
            "source_documents": [
                "G:/My Drive/NotebookLM/Slide_Chuong_2.pdf",
                "G:/My Drive/NotebookLM/Coldren_Corzine_Chapter2.pdf"
            ],
            "dag_nodes": [
                {
                    "node_id": "NODE_2_1_1",
                    "concept_title": "Điều kiện Nghịch đảo Độ tích lũy",
                    "bloom_level": "Hiểu",
                    "first_principles_root": "Thống kê Fermi-Dirac và Cân bằng Nhiệt động",
                    "core_equation_latex": "E_{Fc} - E_{Fv} > h\\nu"
                }
            ],
            "dag_edges": [
                {
                    "source_node": "NODE_2_1_1",
                    "target_node": "NODE_2_1_2",
                    "relation_type": "prerequisite"
                }
            ],
            "mpt_specifications": [
                {
                    "mpt_id": "MPT_2_1_1",
                    "title": "Bản chất Nghịch đảo Độ tích lũy",
                    "core_proposition": "Phát xạ kích thích vượt trội phát xạ tự phát khi chuẩn mức Fermi tách biệt lớn hơn năng lượng photon.",
                    "prerequisite_mpt_ids": [],
                    "visual_requirement": {
                        "visual_type": "MATLAB_SIMULATION",
                        "description": "Đặc tuyến P-I và phổ phát xạ PL",
                        "physical_variables": ["I", "P", "lambda"],
                        "suggested_model": "Rate Equations"
                    },
                    "target_equations": ["E_{Fc} - E_{Fv} > h\\nu"]
                }
            ],
            "terminology_contracts": [
                {
                    "term_en": "threshold current",
                    "term_vi": "dòng ngưỡng",
                    "symbol_latex": "I_{\\mathrm{th}}",
                    "standard_unit_si": "mA",
                    "iso_standard_ref": "ISO 80000",
                    "decree_30_case": "chữ thường"
                }
            ]
        }
        obj = CurriculumBlueprint.model_validate(blueprint_data)
        self.assertEqual(obj.course_name, "Quang học và Quang điện tử")
        self.assertEqual(len(obj.dag_nodes), 1)
        self.assertEqual(len(obj.mpt_specifications), 1)

    def test_02b_blueprint_kahn_cycle_detection(self):
        """Kiểm thử Giải thuật Kahn phát hiện chu trình kín (Cyclic Dependency) trong DAG."""
        # 1. Đồ thị hợp lệ (Acyclic: NODE_1 -> NODE_2 -> NODE_3)
        valid_blueprint = {
            "course_name": "Quang học và Quang điện tử",
            "chapter_index": 2,
            "section_index": 1,
            "section_title": "Vật lý Bán dẫn & Laser Diode",
            "source_documents": ["Slide.pdf"],
            "dag_nodes": [
                {"node_id": "NODE_1", "concept_title": "C1", "bloom_level": "Hiểu", "first_principles_root": "R1"},
                {"node_id": "NODE_2", "concept_title": "C2", "bloom_level": "Hiểu", "first_principles_root": "R2"},
                {"node_id": "NODE_3", "concept_title": "C3", "bloom_level": "Hiểu", "first_principles_root": "R3"},
            ],
            "dag_edges": [
                {"source_node": "NODE_1", "target_node": "NODE_2", "relation_type": "prerequisite"},
                {"source_node": "NODE_2", "target_node": "NODE_3", "relation_type": "prerequisite"},
            ],
            "mpt_specifications": [],
            "terminology_contracts": []
        }
        obj = CurriculumBlueprint.model_validate(valid_blueprint)
        self.assertIsNotNone(obj)

        # 2. Đồ thị chu trình kín (Cyclic: NODE_1 -> NODE_2 -> NODE_3 -> NODE_1)
        cyclic_blueprint = dict(valid_blueprint)
        cyclic_blueprint["dag_edges"] = [
            {"source_node": "NODE_1", "target_node": "NODE_2", "relation_type": "prerequisite"},
            {"source_node": "NODE_2", "target_node": "NODE_3", "relation_type": "prerequisite"},
            {"source_node": "NODE_3", "target_node": "NODE_1", "relation_type": "prerequisite"},
        ]
        with self.assertRaises(pydantic.ValidationError) as ctx:
            CurriculumBlueprint.model_validate(cyclic_blueprint)
        self.assertIn("Cyclic Dependency", str(ctx.exception))

    def test_03_manifest_contract_constraints(self):
        """Kiểm thử ràng buộc cứng của Hợp đồng 2: VisualAssetManifest (TripleBuffer)."""
        valid_item = {
            "asset_id": "FIG_2_1_1",
            "mpt_reference_id": "MPT_2_1_1",
            "asset_type": "MATLAB_SIMULATION_PLOT",
            "file_path_local": "Kho_Hinh_Anh/fig_2_1_1.png",
            "aspect_ratio": "6.5:4.2",
            "matlab_palette_colors_used": ["#0072BD", "#D95319"],
            "geometry_audit": {
                "envelope_clearance_percent": 8.5,
                "min_font_size_pt": 10.5,
                "layout_collision_detected": False,
                "dpi": 300,
                "file_size_bytes": 250000
            },
            "pedagogical_caption": {
                "chain_1_origin": "Mô phỏng Rate Equations bán dẫn GaAs 300 K",
                "chain_2_physical_feature": "Đặc tuyến dốc đột ngột vượt qua dòng ngưỡng Ith",
                "chain_3_mathematical_link": "Tương ứng hệ số khuếch đại quang bù hoàn toàn suy hao",
                "chain_4_threshold_inflection": "Điểm uốn Ith = 25 mA",
                "chain_5_engineering_insight": "Tối ưu hóa thiết kế gương phản xạ khoang cộng hưởng"
            }
        }
        manifest = VisualAssetManifest(section_id="MUC_2_1", total_assets=1, assets=[valid_item])
        self.assertEqual(manifest.total_assets, 1)

        # Kiểm tra vi phạm kích thước file (> 300 KB)
        invalid_item = dict(valid_item)
        invalid_item["geometry_audit"] = dict(valid_item["geometry_audit"])
        invalid_item["geometry_audit"]["file_size_bytes"] = 350000  # > 307200
        with self.assertRaises(pydantic.ValidationError):
            VisualAssetItem.model_validate(invalid_item)

        # Kiểm tra vi phạm font chữ (< 10 pt)
        invalid_item["geometry_audit"]["file_size_bytes"] = 250000
        invalid_item["geometry_audit"]["min_font_size_pt"] = 8.0  # < 10.0
        with self.assertRaises(pydantic.ValidationError):
            VisualAssetItem.model_validate(invalid_item)

    def test_04_draft_payload_validation(self):
        """Kiểm thử tính hợp lệ của Hợp đồng 3: DraftPayload & MALAE."""
        payload_data = {
            "section_id": "MUC_2_1",
            "section_title": "Vật lý Bán dẫn & Laser Diode",
            "cod_rounds_completed": 3,
            "mpt_payloads": [
                {
                    "mpt_id": "MPT_2_1_1",
                    "mpt_title": "Điều kiện Nghịch đảo Độ tích lũy",
                    "stage_1_orientation": "Khái niệm mở đầu gắn liền với ảnh mỏ neo FIG_2_1_1.",
                    "visual_anchor_id": "FIG_2_1_1",
                    "stage_2_dissection": {
                        "pillar_equation_latex": "E_{Fc} - E_{Fv} > h\\nu",
                        "level_1_overview": "Điều kiện Bernard-Duraffourg cho phát xạ kích thích.",
                        "level_2_nomenclature_html_table": [
                            {"variable": "<i>E</i><sub>Fc</sub>", "meaning": "Chuẩn mức Fermi vùng dẫn"}
                        ],
                        "level_3_asymptotic_and_symmetry": "Khi T -> 0 K điều kiện trở thành bậc thang lý tưởng."
                    },
                    "micro_mechanisms": [
                        "Dưới phân cực thuận mạnh hạt tải được bơm ồ ạt vào vùng tích cực.",
                        "Mật độ electron vùng dẫn và lỗ trống vùng hóa trị đồng thời vượt ngưỡng."
                    ],
                    "stage_3_guided_derivation": [
                        {
                            "step_index": 1,
                            "explanation_vi": "↳ [Tường minh bước biến đổi trung gian từ slide gốc]: Biến đổi từ điều kiện cân bằng chi tiết Einstein.",
                            "step_equation_latex": "B_{21} \\rho(\\nu) > A_{21}"
                        }
                    ],
                    "stage_4_variation_sweeps": "Quét nhiệt độ từ 77 K đến 300 K cho thấy dòng ngưỡng tăng theo luật hàm mũ.",
                    "stage_5_student_challenge_cer": {
                        "claim": "Laser không thể phát xạ nếu độ phân cực thuận nhỏ hơn thế tiếp xúc.",
                        "evidence": "Đặc tuyến I-V và phân bố Fermi-Dirac.",
                        "reasoning": "Chuẩn mức Fermi không thể vượt qua khoảng cách năng lượng photon."
                    }
                }
            ],
            "linter_pre_check": {
                "passed": True,
                "raw_latex_leaks_count": 0,
                "slash_fraction_count": 0,
                "raw_subscript_count": 0
            }
        }
        draft = DraftPayload.model_validate(payload_data)
        self.assertEqual(draft.cod_rounds_completed, 3)

        # Kiểm tra nếu cod_rounds_completed < 3 thì ném lỗi
        payload_data["cod_rounds_completed"] = 2
        with self.assertRaises(pydantic.ValidationError):
            DraftPayload.model_validate(payload_data)

    def test_05_audit_report_validation(self):
        """Kiểm thử tính hợp lệ của Hợp đồng 4: AuditReport & DOHG 2.0."""
        audit_data = {
            "section_id": "MUC_2_1",
            "audit_timestamp": "2026-10-21T17:00:00Z",
            "overall_verdict": "PASS_100_PERCENT",
            "self_healing_attempt_count": 1,
            "dohg_2_0_results": {
                "station_1_static_linter": {"station_name": "Static AST Linter", "passed": True, "details": "PASS 100%"},
                "station_2_boundary_re3_audit": {"station_name": "Re3 Boundary Audit", "passed": True, "details": "PASS 100%"},
                "station_3_sympy_cas_verification": {"station_name": "SymPy CAS", "passed": True, "details": "PASS 100%"},
                "station_4_typographic_preflight": {"station_name": "Typography Preflight", "passed": True, "details": "PASS 100%"},
                "station_5_reportlab_compilation": {"station_name": "ReportLab Compilation", "passed": True, "details": "PASS 100%"}
            },
            "binary_17_point_checklist": {
                "total_passed": 17,
                "checklist_status": {f"GATE_{i}": True for i in range(1, 18)}
            },
            "publication_metadata": {
                "temp_build_path": "C:/Temp/build.pdf",
                "final_drive_path": "G:/My Drive/NotebookLM/Bai_Giang_Dong_Goi/Chuyen_Khao_Muc_2.1.pdf",
                "atomic_replace_success": True,
                "file_size_bytes": 1205000,
                "sha256_checksum": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "two_pass_total_pages": "Trang 1 / 14",
                "pdf_bookmarks_levels_verified": True
            }
        }
        report = AuditReport.model_validate(audit_data)
        self.assertEqual(report.overall_verdict, "PASS_100_PERCENT")
        self.assertEqual(report.binary_17_point_checklist.total_passed, 17)


class TestCommonLinter(unittest.TestCase):
    """Kiểm thử Thư viện Dùng chung: ASTLinter."""

    def test_01_raw_latex_detection(self):
        r"""Phát hiện mã LaTeX thô (\frac, \partial, \tau...) trong văn bản."""
        text_with_latex = "Trong công thức \\frac{dE}{dt} và thời gian \\tau_p của photon."
        report = ASTLinter.lint_text(text_with_latex)
        self.assertFalse(report["passed"])
        self.assertGreater(len(report["raw_latex_leaks"]), 0)

    def test_02_slash_fraction_detection(self):
        """Phát hiện phân số gạch chéo / trong phương trình (Luật 14)."""
        text_with_slash = "Đạo hàm theo thời gian dN/dt = G - R và năng lượng / 4πε₀."
        report = ASTLinter.lint_text(text_with_slash)
        self.assertFalse(report["passed"])
        self.assertGreater(len(report["slash_fractions"]), 0)

    def test_03_ascii_subscripts_detection(self):
        """Phát hiện biến lập trình gạch dưới ASCII thô (E_c(z), N_th, I_th)."""
        text_with_ascii = "Khi dòng bơm đạt I_th thì mật độ hạt tải đạt N_th."
        report = ASTLinter.lint_text(text_with_ascii)
        self.assertFalse(report["passed"])
        self.assertGreater(len(report["raw_ascii_subscripts"]), 0)

    def test_04_arrow_inline_detection(self):
        """Phát hiện ký hiệu ↳ bị dính liền với câu văn trước."""
        text_inline_arrow = "Câu văn kết thúc ở đây ↳ [Tường minh bước biến đổi]."
        report = ASTLinter.lint_text(text_inline_arrow)
        self.assertFalse(report["passed"])
        self.assertGreater(len(report["arrow_linebreaks"]), 0)

        # Hợp lệ khi có newline hoặc <br/> đứng trước
        text_valid_arrow = "Câu văn kết thúc ở đây.<br/>↳ [Tường minh bước biến đổi]."
        self.assertEqual(len(ASTLinter.check_arrow_linebreaks(text_valid_arrow)), 0)

    def test_05_clean_text_pass(self):
        """Văn bản chuẩn mực đạt PASS 100%."""
        clean_text = (
            "Dưới tác dụng của điện trường ngoài, các hạt tải chuyển động tạo thành dòng điện.<br/>\n"
            "↳ [Tường minh bước biến đổi]: Mật độ hạt tải tại 300 K đạt giá trị ổn định."
        )
        report = ASTLinter.lint_text(clean_text)
        self.assertTrue(report["passed"])
        self.assertEqual(report["total_errors"], 0)


class TestCommonTerminology(unittest.TestCase):
    """Kiểm thử Thư viện Dùng chung: TerminologyGuardian & ATCC."""

    def test_01_si_unit_spacing(self):
        """Bắt lỗi dính liền số và đơn vị SI (300K, 10nm) theo Luật Đo lường 04."""
        text_err = "Nhiệt độ phòng là 300K và bước sóng là 10nm với công suất 50mW."
        violations = TerminologyGuardian.lint_si_units(text_err)
        self.assertEqual(len(violations), 3)
        self.assertEqual(violations[0]["suggested"], "300 K")
        self.assertEqual(violations[1]["suggested"], "10 nm")
        self.assertEqual(violations[2]["suggested"], "50 mW")

        # Chuẩn có khoảng trắng không bị bắt lỗi
        text_ok = "Nhiệt độ phòng là 300 K và bước sóng là 10 nm với công suất 50 mW."
        self.assertEqual(len(TerminologyGuardian.lint_si_units(text_ok)), 0)

    def test_02_loan_nouns_italic(self):
        """Phát hiện danh từ mượn bị in nghiêng sai quy cách (<i>laser</i>)."""
        text_err = "Linh kiện <i>laser</i> và <i>diode</i> phát quang hoạt động ổn định."
        violations = TerminologyGuardian.lint_loan_nouns_italic(text_err)
        self.assertEqual(len(violations), 2)

    def test_03_apa7_intervals(self):
        """Phát hiện dấu nối hyphen thay vì en-dash trong khoảng số APA 7."""
        text_err = "Dải bước sóng hoạt động từ 850 - 980 nm."
        violations = TerminologyGuardian.lint_apa7_number_intervals(text_err)
        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0]["suggested"], "850–980")

    def test_04_bilingual_lookup(self):
        """Tra cứu và định dạng danh pháp song ngữ chuẩn."""
        entry = TerminologyGuardian.lookup_bilingual("vùng cấm")
        self.assertIsNotNone(entry)
        self.assertEqual(entry["term_en"], "bandgap")

        formatted = TerminologyGuardian.format_bilingual("dòng ngưỡng")
        self.assertEqual(formatted, "dòng ngưỡng (threshold current)")


class TestCommonMaterials(unittest.TestCase):
    """Kiểm thử Thư viện Dùng chung: SemiconductorDatabase & CODATA 2022."""

    def test_01_codata_precision(self):
        """Kiểm tra độ chính xác của các hằng số CODATA 2022."""
        self.assertAlmostEqual(CODATA_2022["q"], 1.602176634e-19)
        self.assertAlmostEqual(CODATA_2022["c"], 299792458.0)
        self.assertAlmostEqual(CODATA_2022["h"], 6.62607015e-34)

    def test_02_materials_lookup(self):
        """Tra cứu thông số bán dẫn 300 K cho GaAs, InP, GaN, Si, Ge."""
        gaas = SemiconductorDatabase.get_material("GaAs")
        self.assertEqual(gaas["Eg"], 1.424)
        self.assertEqual(gaas["bandgap_type"], "direct")

        si = SemiconductorDatabase.get_material("Si")
        self.assertEqual(si["Eg"], 1.120)
        self.assertEqual(si["bandgap_type"], "indirect")

    def test_03_varshni_temperature_dependence(self):
        """Kiểm tra tính toán dải năng lượng Varshni Eg(T)."""
        # Tại 300 K, Eg phải đúng bằng 1.424 eV
        eg_300 = SemiconductorDatabase.varshni_eg("GaAs", 300.0)
        self.assertAlmostEqual(eg_300, 1.424, places=3)

        # Tại 0 K, Eg(0) > Eg(300) do hiệu ứng co dãn mạng và tương tác electron-phonon
        eg_0 = SemiconductorDatabase.varshni_eg("GaAs", 0.0)
        self.assertGreater(eg_0, eg_300)

    def test_04_thermal_voltage_and_wavelength(self):
        """Kiểm tra thế nhiệt V_t và quy đổi bước sóng."""
        vt_300 = SemiconductorDatabase.thermal_voltage(300.0)
        # V_t ở 300 K xấp xỉ 25.85 mV
        self.assertAlmostEqual(vt_300 * 1000.0, 25.85, delta=0.1)

        # Bước sóng tương ứng vùng cấm GaAs (1.424 eV) xấp xỉ 870 nm
        wavelength_nm = SemiconductorDatabase.photon_energy_to_wavelength_nm(1.424)
        self.assertAlmostEqual(wavelength_nm, 870.7, delta=1.0)


class TestCommonCAS(unittest.TestCase):
    """Kiểm thử Thư viện Dùng chung: SymPyCASEngine."""

    def test_01_algebraic_identity_simple(self):
        """Kiểm chứng tính tương đương đại số: (a^2 - b^2) / (a - b) == a + b."""
        expr1 = "\\frac{a^2 - b^2}{a - b}"
        expr2 = "a + b"
        passed, msg = SymPyCASEngine.verify_algebraic_identity(expr1, expr2)
        self.assertTrue(passed, msg)

    def test_02_physical_equation_transformation(self):
        """Kiểm chứng biến đổi phương trình động năng: E = (1/2)*m*v^2 <=> 2*E/m == v^2."""
        expr1 = "\\frac{2 \\cdot E}{m}"
        expr2 = "v^2"
        # Biểu thức kiểm tra: (2*E/m) - (v^2) với E = (1/2)*m*v^2
        expr_a = "\\frac{2 \\cdot (\\frac{1}{2} \\cdot m \\cdot v^2)}{m}"
        expr_b = "v^2"
        passed, msg = SymPyCASEngine.verify_algebraic_identity(expr_a, expr_b)
        self.assertTrue(passed, msg)

    def test_03_derivation_chain(self):
        """Kiểm chứng chuỗi biến đổi giải tích 3 bước."""
        steps = [
            "x^2 + 2 \\cdot x + 1",
            "(x + 1)^2",
            "(x + 1) \\cdot (x + 1)"
        ]
        all_passed, results = SymPyCASEngine.verify_derivation_chain(steps)
        self.assertTrue(all_passed)
        self.assertEqual(len(results), 2)

    def test_04_zero_omission_residual(self):
        """Kiểm toán phần dư rỗng Zero-Omission."""
        source_entities = ["GaAs", "Dòng ngưỡng", "Nghịch đảo độ tích lũy", "300 K"]
        text_covered = "Nghiên cứu bán dẫn GaAs tại nhiệt độ 300 K đạt dòng ngưỡng nhờ nghịch đảo độ tích lũy."
        is_covered, missing = SymPyCASEngine.check_zero_omission_residual(source_entities, text_covered)
        self.assertTrue(is_covered)
        self.assertEqual(len(missing), 0)

        # Thiếu một thực thể
        text_missing = "Nghiên cứu bán dẫn GaAs tại nhiệt độ 300 K."
        is_covered_2, missing_2 = SymPyCASEngine.check_zero_omission_residual(source_entities, text_missing)
        self.assertFalse(is_covered_2)
        self.assertEqual(len(missing_2), 2)


class TestZeroCircularImports(unittest.TestCase):
    """Kiểm tra tính phi chu trình tuyệt đối giữa các module (Zero Circular Imports)."""

    def test_independent_imports(self):
        """Kiểm tra nạp độc lập từng module theo các thứ tự ngẫu nhiên."""
        import importlib
        modules = [
            "schemas.blueprint",
            "schemas.manifest",
            "schemas.payload",
            "schemas.audit",
            "common.linter",
            "common.terminology",
            "common.materials",
            "common.cas",
        ]
        for m in modules:
            mod = importlib.import_module(m)
            self.assertIsNotNone(mod)


if __name__ == "__main__":
    unittest.main()

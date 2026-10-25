# -*- coding: utf-8 -*-
"""
Unit Test Suite cho Pha 1: Curriculum & Structural Architect (Agent 1)
Antigravity 2.0 - Phân rã học liệu, Kiểm toán Kahn DAG và Hợp đồng CurriculumBlueprint.
Chủ thể phê duyệt: Lead Researcher ().
"""

import unittest
import os
import sys
import json
import tempfile

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import agents
from agents.curriculum_architect.architect import CurriculumArchitect
from agents.schemas import (
    CurriculumBlueprint,
    KnowledgeDAGNode,
    KnowledgeDAGEdge,
    MicroPointTopicSpec,
    VisualRequirement,
    TerminologyEntry,
)


class TestPhase1CurriculumArchitect(unittest.TestCase):
    """Bộ kiểm thử đơn vị cho Tác nhân 1: Curriculum & Structural Architect."""

    def setUp(self):
        self.architect = CurriculumArchitect()
        self.sample_course = "Quang học và Quang điện tử"
        self.sample_chapter = 2
        self.sample_section = 1
        self.sample_title = "Vật lý Bán dẫn & Laser Diode"

    def test_01_token_set_ratio_and_handshake(self):
        """Kiểm thử Thuật toán 1 (HDIR/DICG): Token Set Ratio và Pre-Scan Handshake."""
        # 1. So khớp mờ có dấu vs không dấu
        ratio = self.architect.token_set_ratio(
            "Vat ly ban dan va linh kien",
            "Vật lý Bán dẫn và Linh kiện Quang điện tử"
        )
        self.assertGreaterEqual(ratio, 0.8)

        # 2. Handshake đủ 2 nguồn
        mock_ok = [
            "Slide_Chuong_2_HUST.pdf",
            "Giao_Trinh_Chuong_2_Reference.pdf"
        ]
        res_ok = self.architect.pre_scan_handshake(self.sample_course, 2, mock_ok)
        self.assertTrue(res_ok["handshake_passed"])
        self.assertIsNotNone(res_ok["slide_path"])
        self.assertIsNotNone(res_ok["textbook_path"])

        # 3. Handshake thiếu Slide
        mock_no_slide = ["Giao_Trinh_Chuong_2_Reference.pdf"]
        res_no_slide = self.architect.pre_scan_handshake(self.sample_course, 2, mock_no_slide)
        self.assertFalse(res_no_slide["handshake_passed"])
        self.assertIn("Slide bài giảng", res_no_slide["error_message"])

        # 4. Handshake thiếu Sách
        mock_no_book = ["Slide_Chuong_2_HUST.pdf"]
        res_no_book = self.architect.pre_scan_handshake(self.sample_course, 2, mock_no_book)
        self.assertFalse(res_no_book["handshake_passed"])
        self.assertIn("Sách giáo trình", res_no_book["error_message"])

    def test_02_decontextualization(self):
        """Kiểm thử Thuật toán 2 (HPDE 2.0): Khử phụ thuộc ngữ cảnh đại từ chỉ định."""
        raw_text = "Nó có nồng độ hạt tải cao, khi chúng được tiêm qua tiếp giáp thì điều này tạo ra nghịch đảo tích lũy."
        cleaned = self.architect.decontextualize_proposition(raw_text)
        self.assertNotIn("nó", cleaned.lower().split())
        self.assertNotIn("chúng", cleaned.lower().split())
        self.assertIn("linh kiện", cleaned)
        self.assertIn("các hạt tải", cleaned)

    def test_03_dag_kahn_cycle_breaking(self):
        """Kiểm thử Thuật toán 4 (PLBE): Giải thuật Kahn và tự bẻ gãy chu trình GREEDYCYCLEBREAK."""
        nodes = [
            KnowledgeDAGNode(node_id="N1", concept_title="C1", bloom_level="Nhớ", first_principles_root="R1"),
            KnowledgeDAGNode(node_id="N2", concept_title="C2", bloom_level="Hiểu", first_principles_root="R2"),
            KnowledgeDAGNode(node_id="N3", concept_title="C3", bloom_level="Vận dụng", first_principles_root="R3"),
        ]

        # Chu trình kín: N1 -> N2 -> N3 -> N1
        cyclic_edges = [
            KnowledgeDAGEdge(source_node="N1", target_node="N2", relation_type="prerequisite"),
            KnowledgeDAGEdge(source_node="N2", target_node="N3", relation_type="prerequisite"),
            KnowledgeDAGEdge(source_node="N3", target_node="N1", relation_type="causal"),
        ]

        is_acyclic, clean_edges, log = self.architect.detect_and_break_dag_cycles(nodes, cyclic_edges)
        self.assertTrue(is_acyclic)
        self.assertEqual(len(clean_edges), 2)
        self.assertGreater(len(log), 0)

    def test_04_mpt_decomposition_and_visual_requirements(self):
        """Kiểm thử Thuật toán 4 (PLBE): Phân rã MPT và kiểm định VisualRequirement."""
        vis = VisualRequirement(
            visual_type="MATLAB_SIMULATION",
            description="Đặc tuyến dải năng lượng E(k)",
            physical_variables=["E", "k", "E_g"],
            suggested_model="Varshni & Kane",
            target_material="GaAs",
            operating_temperature_k=300.0
        )
        mpt = MicroPointTopicSpec(
            mpt_id="MPT_TEST_1",
            title="Khảo sát dải năng lượng",
            core_proposition="Chất bán dẫn trực tiếp tái hợp photon trực tiếp.",
            prerequisite_mpt_ids=[],
            visual_requirement=vis,
            target_equations=["E = h \\cdot \\nu"]
        )
        self.assertEqual(mpt.mpt_id, "MPT_TEST_1")
        self.assertEqual(mpt.visual_requirement.visual_type, "MATLAB_SIMULATION")
        self.assertIn("E_g", mpt.visual_requirement.physical_variables)
        self.assertEqual(mpt.visual_requirement.target_material, "GaAs")
        self.assertEqual(mpt.visual_requirement.operating_temperature_k, 300.0)

        # Kiểm tra tự động suy luận vật liệu từ văn bản ngữ cảnh
        inferred = self.architect.infer_target_material("Mô phỏng laser bán dẫn InP và giếng lượng tử InGaAsP")
        self.assertEqual(inferred, "InGaAsP")

    def test_05_atcc_terminology_standardization(self):
        """Kiểm thử Thuật toán 10 (ATCC): Chuẩn hóa danh mục danh pháp song ngữ."""
        raw_terms = [
            {
                "term_en": "population inversion",
                "term_vi": "nghịch đảo độ tích lũy",
                "symbol_latex": "\\Delta N",
                "standard_unit_si": "cm^{-3}",
                "iso_standard_ref": "ISO 80000",
                "decree_30_case": "lower"
            }
        ]
        entries = self.architect.standardize_terminology_entries(raw_terms)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].term_vi, "nghịch đảo độ tích lũy")
        self.assertEqual(entries[0].term_en, "population inversion")

    def test_06_blueprint_generation_and_validation(self):
        """Kiểm thử toàn trình hàm generate_blueprint và thẩm định Schema CurriculumBlueprint."""
        raw_nodes = [
            {"node_id": "NODE_1", "concept_title": "C1", "bloom_level": "Hiểu", "first_principles_root": "R1"},
            {"node_id": "NODE_2", "concept_title": "C2", "bloom_level": "Phân tích", "first_principles_root": "R2"},
        ]
        raw_edges = [
            {"source_node": "NODE_1", "target_node": "NODE_2", "relation_type": "prerequisite"},
        ]
        raw_mpts = [
            {
                "mpt_id": "MPT_1",
                "title": "Luận điểm 1",
                "core_proposition": "Nó hoạt động bình thường.",
                "prerequisite_mpt_ids": [],
                "target_equations": ["E = mc^2"]
            }
        ]
        raw_terms = [
            {
                "term_en": "gain",
                "term_vi": "độ khuếch đại",
                "symbol_latex": "g",
                "standard_unit_si": "cm^{-1}",
                "iso_standard_ref": "ISO 80000",
                "decree_30_case": "lower"
            }
        ]

        bp = self.architect.generate_blueprint(
            course_name=self.sample_course,
            chapter_index=self.sample_chapter,
            section_index=self.sample_section,
            section_title=self.sample_title,
            source_documents=["Slide.pdf", "Book.pdf"],
            raw_dag_nodes=raw_nodes,
            raw_dag_edges=raw_edges,
            raw_mpt_specs=raw_mpts,
            raw_terms=raw_terms
        )

        self.assertIsInstance(bp, CurriculumBlueprint)
        self.assertEqual(len(bp.dag_nodes), 2)
        self.assertEqual(len(bp.dag_edges), 1)
        self.assertEqual(len(bp.mpt_specifications), 1)
        # Kiểm tra đã khử ngữ cảnh "Nó" thành "linh kiện"
        self.assertIn("linh kiện", bp.mpt_specifications[0].core_proposition)

    def test_07_export_and_roundtrip_json(self):
        """Kiểm thử xuất bản và đọc lại tệp JSON bảo đảm tính nguyên vẹn dữ liệu."""
        raw_nodes = [
            {"node_id": "NODE_1", "concept_title": "C1", "bloom_level": "Hiểu", "first_principles_root": "R1"}
        ]
        raw_edges = []
        raw_mpts = [
            {"mpt_id": "MPT_1", "title": "M1", "core_proposition": "P1", "prerequisite_mpt_ids": []}
        ]
        raw_terms = []

        bp = self.architect.generate_blueprint(
            course_name=self.sample_course,
            chapter_index=1,
            section_index=1,
            section_title="Mục 1",
            source_documents=["A.pdf", "B.pdf"],
            raw_dag_nodes=raw_nodes,
            raw_dag_edges=raw_edges,
            raw_mpt_specs=raw_mpts,
            raw_terms=raw_terms
        )

        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
            temp_path = tf.name

        try:
            self.architect.export_blueprint_json(bp, temp_path)
            self.assertTrue(os.path.exists(temp_path))
            with open(temp_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            loaded = CurriculumBlueprint.model_validate(data)
            self.assertEqual(loaded.section_title, "Mục 1")
            self.assertEqual(len(loaded.dag_nodes), 1)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()

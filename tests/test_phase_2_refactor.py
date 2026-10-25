# -*- coding: utf-8 -*-
"""
Test Suite for Phase 2 Refactoring: 3-Block Seamless Cognitive Stream & Open CER Challenge
Xác minh:
1. Lược đồ Hợp đồng Dữ liệu Pydantic mới (OrthogonalPerspective, OpenCERChallenge, OrthogonalAndCERBlock).
2. Dây cáp chuyển giao nhận thức (Cognitive Handover Cables) giữa Khối 1 -> Khối 2 -> Khối 3.
3. Hàm vẽ Flowable make_open_cer_box trong hust_pdf_engine.py:
   - Hiển thị đầy đủ Bối cảnh, Đề bài chẩn đoán, Định hướng Claim - Evidence - Reasoning, Bẫy ngộ nhận.
   - ZERO LỜI GIẢI TRONG PDF (Chốt chặn bảo mật tư duy).
4. Tính toàn vẹn và tương thích ngược 100% với các trường di sản.
"""

import unittest
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

PDF_SCRIPTS = os.path.join(PROJECT_ROOT, ".agents", "skills", "monograph-pdf-publisher", "scripts")
if PDF_SCRIPTS not in sys.path:
    sys.path.insert(0, PDF_SCRIPTS)

import hust_pdf_engine

from agents.schemas.payload import (
    DraftPayload,
    MicroPointTopicPayload,
    OrthogonalPerspective,
    OpenCERChallenge,
    OrthogonalAndCERBlock,
    TeleologySpatialContext,
    MechanisticBlendingEquation,
    BoundaryAuditEngineeringSchema,
)
from agents.schemas.blueprint import MicroPointTopicSpec


class TestPhase2RefactorProtocol(unittest.TestCase):
    """Kiểm thử nghiệm thu cho đợt tái cấu trúc Pha 2."""

    def test_01_payload_schemas_instantiation(self):
        """Khởi tạo thành công các lớp Schema Khối 3 mới."""
        ortho = OrthogonalPerspective(
            dimension_shifts=[
                {"axis": "z vs k", "insight": "Giam giữ theo z nhưng tự do 2D trong mặt phẳng (x, y)."},
                {"axis": "Tĩnh vs Động 300 K", "insight": "Năng lượng nhiệt kB*T làm rung lắc mạng tinh thể."},
                {"axis": "Lý tưởng vs Nhám biên", "insight": "Độ nhấp nhô nguyên tử làm giãn rộng phổ phát xạ."}
            ],
            intuitive_dissection="Giải thích trực quan dung dị cho người mới tiếp cận 1 tháng.",
            practical_limitations="Cân bằng kích thước hình học và năng lượng kích thích nhiệt."
        )
        self.assertEqual(len(ortho.dimension_shifts), 3)
        self.assertIn("1 tháng", ortho.intuitive_dissection)

        cer = OpenCERChallenge(
            challenge_context="Thí nghiệm đo phổ phát xạ laser tại 300 K.",
            diagnostic_question="Vì sao đỉnh phổ bị dịch xanh 18 meV?",
            claim_guidance="Khẳng định mật độ bơm cao làm biến dạng thế năng.",
            evidence_required="Tra cứu năng lượng Fermi và hằng số bán dẫn 300 K.",
            reasoning_rubric="Xây dựng chuỗi nhân quả Band-filling.",
            misconception_trap="Tránh nhầm lẫn với hiện tượng trôi nhiệt.",
            chat_evaluation_key="Đáp án mẫu độc quyền trên Chat: Do hiệu ứng nén hạt tải..."
        )
        self.assertIn("Chat", cer.chat_evaluation_key)

        b3 = OrthogonalAndCERBlock(
            orthogonal_perspective=ortho,
            open_cer_challenge=cer
        )
        self.assertEqual(b3.open_cer_challenge.diagnostic_question, "Vì sao đỉnh phổ bị dịch xanh 18 meV?")

    def test_02_cognitive_handover_cables_present(self):
        """Xác minh sự hiện diện của Dây cáp chuyển giao nhận thức ở Khối 1 và Khối 2."""
        k1 = TeleologySpatialContext(
            systemic_teleology_sbf="Giải quyết nút thắt rò rỉ photon ở bulk.",
            plain_english_axiom="Nhốt hạt vào phòng nanomet để tăng xác suất phát quang.",
            tangible_mechanistic_analogy="Mô hình đàn cừu và mương hẹp.",
            cognitive_handover_to_block_2="Hình thù thực tế ra sao?"
        )
        self.assertEqual(k1.cognitive_handover_to_block_2, "Hình thù thực tế ra sao?")

        k2 = MechanisticBlendingEquation(
            first_principles_origin="Từ phương trình vi phân và định luật bảo toàn.",
            cognitive_handover_to_block_3="Ra ngoài đời va phải chướng ngại gì?"
        )
        self.assertEqual(k2.cognitive_handover_to_block_3, "Ra ngoài đời va phải chướng ngại gì?")

    def test_03_mpt_payload_bidirectional_sync(self):
        """Xác minh tính tương thích ngược hai chiều giữa block_3_orthogonal_cer và boundary_audit_and_engineering_schema."""
        mpt_dict = {
            "mpt_id": "MPT_TEST_01",
            "mpt_title": "Kiểm thử tương thích hai chiều",
            "teleology_and_spatial_context": {
                "systemic_teleology_sbf": "SBF test",
                "plain_english_axiom": "Axiom test",
            },
            "mechanistic_blending_equation": {
                "first_principles_origin": "Origin test",
            },
            "block_3_orthogonal_cer": {
                "orthogonal_perspective": {
                    "intuitive_dissection": "Góc nhìn đối trọng test",
                    "practical_limitations": "Giới hạn thực tế test"
                },
                "open_cer_challenge": {
                    "challenge_context": "Bối cảnh test",
                    "diagnostic_question": "Câu hỏi chẩn đoán test",
                    "claim_guidance": "Claim test",
                    "evidence_required": "Evidence test",
                    "reasoning_rubric": "Reasoning test",
                    "misconception_trap": "Trap test"
                }
            }
        }
        mpt = MicroPointTopicPayload.model_validate(mpt_dict)
        # Kiểm tra tự động populate trường legacy
        self.assertIsNotNone(mpt.boundary_audit_and_engineering_schema)
        self.assertIn("Góc nhìn đối trọng test", mpt.stage_4_variation_sweeps)
        self.assertEqual(mpt.stage_5_student_challenge_cer["challenge_prompt"], "Câu hỏi chẩn đoán test")
        self.assertEqual(mpt.stage_5_student_challenge_cer["misconception_warning"], "Trap test")

    def test_04_make_open_cer_box_rendering_and_zero_solution(self):
        """Khóa cứng hàm make_open_cer_box: Vẽ Flowable đẹp, bảo mật ZERO LỜI GIẢI trong PDF."""
        cer = OpenCERChallenge(
            challenge_context="Lab Quang điện tử đo đạc mẫu Laser InGaAs/GaAs.",
            diagnostic_question="Vì sao xuất hiện đỉnh phát xạ thứ hai ở bước sóng ngắn?",
            claim_guidance="Định hướng: Mức năng lượng n=1 bị lấp đầy hoàn toàn.",
            evidence_required="Tra cứu mật độ trạng thái DOS 2D và dòng bơm I_th.",
            reasoning_rubric="Liên kết hiện tượng Band-filling và chuyển mức n=2.",
            misconception_trap="Cảnh báo: Không phải do trôi nhiệt sinh mode ký sinh.",
            chat_evaluation_key="ĐÁP ÁN BẢO MẬT: Do mật độ dòng bơm vượt quá 2.0 I_th..."
        )
        styles = hust_pdf_engine.get_hust_styles()
        cer_box_flowable = hust_pdf_engine.make_open_cer_box(cer, styles, mpt_id="2.1.2")
        self.assertIsNotNone(cer_box_flowable)

        # Trích xuất toàn bộ văn bản trong khối Flowable
        extracted_texts = hust_pdf_engine._extract_flowable_texts([cer_box_flowable])
        full_text = " ".join(extracted_texts)

        # 1. Bắt buộc có các thành phần hướng dẫn
        self.assertIn("OPEN CER CHALLENGE", full_text)
        self.assertIn("MPT 2.1.2", full_text)
        self.assertIn("Vì sao xuất hiện đỉnh phát xạ thứ hai", full_text)
        self.assertIn("Claim Guide", full_text)
        self.assertIn("Evidence Guide", full_text)
        self.assertIn("Reasoning Guide", full_text)
        self.assertIn("Bẫy ngộ nhận cần tránh", full_text)
        self.assertIn("Chốt chặn bảo mật tư duy", full_text)

        # 2. KHÓA CỨNG: TUYỆT ĐỐI CẤM RÒ RỈ LỜI GIẢI / CHAT KEY TRONG PDF
        self.assertNotIn("ĐÁP ÁN BẢO MẬT", full_text)
        self.assertNotIn("chat_evaluation_key", full_text)

    def test_05_block_titles_updated(self):
        """Xác minh từ điển BLOCK_H3_TITLES trong hust_pdf_engine mang đúng tên gọi chuẩn mới."""
        titles = hust_pdf_engine.BLOCK_H3_TITLES
        self.assertIn("Nỗi đau Công nghệ", titles[1])
        self.assertIn("Mô hình hóa", titles[2])
        self.assertIn("Góc Nhìn Đối Trọng", titles[3])
        self.assertIn("Open CER Challenge", titles[3])


if __name__ == "__main__":
    unittest.main()

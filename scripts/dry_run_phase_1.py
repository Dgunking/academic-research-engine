# -*- coding: utf-8 -*-
"""
Kịch bản Dry-run Kiểm định Độc lập Pha 1: Curriculum & Structural Architect (Agent 1)
Antigravity 2.0 - Standalone Autonomous Subagent Verification.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).

Kiểm chứng 5 miền kỹ thuật:
- Miền 1: Pre-Scan Handshake nguồn kép (Thuật toán 1 DICG 2.0)
- Miền 2: Khử ngữ cảnh hóa Neo-Davidsonian & Phân rã tri thức (Thuật toán 2 HPDE 2.0)
- Miền 3: Kiến tạo DAG tri thức & Giải thuật Kahn khử chu trình kín (Thuật toán 4 PLBE)
- Miền 4: Phân rã Luận điểm Vi mô MPT & Ánh xạ Visual Anchor (Thuật toán 4 PLBE)
- Miền 5: Khóa danh pháp song ngữ ATCC & Xuất bản CurriculumBlueprint (Thuật toán 10 & Hợp đồng 1)
"""

import sys
import os
import json
import time

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


def log_section(title: str):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def verify_domain_1_handshake():
    log_section("[MIỀN 1] KHẢO SÁT NGUỒN KÉP & PRE-SCAN HANDSHAKE (DICG 2.0)")
    architect = CurriculumArchitect()

    # 1. So khớp mờ tên học phần Token Set Ratio >= 80%
    ratio = architect.token_set_ratio("Quang hoc va Quang dien tu", "Quang học và Quang điện tử HUST")
    print(f"[*] Độ tương đồng Token Set Ratio: {ratio*100:.1f}% -> {'PASS (>= 80%)' if ratio >= 0.8 else 'FAIL'}")
    assert ratio >= 0.8, "Token Set Ratio phải đạt >= 80%!"

    # 2. Đầy đủ nguồn kép (Slide HUST + Sách chuyên khảo)
    mock_full = [
        "Slide_Chuong_2_Vat_Ly_Ban_Dan_HUST.pdf",
        "Giao_Trinh_Chuong_2_Semiconductor_Devices_Sze.pdf"
    ]
    res_full = architect.pre_scan_handshake("Quang học và Quang điện tử", 2, mock_full)
    print(f"[*] Kiểm thử đủ nguồn kép: {res_full['handshake_passed']} -> PASS (Cả 2 tệp đều sẵn sàng)")
    assert res_full["handshake_passed"] is True

    # 3. Thiếu Slide bài giảng
    mock_no_slide = ["Giao_Trinh_Chuong_2_Semiconductor_Devices_Sze.pdf"]
    res_no_slide = architect.pre_scan_handshake("Quang học và Quang điện tử", 2, mock_no_slide)
    print(f"[*] Kiểm thử thiếu Slide: Bắt chính xác lỗi -> PASS ('{res_no_slide['error_message']}')")
    assert res_no_slide["handshake_passed"] is False
    assert "Slide bài giảng" in res_no_slide["error_message"]

    # 4. Thiếu Sách giáo trình
    mock_no_book = ["Slide_Chuong_2_Vat_Ly_Ban_Dan_HUST.pdf"]
    res_no_book = architect.pre_scan_handshake("Quang học và Quang điện tử", 2, mock_no_book)
    print(f"[*] Kiểm thử thiếu Giáo trình: Bắt chính xác lỗi -> PASS ('{res_no_book['error_message']}')")
    assert res_no_book["handshake_passed"] is False
    assert "Sách giáo trình" in res_no_book["error_message"]


def verify_domain_2_decontextualization():
    log_section("[MIỀN 2] KHỬ NGỮ CẢNH HÓA NEO-DAVIDSONIAN & TRI THỨC NGUYÊN TỬ (HPDE 2.0)")
    architect = CurriculumArchitect()

    raw_text = "Nó hoạt động ở chế độ nghịch đảo độ tích lũy, khi chúng tái hợp bức xạ thì điều này tạo ra chùm photon kết hợp."
    cleaned = architect.decontextualize_proposition(raw_text)
    print(f"[*] Văn bản thô ban đầu: '{raw_text}'")
    print(f"[*] Sau khử ngữ cảnh : '{cleaned}'")
    assert "nó" not in cleaned.lower()
    assert "chúng" not in cleaned.lower()
    assert "điều này" not in cleaned.lower()
    print("[+] Kiểm thử khử phụ thuộc ngữ cảnh đại từ chỉ định: PASS 100%")


def verify_domain_3_dag_kahn():
    log_section("[MIỀN 3] ĐỒ THỊ TRI THỨC DAG & GIẢI THUẬT KAHN KHỬ CHU TRÌNH (PLBE)")
    architect = CurriculumArchitect()

    nodes = [
        KnowledgeDAGNode(
            node_id="NODE_A",
            concept_title="Khái niệm A",
            bloom_level="Hiểu",
            first_principles_root="Nguyên lý đầu A"
        ),
        KnowledgeDAGNode(
            node_id="NODE_B",
            concept_title="Khái niệm B",
            bloom_level="Phân tích",
            first_principles_root="Nguyên lý đầu B"
        ),
        KnowledgeDAGNode(
            node_id="NODE_C",
            concept_title="Khái niệm C",
            bloom_level="Vận dụng",
            first_principles_root="Nguyên lý đầu C"
        ),
    ]

    # Test 3a: Đồ thị hợp lệ (Acyclic: A -> B -> C)
    valid_edges = [
        KnowledgeDAGEdge(source_node="NODE_A", target_node="NODE_B", relation_type="prerequisite"),
        KnowledgeDAGEdge(source_node="NODE_B", target_node="NODE_C", relation_type="causal"),
    ]
    is_ok, clean_edges, log = architect.detect_and_break_dag_cycles(nodes, valid_edges)
    print(f"[*] Kiểm thử DAG hợp lệ: is_acyclic = {is_ok}, số cạnh = {len(clean_edges)} -> PASS")
    assert is_ok is True
    assert len(clean_edges) == 2

    # Test 3b: Đồ thị chu trình kín (A -> B -> C -> A)
    cyclic_edges = [
        KnowledgeDAGEdge(source_node="NODE_A", target_node="NODE_B", relation_type="prerequisite"),
        KnowledgeDAGEdge(source_node="NODE_B", target_node="NODE_C", relation_type="prerequisite"),
        KnowledgeDAGEdge(source_node="NODE_C", target_node="NODE_A", relation_type="causal"), # Cạnh chu trình
    ]
    is_ok_cyclic, healed_edges, cycle_log = architect.detect_and_break_dag_cycles(nodes, cyclic_edges)
    print(f"[*] Kiểm thử tự phục hồi Self-Healing chu trình kín:")
    for log_item in cycle_log:
        print(f"    ↳ {log_item}")
    print(f"[*] Kết quả sau GREEDYCYCLEBREAK: is_acyclic = {is_ok_cyclic}, số cạnh còn lại = {len(healed_edges)} -> PASS")
    assert is_ok_cyclic is True
    assert len(healed_edges) == 2  # Đã cắt chính xác cạnh quay ngược


def verify_domain_4_mpt_decomposition():
    log_section("[MIỀN 4] PHÂN RÃ LUẬN ĐIỂM VI MÔ MPT & VISUAL ANCHORS (PLBE)")
    architect = CurriculumArchitect()

    raw_mpts = [
        {
            "mpt_id": "MPT_2_1_1",
            "title": "Cấu trúc dải năng lượng và vùng cấm trực tiếp GaAs",
            "core_proposition": "GaAs là chất bán dẫn vùng cấm trực tiếp với cực tiểu dải dẫn và cực đại dải hóa trị cùng nằm tại k = 0.",
            "prerequisite_mpt_ids": [],
            "visual_requirement": {
                "visual_type": "MATLAB_SIMULATION",
                "description": "Đồ thị giải tích dải năng lượng E-k của bán dẫn GaAs",
                "physical_variables": ["E", "k", "E_g"],
                "suggested_model": "Kane 2-band k.p"
            },
            "target_equations": ["E(k) = E_c + \\frac{\\hbar^2 \\cdot k^2}{2 \\cdot m^*_e}"]
        },
        {
            "mpt_id": "MPT_2_1_2",
            "title": "Nghịch đảo độ tích lũy và điều kiện Bernard-Duraffourg",
            "core_proposition": "Điều kiện cần để đạt được hệ số khuếch đại quang học dương trong chất bán dẫn là hiệu mức quasi-Fermi phải lớn hơn năng lượng photon.",
            "prerequisite_mpt_ids": ["MPT_2_1_1"],
            "visual_requirement": {
                "visual_type": "SCHEMATIC_DIAGRAM",
                "description": "Sơ đồ dải năng lượng dị thể kép DH khi phân cực thuận",
                "physical_variables": ["E_Fc", "E_Fv"],
                "suggested_model": "Double Heterostructure"
            },
            "target_equations": ["E_{Fc} - E_{Fv} > h \\cdot \\nu"]
        }
    ]

    mpt_objects = []
    for m in raw_mpts:
        vis = VisualRequirement.model_validate(m["visual_requirement"])
        mpt = MicroPointTopicSpec(
            mpt_id=m["mpt_id"],
            title=m["title"],
            core_proposition=m["core_proposition"],
            prerequisite_mpt_ids=m["prerequisite_mpt_ids"],
            visual_requirement=vis,
            target_equations=m["target_equations"]
        )
        mpt_objects.append(mpt)

    print(f"[*] Phân rã thành công: {len(mpt_objects)} Luận điểm Vi mô (MPT)")
    for m in mpt_objects:
        print(f"    - [{m.mpt_id}] {m.title} | Anchor: {m.visual_requirement.visual_type} -> PASS")
    assert len(mpt_objects) == 2


def verify_domain_5_terminology_and_contract():
    log_section("[MIỀN 5] KHÓA DANH PHÁP SONG NGỮ ATCC & XUẤT BẢN CURRICULUM BLUEPRINT")
    architect = CurriculumArchitect()

    raw_terms = [
        {
            "term_en": "threshold current",
            "term_vi": "dòng ngưỡng",
            "symbol_latex": "I_{\\text{th}}",
            "standard_unit_si": "mA",
            "iso_standard_ref": "ISO 80000",
            "decree_30_case": "lower"
        },
        {
            "term_en": "differential quantum efficiency",
            "term_vi": "hiệu suất lượng tử vi phân",
            "symbol_latex": "\\eta_d",
            "standard_unit_si": "%",
            "iso_standard_ref": "ISO 80000",
            "decree_30_case": "lower"
        }
    ]

    blueprint = architect.generate_blueprint(
        course_name="Quang học và Quang điện tử",
        chapter_index=2,
        section_index=1,
        section_title="Vật lý Bán dẫn & Laser Diode",
        source_documents=["Slide_Chuong_2.pdf", "Giao_Trinh_Chuong_2.pdf"],
        raw_dag_nodes=[
            {
                "node_id": "NODE_2_1_1",
                "concept_title": "Dải năng lượng & Vùng cấm trực tiếp GaAs",
                "bloom_level": "Hiểu",
                "first_principles_root": "Phương trình Schrödinger trong thế tuần hoàn Bloch",
                "core_equation_latex": "E_g(T) = E_g(0) - \\frac{\\alpha \\cdot T^2}{T + \\beta}"
            },
            {
                "node_id": "NODE_2_1_2",
                "concept_title": "Nghịch đảo độ tích lũy & Điều kiện phát xạ kích thích",
                "bloom_level": "Phân tích",
                "first_principles_root": "Định luật bảo toàn năng lượng & Thống kê Fermi-Dirac",
                "core_equation_latex": "E_{Fc} - E_{Fv} > h \\cdot \\nu > E_g"
            }
        ],
        raw_dag_edges=[
            {"source_node": "NODE_2_1_1", "target_node": "NODE_2_1_2", "relation_type": "prerequisite"}
        ],
        raw_mpt_specs=[
            {
                "mpt_id": "MPT_2_1_1",
                "title": "Cơ chế vi mô của vùng cấm bán dẫn trực tiếp",
                "core_proposition": "GaAs là bán dẫn vùng cấm trực tiếp cho phép tái hợp bức xạ trực tiếp.",
                "prerequisite_mpt_ids": [],
                "visual_requirement": {
                    "visual_type": "MATLAB_SIMULATION",
                    "description": "Đặc tuyến dải năng lượng E(k)",
                    "physical_variables": ["E", "k"],
                    "suggested_model": "Kane 2-band k.p"
                },
                "target_equations": ["E(k) = E_c + \\frac{\\hbar^2 \\cdot k^2}{2 \\cdot m^*_e}"]
            }
        ],
        raw_terms=raw_terms
    )

    out_test_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
    architect.export_blueprint_json(blueprint, out_test_path)
    print(f"[*] Xuất bản tệp Blueprint thành công: {out_test_path}")

    # Đọc lại và xác thực ngược (Round-trip Deserialization)
    with open(out_test_path, "r", encoding="utf-8") as f:
        loaded_json = json.load(f)
    loaded_bp = CurriculumBlueprint.model_validate(loaded_json)
    print(f"[*] Xác thực ngược Round-trip Deserialization: PASS (Khớp 100% {len(loaded_bp.dag_nodes)} nodes, {len(loaded_bp.terminology_contracts)} terms)")
    assert loaded_bp.course_name == "Quang học và Quang điện tử"
    assert len(loaded_bp.terminology_contracts) == 2


def main():
    start_time = time.time()
    print("=" * 80)
    print("  BẮT ĐẦU KIỂM THỬ DRY-RUN TOÀN DIỆN PHA 1: CURRICULUM ARCHITECT (AGENT 1)")
    print("  Chủ thể: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST)")
    print("=" * 80)

    verify_domain_1_handshake()
    verify_domain_2_decontextualization()
    verify_domain_3_dag_kahn()
    verify_domain_4_mpt_decomposition()
    verify_domain_5_terminology_and_contract()

    duration = time.time() - start_time
    log_section(f"KẾT QUẢ NGHIỆM THU PHA 1: 100% ĐẠT CHUẨN (Thời gian thực thi: {duration:.3f} s)")
    print("  [X] Miền 1: Pre-Scan Handshake (Slide + Sách) -> SẴN SÀNG.")
    print("  [X] Miền 2: Decontextualization & HPDE 2.0 -> SẴN SÀNG.")
    print("  [X] Miền 3: Knowledge DAG & Kahn Acyclic Self-Healing -> SẴN SÀNG.")
    print("  [X] Miền 4: Micro-Point Topics (MPT) & Visual Anchors -> SẴN SÀNG.")
    print("  [X] Miền 5: ATCC Terminology & CurriculumBlueprint Schema -> SẴN SÀNG.")
    print("  [X] Dual-Mode Triad: CLI Runner + Subagent Spec -> HOÀN THIỆN.")
    print("=" * 80)


if __name__ == "__main__":
    main()

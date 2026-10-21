# -*- coding: utf-8 -*-
"""
CLI Runner độc lập cho Curriculum & Structural Architect Subagent (Agent 1).
Cho phép Bùi Trung Dũng chạy kiểm thử và trích xuất Blueprint từ dòng lệnh PowerShell/Terminal.
"""

import os
import sys
import argparse
import json

# Cấu hình UTF-8 cho Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import agents
from agents.curriculum_architect.architect import CurriculumArchitect


def main():
    parser = argparse.ArgumentParser(
        description="CLI Runner cho Agent 1: Curriculum & Structural Architect (curriculum-architect)"
    )
    parser.add_argument("--course", type=str, default="Quang học và Quang điện tử", help="Tên học phần")
    parser.add_argument("--chapter", type=int, default=2, help="Chỉ số chương")
    parser.add_argument("--section", type=int, default=1, help="Chỉ số phân mục")
    parser.add_argument("--title", type=str, default="Vật lý Bán dẫn & Laser Diode", help="Tiêu đề phân mục")
    parser.add_argument("--out", type=str, default="output/blueprints/BLUEPRINT_TEST.json", help="Đường dẫn file JSON xuất ra")
    parser.add_argument("--handshake-only", action="store_true", help="Chỉ chạy Pre-scan Handshake")

    args = parser.parse_args()

    print("=" * 80)
    print("  KÍCH HOẠT CLI RUNNER: CURRICULUM & STRUCTURAL ARCHITECT (AGENT 1)")
    print(f"  Học phần: {args.course} | Chương {args.chapter} - Mục {args.section}: {args.title}")
    print("=" * 80)

    architect = CurriculumArchitect()

    # 1. Chạy Pre-Scan Handshake
    handshake = architect.pre_scan_handshake(
        course_name=args.course,
        chapter_index=args.chapter,
        mock_file_list=[
            f"Slide_Chuong_{args.chapter}_HUST.pdf",
            f"Giao_Trinh_Chuong_{args.chapter}_Reference.pdf"
        ]
    )
    print(f"[*] Pre-Scan Handshake: {'PASS' if handshake['handshake_passed'] else 'FAIL'}")
    if not handshake["handshake_passed"]:
        print(f"    Chi tiết: {handshake['error_message']}")
        if args.handshake_only:
            sys.exit(1)

    if args.handshake_only:
        print("[+] Hoàn tất bước kiểm tra Pre-scan Handshake!")
        sys.exit(0)

    # 2. Xây dựng Blueprint mẫu chuẩn kiến trúc
    sample_nodes = [
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
        },
        {
            "node_id": "NODE_2_1_3",
            "concept_title": "Dòng ngưỡng & Cân bằng hạt tải laser diode",
            "bloom_level": "Vận dụng",
            "first_principles_root": "Phương trình liên tục hạt tải & Định luật bảo toàn hạt",
            "core_equation_latex": "I_{\\text{th}} = \\frac{q \\cdot V_{\\text{act}} \\cdot N_{\\text{th}}}{\\tau_n}"
        }
    ]

    sample_edges = [
        {"source_node": "NODE_2_1_1", "target_node": "NODE_2_1_2", "relation_type": "prerequisite"},
        {"source_node": "NODE_2_1_2", "target_node": "NODE_2_1_3", "relation_type": "causal"},
    ]

    sample_mpts = [
        {
            "mpt_id": "MPT_2_1_1",
            "title": "Cơ chế vi mô của vùng cấm bán dẫn trực tiếp và phát xạ tái hợp",
            "core_proposition": "GaAs là bán dẫn vùng cấm trực tiếp cho phép tái hợp bức xạ trực tiếp giữa electron đáy dải dẫn và lỗ trống đỉnh dải hóa trị mà không cần phonon bảo toàn động lượng.",
            "prerequisite_mpt_ids": [],
            "visual_requirement": {
                "visual_type": "MATLAB_SIMULATION",
                "description": "Đặc tuyến dải năng lượng E(k) của GaAs so với Si",
                "physical_variables": ["E", "k", "E_g"],
                "suggested_model": "Kane 2-band k.p"
            },
            "target_equations": ["E(k) = E_c + \\frac{\\hbar^2 \\cdot k^2}{2 \\cdot m^*_e}"]
        },
        {
            "mpt_id": "MPT_2_1_2",
            "title": "Điều kiện Bernard-Duraffourg và cơ chế nghịch đảo hạt tải",
            "core_proposition": "Laser diode chỉ đạt được khuếch đại quang học khi hiệu hai mức quasi-Fermi vượt quá năng lượng photon phát xạ.",
            "prerequisite_mpt_ids": ["MPT_2_1_1"],
            "visual_requirement": {
                "visual_type": "SCHEMATIC_DIAGRAM",
                "description": "Sơ đồ dải năng lượng dị thể kép DH khi phân cực thuận",
                "physical_variables": ["E_Fc", "E_Fv", "qV_a"],
                "suggested_model": "Double Heterostructure"
            },
            "target_equations": ["E_{Fc} - E_{Fv} > h \\cdot \\nu"]
        }
    ]

    sample_terms = [
        {
            "term_en": "threshold current",
            "term_vi": "dòng ngưỡng",
            "symbol_latex": "I_{\\text{th}}",
            "standard_unit_si": "mA",
            "iso_standard_ref": "ISO 80000",
            "decree_30_case": "lower"
        },
        {
            "term_en": "quasi-fermi level",
            "term_vi": "mức quasi-fermi",
            "symbol_latex": "E_{Fc}",
            "standard_unit_si": "eV",
            "iso_standard_ref": "ISO 80000",
            "decree_30_case": "lower"
        }
    ]

    print("[*] Đang kiến tạo và kiểm toán Curriculum Blueprint...")
    blueprint = architect.generate_blueprint(
        course_name=args.course,
        chapter_index=args.chapter,
        section_index=args.section,
        section_title=args.title,
        source_documents=[f"Slide_Chuong_{args.chapter}.pdf", f"Giao_Trinh_Chuong_{args.chapter}.pdf"],
        raw_dag_nodes=sample_nodes,
        raw_dag_edges=sample_edges,
        raw_mpt_specs=sample_mpts,
        raw_terms=sample_terms
    )

    out_file = architect.export_blueprint_json(blueprint, args.out)
    print(f"[+] Xuất bản thành công Hợp đồng Dữ liệu: {out_file}")
    print(f"    - Tổng số Node DAG: {len(blueprint.dag_nodes)}")
    print(f"    - Tổng số Edge DAG: {len(blueprint.dag_edges)}")
    print(f"    - Tổng số MPT: {len(blueprint.mpt_specifications)}")
    print(f"    - Tổng số Giao ước danh pháp ATCC: {len(blueprint.terminology_contracts)}")
    print("=" * 80)


if __name__ == "__main__":
    main()

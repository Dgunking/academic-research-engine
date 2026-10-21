# -*- coding: utf-8 -*-
"""
Kịch bản Dry-run Kiểm định Độc lập Pha 3: Deep Pedagogical Author (Agent 3 - pedagogical-author)
Antigravity 2.0 - Standalone Autonomous Subagent Verification.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).

Kiểm chứng 5 miền kỹ thuật:
- Miền 1: Khung Sư phạm Feynman Hợp nhất UFME 5 Giai đoạn (Thuật toán 5)
- Miền 2: Giải phẫu Phương trình 3 Cấp độ MALAE (Thuật toán 12)
- Miền 3: Chuỗi Biến đổi Nhân quả Vi mô & Khóa cứng <= 65 từ/khối (Causal Flowchain Compiler)
- Miền 4: Tích hợp Động 5 Mắt xích OCR & Nén Chain-of-Density (Zero-Omission Gate & CoD >= 3)
- Miền 5: Hợp đồng DraftPayload & Kiểm định Tĩnh Trạm 1 AST Linter (Thuật toán 8 & Luật 14, 15)
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
from agents.pedagogical_author.author import (
    PedagogicalAuthor,
    UFMEEngine,
    MALAEEngine,
    CausalFlowchainCompiler,
    sanitize_text_for_typography,
)
from agents.schemas.blueprint import CurriculumBlueprint
from agents.schemas.manifest import VisualAssetManifest
from agents.schemas.payload import (
    DraftPayload,
    MicroPointTopicPayload,
    EquationDissectionMALAE,
    IntermediateDerivationStep,
    InternalASTLinterReport,
)
from agents.common.linter import ASTLinter


def log_section(title: str):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def verify_domain_1_ufme_five_stages(payload: DraftPayload):
    log_section("[MIỀN 1] KHUNG SƯ PHẠM FEYNMAN HỢP NHẤT UFME 5 GIAI ĐOẠN (THUẬT TOÁN 5)")

    assert len(payload.mpt_payloads) > 0, "[-] Lỗi: Không có MPT nào trong payload!"
    mpt = payload.mpt_payloads[0]

    # 1. Giai đoạn 1: Orientation & Upfront Visual Anchor
    print(f"[*] Giai đoạn 1 (Định hướng & Mở đầu):")
    print(f"    - Neo trực quan mỏ neo: {mpt.visual_anchor_id}")
    print(f"    - Nội dung định hướng: {mpt.stage_1_orientation[:120]}...")
    assert mpt.visual_anchor_id is not None, "[-] Giai đoạn 1 thiếu visual_anchor_id!"
    assert len(mpt.stage_1_orientation) > 50, "[-] Giai đoạn 1 nội dung quá ngắn hoặc thiếu!"
    print("    [+] Giai đoạn 1: ĐẠT CHUẨN (Upfront Visual Anchor).")

    # 2. Giai đoạn 2: Minimal Example & MALAE Dissection
    print(f"[*] Giai đoạn 2 (Ví dụ tối giản & Giải phẫu MALAE):")
    assert mpt.stage_2_dissection is not None, "[-] Giai đoạn 2 thiếu giải phẫu MALAE!"
    print(f"    - Phương trình cột trụ: {mpt.stage_2_dissection.pillar_equation_latex}")
    print("    [+] Giai đoạn 2: ĐẠT CHUẨN.")

    # 3. Giai đoạn 3: Guided Derivation & Intermediate Steps
    print(f"[*] Giai đoạn 3 (Thực hành có hướng dẫn & Dẫn xuất trung gian):")
    assert len(mpt.stage_3_guided_derivation) >= 1, "[-] Giai đoạn 3 thiếu bước dẫn xuất trung gian!"
    for step in mpt.stage_3_guided_derivation:
        print(f"    - Bước {step.step_index}: {step.explanation_vi[:60]}...")
        print(f"      Công thức: {step.step_equation_latex}")
        assert step.explanation_vi.startswith(UFMEEngine.MANDATORY_DERIVATION_PREFIX), (
            f"[-] Bước {step.step_index} vi phạm tiền tố bắt buộc ↳!"
        )
        assert "/" not in step.step_equation_latex, (
            f"[-] Bước {step.step_index} chứa phân số gạch chéo / trái luật 14: {step.step_equation_latex}"
        )
    print("    [+] Giai đoạn 3: ĐẠT CHUẨN (Zero-Skipped-Steps & Zero-Slash-Fractions).")

    # 4. Giai đoạn 4: Variation Sweeps & Asymptotic Limits
    print(f"[*] Giai đoạn 4 (Phân tích biến thể & Quét tiệm cận):")
    assert len(mpt.stage_4_variation_sweeps) > 50, "[-] Giai đoạn 4 thiếu phân tích biến thể!"
    print(f"    - Nội dung biến thể: {mpt.stage_4_variation_sweeps[:120]}...")
    print("    [+] Giai đoạn 4: ĐẠT CHUẨN.")

    # 5. Giai đoạn 5: Student Challenge CER & Rubric
    print(f"[*] Giai đoạn 5 (Thử thách sinh viên CER & Rubric):")
    cer = mpt.stage_5_student_challenge_cer
    assert "challenge_prompt" in cer and "claim_guidance" in cer and "evidence_required" in cer and "reasoning_rubric" in cer, (
        "[-] Giai đoạn 5 thiếu các trường bắt buộc trong cấu trúc CER!"
    )
    print(f"    - Challenge Prompt: {cer['challenge_prompt'][:90]}...")
    print(f"    - Claim Guidance: {cer['claim_guidance'][:90]}...")
    print("    [+] Giai đoạn 5: ĐẠT CHUẨN (CER Framework & Rubric).")

    print("[+] KẾT QUẢ MIỀN 1: PASS 100% (UFME 5 Giai đoạn toàn diện).")


def verify_domain_2_malae_equation_dissection(payload: DraftPayload):
    log_section("[MIỀN 2] GIẢI PHẪU PHƯƠNG TRÌNH 3 CẤP ĐỘ MALAE (THUẬT TOÁN 12)")

    mpt = payload.mpt_payloads[0]
    dissection = mpt.stage_2_dissection

    # 1. Cấp 1: Tổng quan ý nghĩa vật lý
    print("[*] Cấp 1 (Tổng quan vật lý & Bảo toàn):")
    print(f"    - {dissection.level_1_overview[:120]}...")
    assert len(dissection.level_1_overview) > 30, "[-] Cấp 1 thiếu phân tích nguyên lý đầu!"
    print("    [+] Cấp 1: ĐẠT CHUẨN.")

    # 2. Cấp 2: Bảng định danh HTML
    print("[*] Cấp 2 (Bảng định danh HTML & Đơn vị SI ISO 80000):")
    table = dissection.level_2_nomenclature_html_table
    assert len(table) >= 3, f"[-] Cấp 2 có quá ít đại lượng giải phẫu: {len(table)}"
    for row in table:
        sym = row.get("symbol_html", "")
        name = row.get("name_vi", "")
        unit = row.get("standard_unit_si", "")
        role = row.get("physical_role", "")
        print(f"    - {sym} | {name} | Đơn vị: [{unit}] | Vai trò: {role[:40]}...")
        assert "<i>" in sym or "<sub>" in sym or "<sup>" in sym, (
            f"[-] Ký hiệu '{sym}' chưa bọc thẻ Typography HTML!"
        )
        assert "/" not in unit, f"[-] Đơn vị '{unit}' chứa dấu gạch chéo trái luật 14!"
    print("    [+] Cấp 2: ĐẠT CHUẨN (HTML Typography & ISO 80000).")

    # 3. Cấp 3: Khảo sát tiệm cận cực trị biên & đối xứng
    print("[*] Cấp 3 (Phân tích giới hạn tiệm cận & Đối xứng chẵn lẻ):")
    print(f"    - {dissection.level_3_asymptotic_and_symmetry[:120]}...")
    assert "tiệm cận" in dissection.level_3_asymptotic_and_symmetry.lower() or "đối xứng" in dissection.level_3_asymptotic_and_symmetry.lower(), (
        "[-] Cấp 3 thiếu khảo sát tiệm cận hoặc đối xứng!"
    )
    print("    [+] Cấp 3: ĐẠT CHUẨN.")

    print("[+] KẾT QUẢ MIỀN 2: PASS 100% (MALAE 3 Cấp độ chuẩn xác).")


def verify_domain_3_causal_flowchain(payload: DraftPayload):
    log_section("[MIỀN 3] CHUỖI BIẾN ĐỔI NHÂN QUẢ VI MÔ & KHÓA CỨNG <= 65 TỪ/KHỐI (THUẬT TOÁN 5)")

    mpt = payload.mpt_payloads[0]
    mechanisms = mpt.micro_mechanisms
    assert len(mechanisms) >= 2, f"[-] Số lượng khối nhân quả vi mô quá ít: {len(mechanisms)}"

    for idx, block in enumerate(mechanisms, 1):
        word_count = len(block.strip().split())
        print(f"[*] Khối nhân quả {idx}:")
        print(f"    - Độ dài: {word_count} từ (Giới hạn trần <= 65 từ)")
        print(f"    - Văn bản: {block[:100]}...")
        assert word_count <= 65, f"[-] Khối nhân quả {idx} vượt quá 65 từ ({word_count} từ)!"
        assert "──>" in block or "-->" in block or "══>" in block or "==>" in block, (
            f"[-] Khối nhân quả {idx} thiếu cấu trúc mũi tên có hướng!"
        )
        print(f"    [+] Khối {idx}: ĐẠT CHUẨN ({word_count} <= 65 từ).")

    print("[+] KẾT QUẢ MIỀN 3: PASS 100% (Khóa cứng độ dài Causal Flowchain).")


def verify_domain_4_five_link_ocr_and_cod(author: PedagogicalAuthor, payload: DraftPayload):
    log_section("[MIỀN 4] TÍCH HỢP ĐỘNG 5 MẮT XÍCH OCR & NÉN CHAIN-OF-DENSITY (ZERO-OMISSION)")

    # 1. Kiểm tra số vòng nén CoD
    print(f"[*] Số vòng nén Chain-of-Density đã hoàn tất: {payload.cod_rounds_completed}")
    assert payload.cod_rounds_completed >= 3, (
        f"[-] Vi phạm quy chuẩn CoD: Số vòng nén bắt buộc >= 3 (nhận: {payload.cod_rounds_completed})!"
    )
    print("    [+] Khóa cứng CoD >= 3 vòng: ĐẠT CHUẨN.")

    # 2. Kiểm toán độ phủ 5 Mắt xích OCR
    mpt = payload.mpt_payloads[0]
    asset = author.get_asset_for_mpt(mpt.mpt_id)
    assert asset is not None, f"[-] Không tìm thấy tài nguyên hình ảnh cho MPT {mpt.mpt_id}!"

    coverage = author.verify_five_link_coverage(mpt, asset)
    print("[*] Ma trận Kiểm toán Độ phủ 5 Mắt xích OCR:")
    for link_name, covered in coverage.items():
        status = "PASS" if covered else "FAIL"
        print(f"    - [{status}] {link_name}: {'Đã tích hợp hữu cơ' if covered else 'CHƯA PHỦ'}")
        assert covered, f"[-] Mắt xích OCR '{link_name}' bị thiếu hoặc làm lấy lệ!"

    print("[+] KẾT QUẢ MIỀN 4: PASS 100% (Zero-Omission & CoD >= 3).")


def verify_domain_5_draft_payload_and_ast_linter(payload: DraftPayload, output_file: str):
    log_section("[MIỀN 5] HỢP ĐỒNG DRAFT_PAYLOAD.json & KIỂM ĐỊNH TĨNH TRẠM 1 AST LINTER")

    # 1. Kiểm định Trạm 1 AST Linter
    report = payload.linter_pre_check
    print("[*] Kết quả Trạm 1 AST Linter Pre-check:")
    print(f"    - Trạng thái tổng quát: {'PASS (100% Hợp quy)' if report.passed else 'FAIL'}")
    print(f"    - Rò rỉ mã LaTeX thô: {report.raw_latex_leaks_count}")
    print(f"    - Phân số gạch chéo /: {report.slash_fraction_count}")
    print(f"    - Biến ASCII gạch dưới thô: {report.raw_subscript_count}")

    assert report.passed, "[-] AST Linter Pre-check thất bại!"
    assert report.raw_latex_leaks_count == 0, f"[-] Phát hiện {report.raw_latex_leaks_count} mã LaTeX thô!"
    assert report.slash_fraction_count == 0, f"[-] Phát hiện {report.slash_fraction_count} phân số gạch chéo /!"
    assert report.raw_subscript_count == 0, f"[-] Phát hiện {report.raw_subscript_count} biến ASCII gạch dưới thô!"
    print("    [+] AST Linter Pre-check: ĐẠT CHUẨN TUYỆT ĐỐI.")

    # 2. Kiểm tra Serialization / Deserialization hai chiều (Lossless Round-trip)
    print(f"[*] Kiểm tra tệp xuất: {output_file}")
    assert os.path.exists(output_file), f"[-] Không tìm thấy tệp kết xuất: {output_file}"

    with open(output_file, "r", encoding="utf-8") as f:
        loaded_json = json.load(f)

    # Validate lại qua Pydantic
    re_validated = DraftPayload.model_validate(loaded_json)
    assert re_validated.section_id == payload.section_id, "[-] Sai lệch section_id sau round-trip!"
    assert len(re_validated.mpt_payloads) == len(payload.mpt_payloads), "[-] Sai lệch số MPT sau round-trip!"
    assert re_validated.cod_rounds_completed == payload.cod_rounds_completed, "[-] Sai lệch cod_rounds sau round-trip!"
    print("    [+] Lossless Round-trip Deserialization: ĐẠT CHUẨN 100%.")

    print("[+] KẾT QUẢ MIỀN 5: PASS 100% (Hợp đồng DraftPayload & Trạm 1 AST Linter).")


def main():
    start_time = time.time()
    print("=" * 80)
    print("  KỊCH BẢN DRY-RUN KIỂM ĐỊNH ĐỘC LẬP PHA 3 (pedagogical-author)")
    print("  Hệ thống AI Agent Giảng dạy & Chuyên khảo Vật lý Bán dẫn HUST")
    print("  Phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội)")
    print("=" * 80)

    bp_path = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
    mf_path = os.path.join(PROJECT_ROOT, "output", "manifests", "DRY_RUN_ASSET_MANIFEST_2_1.json")
    out_payload_path = os.path.join(PROJECT_ROOT, "output", "payloads", "DRY_RUN_DRAFT_PAYLOAD_2_1.json")

    print(f"[*] Nạp Blueprint: {bp_path}")
    print(f"[*] Nạp Manifest: {mf_path}")

    author = PedagogicalAuthor()
    author.load_inputs(bp_path, mf_path)

    # Sinh Payload với CoD >= 3
    payload = author.draft_section_payload(cod_rounds=3)
    author.export_payload_json(out_payload_path, payload)

    # Kiểm chứng 5 miền kỹ thuật
    verify_domain_1_ufme_five_stages(payload)
    verify_domain_2_malae_equation_dissection(payload)
    verify_domain_3_causal_flowchain(payload)
    verify_domain_4_five_link_ocr_and_cod(author, payload)
    verify_domain_5_draft_payload_and_ast_linter(payload, out_payload_path)

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"  TỔNG KẾT DRY-RUN PHA 3: TẤT CẢ 5 MIỀN KỸ THUẬT ĐẠT PASS 100%!")
    print(f"  Thời gian thực thi: {elapsed:.3f} giây | 0 ERRORS | 0 FAILURES")
    print("=" * 80)


if __name__ == "__main__":
    main()

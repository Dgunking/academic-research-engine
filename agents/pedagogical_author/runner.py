# -*- coding: utf-8 -*-
"""
CLI Runner độc lập cho Pedagogical Author Subagent (Agent 3 - pedagogical-author).
Cho phép Bùi Trung Dũng chạy tổng hợp bài giảng, nén CoD và xuất draft payload từ terminal/PowerShell.
"""

import os
import sys
import argparse
import json
from pathlib import Path

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
from agents.pedagogical_author.author import PedagogicalAuthor
from agents.schemas.blueprint import CurriculumBlueprint
from agents.schemas.manifest import VisualAssetManifest
from agents.schemas.payload import DraftPayload
from agents.common.linter import ASTLinter


def main():
    parser = argparse.ArgumentParser(
        description="CLI Runner cho Agent 3: Deep Pedagogical Author (pedagogical-author)"
    )
    parser.add_argument("--blueprint", type=str, default=None, help="Đường dẫn tệp BLUEPRINT_MUC_X.Y.json")
    parser.add_argument("--manifest", type=str, default=None, help="Đường dẫn tệp ASSET_MANIFEST.json")
    parser.add_argument("--cod-rounds", type=int, default=3, help="Số vòng lặp nén Chain-of-Density (tối thiểu 3)")
    parser.add_argument("--output", type=str, default=None, help="Đường dẫn xuất tệp DRAFT_PAYLOAD.json")
    parser.add_argument("--verify-only", type=str, default=None, help="Đường dẫn tệp DRAFT_PAYLOAD.json cần kiểm định")

    args = parser.parse_args()

    print("=" * 80)
    print("  KÍCH HOẠT CLI RUNNER: DEEP PEDAGOGICAL AUTHOR (AGENT 3 - pedagogical-author)")
    print(f"  Số vòng nén CoD: {args.cod_rounds} (quy chuẩn >= 3)")
    print("=" * 80)

    # 1. Chế độ kiểm định tệp DraftPayload có sẵn
    if args.verify_only:
        print(f"[*] Chế độ xác thực kiểm định: {args.verify_only}")
        try:
            with open(args.verify_only, "r", encoding="utf-8") as f:
                data = json.load(f)
            payload = DraftPayload.model_validate(data)
            print(f"[+] Schema validation: PASS (Phân mục: {payload.section_id})")
            print(f"[+] Số MPT đã triển khai: {len(payload.mpt_payloads)}")
            print(f"[+] Vòng nén CoD: {payload.cod_rounds_completed}")
            print(f"[+] AST Linter Pre-check: {'PASS' if payload.linter_pre_check.passed else 'FAIL'}")
            if not payload.linter_pre_check.passed:
                print(f"[-] Rò rỉ LaTeX thô: {payload.linter_pre_check.raw_latex_leaks_count}")
                print(f"[-] Phân số gạch chéo: {payload.linter_pre_check.slash_fraction_count}")
                print(f"[-] Biến ASCII gạch dưới: {payload.linter_pre_check.raw_subscript_count}")
                sys.exit(1)
            print("[+] Kết quả kiểm định toàn diện: PASS 100% HỢP QUY.")
            sys.exit(0)
        except Exception as e:
            print(f"[-] Kết quả kiểm định thất bại: {e}")
            sys.exit(1)

    # 2. Chế độ chấp bút từ Blueprint & Manifest
    if not args.blueprint:
        print("[-] Lỗi: Cần cung cấp --blueprint hoặc --verify-only.")
        sys.exit(1)

    author = PedagogicalAuthor()
    print(f"[*] Nạp Blueprint: {args.blueprint}")
    author.load_inputs(args.blueprint, args.manifest)

    if args.manifest:
        print(f"[*] Nạp Asset Manifest: {args.manifest}")

    print(f"[*] Khởi động động cơ sư phạm UFME 5 Giai đoạn & MALAE 3 Cấp...")
    payload = author.draft_section_payload(cod_rounds=args.cod_rounds)

    # Xác định đường dẫn xuất
    if args.output:
        out_path = Path(args.output)
    else:
        out_path = Path(PROJECT_ROOT) / "output" / "payloads" / f"DRAFT_PAYLOAD_{payload.section_id}.json"

    saved_file = author.export_payload_json(out_path, payload)

    print(f"[+] Hoàn tất chấp bút phân mục: {payload.section_id} - {payload.section_title}")
    print(f"[+] Tổng số MPT: {len(payload.mpt_payloads)}")
    for m in payload.mpt_payloads:
        print(f"    - [{m.mpt_id}] {m.mpt_title} | Neo: {m.visual_anchor_id} | Dẫn xuất: {len(m.stage_3_guided_derivation)} bước")
    print(f"[+] AST Linter Pre-check: {'PASS' if payload.linter_pre_check.passed else 'FAIL'}")
    print(f"[+] Hợp đồng Bản thảo Bài giảng Chi tiết: {saved_file}")
    sys.exit(0)


if __name__ == "__main__":
    main()

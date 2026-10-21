# -*- coding: utf-8 -*-
"""
CLI Runner độc lập cho Physical Simulation & Graphic Artist Subagent (Agent 2).
Cho phép Bùi Trung Dũng chạy mô phỏng, bóc tách ảnh và xuất manifest từ terminal/PowerShell.
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
from agents.physics_graphic_artist.artist import PhysicsGraphicArtist
from agents.schemas.blueprint import CurriculumBlueprint
from agents.schemas.manifest import VisualAssetManifest


def main():
    parser = argparse.ArgumentParser(
        description="CLI Runner cho Agent 2: Physical Simulation & Graphic Artist (physics-graphic-artist)"
    )
    parser.add_argument("--blueprint", type=str, default=None, help="Đường dẫn tệp BLUEPRINT_MUC_X.Y.json")
    parser.add_argument("--mpt", type=str, default=None, help="Mã MPT cụ thể (ví dụ: MPT_2_1_1)")
    parser.add_argument("--plot-type", type=str, choices=["structural", "performance", "dsafe"], default="structural",
                        help="Loại hình ảnh khi chạy đơn lẻ")
    parser.add_argument("--material", type=str, default="GaAs", help="Vật liệu bán dẫn (GaAs, InP, GaN, Si, Ge)")
    parser.add_argument("--temperature", type=float, default=300.0, help="Nhiệt độ vận hành [K]")
    parser.add_argument("--out-dir", type=str, default="output/figures", help="Thư mục xuất ảnh")
    parser.add_argument("--out-manifest", type=str, default="output/manifests/ASSET_MANIFEST.json", help="Đường dẫn file manifest JSON")
    parser.add_argument("--verify-only", type=str, default=None, help="Đường dẫn file manifest cần xác thực")

    args = parser.parse_args()

    artist = PhysicsGraphicArtist(
        output_dir=args.out_dir,
        manifest_dir=os.path.dirname(args.out_manifest) or "output/manifests"
    )

    print("=" * 80)
    print("  KÍCH HOẠT CLI RUNNER: PHYSICAL SIMULATION & GRAPHIC ARTIST (AGENT 2)")
    print(f"  Vật liệu: {args.material} | Nhiệt độ: {args.temperature:.1f} K | Thư mục: {args.out_dir}")
    print("=" * 80)

    # 1. Chế độ kiểm tra manifest có sẵn
    if args.verify_only:
        print(f"[*] Chế độ xác thực kiểm định: {args.verify_only}")
        try:
            valid = artist.verify_asset_manifest(args.verify_only)
            print("[+] Kết quả kiểm định: PASS 100% HỢP QUY.")
            sys.exit(0)
        except Exception as e:
            print(f"[-] Kết quả kiểm định: THẤT BẠI - {e}")
            sys.exit(1)

    # 2. Chế độ xử lý toàn trình từ CurriculumBlueprint
    if args.blueprint:
        print(f"[*] Đọc tệp CurriculumBlueprint: {args.blueprint}")
        with open(args.blueprint, "r", encoding="utf-8") as f:
            bp_data = json.load(f)
        blueprint = CurriculumBlueprint.model_validate(bp_data)
        manifest = artist.process_blueprint(blueprint)
        out_path = artist.export_manifest(manifest, args.out_manifest)
        print(f"[+] Hoàn tất xử lý Blueprint: {manifest.total_assets} tài nguyên đồ họa đã tạo.")
        print(f"[+] Hợp đồng Danh mục Tài nguyên: {out_path}")
        sys.exit(0)

    # 3. Chế độ sinh đơn lẻ theo tham số dòng lệnh
    mpt_id = args.mpt or "MPT_2_1_1"
    print(f"[*] Sinh đồ thị đơn lẻ: {args.plot_type} cho {mpt_id}")

    if args.plot_type == "structural":
        img_path, item = artist.generate_type1_structural_plot(
            mpt_id=mpt_id,
            material=args.material,
            T_K=args.temperature
        )
    elif args.plot_type == "performance":
        img_path, item = artist.generate_type2_performance_plot(
            mpt_id=mpt_id,
            material=args.material,
            T_K=args.temperature
        )
    elif args.plot_type == "dsafe":
        img_path, item = artist.auto_crop_dsafe_figure(
            input_image_path=os.path.join(args.out_dir, f"raw_{mpt_id}.png"),
            output_filename=f"Goc_{mpt_id}_DSAFE_Crop.png",
            pad_px=10,
            mpt_id=mpt_id
        )

    manifest = VisualAssetManifest(
        section_id="MUC_TEST",
        total_assets=1,
        assets=[item]
    )
    artist.export_manifest(manifest, args.out_manifest)
    print(f"[+] Đã tạo tệp ảnh: {img_path}")
    print(f"[+] Đã xuất manifest: {args.out_manifest}")


if __name__ == "__main__":
    main()

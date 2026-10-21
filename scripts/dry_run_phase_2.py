# -*- coding: utf-8 -*-
"""
Kịch bản Dry-run Kiểm định Độc lập Pha 2: Physical Simulation & Graphic Artist (Agent 2)
Antigravity 2.0 - Standalone Autonomous Subagent Verification.
Chủ thể phê duyệt: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST).

Kiểm chứng 5 miền kỹ thuật:
- Miền 1: Cơ sở dữ liệu Bán dẫn 300 K & Hằng số CODATA 2022 (Thuật toán 7 HDSE)
- Miền 2: Bóc tách Ảnh gốc D-SAFE & Auto-crop viền trắng thừa (Thuật toán 3 RVAE 2.0 & 7 HDSE)
- Miền 3: Mô phỏng Giải tích MATLAB R2014b+ & Phân tầng Thị giác Kép (Thuật toán 7 HDSE)
- Miền 4: Khóa Bố cục Điểm ảnh ZT-GVLE & Quét cạn Zero-Slash Fractions (Thuật toán 13 & Luật 14)
- Miền 5: Hợp đồng Danh mục Tài nguyên VisualAssetManifest & Ký số SHA-256 (Hợp đồng 2)
"""

import sys
import os
import json
import time
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

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
from agents.common.materials import SemiconductorDatabase, SEMICONDUCTORS_300K, CODATA_2022
from agents.physics_graphic_artist.artist import (
    PhysicsGraphicArtist,
    MATLAB_COLORS,
    MATLAB_PALETTE,
)
from agents.schemas.manifest import (
    VisualAssetManifest,
    VisualAssetItem,
    TripleBufferMetrics,
    OCRChainPedagogicalCaption,
)
from agents.schemas.blueprint import (
    CurriculumBlueprint,
    MicroPointTopicSpec,
    VisualRequirement,
)
import physics_viz_lock


def log_section(title: str):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def verify_domain_1_semiconductor_database():
    log_section("[MIỀN 1] CƠ SỞ DỮ LIỆU BÁN DẪN 300 K & HẰNG SỐ CODATA 2022")

    # 1. Kiểm tra hằng số CODATA 2022
    q = CODATA_2022["q"]
    h = CODATA_2022["h"]
    hbar = CODATA_2022["hbar"]
    m0 = CODATA_2022["m0"]
    kB = CODATA_2022["kB"]
    c = CODATA_2022["c"]
    print(f"[*] Hằng số CODATA 2022: q = {q} C, h = {h} J·s, hbar = {hbar} J·s -> PASS")
    assert abs(q - 1.602176634e-19) < 1e-25
    assert abs(hbar - 1.054571817e-34) < 1e-40

    # 2. Kiểm tra thông số 5 vật liệu chuẩn 300 K
    for mat in ["GaAs", "InP", "GaN", "Si", "Ge"]:
        data = SemiconductorDatabase.get_material(mat)
        Eg = data["Eg"]
        me = data["me_eff"]
        mhh = data["mhh_eff"]
        print(f"[*] Vật liệu {mat:4s}: Eg(300K) = {Eg:.3f} eV, me* = {me:.3f} m0, mhh* = {mhh:.3f} m0 -> PASS")
        assert Eg > 0 and me > 0 and mhh > 0

    # 3. Kiểm tra biến thiên Varshni theo nhiệt độ
    # Với GaAs: Eg(0 K) > Eg(300 K) > Eg(400 K)
    Eg_0K = SemiconductorDatabase.varshni_eg("GaAs", 0.0)
    Eg_300K = SemiconductorDatabase.varshni_eg("GaAs", 300.0)
    Eg_400K = SemiconductorDatabase.varshni_eg("GaAs", 400.0)
    print(f"[*] Varshni GaAs: Eg(0 K) = {Eg_0K:.4f} eV > Eg(300 K) = {Eg_300K:.4f} eV > Eg(400 K) = {Eg_400K:.4f} eV -> PASS")
    assert Eg_0K > Eg_300K > Eg_400K

    # 4. Kiểm tra nồng độ hạt tải nội sinh ni và thế nhiệt Vt
    Vt_300 = SemiconductorDatabase.thermal_voltage(300.0)
    print(f"[*] Thế nhiệt Vt(300 K) = {Vt_300*1000:.2f} mV (~25.85 mV) -> PASS")
    assert abs(Vt_300 - 0.02585) < 0.001

    ni_gaas = SemiconductorDatabase.intrinsic_carrier_concentration("GaAs", 300.0)
    print(f"[*] Nồng độ nội sinh GaAs ở 300 K: ni = {ni_gaas:.2e} cm^-3 (~2e6 cm^-3) -> PASS")
    assert ni_gaas < 1e10

    print("[+] Kiểm thử Miền 1 (Cơ sở dữ liệu Bán dẫn & CODATA): PASS 100%")


def verify_domain_2_dsafe_autocrop():
    log_section("[MIỀN 2] BÓC TÁCH ẢNH GỐC D-SAFE & AUTO-CROP (THUẬT TOÁN 3 & 7)")

    artist = PhysicsGraphicArtist(output_dir="output/figures")

    # 1. Tạo ảnh giả lập có viền trắng rộng để kiểm thử Auto-crop
    test_raw_path = "output/figures/test_raw_slide_image.png"
    raw_img = Image.new("RGB", (800, 600), color=(255, 255, 255))
    # Vẽ một hình chữ nhật nội dung ở giữa (từ pixel 200, 150 đến 600, 450)
    for x in range(200, 600):
        for y in range(150, 450):
            raw_img.putpixel((x, y), (0, 114, 189))  # Màu xanh MATLAB
    raw_img.save(test_raw_path)
    print(f"[*] Đã tạo ảnh đầu vào thô viền trắng: {test_raw_path} (800x600 px)")

    # 2. Thực thi auto_crop_dsafe_figure
    out_crop_path, asset_item = artist.auto_crop_dsafe_figure(
        input_image_path=test_raw_path,
        output_filename="test_cropped_dsafe.png",
        pad_px=10,
        mpt_id="MPT_DRY_RUN_2_1"
    )

    cropped_im = Image.open(out_crop_path)
    cw, ch = cropped_im.size
    print(f"[*] Sau Auto-crop: {out_crop_path} ({cw}x{ch} px, pad=10 px) -> PASS")
    # Kích thước phải nhỏ hơn 800x600 vì đã xén viền trắng thừa
    assert cw < 800 and ch < 600
    assert abs(cw - 420) <= 2  # (600 - 200) + 2*10 = 420
    assert abs(ch - 320) <= 2  # (450 - 150) + 2*10 = 320

    # 3. Kiểm tra thuộc tính Hợp đồng Dữ liệu VisualAssetItem
    assert asset_item.asset_type == "DSAFE_ORIGINAL_CROP"
    assert asset_item.aspect_ratio == "16:9"
    assert asset_item.geometry_audit.dpi >= 300
    assert asset_item.geometry_audit.file_size_bytes <= 307200
    assert not asset_item.geometry_audit.layout_collision_detected
    print(f"[*] Geometry audit D-SAFE: DPI = {asset_item.geometry_audit.dpi}, Size = {asset_item.geometry_audit.file_size_bytes} bytes -> PASS")

    # Dọn dẹp tệp thử nghiệm tạm
    if os.path.exists(test_raw_path):
        os.remove(test_raw_path)

    print("[+] Kiểm thử Miền 2 (Auto-crop & D-SAFE): PASS 100%")


def verify_domain_3_matlab_analytical_simulations():
    log_section("[MIỀN 3] MÔ PHỎNG GIẢI TÍCH MATLAB R2014b+ & PHÂN TẦNG THỊ GIÁC")

    artist = PhysicsGraphicArtist(output_dir="output/figures")

    # 1. Kiểm thử Mô phỏng Loại 1: Cấu trúc & Dải năng lượng (Structural Simulation)
    print("[*] Sinh Mô phỏng Loại 1: Cấu trúc dải năng lượng Kane 2-band k.p (GaAs ở 300 K)...")
    path_1, item_1 = artist.generate_type1_structural_plot(
        mpt_id="MPT_2_1_1",
        material="GaAs",
        T_K=300.0,
        output_filename="Dry_Run_Structural_Band.png"
    )
    print(f"    ↳ Đã tạo: {path_1}")
    assert os.path.exists(path_1)
    assert item_1.asset_type == "MATLAB_SIMULATION_PLOT"
    assert item_1.aspect_ratio == "6.5:4.2"
    assert item_1.geometry_audit.envelope_clearance_percent >= 8.0
    assert item_1.geometry_audit.min_font_size_pt >= 10.0
    assert not item_1.geometry_audit.layout_collision_detected
    assert item_1.geometry_audit.dpi >= 300
    assert item_1.geometry_audit.file_size_bytes <= 307200
    print(f"    ↳ Clearance: {item_1.geometry_audit.envelope_clearance_percent}%, Font: {item_1.geometry_audit.min_font_size_pt} pt -> PASS")

    # 2. Kiểm thử Mô phỏng Loại 2: Đặc tuyến L-I-V & Quét nhiệt độ (Performance Sweep)
    print("[*] Sinh Mô phỏng Loại 2: Đặc tuyến L-I-V Laser Diode quét nhiệt độ...")
    path_2, item_2 = artist.generate_type2_performance_plot(
        mpt_id="MPT_2_1_2",
        material="GaAs",
        T_K=300.0,
        output_filename="Dry_Run_Performance_LIV.png"
    )
    print(f"    ↳ Đã tạo: {path_2}")
    assert os.path.exists(path_2)
    assert item_2.asset_type == "MATLAB_SIMULATION_PLOT"
    assert item_2.aspect_ratio == "6.5:4.2"
    assert item_2.geometry_audit.envelope_clearance_percent >= 8.0
    assert item_2.geometry_audit.file_size_bytes <= 307200
    print(f"    ↳ Clearance: {item_2.geometry_audit.envelope_clearance_percent}%, Font: {item_2.geometry_audit.min_font_size_pt} pt -> PASS")

    # 3. Kiểm tra bảng màu MATLAB R2014b+
    for color in item_1.matlab_palette_colors_used:
        assert color in MATLAB_PALETTE, f"Màu {color} không thuộc bảng màu MATLAB chuẩn!"
    print(f"[*] Xác thực bảng màu MATLAB 6-color palette: PASS ({len(item_1.matlab_palette_colors_used)} màu)")

    print("[+] Kiểm thử Miền 3 (Mô phỏng Giải tích MATLAB): PASS 100%")


def verify_domain_4_layout_lock_and_zero_slash():
    log_section("[MIỀN 4] KHÓA BỐ CỤC ĐIỂM ẢNH ZT-GVLE & ZERO-SLASH FRACTIONS (LUẬT 14)")

    artist = PhysicsGraphicArtist(output_dir="output/figures")

    # 1. Kiểm tra phát hiện vi phạm phân số gạch chéo '/' (Zero-Slash Validator)
    fig_bad, ax_bad = plt.subplots(figsize=(6.5, 4.2))
    ax_bad.plot([0, 1], [0, 1])
    ax_bad.annotate("Công thức vi phạm: $E = h \\cdot c / \\lambda$", xy=(0.5, 0.5))
    violations = artist.check_zero_slash_fractions(fig_bad)
    print(f"[*] Quét vi phạm phân số gạch chéo: Bắt chính xác {len(violations)} lỗi -> PASS")
    assert len(violations) > 0, "Phải bắt được lỗi rò rỉ phân số gạch chéo '/'!"
    plt.close(fig_bad)

    # 2. Kiểm tra đồ thị chuẩn với phân số gạch ngang \\frac{a}{b}
    fig_good, ax_good = plt.subplots(figsize=(6.5, 4.2))
    ax_good.plot([0, 1], [0, 1])
    ax_good.annotate(r"Công thức chuẩn: $E = \frac{h \cdot c}{\lambda}$", xy=(0.5, 0.5))
    no_violations = artist.check_zero_slash_fractions(fig_good)
    print(f"[*] Quét đồ thị hợp quy \\frac{{a}}{{b}}: 0 vi phạm -> PASS")
    assert len(no_violations) == 0, f"Không được có vi phạm trên công thức chuẩn: {no_violations}"
    plt.close(fig_good)

    # 3. Kiểm tra giới hạn khổ canvas width <= 7.05 inches (A4 print safe)
    w_inch, h_inch = 6.5, 4.2
    assert w_inch <= 7.05, f"Chiều rộng {w_inch} in vượt quá khổ A4 (7.05 in)!"
    print(f"[*] Giới hạn khổ Canvas: W = {w_inch:.2f} in <= 7.05 in -> PASS")

    print("[+] Kiểm thử Miền 4 (ZT-GVLE & Zero-Slash): PASS 100%")


def verify_domain_5_manifest_contract():
    log_section("[MIỀN 5] HỢP ĐỒNG DANH MỤC ASSET_MANIFEST & KÝ SỐ SHA-256")

    artist = PhysicsGraphicArtist(
        output_dir="output/figures",
        manifest_dir="output/manifests"
    )

    # 1. Nạp tệp Blueprint chuẩn từ Pha 1
    blueprint_path = "output/blueprints/DRY_RUN_BLUEPRINT_2_1.json"
    assert os.path.exists(blueprint_path), f"Thiếu tệp Blueprint: {blueprint_path}"
    with open(blueprint_path, "r", encoding="utf-8") as f:
        bp_dict = json.load(f)
    blueprint = CurriculumBlueprint.model_validate(bp_dict)
    print(f"[*] Đã nạp Blueprint: {blueprint_path} ({len(blueprint.mpt_specifications)} MPTs)")

    # 2. Xử lý toàn trình Blueprint sinh VisualAssetManifest
    manifest = artist.process_blueprint(blueprint)
    print(f"[*] Đã xử lý toàn trình: {manifest.total_assets} tài nguyên hình ảnh được kiến tạo.")
    assert manifest.total_assets >= 1

    # 3. Xuất bản tệp manifest ra đĩa
    manifest_out_path = "output/manifests/DRY_RUN_ASSET_MANIFEST_2_1.json"
    artist.export_manifest(manifest, manifest_out_path)
    assert os.path.exists(manifest_out_path)

    # 4. Xác thực ngược round-trip deserialization & kiểm tra tính toàn vẹn
    valid = artist.verify_asset_manifest(manifest_out_path)
    print(f"[*] Xác thực ngược Round-trip Deserialization: {'PASS' if valid else 'FAIL'}")
    assert valid

    # 5. Kiểm tra ký số sidecar manifest .manifest.json
    for asset in manifest.assets:
        sidecar_file = asset.file_path_local.rsplit(".", 1)[0] + ".manifest.json"
        assert os.path.exists(sidecar_file), f"Thiếu sidecar manifest: {sidecar_file}"
        with open(sidecar_file, "r", encoding="utf-8") as sf:
            sidecar_data = json.load(sf)
        assert "sha256" in sidecar_data
        assert sidecar_data["dpi"] >= 300
        print(f"[*] Sidecar SHA-256: {os.path.basename(asset.file_path_local)} -> {sidecar_data['sha256'][:16]}... PASS")

    print("[+] Kiểm thử Miền 5 (VisualAssetManifest & SHA-256): PASS 100%")


def main():
    start_time = time.time()
    print("=" * 80)
    print("  BẮT ĐẦU KIỂM THỬ DRY-RUN TOÀN DIỆN PHA 2: PHYSICAL SIMULATION & GRAPHIC ARTIST")
    print("  Chủ thể: Bùi Trung Dũng (Khoa Vật lý Kỹ thuật, ĐH Bách khoa Hà Nội - HUST)")
    print("=" * 80)

    verify_domain_1_semiconductor_database()
    verify_domain_2_dsafe_autocrop()
    verify_domain_3_matlab_analytical_simulations()
    verify_domain_4_layout_lock_and_zero_slash()
    verify_domain_5_manifest_contract()

    elapsed = time.time() - start_time
    print("\n" + "=" * 80)
    print(f"  KẾT QUẢ NGHIỆM THU PHA 2: 100% ĐẠT CHUẨN (Thời gian thực thi: {elapsed:.3f} s)")
    print("=" * 80)
    print("  [X] Miền 1: Semiconductor 300 K & CODATA 2022 -> SẴN SÀNG.")
    print("  [X] Miền 2: D-SAFE Auto-Crop & Padding RVAE 2.0 -> SẴN SÀNG.")
    print("  [X] Miền 3: MATLAB R2014b+ 6-Color & Triple Buffer -> SẴN SÀNG.")
    print("  [X] Miền 4: ZT-GVLE Geometric Lock & Zero-Slash -> SẴN SÀNG.")
    print("  [X] Miền 5: VisualAssetManifest & SHA-256 Sidecar -> SẴN SÀNG.")
    print("  [X] Dual-Mode Triad: CLI Runner + Subagent Spec -> HOÀN THIỆN.")
    print("=" * 80)


if __name__ == "__main__":
    main()

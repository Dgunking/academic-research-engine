# -*- coding: utf-8 -*-
"""
tests/test_phase_2.py — Bộ Kiểm Thử Đơn Vị Toàn Diện Cho Pha 2 (Agent 2)
Kiểm thử tự động cho Physical Simulation & Graphic Artist Subagent (physics-graphic-artist).
Chủ thể: Lead Researcher ().
"""

import os
import sys
import json
import math
import hashlib
import unittest

# Cấu hình UTF-8 cho Windows console khi chạy qua python -m unittest
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

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


class TestPhase2PhysicalSimulationAndGraphicArtist(unittest.TestCase):
    """Bộ kiểm thử đơn vị cho Agent 2: Physical Simulation & Graphic Artist."""

    @classmethod
    def setUpClass(cls):
        cls.test_output_dir = os.path.join(PROJECT_ROOT, "output", "test_phase_2_tmp")
        cls.test_manifest_dir = os.path.join(cls.test_output_dir, "manifests")
        os.makedirs(cls.test_output_dir, exist_ok=True)
        os.makedirs(cls.test_manifest_dir, exist_ok=True)
        cls.artist = PhysicsGraphicArtist(
            output_dir=cls.test_output_dir,
            manifest_dir=cls.test_manifest_dir,
            dpi=300,
            max_file_size_bytes=307200
        )

    @classmethod
    def tearDownClass(cls):
        import shutil
        if os.path.exists(cls.test_output_dir):
            shutil.rmtree(cls.test_output_dir, ignore_errors=True)

    def test_01_semiconductor_database_and_codata(self):
        """Kiểm tra hằng số CODATA 2022 và thông số 5 vật liệu bán dẫn ở 300 K."""
        self.assertAlmostEqual(CODATA_2022["q"], 1.602176634e-19, delta=1e-25)
        self.assertAlmostEqual(CODATA_2022["h"], 6.62607015e-34, delta=1e-40)
        self.assertAlmostEqual(CODATA_2022["hbar"], 1.054571817e-34, delta=1e-40)

        for mat in ["GaAs", "InP", "GaN", "Si", "Ge"]:
            data = SemiconductorDatabase.get_material(mat)
            self.assertIn("Eg", data)
            self.assertIn("me_eff", data)
            self.assertIn("mhh_eff", data)
            self.assertGreater(data["Eg"], 0.0)

        # Mô hình Varshni: Eg phải giảm đơn điệu theo nhiệt độ T
        Eg_0 = SemiconductorDatabase.varshni_eg("GaAs", 0.0)
        Eg_300 = SemiconductorDatabase.varshni_eg("GaAs", 300.0)
        Eg_400 = SemiconductorDatabase.varshni_eg("GaAs", 400.0)
        self.assertGreater(Eg_0, Eg_300)
        self.assertGreater(Eg_300, Eg_400)

        # Thế nhiệt Vt ở 300 K ~ 25.85 mV
        Vt = SemiconductorDatabase.thermal_voltage(300.0)
        self.assertAlmostEqual(Vt, 0.02585, delta=1e-4)

    def test_02_effective_density_of_states_and_ni(self):
        """Kiểm tra tính toán Nc, Nv và nồng độ hạt tải nội sinh ni."""
        mat = SemiconductorDatabase.get_material("GaAs")
        Nc = SemiconductorDatabase.effective_density_of_states(mat["me_eff"], 300.0)
        Nv = SemiconductorDatabase.effective_density_of_states(mat["mhh_eff"], 300.0)
        self.assertGreater(Nc, 1e16)
        self.assertGreater(Nv, 1e18)

        ni = SemiconductorDatabase.intrinsic_carrier_concentration("GaAs", 300.0)
        self.assertGreater(ni, 1e5)
        self.assertLess(ni, 1e8)

    def test_03_photon_energy_to_wavelength(self):
        """Kiểm tra chuyển đổi năng lượng photon sang bước sóng lambda = hc/E."""
        # Với GaAs ở 300 K (Eg = 1.424 eV), bước sóng phát xạ ~ 870.7 nm
        lambda_nm = SemiconductorDatabase.photon_energy_to_wavelength_nm(1.424)
        self.assertAlmostEqual(lambda_nm, 870.675, delta=0.5)

        with self.assertRaises(ValueError):
            SemiconductorDatabase.photon_energy_to_wavelength_nm(-1.0)

    def test_04_matlab_style_and_palette(self):
        """Kiểm tra bảng 6 màu MATLAB R2014b+ chuẩn mực."""
        expected_colors = ["#0072BD", "#D95319", "#EDB120", "#7E2F8E", "#77AC30", "#7F7F7F"]
        for col in expected_colors:
            self.assertIn(col, MATLAB_PALETTE)
        self.assertEqual(len(MATLAB_PALETTE), 6)

    def test_05_zero_slash_fractions_detection(self):
        """Kiểm tra quét cạn phát hiện vi phạm phân số gạch chéo '/' (Luật 14)."""
        fig_viol, ax_viol = plt.subplots()
        ax_viol.annotate("Lỗi: $y = 1 / x$", xy=(0.5, 0.5))
        violations = self.artist.check_zero_slash_fractions(fig_viol)
        self.assertGreater(len(violations), 0)
        plt.close(fig_viol)

        fig_clean, ax_clean = plt.subplots()
        ax_clean.annotate(r"Hợp quy: $y = \frac{1}{x}$", xy=(0.5, 0.5))
        no_violations = self.artist.check_zero_slash_fractions(fig_clean)
        self.assertEqual(len(no_violations), 0)
        plt.close(fig_clean)

    def test_06_canvas_width_restriction(self):
        """Kiểm tra khóa cứng chiều rộng canvas <= 7.05 inches (vùng in A4 an toàn)."""
        fig_wide, ax_wide = plt.subplots(figsize=(8.0, 4.0))
        ax_wide.plot([0, 1], [0, 1])
        wide_path = os.path.join(self.test_output_dir, "wide_fail.png")

        with self.assertRaises(AssertionError) as ctx:
            physics_viz_lock.export_with_sidecar_manifest(fig_wide, wide_path)
        self.assertIn("CANVAS WIDTH VIOLATION", str(ctx.exception))
        plt.close(fig_wide)

    def test_07_autocrop_padding_and_dsafe(self):
        """Kiểm tra thuật toán Auto-crop xén viền trắng với padding an toàn."""
        raw_test_file = os.path.join(self.test_output_dir, "synthetic_raw.png")
        img = Image.new("RGB", (600, 400), color=(255, 255, 255))
        for x in range(150, 450):
            for y in range(100, 300):
                img.putpixel((x, y), (0, 114, 189))
        img.save(raw_test_file)

        out_cropped, asset_item = self.artist.auto_crop_dsafe_figure(
            input_image_path=raw_test_file,
            output_filename="synthetic_cropped.png",
            pad_px=10,
            mpt_id="MPT_TEST_CROP"
        )

        with Image.open(out_cropped) as c_img:
            cw, ch = c_img.size
            # Kích thước ban đầu 300x200 + 2*10 padding = 320x220
            self.assertAlmostEqual(cw, 320, delta=2)
            self.assertAlmostEqual(ch, 220, delta=2)
        self.assertEqual(asset_item.asset_type, "DSAFE_ORIGINAL_CROP")
        self.assertEqual(asset_item.aspect_ratio, "16:9")

        if os.path.exists(raw_test_file):
            os.remove(raw_test_file)

    def test_08_type1_structural_plot_generation(self):
        """Kiểm tra sinh mô phỏng Loại 1: Cấu trúc dải năng lượng Kane 2-band."""
        png_path, item = self.artist.generate_type1_structural_plot(
            mpt_id="MPT_TEST_1",
            material="GaAs",
            T_K=300.0,
            output_filename="Test_Structural_Band.png"
        )
        self.assertTrue(os.path.exists(png_path))
        self.assertEqual(item.asset_type, "MATLAB_SIMULATION_PLOT")
        self.assertEqual(item.aspect_ratio, "6.5:4.2")
        self.assertGreaterEqual(item.geometry_audit.envelope_clearance_percent, 8.0)
        self.assertGreaterEqual(item.geometry_audit.min_font_size_pt, 10.0)
        self.assertFalse(item.geometry_audit.layout_collision_detected)
        self.assertGreaterEqual(item.geometry_audit.dpi, 300)
        self.assertLessEqual(item.geometry_audit.file_size_bytes, 307200)

        # Kiểm tra sự tồn tại của sidecar manifest
        sidecar = png_path.rsplit(".", 1)[0] + ".manifest.json"
        self.assertTrue(os.path.exists(sidecar))

    def test_09_type2_performance_plot_generation(self):
        """Kiểm tra sinh mô phỏng Loại 2: Đặc tuyến L-I-V Laser Diode quét nhiệt độ."""
        png_path, item = self.artist.generate_type2_performance_plot(
            mpt_id="MPT_TEST_2",
            material="GaAs",
            T_K=300.0,
            output_filename="Test_Performance_LIV.png"
        )
        self.assertTrue(os.path.exists(png_path))
        self.assertEqual(item.asset_type, "MATLAB_SIMULATION_PLOT")
        self.assertEqual(item.aspect_ratio, "6.5:4.2")
        self.assertGreaterEqual(item.geometry_audit.envelope_clearance_percent, 8.0)
        self.assertGreaterEqual(item.geometry_audit.min_font_size_pt, 10.0)
        self.assertFalse(item.geometry_audit.layout_collision_detected)
        self.assertLessEqual(item.geometry_audit.file_size_bytes, 307200)

        sidecar = png_path.rsplit(".", 1)[0] + ".manifest.json"
        self.assertTrue(os.path.exists(sidecar))

    def test_10_triple_buffer_metrics_validation(self):
        """Kiểm tra ràng buộc Pydantic cứng trên TripleBufferMetrics."""
        # 1. Hợp quy
        valid = TripleBufferMetrics(
            envelope_clearance_percent=8.5,
            min_font_size_pt=10.0,
            layout_collision_detected=False,
            dpi=300,
            file_size_bytes=200000
        )
        self.assertEqual(valid.envelope_clearance_percent, 8.5)

        # 2. Vi phạm clearance < 8.0%
        with self.assertRaises(Exception):
            TripleBufferMetrics(
                envelope_clearance_percent=7.9,
                min_font_size_pt=10.0,
                layout_collision_detected=False,
                dpi=300,
                file_size_bytes=200000
            )

        # 3. Vi phạm font size < 10.0 pt
        with self.assertRaises(Exception):
            TripleBufferMetrics(
                envelope_clearance_percent=8.5,
                min_font_size_pt=9.5,
                layout_collision_detected=False,
                dpi=300,
                file_size_bytes=200000
            )

        # 4. Vi phạm dung lượng > 300 KB (307,200 bytes)
        with self.assertRaises(Exception):
            TripleBufferMetrics(
                envelope_clearance_percent=8.5,
                min_font_size_pt=10.0,
                layout_collision_detected=False,
                dpi=300,
                file_size_bytes=307201
            )

    def test_11_ocr_5chain_caption_validation(self):
        """Kiểm tra giải trình đầy đủ 5 Mắt xích OCR Pedagogical Caption."""
        caption = OCRChainPedagogicalCaption(
            chain_1_origin="Nguồn gốc mô phỏng giải tích 300 K.",
            chain_2_physical_feature="Cơ chế tái hợp bức xạ hạt tải vi mô.",
            chain_3_mathematical_link=r"Phương trình cột trụ $E(k)$.",
            chain_4_threshold_inflection="Điểm uốn chuyển pha tại dòng ngưỡng.",
            chain_5_engineering_insight="Ý nghĩa thực tế chế tạo diode bán dẫn."
        )
        self.assertTrue(caption.chain_1_origin)
        self.assertTrue(caption.chain_2_physical_feature)
        self.assertTrue(caption.chain_3_mathematical_link)
        self.assertTrue(caption.chain_4_threshold_inflection)
        self.assertTrue(caption.chain_5_engineering_insight)

    def test_12_process_blueprint_end_to_end(self):
        """Kiểm tra xử lý toàn trình từ CurriculumBlueprint sang VisualAssetManifest."""
        blueprint_file = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        self.assertTrue(os.path.exists(blueprint_file))

        with open(blueprint_file, "r", encoding="utf-8") as f:
            bp_data = json.load(f)
        blueprint = CurriculumBlueprint.model_validate(bp_data)

        manifest = self.artist.process_blueprint(blueprint)
        self.assertEqual(manifest.section_id, "MUC_2_1")
        self.assertEqual(manifest.total_assets, len(manifest.assets))
        self.assertGreaterEqual(manifest.total_assets, 1)

    def test_13_manifest_export_and_roundtrip_verification(self):
        """Kiểm tra xuất bản manifest ra đĩa và xác thực ngược round-trip."""
        blueprint_file = os.path.join(PROJECT_ROOT, "output", "blueprints", "DRY_RUN_BLUEPRINT_2_1.json")
        with open(blueprint_file, "r", encoding="utf-8") as f:
            bp_data = json.load(f)
        blueprint = CurriculumBlueprint.model_validate(bp_data)

        manifest = self.artist.process_blueprint(blueprint)
        out_manifest_path = os.path.join(self.test_manifest_dir, "ROUNDTRIP_ASSET_MANIFEST.json")
        self.artist.export_manifest(manifest, out_manifest_path)

        self.assertTrue(os.path.exists(out_manifest_path))
        valid = self.artist.verify_asset_manifest(out_manifest_path)
        self.assertTrue(valid)

    def test_14_sidecar_sha256_cryptographic_integrity(self):
        """Kiểm tra tính toàn vẹn mật mã SHA-256 giữa sidecar manifest và tệp ảnh thực tế."""
        _, item = self.artist.generate_type1_structural_plot(
            mpt_id="MPT_SHA_TEST",
            material="GaAs",
            T_K=300.0,
            output_filename="Sha_Test_Image.png"
        )
        png_path = item.file_path_local
        sidecar_path = png_path.rsplit(".", 1)[0] + ".manifest.json"
        self.assertTrue(os.path.exists(sidecar_path))

        with open(sidecar_path, "r", encoding="utf-8") as sf:
            sidecar_data = json.load(sf)

        with open(png_path, "rb") as f:
            actual_sha256 = hashlib.sha256(f.read()).hexdigest()

        self.assertEqual(sidecar_data["sha256"], actual_sha256)

    def test_15_file_size_upper_bound_300kb(self):
        """Kiểm tra bảo đảm dung lượng mọi tệp hình ảnh không bao giờ vượt quá 300 KB."""
        for filename in os.listdir(self.test_output_dir):
            if filename.endswith(".png"):
                full_path = os.path.join(self.test_output_dir, filename)
                size_bytes = os.path.getsize(full_path)
                self.assertLessEqual(
                    size_bytes, 307200,
                    f"Tệp {filename} có dung lượng {size_bytes} bytes > 307,200 bytes (300 KB)!"
                )


if __name__ == "__main__":
    unittest.main()

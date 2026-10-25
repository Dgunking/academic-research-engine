# -*- coding: utf-8 -*-
"""
Hợp đồng Dữ liệu 2: VisualAssetManifest (ASSET_MANIFEST.json)
Sinh ra bởi: physics-graphic-artist (Thuật toán 3, 7, 13, 10)
Tiêu thụ bởi: pedagogical-author, quality-gatekeeper.
"""

from typing import List, Dict, Optional, Literal
import pydantic


class TripleBufferMetrics(pydantic.BaseModel):
    """Số liệu kiểm định Hình học Đồ thị Triple Buffer Envelope (HDSE & ZT-GVLE)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    envelope_clearance_percent: float = pydantic.Field(
        ge=8.0,
        description="Khoảng đệm an toàn delta_geom >= 8.0% cách tuyệt đối mọi nét vẽ"
    )
    min_font_size_pt: float = pydantic.Field(
        ge=10.0,
        description="Kích thước font chữ nhỏ nhất trên đồ thị >= 10.0 pt"
    )
    layout_collision_detected: bool = pydantic.Field(
        default=False,
        description="Phát hiện va chạm nhãn hoặc nét vẽ (False là hợp lệ)"
    )
    dpi: int = pydantic.Field(
        ge=300,
        description="Độ phân giải hình ảnh xuất bản >= 300 DPI"
    )
    file_size_bytes: int = pydantic.Field(
        le=307200,
        description="Dung lượng tệp ảnh <= 300 KB (307,200 bytes)"
    )


class OCRChainPedagogicalCaption(pydantic.BaseModel):
    """Giải trình 5 Mắt xích OCR bảo toàn ký hiệu quang học và bản chất vật lý vi mô."""
    model_config = pydantic.ConfigDict(extra="forbid")

    chain_1_origin: str = pydantic.Field(
        description="Mắt xích 1: Nguồn gốc và bối cảnh trích xuất/mô phỏng"
    )
    chain_2_physical_feature: str = pydantic.Field(
        description="Mắt xích 2: Xu hướng biến thiên và cơ chế lực vi mô"
    )
    chain_3_mathematical_link: str = pydantic.Field(
        description="Mắt xích 3: Liên hệ trực tiếp với phương trình cột trụ"
    )
    chain_4_threshold_inflection: str = pydantic.Field(
        description="Mắt xích 4: Điểm ngưỡng, điểm uốn hoặc tiệm cận"
    )
    chain_5_engineering_insight: str = pydantic.Field(
        description="Mắt xích 5: Ý nghĩa thực tiễn chế tạo linh kiện"
    )


class VisualAssetItem(pydantic.BaseModel):
    """Một thực thể tài nguyên hình ảnh hoặc đồ thị hoàn chỉnh."""
    model_config = pydantic.ConfigDict(extra="forbid")

    asset_id: str = pydantic.Field(description="Mã định danh duy nhất (ví dụ: FIG_2_1_1)")
    mpt_reference_id: str = pydantic.Field(description="Mã MPT tham chiếu trực tiếp (ví dụ: MPT_2_1_1)")
    asset_type: Literal["MATLAB_SIMULATION_PLOT", "DSAFE_ORIGINAL_CROP", "SCHEMATIC_VECTOR_DIAGRAM"] = pydantic.Field(
        description="Loại tài nguyên hình ảnh"
    )
    file_path_local: str = pydantic.Field(description="Đường dẫn tệp ảnh cục bộ")
    aspect_ratio: Literal["16:9", "6.5:4.2"] = pydantic.Field(
        description="Tỷ lệ khung hình chuẩn hóa: 16:9 cho sơ đồ/ảnh gốc, 6.5:4.2 cho đồ thị MATLAB"
    )
    matlab_palette_colors_used: List[str] = pydantic.Field(
        description="Danh sách mã màu hex đã sử dụng tuân thủ bảng màu MATLAB chuẩn"
    )
    geometry_audit: TripleBufferMetrics = pydantic.Field(
        description="Số liệu đo đạc kiểm định hình học và bộ nhớ đệm"
    )
    pedagogical_caption: OCRChainPedagogicalCaption = pydantic.Field(
        description="Giải trình 5 Mắt xích OCR hoàn chỉnh"
    )
    semiconductor_parameters: Optional[Dict[str, float]] = pydantic.Field(
        default=None,
        description="Thông số vật liệu 300 K và hằng số CODATA áp dụng"
    )
    ground_truth_ref: Optional[str] = pydantic.Field(
        default=None,
        description="Mã định danh thực thể nguồn trong Ground Truth Manifest (ví dụ: GT_SCHEME_1, GT_FIG_1_A)"
    )


class VisualAssetManifest(pydantic.BaseModel):
    """Hợp đồng Danh mục Tài nguyên Hình ảnh (Visual Asset Manifest Contract)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    section_id: str = pydantic.Field(description="Mã phân mục bài giảng (ví dụ: MUC_2_1)")
    total_assets: int = pydantic.Field(ge=0, description="Tổng số lượng tài nguyên hình ảnh")
    assets: List[VisualAssetItem] = pydantic.Field(
        default_factory=list,
        description="Danh sách chi tiết các tài nguyên hình ảnh đã kiểm định"
    )
    ground_truth_manifest_path: Optional[str] = pydantic.Field(
        default=None,
        description="Đường dẫn đến tệp GROUND_TRUTH_MANIFEST.json đối chiếu chéo"
    )

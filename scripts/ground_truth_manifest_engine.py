# -*- coding: utf-8 -*-
"""
scripts/ground_truth_manifest_engine.py — Động Cơ Quét Tất Định DOM PyMuPDF Trích Xuất Ground Truth
Antigravity 2.0 - Standalone Autonomous Ground Truth Manifest Engine
Chủ thể phê duyệt: Lead Researcher ().

Mục tiêu tối thượng:
- Phân tích cây đối tượng DOM, image xrefs và text blocks của tài liệu gốc (PDF).
- Nhận diện tất định: Scheme, Figure, Sub-panel (a, b, c, d), Table.
- Trích xuất mã băm SHA-256 của stream ảnh gốc và tọa độ hộp bao (Bounding Box).
- Xuất bản hợp đồng dữ liệu chuẩn Pydantic: GroundTruthManifest (GROUND_TRUTH_MANIFEST.json).
"""

import os
import sys
import re
import json
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Tuple, Literal, Any
import pydantic

try:
    import pymupdf
    fitz = pymupdf
except ImportError:
    import fitz


# ===========================================================================
# 1. Hợp đồng Dữ liệu Pydantic (Data Contract Schemas)
# ===========================================================================

class GroundTruthEntity(pydantic.BaseModel):
    """Một thực thể hình ảnh / sơ đồ / bảng biểu bóc tách tất định từ DOM tài liệu gốc."""
    model_config = pydantic.ConfigDict(extra="ignore")

    entity_id: str = pydantic.Field(
        description="Mã định danh duy nhất (ví dụ: GT_SCHEME_1, GT_FIG_1_A, GT_FIG_1_B)"
    )
    entity_type: Literal["FIGURE", "SCHEME", "TABLE", "SUB_PANEL", "COMPOSITE_FIGURE"] = pydantic.Field(
        description="Chủng loại thực thể trong tài liệu gốc"
    )
    parent_id: Optional[str] = pydantic.Field(
        default=None,
        description="Mã định danh của thực thể mẹ nếu là sub-panel (ví dụ: GT_FIG_1 cho GT_FIG_1_A)"
    )
    page_number: int = pydantic.Field(
        ge=1,
        description="Số trang trong tài liệu gốc (bắt đầu từ 1)"
    )
    bbox: List[float] = pydantic.Field(
        description="Tọa độ hộp bao [x0, y0, x1, y1] theo hệ tọa độ trang PyMuPDF (points)"
    )
    caption_text: str = pydantic.Field(
        description="Đoạn văn bản chú thích liền kề bóc tách từ text blocks"
    )
    label_extracted: str = pydantic.Field(
        description="Nhãn trích xuất chính thức (ví dụ: 'Scheme 1', 'Figure 1(a)', 'Fig. 1b')"
    )
    image_xref: Optional[int] = pydantic.Field(
        default=None,
        description="Số hiệu xref của raster image trong PDF (nếu là ảnh bitmap)"
    )
    is_vector: bool = pydantic.Field(
        default=False,
        description="Đánh dấu nếu đối tượng được vẽ bằng đồ họa vector (đường nét, path)"
    )
    sha256_hash: Optional[str] = pydantic.Field(
        default=None,
        description="Mã băm SHA-256 của stream ảnh trích xuất trực tiếp từ PDF"
    )


class GroundTruthManifest(pydantic.BaseModel):
    """Hợp đồng Danh mục Thực thể Nguồn Tất định (Ground Truth Manifest Contract)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    source_document_path: str = pydantic.Field(
        description="Đường dẫn tuyệt đối hoặc tương đối tới tệp PDF tài liệu gốc"
    )
    section_id: Optional[str] = pydantic.Field(
        default=None,
        description="Mã phân mục bài giảng liên kết (ví dụ: MUC_3_1)"
    )
    total_entities: int = pydantic.Field(
        ge=0,
        description="Tổng số lượng thực thể đồ họa bóc tách được từ tài liệu gốc"
    )
    entities: List[GroundTruthEntity] = pydantic.Field(
        default_factory=list,
        description="Danh sách chi tiết các thực thể Ground Truth"
    )
    scan_timestamp: str = pydantic.Field(
        description="Thời điểm quét DOM theo chuẩn ISO 8601"
    )
    scanner_version: str = pydantic.Field(
        default="1.0.0-pymupdf-dom",
        description="Phiên bản của động cơ quét"
    )

    def export_json(self, output_path: str) -> str:
        """Xuất bản hợp đồng ra tệp tin JSON với mã hóa UTF-8."""
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(self.model_dump_json(indent=2))
        return output_path

    @classmethod
    def load_json(cls, input_path: str) -> "GroundTruthManifest":
        """Nạp và kiểm thực hợp đồng từ tệp JSON."""
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.model_validate(data)


# ===========================================================================
# 2. Động Cơ Quét Tất Định PyMuPDF DOM (GroundTruthManifestEngine)
# ===========================================================================

class GroundTruthManifestEngine:
    """
    Động cơ phân tích cú pháp DOM tài liệu gốc sử dụng PyMuPDF.
    Phát hiện Schemes, Figures, Sub-panels qua heuristics không gian và Regex.
    """

    RE_SCHEME = re.compile(r"^\s*(?:Scheme|Sơ đồ)\s*(\d+[a-zA-Z]?)[\.:\s]", re.I)
    RE_FIGURE = re.compile(r"^\s*(?:Fig(?:ure|\.)?|Hình)\s*(\d+[a-zA-Z]?(?:[-–]\d+)?)[\.:\s]", re.I)
    RE_TABLE = re.compile(r"^\s*(?:Table|Bảng)\s*(\d+[a-zA-Z]?)[\.:\s]", re.I)

    @classmethod
    def extract_sub_panels(cls, text: str) -> List[Tuple[str, str]]:
        """
        Trích xuất các sub-panels (a, b, c, d, e, f, g...) từ đoạn văn bản chú thích figure.
        Hỗ trợ các định dạng: (a) ..., (b) ... hoặc a. ..., b. ...
        """
        pattern = re.compile(r"(?:\(([a-z])\)|\b([a-z])\.)\s*([^();\n]+)", re.I)
        matches = pattern.findall(text)
        sub_panels = []
        for m in matches:
            label = (m[0] or m[1]).strip().lower()
            desc = m[2].strip()
            desc = re.sub(r"\s+(?:and|và|or|hoặc)\s*$", "", desc, flags=re.I).strip()
            if label:
                sub_panels.append((label, desc))
        return sub_panels

    def __init__(self, pdf_path: str):
        self.pdf_path = os.path.abspath(pdf_path)
        if not os.path.exists(self.pdf_path):
            raise FileNotFoundError(f"Không tìm thấy tài liệu gốc tại: {self.pdf_path}")

    def scan_document(
        self,
        section_id: Optional[str] = None,
        page_range: Optional[Tuple[int, int]] = None,
    ) -> GroundTruthManifest:
        """
        Quét cây đối tượng DOM trên dải trang chỉ định và trích xuất danh mục thực thể.
        """
        doc = fitz.open(self.pdf_path)
        entities: List[GroundTruthEntity] = []
        seen_entity_ids = set()

        total_pages = len(doc)
        start_page = 1
        end_page = total_pages

        if page_range:
            start_page = max(1, page_range[0])
            end_page = min(total_pages, page_range[1])

        for page_idx in range(start_page - 1, end_page):
            page_num = page_idx + 1
            page = doc[page_idx]

            # 1. Trích xuất danh sách raster images và xrefs trên trang
            page_images = []
            for img_info in page.get_images(full=True):
                xref = img_info[0]
                rects = page.get_image_rects(xref)
                sha256_hash = None
                try:
                    base_img = doc.extract_image(xref)
                    if base_img and "image" in base_img:
                        sha256_hash = hashlib.sha256(base_img["image"]).hexdigest()
                except Exception:
                    pass

                for r in rects:
                    page_images.append({
                        "xref": xref,
                        "rect": [r.x0, r.y0, r.x1, r.y1],
                        "sha256": sha256_hash,
                    })

            # 2. Trích xuất các khối văn bản (text blocks)
            blocks = page.get_text("blocks")
            # blocks: (x0, y0, x1, y1, text, block_no, block_type)

            for b in blocks:
                b_rect = [b[0], b[1], b[2], b[3]]
                text = b[4].strip()
                if not text:
                    continue

                # A. Kiểm tra Scheme
                m_scheme = self.RE_SCHEME.match(text)
                if m_scheme:
                    scheme_num = m_scheme.group(1).upper()
                    entity_id = f"GT_SCHEME_{scheme_num}"
                    if entity_id not in seen_entity_ids:
                        seen_entity_ids.add(entity_id)

                        # Tìm ảnh gần nhất với caption này
                        matched_img = self._find_nearest_image(b_rect, page_images)
                        bbox = matched_img["rect"] if matched_img else b_rect

                        entities.append(
                            GroundTruthEntity(
                                entity_id=entity_id,
                                entity_type="SCHEME",
                                parent_id=None,
                                page_number=page_num,
                                bbox=bbox,
                                caption_text=text[:300],
                                label_extracted=f"Scheme {scheme_num}",
                                image_xref=matched_img["xref"] if matched_img else None,
                                is_vector=(matched_img is None),
                                sha256_hash=matched_img["sha256"] if matched_img else None,
                            )
                        )
                    continue

                # B. Kiểm tra Figure
                m_fig = self.RE_FIGURE.match(text)
                if m_fig:
                    fig_num = m_fig.group(1).upper().replace("-", "_").replace("–", "_")
                    parent_id = f"GT_FIG_{fig_num}"

                    # Kiểm tra xem caption có liệt kê các sub-panels (a), (b), (c), (d) không
                    sub_panels = self.extract_sub_panels(text)

                    matched_img = self._find_nearest_image(b_rect, page_images)
                    bbox = matched_img["rect"] if matched_img else b_rect

                    if sub_panels:
                        # Tạo thực thể mẹ đại diện (COMPOSITE_FIGURE)
                        if parent_id not in seen_entity_ids:
                            seen_entity_ids.add(parent_id)
                            entities.append(
                                GroundTruthEntity(
                                    entity_id=parent_id,
                                    entity_type="COMPOSITE_FIGURE",
                                    parent_id=None,
                                    page_number=page_num,
                                    bbox=bbox,
                                    caption_text=text[:300],
                                    label_extracted=f"Fig. {fig_num}",
                                    image_xref=matched_img["xref"] if matched_img else None,
                                    is_vector=(matched_img is None),
                                    sha256_hash=matched_img["sha256"] if matched_img else None,
                                )
                            )

                        # Tạo các sub-panels độc lập
                        for sub_label, sub_desc in sub_panels:
                            sub_id = f"{parent_id}_{sub_label.upper()}"
                            if sub_id not in seen_entity_ids:
                                seen_entity_ids.add(sub_id)
                                entities.append(
                                    GroundTruthEntity(
                                        entity_id=sub_id,
                                        entity_type="SUB_PANEL",
                                        parent_id=parent_id,
                                        page_number=page_num,
                                        bbox=bbox,
                                        caption_text=f"({sub_label}) {sub_desc.strip()}"[:200],
                                        label_extracted=f"Fig. {fig_num}({sub_label.lower()})",
                                        image_xref=matched_img["xref"] if matched_img else None,
                                        is_vector=(matched_img is None),
                                        sha256_hash=matched_img["sha256"] if matched_img else None,
                                    )
                                )
                    else:
                        # Figure đơn lẻ không phân tách panel
                        if parent_id not in seen_entity_ids:
                            seen_entity_ids.add(parent_id)
                            entities.append(
                                GroundTruthEntity(
                                    entity_id=parent_id,
                                    entity_type="FIGURE",
                                    parent_id=None,
                                    page_number=page_num,
                                    bbox=bbox,
                                    caption_text=text[:300],
                                    label_extracted=f"Fig. {fig_num}",
                                    image_xref=matched_img["xref"] if matched_img else None,
                                    is_vector=(matched_img is None),
                                    sha256_hash=matched_img["sha256"] if matched_img else None,
                                )
                            )
                    continue

                # C. Kiểm tra Table
                m_table = self.RE_TABLE.match(text)
                if m_table:
                    tbl_num = m_table.group(1).upper()
                    entity_id = f"GT_TABLE_{tbl_num}"
                    if entity_id not in seen_entity_ids:
                        seen_entity_ids.add(entity_id)
                        entities.append(
                            GroundTruthEntity(
                                entity_id=entity_id,
                                entity_type="TABLE",
                                parent_id=None,
                                page_number=page_num,
                                bbox=b_rect,
                                caption_text=text[:300],
                                label_extracted=f"Table {tbl_num}",
                                image_xref=None,
                                is_vector=True,
                                sha256_hash=None,
                            )
                        )
                    continue

        doc.close()

        return GroundTruthManifest(
            source_document_path=self.pdf_path,
            section_id=section_id,
            total_entities=len(entities),
            entities=entities,
            scan_timestamp=datetime.now().isoformat(),
            scanner_version="1.0.0-pymupdf-dom",
        )

    def _find_nearest_image(
        self,
        caption_rect: List[float],
        images: List[Dict[str, Any]],
        max_distance_pt: float = 120.0,
    ) -> Optional[Dict[str, Any]]:
        """
        Heuristic khoảng cách hình học tìm ảnh nằm sát bên trên hoặc bên dưới caption.
        """
        if not images:
            return None

        c_top = caption_rect[1]
        c_bottom = caption_rect[3]

        best_img = None
        min_dist = float("inf")

        for img in images:
            i_rect = img["rect"]
            i_top = i_rect[1]
            i_bottom = i_rect[3]

            # Khoảng cách giữa đáy ảnh và đỉnh caption
            dist_above = abs(c_top - i_bottom) if c_top >= i_bottom else float("inf")
            # Khoảng cách giữa đỉnh ảnh và đáy caption
            dist_below = abs(i_top - c_bottom) if i_top >= c_bottom else float("inf")

            dist = min(dist_above, dist_below)
            if dist <= max_distance_pt and dist < min_dist:
                min_dist = dist
                best_img = img

        return best_img

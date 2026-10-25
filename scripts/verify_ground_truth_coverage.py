# -*- coding: utf-8 -*-
"""
scripts/verify_ground_truth_coverage.py — Module Kiểm Toán Độ Phủ Thực Thể Nguồn & Số Liệu Thực Nghiệm
Antigravity 2.0 - Standalone Autonomous Ground Truth Coverage Verifier
Áp dụng: ENGINEERING_DISCIPLINE_WORKFLOW.md [PHA 3: NÂNG CẤP & ĐỐI CHIẾU CHÉO]

Mục tiêu kỹ thuật:
- Mở tệp PDF đệm (%TEMP%) bằng PyMuPDF (fitz) trước khi cho phép thay thế nguyên tử.
- Kiểm toán độ phủ Panels ảnh: Đảm bảo toàn bộ panels trong GroundTruthEntityManifest được nhúng.
- Kiểm toán Bảng biểu: Đảm bảo toàn bộ bảng dữ liệu trong manifest được khởi tạo.
- Kiểm toán Số liệu Đo đạc Cứng (Hard Metrics): Quét toàn bộ text PDF để đối chiếu từ điển số liệu thực nghiệm,
  ngăn chặn hiện tượng trôi dạt thông số (Zero-Symbol-Drift).
- Xuất bản hợp đồng dữ liệu chuẩn Pydantic: GroundTruthCoverageReport.
"""

import os
import sys
import re
import json
import argparse
from typing import List, Dict, Optional, Union, Any, Literal
import pydantic

try:
    import pymupdf
    fitz = pymupdf
except ImportError:
    try:
        import fitz
    except ImportError:
        fitz = None

# Đảm bảo import schemas nội bộ
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOT_AGENTS = os.path.join(PROJECT_ROOT, ".agents")
for p in [DOT_AGENTS, PROJECT_ROOT]:
    if p not in sys.path:
        sys.path.insert(0, p)

from schemas.blueprint import (
    GroundTruthPanelSpec,
    GroundTruthTableSpec,
    GroundTruthEntityManifest,
    CurriculumBlueprint,
)


class GroundTruthCoverageReport(pydantic.BaseModel):
    """Hợp đồng Báo cáo Kiểm toán Độ phủ Thực thể Nguồn và Số liệu Thực nghiệm."""
    model_config = pydantic.ConfigDict(extra="ignore")

    status: Literal["PASS", "FAIL"] = pydantic.Field(description="Trạng thái kiểm định toàn diện")
    pdf_path: str = pydantic.Field(description="Đường dẫn tệp PDF được kiểm toán")
    manifest_id: Optional[str] = pydantic.Field(default=None, description="Mã định danh manifest đối chiếu")
    total_panels_expected: int = pydantic.Field(ge=0, description="Số panels ảnh yêu cầu trong manifest")
    total_panels_found: int = pydantic.Field(ge=0, description="Số ảnh phát hiện trong PDF")
    missing_panels: List[str] = pydantic.Field(default_factory=list, description="Danh sách panel bị thiếu")
    total_tables_expected: int = pydantic.Field(ge=0, description="Số bảng biểu yêu cầu trong manifest")
    total_tables_found: int = pydantic.Field(ge=0, description="Số bảng biểu nhận diện trong PDF")
    missing_tables: List[str] = pydantic.Field(default_factory=list, description="Danh sách bảng bị thiếu")
    hard_metrics_total: int = pydantic.Field(ge=0, description="Tổng số tham số thực nghiệm cần đối soát")
    hard_metrics_matched: int = pydantic.Field(ge=0, description="Số tham số thực nghiệm khớp chính xác")
    unmatched_metrics: List[Dict[str, Any]] = pydantic.Field(
        default_factory=list,
        description="Danh sách tham số thực nghiệm bị trôi dạt hoặc không tìm thấy"
    )
    coverage_percent: float = pydantic.Field(ge=0.0, le=100.0, description="Tỷ lệ phủ toàn diện thực thể (%)")
    reasons: List[str] = pydantic.Field(default_factory=list, description="Chi tiết lý do đánh rớt nếu FAIL")


def _normalize_metric_string(val: Any) -> List[str]:
    """Tạo tập hợp các biến thể chuỗi số biểu diễn hợp lệ để đối soát."""
    if val is None:
        return []
    s = str(val).strip()
    variants = {s}
    
    # Hỗ trợ dấu chấm và phẩy thập phân (1.424 <-> 1,424)
    if "." in s:
        variants.add(s.replace(".", ","))
    elif "," in s:
        variants.add(s.replace(",", "."))
        
    # Hỗ trợ có hoặc không có khoảng trắng trước đơn vị (15 mA <-> 15mA)
    m = re.match(r"^([+-]?\d+(?:[\.,]\d+)?)\s*([a-zA-ZμΩ°/%\^\-]+)$", s)
    if m:
        num, unit = m.groups()
        variants.add(f"{num}{unit}")
        variants.add(f"{num} {unit}")
        if "." in num:
            variants.add(f"{num.replace('.', ',')}{unit}")
            variants.add(f"{num.replace('.', ',')} {unit}")
        elif "," in num:
            variants.add(f"{num.replace(',', '.')}{unit}")
            variants.add(f"{num.replace(',', '.')} {unit}")
            
    return list(variants)


def load_manifest(manifest_source: Union[str, dict, GroundTruthEntityManifest, CurriculumBlueprint]) -> GroundTruthEntityManifest:
    """Nạp linh hoạt GroundTruthEntityManifest từ nhiều nguồn khác nhau."""
    if isinstance(manifest_source, GroundTruthEntityManifest):
        return manifest_source
    if isinstance(manifest_source, CurriculumBlueprint):
        if manifest_source.ground_truth_manifest:
            return manifest_source.ground_truth_manifest
        return GroundTruthEntityManifest(manifest_id=f"BP_{manifest_source.course_name}")
    if isinstance(manifest_source, dict):
        if "ground_truth_manifest" in manifest_source and manifest_source["ground_truth_manifest"]:
            return GroundTruthEntityManifest.model_validate(manifest_source["ground_truth_manifest"])
        return GroundTruthEntityManifest.model_validate(manifest_source)
    if isinstance(manifest_source, str):
        if not os.path.exists(manifest_source):
            raise FileNotFoundError(f"Không tìm thấy tệp manifest tại: {manifest_source}")
        with open(manifest_source, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "ground_truth_manifest" in data and data["ground_truth_manifest"]:
            return GroundTruthEntityManifest.model_validate(data["ground_truth_manifest"])
        return GroundTruthEntityManifest.model_validate(data)
    raise TypeError(f"Nguồn manifest không hợp lệ: {type(manifest_source)}")


def verify_ground_truth_coverage(
    pdf_path: str,
    manifest_source: Union[str, dict, GroundTruthEntityManifest, CurriculumBlueprint],
) -> GroundTruthCoverageReport:
    """
    Hàm đối chiếu chéo số liệu thực nghiệm và thực thể nguồn giữa PDF và Manifest.
    Bảo đảm 100% Zero-Orphan, Zero-Omission và Zero-Symbol-Drift.
    """
    if fitz is None:
        raise RuntimeError("PyMuPDF (fitz) chưa được cài đặt trong môi trường Python!")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Không tìm thấy tệp PDF tại: {pdf_path}")

    manifest = load_manifest(manifest_source)
    doc = fitz.open(pdf_path)

    # 1. Trích xuất toàn văn bản và đếm ảnh trong PDF
    full_text = ""
    total_images_in_pdf = 0
    for page in doc:
        full_text += page.get_text("text") + "\n"
        total_images_in_pdf += len(page.get_images())

    reasons = []

    # 2. Kiểm toán Panels ảnh
    missing_panels = []
    expected_panels_count = len(manifest.panels)
    for p in manifest.panels:
        # Kiểm tra xem nhãn hoặc ID của panel có xuất hiện trong PDF không
        label_found = False
        candidates = [p.panel_id, p.panel_label]
        # Thử tìm các định dạng như "Figure 1(a)", "Hình 1(a)", "(a)"
        for c in candidates:
            if c and c.lower() in full_text.lower():
                label_found = True
                break
        if not label_found and expected_panels_count > 0:
            missing_panels.append(p.panel_id)

    # Kiểm tra số lượng ảnh tối thiểu
    if total_images_in_pdf < expected_panels_count:
        reasons.append(
            f"Thiếu hình ảnh: PDF chỉ chứa {total_images_in_pdf} ảnh, yêu cầu tối thiểu {expected_panels_count} panels."
        )

    if missing_panels:
        reasons.append(f"Không tìm thấy các panel bắt buộc: {', '.join(missing_panels)}")

    # 3. Kiểm toán Bảng biểu
    missing_tables = []
    expected_tables_count = len(manifest.tables)
    found_tables_count = 0
    for t in manifest.tables:
        table_found = False
        candidates = [t.table_id, t.table_label, t.caption]
        for c in candidates:
            if c and c.lower() in full_text.lower():
                table_found = True
                break
        if table_found:
            found_tables_count += 1
        else:
            missing_tables.append(t.table_id)

    if missing_tables:
        reasons.append(f"Không tìm thấy các bảng biểu bắt buộc: {', '.join(missing_tables)}")

    # 4. Kiểm toán Số liệu Thực nghiệm Cứng (Hard Metrics)
    total_metrics = len(manifest.hard_metrics_dict)
    matched_metrics_count = 0
    unmatched_metrics = []

    for metric_name, metric_val in manifest.hard_metrics_dict.items():
        variants = _normalize_metric_string(metric_val)
        matched = False
        for var in variants:
            if var in full_text:
                matched = True
                break
        if matched:
            matched_metrics_count += 1
        else:
            unmatched = {
                "metric": metric_name,
                "expected_value": metric_val,
                "searched_variants": variants,
            }
            unmatched_metrics.append(unmatched)
            reasons.append(
                f"Trôi dạt số liệu thực nghiệm: '{metric_name}' = '{metric_val}' không tìm thấy trong PDF xuất bản."
            )

    # 5. Tính toán Tỷ lệ Phủ (Coverage Percentage)
    total_elements = expected_panels_count + expected_tables_count + total_metrics
    if total_elements == 0:
        coverage_percent = 100.0
    else:
        matched_elements = (
            (expected_panels_count - len(missing_panels)) +
            found_tables_count +
            matched_metrics_count
        )
        coverage_percent = round((matched_elements / total_elements) * 100.0, 2)

    status: Literal["PASS", "FAIL"] = "PASS" if len(reasons) == 0 else "FAIL"

    return GroundTruthCoverageReport(
        status=status,
        pdf_path=pdf_path,
        manifest_id=manifest.manifest_id,
        total_panels_expected=expected_panels_count,
        total_panels_found=total_images_in_pdf,
        missing_panels=missing_panels,
        total_tables_expected=expected_tables_count,
        total_tables_found=found_tables_count,
        missing_tables=missing_tables,
        hard_metrics_total=total_metrics,
        hard_metrics_matched=matched_metrics_count,
        unmatched_metrics=unmatched_metrics,
        coverage_percent=coverage_percent,
        reasons=reasons,
    )


def main():
    parser = argparse.ArgumentParser(description="Kiểm toán độ phủ Ground Truth trên PDF đệm (%TEMP%).")
    parser.add_argument("--pdf", required=True, help="Đường dẫn tệp PDF cần kiểm toán")
    parser.add_argument("--manifest", required=True, help="Đường dẫn tệp JSON manifest hoặc blueprint")
    parser.add_argument("--json", action="store_true", help="Xuất kết quả định dạng JSON")
    args = parser.parse_args()

    try:
        report = verify_ground_truth_coverage(args.pdf, args.manifest)
        if args.json:
            print(report.model_dump_json(indent=2))
        else:
            print(f"[*] Trạng thái: {report.status} (Độ phủ: {report.coverage_percent}%)")
            print(f"[*] Panels: {report.total_panels_found}/{report.total_panels_expected}")
            print(f"[*] Bảng: {report.total_tables_found}/{report.total_tables_expected}")
            print(f"[*] Số đo cứng: {report.hard_metrics_matched}/{report.hard_metrics_total}")
            if report.reasons:
                print("[!] Các lý do đánh rớt:")
                for r in report.reasons:
                    print(f"  - {r}")
        sys.exit(0 if report.status == "PASS" else 1)
    except Exception as e:
        print(f"[!] Lỗi khi thực thi kiểm toán: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()

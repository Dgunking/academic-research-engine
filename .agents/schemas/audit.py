# -*- coding: utf-8 -*-
"""
Hợp đồng Dữ liệu 4: AuditReport (AUDIT_REPORT.json)
Sinh ra bởi: quality-gatekeeper (Thuật toán 6, 8 - DOHG 2.0, 9)
Tiêu thụ bởi: orchestration-kernel và Trọng tài Duyệt Bùi Trung Dũng.
"""

from typing import List, Dict, Optional, Literal
import pydantic


class StationResult(pydantic.BaseModel):
    """Kết quả kiểm định tại một trạm thuộc hệ thống 5 trạm chốt chặn DOHG 2.0."""
    model_config = pydantic.ConfigDict(extra="forbid")

    station_name: str = pydantic.Field(description="Tên trạm kiểm định")
    passed: bool = pydantic.Field(description="Trạng thái đạt chuẩn (True/False)")
    details: str = pydantic.Field(description="Mô tả chi tiết kết quả hoặc ghi chú kỹ thuật")
    error_traces: Optional[List[str]] = pydantic.Field(
        default=None,
        description="Danh sách các vết lỗi kỹ thuật chi tiết (nếu có)"
    )


class DOHGStationsResult(pydantic.BaseModel):
    """Tổng hợp kết quả 5 Trạm Chốt chặn Đầu ra Xác định (DOHG 2.0)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    station_1_static_linter: StationResult = pydantic.Field(
        description="Trạm 1: Static AST & Typography Linter"
    )
    station_2_boundary_re3_audit: StationResult = pydantic.Field(
        description="Trạm 2: Geometry Collision & Re3 Boundary Audit"
    )
    station_3_sympy_cas_verification: StationResult = pydantic.Field(
        description="Trạm 3: Formal CAS SymPy Verification (simplify == 0)"
    )
    station_4_typographic_preflight: StationResult = pydantic.Field(
        description="Trạm 4: Typography DejaVu Preflight & Arrow Linebreak Gate"
    )
    station_5_reportlab_compilation: StationResult = pydantic.Field(
        description="Trạm 5: ReportLab DocTemplate Compilation & Page Budget"
    )


class BinarySeventeenPointResult(pydantic.BaseModel):
    """Kết quả chi tiết Bảng kiểm 17 Điểm Nhị phân (Pass/Fail 17-point Checklist)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    total_passed: int = pydantic.Field(
        ge=0,
        le=17,
        description="Tổng số tiêu chí đạt chuẩn (17/17 là điều kiện tiên quyết)"
    )
    checklist_status: Dict[str, bool] = pydantic.Field(
        description="Chi tiết trạng thái của từng tiêu chí trong 17 điểm"
    )


class PublicationMetadata(pydantic.BaseModel):
    """Siêu dữ liệu xuất bản và chữ ký số an toàn trên Google Drive."""
    model_config = pydantic.ConfigDict(extra="forbid")

    temp_build_path: str = pydantic.Field(description="Đường dẫn bản dựng tại thư mục tạm %TEMP%")
    final_drive_path: str = pydantic.Field(description="Đường dẫn tệp đích tại Bai_Giang_Dong_Goi/ trên Drive G:\\")
    atomic_replace_success: bool = pydantic.Field(description="Trạng thái thay thế nguyên tử os.replace")
    file_size_bytes: int = pydantic.Field(ge=1, description="Dung lượng tệp PDF thành phẩm")
    sha256_checksum: str = pydantic.Field(description="Mã băm an toàn SHA-256 của tệp PDF thành phẩm")
    two_pass_total_pages: str = pydantic.Field(description="Định dạng số trang hai lượt: 'Trang X / Y'")
    pdf_bookmarks_levels_verified: bool = pydantic.Field(description="Xác nhận cây bookmark 3 cấp đã hợp lệ")


class AuditReport(pydantic.BaseModel):
    """Hợp đồng Báo cáo Giám định Chất lượng Toàn diện (Audit Report Contract)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    section_id: str = pydantic.Field(description="Mã phân mục bài giảng (ví dụ: MUC_2_1)")
    audit_timestamp: str = pydantic.Field(description="Thời điểm thực thi kiểm định (ISO 8601)")
    overall_verdict: Literal["PASS_100_PERCENT", "FAIL_RETRY_REQUIRED", "CRITICAL_HALT"] = pydantic.Field(
        description="Kết luận chung: ĐẠT 100%, CẦN SỬA LỖI LẠI, hoặc DỪNG KHẨN CẤP"
    )
    self_healing_attempt_count: int = pydantic.Field(
        ge=1,
        le=5,
        description="Số lần thử nghiệm tự sửa lỗi (giới hạn tối đa 5 lần)"
    )
    dohg_2_0_results: DOHGStationsResult = pydantic.Field(
        description="Kết quả kiểm định 5 trạm DOHG 2.0"
    )
    binary_17_point_checklist: BinarySeventeenPointResult = pydantic.Field(
        description="Bảng kiểm 17 điểm nhị phân"
    )
    publication_metadata: Optional[PublicationMetadata] = pydantic.Field(
        default=None,
        description="Siêu dữ liệu xuất bản PDF (chỉ có khi overall_verdict == PASS_100_PERCENT)"
    )

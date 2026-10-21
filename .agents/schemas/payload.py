# -*- coding: utf-8 -*-
"""
Hợp đồng Dữ liệu 3: DraftPayload (DRAFT_PAYLOAD.json)
Sinh ra bởi: pedagogical-author (Thuật toán 5, 12 & Linter Trạm 1)
Tiêu thụ bởi: quality-gatekeeper.
"""

from typing import List, Dict, Optional
import pydantic


class EquationDissectionMALAE(pydantic.BaseModel):
    """Giải phẫu Phương trình 3 Cấp độ theo Động cơ MALAE (Thuật toán 12)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    pillar_equation_latex: str = pydantic.Field(
        description="Phương trình cột trụ chuẩn LaTeX phân số gạch ngang \\frac{a}{b}"
    )
    level_1_overview: str = pydantic.Field(
        description="Cấp 1: Tổng quan ý nghĩa vật lý nguyên lý đầu và bảo toàn"
    )
    level_2_nomenclature_html_table: List[Dict[str, str]] = pydantic.Field(
        description="Cấp 2: Bảng giải phẫu từng thành phần, biến số bọc thẻ <i> và số mũ/chỉ số bọc <sub><sup>"
    )
    level_3_asymptotic_and_symmetry: str = pydantic.Field(
        description="Cấp 3: Phân tích giới hạn tiệm cận, tính đối xứng và thứ nguyên vật lý"
    )


class IntermediateDerivationStep(pydantic.BaseModel):
    """Bước biến đổi trung gian tường minh có gắn nhãn chú giải."""
    model_config = pydantic.ConfigDict(extra="forbid")

    step_index: int = pydantic.Field(ge=1, description="Thứ tự bước biến đổi (1, 2, ...)")
    explanation_vi: str = pydantic.Field(
        description="Giải thích bản chất vật lý; bắt buộc bắt đầu bằng: ↳ [Tường minh bước biến đổi trung gian từ slide gốc]:"
    )
    step_equation_latex: str = pydantic.Field(
        description="Công thức toán học từng bước, tuyệt đối không chứa phân số gạch chéo /, dùng \\frac{}{}"
    )


class MicroPointTopicPayload(pydantic.BaseModel):
    """Nội dung triển khai Luận điểm Vi mô (MPT) đủ 5 Giai đoạn Sư phạm Lũy tiến."""
    model_config = pydantic.ConfigDict(extra="forbid")

    mpt_id: str = pydantic.Field(description="Mã định danh MPT khớp với Blueprint (ví dụ: MPT_2_1_1)")
    mpt_title: str = pydantic.Field(description="Tiêu đề luận điểm vi mô")
    stage_1_orientation: str = pydantic.Field(
        description="Giai đoạn 1: Giới thiệu khái niệm mở đầu, gắn kết visual anchor upfront"
    )
    visual_anchor_id: Optional[str] = pydantic.Field(
        default=None,
        description="Mã asset_id của hình mỏ neo (ví dụ: FIG_2_1_1)"
    )
    stage_2_dissection: EquationDissectionMALAE = pydantic.Field(
        description="Giai đoạn 2: Ví dụ tối giản & Giải phẫu phương trình 3 cấp MALAE"
    )
    micro_mechanisms: List[str] = pydantic.Field(
        description="Chuỗi khối nhân quả vi mô (Causal Flowchain), mỗi khối <= 65 từ"
    )
    stage_3_guided_derivation: List[IntermediateDerivationStep] = pydantic.Field(
        description="Giai đoạn 3: Thực hành có hướng dẫn và biến đổi trung gian tường minh"
    )
    stage_4_variation_sweeps: str = pydantic.Field(
        description="Giai đoạn 4: Phân tích biến thể, quét tiệm cận tham số thực nghiệm"
    )
    stage_5_student_challenge_cer: Dict[str, str] = pydantic.Field(
        description="Giai đoạn 5: Thử thách tự luyện CER (Claim, Evidence, Reasoning) kèm Rubric chấm điểm"
    )


class InternalASTLinterReport(pydantic.BaseModel):
    """Báo cáo sơ bộ của bộ lọc AST Linter nội bộ Trạm 1."""
    model_config = pydantic.ConfigDict(extra="forbid")

    passed: bool = pydantic.Field(description="Kết quả kiểm tra tĩnh (True nếu sạch 100%)")
    raw_latex_leaks_count: int = pydantic.Field(default=0, ge=0, description="Số lượng mã LaTeX thô rò rỉ")
    slash_fraction_count: int = pydantic.Field(default=0, ge=0, description="Số lượng phân số gạch chéo / trái quy tắc")
    raw_subscript_count: int = pydantic.Field(default=0, ge=0, description="Số lượng biến code ASCII gạch dưới thô")


class DraftPayload(pydantic.BaseModel):
    """Hợp đồng Bản thảo Bài giảng Chi tiết (Draft Pedagogical Payload Contract)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    section_id: str = pydantic.Field(description="Mã phân mục bài giảng (ví dụ: MUC_2_1)")
    section_title: str = pydantic.Field(description="Tiêu đề phân mục bài giảng")
    cod_rounds_completed: int = pydantic.Field(
        ge=3,
        description="Số vòng nén Chain-of-Density đã hoàn tất (bắt buộc >= 3)"
    )
    mpt_payloads: List[MicroPointTopicPayload] = pydantic.Field(
        description="Danh sách nội dung triển khai toàn diện của từng MPT"
    )
    linter_pre_check: InternalASTLinterReport = pydantic.Field(
        description="Báo cáo kiểm tra trước AST Linter"
    )

# -*- coding: utf-8 -*-
"""
Hợp đồng Dữ liệu 1: CurriculumBlueprint (BLUEPRINT.json)
Sinh ra bởi: curriculum-architect (Thuật toán 1, 2, 4, 10)
Tiêu thụ bởi: physics-graphic-artist, pedagogical-author, quality-gatekeeper, orchestration-kernel.
"""

from typing import List, Dict, Optional, Literal
import pydantic


class KnowledgeDAGNode(pydantic.BaseModel):
    """Nút Đồ thị Tri thức (Knowledge DAG Node) theo phân loại Bloom & Nguyên lý đầu."""
    model_config = pydantic.ConfigDict(extra="forbid")

    node_id: str = pydantic.Field(
        description="Mã định danh duy nhất của nút tri thức (ví dụ: NODE_2_1_1)"
    )
    concept_title: str = pydantic.Field(
        description="Tiêu đề khái niệm hoặc nguyên lý khoa học"
    )
    bloom_level: Literal["Nhớ", "Hiểu", "Vận dụng", "Phân tích", "Đánh giá", "Sáng tạo"] = pydantic.Field(
        description="Bậc thang nhận thức Bloom"
    )
    first_principles_root: str = pydantic.Field(
        description="Định luật bảo toàn hoặc phương trình nền tảng năm 1-3 làm gốc"
    )
    core_equation_latex: Optional[str] = pydantic.Field(
        default=None,
        description="Công thức toán học cốt lõi dạng LaTeX (nếu có)"
    )


class KnowledgeDAGEdge(pydantic.BaseModel):
    """Cạnh Đồ thị Tri thức thể hiện quan hệ phụ thuộc nhân quả hoặc tiền đề."""
    model_config = pydantic.ConfigDict(extra="forbid")

    source_node: str = pydantic.Field(description="Mã node_id nguồn")
    target_node: str = pydantic.Field(description="Mã node_id đích")
    relation_type: Literal["prerequisite", "causal", "generalization", "boundary_limit"] = pydantic.Field(
        description="Loại quan hệ: tiền đề, nhân quả, tổng quát hóa, hoặc giới hạn biên"
    )


class VisualRequirement(pydantic.BaseModel):
    """Yêu cầu tạo dựng hoặc trích xuất hình ảnh phục vụ Luận điểm Vi mô."""
    model_config = pydantic.ConfigDict(extra="forbid")

    visual_type: Literal["MATLAB_SIMULATION", "DSAFE_CROP", "SCHEMATIC_DIAGRAM"] = pydantic.Field(
        description="Chủng loại đồ họa: mô phỏng MATLAB, trích ảnh gốc D-SAFE, hoặc sơ đồ khối vector"
    )
    description: str = pydantic.Field(
        description="Mô tả trực quan nội dung cần biểu diễn"
    )
    physical_variables: List[str] = pydantic.Field(
        default_factory=list,
        description="Danh sách các biến số vật lý cần hiển thị trên trục hoặc nhãn"
    )
    suggested_model: Optional[str] = pydantic.Field(
        default=None,
        description="Mô hình toán-lý đề xuất (ví dụ: Rate Equations, 8-band k.p, Varshni)"
    )


class MicroPointTopicSpec(pydantic.BaseModel):
    """Đặc tả Luận điểm Vi mô (Micro-Point Topic - MPT) tối thiểu không thể phân rã."""
    model_config = pydantic.ConfigDict(extra="forbid")

    mpt_id: str = pydantic.Field(description="Mã định danh duy nhất (ví dụ: MPT_2_1_1)")
    title: str = pydantic.Field(description="Tiêu đề luận điểm vi mô")
    core_proposition: str = pydantic.Field(
        description="Mệnh đề nguyên tử tối thiểu không thể phân rã"
    )
    prerequisite_mpt_ids: List[str] = pydantic.Field(
        default_factory=list,
        description="Danh sách các mpt_id tiên quyết"
    )
    visual_requirement: Optional[VisualRequirement] = pydantic.Field(
        default=None,
        description="Yêu cầu đồ họa mỏ neo (Visual Anchor) đi kèm"
    )
    target_equations: List[str] = pydantic.Field(
        default_factory=list,
        description="Danh sách các phương trình giải tích trọng tâm của MPT"
    )


class TerminologyEntry(pydantic.BaseModel):
    """Mục danh pháp học thuật khóa cứng theo chuẩn ATCC, ISO 80000 và NĐ 30."""
    model_config = pydantic.ConfigDict(extra="forbid")

    term_en: str = pydantic.Field(description="Thuật ngữ tiếng Anh gốc")
    term_vi: str = pydantic.Field(description="Thuật ngữ tiếng Việt chuẩn hóa")
    symbol_latex: str = pydantic.Field(description="Ký hiệu toán học LaTeX chuẩn")
    standard_unit_si: str = pydantic.Field(description="Đơn vị SI theo Luật Đo lường 04")
    iso_standard_ref: str = pydantic.Field(
        default="ISO 80000",
        description="Chuẩn tham chiếu quốc tế"
    )
    decree_30_case: str = pydantic.Field(
        description="Quy tắc viết hoa danh từ riêng theo Nghị định 30/2020/NĐ-CP"
    )


class CurriculumBlueprint(pydantic.BaseModel):
    """Hợp đồng Thiết kế Khung Bài giảng (Curriculum Blueprint Contract)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    course_name: str = pydantic.Field(description="Tên học phần (ví dụ: Quang học và Quang điện tử)")
    chapter_index: int = pydantic.Field(ge=1, description="Chỉ số chương")
    section_index: int = pydantic.Field(ge=1, description="Chỉ số mục trong chương")
    section_title: str = pydantic.Field(description="Tiêu đề phân mục bài giảng")
    source_documents: List[str] = pydantic.Field(
        description="Danh sách đường dẫn tài liệu Slide & Sách giáo trình gốc đã quét"
    )
    dag_nodes: List[KnowledgeDAGNode] = pydantic.Field(
        description="Danh sách các nút tri thức trong mạng DAG"
    )
    dag_edges: List[KnowledgeDAGEdge] = pydantic.Field(
        description="Danh sách các cạnh quan hệ phụ thuộc giữa các nút"
    )
    mpt_specifications: List[MicroPointTopicSpec] = pydantic.Field(
        description="Danh sách đặc tả các Luận điểm Vi mô (MPT)"
    )
    terminology_contracts: List[TerminologyEntry] = pydantic.Field(
        description="Danh mục các giao ước danh pháp song ngữ chuẩn hóa"
    )

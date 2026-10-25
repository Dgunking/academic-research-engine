# -*- coding: utf-8 -*-
"""
Hợp đồng Dữ liệu 1: CurriculumBlueprint (BLUEPRINT.json)
Sinh ra bởi: curriculum-architect (Thuật toán 1, 2, 4, 10)
Tiêu thụ bởi: physics-graphic-artist, pedagogical-author, quality-gatekeeper, orchestration-kernel.
"""

from typing import List, Dict, Optional, Literal, Any
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
    model_config = pydantic.ConfigDict(extra="ignore")

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
    target_material: Optional[str] = pydantic.Field(
        default=None,
        description="Đích danh vật liệu bán dẫn chỉ định từ ngữ cảnh học liệu (ví dụ: GaAs, InP, GaN, AlGaAs)"
    )
    operating_temperature_k: Optional[float] = pydantic.Field(
        default=300.0,
        description="Nhiệt độ hoạt động chỉ định theo Kelvin (mặc định 300.0 K chuẩn phòng thí nghiệm)"
    )
    lane_type: Literal["NATIVE_ASSET", "ANALYTICAL_SIM"] = pydantic.Field(
        default="ANALYTICAL_SIM",
        description="Làn nạp tài nguyên thị giác: NATIVE_ASSET (Làn 1) vs ANALYTICAL_SIM (Làn 2)"
    )
    archetype: Literal["EMPIRICAL_DATA_PLOT", "PHENOMENON_SIMULATION"] = pydantic.Field(
        default="EMPIRICAL_DATA_PLOT",
        description="Mô thức giải phẫu: Đồ thị dữ liệu thực nghiệm (Nhánh A) vs Mô phỏng hiện tượng không gian (Nhánh B)"
    )
    tvd_sidecar_path: Optional[str] = pydantic.Field(
        default=None,
        description="Đường dẫn tới tệp sidecar TVD (*.tvd.json)"
    )


class VisualAssetSpec(pydantic.BaseModel):
    """Đặc tả Mỏ neo Thị giác tương thích ngược 100% với LessonDeliverable và BLUEPRINT_MUC_X.Y.json."""
    model_config = pydantic.ConfigDict(extra="ignore")

    image_file_path: str = pydantic.Field(description="Đường dẫn tệp hình ảnh")
    interaction_id: str = pydantic.Field(description="Mã định danh tương tác trực quan")
    aspect_ratio: str = pydantic.Field(default="6.5:4.2", description="Tỷ lệ khung hình")
    brand_palette_compliant: bool = pydantic.Field(default=True, description="Tuân thủ bảng màu chuẩn")
    pedagogical_caption: str = pydantic.Field(description="Giải trình chú thích 3 tầng TVD")
    lane_type: Literal["NATIVE_ASSET", "ANALYTICAL_SIM"] = pydantic.Field(
        default="ANALYTICAL_SIM",
        description="Làn nạp: NATIVE_ASSET (Làn 1) hoặc ANALYTICAL_SIM (Làn 2)"
    )
    archetype: Literal["EMPIRICAL_DATA_PLOT", "PHENOMENON_SIMULATION"] = pydantic.Field(
        default="EMPIRICAL_DATA_PLOT",
        description="Chủng loại: Đồ thị thực nghiệm (Nhánh A) hoặc Mô phỏng hiện tượng (Nhánh B)"
    )
    tvd_sidecar_path: Optional[str] = pydantic.Field(
        default=None,
        description="Đường dẫn tệp sidecar *.tvd.json"
    )
    target_material: Optional[str] = pydantic.Field(
        default=None,
        description="Vật liệu bán dẫn mục tiêu (GaAs, InP, GaN, AlGaAs, InGaAsP)"
    )
    parameter_card: Optional[Dict[str, Any]] = pydantic.Field(
        default=None,
        description="Thẻ tham số trích xuất từ kịch bản mô phỏng"
    )


class ChiefEngineerFourQuestionsSpec(pydantic.BaseModel):
    """Đặc tả Giải phẫu Động lực học & Tham số Vận hành theo Thuật toán 4 (PLBE)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    micro_struggle_quantized: str = pydantic.Field(
        description="1. Cơ chế vi mô cốt lõi nào đang diễn ra?"
    )
    engineer_control_knob: str = pydantic.Field(
        description="2. Thông số ta có thể chủ động điều khiển:"
    )
    macroscopic_lab_response: str = pydantic.Field(
        description="3. Tín hiệu thực nghiệm quan sát được trên máy đo:"
    )
    valid_operating_zone_and_breakdown: str = pydantic.Field(
        description="4. Phạm vi hoạt động tối ưu và ngưỡng phá vỡ giới hạn (Điều kiện biên & giới hạn phi tuyến)"
    )


class ToulminFourBeatSpec(pydantic.BaseModel):
    """Đặc tả Chuỗi Suy Luận Nhân Quả 4 Nhịp Toulmin cho Khối 2 trong Blueprint."""
    model_config = pydantic.ConfigDict(extra="ignore")

    visual_evidence: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 1: Điểm gãy/uốn và số liệu SI bóc tách từ ảnh"
    )
    micro_dynamics_warrant: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 2: Động lực học vi mô đối kháng (Carrier Density Pinning, đảo mật độ...)"
    )
    math_blending_scaling: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 3: Phương trình cốt trụ a/b & Phép thử tương quan độ lớn (Scaling Step)"
    )
    engineering_claim: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 4: Khẳng định thiết kế R&D và chỉ tiêu vận hành"
    )


class MicroPointTopicSpec(pydantic.BaseModel):
    """Đặc tả Luận điểm Vi mô (MPT) theo Dòng chảy Nhận thức 3 Khối mới của Thuật toán 4 (PLBE)."""
    model_config = pydantic.ConfigDict(extra="ignore")

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
        description="Yêu cầu đồ họa mỏ neo (Visual Anchor) định vị tại Khối 2"
    )
    target_equations: List[str] = pydantic.Field(
        default_factory=list,
        description="Phương trình cốt trụ duy nhất của MPT"
    )
    chief_engineer_questions: Optional[ChiefEngineerFourQuestionsSpec] = pydantic.Field(
        default=None,
        description="Giải phẫu Động lực học & Tham số Vận hành"
    )
    four_beat_pipeline: Optional[ToulminFourBeatSpec] = pydantic.Field(
        default=None,
        description="Chuỗi Suy Luận Nhân Quả 4 Nhịp Toulmin cho Khối 2"
    )
    block_2_archetype: Literal["EMPIRICAL_DATA_PLOT", "PHENOMENON_SIMULATION"] = pydantic.Field(
        default="EMPIRICAL_DATA_PLOT",
        description="Phân nhánh đa hình cho Khối 2"
    )
    block_3_mode: Optional[str] = pydantic.Field(
        default="ORTHOGONAL_OPEN_CER",
        description="Chế độ thi công Khối 3: Góc nhìn đối trọng & Thử thách chẩn đoán CER mở (Zero-Solution trong PDF)"
    )
    ground_truth_ref: Optional[List[str]] = pydantic.Field(
        default_factory=list,
        description="Danh sách các mã thực thể Ground Truth mà MPT này bao phủ hoặc đối chiếu (ví dụ: ['GT_SCHEME_1'])"
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


class GroundTruthPanelSpec(pydantic.BaseModel):
    """Đặc tả một panel ảnh / sơ đồ nguồn trong tài liệu gốc."""
    model_config = pydantic.ConfigDict(extra="ignore")

    panel_id: str = pydantic.Field(description="Mã định danh panel (ví dụ: GT_FIG_1_A, GT_SCHEME_1)")
    panel_label: str = pydantic.Field(description="Nhãn hiển thị trong tài liệu gốc (ví dụ: Figure 1(a), Scheme 1)")
    description: str = pydantic.Field(description="Mô tả hiện tượng hoặc cơ chế vi mô của panel")
    image_xref: Optional[int] = pydantic.Field(default=None, description="Số hiệu xref ảnh trong PDF")
    sha256_hash: Optional[str] = pydantic.Field(default=None, description="Mã băm SHA-256 đối soát toàn vẹn")


class GroundTruthTableSpec(pydantic.BaseModel):
    """Đặc tả một bảng biểu số liệu trong tài liệu gốc."""
    model_config = pydantic.ConfigDict(extra="ignore")

    table_id: str = pydantic.Field(description="Mã định danh bảng (ví dụ: GT_TABLE_1)")
    table_label: str = pydantic.Field(description="Nhãn bảng trong tài liệu gốc (ví dụ: Table 1)")
    caption: str = pydantic.Field(description="Tiêu đề và nội dung bảng")
    required_columns: List[str] = pydantic.Field(default_factory=list, description="Danh sách cột dữ liệu bắt buộc")


class GroundTruthEntityManifest(pydantic.BaseModel):
    """Hợp đồng Danh mục Thực thể Nguồn (Panels, Tables, Hard Metrics) cho Zero-Orphan Gate."""
    model_config = pydantic.ConfigDict(extra="ignore")

    manifest_id: Optional[str] = pydantic.Field(default="GT_MANIFEST_DEFAULT", description="Mã định danh manifest")
    source_document: Optional[str] = pydantic.Field(default=None, description="Tên hoặc đường dẫn tài liệu gốc")
    panels: List[GroundTruthPanelSpec] = pydantic.Field(
        default_factory=list,
        description="Danh mục panels ảnh và sơ đồ gốc bắt buộc nhúng"
    )
    tables: List[GroundTruthTableSpec] = pydantic.Field(
        default_factory=list,
        description="Danh mục bảng biểu dữ liệu gốc bắt buộc nhúng"
    )
    hard_metrics_dict: Dict[str, Any] = pydantic.Field(
        default_factory=dict,
        description="Từ điển số đo cứng thực nghiệm chống trôi dạt (ví dụ: {'I_th': '15 mA', 'Eg': 1.424})"
    )


class CurriculumBlueprint(pydantic.BaseModel):
    """Hợp đồng Thiết kế Khung Bài giảng (Curriculum Blueprint Contract)."""
    model_config = pydantic.ConfigDict(extra="ignore")

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
    ground_truth_manifest_path: Optional[str] = pydantic.Field(
        default=None,
        description="Đường dẫn tệp GROUND_TRUTH_MANIFEST.json làm mỏ neo đối chiếu Zero-Omission"
    )
    ground_truth_manifest: Optional[GroundTruthEntityManifest] = pydantic.Field(
        default=None,
        description="Hợp đồng Danh mục Thực thể Nguồn (Panels, Tables, Hard Metrics) chống trôi dạt và ảnh mồ côi"
    )

    @pydantic.model_validator(mode="after")
    def validate_dag_acyclic(self) -> "CurriculumBlueprint":
        """
        Kiểm tra tính phi chu trình (Acyclic) của mạng DAG tri thức bằng Giải thuật Kahn.
        Bảo đảm không tồn tại quan hệ phụ thuộc vòng kín (Circular/Deadlock Dependencies).
        """
        all_nodes = {node.node_id for node in self.dag_nodes}
        for edge in self.dag_edges:
            all_nodes.add(edge.source_node)
            all_nodes.add(edge.target_node)

        if not all_nodes:
            return self

        adj_list: Dict[str, List[str]] = {nid: [] for nid in all_nodes}
        in_degree: Dict[str, int] = {nid: 0 for nid in all_nodes}

        for edge in self.dag_edges:
            adj_list[edge.source_node].append(edge.target_node)
            in_degree[edge.target_node] += 1

        queue = [nid for nid, deg in in_degree.items() if deg == 0]
        visited_count = 0

        while queue:
            curr = queue.pop(0)
            visited_count += 1
            for neighbor in adj_list[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if visited_count < len(all_nodes):
            cyclic_nodes = [nid for nid, deg in in_degree.items() if deg > 0]
            raise ValueError(
                f"Phát hiện chu trình kín (Cyclic Dependency) trong DAG tri thức: {cyclic_nodes}. "
                f"Đồ thị vi phạm nguyên tắc DAG Acyclic theo Giải thuật Kahn."
            )

        return self

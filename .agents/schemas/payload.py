# -*- coding: utf-8 -*-
"""
Hợp đồng Dữ liệu 3: DraftPayload (DRAFT_PAYLOAD.json)
Sinh ra bởi: pedagogical-author (Dòng chảy Nhận thức Nguyên lý Đầu 3 Khối & AST Linter)
Tiêu thụ bởi: quality-gatekeeper, hust_pdf_engine.
"""

from typing import List, Dict, Optional, Literal, Any
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
    """Bước biến đổi trung gian tường minh (không ép buộc chuỗi tiền tố cứng nhắc)."""
    model_config = pydantic.ConfigDict(extra="forbid")

    step_index: int = pydantic.Field(ge=1, description="Thứ tự bước biến đổi (1, 2, ...)")
    explanation_vi: str = pydantic.Field(
        description="Giải thích bản chất vật lý và biến đổi toán học tường minh; dòng chảy tự nhiên, cấm huy hiệu rác"
    )
    step_equation_latex: str = pydantic.Field(
        description="Công thức toán học từng bước, tuyệt đối không chứa phân số gạch chéo /, dùng \\frac{}{}"
    )
    step_nature: Literal["EXACT_ALGEBRAIC", "PHYSICAL_APPROXIMATION"] = pydantic.Field(
        default="EXACT_ALGEBRAIC",
        description="Bản chất biến đổi: EXACT_ALGEBRAIC (đồng nhất thức đại số chuẩn xác cần SymPy CAS simplify == 0) hoặc PHYSICAL_APPROXIMATION (xấp xỉ vật lý tiệm cận)"
    )


class ChiefEngineerFourQuestions(pydantic.BaseModel):
    """Giải phẫu Động lực học & Tham số Vận hành (Thuật toán 4, 5, 12)."""
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


class EmpiricalPlotDissection(pydantic.BaseModel):
    """Nhánh A: Đồ thị Dữ liệu Thực nghiệm (EMPIRICAL_DATA_PLOT)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    extracted_metrics: Dict[str, str] = pydantic.Field(
        default_factory=dict,
        description="Số liệu trích xuất chuẩn SI (I_th, SE, T_0...), 100% không có số mồ côi"
    )
    three_tier_linkage: str = pydantic.Field(
        default="",
        description="Móc nối 3 tầng có hồn: Vi mô -> Động học vĩ mô -> Quyết định R&D"
    )


class PhenomenonSimulationDissection(pydantic.BaseModel):
    """Nhánh B: Sơ đồ Hiện tượng & Cấu trúc Không gian (PHENOMENON_SIMULATION)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    spatial_morphology_mapping: str = pydantic.Field(
        default="",
        description="Đọc vị hình thái hình học: độ dốc (điện trường), độ cong (khối lượng hiệu dụng), bậc nhảy (rào thế), đuôi sóng tắt dần"
    )
    gedanken_parameter_sweep: str = pydantic.Field(
        default="",
        description="Thí nghiệm tưởng tượng vặn núm tham số (Gedanken parameter sweep), Zero-Formula"
    )


class TeleologySpatialContext(pydantic.BaseModel):
    """Khối 1: Khởi nguyên & Trực giác (Teleology & Intuitive Spark - Thuật toán 5 UFME)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    systemic_teleology_sbf: str = pydantic.Field(
        description="Định vị mắt xích hệ thống SBF/NFPS: nút thắt ở bước N-1, chức năng can thiệp ở bước N, và đầu ra cấp cho bước N+1"
    )
    plain_english_axiom: str = pydantic.Field(
        description="Bản chất Cốt lõi định nghĩa bản chất bằng ngôn ngữ tự nhiên sắc bén (Zero-Jargon)"
    )
    spatial_topology_anchor: Optional[str] = pydantic.Field(
        default=None,
        description="Mỏ neo không gian 3D: giải mã hình học dải năng lượng E-z, E-k hoặc phân bố mode trường quang"
    )
    tangible_intuitive_framing: Optional[str] = pydantic.Field(
        default=None,
        description="Hình tượng hóa trực giác (dòng chảy 3 nhịp) đời thực đẳng cấu toán học (duy nhất 1 lần, đăng ký SME chống lặp). TUYỆT ĐỐI KHÔNG GHIM ẢNH KỸ THUẬT Ở KHỐI 1."
    )
    cognitive_handover_to_block_2: Optional[str] = pydantic.Field(
        default=None,
        description="Mắt xích Chuyển tiếp sang Khối 2: Câu hỏi gợi mở hình thù thị giác và tín hiệu đo Lab"
    )

    @property
    def tangible_mechanistic_analogy(self) -> Optional[str]:
        return self.tangible_intuitive_framing


class ToulminFourBeatPipeline(pydantic.BaseModel):
    """Chuỗi Suy Luận Nhân Quả 4 Nhịp (Toulmin Causal Pipeline) cho Khối 2."""
    model_config = pydantic.ConfigDict(extra="ignore")

    beat_1_visual_evidence: str = pydantic.Field(
        default="",
        description="Nhịp 1: Bằng chứng thị giác & Tọa độ ngưỡng (Data) - Visual Anchor TVD, điểm gãy/uốn, thông số chuẩn SI"
    )
    beat_2_micro_dynamics_warrant: str = pydantic.Field(
        default="",
        description="Nhịp 2: Giải mã Động lực học Vi mô (Warrant 1) - Cơ chế đối kháng hạt tải/photon/phonon tại điểm đặc trưng"
    )
    beat_3_math_blending_scaling: str = pydantic.Field(
        default="",
        description="Nhịp 3: Ánh xạ Toán – Lý & Thử Tương quan Độ lớn (Warrant 2) - Khớp Phương trình Cốt trụ a/b và Phép thử độ lớn"
    )
    beat_4_engineering_claim: str = pydantic.Field(
        default="",
        description="Nhịp 4: Đúc kết Khẳng định Kỹ thuật (Claim) - Kết luận thiết kế R&D và chỉ tiêu vận hành từ phép thử độ lớn"
    )


class MechanisticBlendingEquation(pydantic.BaseModel):
    """Khối 2: Mỏ neo Thị giác & Phương trình Cốt trụ Hợp nhất (Thuật toán 5, 12, 14 - Chuỗi 4 Nhịp Toulmin)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    # 4 Thành phần chuẩn hóa của Chuỗi Suy Luận Nhân Quả 4 Nhịp Toulmin:
    visual_evidence: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 1: Bằng chứng thị giác & Tọa độ ngưỡng (Data) - Bóc tách điểm uốn/gãy hình học, thông số SI"
    )
    micro_dynamics_warrant: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 2: Giải mã Động lực học Vi mô (Warrant 1) - Cơ chế đối kháng hạt tải/photon/phonon"
    )
    math_blending_scaling: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 3: Ánh xạ Toán – Lý & Thử Tương quan Độ lớn (Warrant 2) - Phương trình a/b & Scaling Step"
    )
    engineering_claim: Optional[str] = pydantic.Field(
        default=None,
        description="Nhịp 4: Đúc kết Khẳng định Kỹ thuật (Claim) - Chỉ tiêu thiết kế R&D từ phép thử độ lớn"
    )
    four_beat_pipeline: Optional[ToulminFourBeatPipeline] = pydantic.Field(
        default=None,
        description="Đối tượng Chuỗi 4 Nhịp Toulmin hợp nhất"
    )

    first_principles_origin: str = pydantic.Field(
        default="Xuất phát từ phương trình vi phân và các định luật bảo toàn gốc.",
        description="Truy vết tiên đề nguyên lý đầu: phương trình bảo toàn gốc (liên tục hạt tải, Poisson, Helmholtz, v.v.)"
    )
    pillar_equation_latex: Optional[str] = pydantic.Field(
        default=None,
        description="Phương trình cốt trụ duy nhất của MPT (chuẩn LaTeX phân số gạch ngang \\frac{a}{b})"
    )
    chief_engineer_questions: Optional[ChiefEngineerFourQuestions] = pydantic.Field(
        default=None,
        description="Giải phẫu Động lực học & Tham số Vận hành"
    )
    living_crystal_entities_mapping: List[Dict[str, str]] = pydantic.Field(
        default_factory=list,
        description="Ánh xạ song đôi: dịch từng ký hiệu thành 'thực thể sống' trong mạng tinh thể"
    )
    archetype: Literal["EMPIRICAL_DATA_PLOT", "PHENOMENON_SIMULATION"] = pydantic.Field(
        default="EMPIRICAL_DATA_PLOT",
        description="Chủng loại giải phẫu đa hình"
    )
    empirical_dissection: Optional[EmpiricalPlotDissection] = None
    phenomenon_dissection: Optional[PhenomenonSimulationDissection] = None
    sweep_script_code: Optional[str] = pydantic.Field(
        default=None,
        description="Kịch bản quét tham số (Sweep Script) 10-15 dòng Python/MATLAB"
    )
    nonlinear_behavior_punchline: Optional[str] = pydantic.Field(
        default=None,
        description="1 câu chốt hành vi phi tuyến của linh kiện"
    )
    visual_anchor_path: Optional[str] = pydantic.Field(
        default=None,
        description="Đường dẫn tệp ảnh mỏ neo TVD (định vị chuẩn tắc tại Khối 2)"
    )
    # Các trường tương thích ngược:
    equation_dissection_malae: Optional[EquationDissectionMALAE] = pydantic.Field(
        default=None,
        description="Giải phẫu phương trình 3 cấp độ MALAE (legacy)"
    )
    causal_flowchain: List[str] = pydantic.Field(
        default_factory=list,
        description="Chuỗi biến đổi nhân quả vi mô (Causal Flowchain), mỗi khối <= 65 từ có ký hiệu điều hướng (->, =>)"
    )
    guided_derivations: List[IntermediateDerivationStep] = pydantic.Field(
        default_factory=list,
        description="Trường di sản duy trì tương thích ngược 100% (mặc định rỗng)"
    )
    toy_model_code: Optional[str] = pydantic.Field(
        default=None,
        description="Mã mô phỏng đồ chơi (Toy Model) Python/MATLAB 15-25 dòng"
    )
    cognitive_handover_to_block_3: Optional[str] = pydantic.Field(
        default=None,
        description="Mắt xích Chuyển tiếp sang Khối 3: Câu hỏi gợi mở va đập với thực tế kỹ thuật và cạm bẫy"
    )


class BoundaryAuditEngineeringSchema(pydantic.BaseModel):
    """Khối 3: Pháp y Thực nghiệm & Bản lĩnh Kỹ sư (Thuật toán 5, 8 - legacy schema)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    adversarial_boundary_audit: str = pydantic.Field(
        description="Kiểm toán giả thiết ngầm định, điểm gãy điều kiện biên/cực trị, phi tuyến, trôi nhiệt và suy hao ký sinh trong thực tế Lab"
    )
    engineering_heuristic_schema: str = pydantic.Field(
        description="Đúc kết sơ đồ tư duy tái sử dụng: Quy tắc thiết kế bất biến (Engineering Heuristic) liên kết cấu trúc - chức năng - đánh đổi"
    )
    student_challenge_cer: Dict[str, str] = pydantic.Field(
        description="Thử thách chẩn đoán R&D thực chiến theo cấu trúc CER (Claim, Evidence, Reasoning) mở trên Chat (cấm giải hộ trong PDF)"
    )
    middendorf_counterfactual_interrogation: Optional[str] = pydantic.Field(
        default=None,
        description="Thẩm vấn phản thực tế Middendorf ('Điều gì xảy ra nếu...?')"
    )
    lab_measurement_fingerprint: Optional[str] = pydantic.Field(
        default=None,
        description="Dấu vân tay thiết bị đo Lab Keithley SMU/OSA và sai số thực nghiệm"
    )
    chief_engineer_tradeoff_law: Optional[str] = pydantic.Field(
        default=None,
        description="Định luật đánh đổi bất biến của Kỹ sư Trưởng"
    )


class OrthogonalPerspective(pydantic.BaseModel):
    """Đầu Khối 3: Bóc tách Góc nhìn Đối trọng (Orthogonal Perspective Dissection).
    Đổi chiều tư duy từ bức tranh lý tưởng ở Khối 2 sang thực tế kỹ thuật:
    z <-> k; Tĩnh <-> Động/Nhiệt; Lý tưởng <-> Khuyết tật/Nhám biên.
    Ngôn ngữ dung dị, trực quan cho sinh viên năm 3 mới tiếp cận 1 tháng.
    """
    model_config = pydantic.ConfigDict(extra="ignore")

    dimension_shifts: List[Dict[str, str]] = pydantic.Field(
        default_factory=list,
        description="Danh sách các trục đối trọng (ví dụ: [{'axis': 'z vs k', 'insight': '...'}])"
    )
    intuitive_dissection: str = pydantic.Field(
        default="",
        description="Diễn giải góc nhìn đối trọng bằng ngôn ngữ tự nhiên mộc mạc, hạ độ dốc nhận thức"
    )
    practical_limitations: str = pydantic.Field(
        default="",
        description="Điểm gãy của mô hình lý tưởng khi đối mặt với trôi nhiệt, khuyết tật và nhám biên"
    )


class OpenCERChallenge(pydantic.BaseModel):
    """Cuối Khối 3: Thử thách Chẩn đoán R&D Mở (Open CER Challenge).
    Định hướng theo khung Claim – Evidence – Reasoning.
    RÀNG BUỘC BẤT BIẾN: CẤM TUYỆT ĐỐI IN LỜI GIẢI TRONG PDF.
    """
    model_config = pydantic.ConfigDict(extra="ignore")

    challenge_context: str = pydantic.Field(
        default="",
        description="Bối cảnh kỹ thuật phòng Lab / dây chuyền sản xuất thực tế liên quan đến hình ảnh Khối 2"
    )
    diagnostic_question: str = pydantic.Field(
        default="",
        description="Câu hỏi chẩn đoán bẫy ngộ nhận kỹ thuật sâu sắc, kích thích tư duy độc lập"
    )
    claim_guidance: str = pydantic.Field(
        default="",
        description="Định hướng tiêu chí cho Khẳng định (Claim), KHÔNG TIẾT LỘ ĐÁP ÁN CUỐI CÙNG"
    )
    evidence_required: str = pydantic.Field(
        default="",
        description="Dữ kiện thực nghiệm / tham số vật lý cần trích xuất làm bằng chứng (Evidence)"
    )
    reasoning_rubric: str = pydantic.Field(
        default="",
        description="Khung logic và mắt xích nhân quả cần chứng minh (Reasoning)"
    )
    misconception_trap: str = pydantic.Field(
        default="",
        description="Cảnh báo bẫy ngộ nhận kinh điển mà sinh viên mới học hay mắc phải"
    )
    chat_evaluation_key: Optional[str] = pydantic.Field(
        default=None,
        description="Lời giải tham chiếu ĐỘC QUYỀN TRÊN CHAT dùng để AI chấm phản biện khi sinh viên nộp bài; CẤM RENDER VÀO PDF"
    )


class OrthogonalAndCERBlock(pydantic.BaseModel):
    """Khối 3 Mới: Góc Nhìn Đối Trọng & Thử Thách Chẩn Đoán CER (Orthogonal Perspective & Open CER Challenge)."""
    model_config = pydantic.ConfigDict(extra="ignore")

    orthogonal_perspective: OrthogonalPerspective = pydantic.Field(
        default_factory=OrthogonalPerspective,
        description="Phần 1: Bóc tách Góc nhìn Đối trọng (z vs k, Tĩnh vs Động, Lý tưởng vs Thực tế)"
    )
    open_cer_challenge: OpenCERChallenge = pydantic.Field(
        default_factory=OpenCERChallenge,
        description="Phần 2: Thử thách Chẩn đoán R&D Mở theo khung CER (Zero lời giải trong PDF)"
    )


class MicroPointTopicPayload(pydantic.BaseModel):
    """Nội dung triển khai Luận điểm Vi mô (MPT) theo Dòng chảy Nhận thức Nguyên lý Đầu 3 Khối Đa Hình."""
    model_config = pydantic.ConfigDict(extra="ignore")

    mpt_id: str = pydantic.Field(description="Mã định danh MPT khớp với Blueprint (ví dụ: MPT_2_1_1)")
    mpt_title: str = pydantic.Field(description="Tiêu đề luận điểm vi mô")
    visual_anchor_id: Optional[str] = pydantic.Field(
        default=None,
        description="Mã asset_id của hình mỏ neo (ví dụ: FIG_2_1_1)"
    )
    teleology_and_spatial_context: TeleologySpatialContext = pydantic.Field(
        description="Khối 1: Khởi nguyên & Nỗi đau Công nghệ (Origin & Technological Bottleneck)"
    )
    mechanistic_blending_equation: MechanisticBlendingEquation = pydantic.Field(
        description="Khối 2: Mỏ neo Thị giác & Mô hình hóa (Visual Anchor & Modeling)"
    )
    boundary_audit_and_engineering_schema: Optional[BoundaryAuditEngineeringSchema] = pydantic.Field(
        default=None,
        description="Khối 3 (Di sản): Pháp y Thực nghiệm & Bản lĩnh Kỹ sư"
    )
    block_3_orthogonal_cer: Optional[OrthogonalAndCERBlock] = pydantic.Field(
        default=None,
        description="Khối 3 (Chuẩn mới): Góc Nhìn Đối Trọng & Thử Thách Chẩn Đoán CER"
    )

    @pydantic.model_validator(mode="before")
    @classmethod
    def convert_legacy_stages_to_three_blocks(cls, data: Any) -> Any:
        """Tự động chuyển đổi tương thích ngược từ cấu trúc 5 giai đoạn cũ sang 3 Khối Nhận thức mới."""
        if not isinstance(data, dict):
            return data

        # Đồng bộ 2 chiều giữa block_3_orthogonal_cer và boundary_audit_and_engineering_schema
        if "block_3_orthogonal_cer" in data and ("boundary_audit_and_engineering_schema" not in data or not data.get("boundary_audit_and_engineering_schema")):
            b3 = data["block_3_orthogonal_cer"]
            if isinstance(b3, dict):
                ortho = b3.get("orthogonal_perspective", {})
                cer = b3.get("open_cer_challenge", {})
                audit_text = ortho.get("intuitive_dissection", "")
                if ortho.get("practical_limitations"):
                    audit_text = f"{audit_text} {ortho.get('practical_limitations')}".strip()
                cer_dict = {
                    "challenge_prompt": cer.get("diagnostic_question") or cer.get("challenge_context", ""),
                    "claim_guidance": cer.get("claim_guidance", ""),
                    "evidence_required": cer.get("evidence_required", ""),
                    "reasoning_rubric": cer.get("reasoning_rubric", ""),
                    "misconception_warning": cer.get("misconception_trap", ""),
                }
                data["boundary_audit_and_engineering_schema"] = {
                    "adversarial_boundary_audit": audit_text,
                    "engineering_heuristic_schema": "Quy tắc thiết kế bất biến: Cân bằng tương tác cấu trúc và quản trị giới hạn nhiệt/Auger tại biên.",
                    "student_challenge_cer": cer_dict
                }
        elif "boundary_audit_and_engineering_schema" in data and ("block_3_orthogonal_cer" not in data or not data.get("block_3_orthogonal_cer")):
            audit = data["boundary_audit_and_engineering_schema"]
            if isinstance(audit, dict):
                cer = audit.get("student_challenge_cer", {})
                data["block_3_orthogonal_cer"] = {
                    "orthogonal_perspective": {
                        "dimension_shifts": [],
                        "intuitive_dissection": audit.get("adversarial_boundary_audit", ""),
                        "practical_limitations": audit.get("engineering_heuristic_schema", "")
                    },
                    "open_cer_challenge": {
                        "challenge_context": cer.get("challenge_prompt", ""),
                        "diagnostic_question": cer.get("challenge_prompt", ""),
                        "claim_guidance": cer.get("claim_guidance", ""),
                        "evidence_required": cer.get("evidence_required", ""),
                        "reasoning_rubric": cer.get("reasoning_rubric", ""),
                        "misconception_trap": cer.get("misconception_warning", ""),
                        "chat_evaluation_key": None
                    }
                }

        # Nếu đã có đủ các khối chuẩn thì không can thiệp
        if (
            "teleology_and_spatial_context" in data
            and "mechanistic_blending_equation" in data
            and ("boundary_audit_and_engineering_schema" in data or "block_3_orthogonal_cer" in data)
        ):
            return data

        # Nếu nạp payload có các trường legacy: stage_1_orientation, stage_2_dissection...
        if "stage_1_orientation" in data or "stage_2_dissection" in data:
            stage_1 = data.get("stage_1_orientation", "")
            stage_2 = data.get("stage_2_dissection", {})
            micro_mechs = data.get("micro_mechanisms", [])
            stage_3 = data.get("stage_3_guided_derivation", [])
            stage_4 = data.get("stage_4_variation_sweeps", "")
            stage_5 = data.get("stage_5_student_challenge_cer", {})

            # 1. Khối 1: Teleology & Spatial Context
            teleology_ctx = {
                "systemic_teleology_sbf": stage_1,
                "plain_english_axiom": f"Bản chất cốt lõi: {stage_1[:120]}...",
                "spatial_topology_anchor": "Mô hình dải năng lượng không gian thực E-z và không gian xung lượng E-k.",
                "tangible_intuitive_framing": None,
                "cognitive_handover_to_block_2": "Cấu trúc này thực sự mang hình thù thế nào trên bức tranh dải năng lượng và tín hiệu đo Lab?"
            }

            # 2. Khối 2: Mechanistic Blending & Derivation
            first_origin = "Xuất phát từ nguyên lý bảo toàn năng lượng và xung lượng tinh thể."
            if isinstance(stage_2, dict) and "level_1_overview" in stage_2:
                first_origin = stage_2["level_1_overview"]
            elif hasattr(stage_2, "level_1_overview"):
                first_origin = getattr(stage_2, "level_1_overview")

            mechanistic_blending = {
                "first_principles_origin": first_origin,
                "equation_dissection_malae": stage_2,
                "causal_flowchain": micro_mechs,
                "guided_derivations": stage_3,
                "toy_model_code": None,
                "cognitive_handover_to_block_3": "Bức tranh lý tưởng trên bản vẽ thật hoàn hảo, nhưng khi đem ra chế tạo màng mỏng ngoài đời thực, ta sẽ va phải chướng ngại gì?"
            }

            # 3. Khối 3: Boundary Audit & Engineering Schema / Orthogonal & CER
            cer_dict = stage_5 if isinstance(stage_5, dict) else {}
            boundary_schema = {
                "adversarial_boundary_audit": stage_4,
                "engineering_heuristic_schema": "Quy tắc thiết kế bất biến: Cân bằng tương tác cấu trúc và quản trị giới hạn nhiệt/Auger tại biên.",
                "student_challenge_cer": cer_dict
            }
            orthogonal_cer = {
                "orthogonal_perspective": {
                    "dimension_shifts": [],
                    "intuitive_dissection": stage_4,
                    "practical_limitations": "Quy tắc thiết kế bất biến: Cân bằng tương tác cấu trúc và quản trị giới hạn nhiệt/Auger tại biên."
                },
                "open_cer_challenge": {
                    "challenge_context": cer_dict.get("challenge_prompt", ""),
                    "diagnostic_question": cer_dict.get("challenge_prompt", ""),
                    "claim_guidance": cer_dict.get("claim_guidance", ""),
                    "evidence_required": cer_dict.get("evidence_required", ""),
                    "reasoning_rubric": cer_dict.get("reasoning_rubric", ""),
                    "misconception_trap": cer_dict.get("misconception_warning", ""),
                    "chat_evaluation_key": None
                }
            }

            clean_data = {
                "mpt_id": data.get("mpt_id", ""),
                "mpt_title": data.get("mpt_title", ""),
                "visual_anchor_id": data.get("visual_anchor_id", None),
                "teleology_and_spatial_context": teleology_ctx,
                "mechanistic_blending_equation": mechanistic_blending,
                "boundary_audit_and_engineering_schema": boundary_schema,
                "block_3_orthogonal_cer": orthogonal_cer,
            }
            return clean_data

        return data

    # --- Các thuộc tính tương thích ngược (Backward-Compatible Properties) ---
    @property
    def stage_1_orientation(self) -> str:
        ctx = self.teleology_and_spatial_context
        parts = [ctx.systemic_teleology_sbf, ctx.plain_english_axiom, ctx.spatial_topology_anchor]
        if ctx.tangible_intuitive_framing:
            parts.append(ctx.tangible_intuitive_framing)
        return " ".join([p for p in parts if p])

    @stage_1_orientation.setter
    def stage_1_orientation(self, value: str):
        self.teleology_and_spatial_context.systemic_teleology_sbf = value

    @property
    def stage_2_dissection(self) -> Optional[EquationDissectionMALAE]:
        return self.mechanistic_blending_equation.equation_dissection_malae

    @stage_2_dissection.setter
    def stage_2_dissection(self, value: EquationDissectionMALAE):
        self.mechanistic_blending_equation.equation_dissection_malae = value

    @property
    def micro_mechanisms(self) -> List[str]:
        return self.mechanistic_blending_equation.causal_flowchain

    @micro_mechanisms.setter
    def micro_mechanisms(self, value: List[str]):
        self.mechanistic_blending_equation.causal_flowchain = value

    @property
    def stage_3_guided_derivation(self) -> List[IntermediateDerivationStep]:
        return self.mechanistic_blending_equation.guided_derivations

    @stage_3_guided_derivation.setter
    def stage_3_guided_derivation(self, value: List[IntermediateDerivationStep]):
        self.mechanistic_blending_equation.guided_derivations = value

    @property
    def stage_4_variation_sweeps(self) -> str:
        if self.boundary_audit_and_engineering_schema:
            audit = self.boundary_audit_and_engineering_schema
            parts = [audit.adversarial_boundary_audit, audit.engineering_heuristic_schema]
            res = " ".join([p for p in parts if p])
            if res.strip():
                return res
        if self.block_3_orthogonal_cer:
            ortho = self.block_3_orthogonal_cer.orthogonal_perspective
            parts = [ortho.intuitive_dissection, ortho.practical_limitations]
            return " ".join([p for p in parts if p])
        return ""

    @stage_4_variation_sweeps.setter
    def stage_4_variation_sweeps(self, value: str):
        if self.boundary_audit_and_engineering_schema:
            self.boundary_audit_and_engineering_schema.adversarial_boundary_audit = value
        if self.block_3_orthogonal_cer:
            self.block_3_orthogonal_cer.orthogonal_perspective.intuitive_dissection = value

    @property
    def stage_5_student_challenge_cer(self) -> Dict[str, str]:
        if self.boundary_audit_and_engineering_schema and self.boundary_audit_and_engineering_schema.student_challenge_cer:
            return self.boundary_audit_and_engineering_schema.student_challenge_cer
        if self.block_3_orthogonal_cer:
            cer = self.block_3_orthogonal_cer.open_cer_challenge
            return {
                "challenge_prompt": cer.diagnostic_question or cer.challenge_context,
                "claim_guidance": cer.claim_guidance,
                "evidence_required": cer.evidence_required,
                "reasoning_rubric": cer.reasoning_rubric,
                "misconception_warning": cer.misconception_trap,
            }
        return {}

    @stage_5_student_challenge_cer.setter
    def stage_5_student_challenge_cer(self, value: Dict[str, str]):
        if self.boundary_audit_and_engineering_schema:
            self.boundary_audit_and_engineering_schema.student_challenge_cer = value
        if self.block_3_orthogonal_cer:
            self.block_3_orthogonal_cer.open_cer_challenge.diagnostic_question = value.get("challenge_prompt", "")
            self.block_3_orthogonal_cer.open_cer_challenge.claim_guidance = value.get("claim_guidance", "")
            self.block_3_orthogonal_cer.open_cer_challenge.evidence_required = value.get("evidence_required", "")
            self.block_3_orthogonal_cer.open_cer_challenge.reasoning_rubric = value.get("reasoning_rubric", "")
            self.block_3_orthogonal_cer.open_cer_challenge.misconception_trap = value.get("misconception_warning", "")


class InternalASTLinterReport(pydantic.BaseModel):
    """Báo cáo sơ bộ của bộ lọc AST Linter nội bộ Trạm 1."""
    model_config = pydantic.ConfigDict(extra="forbid")

    passed: bool = pydantic.Field(description="Kết quả kiểm tra tĩnh (True nếu sạch 100%)")
    raw_latex_leaks_count: int = pydantic.Field(default=0, ge=0, description="Số lượng mã LaTeX thô rò rỉ")
    slash_fraction_count: int = pydantic.Field(default=0, ge=0, description="Số lượng phân số gạch chéo / trái quy tắc")
    raw_subscript_count: int = pydantic.Field(default=0, ge=0, description="Số lượng biến code ASCII gạch dưới thô")
    unwarranted_claims_count: int = pydantic.Field(default=0, ge=0, description="Số lượng khẳng định kỹ thuật mồ côi thiếu warrant")


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
        description="Danh sách nội dung triển khai toàn diện của từng MPT theo Dòng chảy 3 Khối"
    )
    linter_pre_check: InternalASTLinterReport = pydantic.Field(
        description="Báo cáo kiểm tra trước AST Linter"
    )

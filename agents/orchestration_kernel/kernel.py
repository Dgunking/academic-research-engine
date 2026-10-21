# -*- coding: utf-8 -*-
r"""
Central Orchestration Kernel (Bộ Chỉ Huy Điều Phối FSM Trung Tâm)
Hiện thực hóa:
- Thuật toán 11 (H-LCC Scan Engine & Re3 Synchronization)
- Thuật toán 1 (HDIR/DICG 2.0 - Tầng điều phối đầu vào)
- Thuật toán 9 (%TEMP% Isolation & Atomic Replace vào Drive G:\)
- Quy trình 2 Pha (/scan Sample Gate Mục X.1 -> Autonomous Rollout)
- Chu trình Tự phản tỉnh sửa lỗi Lai ghép (Hybrid Self-Healing 1-3 Local / 4-5 Clean-Slate)
"""

import os
import sys
import json
import time
import shutil
import tempfile
from enum import Enum
from typing import List, Dict, Any, Optional, Tuple, Set
from pydantic import BaseModel, Field

# Core subagent imports
from agents.curriculum_architect.architect import CurriculumArchitect
from agents.physics_graphic_artist.artist import PhysicsGraphicArtist
from agents.pedagogical_author.author import PedagogicalAuthor
from agents.quality_gatekeeper.gatekeeper import QualityGatekeeper

from agents.schemas.blueprint import CurriculumBlueprint, MicroPointTopicSpec, VisualRequirement
from agents.schemas.manifest import VisualAssetManifest
from agents.schemas.payload import DraftPayload
from agents.schemas.audit import AuditReport


def atomic_replace(src: str, dst: str) -> None:
    """Ghi đè nguyên tử tệp nguồn sang tệp đích qua tệp đệm cùng volume."""
    dst_dir = os.path.dirname(os.path.abspath(dst))
    os.makedirs(dst_dir, exist_ok=True)
    temp_fd, temp_dst = tempfile.mkstemp(dir=dst_dir, prefix="atomic_")
    os.close(temp_fd)
    try:
        shutil.copy2(src, temp_dst)
        os.replace(temp_dst, dst)
    except Exception:
        if os.path.exists(temp_dst):
            os.remove(temp_dst)
        raise

from agents.orchestration_kernel.fsm import FSMMachine, FSMState, FSMTransition
from agents.orchestration_kernel.self_healing import (
    HybridSelfHealingEngine,
    HealingStrategy,
    TargetSubagent,
    HealingDirective,
)


class RunMode(str, Enum):
    """Chế độ vận hành của Kernel."""
    SAMPLE_GATE = "SAMPLE_GATE"                # Pha 1: Dừng tại Mục X.1 chờ duyệt
    AUTONOMOUS_ROLLOUT = "AUTONOMOUS_ROLLOUT"  # Pha 2: Cuốn chiếu toàn bộ các mục còn lại
    SINGLE_SECTION = "SINGLE_SECTION"          # Chạy đơn lẻ một phân mục chỉ định


class OrchestratorConfig(BaseModel):
    """Cấu hình vận hành Bộ Chỉ Huy Điều Phối."""
    course_name: str = "Quang điện tử & Laser Diode"
    chapter_index: int = 2
    output_dir: str = "output"
    drive_destination_dir: Optional[str] = None
    max_retries: int = 5
    sandbox_root: Optional[str] = None
    dpi: int = 300


class SectionExecutionResult(BaseModel):
    """Kết quả đóng gói thực thi một phân mục của Kernel."""
    section_id: str
    status: str  # "SUCCESS", "SAMPLE_GATE_WAIT", "FAIL_SAFE_HALTED", "RETRY_REQUIRED"
    final_state: FSMState
    attempt_count: int = 1
    blueprint_path: Optional[str] = None
    manifest_path: Optional[str] = None
    payload_path: Optional[str] = None
    report_path: Optional[str] = None
    pdf_path: Optional[str] = None
    drive_pdf_path: Optional[str] = None
    navigation_anchors: Optional[Dict[str, str]] = None
    fsm_history: List[Dict[str, Any]] = Field(default_factory=list)
    error_traces: List[str] = Field(default_factory=list)


class OrchestrationKernel:
    """
    Bộ Tổng Chỉ Huy Điều Phối FSM Trung Tâm (Orchestration Kernel).
    Quản lý luồng dữ liệu một chiều giữa 4 Subagents, thực thi quy trình 2 Pha
    và cơ chế Tự phản tỉnh sửa lỗi Lai ghép Hybrid Self-Healing.
    """

    def __init__(self, config: Optional[OrchestratorConfig] = None):
        self.config = config or OrchestratorConfig()
        self.fsm = FSMMachine(initial_state=FSMState.IDLE)
        self.healer = HybridSelfHealingEngine()

        # Đường dẫn thư mục xuất bản cục bộ
        self.blueprints_dir = os.path.join(self.config.output_dir, "blueprints")
        self.figures_dir = os.path.join(self.config.output_dir, "figures")
        self.manifests_dir = os.path.join(self.config.output_dir, "manifests")
        self.payloads_dir = os.path.join(self.config.output_dir, "payloads")
        self.reports_dir = os.path.join(self.config.output_dir, "reports")
        self.pdf_dir = os.path.join(self.config.output_dir, "pdf")

        for d in [
            self.blueprints_dir,
            self.figures_dir,
            self.manifests_dir,
            self.payloads_dir,
            self.reports_dir,
            self.pdf_dir,
        ]:
            os.makedirs(d, exist_ok=True)

        # Khởi tạo các Subagent chuyên trách
        self.architect = CurriculumArchitect(sandbox_root=self.config.sandbox_root)
        self.artist = PhysicsGraphicArtist(
            output_dir=self.figures_dir,
            manifest_dir=self.manifests_dir,
            dpi=self.config.dpi,
        )
        self.gatekeeper = QualityGatekeeper()

    def run_section_pipeline(
        self,
        section_id: str,
        section_index: int = 1,
        section_title: str = "Vật lý Bán dẫn & Laser Diode",
        run_mode: RunMode = RunMode.SAMPLE_GATE,
        approved_sample: bool = False,
        source_documents: Optional[List[str]] = None,
        raw_dag_nodes: Optional[List[dict]] = None,
        raw_dag_edges: Optional[List[dict]] = None,
        raw_mpt_specs: Optional[List[dict]] = None,
        raw_terms: Optional[List[dict]] = None,
        preloaded_blueprint: Optional[CurriculumBlueprint] = None,
        preloaded_manifest: Optional[VisualAssetManifest] = None,
        preloaded_draft: Optional[DraftPayload] = None,
    ) -> SectionExecutionResult:
        """
        Thực thi quy trình sản xuất chuyên khảo bài giảng hoàn chỉnh cho 1 phân mục.
        Hỗ trợ Hybrid Self-Healing (1-3 Local, 4-5 Clean-Slate, >5 Fail-Safe).
        """
        self.fsm.reset_to_idle(f"Bắt đầu quy trình sản xuất {section_id}")
        attempt = 1
        current_blueprint: Optional[CurriculumBlueprint] = preloaded_blueprint
        current_manifest: Optional[VisualAssetManifest] = preloaded_manifest
        current_draft: Optional[DraftPayload] = preloaded_draft
        audit_report: Optional[AuditReport] = None

        blueprint_path = os.path.join(self.blueprints_dir, f"{section_id}_BLUEPRINT.json")
        manifest_path = os.path.join(self.manifests_dir, f"{section_id}_ASSET_MANIFEST.json")
        payload_path = os.path.join(self.payloads_dir, f"{section_id}_DRAFT_PAYLOAD.json")
        report_path = os.path.join(self.reports_dir, f"{section_id}_AUDIT_REPORT.json")
        pdf_path = os.path.join(self.pdf_dir, f"Chuyen_Khao_{section_id}.pdf")

        while attempt <= self.config.max_retries:
            # -------------------------------------------------------------
            # BƯỚC 1: AGENT 1 - TRÍCH XUẤT BLUEPRINT (CURRICULUM ARCHITECT)
            # -------------------------------------------------------------
            if current_blueprint is None:
                self.fsm.transition_to(
                    FSMState.EXTRACTING_BLUEPRINT,
                    reason=f"Agent 1 trích xuất Blueprint cho {section_id} (Vòng {attempt})",
                )
                current_blueprint = self._execute_agent_1(
                    section_id=section_id,
                    section_index=section_index,
                    section_title=section_title,
                    source_documents=source_documents,
                    raw_dag_nodes=raw_dag_nodes,
                    raw_dag_edges=raw_dag_edges,
                    raw_mpt_specs=raw_mpt_specs,
                    raw_terms=raw_terms,
                )
                # Lưu Blueprint ra Shared Storage
                with open(blueprint_path, "w", encoding="utf-8") as f:
                    f.write(current_blueprint.model_dump_json(indent=2))

            # -------------------------------------------------------------
            # BƯỚC 2: AGENT 2 - VẼ ĐỒ THỊ & XUẤT MANIFEST (PHYSICS GRAPHIC ARTIST)
            # -------------------------------------------------------------
            if current_manifest is None:
                self.fsm.transition_to(
                    FSMState.GENERATING_ASSETS,
                    reason=f"Agent 2 mô phỏng đồ họa và xuất Manifest cho {section_id} (Vòng {attempt})",
                )
                current_manifest = self.artist.process_blueprint(current_blueprint)
                with open(manifest_path, "w", encoding="utf-8") as f:
                    f.write(current_manifest.model_dump_json(indent=2))

            # -------------------------------------------------------------
            # BƯỚC 3: AGENT 3 - SOẠN THẢO BẢN THẢO TOÀN VĂN (PEDAGOGICAL AUTHOR)
            # -------------------------------------------------------------
            if current_draft is None:
                self.fsm.transition_to(
                    FSMState.AUTHORING_DRAFT,
                    reason=f"Agent 3 soạn thảo bản thảo 5 giai đoạn cho {section_id} (Vòng {attempt})",
                )
                author = PedagogicalAuthor(
                    blueprint=current_blueprint, manifest=current_manifest
                )
                current_draft = author.draft_section_payload(cod_rounds=3)
                with open(payload_path, "w", encoding="utf-8") as f:
                    f.write(current_draft.model_dump_json(indent=2))

            # -------------------------------------------------------------
            # BƯỚC 4: AGENT 4 - KIỂM ĐỊNH 5 TRẠM DOHG 2.0 & XUẤT BẢN PDF
            # -------------------------------------------------------------
            self.fsm.transition_to(
                FSMState.AUDITING_QUALITY,
                reason=f"Agent 4 kiểm toán nhị phân 17 điểm và xuất bản PDF (Vòng {attempt})",
            )
            self.gatekeeper.load_inputs(
                blueprint_input=current_blueprint,
                manifest_input=current_manifest,
                draft_payload_input=current_draft,
            )
            audit_report = self.gatekeeper.execute_audit(
                output_pdf_path=pdf_path,
                output_report_path=report_path,
                drive_destination_path=self.config.drive_destination_dir,
                max_attempts=1,  # Kernel trực tiếp quản trị vòng lặp Hybrid Self-Healing
            )

            # -------------------------------------------------------------
            # BƯỚC 5: ĐÁNH GIÁ KẾT QUẢ & ĐIỀU HƯỚNG HYBRID SELF-HEALING
            # -------------------------------------------------------------
            if audit_report.overall_verdict == "PASS_100_PERCENT":
                # Kiểm tra Rào cản Phê duyệt Sample Gate cho Mục X.1
                is_sample_section = (section_index == 1)
                if is_sample_section and run_mode == RunMode.SAMPLE_GATE and not approved_sample:
                    self.fsm.transition_to(
                        FSMState.SAMPLE_GATE_WAIT,
                        reason="Đạt chuẩn Mục X.1 đối chuẩn; dừng tại Sample Gate chờ Bùi Trung Dũng phê duyệt",
                    )
                    anchors = self.format_navigation_anchors(
                        current_blueprint, current_draft, pdf_path, audit_report
                    )
                    return SectionExecutionResult(
                        section_id=section_id,
                        status="SAMPLE_GATE_WAIT",
                        final_state=FSMState.SAMPLE_GATE_WAIT,
                        attempt_count=attempt,
                        blueprint_path=blueprint_path,
                        manifest_path=manifest_path,
                        payload_path=payload_path,
                        report_path=report_path,
                        pdf_path=pdf_path,
                        navigation_anchors=anchors,
                        fsm_history=self.fsm.export_history(),
                    )

                # Chuyển trạng thái hoàn tất thành công
                self.fsm.transition_to(
                    FSMState.COMPLETED,
                    reason=f"Xuất bản thành công {section_id} đạt chuẩn PASS 100%",
                )

                # Chuyển giao nguyên tử an toàn vào Drive nếu có cấu hình
                drive_pdf_path = None
                if self.config.drive_destination_dir and os.path.isdir(self.config.drive_destination_dir):
                    dest_file = os.path.join(
                        self.config.drive_destination_dir, os.path.basename(pdf_path)
                    )
                    atomic_replace(pdf_path, dest_file)
                    drive_pdf_path = dest_file

                anchors = self.format_navigation_anchors(
                    current_blueprint, current_draft, pdf_path, audit_report
                )
                return SectionExecutionResult(
                    section_id=section_id,
                    status="SUCCESS",
                    final_state=FSMState.COMPLETED,
                    attempt_count=attempt,
                    blueprint_path=blueprint_path,
                    manifest_path=manifest_path,
                    payload_path=payload_path,
                    report_path=report_path,
                    pdf_path=pdf_path,
                    drive_pdf_path=drive_pdf_path,
                    navigation_anchors=anchors,
                    fsm_history=self.fsm.export_history(),
                )

            # KIỂM ĐỊNH THẤT BẠI: KÍCH HOẠT ĐỘNG CƠ TỰ SỬA LỖI LAI GHÉP
            attempt += 1
            strategy, directive = self.healer.analyze_audit_report(
                audit_report, current_attempt=attempt
            )

            if strategy == HealingStrategy.FAIL_SAFE_HALT or attempt > self.config.max_retries:
                self.fsm.transition_to(
                    FSMState.FAIL_SAFE_HALTED,
                    reason=f"Chốt dừng an toàn CRITICAL_FAIL_SAFE sau {self.config.max_retries} chu kỳ",
                    metadata={"error_traces": directive.error_summary if directive else []},
                )
                return SectionExecutionResult(
                    section_id=section_id,
                    status="FAIL_SAFE_HALTED",
                    final_state=FSMState.FAIL_SAFE_HALTED,
                    attempt_count=attempt - 1,
                    blueprint_path=blueprint_path,
                    manifest_path=manifest_path,
                    payload_path=payload_path,
                    report_path=report_path,
                    pdf_path=pdf_path,
                    fsm_history=self.fsm.export_history(),
                    error_traces=directive.error_summary if directive else [],
                )

            if strategy == HealingStrategy.LOCAL_DISPATCH:
                self.fsm.transition_to(
                    FSMState.LOCAL_SELF_HEALING,
                    reason=f"Vi phẫu cục bộ Vòng {attempt - 1} cho các Subagent: {[s.value for s in directive.target_subagents]}",
                    metadata={"failed_stations": directive.failed_stations},
                )
                # Chỉ xóa bỏ và chạy lại đúng Subagent có trách nhiệm
                if TargetSubagent.PHYSICS_GRAPHIC_ARTIST in directive.target_subagents:
                    current_manifest = None
                if TargetSubagent.PEDAGOGICAL_AUTHOR in directive.target_subagents:
                    current_draft = None

            elif strategy == HealingStrategy.CLEAN_SLATE_RESET:
                self.fsm.transition_to(
                    FSMState.CLEAN_SLATE_RESET,
                    reason=f"Cuốn chiếu toàn phần Clean-Slate Vòng {attempt - 1}: Làm sạch cache và chạy lại từ đầu",
                )
                current_blueprint = None
                current_manifest = None
                current_draft = None

        # Hết số lần thử
        self.fsm.transition_to(
            FSMState.FAIL_SAFE_HALTED,
            reason="Vượt quá ngưỡng thử lại tối đa",
        )
        return SectionExecutionResult(
            section_id=section_id,
            status="FAIL_SAFE_HALTED",
            final_state=FSMState.FAIL_SAFE_HALTED,
            attempt_count=attempt - 1,
            fsm_history=self.fsm.export_history(),
        )

    def _execute_agent_1(
        self,
        section_id: str,
        section_index: int,
        section_title: str,
        source_documents: Optional[List[str]],
        raw_dag_nodes: Optional[List[dict]],
        raw_dag_edges: Optional[List[dict]],
        raw_mpt_specs: Optional[List[dict]],
        raw_terms: Optional[List[dict]],
    ) -> CurriculumBlueprint:
        """Thực thi Agent 1 với dữ liệu cung cấp hoặc mẫu đối chuẩn mặc định."""
        docs = source_documents or [
            "Slide_Chuong_2_Vat_Ly_Ban_Dan_HUST.pdf",
            "Giao_Trinh_Quang_Dien_Tu_HUST.pdf",
        ]

        nodes = raw_dag_nodes or [
            {
                "node_id": f"NODE_{section_id}_1",
                "concept_title": f"Cơ chế bán dẫn {section_title}",
                "bloom_level": "Hiểu",
                "first_principles_root": "Phương trình dải năng lượng E(k)",
            }
        ]

        edges = raw_dag_edges or []

        clean_sec = section_id.replace("MUC_", "")
        mpts = raw_mpt_specs or [
            {
                "mpt_id": f"MPT_{clean_sec}_1",
                "title": f"Cơ chế vi mô của {section_title}",
                "core_proposition": f"Phân tích giải tích dải năng lượng và quang học của {section_title}.",
                "prerequisite_mpt_ids": [],
                "visual_requirement": {
                    "visual_type": "MATLAB_SIMULATION",
                    "description": f"Đồ thị giải tích dải năng lượng của {section_title}",
                    "physical_variables": ["E", "k", "E_g"],
                    "suggested_model": "Kane 2-band k.p",
                    "target_material": "GaAs",
                    "operating_temperature_k": 300.0,
                },
                "target_equations": [
                    "E(k) = E_c + \\frac{\\hbar^2 \\cdot k^2}{2 \\cdot m^*_e}"
                ],
            }
        ]

        terms = raw_terms or [
            {
                "vietnamese": "Dải dẫn",
                "english": "Conduction band",
                "definition": "Dải năng lượng chứa các electron tự do tham gia dẫn điện.",
            },
            {
                "vietnamese": "Vùng cấm trực tiếp",
                "english": "Direct bandgap",
                "definition": "Vùng cấm trong đó cực tiểu dải dẫn và cực đại dải hóa trị có cùng số sóng k = 0.",
            },
        ]

        return self.architect.generate_blueprint(
            course_name=self.config.course_name,
            chapter_index=self.config.chapter_index,
            section_index=section_index,
            section_title=section_title,
            source_documents=docs,
            raw_dag_nodes=nodes,
            raw_dag_edges=edges,
            raw_mpt_specs=mpts,
            raw_terms=terms,
        )

    def format_navigation_anchors(
        self,
        blueprint: CurriculumBlueprint,
        draft: DraftPayload,
        pdf_path: str,
        audit_report: AuditReport,
    ) -> Dict[str, str]:
        """
        Định dạng Bộ ba Mỏ neo Điều hướng (~2s) xuất ra khung chat theo Luật 9 & Luật 10.
        """
        mpt_titles = [mpt.title for mpt in blueprint.mpt_specifications]
        meta = audit_report.publication_metadata

        anchor_1 = (
            f"**[Mỏ neo 1 - Khái niệm & Luận điểm Vi mô]:** {blueprint.section_title} | "
            f"Gồm {len(mpt_titles)} MPTs: {', '.join(mpt_titles[:2])}"
        )

        total_mpts = len(draft.mpt_payloads)
        anchor_2 = (
            f"**[Mỏ neo 2 - Phương trình Hạt nhân & Dẫn xuất]:** {total_mpts} Luận điểm Vi mô (5 Giai đoạn sư phạm / MPT) | "
            f"100% dẫn xuất trung gian có nhãn ↳ và phân số chuẩn \\frac{{a}}{{b}}."
        )

        size_kb = (meta.file_size_bytes / 1024.0) if meta else 0
        pages_str = meta.two_pass_total_pages if meta else "Trang 1 / 1"
        sha_str = meta.sha256_checksum[:16] if (meta and meta.sha256_checksum) else "N/A"
        anchor_3 = (
            f"**[Mỏ neo 3 - Chuyên khảo PDF Thành phẩm]:** `{os.path.basename(pdf_path)}` "
            f"({pages_str}, {size_kb:.1f} KB, Canvas hai lượt Trang X / Y, SHA-256: {sha_str}...)."
        )

        return {
            "anchor_1_concept": anchor_1,
            "anchor_2_equation": anchor_2,
            "anchor_3_deliverable": anchor_3,
        }

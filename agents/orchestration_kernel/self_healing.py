# -*- coding: utf-8 -*-
"""
Hybrid Self-Healing Engine (Central Orchestration Kernel)
Hiện thực hóa cơ chế Tự phản tỉnh sửa lỗi Lai ghép 2 tầng:
- Vòng 1 -> 3: Vi phẫu Cục bộ (Local Dispatch) tới đúng Subagent gây lỗi.
- Vòng 4 -> 5: Cuốn chiếu Toàn phần (Clean-Slate Re-rollout) làm lại từ đầu.
- Vòng > 5: Chốt dừng An toàn (Fail-Safe Halt - CRITICAL_FAIL_SAFE).
"""

from enum import Enum
from typing import List, Dict, Any, Optional, Tuple, Set
from pydantic import BaseModel, Field

from agents.schemas.audit import AuditReport


class HealingStrategy(str, Enum):
    """Chiến lược tự sửa lỗi của Kernel."""
    NONE = "NONE"
    LOCAL_DISPATCH = "LOCAL_DISPATCH"
    CLEAN_SLATE_RESET = "CLEAN_SLATE_RESET"
    FAIL_SAFE_HALT = "FAIL_SAFE_HALT"


class TargetSubagent(str, Enum):
    """Tác nhân phụ đích nhận chỉ thị khắc phục vi phẫu."""
    CURRICULUM_ARCHITECT = "curriculum_architect"
    PHYSICS_GRAPHIC_ARTIST = "physics_graphic_artist"
    PEDAGOGICAL_AUTHOR = "pedagogical_author"
    QUALITY_GATEKEEPER = "quality_gatekeeper"
    ALL = "ALL"


class HealingDirective(BaseModel):
    """Chỉ thị sửa lỗi có cấu trúc gửi tới tác nhân phụ."""
    attempt_count: int
    strategy: HealingStrategy
    target_subagents: List[TargetSubagent] = Field(default_factory=list)
    failed_stations: List[int] = Field(default_factory=list)
    error_summary: List[str] = Field(default_factory=list)
    corrective_instructions: str = ""


class HybridSelfHealingEngine:
    """
    Động cơ Tự Phản Tỉnh Sửa Lỗi Lai Ghép (Hybrid Self-Healing Engine).
    Giải mã AuditReport từ Agent 4 để quyết định phân luồng cục bộ hay đập đi xây lại.
    """

    MAX_RETRIES: int = 5
    LOCAL_DISPATCH_THRESHOLD: int = 3  # Vòng 1-3: Vi phẫu cục bộ

    @classmethod
    def analyze_audit_report(
        cls, audit_report: AuditReport, current_attempt: int
    ) -> Tuple[HealingStrategy, Optional[HealingDirective]]:
        """
        Phân tích kết quả kiểm toán nhị phân và trả về chiến lược sửa lỗi.
        """
        # 1. Nếu kiểm toán đạt 100%, không cần sửa
        if audit_report.overall_verdict == "PASS_100_PERCENT":
            return HealingStrategy.NONE, None

        # 2. Thu thập danh sách các trạm kiểm định thất bại
        failed_stations: List[int] = []
        error_traces: List[str] = []

        dohg = audit_report.dohg_2_0_results
        if not dohg.station_1_static_linter.passed:
            failed_stations.append(1)
            error_traces.extend(
                [f"[Trạm 1 Linter] {e}" for e in dohg.station_1_static_linter.error_traces]
            )

        if not dohg.station_2_boundary_re3_audit.passed:
            failed_stations.append(2)
            error_traces.extend(
                [f"[Trạm 2 Đồ họa/Mã băm] {e}" for e in dohg.station_2_boundary_re3_audit.error_traces]
            )

        if not dohg.station_3_sympy_cas_verification.passed:
            failed_stations.append(3)
            error_traces.extend(
                [f"[Trạm 3 SymPy CAS] {e}" for e in dohg.station_3_sympy_cas_verification.error_traces]
            )

        if not dohg.station_4_typographic_preflight.passed:
            failed_stations.append(4)
            error_traces.extend(
                [f"[Trạm 4 Typography] {e}" for e in dohg.station_4_typographic_preflight.error_traces]
            )

        if not dohg.station_5_reportlab_compilation.passed:
            failed_stations.append(5)
            error_traces.extend(
                [f"[Trạm 5 ReportLab PDF] {e}" for e in dohg.station_5_reportlab_compilation.error_traces]
            )

        # 3. Chốt dừng an toàn nếu đã thử quá số lần cho phép (> 5 lần)
        if current_attempt > cls.MAX_RETRIES:
            directive = HealingDirective(
                attempt_count=current_attempt,
                strategy=HealingStrategy.FAIL_SAFE_HALT,
                target_subagents=[TargetSubagent.ALL],
                failed_stations=failed_stations,
                error_summary=error_traces,
                corrective_instructions=(
                    f"CHỐT DỪNG AN TOÀN (CRITICAL_FAIL_SAFE): Đã vượt quá {cls.MAX_RETRIES} lần thử lại "
                    f"mà chưa đạt PASS 100%. Dừng an toàn để bảo vệ tính toàn vẹn hệ thống."
                ),
            )
            return HealingStrategy.FAIL_SAFE_HALT, directive

        # 4. Tầng 1: Vi phẫu Cục bộ (Vòng 1 -> 3)
        if current_attempt <= cls.LOCAL_DISPATCH_THRESHOLD:
            target_subagents: List[TargetSubagent] = []
            instructions_parts: List[str] = []

            # Ánh xạ trạm lỗi sang đúng Subagent chịu trách nhiệm
            # Trạm 2: Đồ họa -> Agent 2 (physics_graphic_artist)
            if 2 in failed_stations:
                target_subagents.append(TargetSubagent.PHYSICS_GRAPHIC_ARTIST)
                instructions_parts.append(
                    "Agent 2 cần vẽ lại hoặc hiệu chỉnh đồ thị: bảo đảm khoảng đệm Triple Buffer "
                    "delta_geom >= 8%, font chữ >= 10 pt và cập nhật lại mã băm SHA-256 trong manifest."
                )

            # Trạm 1, 3, 4, 5: Văn bản / Đại số / Sư phạm -> Agent 3 (pedagogical_author)
            text_pedagogical_stations = {1, 3, 4, 5}.intersection(set(failed_stations))
            if text_pedagogical_stations:
                target_subagents.append(TargetSubagent.PEDAGOGICAL_AUTHOR)
                instructions_parts.append(
                    f"Agent 3 cần hiệu chỉnh bản thảo cho các trạm {list(text_pedagogical_stations)}: "
                    "khắc phục rò rỉ mã LaTeX thô / phân số gạch chéo /, sửa các bước biến đổi trung gian "
                    "đại số hình thức để simplify == 0, và bảo đảm chuẩn bảng danh pháp ISO 80000-2."
                )

            directive = HealingDirective(
                attempt_count=current_attempt,
                strategy=HealingStrategy.LOCAL_DISPATCH,
                target_subagents=target_subagents,
                failed_stations=failed_stations,
                error_summary=error_traces,
                corrective_instructions=" | ".join(instructions_parts),
            )
            return HealingStrategy.LOCAL_DISPATCH, directive

        # 5. Tầng 2: Cuốn chiếu Toàn phần Clean-Slate (Vòng 4 -> 5)
        directive = HealingDirective(
            attempt_count=current_attempt,
            strategy=HealingStrategy.CLEAN_SLATE_RESET,
            target_subagents=[TargetSubagent.ALL],
            failed_stations=failed_stations,
            error_summary=error_traces,
            corrective_instructions=(
                f"CLEAN-SLATE RE-ROLLOUT (Vòng {current_attempt}): Đã thử vi phẫu cục bộ nhưng lỗi vẫn tồn đọng. "
                "Kernel kích hoạt làm sạch toàn bộ cache và artifacts tạm thời, tái cấu trúc từ đầu: "
                "Agent 1 -> Agent 2 -> Agent 3 -> Agent 4 để tái đồng bộ ngữ cảnh hoàn hảo."
            ),
        )
        return HealingStrategy.CLEAN_SLATE_RESET, directive

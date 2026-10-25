# -*- coding: utf-8 -*-
"""
Finite State Machine (FSM) Engine for Central Orchestrator
Hiện thực hóa Máy Trạng Thái Hữu Hạn điều phối luồng thực thi liên tác nhân:
- Thuật toán 11 (H-LCC Scan Engine & FSM-SCG)
- Quản lý trạng thái chuyển đổi đơn hướng, chống rẽ nhánh bất hợp lệ
- Nhật ký vết trạng thái có gắn dấu thời gian ISO 8601
"""

import datetime
from enum import Enum
from typing import List, Dict, Any, Optional, Set
from pydantic import BaseModel, Field


class FSMState(str, Enum):
    """Tập trạng thái hữu hạn của Bộ Điều Phối Trung Tâm."""
    IDLE = "IDLE"
    EXTRACTING_BLUEPRINT = "EXTRACTING_BLUEPRINT"
    GENERATING_ASSETS = "GENERATING_ASSETS"
    AUTHORING_DRAFT = "AUTHORING_DRAFT"
    AUDITING_QUALITY = "AUDITING_QUALITY"
    LOCAL_SELF_HEALING = "LOCAL_SELF_HEALING"
    CLEAN_SLATE_RESET = "CLEAN_SLATE_RESET"
    SAMPLE_GATE_WAIT = "SAMPLE_GATE_WAIT"
    COMPLETED = "COMPLETED"
    FAIL_SAFE_HALTED = "FAIL_SAFE_HALTED"


class FSMTransition(BaseModel):
    """Bản ghi vết chuyển dịch trạng thái FSM."""
    from_state: FSMState
    to_state: FSMState
    timestamp: str = Field(default_factory=lambda: datetime.datetime.now().isoformat())
    reason: str = ""
    metadata: Dict[str, Any] = Field(default_factory=dict)


class FSMMachine:
    """
    Máy Trạng Thái Hữu Hạn (FSM Controller) điều phối luồng làm việc của Orchestration Kernel.
    Bảo đảm quy tắc chuyển dịch trạng thái đơn hướng và kiểm soát nghiêm ngặt các ranh giới.
    """

    # Ma trận chuyển dịch hợp lệ: current_state -> set(allowed_next_states)
    VALID_TRANSITIONS: Dict[FSMState, Set[FSMState]] = {
        FSMState.IDLE: {
            FSMState.EXTRACTING_BLUEPRINT,
            FSMState.GENERATING_ASSETS,
            FSMState.AUTHORING_DRAFT,
            FSMState.AUDITING_QUALITY,
            FSMState.CLEAN_SLATE_RESET,
        },
        FSMState.EXTRACTING_BLUEPRINT: {
            FSMState.GENERATING_ASSETS,
            FSMState.LOCAL_SELF_HEALING,
            FSMState.CLEAN_SLATE_RESET,
            FSMState.FAIL_SAFE_HALTED,
        },
        FSMState.GENERATING_ASSETS: {
            FSMState.AUTHORING_DRAFT,
            FSMState.LOCAL_SELF_HEALING,
            FSMState.CLEAN_SLATE_RESET,
            FSMState.FAIL_SAFE_HALTED,
        },
        FSMState.AUTHORING_DRAFT: {
            FSMState.AUDITING_QUALITY,
            FSMState.LOCAL_SELF_HEALING,
            FSMState.CLEAN_SLATE_RESET,
            FSMState.FAIL_SAFE_HALTED,
        },
        FSMState.AUDITING_QUALITY: {
            FSMState.LOCAL_SELF_HEALING,
            FSMState.CLEAN_SLATE_RESET,
            FSMState.SAMPLE_GATE_WAIT,
            FSMState.COMPLETED,
            FSMState.FAIL_SAFE_HALTED,
        },
        FSMState.LOCAL_SELF_HEALING: {
            FSMState.GENERATING_ASSETS,
            FSMState.AUTHORING_DRAFT,
            FSMState.AUDITING_QUALITY,
            FSMState.CLEAN_SLATE_RESET,
            FSMState.FAIL_SAFE_HALTED,
        },
        FSMState.CLEAN_SLATE_RESET: {
            FSMState.EXTRACTING_BLUEPRINT,
            FSMState.FAIL_SAFE_HALTED,
        },
        FSMState.SAMPLE_GATE_WAIT: {
            FSMState.EXTRACTING_BLUEPRINT,
            FSMState.COMPLETED,
            FSMState.IDLE,
        },
        FSMState.COMPLETED: {
            FSMState.IDLE,
            FSMState.EXTRACTING_BLUEPRINT,
            FSMState.SAMPLE_GATE_WAIT,
        },
        FSMState.FAIL_SAFE_HALTED: {
            FSMState.IDLE,  # Chỉ cho phép reset thủ công
        },
    }

    def __init__(self, initial_state: FSMState = FSMState.IDLE):
        self._current_state: FSMState = initial_state
        self._history: List[FSMTransition] = []
        self._record_transition(FSMState.IDLE, initial_state, "Khởi tạo máy trạng thái FSM")

    @property
    def current_state(self) -> FSMState:
        return self._current_state

    @property
    def history(self) -> List[FSMTransition]:
        return list(self._history)

    def can_transition(self, to_state: FSMState) -> bool:
        """Kiểm tra xem chuyển dịch từ trạng thái hiện tại sang to_state có hợp lệ không."""
        allowed = self.VALID_TRANSITIONS.get(self._current_state, set())
        return to_state in allowed

    def transition_to(
        self,
        to_state: FSMState,
        reason: str = "",
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Thực hiện chuyển dịch trạng thái.
        Ném ValueError nếu chuyển dịch vi phạm ma trận trạng thái hợp lệ.
        """
        if not self.can_transition(to_state):
            err_msg = (
                f"LỖI CHUYỂN DỊCH FSM BẤT HỢP LỆ: Không thể chuyển từ "
                f"'{self._current_state.value}' sang '{to_state.value}'. "
                f"Các trạng thái cho phép: {[s.value for s in self.VALID_TRANSITIONS.get(self._current_state, set())]}"
            )
            raise ValueError(err_msg)

        from_state = self._current_state
        self._current_state = to_state
        self._record_transition(from_state, to_state, reason, metadata or {})
        return True

    def _record_transition(
        self,
        from_state: FSMState,
        to_state: FSMState,
        reason: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        transition = FSMTransition(
            from_state=from_state,
            to_state=to_state,
            reason=reason,
            metadata=metadata or {}
        )
        self._history.append(transition)

    def reset_to_idle(self, reason: str = "Thủ công reset về IDLE") -> None:
        """Buộc đặt lại máy trạng thái về IDLE khi cần khởi động phiên mới."""
        from_state = self._current_state
        self._current_state = FSMState.IDLE
        self._record_transition(from_state, FSMState.IDLE, reason, {"manual_reset": True})

    def export_history(self) -> List[Dict[str, Any]]:
        """Xuất nhật ký chuyển dịch FSM dưới dạng danh sách từ điển."""
        return [t.model_dump() for t in self._history]

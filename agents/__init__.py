# -*- coding: utf-8 -*-
"""
Package root for Standalone Autonomous AI Agents (v2.0)
Hỗ trợ cả 2 chuẩn import:
- import agents.common / import agents.schemas
- python -m agents.<agent_name>
"""

import sys
import os

# Thêm thư mục .agents vào sys.path để liên kết các module cốt lõi
_dot_agents = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".agents"))
if _dot_agents not in sys.path:
    sys.path.insert(0, _dot_agents)

try:
    import common as _common
    import schemas as _schemas

    sys.modules["agents.common"] = _common
    sys.modules["agents.schemas"] = _schemas
    common = _common
    schemas = _schemas
except ImportError as e:
    pass

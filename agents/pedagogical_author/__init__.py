# -*- coding: utf-8 -*-
"""
Pedagogical Author Package (Agent 3 - Autonomous Pedagogical Monograph Author)
Triển khai UFME (Thuật toán 5), MALAE 3 Cấp (Thuật toán 12) và Static AST Linter (Thuật toán 8 Trạm 1).
"""

from .author import PedagogicalAuthor, UFMEEngine, MALAEEngine, CausalFlowchainCompiler

__all__ = [
    "PedagogicalAuthor",
    "UFMEEngine",
    "MALAEEngine",
    "CausalFlowchainCompiler",
]

# -*- coding: utf-8 -*-
"""
Package physics_graphic_artist (Agent 2)
Chuyên trách mô phỏng giải tích bán dẫn 300 K, bóc tách ảnh gốc D-SAFE
và khóa bố cục đồ họa ZT-GVLE theo chuẩn MATLAB R2014b+ cho Google Antigravity.
"""

from agents.physics_graphic_artist.artist import (
    PhysicsGraphicArtist,
    MATLAB_PALETTE,
    MATLAB_COLORS
)

__all__ = [
    "PhysicsGraphicArtist",
    "MATLAB_PALETTE",
    "MATLAB_COLORS",
]

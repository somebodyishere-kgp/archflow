from __future__ import annotations

from pydantic import BaseModel


class SpatialMetrics(BaseModel):
    openness_score: float
    compression_ratio: float
    visual_focus_index: float
    circulation_complexity: float

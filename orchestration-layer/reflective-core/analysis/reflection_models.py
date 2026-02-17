from __future__ import annotations

from pydantic import BaseModel


class ReflectionInsight(BaseModel):
    pipeline_id: str
    capability_count: int
    pattern_signature: str

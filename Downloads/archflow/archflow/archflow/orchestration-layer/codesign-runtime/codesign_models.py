from __future__ import annotations

from pydantic import BaseModel


class CoDesignState(BaseModel):
    context_id: str
    revision: int
    recent_deltas: list[dict]
    suggestion_count: int

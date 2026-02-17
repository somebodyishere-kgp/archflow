from __future__ import annotations

from pydantic import BaseModel


class SnapshotContext(BaseModel):
    proposal_id: str
    execution_id: str
    node_count: int
    lineage_depth: int

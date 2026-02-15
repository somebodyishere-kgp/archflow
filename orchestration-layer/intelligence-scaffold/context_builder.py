from __future__ import annotations

from intelligence_models import SnapshotContext


def build_context(
    proposal_id: str,
    execution_id: str,
    node_count: int,
    lineage_depth: int,
) -> SnapshotContext:
    return SnapshotContext(
        proposal_id=proposal_id,
        execution_id=execution_id,
        node_count=node_count,
        lineage_depth=lineage_depth,
    )

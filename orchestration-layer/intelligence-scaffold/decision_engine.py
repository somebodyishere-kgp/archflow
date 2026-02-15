from __future__ import annotations

from intelligence_models import SnapshotContext


def deterministic_decision_summary(context: SnapshotContext) -> dict:
    return {
        "proposal_id": context.proposal_id,
        "execution_id": context.execution_id,
        "status": "context-ready",
        "lineage_depth": context.lineage_depth,
        "node_count": context.node_count,
    }

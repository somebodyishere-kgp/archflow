from __future__ import annotations


def index_reflections(insights: list[dict]) -> dict:
    return {"insight_ids": [insight.get("pipeline_id", "unknown") for insight in insights], "count": len(insights)}

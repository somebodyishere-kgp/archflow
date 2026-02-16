from __future__ import annotations


def build_pattern_memory(patterns: list[dict]) -> dict:
    nodes = []
    for pattern in patterns:
        nodes.append({"id": pattern.get("pipeline_id", "unknown"), "pattern": pattern.get("pattern_signature", "")})
    return {"nodes": nodes, "edges": []}

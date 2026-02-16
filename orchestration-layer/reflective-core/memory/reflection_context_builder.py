from __future__ import annotations


def build_reflection_context(history_index: dict, pattern_graph: dict) -> dict:
    return {
        "history_count": history_index.get("count", 0),
        "pattern_node_count": len(pattern_graph.get("nodes", [])),
    }

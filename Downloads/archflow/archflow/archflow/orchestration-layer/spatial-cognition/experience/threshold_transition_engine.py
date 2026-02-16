from __future__ import annotations


def estimate_threshold_transitions(path_count: int, node_count: int) -> dict:
    return {"transition_density": round(path_count / max(1, node_count), 3)}

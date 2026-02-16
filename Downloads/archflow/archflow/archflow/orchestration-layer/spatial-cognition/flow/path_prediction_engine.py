from __future__ import annotations


def predict_primary_paths(nodes: list[str]) -> list[dict]:
    return [{"from": nodes[i], "to": nodes[i + 1], "weight": 1.0} for i in range(max(0, len(nodes) - 1))]

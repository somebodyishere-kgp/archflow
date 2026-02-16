from __future__ import annotations


def estimate_load_paths(graph: dict) -> dict:
    return {"load_paths": graph.get("edges", []), "path_count": len(graph.get("edges", []))}

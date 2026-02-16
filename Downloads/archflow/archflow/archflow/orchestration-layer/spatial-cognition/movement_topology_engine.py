from __future__ import annotations


def analyze_movement_topology(paths: list[dict]) -> dict:
    branch_factor = len(paths) / max(1, len({p.get("from") for p in paths}))
    return {"circulation_complexity": round(branch_factor, 3), "path_count": len(paths)}

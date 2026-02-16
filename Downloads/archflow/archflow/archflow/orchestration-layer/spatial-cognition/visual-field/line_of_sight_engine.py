from __future__ import annotations


def estimate_line_of_sight(cones: list[dict], blockers: int) -> dict:
    visible_ratio = max(0.0, min(1.0, 1 - blockers / max(1, len(cones) * 3)))
    return {"visible_ratio": round(visible_ratio, 3), "blocker_count": blockers}

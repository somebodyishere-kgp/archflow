from __future__ import annotations


def estimate_atmosphere(openness_score: float, visual_focus_index: float) -> dict:
    return {"atmosphere_index": round((openness_score + visual_focus_index) / 2, 3)}

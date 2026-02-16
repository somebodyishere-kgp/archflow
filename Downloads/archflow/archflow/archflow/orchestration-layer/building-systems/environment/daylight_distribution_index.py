from __future__ import annotations


def estimate_daylight_distribution(openness_score: float, urban_porosity: float) -> dict:
    return {"daylight_distribution_index": round((openness_score * 0.6) + (urban_porosity * 0.4), 3)}

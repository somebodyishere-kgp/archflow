from __future__ import annotations


def predict_passive_cooling(wind_exposure_score: float, urban_porosity: float) -> dict:
    score = round((wind_exposure_score * 0.6) + (urban_porosity * 0.4), 3)
    return {"passive_cooling_score": score, "recommended_strategy": "cross-ventilation" if score > 0.55 else "stack-assisted"}

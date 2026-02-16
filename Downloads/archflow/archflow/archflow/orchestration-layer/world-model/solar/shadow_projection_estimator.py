from __future__ import annotations


def estimate_shadow_factor(height_mm: int, solar_band: str) -> dict:
    multiplier = 1.4 if solar_band == "high" else 1.1
    return {"shadow_projection_mm": int(height_mm * multiplier)}

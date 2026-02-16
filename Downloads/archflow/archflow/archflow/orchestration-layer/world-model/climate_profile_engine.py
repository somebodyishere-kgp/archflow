from __future__ import annotations


def derive_climate_profile(region: str) -> dict:
    key = region.lower()
    return {
        "region": region,
        "solar_priority_index": 0.8 if "tropic" in key else 0.6,
        "wind_exposure_score": 0.7 if "coastal" in key else 0.5,
    }

from __future__ import annotations


def estimate_wind_channels(wind_exposure_score: float) -> dict:
    channel_count = 3 if wind_exposure_score > 0.6 else 2
    return {"channel_count": channel_count, "dominant_vector": "north-east"}

from __future__ import annotations


def derive_cross_ventilation_channels(flow_intensity: float, wind_score: float) -> dict:
    channel_count = max(1, int(round((flow_intensity + wind_score) * 3)))
    return {"ventilation_channel_count": channel_count}

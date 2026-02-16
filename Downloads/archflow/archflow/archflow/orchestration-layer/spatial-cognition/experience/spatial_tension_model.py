from __future__ import annotations


def compute_spatial_tension(compression_ratio: float, circulation_complexity: float) -> dict:
    return {"tension_index": round((compression_ratio * 0.6) + (circulation_complexity * 0.4), 3)}

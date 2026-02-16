from __future__ import annotations


def estimate_shading_need(solar_priority_index: float, thermal_inertia_score: float) -> dict:
    need = round(solar_priority_index * (1.2 - min(1.0, thermal_inertia_score)), 3)
    return {"shading_need_index": need}

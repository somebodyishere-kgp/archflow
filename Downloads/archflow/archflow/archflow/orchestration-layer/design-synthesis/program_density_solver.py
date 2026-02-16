from __future__ import annotations


def solve_program_density(target_density: str, base_area_mm2: int) -> dict:
    factor = {"low": 0.8, "balanced": 1.0, "high": 1.2}.get(target_density, 1.0)
    return {"density_factor": factor, "effective_area_mm2": int(base_area_mm2 * factor)}


def adjust_density_by_world_context(density: dict, urban_intensity: float) -> dict:
    adjustment = 1.0 + min(0.3, max(-0.2, urban_intensity - 0.5))
    return {
        **density,
        "world_adjustment_factor": round(adjustment, 3),
        "effective_area_mm2": int(density["effective_area_mm2"] * adjustment),
    }

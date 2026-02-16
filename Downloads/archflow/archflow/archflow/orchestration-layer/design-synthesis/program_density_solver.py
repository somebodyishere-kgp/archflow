from __future__ import annotations


def solve_program_density(target_density: str, base_area_mm2: int) -> dict:
    factor = {"low": 0.8, "balanced": 1.0, "high": 1.2}.get(target_density, 1.0)
    return {"density_factor": factor, "effective_area_mm2": int(base_area_mm2 * factor)}

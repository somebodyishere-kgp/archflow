from __future__ import annotations


def analyze_urban_density(pop_density: float, built_ratio: float) -> dict:
    urban_porosity = round(max(0.0, 1.0 - built_ratio), 3)
    public_flow_intensity = round(min(1.0, (pop_density / 20000)), 3)
    return {"urban_porosity": urban_porosity, "public_flow_intensity": public_flow_intensity}

from __future__ import annotations


def analyze_thermal_mass(material_depth_index: float, solar_priority_index: float) -> dict:
    heat_gain_zone = "high" if solar_priority_index > 0.7 else "medium"
    return {"thermal_mass_need": round(material_depth_index * solar_priority_index, 3), "heat_gain_zone": heat_gain_zone}

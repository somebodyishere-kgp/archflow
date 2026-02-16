from __future__ import annotations


def analyze_mass_distribution(assemblies: list[dict]) -> dict:
    total_thickness = sum(assembly.get("thickness", 0) for assembly in assemblies)
    return {"material_weight_distribution": total_thickness, "assembly_count": len(assemblies)}

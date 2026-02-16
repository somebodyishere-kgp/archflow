from __future__ import annotations


def derive_material_hierarchy(assemblies: list[dict]) -> dict:
    hierarchy = []
    for assembly in assemblies:
        hierarchy.append(
            {
                "assembly_id": assembly.get("assembly_id"),
                "layer_depth_index": len(assembly.get("material_layers", [])),
                "material_layers": assembly.get("material_layers", []),
            }
        )
    return {"material_hierarchy": hierarchy}

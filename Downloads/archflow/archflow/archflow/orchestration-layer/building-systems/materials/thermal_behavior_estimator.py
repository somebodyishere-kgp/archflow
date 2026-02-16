from __future__ import annotations


def estimate_thermal_inertia(material_layers: list[dict]) -> dict:
    depth = sum(layer.get("thickness_mm", 0) for layer in material_layers)
    return {"thermal_inertia_score": round(depth / 300.0, 3), "layer_depth_index": len(material_layers)}

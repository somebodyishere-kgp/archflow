from __future__ import annotations


def estimate_acoustic_isolation(material_layers: list[dict]) -> dict:
    insulation_layers = [layer for layer in material_layers if "insulation" in str(layer.get("material", "")).lower()]
    return {"acoustic_isolation_index": round(0.4 + (0.2 * len(insulation_layers)), 3)}

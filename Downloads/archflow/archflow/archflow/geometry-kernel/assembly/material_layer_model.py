from __future__ import annotations


def make_material_layers(layers: list[tuple[str, int]]) -> list[dict]:
    return [{"material": material, "thickness_mm": thickness} for material, thickness in layers]

from __future__ import annotations

from material_layer_model import make_material_layers


def build_wall_system(assembly_id: str, length_mm: int, height_mm: int) -> dict:
    return {
        "assembly_id": assembly_id,
        "assembly_type": "wall-system",
        "length_mm": length_mm,
        "height_mm": height_mm,
        "material_layers": make_material_layers([("gypsum-board", 15), ("insulation", 80), ("concrete", 150)]),
        "thickness": 245,
        "metadata_version": "xipp-1",
    }

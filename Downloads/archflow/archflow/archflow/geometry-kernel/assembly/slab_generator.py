from __future__ import annotations

from material_layer_model import make_material_layers


def generate_slab(assembly_id: str, area_mm2: int) -> dict:
    return {
        "assembly_id": assembly_id,
        "assembly_type": "slab",
        "area_mm2": area_mm2,
        "material_layers": make_material_layers([("screed", 40), ("reinforced-concrete", 220)]),
        "thickness": 260,
        "metadata_version": "xipp-1",
    }

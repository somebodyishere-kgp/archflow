from __future__ import annotations

from material_layer_model import make_material_layers


def build_facade_shell(assembly_id: str, perimeter_mm: int, height_mm: int) -> dict:
    return {
        "assembly_id": assembly_id,
        "assembly_type": "facade-shell",
        "perimeter_mm": perimeter_mm,
        "height_mm": height_mm,
        "material_layers": make_material_layers([("cladding", 30), ("air-gap", 40), ("backing-wall", 200)]),
        "thickness": 270,
        "metadata_version": "xipp-1",
    }

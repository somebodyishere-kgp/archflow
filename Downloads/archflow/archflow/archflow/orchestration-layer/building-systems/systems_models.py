from __future__ import annotations

from pydantic import BaseModel


class SystemsNode(BaseModel):
    assembly_id: str
    material_layers: list[dict]
    structural_role: str
    environmental_role: str
    metadata_version: str

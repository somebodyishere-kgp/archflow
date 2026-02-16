from __future__ import annotations

from pydantic import BaseModel


class SystemsNode(BaseModel):
    id: str
    entity_type: str
    system_domain: str
    semantic_tags: list[str]


class SystemsEdge(BaseModel):
    source: str
    target: str
    relation_type: str

from __future__ import annotations

from systems_models import SystemsNode


def abstract_entity(node: dict) -> SystemsNode:
    return SystemsNode(
        id=node["id"],
        entity_type=node.get("entity_type", node.get("type", "unknown")),
        system_domain=node.get("system_domain", "generic"),
        semantic_tags=sorted(node.get("semantic_tags", [])),
    )

from __future__ import annotations

from typing import Any


def preserve_topology_identity(
    previous_topology: dict[str, Any],
    rebuilt_topology: dict[str, Any],
) -> dict[str, Any]:
    previous_ids = previous_topology.get("entity_ids", {})
    rebuilt_entities = rebuilt_topology.get("entities", [])
    mapped_entities = []
    for entity in rebuilt_entities:
        local_key = str(entity.get("local_key", entity.get("id", "")))
        stable_id = previous_ids.get(local_key, entity.get("id", local_key))
        mapped_entities.append({**entity, "stable_id": stable_id})
    return {
        "entities": mapped_entities,
        "identity_preserved": True,
    }


def preserve_parametric_bindings(
    bindings: list[dict[str, Any]],
    topology: dict[str, Any],
) -> list[dict[str, Any]]:
    valid_ids = {str(item.get("stable_id", "")) for item in topology.get("entities", [])}
    preserved = []
    for binding in bindings:
        target = str(binding.get("target_id", ""))
        if target in valid_ids:
            preserved.append({**binding, "binding_state": "preserved"})
        else:
            preserved.append({**binding, "binding_state": "orphaned"})
    return preserved

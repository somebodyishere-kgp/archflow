from __future__ import annotations

from systems_models import SystemsEdge


def infer_relationships(nodes: list[dict]) -> list[SystemsEdge]:
    edges: list[SystemsEdge] = []
    for node in nodes:
        for relation in node.get("relations", []):
            target = relation.get("target_id")
            if target:
                edges.append(
                    SystemsEdge(
                        source=node["id"],
                        target=target,
                        relation_type=relation.get("relation_type", "linked"),
                    )
                )
    return sorted(edges, key=lambda e: (e.source, e.target, e.relation_type))

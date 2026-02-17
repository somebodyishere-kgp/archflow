from __future__ import annotations


def generalize_context(systems_graph: dict) -> dict:
    topology = systems_graph.get("topology", {})
    return {
        "node_count": topology.get("node_count", 0),
        "edge_count": topology.get("edge_count", 0),
        "domains": topology.get("domains", []),
    }

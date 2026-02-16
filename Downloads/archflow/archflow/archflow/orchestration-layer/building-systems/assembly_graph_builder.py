from __future__ import annotations


def build_assembly_graph(assemblies: list[dict]) -> dict:
    nodes = [assembly.get("assembly_id") for assembly in assemblies]
    edges = [{"from": nodes[i], "to": nodes[i + 1], "relation": "connects"} for i in range(max(0, len(nodes) - 1))]
    return {"nodes": nodes, "edges": edges}

from __future__ import annotations


def build_visibility_graph(spaces: list[dict]) -> dict:
    nodes = [space.get("id", f"space-{idx}") for idx, space in enumerate(spaces)]
    edges = [{"from": nodes[i], "to": nodes[i + 1]} for i in range(len(nodes) - 1)]
    return {"nodes": nodes, "edges": edges, "visual_focus_index": round(len(edges) / max(1, len(nodes)), 3)}

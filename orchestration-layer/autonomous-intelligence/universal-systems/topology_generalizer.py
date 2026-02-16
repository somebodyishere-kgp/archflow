from __future__ import annotations


def generalize_topology(nodes: list[dict], edges: list[dict]) -> dict:
    domains = sorted({node.get("system_domain", "generic") for node in nodes})
    return {
        "domain_count": len(domains),
        "domains": domains,
        "node_count": len(nodes),
        "edge_count": len(edges),
    }

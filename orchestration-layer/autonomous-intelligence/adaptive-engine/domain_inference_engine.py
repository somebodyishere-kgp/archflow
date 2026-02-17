from __future__ import annotations


def infer_domain(systems_graph: dict) -> str:
    domains = systems_graph.get("topology", {}).get("domains", [])
    if len(domains) == 1:
        return domains[0]
    if len(domains) > 1:
        return "multi-domain"
    return "generic"

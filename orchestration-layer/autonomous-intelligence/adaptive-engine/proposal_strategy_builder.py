from __future__ import annotations


def build_strategy(domain: str, context_summary: dict) -> dict:
    return {
        "domain": domain,
        "strategy": "generic-optimization",
        "weight": max(1, context_summary.get("node_count", 0)),
    }

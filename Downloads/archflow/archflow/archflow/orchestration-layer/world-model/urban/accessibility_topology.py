from __future__ import annotations


def build_accessibility_topology(primary_edge: str, attractor_count: int) -> dict:
    return {"primary_entry_edge": primary_edge, "frontage_hierarchy": ["primary", "secondary"][: max(1, min(2, attractor_count))]}

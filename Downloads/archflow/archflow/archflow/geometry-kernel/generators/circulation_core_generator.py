from __future__ import annotations


def generate_circulation_core(capacity: int, ring_count: int) -> dict:
    corridor_width_mm = 2200 if capacity > 800 else 1800
    egress_paths = max(2, ring_count // 2)
    return {
        "assembly_id": "circulation-core",
        "circulation_rings": ring_count,
        "corridor_width_mm": corridor_width_mm,
        "egress_paths": egress_paths,
        "egress_logic": "deterministic-distribution",
    }

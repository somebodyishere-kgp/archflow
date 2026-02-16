from __future__ import annotations

from egress_logic_engine import derive_egress_logic
from hierarchy_resolver import resolve_spatial_hierarchy
from program_density_solver import solve_program_density


def solve_layout(program: dict, systems_graph: dict) -> dict:
    zones = systems_graph.get("zones", [])
    density = solve_program_density(program.get("target_density", "balanced"), 400000)
    hierarchy = resolve_spatial_hierarchy([{"zone": zone.get("id", "public")} for zone in zones]) if zones else []
    egress = derive_egress_logic(program.get("capacity", 500))
    return {
        "layout_id": f"layout-{program.get('program_type', 'generic')}",
        "zones": zones,
        "strategy": "deterministic-grid",
        "hierarchy": hierarchy,
        "density": density,
        "egress": egress,
    }

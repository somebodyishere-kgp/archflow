from __future__ import annotations

from egress_logic_engine import derive_egress_logic
from hierarchy_resolver import resolve_spatial_hierarchy
from program_density_solver import adjust_density_by_world_context, solve_program_density


def solve_layout(program: dict, systems_graph: dict) -> dict:
    zones = systems_graph.get("zones", [])
    density = solve_program_density(program.get("target_density", "balanced"), 400000)
    world_context = program.get("world_context", {})
    density = adjust_density_by_world_context(density, world_context.get("urban_intensity", 0.5))
    hierarchy = resolve_spatial_hierarchy([{"zone": zone.get("id", "public")} for zone in zones]) if zones else []
    egress = derive_egress_logic(program.get("capacity", 500))
    return {
        "layout_id": f"layout-{program.get('program_type', 'generic')}",
        "zones": zones,
        "strategy": "deterministic-grid",
        "orientation_hint": world_context.get("preferred_orientation", "north-south"),
        "entry_shift_vector": world_context.get("entry_vector", "north-east"),
        "hierarchy": hierarchy,
        "density": density,
        "egress": egress,
    }

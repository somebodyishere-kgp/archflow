from __future__ import annotations


def generate_auditorium_layout(capacity: int, acoustic_priority: str, zoning_program: dict) -> dict:
    seats_per_ring = max(40, capacity // 12)
    ring_count = max(3, capacity // seats_per_ring)
    aisle_spacing_mm = 1100 if acoustic_priority == "high" else 1000
    return {
        "assembly_id": "auditorium-core",
        "layout_type": "seating-bowl",
        "seat_capacity": capacity,
        "rings": ring_count,
        "seats_per_ring": seats_per_ring,
        "aisle_spacing_mm": aisle_spacing_mm,
        "stage_zone": zoning_program.get("stage_zone", {"width_mm": 18000, "depth_mm": 12000}),
        "backstage_zone": zoning_program.get("backstage_zone", {"width_mm": 12000, "depth_mm": 9000}),
    }

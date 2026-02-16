from __future__ import annotations


def generate_room_clusters(program_density: float, zoning_program: dict) -> list[dict]:
    base_area = max(20000, int(40000 * max(0.5, min(program_density, 2.0))))
    clusters = []
    for idx, zone in enumerate(zoning_program.get("zones", ["public", "service", "support"]), start=1):
        clusters.append(
            {
                "assembly_id": f"cluster-{idx}",
                "zone": zone,
                "target_area_mm2": base_area // idx,
                "metadata_version": "xipp-1",
            }
        )
    return clusters

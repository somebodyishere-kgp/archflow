from __future__ import annotations


def identify_public_attractors(urban_porosity: float, cultural_priority: str) -> dict:
    attractor_count = 3 if urban_porosity > 0.4 else 2
    return {"attractor_count": attractor_count, "priority": cultural_priority}

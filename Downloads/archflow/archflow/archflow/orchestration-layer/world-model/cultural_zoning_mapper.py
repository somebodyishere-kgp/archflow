from __future__ import annotations


def map_cultural_zoning(cultural_tags: list[str]) -> dict:
    priority = "civic" if "public" in [tag.lower() for tag in cultural_tags] else "mixed-use"
    return {"cultural_priority": priority, "cultural_tags": cultural_tags}

from __future__ import annotations


def analyze_scale(space_dimensions: list[dict]) -> dict:
    if not space_dimensions:
        return {"openness_score": 0.0, "compression_ratio": 0.0}
    avg_width = sum(item.get("width_mm", 0) for item in space_dimensions) / len(space_dimensions)
    avg_height = sum(item.get("height_mm", 1) for item in space_dimensions) / len(space_dimensions)
    return {"openness_score": round(avg_width / 10000, 3), "compression_ratio": round(avg_height / max(avg_width, 1), 3)}

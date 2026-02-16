from __future__ import annotations


def generate_grid(total_width_mm: int, total_depth_mm: int, span_mm: int) -> dict:
    x_count = max(2, total_width_mm // span_mm + 1)
    y_count = max(2, total_depth_mm // span_mm + 1)
    return {
        "grid_id": "primary-structural-grid",
        "span_mm": span_mm,
        "x_lines": x_count,
        "y_lines": y_count,
    }

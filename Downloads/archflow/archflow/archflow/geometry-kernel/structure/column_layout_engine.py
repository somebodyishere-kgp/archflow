from __future__ import annotations


def derive_column_layout(grid: dict) -> list[dict]:
    columns = []
    for x_idx in range(grid["x_lines"]):
        for y_idx in range(grid["y_lines"]):
            columns.append(
                {
                    "column_id": f"col-{x_idx}-{y_idx}",
                    "grid_ref": (x_idx, y_idx),
                    "structural_role": "primary" if x_idx in (0, grid["x_lines"] - 1) else "secondary",
                }
            )
    return columns

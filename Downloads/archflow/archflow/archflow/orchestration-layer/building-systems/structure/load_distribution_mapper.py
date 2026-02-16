from __future__ import annotations


def map_load_distribution(columns: list[dict], load_value: float) -> dict:
    if not columns:
        return {"distribution": []}
    distributed = round(load_value / len(columns), 3)
    return {"distribution": [{"column_id": item.get("column_id"), "load": distributed} for item in columns]}

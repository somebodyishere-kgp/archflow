from __future__ import annotations


def detect_bottlenecks(paths: list[dict], threshold: float = 2.0) -> dict:
    heavy = [path for path in paths if path.get("weight", 0) >= threshold]
    return {"bottleneck_count": len(heavy), "bottlenecks": heavy}

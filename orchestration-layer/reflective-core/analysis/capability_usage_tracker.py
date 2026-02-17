from __future__ import annotations


def track_usage(pipelines: list[dict]) -> dict:
    usage: dict[str, int] = {}
    for pipeline in pipelines:
        for capability in pipeline.get("capabilities", []):
            usage[capability] = usage.get(capability, 0) + 1
    return dict(sorted(usage.items()))

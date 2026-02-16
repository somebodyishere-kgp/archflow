from __future__ import annotations


def build_delta_context(previous: dict, current: dict) -> dict:
    changed = {}
    keys = set(previous.keys()) | set(current.keys())
    for key in keys:
        if previous.get(key) != current.get(key):
            changed[key] = {"before": previous.get(key), "after": current.get(key)}
    return {"changed_fields": changed, "change_count": len(changed)}

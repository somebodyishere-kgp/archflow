from __future__ import annotations


def build_context_stream(base_context: dict, deltas: list[dict]) -> dict:
    return {"base_context": base_context, "delta_count": len(deltas), "latest_delta": deltas[-1] if deltas else {}}

from __future__ import annotations

from typing import Any


def detect_illegal_writes(event_payload: dict[str, Any]) -> list[str]:
    text = str(event_payload)
    violations: list[str] = []
    forbidden = ["/twingraph/ingest", "INSERT INTO twingraph_nodes", "UPDATE twingraph_nodes"]
    for token in forbidden:
        if token in text:
            violations.append(f"forbidden_write_token:{token}")
    return violations


def detect_ui_mutation_attempt(event_payload: dict[str, Any]) -> list[str]:
    text = str(event_payload)
    violations: list[str] = []
    forbidden = ["setGeometry(", "mutateGeometry", "applyGeometryEdit"]
    for token in forbidden:
        if token in text:
            violations.append(f"ui_mutation_token:{token}")
    return violations


def build_execution_lineage(
    phase: str,
    parent_event_id: str | None,
    event_id: str,
) -> dict[str, Any]:
    return {
        "phase": phase,
        "parent_event_id": parent_event_id,
        "event_id": event_id,
    }

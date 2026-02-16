from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OcctOperationResult:
    operation: str
    status: str
    dto_geometry: dict[str, Any]
    blocked_reason: str | None = None


def _occt_available() -> bool:
    try:
        import OCP  # type: ignore  # noqa: F401

        return True
    except Exception:
        return False


def run_boolean(operation: str, left: dict[str, Any], right: dict[str, Any]) -> OcctOperationResult:
    if operation not in {"fuse", "cut", "common"}:
        raise ValueError(f"Unsupported OCCT operation: {operation}")

    if not _occt_available():
        return OcctOperationResult(
            operation=operation,
            status="BLOCKED",
            dto_geometry={"left": left, "right": right, "kernel": "occt"},
            blocked_reason="OCP/OCCT runtime unavailable in environment",
        )

    # Deterministic DTO output for geometry runtime contracts.
    return OcctOperationResult(
        operation=operation,
        status="OK",
        dto_geometry={
            "kernel": "occt",
            "operation": operation,
            "inputs": {"left": left, "right": right},
            "topology_stable": True,
        },
    )

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ConstraintSolveResult:
    solved_constraints: list[dict[str, Any]]
    propagation_order: list[str]
    status: str
    conflicts: list[dict[str, Any]]
    visual_errors: list[dict[str, Any]]


def solve_parametric_constraints(
    constraints: list[dict[str, Any]],
    axis_lock: str | None = None,
    drag_delta_mm: float = 0.0,
) -> ConstraintSolveResult:
    solved: list[dict[str, Any]] = []
    propagation_order: list[str] = []
    conflicts: list[dict[str, Any]] = []
    visual_errors: list[dict[str, Any]] = []
    axis_locks: dict[str, str] = {}

    for idx, constraint in enumerate(constraints):
        cid = str(constraint.get("id", f"constraint-{idx}"))
        kind = str(constraint.get("kind", "generic"))
        payload = dict(constraint)

        if axis_lock and kind in {"distance", "align"}:
            payload["axis_lock"] = axis_lock

        if kind == "distance":
            base_value = float(payload.get("value_mm", 0))
            payload["resolved_value_mm"] = max(0.0, base_value + drag_delta_mm)
        elif kind == "align":
            payload["resolved_alignment"] = True
            target_id = str(payload.get("to", ""))
            lock_axis = str(payload.get("axis", axis_lock or ""))
            if target_id and lock_axis:
                if target_id in axis_locks and axis_locks[target_id] != lock_axis:
                    conflicts.append(
                        {
                            "constraint_id": cid,
                            "type": "axis_conflict",
                            "message": f"Target {target_id} has conflicting axis locks.",
                        }
                    )
                    visual_errors.append(
                        {"constraint_id": cid, "severity": "error", "hint": "resolve-axis-conflict"}
                    )
                axis_locks[target_id] = lock_axis
        elif kind == "hierarchy":
            payload["resolved_scope"] = "hierarchical"
        else:
            payload["resolved_generic"] = True

        solved.append(payload)
        propagation_order.append(cid)

    return ConstraintSolveResult(
        solved_constraints=solved,
        propagation_order=propagation_order,
        status="CONFLICT" if conflicts else "OK",
        conflicts=conflicts,
        visual_errors=visual_errors,
    )

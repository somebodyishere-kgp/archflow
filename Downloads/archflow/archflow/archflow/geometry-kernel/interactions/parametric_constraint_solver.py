from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ConstraintSolveResult:
    solved_constraints: list[dict[str, Any]]
    propagation_order: list[str]
    status: str


def solve_parametric_constraints(
    constraints: list[dict[str, Any]],
    axis_lock: str | None = None,
) -> ConstraintSolveResult:
    solved: list[dict[str, Any]] = []
    propagation_order: list[str] = []

    for idx, constraint in enumerate(constraints):
        cid = str(constraint.get("id", f"constraint-{idx}"))
        kind = str(constraint.get("kind", "generic"))
        payload = dict(constraint)

        if axis_lock and kind in {"distance", "align"}:
            payload["axis_lock"] = axis_lock

        if kind == "distance":
            payload["resolved_value_mm"] = float(payload.get("value_mm", 0))
        elif kind == "align":
            payload["resolved_alignment"] = True
        elif kind == "hierarchy":
            payload["resolved_scope"] = "hierarchical"
        else:
            payload["resolved_generic"] = True

        solved.append(payload)
        propagation_order.append(cid)

    return ConstraintSolveResult(
        solved_constraints=solved,
        propagation_order=propagation_order,
        status="OK",
    )

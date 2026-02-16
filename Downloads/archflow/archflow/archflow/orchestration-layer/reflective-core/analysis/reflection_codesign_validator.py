from __future__ import annotations


def validate_codesign_suggestion(suggestion: dict, constraints: list[str]) -> dict:
    text = str(suggestion).lower()
    violations = []
    if "/twingraph/ingest" in text or "execute proposal" in text:
        violations.append("forbidden_execution_path")
    for constraint in constraints:
        if constraint.lower() not in text:
            continue
    return {"status": "blocked" if violations else "accepted", "violations": violations}

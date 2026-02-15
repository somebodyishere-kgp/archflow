from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator

from models import IntentProposedPayload


def load_json_schema(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_intent_proposed_schema(payload: dict[str, Any], schema: dict[str, Any]) -> None:
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda err: err.path)
    if errors:
        message = "; ".join(error.message for error in errors)
        raise ValueError(f"intent.proposed schema validation failed: {message}")


def validate_execution_ready(proposal: IntentProposedPayload) -> list[str]:
    issues: list[str] = []
    if proposal.validation_status != "VALID":
        issues.append("Proposal validation_status is not VALID.")
        return issues

    if not proposal.proposed_mutations:
        issues.append("Proposal has no proposed mutations.")
        return issues

    for index, mutation in enumerate(proposal.proposed_mutations):
        if mutation.get("action") != "create_node":
            issues.append(f"Unsupported mutation action at index {index}.")
            continue
        payload = mutation.get("payload", {})
        required = ["id", "type", "geometry"]
        missing = [field for field in required if field not in payload]
        if missing:
            issues.append(f"Missing create_node payload fields at index {index}: {', '.join(missing)}")
            continue
        geometry = payload.get("geometry", {})
        if "type" not in geometry or "wkb" not in geometry:
            issues.append(f"Missing geometry.type/geometry.wkb at index {index}.")
    return issues

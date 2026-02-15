from __future__ import annotations

from typing import Any

import httpx

from intent_models import IntentRequest
from intent_parser import required_keys_for_intent


def validate_intent_schema(intent: IntentRequest) -> list[str]:
    errors: list[str] = []
    required = required_keys_for_intent(intent.intent_type)
    for key in required:
        if key not in intent.parameters:
            errors.append(f"Missing required parameter: {key}")
    return errors


def validate_twingraph_context(intent: IntentRequest, twingraph_base_url: str) -> list[str]:
    errors: list[str] = []
    params = intent.parameters

    # Deterministic context checks via existing read API only.
    try:
        with httpx.Client(timeout=5.0) as client:
            if intent.intent_type == "create_space":
                relative_to = params.get("relative_to")
                if relative_to:
                    resp = client.get(f"{twingraph_base_url}/twingraph/node/{relative_to}")
                    if resp.status_code != 200:
                        errors.append(f"Reference node not found: {relative_to}")

            if intent.intent_type in {"update_metadata", "tag_zone"}:
                node_id = params.get("node_id")
                if node_id:
                    resp = client.get(f"{twingraph_base_url}/twingraph/node/{node_id}")
                    if resp.status_code != 200:
                        errors.append(f"Target node not found: {node_id}")
    except httpx.HTTPError as exc:
        errors.append(f"TwinGraph query verification failed: {exc.__class__.__name__}")

    return errors

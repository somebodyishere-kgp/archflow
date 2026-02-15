from __future__ import annotations

from intent_models import IntentRequest, ProposedMutation


def parse_intent_to_mutations(intent: IntentRequest) -> list[ProposedMutation]:
    params = intent.parameters

    if intent.intent_type == "create_space":
        return [
            ProposedMutation(
                action="create_node",
                target="twingraph.node",
                payload={
                    "type": params["type"],
                    "count": params["count"],
                    "relative_to": params["relative_to"],
                },
            )
        ]

    if intent.intent_type == "update_metadata":
        return [
            ProposedMutation(
                action="update_node_metadata",
                target=f"twingraph.node.{params['node_id']}",
                payload={
                    "metadata": params["metadata"],
                },
            )
        ]

    if intent.intent_type == "tag_zone":
        return [
            ProposedMutation(
                action="tag_node_zone",
                target=f"twingraph.node.{params['node_id']}",
                payload={
                    "zone_tag": params["zone_tag"],
                },
            )
        ]

    raise ValueError(f"Unsupported intent type: {intent.intent_type}")


def required_keys_for_intent(intent_type: str) -> list[str]:
    mapping: dict[str, list[str]] = {
        "create_space": ["type", "count", "relative_to"],
        "update_metadata": ["node_id", "metadata"],
        "tag_zone": ["node_id", "zone_tag"],
    }
    if intent_type not in mapping:
        raise ValueError(f"Unsupported intent type: {intent_type}")
    return mapping[intent_type]

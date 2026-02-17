from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI

from intent_models import IntentProposedEvent, IntentProposal, IntentRequest
from intent_parser import parse_intent_to_mutations
from validation import validate_intent_schema, validate_twingraph_context


class LocalIntentEventStore:
    def __init__(self, output_path: Path | None = None) -> None:
        self.output_path = output_path
        self._events: list[dict[str, Any]] = []

    def emit(self, event_name: str, payload: dict[str, Any]) -> None:
        event = {"event_name": event_name, "payload": payload}
        self._events.append(event)
        if self.output_path:
            self.output_path.parent.mkdir(parents=True, exist_ok=True)
            with self.output_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(event) + "\n")

    def snapshot(self) -> list[dict[str, Any]]:
        return list(self._events)


def create_app(
    twingraph_base_url: str,
    event_output_path: Path | None = None,
) -> FastAPI:
    app = FastAPI(title="Intent Gateway", version="0.5.0")
    event_store = LocalIntentEventStore(event_output_path)

    @app.post("/intent/propose")
    def propose_intent(intent: IntentRequest) -> dict[str, Any]:
        schema_errors = validate_intent_schema(intent)
        context_errors = validate_twingraph_context(intent, twingraph_base_url)
        errors = [*schema_errors, *context_errors]

        proposed_mutations = parse_intent_to_mutations(intent) if not schema_errors else []
        status = "BLOCKED" if errors else "VALID"

        proposal = IntentProposal.build(
            intent_type=intent.intent_type,
            proposed_mutations=proposed_mutations,
            validation_status=status,
            reasons=errors,
        )
        event_payload = IntentProposedEvent.from_proposal(proposal).model_dump()
        event_store.emit("intent.proposed", event_payload)

        return proposal.model_dump()

    @app.get("/intent/events/audit")
    def intent_events_audit() -> dict[str, Any]:
        return {"count": len(event_store.snapshot()), "events": event_store.snapshot()}

    return app

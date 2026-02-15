from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

import httpx

from models import (
    IntentProposedPayload,
    ProposalBlockedPayload,
    ProposalExecutedPayload,
    TwinGraphMutationRequest,
)
from transport_adapter import LocalTransportAdapter
from validation import (
    load_json_schema,
    validate_execution_ready,
    validate_intent_proposed_schema,
)


class ProposalExecutor:
    def __init__(
        self,
        twingraph_base_url: str,
        intent_gateway_base_url: str,
        intent_schema_path: Path,
        event_output_path: Path | None = None,
    ) -> None:
        self.twingraph_base_url = twingraph_base_url.rstrip("/")
        self.transport = LocalTransportAdapter(intent_gateway_base_url)
        self.intent_schema = load_json_schema(intent_schema_path)
        self.event_output_path = event_output_path
        self._executed_events: list[dict[str, Any]] = []

    @property
    def executed_events(self) -> list[dict[str, Any]]:
        return list(self._executed_events)

    def run_once(self) -> list[dict[str, Any]]:
        events = self.transport.poll_intent_events()
        for event in events:
            payload = event.get("payload", {})
            self._handle_intent_proposed(payload, event.get("event_id"))
        return self.executed_events

    def _handle_intent_proposed(
        self,
        payload: dict[str, Any],
        parent_event_id: str | None,
    ) -> None:
        validate_intent_proposed_schema(payload, self.intent_schema)
        proposal = IntentProposedPayload(**payload)
        issues = validate_execution_ready(proposal)
        execution_id = f"exec-{uuid4()}"
        if issues:
            blocked = ProposalBlockedPayload(
                proposal_id=proposal.proposal_id,
                execution_id=execution_id,
                timestamp=datetime.now(UTC).isoformat(),
                reasons=issues,
            )
            self._emit("proposal.blocked", blocked.model_dump(), parent_event_id=parent_event_id)
            return

        mutation_requests = self._to_twingraph_requests(proposal)
        with httpx.Client(timeout=10.0) as client:
            for req in mutation_requests:
                response = client.post(
                    f"{self.twingraph_base_url}/twingraph/ingest",
                    json={
                        "proposal_id": proposal.proposal_id,
                        "execution_id": execution_id,
                        "intent_source": proposal.intent_type,
                        "parent_event_id": parent_event_id,
                        "node": req.node,
                    },
                )
                response.raise_for_status()

        executed = ProposalExecutedPayload(
            proposal_id=proposal.proposal_id,
            execution_id=execution_id,
            timestamp=datetime.now(UTC).isoformat(),
            executed_mutation_requests=[req.model_dump() for req in mutation_requests],
            execution_status="EXECUTED",
        )
        self._emit("proposal.executed", executed.model_dump(), parent_event_id=parent_event_id)

    def _to_twingraph_requests(
        self, proposal: IntentProposedPayload
    ) -> list[TwinGraphMutationRequest]:
        requests: list[TwinGraphMutationRequest] = []
        for index, mutation in enumerate(proposal.proposed_mutations):
            requests.append(
                TwinGraphMutationRequest(
                    source_proposal_id=proposal.proposal_id,
                    mutation_index=index,
                    node=mutation["payload"],
                )
            )
        return requests

    def _emit(
        self,
        event_name: str,
        payload: dict[str, Any],
        parent_event_id: str | None = None,
    ) -> None:
        event = {
            "event_id": str(uuid4()),
            "parent_event_id": parent_event_id,
            "source_module": "proposal-executor",
            "event_name": event_name,
            "payload": payload,
            "timestamp": datetime.now(UTC).isoformat(),
        }
        self._executed_events.append(event)
        if self.event_output_path:
            self.event_output_path.parent.mkdir(parents=True, exist_ok=True)
            with self.event_output_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(event) + "\n")

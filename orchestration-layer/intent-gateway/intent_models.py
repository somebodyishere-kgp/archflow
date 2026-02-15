from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field


IntentType = Literal["create_space", "update_metadata", "tag_zone"]
ValidationStatus = Literal["VALID", "BLOCKED"]


class IntentRequest(BaseModel):
    intent_type: IntentType
    parameters: dict[str, Any] = Field(default_factory=dict)


class ProposedMutation(BaseModel):
    action: str
    target: str
    payload: dict[str, Any]


class IntentProposal(BaseModel):
    proposal_id: str
    intent_type: IntentType
    proposed_mutations: list[ProposedMutation]
    validation_status: ValidationStatus
    reasons: list[str] = Field(default_factory=list)

    @classmethod
    def build(
        cls,
        intent_type: IntentType,
        proposed_mutations: list[ProposedMutation],
        validation_status: ValidationStatus,
        reasons: list[str] | None = None,
    ) -> "IntentProposal":
        return cls(
            proposal_id=f"proposal-{uuid4()}",
            intent_type=intent_type,
            proposed_mutations=proposed_mutations,
            validation_status=validation_status,
            reasons=reasons or [],
        )


class IntentProposedEvent(BaseModel):
    proposal_id: str
    intent_type: IntentType
    proposed_mutations: list[dict[str, Any]]
    validation_status: ValidationStatus
    timestamp: str

    @classmethod
    def from_proposal(cls, proposal: IntentProposal) -> "IntentProposedEvent":
        return cls(
            proposal_id=proposal.proposal_id,
            intent_type=proposal.intent_type,
            proposed_mutations=[m.model_dump() for m in proposal.proposed_mutations],
            validation_status=proposal.validation_status,
            timestamp=datetime.now(UTC).isoformat(),
        )

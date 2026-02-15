from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field


ValidationStatus = Literal["VALID", "BLOCKED"]


class IntentProposedPayload(BaseModel):
    proposal_id: str
    intent_type: str
    proposed_mutations: list[dict[str, Any]]
    validation_status: ValidationStatus
    timestamp: str


class TwinGraphMutationRequest(BaseModel):
    source_proposal_id: str
    mutation_index: int
    node: dict[str, Any]


class ProposalExecutedPayload(BaseModel):
    proposal_id: str
    execution_id: str = Field(default_factory=lambda: f"exec-{uuid4()}")
    timestamp: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
    executed_mutation_requests: list[dict[str, Any]]
    execution_status: Literal["EXECUTED", "SKIPPED"]


class ProposalBlockedPayload(BaseModel):
    proposal_id: str
    execution_id: str = Field(default_factory=lambda: f"exec-{uuid4()}")
    timestamp: str = Field(default_factory=lambda: datetime.now(UTC).isoformat())
    reasons: list[str]

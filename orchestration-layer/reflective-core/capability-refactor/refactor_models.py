from __future__ import annotations

from pydantic import BaseModel


class CapabilityRefactorProposal(BaseModel):
    proposal_id: str
    action: str
    capabilities: list[str]
    rationale: str

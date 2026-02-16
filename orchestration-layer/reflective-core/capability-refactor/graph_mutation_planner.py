from __future__ import annotations

from uuid import uuid4

from refactor_models import CapabilityRefactorProposal


def propose_refactor(redundant_capabilities: list[str]) -> CapabilityRefactorProposal:
    action = "merge" if len(redundant_capabilities) > 1 else "review"
    return CapabilityRefactorProposal(
        proposal_id=f"cap-refactor-{uuid4()}",
        action=action,
        capabilities=redundant_capabilities,
        rationale="detected structural redundancy in capability usage patterns",
    )

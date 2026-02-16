from __future__ import annotations

from llm_adapter.llm_client import run_llm_reasoning
from llm_adapter.llm_models import LLMRequest
from realtime.context_stream_builder import build_context_stream
from realtime.suggestion_scheduler import schedule_suggestion_ticks


def generate_realtime_suggestion(context_id: str, base_context: dict, deltas: list[dict], provider: str = "openai") -> dict:
    stream = build_context_stream(base_context, deltas)
    schedule = schedule_suggestion_ticks(len(deltas))
    payload = run_llm_reasoning(
        LLMRequest(
            provider=provider,
            prompt=f"Realtime context: {stream}",
            context_id=context_id,
        )
    )
    return {
        "event_name": "design.suggestion.generated",
        "context_id": context_id,
        "schedule": schedule,
        "reasoning": payload,
    }

from __future__ import annotations


def analyze_pipeline(pipeline: dict) -> dict:
    capabilities = pipeline.get("capabilities", [])
    return {
        "pipeline_id": pipeline.get("pipeline_id", "unknown"),
        "capability_count": len(capabilities),
        "structure": sorted(capabilities),
    }

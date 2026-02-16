from __future__ import annotations


def analyze_space_sequence(sequence: list[str]) -> dict:
    return {"sequence_length": len(sequence), "transition_intensity": round(len(sequence) / 5.0, 3)}

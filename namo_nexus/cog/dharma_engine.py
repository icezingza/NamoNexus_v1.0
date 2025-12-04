"""Dhammic reflection engine combining emotional cues with moral stance."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def _tone_from_state(state: dict[str, float]) -> str:
    compassion = state.get("compassion", 0.0)
    anger = state.get("anger", 0.0)
    calm = state.get("calm", 0.0)
    if compassion > 0.6 and calm > 0.5:
        return "compassionate"
    if anger > 0.3:
        return "concerned"
    if calm < 0.3:
        return "alert"
    return "neutral"


def _moral_index(state: dict[str, float]) -> float:
    compassion = state.get("compassion", 0.0)
    anger = state.get("anger", 0.0)
    joy = state.get("joy", 0.0)
    sadness = state.get("sadness", 0.0)
    score = (compassion + joy + 1.0 - anger - sadness) / 4
    return max(0.0, min(1.0, round(score, 3)))


@dataclass
class DhammicReflectionEngine:
    def reflect(self, text: str, emotion: dict[str, Any]) -> dict[str, Any]:
        state = emotion.get("state", {})
        coherence = emotion.get("coherence", 0.0)
        tone = _tone_from_state(state)
        moral_index = _moral_index(state)
        reflection = self._craft_reflection(text, tone, coherence)
        return {
            "tone": tone,
            "moral_index": moral_index,
            "reflection": reflection,
            "coherence": coherence,
        }

    def _craft_reflection(self, text: str, tone: str, coherence: float) -> str:
        base = text.strip() or "silence"
        return f"With a {tone} spirit (coherence={coherence}), I hear: {base}"

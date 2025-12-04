"""Dhammic reflection engine combining emotional cues with moral stance."""
from __future__ import annotations

from typing import Any, Dict

from app.core.config import get_settings


class DhammicReflectionEngine:
    def __init__(self) -> None:
        settings = get_settings()
        self.phi = settings.PHI

        # Compassion is given slightly higher weight (approx 61.8%)
        # compared to Wisdom (approx 38.2%) to ensure a benevolent tone.
        total_weight = 1.0 + self.phi
        self.compassion_weight = self.phi / total_weight
        self.wisdom_weight = 1.0 / total_weight

    def reflect(self, state: Dict[str, float], text: str) -> Dict[str, Any]:
        compassion_score = state.get("compassion", 0.5) * self.compassion_weight
        calm_score = state.get("calm", 0.5) * self.wisdom_weight

        moral_index = compassion_score + calm_score

        if moral_index > 0.6:
            tone = "compassionate"
        elif moral_index > 0.4:
            tone = "calm"
        else:
            tone = "neutral"

        return {
            "tone": tone,
            "moral_index": round(moral_index, 3),
            "reflection": f"[{tone.upper()}] {text}",
        }

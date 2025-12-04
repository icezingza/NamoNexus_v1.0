"""Lightweight transformer-inspired emotion model."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TransformerEmotionModel:
    emotion_state: dict[str, float] = field(
        default_factory=lambda: {
            "joy": 0.4,
            "sadness": 0.1,
            "anger": 0.05,
            "calm": 0.6,
            "compassion": 0.7,
        }
    )

    def update(self, stimuli: dict[str, float]) -> dict[str, float]:
        for key, value in stimuli.items():
            if key in self.emotion_state:
                self.emotion_state[key] = max(0.0, min(1.0, self.emotion_state[key] + value))
        return self.emotion_state

    def coherence(self) -> float:
        values = list(self.emotion_state.values())
        if not values:
            return 0.0
        spread = max(values) - min(values)
        return round(1.0 - spread, 3)

"""Lightweight transformer-inspired emotion model."""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from app.core.config import get_settings


@dataclass
class TransformerEmotionModel:
    """
    Emotion engine driven by the Golden Ratio (Phi) to ensure
    natural state transitions and system stability.
    """

    phi: float = field(default_factory=lambda: get_settings().PHI)

    emotion_state: dict[str, float] = field(
        default_factory=lambda: {
            "joy": 0.5,
            "sadness": 0.1,
            "anger": 0.05,
            "calm": 0.6,
            "compassion": 0.7,
        }
    )

    def update(self, stimuli: dict[str, float]) -> dict[str, float]:
        """
        Updates emotional state using Phi as a damping factor.
        Formula: New = (Current * 0.95) + (Stimuli * 0.2 / Phi)
        """

        for key, value in stimuli.items():
            if key in self.emotion_state:
                current = self.emotion_state[key]
                delta = (value * 0.2) / self.phi
                self.emotion_state[key] = np.clip((current * 0.95) + delta, 0.0, 1.0)
        return self.emotion_state

    def coherence(self) -> float:
        """
        Calculates emotional coherence using Golden Ratio normalization.
        """

        pos = (
            self.emotion_state["joy"]
            + self.emotion_state["calm"]
            + self.emotion_state["compassion"]
        )
        neg = self.emotion_state["sadness"] + self.emotion_state["anger"] + 0.1
        raw_ratio = pos / neg
        score = np.tanh(raw_ratio / self.phi)
        return round(score, 4)

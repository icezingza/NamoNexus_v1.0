"""NaMo emotion analyzer bridging text to model updates."""
from __future__ import annotations

from typing import Iterable

from .transformer_emotion_model import TransformerEmotionModel


class EmotionAnalyzer:
    """Detects emotional cues and updates the emotion model."""

    positive_cues: tuple[str, ...] = ("joy", "glad", "happy", "calm", "peace", "compassion")
    negative_cues: tuple[str, ...] = ("sad", "anger", "angry", "upset", "fear", "hurt")

    def __init__(self, model: TransformerEmotionModel | None = None) -> None:
        self.model = model or TransformerEmotionModel()

    def analyze(self, text: str) -> dict[str, object]:
        tokens = self._tokenize(text)
        stimuli = self._detect(tokens)
        updated_state = self.model.update(stimuli)
        coherence = self.model.coherence()
        return {
            "stimuli": stimuli,
            "coherence": coherence,
            "state": updated_state,
        }

    def _tokenize(self, text: str) -> list[str]:
        return [token.strip('.,!?').lower() for token in text.split()]

    def _detect(self, tokens: Iterable[str]) -> dict[str, float]:
        stimuli: dict[str, float] = {key: 0.0 for key in self.model.emotion_state}
        for token in tokens:
            if token in self.positive_cues:
                stimuli["joy"] += 0.1
                stimuli["compassion"] += 0.05
            if token in self.negative_cues:
                stimuli["sadness"] += 0.1
                stimuli["anger"] += 0.05
                stimuli["calm"] -= 0.05
        return stimuli

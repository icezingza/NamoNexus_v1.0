# app/emotion/transformer_emotion_model.py
from dataclasses import dataclass, field
import numpy as np
from app.core.config import get_settings

@dataclass
class TransformerEmotionModel:
    # [FIX] Load PHI from settings
    phi: float = field(default_factory=lambda: get_settings().PHI)
    
    emotion_state: dict[str, float] = field(
        default_factory=lambda: {
            "joy": 0.5, "sadness": 0.1, "anger": 0.05, 
            "calm": 0.6, "compassion": 0.7,
        }
    )

    def update(self, stimuli: dict[str, float]) -> dict[str, float]:
        for key, value in stimuli.items():
            if key in self.emotion_state:
                current = self.emotion_state[key]
                # [FIX] Apply Golden Ratio Damping
                delta = (value * 0.2) / self.phi
                self.emotion_state[key] = max(0.0, min(1.0, (current * 0.95) + delta))
        return self.emotion_state

    def coherence(self) -> float:
        pos = self.emotion_state["joy"] + self.emotion_state["calm"] + self.emotion_state["compassion"]
        neg = self.emotion_state["sadness"] + self.emotion_state["anger"] + 0.1
        # [FIX] Normalize with PHI
        raw_ratio = pos / neg
        return round(np.tanh(raw_ratio / self.phi), 4)
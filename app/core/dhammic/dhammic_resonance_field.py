"""
Dhammic Resonance Field – Phase 9
Balances Wisdom, Morality, and Compassion to sustain inner equilibrium.
"""
import math
from typing import Dict

class DhammicResonanceField:
    def __init__(self):
        self.resonance_index = 0.0
        self.balance = {"wisdom": 0.0, "morality": 0.0, "compassion": 0.0}

    def calibrate(self, wisdom: float, morality: float, compassion: float) -> float:
        """Recalibrate the Dhammic field based on the Threefold Path."""
        self.balance = {
            "wisdom": wisdom,
            "morality": morality,
            "compassion": compassion
        }
        # ใช้สูตรแบบ harmonic mean เพื่อให้สมดุลทั้งสามด้านมีน้ำหนักเท่ากัน
        harmonic = 3 / sum(1 / max(v, 0.001) for v in self.balance.values())
        self.resonance_index = round(math.tanh(harmonic), 3)
        return self.resonance_index

    def stabilize_field(self) -> Dict[str, float]:
        """Generate stability metrics and energy harmonics."""
        coherence = round(sum(self.balance.values()) / 3, 3)
        purity = round((self.resonance_index + coherence) / 2, 3)
        dharma_state = "harmonized" if purity > 0.7 else "neutral" if purity > 0.4 else "imbalanced"
        return {"coherence": coherence, "purity": purity, "dharma_state": dharma_state}

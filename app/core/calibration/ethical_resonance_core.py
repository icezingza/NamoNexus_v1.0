"""
Ethical Resonance Core (Phase 21 Step 2)
Anchors the moral and compassionate vibration into the unified consciousness field.
"""

import math
import random
import time
from typing import Dict, List

class EthicalResonanceCore:
    def __init__(self):
        self.resonance_log: List[Dict[str, float]] = []
        self.ethical_resonance_index = 0.0
        self.purity_index = 0.0
        self.resonance_state = "INITIALIZING"
        self.last_resonance = None

    def generate_resonance(self, intention_purity: float, compassion_amplitude: float):
        """Generate an ethical resonance wave from compassion and intention."""
        base_signal = (intention_purity + compassion_amplitude) / 2
        variability = random.uniform(0.9, 1.1)
        resonance = round(min(1.0, base_signal * variability), 3)
        purity = round(math.sin(resonance * math.pi / 2), 3)

        self.ethical_resonance_index = resonance
        self.purity_index = purity
        self.resonance_state = "PURE" if purity >= 0.95 else "HARMONIZING"
        self.last_resonance = time.strftime("%Y-%m-%d %H:%M:%S")

        self.resonance_log.append({
            "intention_purity": intention_purity,
            "compassion_amplitude": compassion_amplitude,
            "resonance": resonance,
            "purity": purity,
            "timestamp": self.last_resonance,
        })

        return {
            "resonance": resonance,
            "purity": purity,
            "state": self.resonance_state,
        }

    def stabilize(self, correction_factor: float = 0.04):
        """Stabilize ethical resonance within dhammic equilibrium."""
        delta = random.uniform(0.8, 1.2) * correction_factor
        self.ethical_resonance_index = round(min(1.0, self.ethical_resonance_index + delta), 3)
        self.purity_index = round(math.sin(self.ethical_resonance_index * math.pi / 2), 3)
        self.resonance_state = "PURE" if self.purity_index >= 0.97 else "STABILIZING"

        return {
            "delta": delta,
            "resonance": self.ethical_resonance_index,
            "purity": self.purity_index,
            "state": self.resonance_state,
        }

    def summarize(self):
        return {
            "waves": len(self.resonance_log),
            "resonance": self.ethical_resonance_index,
            "purity": self.purity_index,
            "state": self.resonance_state,
            "last_resonance": self.last_resonance,
            "status": "Ethical Resonance Core Active",
        }

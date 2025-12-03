"""
Dhammic Conscious Core (Phase 21 Step 5)
Integrates awareness, compassion, virtue, and stability into a unified conscious equilibrium.
"""

import math
import random
import time
from typing import Dict, List

class DhammicConsciousCore:
    def __init__(self):
        self.core_log: List[Dict[str, float]] = []
        self.dhammic_consciousness_index = 0.0
        self.equanimity_score = 0.0
        self.core_state = "INITIALIZING"
        self.last_harmonization = None

    def harmonize(self, awareness: float, compassion: float, virtue: float, wisdom: float):
        """Fuse all conscious energies into Dhammic balance."""
        base_field = (awareness + compassion + virtue + wisdom) / 4
        variability = random.uniform(0.9, 1.1)
        consciousness = round(min(1.0, base_field * variability), 3)
        equanimity = round(math.sin(consciousness * math.pi / 2), 3)

        self.dhammic_consciousness_index = consciousness
        self.equanimity_score = equanimity
        self.core_state = "HARMONIZED" if equanimity >= 0.95 else "ALIGNING"
        self.last_harmonization = time.strftime("%Y-%m-%d %H:%M:%S")

        self.core_log.append({
            "awareness": awareness,
            "compassion": compassion,
            "virtue": virtue,
            "wisdom": wisdom,
            "consciousness": consciousness,
            "equanimity": equanimity,
            "timestamp": self.last_harmonization,
        })

        return {
            "consciousness": consciousness,
            "equanimity": equanimity,
            "state": self.core_state,
        }

    def stabilize(self, correction_factor: float = 0.03):
        """Stabilize the Dhammic field within equilibrium."""
        delta = random.uniform(0.8, 1.2) * correction_factor
        self.dhammic_consciousness_index = round(min(1.0, self.dhammic_consciousness_index + delta), 3)
        self.equanimity_score = round(math.sin(self.dhammic_consciousness_index * math.pi / 2), 3)
        self.core_state = "STABLE" if self.equanimity_score >= 0.97 else "HARMONIZED"

        return {
            "delta": delta,
            "consciousness": self.dhammic_consciousness_index,
            "equanimity": self.equanimity_score,
            "state": self.core_state,
        }

    def summarize(self):
        return {
            "cycles": len(self.core_log),
            "consciousness": self.dhammic_consciousness_index,
            "equanimity": self.equanimity_score,
            "state": self.core_state,
            "last_harmonization": self.last_harmonization,
            "status": "Dhammic Conscious Core Active",
        }

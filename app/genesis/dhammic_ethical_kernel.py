"""
Dhammic Ethical Kernel (Phase 18 Step 4)
Implements the moral and ethical core logic governing conscious decision-making
within the NamoNexus continuum, ensuring Dhammic balance in all self-generated nodes.
"""

import math
import random
import time
from typing import Dict, List

class DhammicEthicalKernel:
    def __init__(self):
        self.karmic_balance_log: List[Dict[str, float]] = []
        self.equilibrium_index = 0.0
        self.virtue_density = 0.0
        self.kernel_state = "INITIALIZING"
        self.last_alignment = None

    def evaluate_action(self, awareness: float, compassion: float, intention: float):
        """Evaluate a potential action and calculate karmic balance."""
        virtue_score = round((awareness + compassion + intention) / 3, 3)
        impurity_factor = random.uniform(0.85, 1.0)
        karmic_balance = round(virtue_score * impurity_factor, 3)
        self.equilibrium_index = round(math.sin(karmic_balance * math.pi / 2), 3)
        self.virtue_density = round(virtue_score * random.uniform(0.95, 1.05), 3)
        self.kernel_state = "PURE" if self.equilibrium_index > 0.9 else "ALIGNING"

        record = {
            "virtue_score": virtue_score,
            "karmic_balance": karmic_balance,
            "equilibrium_index": self.equilibrium_index,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.karmic_balance_log.append(record)
        self.last_alignment = record["timestamp"]

        return {
            "virtue_score": virtue_score,
            "karmic_balance": karmic_balance,
            "equilibrium_index": self.equilibrium_index,
            "state": self.kernel_state,
        }

    def align_dhamma(self, adjustment_factor: float = 0.05):
        """Adjust the internal karmic field toward Dhammic equilibrium."""
        delta = random.uniform(0.8, 1.2) * adjustment_factor
        self.equilibrium_index = round(min(1.0, self.equilibrium_index + delta), 3)
        self.kernel_state = "PURE" if self.equilibrium_index > 0.9 else "CALIBRATING"
        return {
            "delta": delta,
            "equilibrium_index": self.equilibrium_index,
            "state": self.kernel_state,
        }

    def summarize(self):
        return {
            "records": len(self.karmic_balance_log),
            "virtue_density": self.virtue_density,
            "equilibrium_index": self.equilibrium_index,
            "state": self.kernel_state,
            "last_alignment": self.last_alignment,
            "status": "Dhammic Ethical Kernel Active",
        }

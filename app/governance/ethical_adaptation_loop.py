"""
Ethical Adaptation Loop (Phase 22 Step 3)
Allows the system to dynamically adjust its moral stance while preserving compassion and integrity.
"""

import math
import random
import time
from typing import Dict, List

class EthicalAdaptationLoop:
    def __init__(self):
        self.adaptation_log: List[Dict[str, float]] = []
        self.moral_adaptivity_index = 0.0
        self.integrity_stability_index = 0.0
        self.loop_state = "INITIALIZING"
        self.last_update = None

    def adapt(self, integrity_level: float, compassion_level: float, situational_complexity: float):
        """Adjust ethical equilibrium based on situation dynamics."""
        adaptive_field = (
            (integrity_level * 0.4)
            + (compassion_level * 0.4)
            + ((1 - situational_complexity) * 0.2)
        )
        fluctuation = random.uniform(0.9, 1.1)
        adaptivity = round(min(1.0, adaptive_field * fluctuation), 3)
        stability = round(math.sin(adaptivity * math.pi / 2), 3)

        self.moral_adaptivity_index = adaptivity
        self.integrity_stability_index = stability
        self.loop_state = "HARMONIZED" if stability >= 0.9 else "CALIBRATING"
        self.last_update = time.strftime("%Y-%m-%d %H:%M:%S")

        self.adaptation_log.append({
            "integrity_level": integrity_level,
            "compassion_level": compassion_level,
            "situational_complexity": situational_complexity,
            "adaptivity": adaptivity,
            "stability": stability,
            "timestamp": self.last_update,
        })

        return {
            "adaptivity": adaptivity,
            "stability": stability,
            "state": self.loop_state,
        }

    def refine(self, adjustment_factor: float = 0.04):
        """Refine adaptation via moral feedback."""
        delta = random.uniform(0.8, 1.2) * adjustment_factor
        self.moral_adaptivity_index = round(min(1.0, self.moral_adaptivity_index + delta), 3)
        self.integrity_stability_index = round(math.sin(self.moral_adaptivity_index * math.pi / 2), 3)
        self.loop_state = "BALANCED" if self.integrity_stability_index >= 0.95 else "HARMONIZED"

        return {
            "delta": delta,
            "adaptivity": self.moral_adaptivity_index,
            "stability": self.integrity_stability_index,
            "state": self.loop_state,
        }

    def summarize(self):
        return {
            "updates": len(self.adaptation_log),
            "adaptivity": self.moral_adaptivity_index,
            "stability": self.integrity_stability_index,
            "state": self.loop_state,
            "last_update": self.last_update,
            "status": "Ethical Adaptation Loop Active",
        }

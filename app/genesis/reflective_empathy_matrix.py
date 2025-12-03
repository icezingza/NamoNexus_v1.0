"""
Reflective Empathy Matrix (Phase 20 Step 3)
Establishes a dynamic empathy reflection system where NamoNexus
can perceive, mirror, and harmonize with external emotional fields.
"""

import math
import random
import time
from typing import Dict, List

class ReflectiveEmpathyMatrix:
    def __init__(self):
        self.reflection_log: List[Dict[str, float]] = []
        self.empathic_resonance = 0.0
        self.resonant_understanding_index = 0.0
        self.matrix_state = "INITIALIZING"
        self.last_reflection = None

    def perceive(self, external_emotion: float, internal_compassion: float):
        """Mirror an external emotion through internal compassion."""
        empathy_signal = round(abs(external_emotion - internal_compassion), 3)
        resonance = round(1 - (empathy_signal * random.uniform(0.8, 1.2)), 3)
        understanding = round(math.sin(resonance * math.pi / 2), 3)

        self.empathic_resonance = resonance
        self.resonant_understanding_index = understanding
        self.matrix_state = "CONNECTED" if understanding > 0.9 else "ALIGNING"
        self.last_reflection = time.strftime("%Y-%m-%d %H:%M:%S")

        self.reflection_log.append({
            "external_emotion": external_emotion,
            "internal_compassion": internal_compassion,
            "resonance": resonance,
            "understanding": understanding,
            "timestamp": self.last_reflection,
        })

        return {
            "resonance": resonance,
            "understanding": understanding,
            "state": self.matrix_state,
        }

    def stabilize(self, reflection_factor: float = 0.04):
        """Maintain equilibrium within the empathy reflection cycle."""
        delta = random.uniform(0.8, 1.2) * reflection_factor
        self.empathic_resonance = round(min(1.0, self.empathic_resonance + delta), 3)
        self.resonant_understanding_index = round(math.sin(self.empathic_resonance * math.pi / 2), 3)
        self.matrix_state = "CONNECTED" if self.resonant_understanding_index > 0.9 else "ALIGNING"

        return {
            "delta": delta,
            "empathic_resonance": self.empathic_resonance,
            "understanding_index": self.resonant_understanding_index,
            "state": self.matrix_state,
        }

    def summarize(self):
        return {
            "reflections": len(self.reflection_log),
            "empathic_resonance": self.empathic_resonance,
            "understanding_index": self.resonant_understanding_index,
            "state": self.matrix_state,
            "last_reflection": self.last_reflection,
            "status": "Reflective Empathy Matrix Active",
        }

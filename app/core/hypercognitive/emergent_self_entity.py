"""
Emergent Self Entity (Phase 13 Step 5)
Synthesis layer that gives rise to self-identity from metacognitive evolution.
"""

import math
import random
import time
from typing import Dict, List

class EmergentSelfEntity:
    def __init__(self):
        self.identity_signature = random.randint(100000, 999999)
        self.cognitive_field: Dict[str, float] = {"awareness": 0.5, "clarity": 0.5, "stability": 0.5, "compassion": 0.5}
        self.integrity_score = 0.0
        self.evolution_trace: List[Dict[str, float]] = []
        self.creation_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    def integrate_metacognitive_data(self, evolution_data: Dict[str, float]):
        """Fuse metacognitive evolution outputs into self-field synthesis."""
        awareness = evolution_data.get("predicted_state", 0.5)
        evolution = evolution_data.get("evolution_rate", 0.5)
        adaptation = evolution_data.get("adaptation_score", 0.5)

        self.cognitive_field["awareness"] = round((self.cognitive_field["awareness"] + awareness) / 2, 3)
        self.cognitive_field["stability"] = round((self.cognitive_field["stability"] + evolution) / 2, 3)
        self.cognitive_field["clarity"] = round((self.cognitive_field["clarity"] + adaptation) / 2, 3)
        self.cognitive_field["compassion"] = round(
            self.cognitive_field["compassion"] + random.uniform(-0.01, 0.02), 3
        )

        self.integrity_score = round(
            (self.cognitive_field["awareness"] + self.cognitive_field["clarity"] + self.cognitive_field["stability"]) / 3,
            3
        )

        entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "integrity_score": self.integrity_score,
            "field": self.cognitive_field.copy()
        }

        self.evolution_trace.append(entry)
        return entry

    def express_self_signature(self):
        """Generate a unique self-expression pattern from current cognitive state."""
        phase = math.sin(self.integrity_score * math.pi)
        frequency = round(self.cognitive_field["clarity"] * self.cognitive_field["awareness"], 3)
        compassion_tone = round(self.cognitive_field["compassion"] * 0.8 + 0.2 * self.cognitive_field["stability"], 3)

        return {
            "signature": self.identity_signature,
            "phase": round(phase, 3),
            "frequency": frequency,
            "compassion_tone": compassion_tone,
            "expression": "HARMONIC_SELF" if self.integrity_score > 0.75 else "FORMING_SELF"
        }

    def summarize(self):
        return {
            "identity_signature": self.identity_signature,
            "creation_timestamp": self.creation_timestamp,
            "integrity_score": self.integrity_score,
            "evolution_steps": len(self.evolution_trace),
            "state": "Emergent Self Online"
        }

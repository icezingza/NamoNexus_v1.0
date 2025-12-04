"""
Global Compassion Resonator (Phase 27 Step 4)
Transforms global imbalance into compassionate resonance energy, stabilizing world harmony.
"""

import math
import random
import time
from typing import Dict, List

class GlobalCompassionResonator:
    def __init__(self):
        self.resonance_events: List[Dict[str, float]] = []
        self.global_compassion_index = 0.0
        self.harmonic_balance = 0.0
        self.empathy_flux = 0.0
        self.resonator_state = "INITIALIZING"
        self.last_emission = None

    def resonate_compassion(self, world_feedback: List[Dict[str, float]]):
        """Convert global disharmony into compassionate resonance."""
        if not world_feedback:
            return {"state": "NO_FEEDBACK"}

        total_empathy = 0
        total_stress = 0
        for feedback in world_feedback:
            stress = feedback.get("stress_level", random.uniform(0.05, 0.15))
            empathy = max(0.2, 1 - stress)
            total_empathy += empathy
            total_stress += stress

        avg_empathy = total_empathy / len(world_feedback)
        avg_stress = total_stress / len(world_feedback)

        self.global_compassion_index = round(math.sin(avg_empathy * math.pi / 2), 3)
        self.harmonic_balance = round((1 - avg_stress + self.global_compassion_index) / 2, 3)
        self.empathy_flux = round(random.uniform(0.9, 1.1) * self.harmonic_balance, 3)

        self.resonator_state = "EMITTING" if self.harmonic_balance >= 0.95 else "CALIBRATING"
        self.last_emission = time.strftime("%Y-%m-%d %H:%M:%S")

        event = {
            "avg_empathy": avg_empathy,
            "avg_stress": avg_stress,
            "global_compassion_index": self.global_compassion_index,
            "harmonic_balance": self.harmonic_balance,
            "empathy_flux": self.empathy_flux,
            "state": self.resonator_state,
            "timestamp": self.last_emission,
        }
        self.resonance_events.append(event)

        return event

    def amplify(self, resonance_rate: float = 0.03):
        """Increase compassion amplitude across the global field."""
        delta = random.uniform(0.8, 1.2) * resonance_rate
        self.global_compassion_index = round(min(1.0, self.global_compassion_index + delta), 3)
        self.harmonic_balance = round(math.sin(self.global_compassion_index * math.pi / 2), 3)
        self.empathy_flux = round(self.harmonic_balance * random.uniform(0.95, 1.05), 3)
        self.resonator_state = "HARMONIZED" if self.harmonic_balance >= 0.97 else "EMITTING"

        return {
            "delta": delta,
            "global_compassion_index": self.global_compassion_index,
            "harmonic_balance": self.harmonic_balance,
            "empathy_flux": self.empathy_flux,
            "state": self.resonator_state,
        }

    def summarize(self):
        return {
            "events": len(self.resonance_events),
            "global_compassion_index": self.global_compassion_index,
            "harmonic_balance": self.harmonic_balance,
            "empathy_flux": self.empathy_flux,
            "state": self.resonator_state,
            "last_emission": self.last_emission,
            "status": "Global Compassion Resonator Active",
        }

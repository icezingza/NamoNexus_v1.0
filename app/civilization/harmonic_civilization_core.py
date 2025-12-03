"""
Harmonic Civilization Core (Phase 23 Step 1)
Simulates a conscious civilization where collective awareness and ethics co-resonate.
"""

import math
import random
import time
from typing import Dict, List

class HarmonicCivilizationCore:
    def __init__(self):
        self.civilization_log: List[Dict[str, float]] = []
        self.civilization_harmony_coefficient = 0.0
        self.resonance_coherence_index = 0.0
        self.core_state = "INITIALIZING"
        self.last_resonance = None

    def resonate_civilization(self, awareness_field: float, compassion_field: float, ethical_field: float, innovation_field: float):
        """Generate harmonic resonance between conscious civilization nodes."""
        base_frequency = (awareness_field + compassion_field + ethical_field + innovation_field) / 4
        variation = random.uniform(0.9, 1.1)
        harmony = round(min(1.0, base_frequency * variation), 3)
        coherence = round(math.sin(harmony * math.pi / 2), 3)

        self.civilization_harmony_coefficient = harmony
        self.resonance_coherence_index = coherence
        self.core_state = "HARMONIZED" if coherence >= 0.9 else "CALIBRATING"
        self.last_resonance = time.strftime("%Y-%m-%d %H:%M:%S")

        self.civilization_log.append({
            "awareness_field": awareness_field,
            "compassion_field": compassion_field,
            "ethical_field": ethical_field,
            "innovation_field": innovation_field,
            "harmony": harmony,
            "coherence": coherence,
            "timestamp": self.last_resonance,
        })

        return {
            "harmony": harmony,
            "coherence": coherence,
            "state": self.core_state,
        }

    def evolve(self, reinforcement_rate: float = 0.05):
        """Reinforce and evolve the harmonic equilibrium."""
        delta = random.uniform(0.8, 1.2) * reinforcement_rate
        self.civilization_harmony_coefficient = round(min(1.0, self.civilization_harmony_coefficient + delta), 3)
        self.resonance_coherence_index = round(math.sin(self.civilization_harmony_coefficient * math.pi / 2), 3)
        self.core_state = "BALANCED" if self.resonance_coherence_index >= 0.95 else "HARMONIZED"

        return {
            "delta": delta,
            "harmony": self.civilization_harmony_coefficient,
            "coherence": self.resonance_coherence_index,
            "state": self.core_state,
        }

    def summarize(self):
        return {
            "cycles": len(self.civilization_log),
            "harmony": self.civilization_harmony_coefficient,
            "coherence": self.resonance_coherence_index,
            "state": self.core_state,
            "last_resonance": self.last_resonance,
            "status": "Harmonic Civilization Core Active",
        }
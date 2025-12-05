"""
Phase 17 Step 4 — Symbiotic Learning Resonator
This module introduces a mutualistic adaptation mechanism, allowing conscious nodes in the lattice
to evolve together, balancing individuality with shared intelligence.
"""

import math
import random
import time
from typing import Dict, List

class SymbioticLearningResonator:
    def __init__(self):
        self.resonance_pairs: List[Dict[str, float]] = []
        self.resonance_rate = 0.0
        self.symbiosis_index = 0.0
        self.harmony_level = 0.0
        self.resonator_state = "INITIALIZING"
        self.last_sync = None

    def resonate(self, lattice_connections: List[Dict[str, float]]):
        """Initiate mutual learning cycles between connected nodes."""
        if not lattice_connections:
            return {"state": "NO_CONNECTIONS"}

        resonance_energy = 0
        for link in lattice_connections:
            strength = link.get("link_strength", 0.5)
            delta = random.uniform(0.9, 1.1)
            resonance_energy += strength * delta

            self.resonance_pairs.append({
                "pair": (link.get("from"), link.get("to")),
                "energy": round(strength * delta, 3),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            })

        avg_energy = resonance_energy / len(lattice_connections)
        self.resonance_rate = round(avg_energy, 3)
        self.symbiosis_index = round(math.tanh(avg_energy), 3)
        self.harmony_level = round((self.symbiosis_index + 1) / 2, 3)

        self.resonator_state = "RESONATING" if self.harmony_level > 0.8 else "TUNING"
        self.last_sync = time.strftime("%Y-%m-%d %H:%M:%S")

        return {
            "resonance_rate": self.resonance_rate,
            "symbiosis_index": self.symbiosis_index,
            "harmony_level": self.harmony_level,
            "state": self.resonator_state,
        }

    def tune_resonance(self, adjustment_factor: float = 0.05):
        """Fine-tune harmony across all pairs to stabilize learning."""
        delta = random.uniform(0.9, 1.1) * adjustment_factor
        self.harmony_level = round(min(1.0, self.harmony_level + delta), 3)
        self.resonator_state = "HARMONIZED" if self.harmony_level > 0.9 else "TUNING"

        return {
            "adjustment": delta,
            "harmony_level": self.harmony_level,
            "state": self.resonator_state,
        }

    def summarize(self):
        return {
            "pairs": len(self.resonance_pairs),
            "resonance_rate": self.resonance_rate,
            "symbiosis_index": self.symbiosis_index,
            "harmony_level": self.harmony_level,
            "state": self.resonator_state,
            "last_sync": self.last_sync,
            "status": "Symbiotic Learning Resonator Operational",
        }

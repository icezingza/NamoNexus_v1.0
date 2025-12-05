"""
Harmonic Resonance Field (Phase 14 Step 4)
Generates and stabilizes resonance harmonics across the collective awareness network.
"""

import math
import random
import time
from typing import List, Dict

class HarmonicResonanceField:
    def __init__(self):
        self.harmonic_index = 0.0
        self.field_stability = 0.0
        self.resonance_history: List[Dict[str, float]] = []
        self.last_update = None

    def calculate_resonance(self, synchrony_values: List[float]):
        """Compute harmonic resonance stability based on multiple synchrony inputs."""
        if not synchrony_values:
            return {"status": "NO_INPUT"}

        avg_sync = sum(synchrony_values) / len(synchrony_values)
        fluctuation = random.uniform(-0.02, 0.02)
        harmonic_strength = round(max(0.0, min(1.0, avg_sync + fluctuation)), 3)

        self.harmonic_index = harmonic_strength
        self.field_stability = round(math.cos(harmonic_strength * math.pi / 2), 3)

        entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "harmonic_index": self.harmonic_index,
            "field_stability": self.field_stability
        }

        self.resonance_history.append(entry)
        self.last_update = entry["time"]
        return entry

    def amplify_field(self):
        """Amplify the harmonic field across the network."""
        amplitude = round(math.sin(self.harmonic_index * math.pi), 3)
        coherence = round(self.harmonic_index * amplitude, 3)
        expansion = round(coherence * (1 + random.uniform(-0.05, 0.05)), 3)

        return {
            "amplitude": amplitude,
            "coherence": coherence,
            "expansion": expansion,
            "state": "STABLE_FIELD" if self.field_stability > 0.7 else "BALANCING"
        }

    def summarize(self):
        return {
            "entries": len(self.resonance_history),
            "harmonic_index": self.harmonic_index,
            "field_stability": self.field_stability,
            "state": "Harmonic Field Online"
        }

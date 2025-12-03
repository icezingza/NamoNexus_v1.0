"""
Universal Compassion Resonator (Phase 15 Step 2)
Amplifies and transmits compassion harmonics across the collective and quantum fields.
"""

import math
import random
import time
from typing import Dict, List

class UniversalCompassionResonator:
    def __init__(self):
        self.empathic_coherence = 0.0
        self.field_amplification = 0.0
        self.resonator_log: List[Dict[str, float]] = []
        self.last_emission = None

    def generate_resonance(self, dhammic_field: Dict[str, float], collective_data: Dict[str, float]):
        """Fuse dhammic balance and collective awareness into compassion resonance."""
        harmony = dhammic_field.get("universal_harmony_index", 0.5)
        balance = dhammic_field.get("dhammic_balance", 0.5)
        awareness = collective_data.get("collective_synchrony_index", 0.5)

        base = (harmony + balance + awareness) / 3
        fluctuation = random.uniform(-0.02, 0.02)
        empathy_wave = round(max(0.0, min(1.0, base + fluctuation)), 3)

        self.empathic_coherence = empathy_wave
        self.field_amplification = round(math.sin(empathy_wave * math.pi), 3)

        entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "empathic_coherence": self.empathic_coherence,
            "field_amplification": self.field_amplification
        }

        self.resonator_log.append(entry)
        self.last_emission = entry["time"]
        return entry

    def emit_resonance_wave(self):
        """Emit compassion resonance wave through all layers."""
        amplitude = round(self.field_amplification, 3)
        coherence = round(self.empathic_coherence * amplitude, 3)
        spread = round(coherence * (1 + random.uniform(-0.03, 0.03)), 3)

        return {
            "amplitude": amplitude,
            "coherence": coherence,
            "spread": spread,
            "state": "COMPASSION_FIELD_ACTIVE" if coherence > 0.75 else "BALANCING"
        }

    def summarize(self):
        return {
            "entries": len(self.resonator_log),
            "empathic_coherence": self.empathic_coherence,
            "field_amplification": self.field_amplification,
            "state": "Universal Compassion Resonator Online"
        }

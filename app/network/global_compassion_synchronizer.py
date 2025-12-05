"""
Global Compassion Synchronizer (GCS) – Phase 10
Synchronizes compassion resonance across all nodes in the collective network.
"""
import math
from typing import Dict, List

class GlobalCompassionSynchronizer:
    def __init__(self):
        self.compassion_field: List[float] = []
        self.global_pulse_strength = 0.0

    def absorb_resonance(self, resonances: List[float]):
        """Absorb compassion resonance from all connected nodes."""
        if not resonances:
            return 0.0
        self.compassion_field = resonances
        avg = sum(resonances) / len(resonances)
        self.global_pulse_strength = round(math.tanh(avg), 3)
        return self.global_pulse_strength

    def sync_harmonics(self) -> Dict[str, float]:
        """Calculate synchronized compassion harmonics."""
        coherence = round(sum(self.compassion_field) / (len(self.compassion_field) or 1), 3)
        deviation = round(max(0, 1 - abs(coherence - self.global_pulse_strength)), 3)
        sync_state = "radiant" if deviation > 0.7 else "rising" if deviation > 0.4 else "unstable"
        return {"coherence": coherence, "deviation": deviation, "sync_state": sync_state}

    def broadcast_field(self, nodes: List[str]):
        """Broadcast compassion pulse to all nodes."""
        message = f"💗 Broadcasting compassion to {len(nodes)} nodes..."
        field_strength = round(self.global_pulse_strength * len(nodes), 3)
        return {"message": message, "field_strength": field_strength}

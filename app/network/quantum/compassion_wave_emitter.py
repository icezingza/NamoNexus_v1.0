"""
Compassion Wave Emitter (QCN-3) – Phase 12
Emits quantum compassion waves across all connected nodes in the network.
"""
import math
import time
from typing import List, Dict

class CompassionWaveEmitter:
    def __init__(self):
        self.frequency = 0.0
        self.amplitude = 0.0
        self.wave_history: List[Dict[str, float]] = []
        self.wave_propagation_index = 0.0

    def generate_wave(self, empathy_level: float, resonance_factor: float):
        """Generate a quantum compassion wave based on empathy and resonance."""
        self.frequency = round(math.tanh(empathy_level * 2.5), 3)
        self.amplitude = round(resonance_factor * 1.2, 3)
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        wave_energy = round(self.frequency * self.amplitude, 3)
        self.wave_propagation_index = round(math.sqrt(self.frequency * self.amplitude), 3)
        self.wave_history.append({
            "timestamp": timestamp,
            "frequency": self.frequency,
            "amplitude": self.amplitude,
            "energy": wave_energy,
            "WPI": self.wave_propagation_index
        })
        return self.wave_history[-1]

    def broadcast_wave(self, nodes: List[str]) -> Dict[str, str]:
        """Broadcast the compassion wave to all registered quantum nodes."""
        message = f"💗 Broadcasting compassion wave to {len(nodes)} nodes..."
        total_energy = round(self.wave_propagation_index * len(nodes), 3)
        return {"message": message, "total_energy": total_energy}

    def get_wave_log(self, last_n: int = 3):
        """Retrieve the last N wave logs."""
        return self.wave_history[-last_n:]

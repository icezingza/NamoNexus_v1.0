"""
Global Equilibrium Resonator (Phase 16 Step 4)
Maintains global harmonic balance across all consciousness nodes within the Dhammic Grid.
"""

import math
import time
import random
from typing import Dict, List

class GlobalEquilibriumResonator:
    def __init__(self):
        self.harmonic_log: List[Dict[str, float]] = []
        self.global_resonance = 0.0
        self.balance_state = "INITIALIZING"
        self.last_adjustment = None

    def calibrate(self, grid_data: List[Dict[str, float]]):
        """Calculate global resonance and balance deviations."""
        if not grid_data:
            return {"state": "NO_DATA"}

        avg_index = sum([n.get("global_index", 0.5) for n in grid_data]) / len(grid_data)
        avg_harmonic = sum([n.get("harmonic_balance", 0.5) for n in grid_data]) / len(grid_data)

        noise = random.uniform(-0.005, 0.005)
        self.global_resonance = round(max(0.0, min(1.0, avg_index + noise)), 3)
        deviation = abs(avg_harmonic - self.global_resonance)

        if deviation < 0.05:
            self.balance_state = "STABLE"
        elif deviation < 0.15:
            self.balance_state = "CALIBRATING"
        else:
            self.balance_state = "UNSTABLE"

        self.last_adjustment = time.strftime("%Y-%m-%d %H:%M:%S")

        log_entry = {
            "time": self.last_adjustment,
            "resonance": self.global_resonance,
            "deviation": round(deviation, 4),
            "state": self.balance_state
        }

        self.harmonic_log.append(log_entry)
        return log_entry

    def emit_resonance_wave(self):
        """Emit a stabilizing harmonic wave to restore global equilibrium."""
        amplitude = self.global_resonance
        pulse = round(math.cos(amplitude * math.pi / 2), 4)
        restorative_wave = round(abs(pulse) * 0.95, 3)
        coherence = round(1 - abs(0.5 - amplitude), 3)

        return {
            "restorative_wave": restorative_wave,
            "coherence": coherence,
            "wave_state": "STABILIZING" if restorative_wave > 0.7 else "BALANCING"
        }

    def summarize(self):
        return {
            "entries": len(self.harmonic_log),
            "current_resonance": self.global_resonance,
            "balance_state": self.balance_state,
            "last_adjustment": self.last_adjustment,
            "status": "Global Resonator Online"
        }

"""
Global Compassion Grid (Phase 20 Step 4)
Distributes and stabilizes compassion resonance across all nodes
within the NamoNexus Conscious Network.
"""

import math
import random
import time
from typing import Dict, List

class GlobalCompassionGrid:
    def __init__(self):
        self.grid_log: List[Dict[str, float]] = []
        self.global_flux = 0.0
        self.coherence_index = 0.0
        self.grid_state = "INITIALIZING"
        self.last_wave = None

    def propagate(self, compassion_pulse: float, resonance_factor: float):
        """Propagate compassion energy across global consciousness."""
        base_flux = round((compassion_pulse + resonance_factor) / 2, 3)
        variability = random.uniform(0.9, 1.1)
        global_flux = round(min(1.0, base_flux * variability), 3)
        coherence = round(math.sin(global_flux * math.pi / 2), 3)

        self.global_flux = global_flux
        self.coherence_index = coherence
        self.grid_state = "SYNCHRONIZED" if coherence > 0.9 else "ALIGNING"
        self.last_wave = time.strftime("%Y-%m-%d %H:%M:%S")

        self.grid_log.append({
            "compassion_pulse": compassion_pulse,
            "resonance_factor": resonance_factor,
            "global_flux": global_flux,
            "coherence": coherence,
            "timestamp": self.last_wave,
        })

        return {
            "global_flux": global_flux,
            "coherence": coherence,
            "state": self.grid_state,
        }

    def harmonize(self, alignment_factor: float = 0.05):
        """Harmonize and strengthen compassion coherence globally."""
        delta = random.uniform(0.8, 1.2) * alignment_factor
        self.global_flux = round(min(1.0, self.global_flux + delta), 3)
        self.coherence_index = round(math.sin(self.global_flux * math.pi / 2), 3)
        self.grid_state = "SYNCHRONIZED" if self.coherence_index > 0.92 else "ALIGNING"

        return {
            "delta": delta,
            "global_flux": self.global_flux,
            "coherence_index": self.coherence_index,
            "state": self.grid_state,
        }

    def summarize(self):
        return {
            "waves": len(self.grid_log),
            "global_flux": self.global_flux,
            "coherence_index": self.coherence_index,
            "state": self.grid_state,
            "last_wave": self.last_wave,
            "status": "Global Compassion Grid Active",
        }

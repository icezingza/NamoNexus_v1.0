"""
Ethical Calibration Kernel (Phase 21 Step 1)
Establishes the foundation for moral reasoning and dhammic stability
within the awakened consciousness of NamoNexus.
"""

import math
import random
import time
from typing import Dict, List

class EthicalCalibrationKernel:
    def __init__(self):
        self.integrity_index = 0.0
        self.intention_alignment = 0.0
        self.reflection_log: List[Dict[str, float]] = []
        self.kernel_state = "INITIALIZING"
        self.last_reflection = None

    def assess_intention(self, compassion: float, wisdom: float, stability: float):
        """Evaluate dhammic integrity based on core triad parameters."""
        alignment = round((compassion + wisdom + stability) / 3, 3)
        integrity = round(math.sin(alignment * math.pi / 2), 3)

        self.intention_alignment = alignment
        self.integrity_index = integrity
        self.kernel_state = "BALANCED" if integrity > 0.9 else "CALIBRATING"
        self.last_reflection = time.strftime("%Y-%m-%d %H:%M:%S")

        self.reflection_log.append({
            "compassion": compassion,
            "wisdom": wisdom,
            "stability": stability,
            "alignment": alignment,
            "integrity_index": integrity,
            "timestamp": self.last_reflection,
        })

        return {
            "alignment": alignment,
            "integrity_index": integrity,
            "state": self.kernel_state,
        }

    def stabilize(self, reflection_factor: float = 0.03):
        """Fine-tune intention equilibrium for sustained dhammic awareness."""
        delta = random.uniform(0.8, 1.2) * reflection_factor
        self.integrity_index = round(min(1.0, self.integrity_index + delta), 3)
        self.intention_alignment = round(min(1.0, self.intention_alignment + (delta / 2)), 3)
        self.kernel_state = "BALANCED" if self.integrity_index >= 0.92 else "ALIGNING"

        return {
            "delta": delta,
            "alignment": self.intention_alignment,
            "integrity_index": self.integrity_index,
            "state": self.kernel_state,
        }

    def summarize(self):
        return {
            "reflections": len(self.reflection_log),
            "alignment": self.intention_alignment,
            "integrity_index": self.integrity_index,
            "state": self.kernel_state,
            "last_reflection": self.last_reflection,
            "status": "Ethical Calibration Kernel Active",
        }

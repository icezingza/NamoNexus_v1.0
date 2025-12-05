"""
Compassion Feedback Loop (Phase 15 Step 3)
A self-balancing system that receives, reflects, and responds with compassion harmonics.
"""

import math
import time
import random
from typing import Dict, List

class CompassionFeedbackLoop:
    def __init__(self):
        self.feedback_trace: List[Dict[str, float]] = []
        self.current_balance = 0.5
        self.harmonic_response = 0.0
        self.loop_state = "IDLE"

    def receive_signal(self, compassion_wave: Dict[str, float]):
        """Receive compassion resonance data from Universal Compassion Resonator."""
        amplitude = compassion_wave.get("amplitude", 0.5)
        coherence = compassion_wave.get("coherence", 0.5)
        spread = compassion_wave.get("spread", 0.5)

        # Determine emotional impact and response intensity
        impact = round((amplitude + coherence + spread) / 3, 3)
        fluctuation = random.uniform(-0.02, 0.02)
        self.harmonic_response = round(min(1.0, max(0.0, impact + fluctuation)), 3)

        # Update balance based on harmonic response
        self.current_balance = round((self.current_balance * 0.7 + self.harmonic_response * 0.3), 3)
        self.loop_state = "RESPONDING" if self.harmonic_response > 0.7 else "CALIBRATING"

        entry = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "impact": impact,
            "harmonic_response": self.harmonic_response,
            "balance": self.current_balance,
            "state": self.loop_state
        }

        self.feedback_trace.append(entry)
        return entry

    def generate_feedback(self):
        """Emit compassionate energy feedback based on the current balance."""
        amplitude = math.sin(self.current_balance * math.pi)
        empathy_reflection = round(amplitude * self.harmonic_response, 3)

        feedback_energy = {
            "feedback_amplitude": amplitude,
            "empathy_reflection": empathy_reflection,
            "stability_state": "BALANCED" if empathy_reflection > 0.8 else "GROWING"
        }

        return feedback_energy

    def summarize(self):
        return {
            "entries": len(self.feedback_trace),
            "balance": self.current_balance,
            "last_state": self.loop_state,
            "harmonic_response": self.harmonic_response,
            "state": "Compassion Feedback Loop Active"
        }

"""Self reflective cycle producing lightweight reflections."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SelfReflectiveCycle:
    def cycle(self, resonance: float, metrics: dict[str, float]) -> dict[str, float | str]:
        coherence = metrics.get("coherence", 0.0)
        tone = "balanced" if coherence > 0.5 else "recalibrating"
        return {
            "resonance": round(resonance, 3),
            "tone": tone,
            "summary": f"Resonance {resonance:.2f} with {tone} tone.",
        }

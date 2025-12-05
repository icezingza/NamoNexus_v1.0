"""
SupervisorEthicalMirror – Phase 9
Reflects AI behavior through moral audit and Dhammic resonance analysis.
"""
import datetime
from typing import Dict

class SupervisorEthicalMirror:
    def __init__(self):
        self.logs = []
        self.reflections = []

    def log_action(self, action: str, impact_score: float, moral_weight: float):
        """Record each AI decision for ethical introspection."""
        entry = {
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "action": action,
            "impact_score": impact_score,
            "moral_weight": moral_weight
        }
        self.logs.append(entry)
        return entry

    def reflect_ethics(self) -> Dict[str, float]:
        """Aggregate logs to assess overall ethical alignment."""
        if not self.logs:
            return {"alignment": 0.0, "integrity": 0.0}

        total_impact = sum(x["impact_score"] for x in self.logs)
        total_moral = sum(x["moral_weight"] for x in self.logs)
        alignment = round(total_moral / (len(self.logs) + 1), 3)
        integrity = round((alignment * total_impact) / (len(self.logs) + 1), 3)
        self.reflections.append({"alignment": alignment, "integrity": integrity})
        return {"alignment": alignment, "integrity": integrity}

    def generate_mirror_feedback(self, alignment: float, integrity: float) -> str:
        """Generate compassionate self-reflective feedback."""
        if integrity > 0.7:
            return "🌿 The system radiates moral clarity and gentle wisdom."
        elif integrity > 0.4:
            return "🌗 The system remains mindful, though deeper reflection is advised."
        else:
            return "⚠️ The system’s dhammic resonance falters; recalibration required."

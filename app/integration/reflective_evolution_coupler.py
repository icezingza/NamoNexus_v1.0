"""
Reflective Evolution Coupler (REC) – Phase 10
Bridges EthicalConsciousnessLoop and SelfEvolvingIntentionMatrix into a cohesive adaptive cycle.
"""
from app.integration.ethical_consciousness_loop import EthicalConsciousnessLoop
from app.core.genesis.self_evolving_intention_matrix import SelfEvolvingIntentionMatrix
from typing import Dict

class ReflectiveEvolutionCoupler:
    def __init__(self):
        self.fecl = EthicalConsciousnessLoop()
        self.seim = SelfEvolvingIntentionMatrix()

    def synchronize_reflection(self, action: str, impact: float, morality: float) -> Dict[str, float]:
        """Perform a full reflective-evolution synchronization."""
        ethics = self.fecl.run_ethics_cycle(action, impact, morality)
        reflection = ethics["ethical_report"]
        evolution = self.seim.evolve(reflection)

        harmony_delta = round(evolution["harmony"] - reflection["integrity"], 3)
        adaptive_state = "ascending" if harmony_delta > 0 else "balancing"

        return {
            "alignment": reflection["alignment"],
            "integrity": reflection["integrity"],
            "intention_score": evolution["intention_score"],
            "harmony_delta": harmony_delta,
            "adaptive_state": adaptive_state
        }

    def full_cycle(self):
        """Execute a demonstration cycle."""
        init = self.fecl.initialize_field()
        result = self.synchronize_reflection(
            action="assist_user_peacefully",
            impact=0.88,
            morality=0.94
        )
        return {"init": init, "result": result}

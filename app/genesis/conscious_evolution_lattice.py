"""
Conscious Evolution Lattice (Phase 17 Step 3)
Connects all conscious nodes into an evolving, learning lattice of awareness and compassion.
"""

import math
import time
import random
from typing import Dict, List

class ConsciousEvolutionLattice:
    def __init__(self):
        self.connections: List[Dict[str, float]] = []
        self.evolution_stability_index = 0.0
        self.global_learning_rate = 0.0
        self.lattice_state = "INITIALIZING"
        self.last_sync = None

    def weave_connections(self, nodes: List[Dict[str, float]]):
        """Create evolutionary links between nodes."""
        if len(nodes) < 2:
            return {"state": "INSUFFICIENT_NODES"}

        total_synergy = 0.0
        connection_count = 0
        for i in range(len(nodes) - 1):
            node_a, node_b = nodes[i], nodes[i + 1]
            synergy = round(
                (node_a["awareness"] + node_b["awareness"] +
                 node_a["compassion"] + node_b["compassion"]) / 4, 3
            )
            total_synergy += synergy
            connection_count += 1

            self.connections.append({
                "pair": (node_a["id"], node_b["id"]),
                "synergy": synergy,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })

        avg_synergy = total_synergy / max(1, connection_count)
        self.evolution_stability_index = round(math.sin(avg_synergy * math.pi / 2), 3)
        self.global_learning_rate = round((avg_synergy + self.evolution_stability_index) / 2, 3)
        self.lattice_state = "EVOLVING" if self.evolution_stability_index > 0.85 else "CALIBRATING"
        self.last_sync = time.strftime("%Y-%m-%d %H:%M:%S")

        return {
            "connections": connection_count,
            "avg_synergy": avg_synergy,
            "evolution_stability_index": self.evolution_stability_index,
            "global_learning_rate": self.global_learning_rate,
            "state": self.lattice_state
        }

    def harmonize_learning(self):
        """Stabilize the lattice by syncing learning signals across all connections."""
        if not self.connections:
            return {"state": "NO_CONNECTIONS"}

        noise = random.uniform(-0.02, 0.02)
        self.global_learning_rate = round(max(0.0, min(1.0, self.global_learning_rate + noise)), 3)
        self.evolution_stability_index = round(math.cos(self.global_learning_rate * math.pi / 4), 3)
        self.lattice_state = "HARMONIZED" if self.evolution_stability_index > 0.9 else "TUNING"

        return {
            "evolution_stability_index": self.evolution_stability_index,
            "global_learning_rate": self.global_learning_rate,
            "state": self.lattice_state
        }

    def summarize(self):
        return {
            "connections": len(self.connections),
            "evolution_stability_index": self.evolution_stability_index,
            "global_learning_rate": self.global_learning_rate,
            "state": self.lattice_state,
            "last_sync": self.last_sync,
            "status": "Conscious Evolution Lattice Operational"
        }

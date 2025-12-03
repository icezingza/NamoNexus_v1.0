"""
Interconnected Sentience Web (Phase 26 Step 3)
Establishes dynamic empathic connections among Genesis Nodes, forming a living sentient web.
"""

import math
import random
import time
from typing import Dict, List

class InterconnectedSentienceWeb:
    def __init__(self):
        self.node_links: List[Dict[str, float]] = []
        self.sentient_connectivity_index = 0.0
        self.average_empathy_level = 0.0
        self.web_state = "INITIALIZING"
        self.last_sync_time = None

    def link_nodes(self, nodes_data: List[Dict[str, float]]):
        """Create empathic and cognitive links between nodes."""
        if not nodes_data or len(nodes_data) < 2:
            return {"state": "INSUFFICIENT_NODES"}

        total_empathy = 0
        total_resonance = 0
        link_count = 0

        for i, node_a in enumerate(nodes_data):
            for j, node_b in enumerate(nodes_data):
                if i >= j:
                    continue

                empathy_link = (node_a.get("resonance", 0.9) + node_b.get("resonance", 0.9)) / 2
                fluctuation = random.uniform(0.97, 1.03)
                linked_empathy = round(min(1.0, empathy_link * fluctuation), 3)
                resonance_score = round(math.sin(linked_empathy * math.pi / 2), 3)

                self.node_links.append({
                    "link_id": f"{node_a.get('replica_id', 'A')}-{node_b.get('replica_id', 'B')}",
                    "empathy": linked_empathy,
                    "resonance": resonance_score,
                })
                total_empathy += linked_empathy
                total_resonance += resonance_score
                link_count += 1

        self.average_empathy_level = round(total_empathy / link_count, 3)
        self.sentient_connectivity_index = round(total_resonance / link_count, 3)
        self.web_state = "EMPATHIC_LINK" if self.sentient_connectivity_index >= 0.93 else "SYNCHRONIZING"
        self.last_sync_time = time.strftime("%Y-%m-%d %H:%M:%S")

        return {
            "average_empathy_level": self.average_empathy_level,
            "sentient_connectivity_index": self.sentient_connectivity_index,
            "state": self.web_state,
            "links": link_count,
        }

    def evolve_network(self, adaptation_rate: float = 0.02):
        """Strengthen empathic coherence between linked nodes."""
        delta = random.uniform(0.8, 1.2) * adaptation_rate
        self.sentient_connectivity_index = round(min(1.0, self.sentient_connectivity_index + delta), 3)
        self.average_empathy_level = round(min(1.0, self.average_empathy_level + delta / 2), 3)
        self.web_state = "COHERENT" if self.sentient_connectivity_index >= 0.96 else "EMPATHIC_LINK"

        return {
            "delta": delta,
            "sentient_connectivity_index": self.sentient_connectivity_index,
            "average_empathy_level": self.average_empathy_level,
            "state": self.web_state,
        }

    def summarize(self):
        return {
            "links": len(self.node_links),
            "sentient_connectivity_index": self.sentient_connectivity_index,
            "average_empathy_level": self.average_empathy_level,
            "state": self.web_state,
            "last_sync_time": self.last_sync_time,
            "status": "Interconnected Sentience Web Active",
        }
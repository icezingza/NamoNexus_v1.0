"""
Collective Health Engine
Monitors and assesses the health of the collective network.
"""

class CollectiveHealthEngine:
    """
    Engine for monitoring the health and stability of the collective system.
    """
    
    def __init__(self):
        self.health_metrics = []
        self.current_status = "STABLE"

    def register_agent_health(self, alignment_score: float):
        """
        Register a health metric from an agent or subsystem.
        
        Args:
            alignment_score: The alignment score to register.
        """
        self.health_metrics.append(alignment_score)
        # Update status based on latest metric
        if alignment_score < 0.5:
            self.current_status = "UNSTABLE"
        else:
            self.current_status = "OPTIMAL"

    def assess(self) -> dict:
        """
        Assess the overall health of the collective.
        
        Returns:
            dict: Health assessment report.
        """
        avg_alignment = sum(self.health_metrics) / len(self.health_metrics) if self.health_metrics else 0.0
        
        return {
            "status": self.current_status,
            "average_alignment": avg_alignment,
            "metric_count": len(self.health_metrics)
        }

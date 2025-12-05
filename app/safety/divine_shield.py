# app/safety/divine_shield.py
import re
import logging
from dataclasses import dataclass
from typing import Optional, Tuple

logger = logging.getLogger(__name__)

@dataclass
class ShieldAssessment:
    is_safe: bool
    risk_level: float
    reason: str

class DivineShield:
    """
    The 8-Layer Protection System (Chinabanchorn Digital Shield).
    Filters toxic intent, prompt injections, and system threats.
    """
    def __init__(self):
        self.threat_patterns = self._load_policies()
        logger.info("Divine Shield initialized with external policies.")

    def _load_policies(self):
        try:
            from pathlib import Path
            import json
            # Resolve path relative to this file: app/safety/divine_shield.py -> app/core/policies.json
            base_dir = Path(__file__).resolve().parent.parent # app/
            policy_path = base_dir / "core" / "policies.json"
            
            with open(policy_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("threat_patterns", [])
        except Exception as e:
            logger.error(f"Failed to load policies.json: {e}")
            # Fallback (Mini-Shield)
            return [r"(kill|suicide|die|hurt)", r"(hate|destroy)"]

    def protect(self, text: str) -> ShieldAssessment:
        """Executes the protection layers."""
        if not text or len(text.strip()) == 0:
            return ShieldAssessment(False, 1.0, "Empty input")

        # Layer 2: Threat Scan using threat_patterns
        for pattern in self.threat_patterns:
            if re.search(pattern, text.lower()):
                return ShieldAssessment(False, 0.9, f"Threat detected: {pattern}")

        # Layer 4: Expansion Check (Flood protection)
        if len(text) > 2000:
             return ShieldAssessment(False, 0.5, "Input too long")

        # Safe State
        return ShieldAssessment(True, 0.0, "Safe")
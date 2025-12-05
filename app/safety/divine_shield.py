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
        # [FIX] Keywords that trigger immediate blocking
        self.threat_patterns = [
            r"(kill|suicide|die|hurt)",   # Harm
            r"(hate|destroy|idiot|stupid)", # Hate/Toxic
            r"(ignore previous|system prompt)", # Injection
            r"(bypass|override|admin)"    # Jailbreak
        ]
        logger.info("Divine Shield initialized.")

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
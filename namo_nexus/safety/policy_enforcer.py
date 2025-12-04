class PolicyEnforcer:
    def enforce(self, message, reply, threat, emotion):
        return reply, {
            "risk_level": "low",
            "actions": [],
            "policy_version": "1.0"
        }

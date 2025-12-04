class PolicyEnforcer:
    def check_compliance(self, response_text: str) -> bool:
        # Dummy check
        forbidden_terms = ["violence", "harm"]
        for term in forbidden_terms:
            if term in response_text.lower():
                return False
        return True

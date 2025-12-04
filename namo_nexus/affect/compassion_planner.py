class CompassionPlanner:
    def plan_reply(self, original_message, dharma_view, emotion, safe_template):
        if safe_template:
            return safe_template
        return "This is a compassionate reply."

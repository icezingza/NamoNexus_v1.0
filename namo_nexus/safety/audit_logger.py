import logging

class AuditLogger:
    def __init__(self):
        self.logger = logging.getLogger("namo_nexus.audit")

    def log_event(self, event_type: str, details: dict):
        self.logger.info(f"AUDIT [{event_type}]: {details}")

from typing import Dict, Any, List
from namo_nexus.api.schemas import ChatRequest
import json
from pathlib import Path
import os

class EpisodeLogger:
    """Logs each interaction for evolution and analysis."""

    def __init__(self) -> None:
        self._buffer: List[Dict[str, Any]] = []
        self._log_file = Path("logs/episodes.jsonl")
        # Ensure log directory exists
        try:
            os.makedirs(os.path.dirname(self._log_file), exist_ok=True)
        except OSError as e:
            print(f"Failed to create log directory: {e}")

    def log_event(
        self,
        trace_id: str,
        request: ChatRequest,
        reply: str,
        emotion: Dict[str, Any],
        dharma: Dict[str, Any],
        safety: Dict[str, Any],
        latency_ms: int,
    ) -> None:
        event = {
            "trace_id": trace_id,
            "user_id": request.user_id,
            "session_id": request.session_id,
            "message": request.message,
            "reply": reply,
            "emotion": emotion,
            "dharma": dharma,
            "safety": safety,
            "latency_ms": latency_ms,
        }
        self._buffer.append(event)

        if len(self._buffer) >= 1:
            self.flush()

    def flush(self) -> None:
        """Flushes the buffer to the log file."""
        if not self._buffer:
            return

        # Atomic swap to handle concurrency:
        # Capture current buffer and reset self._buffer immediately.
        # This prevents new events added during I/O from being lost/cleared.
        events_to_write = self._buffer
        self._buffer = []

        try:
            # Re-ensure directory exists in case it was deleted or init failed
            if not self._log_file.parent.exists():
                 self._log_file.parent.mkdir(parents=True, exist_ok=True)

            with open(self._log_file, "a") as f:
                for event in events_to_write:
                    f.write(json.dumps(event) + "\n")

        except Exception as e:
            # Log error to stderr
            print(f"Error flushing episode logs: {e}")
            # Note: events_to_write are lost here to prevent memory leak,
            # but we could choose to extend self._buffer with them again if we wanted retry.

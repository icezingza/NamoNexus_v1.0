"""Simple logging middleware for NaMoNexus.
Logs messages to stdout and to a rotating file under ./logs/.
"""
from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any


class LoggingMiddleware:
    """Lightweight logger that writes to console and file."""

    def __init__(self, name: str = "NaMoNexus", log_dir: str | Path = "logs", level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self._configure(log_dir, level)

    def _configure(self, log_dir: str | Path, level: int) -> None:
        log_path = Path(log_dir)
        log_path.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(log_path / "namo.log", maxBytes=512_000, backupCount=3)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.logger.setLevel(level)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def log(self, level: int, message: str, **extra: Any) -> None:
        self.logger.log(level, message, extra=extra if extra else None)

    def info(self, message: str, **extra: Any) -> None:
        self.log(logging.INFO, message, **extra)

    def warning(self, message: str, **extra: Any) -> None:
        self.log(logging.WARNING, message, **extra)

    def error(self, message: str, **extra: Any) -> None:
        self.log(logging.ERROR, message, **extra)

    def debug(self, message: str, **extra: Any) -> None:
        self.log(logging.DEBUG, message, **extra)

"""FastAPI logging middleware for request tracing and metrics."""
from __future__ import annotations

import logging
import time
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Awaitable, Callable
from uuid import uuid4

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from namo_nexus.core.config import get_settings


def setup_logging() -> None:
    """Configure root logging based on application settings."""

    settings = get_settings()
    if not settings.FEATURE_FLAGS.get("ENABLE_LOGGING", True):
        return

    level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    logger = logging.getLogger()

    if logger.handlers:
        logger.setLevel(level)
        return

    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(log_dir / "namo_requests.log", maxBytes=1_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware that logs HTTP method, path, status, and latency with a request ID."""

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        settings = get_settings()
        if not settings.FEATURE_FLAGS.get("ENABLE_LOGGING", True):
            return await call_next(request)

        request_id = str(uuid4())
        start_time = time.perf_counter()

        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        logging.getLogger(__name__).info(
            "%s %s -> %s in %.2fms [req_id=%s]",
            request.method,
            request.url.path,
            response.status_code,
            elapsed_ms,
            request_id,
        )

        response.headers["X-Request-ID"] = request_id
        return response

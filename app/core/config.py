"""Configuration utilities for NaMoNexus core settings."""
from functools import lru_cache
from typing import Dict

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment or defaults."""

    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MEMORY_PATH: str = "data/memory_log.json"
    MAX_MEMORY_ENTRIES: int = 200

    FEATURE_FLAGS: Dict[str, bool] = {
        "ENABLE_SAFETY": True,
        "ENABLE_MEMORY": True,
        "ENABLE_DHAMMA_REFLECTION": True,
        "ENABLE_COHERENCE_SCORE": True,
        "ENABLE_LOGGING": True,
    }

    class Config:
        env_prefix = "NAMO_"
        case_sensitive = False


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance."""

    return Settings()

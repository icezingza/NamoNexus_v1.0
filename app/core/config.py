# app/core/config.py
from functools import lru_cache
from typing import Dict, Any

# Robust import for BaseSettings + ConfigDict (supports pydantic v1/v2)
try:
    try:
        from pydantic_settings import BaseSettings
    except ImportError:
        from pydantic import BaseSettings
    from pydantic import ConfigDict
except Exception:
    # Fallback if pydantic_settings is broken or missing
    from pydantic import BaseModel

    class BaseSettings(BaseModel):
        pass

    class ConfigDict(dict):  # type: ignore
        def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)


class Settings(BaseSettings):
    """Application settings loaded from environment or defaults."""

    model_config = ConfigDict(env_prefix="NAMO_", case_sensitive=False)

    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"
    MEMORY_PATH: str = "data/memory_log.json"
    MAX_MEMORY_ENTRIES: int = 200

    # [NEW] The Golden Ratio Constant
    PHI: float = 1.61803398875

    FEATURE_FLAGS: Dict[str, bool] = {
        "ENABLE_SAFETY": True,
        "ENABLE_MEMORY": True,
        "ENABLE_DHAMMA_REFLECTION": True,
        "ENABLE_COHERENCE_SCORE": True,
        "ENABLE_LOGGING": True,
        "ENABLE_INFINITY_MEMORY": True,
    }


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

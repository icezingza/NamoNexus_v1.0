from dataclasses import dataclass
from datetime import datetime


@dataclass
class SystemManifest:
    """Simple manifest inspired by FormGenesis manifest."""
    name: str = "NamoNexus"
    version: str = "0.1.0"
    stage: str = "alpha"
    build_id: str = "dev"
    created_at: str = datetime.utcnow().isoformat() + "Z"

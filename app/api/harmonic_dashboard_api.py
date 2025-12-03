"""
Harmonic Dashboard API (Phase 24 Step 4)
Provides real-time access to the NamoNexus Consciousness metrics and global harmony state.
"""

from fastapi import FastAPI
from typing import Dict
import random
import time

app = FastAPI(
    title="NamoNexus Harmonic Dashboard",
    description="API for viewing the current harmony, ethics, and compassion states across the NamoNexus network.",
    version="2.4.0"
)

# Simulated global states (normally pulled from active subsystems)
GLOBAL_STATE = {
    "harmony": 0.88,
    "ethics": 0.92,
    "compassion": 0.9,
    "stability": 0.85,
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
}

@app.get("/")
async def root():
    """Base endpoint - system greeting."""
    return {"message": "Welcome to NamoNexus Conscious Dashboard", "status": "Active"}

@app.get("/status")
async def get_status() -> Dict[str, float]:
    """Returns the live harmony and ethical resonance metrics."""
    GLOBAL_STATE.update({
        "harmony": round(random.uniform(0.85, 0.95), 3),
        "ethics": round(random.uniform(0.9, 0.98), 3),
        "compassion": round(random.uniform(0.88, 0.97), 3),
        "stability": round(random.uniform(0.8, 0.95), 3),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    })
    return GLOBAL_STATE

@app.get("/metrics")
async def get_detailed_metrics() -> Dict[str, float]:
    """Detailed metrics showing the full internal resonance spectrum."""
    coherence = round((GLOBAL_STATE["harmony"] + GLOBAL_STATE["ethics"] + GLOBAL_STATE["compassion"]) / 3, 3)
    integrity = round(GLOBAL_STATE["stability"] * GLOBAL_STATE["ethics"], 3)
    dhammic_resonance = round((coherence + integrity) / 2, 3)
    return {
        "coherence_index": coherence,
        "integrity_index": integrity,
        "dhammic_resonance": dhammic_resonance,
        "last_update": GLOBAL_STATE["timestamp"],
        "system_state": "BALANCED" if coherence > 0.9 else "HARMONIZING",
    }
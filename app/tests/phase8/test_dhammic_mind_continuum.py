"""
Test for Phase 8: Dhammic Mind Continuum
"""
import asyncio
import pytest
from app.core.continuum.reflective_synchrony_engine import ReflectiveSynchronyEngine
from app.core.continuum.collective_growth_matrix import CollectiveGrowthMatrix
from app.core.continuum.adaptive_continuum_memory import AdaptiveContinuumMemory
from app.core.continuum.supervisor_mirror_protocol import SupervisorMirrorProtocol

@pytest.mark.asyncio
async def test_dhammic_mind_continuum_flow():
    rse = ReflectiveSynchronyEngine()
    cgm = CollectiveGrowthMatrix()
    acm = AdaptiveContinuumMemory()
    smp = SupervisorMirrorProtocol()

    reflections = [
        ("A1", "Compassion grows with awareness", 0.72),
        ("A2", "Understanding impermanence", 0.65),
        ("A3", "Calm reflects clarity", 0.83)
    ]

    for a, r, g in reflections:
        ref = await rse.synchronize(a, r, g)
        acm.append(ref)
        cgm.record_growth(a, compassion=g, wisdom=(g + 0.2))

    summary = await rse.summarize()
    dri = cgm.compute_continuum()
    note = smp.evaluate(summary)

    print("🪞 Continuum Summary:", summary)
    print("💠 Dhammic Resonance Index (DRI):", dri)
    print("📡 Supervisor Mirror:", note)



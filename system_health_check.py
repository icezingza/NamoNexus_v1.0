import sys
import os
import traceback
import asyncio
from typing import Dict, Any

print("="*60)
print("NAMO NEXUS: SYSTEM HEALTH DIAGNOSTIC")
print("="*60)

# 1. Environment Check
print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")
print("-" * 60)

# 2. Import Check
modules_to_check = [
    "app.core.config",
    "app.memory.infinity_memory",
    "app.emotion.neuro_empathic_mirror",
    "app.personality.dhammic_reflection_engine",
    "app.safety.divine_shield",
    "app.personality.namo_persona_core",
    "app.api.gateway"
]

failed_imports = []

for module in modules_to_check:
    try:
        print(f"Testing Import: {module}...", end=" ")
        __import__(module)
        print("[OK]")
    except Exception as e:
        print("[FAIL]")
        print(f"   Error: {e}")
        failed_imports.append(module)

if failed_imports:
    print("-" * 60)
    print(f"[CRITICAL] {len(failed_imports)} modules failed to import.")
    print("   Please fix the environment or dependencies first.")
    sys.exit(1)

print("-" * 60)
print("[OK] All core modules imported successfully.")
print("-" * 60)

# 3. Logic Check (Simulation)
async def run_simulation():
    print("Initializing NamoPersonaCore...")
    try:
        from app.personality.namo_persona_core import NamoPersonaCore
        persona = NamoPersonaCore()
        
        test_input = "I feel a bit lost and anxious today."
        print(f"[User] {test_input!r}")
        
        print("Processing...")
        result = await persona.process(test_input)
        
        print("\nProcessing complete.")
        print(f"   Response: {result.get('reflection_text')}")
        print(f"   Tone: {result.get('tone')}")
        print(f"   Coherence: {result.get('coherence')}")
        print(f"   Memory: {result.get('memory_summary')}")
        
        return True
    except Exception as e:
        print(f"\n❌ Runtime Error during simulation:")
        traceback.print_exc()
        return False

# Run Async Simulation
try:
    success = asyncio.run(run_simulation())
    print("-" * 60)
    if success:
        print("SYSTEM STATUS: OPERATIONAL")
    else:
        print("SYSTEM STATUS: PARTIALLY BROKEN")
except Exception as e:
    print(f"Fatal Error: {e}")

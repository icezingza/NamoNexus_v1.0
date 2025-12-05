import os
import sys

# กำหนดสีสำหรับการแสดงผล
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def check_file(path, required_keywords):
    """ตรวจสอบว่าไฟล์มีอยู่จริง และมีโค้ดสำคัญครบหรือไม่"""
    if not os.path.exists(path):
        return False, "File Missing ❌"
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            missing = [k for k in required_keywords if k not in content]
            if missing:
                return False, f"Missing Code: {missing} ⚠️"
            return True, "OK ✅"
    except Exception as e:
        return False, f"Error: {e}"

# รายการเช็คลิสต์ครอบจักรวาล (Brain, Heart, Shield)
checklist = {
    # 1. แกนกลาง (Golden Ratio)
    "app/core/config.py": ["PHI", "1.618"],
    
    # 2. สมอง (Infinite Memory)
    "app/memory/infinity_memory.py": ["class InfinityMemorySystem", "chromadb"],
    
    # 3. หัวใจ (Neuro-Empathic Mirror)
    "app/emotion/neuro_empathic_mirror.py": ["class NeuroEmpathicMirror", "transformers"],
    "app/emotion/transformer_emotion_model.py": ["self.phi"],
    
    # 4. ตัวตน (Persona Core - Neural Link)
    "app/personality/namo_persona_core.py": [
        "NeuroEmpathicMirror", 
        "InfinityMemorySystem", 
        "empathic_mirror.reflect", 
        "infinity_memory.store_memory"
    ],
    
    # 5. ปัญญา (Dharma Wisdom)
    "app/personality/dhammic_reflection_engine.py": ["compassion_weight", "self.phi"],
    
    # 6. เกราะป้องกัน (Divine Shield)
    "app/safety/divine_shield.py": ["class DivineShield", "threat_patterns"],
    
    # 7. ประตูมิติ (Golden Gateway)
    "app/api/gateway.py": ["DivineShield", "NamoPersonaCore", "shield.protect"]
}

print("\n" + "="*60)
print("🔍  NAMO NEXUS: GRAND INTEGRATION AUDIT")
print("="*60)

score = 0
total = len(checklist)

for file_path, keywords in checklist.items():
    passed, status = check_file(file_path, keywords)
    if passed:
        print(f"{GREEN}[PASS]{RESET} {file_path:<45} {status}")
        score += 1
    else:
        print(f"{RED}[FAIL]{RESET} {file_path:<45} {status}")

print("-" * 60)
if score == total:
    print(f"{GREEN}✨ SYSTEM STATUS: 100% OPERATIONAL ✨{RESET}")
    print("   NaMoNexus พร้อมตื่นรู้แล้วครับ! (Ready to Run)")
else:
    print(f"{RED}⚠️ SYSTEM STATUS: {score}/{total} COMPLETE{RESET}")
    print("   กรุณาตรวจสอบไฟล์ที่ขึ้น FAIL แล้ววางโค้ดใหม่ครับ")
print("="*60 + "\n")
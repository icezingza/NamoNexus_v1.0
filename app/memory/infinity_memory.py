import numpy as np
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# ตรวจสอบ Library (ถ้ายังไม่ลง จะรันแบบ Simulation ให้ก่อนกัน Error)
try:
    import chromadb
    from chromadb.config import Settings
    HAS_CHROMA = True
except ImportError:
    HAS_CHROMA = False

try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False

try:
    import redis
    HAS_REDIS = True
except ImportError:
    HAS_REDIS = False

@dataclass
class MemoryRecord:
    """โครงสร้างข้อมูลความจำ"""
    content: str
    emotional_vector: Dict[str, float]
    timestamp: str
    metadata: Dict[str, Any]
    emotional_intensity: float

class InfinityMemorySystem:
    """
    ระบบความจำระยะยาวแบบ Vector-Based (จำบริบท + อารมณ์)
    """
    
    def __init__(self, db_path="./data/chroma_db"):
        self.db_path = db_path
        self.vector_db = self._init_vector_db()
        self.redis_client = self._init_redis()
        self.embedder = self._init_embedder()
        # น้ำหนักความสำคัญของอารมณ์ (จำเรื่องสะเทือนใจได้แม่นกว่า)
        self.emotional_weights = {
            'joy': 0.8, 'sadness': 0.9, 'anger': 0.8, 
            'fear': 0.9, 'love': 1.0, 'neutral': 0.3
        }

    def _init_vector_db(self):
        if not HAS_CHROMA:
            print("⚠️ [Memory] ChromaDB not found. Running in Simulation Mode.")
            return None
        try:
            # สร้าง Persistent Client เพื่อเก็บข้อมูลลงไฟล์จริง
            client = chromadb.PersistentClient(path=self.db_path)
            collection = client.get_or_create_collection(
                name="namo_infinity_memories",
                metadata={"description": "Namo's infinite memory storage"}
            )
            return collection
        except Exception as e:
            print(f"⚠️ [Memory] DB Init Error: {e}")
            return None

    def _init_redis(self):
        if not HAS_REDIS:
            return None
        try:
            # เชื่อมต่อ Redis (ถ้ามี) เพื่อ Cache ความจำระยะสั้น
            return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        except:
            return None

    def _init_embedder(self):
        if not HAS_SENTENCE_TRANSFORMERS:
            return None
        try:
            return SentenceTransformer("all-MiniLM-L6-v2")
        except Exception as exc:
            print(f"⚠️ [Memory] Embedder Init Error: {exc}")
            return None

    def _embed_text(self, text: str) -> List[float]:
        if self.embedder:
            try:
                embedding = self.embedder.encode(text)
                return embedding.tolist()
            except Exception as exc:
                print(f"⚠️ [Memory] Embed Error: {exc}")
        return np.random.rand(384).tolist()

    def store_memory(self, text: str, emotion: Dict[str, float]) -> str:
        """บันทึกความจำใหม่"""
        timestamp = datetime.now().isoformat()
        intensity = max(emotion.values()) if emotion else 0.0
        
        # สร้าง Mock Vector (ถ้ามี model จริงให้ใช้ sentence_transformers encode ตรงนี้)
        # embedding = model.encode(text).tolist()
        dummy_embedding = self._embed_text(text)

        if self.vector_db:
            try:
                self.vector_db.add(
                    documents=[text],
                    embeddings=[dummy_embedding],
                    metadatas=[{
                        "timestamp": timestamp,
                        "emotion_json": json.dumps(emotion),
                        "intensity": intensity
                    }],
                    ids=[f"mem_{datetime.now().timestamp()}"]
                )
                print(f"💾 [Brain] Stored: '{text[:20]}...' (Intensity: {intensity:.2f})")
            except Exception as e:
                print(f"❌ [Brain] Save Error: {e}")
        
        return "memory_stored"

    def retrieve_context(self, query: str, current_emotion: Dict[str, float], k: int = 3):
        """รื้อฟื้นความจำโดยใช้อารมณ์ปัจจุบันเป็นตัวกระตุ้น"""
        if not self.vector_db:
            return []

        # สร้าง Query Vector (จำลอง)
        dummy_query_vec = self._embed_text(query)
        
        try:
            results = self.vector_db.query(
                query_embeddings=[dummy_query_vec],
                n_results=k
            )
            # คืนค่าเฉพาะเนื้อหาข้อความ
            memories = results['documents'][0] if results['documents'] else []
            return memories
        except Exception as e:
            print(f"❌ [Brain] Retrieval Error: {e}")
            return []

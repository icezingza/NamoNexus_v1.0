import json
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

import numpy as np
from app.core.config import get_settings

# ตรวจสอบ Library (ถ้ายังไม่ลง จะรันแบบ Simulation ให้ก่อนกัน Error)
try:
    import chromadb
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

logger = logging.getLogger(__name__)

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
        self.settings = get_settings()
        self.phi = self.settings.PHI
        self.db_path = db_path
        self.vector_db = self._init_vector_db()
        self.redis_client = self._init_redis()
        self.embedder = self._init_embedder()
        # น้ำหนักความสำคัญของอารมณ์ (จำเรื่องสะเทือนใจได้แม่นกว่า)
        self.emotional_weights = {
            'joy': 0.8, 'sadness': 0.7, 'anger': 0.6,
            'fear': 0.9, 'surprise': 0.5, 'love': 1.0
        }

    def _init_vector_db(self):
        if not HAS_CHROMA:
            logger.warning("ChromaDB not found. Running in Simulation Mode.")
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
            logger.error(f"Failed to initialize ChromaDB: {e}")
            return None

    def _init_redis(self):
        if not HAS_REDIS:
            return None
        try:
            # เชื่อมต่อ Redis (ถ้ามี) เพื่อ Cache ความจำระยะสั้น
            return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        except Exception as exc:
            logger.warning(f"Failed to connect to Redis: {exc}")
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

    def _calculate_temporal_relevance(self, memory_timestamp: str) -> float:
        """คำนวณน้ำหนักความเกี่ยวข้องตามเวลาโดยใช้ค่า Phi."""
        try:
            mem_time = datetime.fromisoformat(memory_timestamp)
            hours_passed = (datetime.now() - mem_time).total_seconds() / 3600
            decay_factor = self.phi ** (hours_passed / 24.0)
            return 1.0 / decay_factor
        except Exception:
            return 1.0

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
                logger.info(f"Memory stored successfully. Intensity: {intensity:.2f}")
            except Exception as e:
                logger.error(f"Error storing memory: {e}")

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
                n_results=k,
                include=["documents", "metadatas"]
            )
            # คืนค่าเฉพาะเนื้อหาข้อความ
            documents = results.get('documents', [])
            metadatas = results.get('metadatas', [])

            if documents and metadatas:
                scored_results = []
                for doc, meta in zip(documents[0], metadatas[0]):
                    timestamp = meta.get("timestamp") if isinstance(meta, dict) else None
                    intensity = float(meta.get("intensity", 0.0)) if isinstance(meta, dict) else 0.0
                    temporal_score = self._calculate_temporal_relevance(timestamp) if timestamp else 1.0
                    combined_score = temporal_score * max(intensity, 0.0)
                    scored_results.append((doc, combined_score))

                scored_results.sort(key=lambda item: item[1], reverse=True)
                return [doc for doc, _ in scored_results]

            return documents[0] if documents else []
        except Exception as e:
            logger.error(f"Error retrieving context: {e}")
            return []

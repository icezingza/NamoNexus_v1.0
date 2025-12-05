"""
Database Integration (Phase 30 Step 2)
Persistent memory store for NamoNexus.
"""

from sqlalchemy import create_engine, Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./namo_memory.db"  # replace with PostgreSQL in production

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Memory(Base):
    __tablename__ = "memory"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    message = Column(Text)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def log_interaction(user_id, message, response):
    session = SessionLocal()
    record = Memory(user_id=user_id, message=message, response=response)
    session.add(record)
    session.commit()
    session.close()


NamoNexus FastAPI Gateway (Phase 30 Step 1)
Provides RESTful endpoints for interacting with the AI Core.
"""

from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.core.supervisor import Supervisor
from app.core.memory import MemoryStore

app = FastAPI(title="NamoNexus API", version="1.0")

supervisor = Supervisor()
memory = MemoryStore()

class UserQuery(BaseModel):
    user_id: str
    message: str

@app.post("/interact")
async def interact(query: UserQuery):
    """Handle user message and return AI response."""
    memory.save_interaction(query.user_id, query.message)
    response = supervisor.process_input(query.message)
    memory.save_response(query.user_id, response)
    return {"user": query.user_id, "response": response}

@app.get("/status")
def status():
    """System health check."""
    return {"system": "NamoNexus", "status": "active", "version": "1.0"}

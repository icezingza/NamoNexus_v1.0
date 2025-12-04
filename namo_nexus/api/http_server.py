from fastapi import FastAPI, HTTPException
from namo_nexus.api.schemas import ChatRequest, ChatResponse
from namo_nexus.core.orchestrator import Orchestrator

app = FastAPI(title="NamoNexus API", version="1.0")
orchestrator = Orchestrator()

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = await orchestrator.process(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "NamoNexus"}

# app/api/http_server.py
from fastapi import FastAPI, Depends
from app.api.schemas import ChatRequest, ChatResponse
from app.core.orchestrator import Orchestrator

app = FastAPI(title="NamoNexus API", version="0.1.0")


def get_orchestrator() -> Orchestrator:
    # In real deployment you may want a singleton / DI container.
    return Orchestrator()


@app.post("/v1/chat", response_model=ChatResponse)
def chat(req: ChatRequest, orchestrator: Orchestrator = Depends(get_orchestrator)) -> ChatResponse:
    return orchestrator.process_chat(req)


@app.get("/v1/health")
def health() -> dict:
    return {"status": "ok"}

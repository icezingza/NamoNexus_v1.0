from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's message")
    user_id: str = Field(default="default_user", description="The ID of the user")

class ChatResponse(BaseModel):
    response: str = Field(..., description="The response from the AI")

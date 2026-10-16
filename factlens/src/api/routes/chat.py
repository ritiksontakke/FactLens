from fastapi import APIRouter

from src.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chats"])

@router.post("",response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatRequest:
    return ChatResponse(
        project="FactLens",
        question=request.question,
        message="Your question was received successfully.",
        status="received",
    )
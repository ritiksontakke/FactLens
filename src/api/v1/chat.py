from src.schemas.chat import ChatRequest,ChatResponse

from fastapi import APIRouter

router = APIRouter(prefix="/Chat" , tags=["Chat"])

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return ChatResponse(
        answer=f"FactLens received your question: {request.query}",
        status="received",
    )
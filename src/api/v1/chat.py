from fastapi import APIRouter, HTTPException

from src.schemas.chat import ChatRequest, ChatResponse
from src.agents.Orchestrator_Agent import orchestratorAgent

router = APIRouter(prefix="/Chat", tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    print("\n[API] NEW CHAT REQUEST RECEIVED")
    print("[API] User Query:", request.query)

    try:

        result = orchestratorAgent(request.query)

        print("\n[API] RESPONSE SENT SUCCESSFULLY")

        return ChatResponse(
            answer=result["final_answer"]
        )

    except Exception as e:

        print("\n[API ERROR]", str(e))

        raise HTTPException(
            status_code=500,
            detail=f"Research failed: {str(e)}"
        )
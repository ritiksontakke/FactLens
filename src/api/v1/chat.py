from src.schemas.chat import ChatRequest,ChatResponse

from fastapi import APIRouter,HTTPException
from src.agents.researcherAgent import research_agent

router = APIRouter(prefix="/Chat" , tags=["Chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = research_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.query,
                    }
                ]
            }
        )

        answer = result["messages"][-1].content

        return ChatResponse(answer=answer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Research failed: {str(e)}",
        )

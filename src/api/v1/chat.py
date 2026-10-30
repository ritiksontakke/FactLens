from fastapi import APIRouter, HTTPException
from src.schemas.chat import ChatRequest, ChatResponse
from src.agents.Orchestrator_Agent import orchestratorAgent
import logging

router = APIRouter(prefix="/Chat", tags=["Chat"])



@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:
        print("Calling orchestratorAgent...")

        agent = orchestratorAgent()

        print("Returned object:", agent)
        print("Returned type:", type(agent))


        result = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": request.query
                }
            ]
        })

        answer = result["messages"][-1].content

        return ChatResponse(answer=answer)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Research failed: {str(e)}"
        )
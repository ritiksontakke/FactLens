from pydantic import BaseModel , Field

class ChatRequest(BaseModel):
    query : str = Field(
        min_length=1,
        max_length=2000,
        description="Question to research using FactLens"
    )

class ChatResponse(BaseModel):
    answer: str
    status : str
from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI(
    title="FactLens",
    description="AI-powered research and fact-checking assistant",
    version="0.1.0",
)


from src.api.v1.chat import router as chat_router

app.include_router(chat_router, prefix="/api/v1")

@app.get("/")
async def home():
    return {
        "app": "FactLens",
        "message": "Welcome to FactLens!",
        "status": "running",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


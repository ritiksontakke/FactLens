from fastapi  import FastAPI

app = FastAPI(
    title="FactLens API",
    description="Evidence-based current information and fact verification.",
    version="0.1.0",
)

@app.get("/")
def root():
    return{
        "project": "FactLens",
        "message": "FactLens backend is running",
        "status": "ok",
    }

@app.get("/health")
def health():
    return{
        "status": "healthy"
    }

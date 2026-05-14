from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="UOSADVICE API",
    description="Backend services for the UOSADVICE platform",
    version="1.0.0"
)

@app.get("/", tags=["Health Check"])
async def root():
    """
    Returns the current status of the backend.
    """
    return {
        "status": "online",
        "service": "UOSADVICE Backend",
        "timestamp": datetime.now().isoformat(),
        "docs": "/docs"
    }

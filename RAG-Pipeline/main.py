# Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Router imports
from app.router.fileRouter import FileRouter
from app.router.ragRouter import RagRouter

# Server object
app = FastAPI(
    title="RAG Pipeline",
    version="0.1.0",
    description="Example of how RAG Pipeline works"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def root_route():
    return {
        "message": "RAG Pipeline API is running !"
    }

# Routers
# Upload router
app.include_router(FileRouter, prefix="/api/v1/file", tags=["upload"])

# ask router
app.include_router(RagRouter, prefix="/api/v1/ask", tags=["ask"])


# Entry point
if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True
    )



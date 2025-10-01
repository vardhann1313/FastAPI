from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Getting Started",
    description="A simple FastAPI application",
    version="0.0.1",
)

@app.get("/")
def read_root():
    return {
        "message": "Server is running !"
    }

# Mandatory while running using "uv run main.py"
if __name__ == "__main__":
    uvicorn.run(app)

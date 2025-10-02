import uvicorn
from fastapi import FastAPI
from Routes.TodoRoutes import router

app = FastAPI()

# Root Route
@app.get("/")
def read_root():
    return {"message": "Server is running !"}

# Todo router
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app)
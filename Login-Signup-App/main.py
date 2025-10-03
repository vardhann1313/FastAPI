# Importing modules
from fastapi import FastAPI
import uvicorn

# Importing router
from App.Route import Router

# Creating server
app = FastAPI(
    title="Login-Signup-App",
    description="Login-Signup-App using mongoDB",
    version="0.0.1",
)

# Root route
@app.get("/")
def root() : return{"message": "Server is running !"}

# Auth route
app.include_router(Router, prefix="/api/v1", tags=["Auth"])

# Starting server
if __name__ == "__main__":
    uvicorn.run(app)
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK
import uvicorn

from Service import Hash_password

# Server creation
app = FastAPI(
    title = "Password Hash generator",
    description = "Hash generator from a simple password",
    version = "1.0.0"
)

# Root route
@app.get("/")
def root():
    return {
        "message": "Server is running !",
        "success": True
    }

# password hashing route
@app.post("/get_HashCode")
def hash_Pass(password: str) -> JSONResponse:

    #Get password hash
    hashCode = Hash_password(password)

    # Send response back
    return JSONResponse(
        status_code=HTTP_200_OK,
        content={
            "hashCode": hashCode,
            "success": True
        }
    )

# Starting server
if __name__ == "__main__":
    uvicorn.run(app)

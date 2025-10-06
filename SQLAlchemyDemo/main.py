# Module imports
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.responses import JSONResponse
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
import uvicorn

# Custom module imports
from App.DTOs import UserSignup
from App.Dependencies import get_db
from App.model import User

# Server creation
app = FastAPI(
    title="Setting up SQLAlchemy",
    description="Understanding SQLAlchemy work flow",
    version="1.0.0"
)

# Root route
@app.get("/")
def root_route():
    return {
        "message": "Server is running !",
        "success": True
    }

# User Signup route
@app.post("/create_user")
async def user_signup(user : UserSignup, db : AsyncSession = Depends(get_db)) -> JSONResponse:
    
    try:

        # Checking if user already present
        isUser = await db.execute(select(User).where(User.email == user.email))
        if isUser:
            # If so, raise error
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="User already registered !"
            )

        # If not, create user object
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password    
        )

        # Save it in DB
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        # Send back response
        return JSONResponse(
            status_code=HTTP_201_CREATED,
            content={
                "data": {
                    "id": new_user.id,
                    "name": new_user.name,
                    "email": new_user.email
                },
                "success": True
            }
        )

    # Handle exception if any
    except Exception as e:

        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


# Start server
if __name__ == "__main__":
    uvicorn.run(app)

# Importing modules for JWT token ---------
from turtle import st
from fastapi import HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from starlette.status import HTTP_401_UNAUTHORIZED

# Define configuration constants (Should be in dotenv folder)
SECRET_KEY = "your-secret-key-keep-it-secret"  # A random secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# -------------------------------------------------------

# Function to create jwt token --------------------------
def create_token(data: dict) -> str:

    # Setting expiration time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Setting data for encoding
    to_encode = data.copy()
    to_encode.update({"exp": expire})

    # Generating token
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Return token 
    return token
# --------------------------------------------------------

# Function to validate incoming token --------------------
def validate_token(token: str) -> str:
    try:
        # Decoding token 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extract userId from token
        userId: str = payload.get("userId")

        # Checking if userId is present
        if userId is None:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid token !"
            )

        # Returning userId
        return userId

    except JWTError:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid token !",
        )
# -----------------------------------------------------------
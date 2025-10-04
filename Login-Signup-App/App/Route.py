from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

# Setting up token retrieval -- expects /login to provide token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()

from .Model import UserLogin, UserSignup
from .AuthService import signup, login, get_details

# Creating router
Router = APIRouter()

# Signup router
@Router.post("/signup")
async def signup_route(user: UserSignup) -> JSONResponse:
    return await signup(user.model_dump())

# Login router
@Router.post("/login")
async def login_route(user: UserLogin) -> JSONResponse:
    return await login(user.model_dump())

# Restricted resource
@Router.get("/get")
async def get_user_details(credentials: HTTPAuthorizationCredentials = Depends(security)) -> JSONResponse:
    return await get_details(token=credentials.credentials)
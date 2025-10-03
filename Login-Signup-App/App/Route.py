from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .Model import UserLogin, UserSignup
from .AuthService import signup, login

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
from typing import Dict
from bson import ObjectId
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

# JWT, DB and password hashing functions
from .Database import DB
from App.Utils.JWTUtils import create_token, validate_token
from App.Utils.PasswordUtils import hash_password, verify_password

# User signup service method
async def signup(user: Dict) -> JSONResponse:
    try:
        # Find if user is already present --
        if await DB["users"].find_one({"email": user["email"]}):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="User already registered !"
            )

        # If user is not already registered then Hash password --
        user["password"] = hash_password(user["password"])

        # Insert user into database --
        result = await DB["users"].insert_one(user)

        # Retrieve the saved user & convert ObjectId to string --
        saved_user = await DB["users"].find_one({"_id": result.inserted_id})
        saved_user["_id"] = str(saved_user["_id"])
    
        # Set token to send back in response --
        token = create_token(data={"userId": saved_user["_id"]})

        # Sending response --
        return JSONResponse(
            status_code=HTTP_201_CREATED,
            content={
                "message": "User created successfully",
                "success": True,
                "user": saved_user,
                "token": token
            }
        )

    except Exception as e:
        # Extract code from exception
        code = int(str(e).split(":")[0])
        raise HTTPException(
            status_code=code,
            detail=str(e)
        )

# User login service method
async def login(user: Dict) -> JSONResponse:

    try:
        # Find user in DB
        found_user = await DB["users"].find_one({"email": user["email"]})
        if not found_user:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="User not found !"
            )

        # validating password
        if not verify_password(plain_pass=user["password"], hash_pass=found_user["password"]):
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Invalid email or password !"
            )

        # If user found, update its objectId for JSON serializable
        found_user["_id"] = str(found_user["_id"])

        # If password matches generate JWT and return with response
        token = create_token(data={"userId": found_user["_id"]})

        # Sending response
        return JSONResponse(
            status_code=HTTP_200_OK,
            content={
                "message": "Login successfull",
                "success": True,
                "user": user,
                "token": token
            }
        )

    except Exception as e:
        # Extract code from exception and raise error
        code = int(str(e).split(":")[0])
        raise HTTPException(
            status_code=code,
            detail=str(e)
        )

# Restricted API example
async def get_details(token: str) -> JSONResponse:

    # Extracting userId from token
    userId = ObjectId(validate_token(token=token))

    try:

        # Finding user in DB
        user = await DB["users"].find_one({"_id": userId})
        if not user:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="User not found !"
            )

        # Solving ObjectId issue
        user["_id"] = str(user["_id"])

        # Sending response
        return JSONResponse(
            status_code=HTTP_200_OK,
            content={
                "success": True,
                "data": user
            }
        )

    except Exception as e:
        code = int(str(e).split(":")[0])
        raise HTTPException(
            status_code=code,
            detail=str(e)
        )
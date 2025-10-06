from pydantic import BaseModel, EmailStr

# UserSignup Data Transfer Object
class UserSignup(BaseModel):

    name: str
    email: EmailStr
    password: str

# UserLogin Data Transfer Object
class UserLogin(BaseModel):

    email: EmailStr
    password: str
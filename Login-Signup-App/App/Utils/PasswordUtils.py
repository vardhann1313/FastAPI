# Importing modules for passowrd hashing ---------
from passlib.context import CryptContext

# Creating context -------------------------------
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Function to hash password ----------------------
def hash_password(password: str) -> str:

    return  pwd_context.hash(password)

# Function to verify password ---------------------
def verify_password(plain_pass: str, hash_pass: str) -> bool:

    return pwd_context.verify(plain_pass, hash_pass)

# -------------------------------------------------
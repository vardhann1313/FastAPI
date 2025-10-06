# Module import for password hashing
from passlib.context import CryptContext

# Password context
pass_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Function to hash password
def Hash_password(password: str) -> str:
    return pass_context.hash(password)

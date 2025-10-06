from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Connection string
DATABASE_URL = "mysql+aiomysql://root:root@localhost:3306/fastapiTesting"

# Creating async engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Creating async session
async_session_maker = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Base class for models
Base = declarative_base()
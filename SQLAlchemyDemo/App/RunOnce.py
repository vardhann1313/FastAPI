""" This file needs to be ran once to create and map all tables written in model with actual database """

# Module imports
import asyncio
from Database import Base, engine
from model import User  # Import the model to register it with Base

# Function to init tables
async def init_models():
    async with engine.begin() as conn:

        # Drop previous tables if exists and create fresh tables
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# Running function
if __name__=="__main__":
    asyncio.run(init_models())
from App.Database import async_session_maker

# To get DB instance
async def get_db():
    async with async_session_maker() as session:
        yield session
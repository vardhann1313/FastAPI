from fastapi import APIRouter, Query
from app.service.ragService import ask_service

# Router
RagRouter = APIRouter()

# Router to get answer from uploaded file
@RagRouter.post("/{filename}")
async def ask_route(
        filename: str,
        question: str = Query(...)
    ):

    # Call service method
    return await ask_service(filename, question)
from fastapi import APIRouter, UploadFile, File
from app.service.fileService import upload_file_service

# Router
FileRouter = APIRouter()

# Router to create new chat
@FileRouter.post("/upload")
async def upload_file_route(file: UploadFile = File(...)):

    # Call service method
    return await upload_file_service(file=file)
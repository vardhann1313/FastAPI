# Inbuilt imports
import os
from pypdf import PdfReader
import docx2txt
import uuid
from fastapi import UploadFile, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

# Custom imports
from app.config.directoryConfig import UPLOAD_DIR


# Allowed extentions
ALLOWED_EXTENTIONS = {".pdf", ".txt", ".docx"}

# Function to validate extentions
def validate_extentions(filename: str):
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENTIONS:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Unsupported file type !"
        )

    return ext

# Generate unique filename
def generate_unique_filename(original_filename: str) -> str:
    ext = os.path.splitext(original_filename)[1]  
    unique_name = f"{uuid.uuid4().hex}{ext}"     
    return unique_name

# Function to save file in Uploads folder
async def save_file(file: UploadFile):

    # Validate extentions of file
    validate_extentions(file.filename)

    # Assign unique name to file
    file.filename = generate_unique_filename(file.filename)

    # Create filepath
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Return info of saved file
    return {
        "filename": file.filename,
        "path": file_path,
        "content_type": file.content_type 
    }


# Helper function for extracting text from files
def extract_text(file_path: str, ext: str) -> str:
    
    """
    Extracts text content from PDF, DOCX, or TXT files.
    Returns plain text as a single string.
    """
    text = ""

    try:
        if ext == ".pdf":
            with open(file_path, "rb") as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() or ""

        elif ext == ".docx":
            text = docx2txt.process(file_path)

        elif ext in [".txt", ".md"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

        else:
            raise ValueError(f"Unsupported file format: {ext}")

    except Exception as e:
        raise Exception(f"Failed to extract text from {file_path}: {str(e)}")

    return text



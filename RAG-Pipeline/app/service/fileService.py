# Inbuilt module imports
from fastapi.responses import JSONResponse
from starlette.status import HTTP_202_ACCEPTED, HTTP_500_INTERNAL_SERVER_ERROR
from fastapi import HTTPException, UploadFile

# Custom module imports 
from app.util.fileUtils import save_file
from app.util.ragUtils import process_chat_document


# File Upload
async def upload_file_service(file: UploadFile):

    try:

        # Upload file in local storage
        result = await save_file(file=file)

        # Extract filepath & filename and send back
        filepath = result["path"]
        filename = result["filename"]

        # Call embedding function to create chunks or doc and save embeddings in vectorDB
        ragOutput = process_chat_document(file_path=filepath, filename=filename)

        # Return response
        return JSONResponse(
            status_code=HTTP_202_ACCEPTED,
            content={
                "message": "Context uploaded succesfully !",
                "chunk_len": ragOutput["chunk_len"],
                "success": True,
                "unique_file_name": filename
            }
        )

    # Handle exceptions 
    except HTTPException:
        raise

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong !"
        )


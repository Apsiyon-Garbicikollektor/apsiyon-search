import os
import uvicorn
import fastapi
from dotenv import load_dotenv
from fastapi import UploadFile, File, Depends

from services import SearchService
from utils import convert_bytes_to_dataframe

if os.getenv("ENVIRONMENT", "local") == "local":
    load_dotenv(f"{os.getcwd()}/.env.local")
else:
    load_dotenv(f"{os.getcwd()}/.env.docker")

app = fastapi.FastAPI()


@app.post("/upload-data")
async def upload_data(
    file: UploadFile = File(...), search_service: SearchService = Depends(SearchService)
):
    content = await file.read()
    df = convert_bytes_to_dataframe(content=content, content_type=file.content_type)
    search_service.upload_data(df=df)
    await file.close()


@app.post("/search")
def search(search_service: SearchService = Depends(SearchService)):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

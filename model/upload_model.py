from pydantic import BaseModel
from fastapi import UploadFile, File

class Upload(BaseModel):
    productId: str
    pathImg: bytes
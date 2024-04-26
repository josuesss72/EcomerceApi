from fastapi import APIRouter
from controllers.upload_controller import uploadImageProduct
from fastapi import File, UploadFile, Form

upload = APIRouter()

@upload.post("/api/upload/image", tags=['upload'])
async def uploadDriveImageRoute(
    productId: str = Form(None),
    pathImg: UploadFile = File(...),
):
    return await uploadImageProduct(productId, pathImg)
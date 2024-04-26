from fastapi import UploadFile
from model.upload_model import Upload
from config.db import createDocument
from bson import Binary
from schema.upload_schema import upload_Entity
import base64

async def uploadImageProduct(
    productId: str,
    pathImg: UploadFile,
):
    try:
        file = await pathImg.read()
        binary_data = Binary(file)
        img_base64 = base64.b64encode(binary_data)

        upload = createDocument('upload', dict(Upload(productId=productId, pathImg=img_base64)))
        return { 'upload': upload_Entity(upload) }
    except Exception as e:
        print('Error =>', e)
        return { 'Error': 'fail' }
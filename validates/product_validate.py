from bson import ObjectId
from config.db import collection_product
from interfaces.db_interface import TRequestDocument
from validates.validate import TValidate


def validateProductExistsById(id: str) -> TValidate:
    objId = ObjectId(id)
    product: TRequestDocument = collection_product.find_one({"_id": objId})

    if product:
        return product
    return False

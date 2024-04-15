from datetime import datetime
from bson import ObjectId
from starlette.responses import JSONResponse
from model.product_model import Product
from config.db import (
    createDocument,
    deleteDocument,
    getDocuments,
    updateDocument,
)
from validates.product_validate import validateProductExistsById
from schema.product_schema import product_Entity, products_Entities
from schema.response_schema import responsesHttp


# __PRODUCT_CONTROLLER__


def createProduct(data: Product) -> JSONResponse:
    newData = dict(data)
    del newData["id"]

    product = createDocument("product", newData)
    return responsesHttp(product_Entity(product)).HTTP_201


def getAllProducts() -> JSONResponse:
    products = getDocuments("product")
    return responsesHttp(products_Entities(products)).HTTP_200


def updateProduct(data: Product, id: str) -> JSONResponse:
    newData = dict(data)
    newData["update_at"] = str(datetime.now)

    existProduct = validateProductExistsById(id)
    if existProduct == False:
        return responsesHttp("product").HTTP_404

    objId = ObjectId(id)
    productUpdated = updateDocument("product", newData, {"_id": objId})
    return responsesHttp(product_Entity(productUpdated)).HTTP_200


def getProduct(id) -> JSONResponse:
    product = validateProductExistsById(id)

    if product == False:
        return responsesHttp("product").HTTP_404

    return responsesHttp(product_Entity(product)).HTTP_200


def deleteProduct(id) -> JSONResponse:
    existProduct = validateProductExistsById(id)

    if existProduct == False:
        return responsesHttp("product").HTTP_404

    objId = ObjectId(id)
    product = deleteDocument("product", {"_id": objId})
    return responsesHttp(product_Entity(product)).HTTP_200

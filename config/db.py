# CREAR CONECCION CON MOMGODB
from config.config import settings
from pymongo import MongoClient
from interfaces.db_interface import TRequestDocument, TRequestDocumentAll
from typing import Dict, Any

conn = MongoClient(settings.MONGODB_DATABASE_URL)

db = conn[f"{settings.MONGODB_DATABASE_NAME}"]
collection_user = db["user"]
collection_product = db["product"]


def getDocuments(collection: str) -> TRequestDocumentAll:
    fetch: TRequestDocumentAll = db[collection].find()
    return fetch


def getDocument(collection: str, filter: Dict[str, Any]) -> TRequestDocument:
    fetch: TRequestDocument = db[collection].find_one(filter)
    return fetch


def updateDocument(
    collection: str, data: Dict[str, Any], filter: Dict[str, Any]
) -> TRequestDocument:
    db[collection].find_one_and_update(filter, {"$set": dict(data)})
    return getDocument(collection, filter)


def createDocument(collection: str, data: Dict[str, Any]) -> TRequestDocument:
    objId = db[collection].insert_one(data).inserted_id
    return getDocument(collection, {"_id": objId})


def deleteDocument(collection: str, filter: Dict[str, Any]) -> TRequestDocument:
    fetch: TRequestDocument = db[collection].find_one_and_delete(filter)
    return fetch

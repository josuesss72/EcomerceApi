from starlette.status import *
from config.db import createDocument, getDocuments, updateDocument
from fastapi.responses import JSONResponse
from schema.user_schema import user_Entity, users_Entities
from validates.user_validate import (
    validateUserExistById,
    validateUserExistByEmail,
)
from utils.bcrypt import getPasswordHash
from datetime import datetime
from schema.response_schema import responsesHttp
from model.user_model import User, UserUpdate
from bson import ObjectId


def getAllUser() -> JSONResponse:
    users = getDocuments("user")
    return responsesHttp(users_Entities(users)).HTTP_200


def getOneUser(id: str) -> JSONResponse:
    user = validateUserExistById(id=id)
    if user:
        return responsesHttp(user_Entity(user)).HTTP_200
    return responsesHttp("user").HTTP_404


def createUser(data: User) -> JSONResponse:
    new_user = dict(data)
    del new_user["confirm_password"]

    userIsCreated = validateUserExistByEmail(new_user["email"])
    if userIsCreated:
        return responsesHttp("user").HTTP_409

    # ENCRIPTAMOS PASSWORD
    new_user["password"] = getPasswordHash(new_user["password"])
    # INSERTAMOS THE DATE
    new_user["created_at"] = str(datetime.now())
    # CREAMOS USER
    user = createDocument("user", new_user)
    return responsesHttp(user_Entity(user)).HTTP_201


def updateUser(id: str, data: UserUpdate) -> JSONResponse:
    newData = dict(data)
    newData["update_at"] = str(datetime.now())

    user = validateUserExistById(id)
    if user:
        objId = ObjectId(id)
        user = updateDocument("user", newData, {"_id": objId})
        return responsesHttp(user_Entity(user)).HTTP_200

    return responsesHttp("user").HTTP_409

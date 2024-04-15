from config.db import getDocument
from bson import ObjectId


def validateUserExistById(id: str):
    objId = ObjectId(id)
    user = getDocument("user", {"_id": objId})
    if not user:
        return False
    return user


def validateUserExistByEmail(email: str):
    user = getDocument("user", {"email": email})
    if user:
        return user
    return False

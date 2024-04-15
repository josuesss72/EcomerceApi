from typing import Dict, Any, Union
from datetime import timedelta, datetime
from jose import jwt, JWTError
from config.config import Settings
from passlib.context import CryptContext
from fastapi import HTTPException, Request
from validates.user_validate import validateUserExistByEmail
from schema.user_schema import user_Entity
from config.db import getDocument



class Auth():

    def __init__(self):
        self.pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.credentialsException = HTTPException(
            status_code=401,
            detail="not authorized",
            headers={"WWW-Authenticate": "Bearer"},
        )
        self.tokenException = HTTPException(
            status_code=401,
            detail="Token invalid",
        )


    def createToken(self, data: Dict[str, Any], timeExpires: Union[timedelta, None] = None):
        dataCopy = data.copy()
        if timeExpires is None:
            expires = datetime.utcnow() + timedelta(minutes=15)
        else:
            expires = datetime.utcnow() + timeExpires

        dataCopy.update({"exp": expires})

        if "sub" in dataCopy:
            dataCopy["sub"] = str(dataCopy["sub"])

        tokenJwt = jwt.encode(
            dataCopy, key=str(Settings.SECRET_KEY), algorithm=str(Settings.ALGORITHM)
        )
        return tokenJwt


    def verifyPassword(self, plane_password: str, hashed_password: str) -> bool:
        return self.pwdContext.verify(plane_password, hashed_password)


    def authentication(self, username: str, password: str):
        user = validateUserExistByEmail(username)
        if not user:
            raise self.credentialsException 
        if not self.verifyPassword(password, user_Entity(user).get("password")):
            raise self.credentialsException 
        return user


    def getCurrentUser(self, request: Request):
        authorization: Union[str, None] = request.headers.get("authorization")
        if authorization is None:
            raise self.credentialsException

        token = authorization.split(" ")[1]
        try:
            payload = jwt.decode(token, str(Settings.SECRET_KEY), str(Settings.ALGORITHM))
        except JWTError:
            raise self.tokenException

        username: Union[str, None] = payload.get("sub")
        if username is None:
            raise self.credentialsException
        user = getDocument("user", {"email": username})
        if user is None:
            raise self.credentialsException
        return user

auth = Auth()

from model.login_model import Login
from model.user_model import User, UserUpdate
from fastapi import APIRouter, Depends, Request
from controllers.authentication_controller import login
from controllers.user_controller import getOneUser, createUser, getAllUser, updateUser
from model.auth_model import auth


# NOS PERMITE MODULARIAZAR NUESTRAS RUTAS
user = APIRouter()


@user.get("/api/user", tags=["users"])
async def root(user=Depends(auth.getCurrentUser)):
    return getAllUser()


@user.post("/api/user", tags=["users"])
async def newUserRoute(user: User):
    return createUser(user)


@user.get("/api/user/{id}", tags=["users"])
async def getUserRoute(id: str, userLoged=Depends(auth.getCurrentUser)):
    return getOneUser(id)


@user.put("/api/user/update/me", tags=["users"])
async def updateUserRoute(data: UserUpdate, userLoged=Depends(auth.getCurrentUser)):
    return updateUser(id=str(userLoged.get("_id")), data=data)


@user.post("/api/user/login", tags=["users"])
async def loginRoute(formData: Login):
    return login(formData)

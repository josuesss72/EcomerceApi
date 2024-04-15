from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


cart = APIRouter()

@cart.get("/api/cart", tags=["cart"])
async def getCartRouter():
    pass

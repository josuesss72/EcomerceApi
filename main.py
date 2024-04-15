from fastapi import FastAPI
from router.user_router import user
from router.product_router import product
from router.cart_router import cart

app = FastAPI()

app.include_router(user)
app.include_router(product)
app.include_router(cart)

from fastapi import FastAPI
from router.user_router import user
from router.product_router import product
from router.cart_router import cart

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Para resolver el problema de CORS (Cross-Origin Resource Sharing)
# para permitir solicitudes
origins = [
    "http://localhost:5173"
]

# ADD MIDDLEWARES
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(product)
app.include_router(cart)

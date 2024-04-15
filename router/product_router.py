from fastapi import APIRouter
from model.product_model import Product
from controllers.product_controller import (
    createProduct,
    getAllProducts,
    updateProduct,
    getProduct,
    deleteProduct,
)

product = APIRouter()


@product.get("/api/product", tags=["product"])
async def allProductRoute():
    return getAllProducts()


@product.post("/api/product", tags=["product"])
async def newProductRoute(product: Product):
    return createProduct(product)


@product.put("/api/product/{id}", tags=["product"])
async def updateProductRoute(product: Product, id: str):
    return updateProduct(product, id)


@product.get("/api/product/{id}", tags=["product"])
async def getProductRoute(id: str):
    return getProduct(id)


@product.delete("/api/product/{id}", tags=["product"])
async def deleteProductRoute(id: str):
    return deleteProduct(id)

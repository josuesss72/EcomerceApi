from typing import Any, Optional, Callable
from pydantic import BaseModel, root_validator


class Product(BaseModel):
    id: Optional[str]
    name: str
    stock: int
    category_id: str = "not category"
    unit_cost: int
    price: int

    @root_validator()
    def root(cls, values):
        unit_cost = values.get("unit_cost")
        price = values.get("price")
        stock = values.get("stock")

        positive: Callable[[int], bool] = lambda x: x < 0
        numeric: Callable[[Any], bool] = lambda x: type(x) is not int

        if numeric(stock) or positive(stock):
            raise ValueError("The stock must numerical and positive")

        if numeric(price) or positive(price):
            raise ValueError("The price must numerical and positive")

        if numeric(unit_cost) or positive(unit_cost):
            raise ValueError("The unit_cost must numerical and positive")
        return values

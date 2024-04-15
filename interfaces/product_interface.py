from typing import TypedDict, Optional


class IProduct(TypedDict):
    id: Optional[str]
    name: str
    stock: int
    category_id: str
    unit_cost: str
    price: int

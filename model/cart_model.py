from pydantic import BaseModel
from typing import Optional


class Cart(BaseModel):
    id: Optional[str]
    products: list[str]
    user_id:str

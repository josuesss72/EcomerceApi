from typing import Optional, TypedDict
from datetime import datetime


class IUser(TypedDict):
    id: str
    name: str
    email: str
    password: str
    created_at: datetime
    update_at: Optional[datetime]

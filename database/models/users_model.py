
### User model ###

from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    _id: Optional[str]
    name: str
    password: str
    is_active: bool = True


# Short vertion
class UserShort(BaseModel):
    _id: str
    name: str

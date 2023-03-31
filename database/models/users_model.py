
### User model ###

from pydantic import BaseModel, Field
# from typing import Optional
from bson import ObjectId


class User(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    password: str
    is_active: bool = True


# Short vertion
class UserShort(BaseModel):
    id: str
    name: str

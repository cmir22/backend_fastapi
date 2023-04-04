
### User model ###

from pydantic import BaseModel, Field
# from typing import Optional
from bson import ObjectId
from datetime import datetime


# Long vertion
class User(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    password: str
    is_active: bool = True
    join_date = datetime.now().time()


# Short vertion
class UserShort(BaseModel):
    id: str
    name: str

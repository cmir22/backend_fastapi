
### User model ###

from pydantic import BaseModel, Field, EmailStr, SecretStr
# from typing import Optional
from bson import ObjectId
from datetime import datetime


# Long vertion
class User(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    email: EmailStr
    password: SecretStr
    is_active: bool = True
    join_date = datetime.now().today()


# Short vertion
class UserShort(BaseModel):
    id: str
    name: str

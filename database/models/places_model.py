
### User model ###

from pydantic import BaseModel, Field, EmailStr
# from typing import Optional
from bson import ObjectId
from datetime import datetime


# Long vertion
class Place(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    email: EmailStr
    password: str
    is_active: bool = True
    join_date = datetime.now().today()

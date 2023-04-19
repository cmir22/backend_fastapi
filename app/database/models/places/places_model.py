
### User model ###

from pydantic import BaseModel, Field, EmailStr
# from typing import Optional
from bson import ObjectId
from datetime import datetime


# Long vertion
class Place(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    phone: str
    email: EmailStr
    web_site: str
    image: str
    is_active: bool = True
    last_edit_date = datetime.now().today()


class UpdatePlace(BaseModel):
    name: str
    phone: str
    email: EmailStr
    web_site: str
    image: str
    last_edit_date = datetime.now().today()

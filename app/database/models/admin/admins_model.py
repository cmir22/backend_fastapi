
### User model ###

from pydantic import BaseModel, Field, EmailStr
# from typing import Optional
from bson import ObjectId
from datetime import datetime


# Long vertion
class Admin(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    email: EmailStr
    phone: str
    password: str
    is_active: bool = True
    join_date = datetime.now().today()


# Short vertion
class UserShort(BaseModel):
    id: str
    id_place: str
    name: str
    email: EmailStr


# Short vertion
class AdminLogin(BaseModel):
    email: EmailStr
    password: str


# Short vertion
class AdminLogged(BaseModel):
    _id: str
    id_place: str
    email: EmailStr
    name: str
    phone: str


# Admin details
class AdminDetails(BaseModel):
    _id: ObjectId
    id_place: str
    email: EmailStr
    name: str
    is_active: bool
    join_date: datetime

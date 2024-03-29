
### User model ###

from pydantic import BaseModel, Field, EmailStr
# from typing import Optional
from bson import ObjectId
from datetime import datetime


# Long vertion
class User(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    email: EmailStr
    password: str
    is_active: bool = True
    join_date = datetime.now().today()


# Short vertion
class UserShort(BaseModel):
    id: str
    name: str
    email: EmailStr


# Short vertion
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Short vertion
class UserLogged(BaseModel):
    _id: str
    email: EmailStr
    name: str


# User details
class UserDetails(BaseModel):
    _id: ObjectId
    email: EmailStr
    name: str
    is_active: bool
    join_date: datetime

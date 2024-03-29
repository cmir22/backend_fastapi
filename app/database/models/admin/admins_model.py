
### User model ###

from pydantic import BaseModel, Field, EmailStr
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
class AdminShort(BaseModel):
    id: str
    id_business: str
    name: str
    email: EmailStr


# Short vertion
class AdminLogin(BaseModel):
    email: EmailStr
    password: str


# Short vertion
class AdminLogged(BaseModel):
    _id: str
    id_business: str
    email: EmailStr
    name: str
    phone: str


# Admin details
class AdminDetails(BaseModel):
    _id: ObjectId
    id_business: str
    email: EmailStr
    name: str
    is_active: bool
    join_date: datetime


# Set select
class SelectAdminDetails(BaseModel):
    _id = Field(alias='_id', default=False)
    id_business = False
    join_date = False
    password = False
    is_active = False


# Update admin details
class UpdateAdminDetails(BaseModel):
    _id: ObjectId = Field(alias='_id')
    email: EmailStr
    name: str
    phone: str

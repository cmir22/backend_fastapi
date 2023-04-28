
### Category model ###

from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime


# Long vertion
class Category(BaseModel):
    _id: ObjectId = Field(alias='_id')
    name: str
    description: str
    is_active = True
    last_update = datetime.now().today()
    created_date = datetime.now().today()


# Select vertion
class SelectCategory(BaseModel):
    is_active = False
    last_update = False
    created_date = False
    id_place = False


# Update vertion
class UpdateCategory(BaseModel):
    name: str
    description: str

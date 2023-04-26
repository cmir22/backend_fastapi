
### Location model ###

from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime


# Long vertion
class Location(BaseModel):
    _id: ObjectId = Field(alias='_id')
    city: str
    state: str
    address: str
    country: str
    lat: str
    lng: str
    last_update = datetime.now().today()


class LocationSelect(BaseModel):
    # _id = False
    last_update = False
    id_place = False

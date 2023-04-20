
### User model ###

from pydantic import BaseModel, Field
# from typing import Optional
from bson import ObjectId
from datetime import datetime
from datetime import time


# Long vertion
class PlaceSchedule(BaseModel):
    _id: ObjectId = Field(alias='_id')
    _id_place: str
    day: str
    open_time: time
    close_time: time
    last_edit_date = datetime.now().today()

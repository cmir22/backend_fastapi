
### User model ###

from pydantic import BaseModel  # , Field
# from typing import Optional
# from bson import ObjectId
# from datetime import datetime
from datetime import time


class Schedule(BaseModel):
    _id_place: str
    day_number: int
    open_time: time
    close_time: time


# Long vertion
class PlaceSchedule(BaseModel):
    days: list[Schedule]
    # _id: ObjectId = Field(alias='_id')
    # _id_place: str
    # day_number: int
    # open_time: time
    # close_time: time
    # last_edit_date = datetime.now().today()


### Places schedule model ###

from pydantic import BaseModel
from datetime import datetime


class Schedule(BaseModel):
    day_number: int
    open_time: str
    close_time: str


class ScheduleDay(BaseModel):
    id_place: str
    day_number: int
    open_time: datetime
    close_time: datetime


class PlaceSchedule(BaseModel):
    days: list[Schedule]


### Places schedule model ###

from pydantic import BaseModel
from datetime import datetime, time


class Schedule(BaseModel):
    day_number: int
    open_time: str
    close_time: str


class ScheduleDay(BaseModel):
    id_place: str
    day_number: int
    open_time: time
    close_time: time


class PlaceSchedule(BaseModel):
    days: list[Schedule]


### Places schedule model ###

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Schedule(BaseModel):
    day_number: int
    is_open: bool
    open_time: Optional[str] = None
    close_time: Optional[str] = None


class ScheduleDay(BaseModel):
    id_place: str
    day_number: int
    is_open: bool
    open_time: Optional[datetime] = None
    close_time: Optional[datetime] = None
    today_open: Optional[bool] = None


class PlaceSchedule(BaseModel):
    days: list[Schedule]

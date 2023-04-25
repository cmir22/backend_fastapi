
### Place schedule  ###

from fastapi import APIRouter, Header
from database.collections import places_schedule_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.places.places_schedule_model import PlaceSchedule, ScheduleDay
from helpers.responses import success_message
from security.jwt_decode import decode_token
# from helpers.dates.week_days import weekdays
from datetime import datetime, time

# Router
router = APIRouter(prefix="/places/schedule", tags=["Places Schedule"])

# Collection
places_schedule_collection = database[places_schedule_collection]


@router.post("/create")
async def create_place_info(schedule: PlaceSchedule, Authorization: str = Header(None)):
    try:
        id_place = decode_token(Authorization)["id_place"]
        schedule_dict = dict(schedule)["days"]
        new_list = []

        for day in schedule_dict:
            day = dict(day)
            day["id_place"] = str(id_place)
            day['open_time'] = convert_hours(day['open_time'])
            day['close_time'] = convert_hours(day['close_time'])
            schedule_day = dict(ScheduleDay(**day))
            new_list.append(schedule_day)

        print(new_list)

        document = places_schedule_collection.insert_many(new_list)

    except Exception as exs:
        raise error_insert(exs)
    return success_message(document)


def convert_hours(my_time: str):
    time_format = "%H:%M %p"
    formated = datetime.strptime(my_time, time_format)
    return formated

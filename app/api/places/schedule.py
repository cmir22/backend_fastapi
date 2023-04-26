
### Place schedule  ###

from fastapi import APIRouter, Header
import pymongo
from database.collections import places_schedule_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.places.places_schedule_model import PlaceSchedule, ScheduleDay
from helpers.responses import success_message, format_respose
from helpers.dates.time_hours import convert_hours
from security.headers import header_id_place

# Router
router = APIRouter(prefix="/places/schedule", tags=["Places Schedule"])

# Collection
places_schedule_collection = database[places_schedule_collection]


@router.post("/create")
async def create_place_schedule(schedule: PlaceSchedule, Authorization=Header(None)):
    response = {}

    try:
        id_place = header_id_place(Authorization)
        schedule_dict: dict = dict(schedule)["days"]
        new_list = []

        for day in schedule_dict:
            day = dict(day)
            day["id_place"] = id_place
            day['open_time'] = convert_hours(day['open_time'])
            day['close_time'] = convert_hours(day['close_time'])
            schedule_day = ScheduleDay(**day)
            new_list.append(dict(schedule_day))

        # Insert into database
        places_schedule_collection.insert_many(new_list)
        response = success_message(id_place)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.put("/update")
async def update_place_schedule(schedule: PlaceSchedule, Authorization=Header(None)):
    response = {}

    try:
        id_place = header_id_place(Authorization)
        schedule_dict: dict = dict(schedule)["days"]

        for day in schedule_dict:
            day = dict(day)
            day["id_place"] = id_place
            day['open_time'] = convert_hours(day['open_time'])
            day['close_time'] = convert_hours(day['close_time'])
            schedule_day = dict(ScheduleDay(**day))
            query = {"id_place": id_place, "day_number": day['day_number']}
            update = {"$set": schedule_day}
            places_schedule_collection.update_one(query, update)

        response = success_message(id_place)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.get("/get/{id_place}")
async def get_place_schedule(id_place: str):
    response = {}

    try:
        select = {"_id": False}
        query = {"id_place": id_place}
        document = places_schedule_collection.find(query, select)
        document = document.sort("day_number", pymongo.ASCENDING)
        response = format_respose(list(document))

    except Exception as exs:
        raise error_insert(exs)
    return response

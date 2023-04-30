
### Business schedule  ###

from fastapi import APIRouter, Header
import pymongo
from database.collections import business_schedule_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.business.business_schedule_model import BusinessSchedule
from helpers.responses import success_message, format_respose
from helpers.dates.time_hours import convert_hours
from security.headers import header_id_business

# Router
router = APIRouter(prefix="/business/schedule", tags=["Business Schedule"])

# Collection
BUSINESS_SCHEDULE_COLLECTION = database[business_schedule_collection]


@router.post("/create")
async def create_business_schedule(schedule: BusinessSchedule, Authorization=Header(None)):
    response = {}

    try:
        id_business = header_id_business(Authorization)
        schedule_dict: dict = dict(schedule)["days"]
        new_list = []

        for day in schedule_dict:
            day = dict(day)
            day["id_business"] = id_business
            day['open_time'] = convert_hours(day['open_time'])
            day['close_time'] = convert_hours(day['close_time'])
            schedule_day = BusinessSchedule(**day)
            new_list.append(dict(schedule_day))

        # Insert into database
        BUSINESS_SCHEDULE_COLLECTION.insert_many(new_list)
        response = success_message(id_business)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.put("/update")
async def update_business_schedule(schedule: BusinessSchedule, Authorization=Header(None)):
    response = {}

    try:
        id_business = header_id_business(Authorization)
        schedule_dict: dict = dict(schedule)["days"]

        for day in schedule_dict:
            day = dict(day)
            day["id_business"] = id_business
            day['open_time'] = convert_hours(day['open_time'])
            day['close_time'] = convert_hours(day['close_time'])
            schedule_day = dict(BusinessSchedule(**day))

            WHERE = {"id_business": id_business,
                     "day_number": day['day_number']}
            UPDATE = {"$set": schedule_day}

            BUSINESS_SCHEDULE_COLLECTION.update_one(WHERE, UPDATE)

        response = success_message(id_business)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.get("/get/{id_business}")
async def get_business_schedule(id_business: str):
    response = {}

    try:
        SELECT = {"_id": False}
        WHERE = {"id_business": id_business}

        document = BUSINESS_SCHEDULE_COLLECTION.find(WHERE, SELECT)
        document = document.sort("day_number", pymongo.ASCENDING)

        response = format_respose(document)

    except Exception as exs:
        raise error_insert(exs)
    return response

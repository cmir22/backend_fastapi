
### Place schedule  ###

from fastapi import APIRouter, Header
from database.collections import places_schedule_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.places.places_schedule_model import PlaceSchedule
from helpers.responses import success_message
from security.jwt_decode import decode_token

# Router
router = APIRouter(prefix="/places/schedule", tags=["Places Schedule"])

# Collection
places_schedule_collection = database[places_schedule_collection]


@router.post("/create")
async def create_place_info(schedule: PlaceSchedule, Authorization: str = Header(None)):
    days = [0, 2, 3, 4, 5, 6, 7, 8]
    try:
        id_place = decode_token(Authorization)["id_place"]
        schedule_dict = dict(schedule)["days"]
        schedule_list = []

        for sch in schedule_dict:
            schedule_list[str(sch["day_number"])] = sch

        # print(sche)

        # document = places_schedule_collection.insert_many(schedule_dict)
    except Exception as exs:
        raise error_insert(exs)

    return {}
    # return success_message(document.inserted_id)

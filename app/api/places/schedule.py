
### Place schedule  ###

from fastapi import APIRouter, Header
from database.collections import places_schedule_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.places.places_model import Place
from helpers.responses import success_message
from security.jwt_decode import decode_token

# Router
router = APIRouter(prefix="/places/schedule", tags=["Places Schedule"])

# Collection
places_schedule_collection = database[places_schedule_collection]


@router.post("/create")
async def create_place_info(schedule: Place, Authorization: str = Header(None)):
    print(decode_token(Authorization))
    # try:
    #     schedule_dict = dict(schedule)
    #     document = places_schedule_collection.insert_one(schedule_dict)
    # except Exception as exs:
    #     raise error_insert(exs)

    # return success_message(document.inserted_id)
    return {}

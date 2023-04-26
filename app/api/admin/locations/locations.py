
### Place Information  ###

from fastapi import APIRouter, Header
from database.collections import locations_collection
from database.db import database
from helpers.exeptions import error_insert
from helpers.responses import success_message
from database.models.admin.locations.locations_model import Location
from security.headers import header_id_place

# Router
router = APIRouter(prefix="/locations", tags=["Locations"])

# Collection
locations_collection = database[locations_collection]


@router.post("/create")
async def create_place(place: Location, Authorization=Header(None)):
    response: str
    place = dict(place)

    try:
        place["id_place"] = header_id_place(Authorization)
        document = locations_collection.insert_one(place)
        response = success_message(document.inserted_id)

    except Exception as exs:
        raise error_insert(exs)
    return response

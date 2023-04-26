
### Location  ###

from fastapi import APIRouter, Header
from database.collections import locations_collection
from database.db import database
from helpers.exeptions import error_insert
from helpers.responses import success_message, format_respose
from database.models.admin.locations.locations_model import Location
from security.headers import header_id_place
# from bson.objectid import ObjectId

# Router
router = APIRouter(prefix="/locations", tags=["Locations"])

# Collection
LOCATIONS_COLLECTION = database[locations_collection]


@router.post("/create")
async def create_place_location(place: Location, Authorization=Header(None)):
    response: str
    place = dict(place)

    try:
        place["id_place"] = header_id_place(Authorization)
        document = LOCATIONS_COLLECTION.insert_one(place)
        response = success_message(document.inserted_id)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.get("/get")
async def get_place_location(Authorization=Header(None)):
    response = {}

    try:
        SELECT = {"_id": False, "last_update": False, "id_place": False}
        WHERE = {"id_place": header_id_place(Authorization, "id_place")}

        document = LOCATIONS_COLLECTION.find_one(WHERE, SELECT)

        response = format_respose([dict(document)])

    except Exception as exs:
        raise error_insert(exs)
    return response

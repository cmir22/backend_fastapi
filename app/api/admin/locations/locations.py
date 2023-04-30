
### Location  ###

from fastapi import APIRouter, Header
from database.collections import locations_collection
from database.db import database
from helpers.exeptions import error_insert
from helpers.responses import success_message, format_respose
from database.models.admin.locations.locations_model import Location
from security.headers import header_id_business

# Router
router = APIRouter(prefix="/locations", tags=["Locations"])

# Collection
LOCATIONS_COLLECTION = database[locations_collection]


@router.post("/create")
async def create_business_location(business: Location, Authorization=Header(None)):
    response = {}
    business = dict(business)

    try:
        business["id_business"] = header_id_business(Authorization)
        document = LOCATIONS_COLLECTION.insert_one(business)
        response = success_message(document.inserted_id)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.get("/get")
async def get_business_location(Authorization=Header(None)):
    response = {}

    try:
        SELECT = {"_id": False, "last_update": False, "id_business": False}
        WHERE = {"id_business": header_id_business(
            Authorization, "id_business")}

        document = LOCATIONS_COLLECTION.find_one(WHERE, SELECT)

        response = format_respose([dict(document)])

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.put("/update")
async def get_business_location(location: Location, Authorization=Header(None)):
    response = {}

    try:
        WHERE = {"id_business": header_id_business(
            Authorization, "id_business")}
        UPDATE = {"$set": dict(location)}

        LOCATIONS_COLLECTION.find_one_and_update(WHERE, UPDATE)
        response = success_message(WHERE["id_business"])

    except Exception as exs:
        raise error_insert(exs)
    return response


### Place Information  ###

from fastapi import APIRouter, Header
from database.collections import locations_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.places.places_model import Place, UpdatePlace
from helpers.responses import success_message, not_found_message, format_respose
from bson.objectid import ObjectId
from database.models.admin.locations.locations_model import Location
from security.headers import header_id_place

# Router
router = APIRouter(prefix="/locations", tags=["Locations"])

# Collection
locations_collection = database[locations_collection]


@router.post("/create")
async def create_place(place: Location, Authorization=Header(None)):
    id_place = header_id_place(Authorization, "_id")

    print(place)

    return {}

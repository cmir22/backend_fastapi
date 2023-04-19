
### Place Information  ###

from fastapi import APIRouter
from database.collections import places_collection
from database.db import database
from helpers.exeptions import error_insert, validate_schema
from database.models.places.places_model import Place
from database.schemas.places.places_schema import place_schema
# Router
router = APIRouter(prefix="/places", tags=["Places"])

# Collection
places_collection = database[places_collection]


@router.post("/create")
async def create_place_info(place: Place):
    validate_schema(place, place_schema)
    try:
        place_dict = dict(place)
        result = places_collection.insert_one(place_dict)
    except Exception as exs:
        raise error_insert(exs)
    return {}

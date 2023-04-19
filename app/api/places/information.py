
### Place Information  ###

from fastapi import APIRouter
from database.collections import admins_collection
from database.db import database
from helpers.exeptions import validate_schema
from database.models.places.places_model import Place
from database.schemas.places.places_schema import place_schema
# Router
router = APIRouter(prefix="/places/information", tags=["Places"])

# Collection
collection = database[admins_collection]


@router.post("/create")
async def create_place_info(place: Place):
    validate_schema(place, place_schema)

    print(place)
    return {}

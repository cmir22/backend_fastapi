
### Place Information  ###

from fastapi import APIRouter
from database.collections import places_collection
from database.db import database
from helpers.exeptions import error_insert, validate_schema
from database.models.places.places_model import Place
from database.schemas.places.places_schema import place_schema
from helpers.responses import success_message, not_found_message, format_respose
from bson.objectid import ObjectId

# Router
router = APIRouter(prefix="/places", tags=["Places"])

# Collection
places_collection = database[places_collection]


@router.post("/create")
async def create_place_info(place: Place):
    validate_schema(place, place_schema)

    try:
        place_dict = dict(place)
        document = places_collection.insert_one(place_dict)
    except Exception as exs:
        raise error_insert(exs)

    return success_message(document.inserted_id)


@router.get("/{_id}")
async def get_place_info(_id: str):
    document: Place = {}

    try:
        query = {"_id": ObjectId(_id)}
        document = places_collection.find_one(query)
        document = format_respose(Place(**document))

    except Exception as exs:
        raise not_found_message()

    return document


@router.delete("delete/{_id}")
async def delete_place(_id: str):
    document = {}

    try:
        query = {"_id": ObjectId(_id)}
        deleted_count = places_collection.delete_one(query).deleted_count

        if deleted_count == 1:
            document = _id
        else:
            not_found_message()

    except Exception as exs:
        raise not_found_message()

    return success_message(document)

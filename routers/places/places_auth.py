
### User  ###

from fastapi import APIRouter
from database.collections import places_collection
from database.db import database

# Router
router = APIRouter(prefix="/places", tags=["places"])

# Collection
collection = database[places_collection]


@router.post("/create")
async def create_user(user):
    return {}

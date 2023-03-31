
### User  ###

from fastapi import APIRouter
from database.collections import users_collection
from database.db import database
from database.models.users_model import User, UserShort
from database.schemas.users_schema import user_schema
from helpers.exeptions import error_insert, validate_schema

# Router
router = APIRouter(prefix="/users", tags=["users"])

# Collection
collection = database[users_collection]


@router.post("/create")
async def create_user(user: User):
    validate_schema(user, user_schema)
    try:
        user_dict = dict(user)
        result = collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)
    except Exception as exs:
        raise error_insert(exs)
    return UserShort(**user_dict)

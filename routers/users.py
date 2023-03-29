
### User  ###

from fastapi import APIRouter, HTTPException, status
from database.collections import users_collection
from database.db import database
from database.models.users_model import User, UserShort
import jsonschema
from database.schemas import users_schema
from helpers.exeptions import msg_exeption


# Router
router = APIRouter(prefix="/users", tags=["users"])


# Collection
collection = database[users_collection]


@router.post("/create")
async def create_user(user: User):
    try:
        jsonschema.validate(user, users_schema)
        user_dict = dict(user)
        result = collection.insert_one(user_dict)
        user_dict["_id"] = str(result.inserted_id)
    except Exception as exs:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=msg_exeption("Error to create user", exs))
    return UserShort(**user_dict)

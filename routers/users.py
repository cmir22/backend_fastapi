# Users
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status
from database.collections import users_collection
from database.db import database


# Router
router = APIRouter(prefix="/users", tags=["users"])


# Collection
collection = database[users_collection]


class User(BaseModel):
    name: str
    password: str
    is_active: bool = True


@router.post("/create")
async def create_user(user: User):
    try:
        result = collection.insert_one(user)
        userss = {"id": str(result.inserted_id)}.update(user)
        print(userss)
        # user["_id"] = str(result.inserted_id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Error to create user")
    return userss

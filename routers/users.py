from fastapi import APIRouter
from database.collections import users
from database.db import db

# Router
router = APIRouter(prefix="/users", tags=["userdb"])

# Collection
collection = db[users]


@router.post("/create")
async def root():
    user = {
        "userr": "wdw"
    }
    result = collection.insert_one(user)
    user["_id"]: dict = str(result.inserted_id)
    return user

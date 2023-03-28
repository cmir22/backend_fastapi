from fastapi import APIRouter
from pymongo import MongoClient

# Router
router = APIRouter(prefix="/users", tags=["userdb"])

client = MongoClient('mongodb://localhost:27017/')

db = client["tesign_database"]

user = {
    "username": "johndoe",
    "email": "johndoe@example.com"
}


@router.post("/create")
async def root():
    collection = db["collection_name"]
    result = collection.insert_one(user)
    return {"id": str(result)}.update(user)

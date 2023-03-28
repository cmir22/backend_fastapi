from fastapi import APIRouter
from pymongo import MongoClient

# Router
router = APIRouter(prefix="/users", tags=["userdb"])

client = MongoClient('mongodb://localhost:27017/')

db = client["tesign_database"]


@router.post("/create")
async def root():
    user = {
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    collection = db["collection_name"]
    result = collection.insert_one(user)
    simona = collection.find_one({"_id": str(result.inserted_id)})
    print(simona)
    return print(simona)

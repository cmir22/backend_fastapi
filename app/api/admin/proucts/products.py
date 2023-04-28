
### Categories ###

from fastapi import APIRouter, Header
import pymongo
from database.collections import categories_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.products.category_model import Category, SelectCategory, UpdateCategory
from security.headers import header_id_place
from helpers.responses import success_message, format_respose
from bson.objectid import ObjectId

# Router
router = APIRouter(prefix="/products/categories", tags=["Categories"])

# Collection
CATEGORIES_COLLECTION = database[categories_collection]


@router.post("/create")
async def create_category(category: Category, Authorization=Header(None)):
    response = {}
    category = dict(category)

    try:
        category["id_place"] = header_id_place(Authorization)
        document = CATEGORIES_COLLECTION.insert_one(category)

        UPDATE = {"$set": {"id_category": str(document.inserted_id)}}
        WHERE = {"_id": ObjectId(document.inserted_id)}

        CATEGORIES_COLLECTION.update_one(WHERE, UPDATE)

        response = success_message(document.inserted_id)

    except Exception as exs:
        raise error_insert(exs)
    return response

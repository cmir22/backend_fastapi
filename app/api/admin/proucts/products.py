
### Products ###

from fastapi import APIRouter, Header
from database.collections import products_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.products.category_model import Category
from security.headers import header_id_place
from helpers.responses import success_message
from bson.objectid import ObjectId

# Router
router = APIRouter(prefix="/products", tags=["Products"])

# Collection
PRODUCTS_COLLECTION = database[products_collection]


@router.post("/create")
async def create_product(product: Category, Authorization=Header(None)):
    response = {}
    product = dict(product)

    try:
        product["id_place"] = header_id_place(Authorization)
        document = PRODUCTS_COLLECTION.insert_one(product)

        UPDATE = {"$set": {"id_category": str(document.inserted_id)}}
        WHERE = {"_id": ObjectId(document.inserted_id)}

        PRODUCTS_COLLECTION.update_one(WHERE, UPDATE)

        response = success_message(document.inserted_id)

    except Exception as exs:
        raise error_insert(exs)
    return response

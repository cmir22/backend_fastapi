
### Categories  ###

from fastapi import APIRouter, Header
from database.collections import categories_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.products.category_model import Category, SelectCategory
from security.headers import header_id_place
from helpers.responses import success_message, format_respose


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
        response = success_message(document.inserted_id)

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.get("/get/{id_place}")
async def get_categories(id_place: str):
    response = {}

    # try:
    #     SELECT = dict(SelectCategory())
    #     WHERE = {"id_place": id_place}

    #     document = CATEGORIES_COLLECTION.find(WHERE, SELECT)
    #     response = format_respose(document)

    # except Exception as exs:
    #     raise error_insert(exs)
    return response

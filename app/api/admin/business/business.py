
### Business Information  ###

from fastapi import APIRouter
from database.collections import business_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.business.business_model import Business, UpdateBusiness
from helpers.responses import success_message, not_found_message, format_respose
from bson.objectid import ObjectId

# Router
router = APIRouter(prefix="/business", tags=["Business"])

# Collection
BUSINESS_COLLECTION = database[business_collection]


@router.post("/create")
async def create_business(business: Business):
    try:
        INSERT = dict(business)
        document = BUSINESS_COLLECTION.insert_one(INSERT)

    except Exception as exs:
        raise error_insert(exs)

    return success_message(document.inserted_id)


@router.get("/{_id}")
async def get_business(_id: str):
    document: Business = {}

    try:
        WHERE = {"_id": ObjectId(_id)}

        document = BUSINESS_COLLECTION.find_one(WHERE)
        document = format_respose(Business(**document))

    except Exception as exs:
        raise not_found_message()

    return document


@router.delete("/delete/{_id}")
async def delete_business(_id: str):
    document = {}

    try:
        WHERE = {"_id": ObjectId(_id)}

        deleted_count = BUSINESS_COLLECTION.delete_one(WHERE).deleted_count

        if deleted_count == 1:
            document = _id
        else:
            not_found_message()

    except Exception as exs:
        raise not_found_message()

    return success_message(document)


@router.put("/update/{_id}")
async def delete_business(business: UpdateBusiness, _id: str):
    document = {}

    try:
        UPDATE = {"$set": UpdateBusiness(**dict(business)).dict()}
        WHERE = {"_id": ObjectId(_id)}

        modified_count = BUSINESS_COLLECTION.update_one(WHERE, UPDATE)

        if modified_count.modified_count == 1:
            document = _id
        else:
            not_found_message()

    except Exception as exs:
        print(exs)
        raise not_found_message()

    return success_message(document)

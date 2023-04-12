
### Response messages ###

from fastapi import HTTPException, status
from database.db import database
from database.collections import exeption_collection


def success_message():
    response = {
        "msg": "success",
        "is_success": True
    }

    return HTTPException(status_code=status.HTTP_201_CREATED, detail=response)


def failed_message(_id: str, endpoint: str):
    # Collection
    collection = database[exeption_collection]

    response = msg(_id, endpoint)
    collection.insert_one(response)

    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=response)


def msg(_id: str, endpoint: str):
    response: dict = (
        {
            "msg": "Error to insert",
            "is_success": False,
            "user_id": _id,
            "endpoint": endpoint
        }
    )
    return response

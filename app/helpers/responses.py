
### Response messages ###

from fastapi import HTTPException, status
from database.db import database
from database.collections import exeption_collection
from database.models.response_model import ResponseModel, FormatResponseModel


def success_message(_id=None):
    response = {
        "message": "success",
        "is_success": True,
        "_id": str(_id)
    }

    return HTTPException(status_code=status.HTTP_200_OK, detail=response)


def format_respose(data={}):
    response = {
        "message": "success",
        "loaded": True,
        "is_success": True,
        "data": list(data)
    }

    return FormatResponseModel(**response)


def not_found_message():
    response = {
        "message": "record not found",
        "is_success": False,
    }

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response)


def failed_message(_id: str, endpoint: str, exeption: Exception):
    # Collection
    collection = database[exeption_collection]
    query = set_detail(_id, endpoint, exeption)
    collection.insert_one(dict(query))
    detail = {"error": True, "action": endpoint}
    headers = {"X-Error": "Error on: " + endpoint}

    return HTTPException(status_code=status.HTTP_409_CONFLICT,
                         detail=detail,
                         headers=headers)


def set_detail(_id: str, endpoint: str, exeption):
    detail: dict = {
        "message": "Error to insert",
        "user_id": _id,
        "endpoint": endpoint,
        "exeption": str(exeption)
    }

    return ResponseModel(**detail)

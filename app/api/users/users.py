
### User  ###

from fastapi import APIRouter
from database.collections import users_collection
from database.db import database
from database.models.users_model import User, UserShort, UserLogin, UserLogged, UserDetails
from helpers.exeptions import error_insert, error_user, error_user_not_found
from security.jwt_generator import generate_token
from security.bcrypt_hash import hash_password
from security.bcrypt_validate import validate_hash
from helpers.responses import success_message, not_found_message, failed_message
from bson.objectid import ObjectId


# Router
router = APIRouter(prefix="/user", tags=["User"])

# Collection
collection = database[users_collection]


@router.post("/create")
async def create_user(user: User):
    try:
        user_dict = dict(user)
        hashed_password = hash_password(user.password)

        user_dict["password"] = hashed_password
        result = collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)
        # Generate token
        token = generate_token(UserShort(**user_dict))
    except Exception as exs:
        raise error_insert(exs)
    return token


@router.post("/login")
async def login(user: UserLogin):
    response = {}
    is_valid = True
    user_not_found = False

    try:
        query = {"email": user.email}
        document = collection.find_one(query)

        if not document:
            user_not_found = True
            raise error_user()

        is_auth_valid = validate_hash(user.password, document["password"])

        # Validate authentication
        if is_auth_valid:
            response = dict(UserLogged(**document))
            response["_id"] = str(document["_id"])
            response = generate_token(response)
        else:
            is_valid = False
            raise error_user()

    except Exception as exs:
        if is_valid == False:
            raise error_user()
        elif user_not_found:
            raise error_user_not_found()
        else:
            raise error_insert(exs)

    return response


@router.delete("/delete/{user_id}")
async def delete_user(user_id: str):
    response = {}

    try:
        query = {"_id": ObjectId(user_id)}
        response = collection.delete_one(query)
    except Exception as exs:
        raise failed_message(user_id, "Delete user", exs)

    if response.deleted_count == 1:
        raise success_message()
    else:
        raise not_found_message()


@router.get("/details/{user_id}")
async def get_user_details(user_id: str):
    result = {}

    try:
        query = {"_id": ObjectId(user_id)}
        result = collection.find_one(query)
        return UserDetails(**result)

    except Exception as exs:
        raise failed_message(user_id, "User not found", exs)

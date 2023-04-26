
### Admin  ###

from fastapi import APIRouter, Header
from helpers.responses import success_message, format_respose
from database.collections import admins_collection, places_collection
from database.db import database
from database.models.admin.admins_model import Admin, AdminShort, AdminLogin, AdminLogged, SelectAdminDetails, UpdateAdminDetails
from database.models.places.places_model import Place
from helpers.exeptions import error_insert, error_user, error_user_not_found
from security.jwt_generator import generate_token
from security.bcrypt_hash import hash_password
from security.bcrypt_validate import validate_hash
from helpers.responses import success_message, not_found_message, failed_message
from bson.objectid import ObjectId
from security.headers import header_id_place

# Router
router = APIRouter(prefix="/admin", tags=["Admin"])

# Collection
admins_collection = database[admins_collection]
places_collection = database[places_collection]


@router.post("/create")
async def create_admin(admin: Admin):
    # Declare variables
    user_dict = dict(admin)

    try:
        # Hash password
        hashed_password = hash_password(admin.password)
        user_dict["password"] = hashed_password

        # Generate new place
        new_place = await create_place()
        user_dict["id_place"] = str(new_place)

        # Inert new user
        result = admins_collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)

        # Generate token
        token = generate_token(AdminShort(**user_dict))

    except Exception as exs:
        raise error_insert(exs)
    return token


async def create_place():
    try:
        place_dict: Place = {
            "name": None,
            "phone": None,
            "email": None,
            "web_site": None,
            "image": None
        }
        document = places_collection.insert_one(place_dict)
        document = str(document.inserted_id)
    except Exception as exs:
        raise error_insert(exs)

    return document


@router.post("/login")
async def login(admin: AdminLogin):
    response = {}
    is_valid = True
    user_not_found = False

    try:
        query = {"email": admin.email}
        document = admins_collection.find_one(query)

        if not document:
            user_not_found = True
            raise error_user()

        is_auth_valid = validate_hash(admin.password, document["password"])

        # Validate authentication
        if is_auth_valid:
            response = dict(AdminLogged(**document))
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


@router.delete("/delete/{admin_id}")
async def delete_user(admin_id: str):
    response = {}

    try:
        query = {"_id": ObjectId(admin_id)}
        response = admins_collection.delete_one(query)
    except Exception as exs:
        raise failed_message(admin_id, "Delete user", exs)

    if response.deleted_count == 1:
        raise success_message()
    else:
        raise not_found_message()


@router.get("/details")
async def get_user_details(Authorization=Header(None)):
    response = {}

    try:
        id_admin = header_id_place(Authorization, "_id")
        SELECT = dict(SelectAdminDetails())
        WHERE = {"_id": ObjectId(id_admin)}

        document = admins_collection.find_one(WHERE, SELECT)
        document.pop("_id")

        response = format_respose([document])

    except Exception as exs:
        raise error_insert(exs)
    return response


@router.put("/details/update")
async def update_user_details(details: UpdateAdminDetails, Authorization=Header(None)):
    response = {}

    try:
        WHERE = {"_id": ObjectId(header_id_place(Authorization, "_id"))}
        UPDATE = {"$set": dict(details)}

        admins_collection.find_one_and_update(WHERE, UPDATE)
        response = format_respose()

    except Exception as exs:
        raise error_insert(exs)
    return response

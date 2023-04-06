
### User  ###

from fastapi import APIRouter
from database.collections import users_collection
from database.db import database
from database.models.users_model import User, UserShort, UserLogin
from database.schemas.users_schema import user_schema
from helpers.exeptions import error_insert, validate_schema
from security.jwt_generator import generate_token
from security.bcrypt_hash import hash_password
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# Router
router = APIRouter(prefix="/users", tags=["users"])

# Collection
collection = database[users_collection]


@router.post("/create")
async def create_user(user: User):
    validate_schema(user, user_schema)
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

    try:
        # user_dict = dict(user)
        query = {"email": "Adelaila@gmail.com"}
        document = collection.find_one(query)
        return JSONResponse(content=jsonable_encoder(dict(document)), status_code=200)
    except Exception as exs:
        raise error_insert(exs)
    # return JSONResponse(content=jsonable_encoder(document), status_code=200)

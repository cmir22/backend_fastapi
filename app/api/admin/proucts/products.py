
### Products ###

from fastapi import APIRouter, Header
from database.collections import products_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.products.products_model import Product
from helpers.aws.s3 import upload_image_s3
from security.headers import header_id_business

# Router
router = APIRouter(prefix="/products", tags=["Products"])

# Collection
PRODUCTS_COLLECTION = database[products_collection]


@router.post("/create")
async def create_product(product: Product, Authorization=Header(None)):
    response = {}
    product = dict(product)

    try:
        # Get user id from header
        id_business = header_id_business(Authorization)

        # Upload image
        NEW_URL = upload_image_s3(product["image"], id_business, "products")

        # Assign values to dict
        product["image"] = NEW_URL["new_url"]
        product["image_key"] = NEW_URL["image_key"]

        # Insert to database
        document = PRODUCTS_COLLECTION.insert_one(product)

        return product

    except Exception as exs:
        raise error_insert(exs)
    return response

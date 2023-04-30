
### Products ###

from fastapi import APIRouter, Header
from database.collections import products_collection
from database.db import database
from helpers.exeptions import error_insert
from database.models.admin.products.products_model import Product
# from security.headers import header_id_business
# from helpers.responses import success_message
# from bson.objectid import ObjectId
from helpers.aws.s3 import upload_image_s3

# Router
router = APIRouter(prefix="/products", tags=["Products"])

# Collection
PRODUCTS_COLLECTION = database[products_collection]


@router.post("/create")
async def create_product(product: Product, Authorization=Header(None)):
    response = {}

    try:
        upload_image_s3(product.image)

    except Exception as exs:
        raise error_insert(exs)
    return response

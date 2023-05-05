
### Products model ###

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Long vertion
class Product(BaseModel):
    name: str
    description: str
    price: Optional[str] = None
    image_key: Optional[str] = None
    image: str
    id_category: str
    is_recommended = False
    is_available = True
    is_active = True
    last_update = datetime.now().today()
    created_date = datetime.now().today()


# To select data
class SelectedProduct(BaseModel):
    price = False
    image_key = False
    id_category = False
    last_update = False
    created_date = False

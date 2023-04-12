
### User model ###

from pydantic import BaseModel
from datetime import datetime


# Long vertion
class ResponseModel(BaseModel):
    message = "Error to insert"
    user_id: str
    endpoint: str
    is_success = False
    created_at = datetime.now().today()
    exeption: str

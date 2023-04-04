
### User  ###

from fastapi import Request, status
from fastapi.responses import JSONResponse
import jwt
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

#  Set token key value
TOKEN_KEY = str(os.environ.get("TOKEN_KEY", "error_token"))


async def validate_jwt(request: Request, call_next: any):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        jwt.decode(token, TOKEN_KEY, algorithms=["HS256"])
    except:
        detail_msg = {'detail': "Unauthorized"}
        return JSONResponse(content=detail_msg, status_code=status.HTTP_401_UNAUTHORIZED)

    return await call_next(request)

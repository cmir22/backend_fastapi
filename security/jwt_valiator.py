
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

EXCLUDE_DOC_ROUTES = ["/docs", "/favicon.ico", "/openapi.json"]
EXCLUDE_ROUTES = ["/users/login"] + EXCLUDE_DOC_ROUTES


async def validate_jwt(request: Request, call_next: any):
    if request.url.path in EXCLUDE_ROUTES:
        response = await call_next(request)
    else:
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        try:
            jwt.decode(token, TOKEN_KEY, algorithms=["HS256"])
            response = await call_next(request)
        except:
            detail_msg = {'detail': "Unauthorized"}
            return JSONResponse(content=detail_msg, status_code=status.HTTP_401_UNAUTHORIZED)

    return response

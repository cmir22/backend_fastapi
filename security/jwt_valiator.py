from fastapi import Request, status
from fastapi.responses import JSONResponse
import jwt
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

TOKEN_KEY = str(os.environ.get("TOKEN_KEY", "error_token"))


async def validate_jwt(request: Request, call_next):
    # decoded_payload = jwt.decode(jwt_token, secret_key, algorithms=['HS256'])
    # response = await call_next(request)
    # print(request.headers.get('Authorization', '').replace('Bearer ', ''))
    return call_next(request)


def on_invalid_token():
    detail_msg = {'detail': "Unauthorized"}
    return JSONResponse(content=detail_msg, status_code=status.HTTP_401_UNAUTHORIZED)

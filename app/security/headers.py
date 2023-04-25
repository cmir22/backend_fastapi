
### Decode JWT  ###


from fastapi import status
from fastapi.responses import JSONResponse
import jwt
from dotenv import load_dotenv
import os
from security.jwt_decode import decode_token

# Load .env
load_dotenv()

#  Set token key value
TOKEN_KEY = str(os.environ.get("TOKEN_KEY", "error_token"))


def header_id_place(authorization: str):
    try:
        id_place = decode_token(authorization)["id_place"]
        id_place = str(id_place)
    except:
        detail_msg = {'detail': "Unauthorized"}
        return JSONResponse(content=detail_msg, status_code=status.HTTP_401_UNAUTHORIZED)

    return id_place

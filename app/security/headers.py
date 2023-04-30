
### Decode JWT  ###


from fastapi import status
from fastapi.responses import JSONResponse
from security.jwt_decode import decode_token


def header_id_business(authorization: str, element="id_business"):
    try:
        id_business = decode_token(authorization)[element]
        id_business = str(id_business)
    except:
        detail_msg = {'detail': "Unauthorized"}
        return JSONResponse(content=detail_msg, status_code=status.HTTP_401_UNAUTHORIZED)

    return id_business

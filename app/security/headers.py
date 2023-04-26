
### Decode JWT  ###


from fastapi import status
from fastapi.responses import JSONResponse
from security.jwt_decode import decode_token


def header_id_place(authorization: str, element="id_place"):
    try:
        id_place = decode_token(authorization)[element]
        id_place = str(id_place)
    except:
        detail_msg = {'detail': "Unauthorized"}
        return JSONResponse(content=detail_msg, status_code=status.HTTP_401_UNAUTHORIZED)

    return id_place

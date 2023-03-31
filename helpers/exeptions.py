
### Exeptions helper ###

from fastapi import HTTPException, status
from jsonschema import Draft7Validator


def format_msg_exeption(message: str, exeption: Exception):
    response: dict = (
        {
            "message": message,
            "exeption": str(exeption)
        }
    )
    return response


def validate_schema(data: any, schema: any):
    try:
        Draft7Validator(schema).validate(dict(data))
    except Exception as exs:
        raise error_schema(exs)


def error_schema(exs: Exception):
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                         detail=format_msg_exeption("Error on schema", exs))


def error_insert(exs: Exception):
    return HTTPException(status_code=status.HTTP_409_CONFLICT,
                         detail=format_msg_exeption("Error on insert", exs))

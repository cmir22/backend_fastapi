
### Exeptions helper ###

def msg_exeption(message: str, exeption: Exception):
    response: dict = (
        {
            "message": message,
            "exeption": str(exeption)
        }
    )
    return response

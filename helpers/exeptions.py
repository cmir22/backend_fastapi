
### Exeptions helper ###

def msg_exeption(message: str, exeption):
    response: dict = (
        {"message": message,
         "exeption": str(exeption)
         }
    )
    return response

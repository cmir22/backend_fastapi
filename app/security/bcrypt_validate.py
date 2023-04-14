
### Validate ncrypt password ###

import bcrypt


def validate_hash(password: str, stored_password):
    input_password = password.encode('utf-8')
    stored_password_hash = stored_password.encode('utf-8')

    if bcrypt.checkpw(input_password, stored_password_hash):
        return True
    else:
        return False

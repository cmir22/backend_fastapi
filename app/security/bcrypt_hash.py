import bcrypt


def hash_password(password: str):
    rounds: int = 14
    salt = bcrypt.gensalt(rounds=rounds)
    byte_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_password, salt)
    decoded_password: str = hashed_password.decode('utf-8')
    return decoded_password

import bcrypt


def hash_password(password: str):
    rounds = 14
    salt = bcrypt.gensalt(rounds=rounds)
    byte_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return hashed_password

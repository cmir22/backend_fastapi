import jwt
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()


def generate_token(data):
    TOKEN_KEY = str(os.environ.get("TOKEN_KEY", "error_token"))
    token = str(jwt.encode(dict(data), TOKEN_KEY, algorithm='HS256'))
    return {"token": token}

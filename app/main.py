
### Main file ###

from fastapi import FastAPI
from api.users import users
from api.admin import admins
# from security.jwt_valiator import validate_jwt

app = FastAPI()

# app.middleware("http")(validate_jwt)

# Routers
app.include_router(users.router)
app.include_router(admins.router)

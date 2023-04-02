
### Main file ###

from fastapi import FastAPI
from routers import users
from security.jwt_valiator import validate_jwt

app = FastAPI()

app.middleware("http")(validate_jwt)

# Routers
app.include_router(users.router)

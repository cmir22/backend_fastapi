
### Main file ###

from fastapi import FastAPI
from api.users import users
from api.admin import admins
from api.admin.places import places, schedule
from api.admin.locations import locations
# from security.jwt_valiator import validate_jwt


# App
app = FastAPI()

# Security
# app.middleware("http")(validate_jwt)

# Routers
app.include_router(users.router)
app.include_router(admins.router)
app.include_router(places.router)
app.include_router(schedule.router)
app.include_router(locations.router)


### Main file ###

from fastapi import FastAPI
from api.users import users
from api.admin import admins
from api.admin.business import business, schedule
from api.admin.locations import locations
from api.admin.locations import locations
from api.admin.proucts import categories, products
# from security.jwt_valiator import validate_jwt


# App
app = FastAPI()

# Security
# app.middleware("http")(validate_jwt)

# Routers
app.include_router(users.router)
app.include_router(admins.router)
app.include_router(business.router)
app.include_router(schedule.router)
app.include_router(locations.router)
app.include_router(categories.router)
app.include_router(products.router)


### Main file ###

from fastapi import FastAPI
from routers import users

app = FastAPI()

# Routers
app.include_router(users.router)

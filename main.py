from fastapi import FastAPI
from routers import users
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

# Routers
app.include_router(users.router)

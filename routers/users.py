from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users")


@router.get("/")
async def root():
    return {"Hola users!"}

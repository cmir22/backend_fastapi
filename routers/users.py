from fastapi import APIRouter
from pydantic import BaseModel

# Router
router = APIRouter(prefix="/users")


@router.get("/")
async def root():
    return {"si"}

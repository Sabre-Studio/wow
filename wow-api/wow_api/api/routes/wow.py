from fastapi import APIRouter

wow_router = APIRouter()


@wow_router.get("/wow", tags=["wow"])
async def get_wow() -> str:
    return "hi"

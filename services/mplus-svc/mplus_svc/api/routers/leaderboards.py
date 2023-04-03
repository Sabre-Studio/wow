from fastapi import APIRouter

leaderboard_router = APIRouter()


@leaderboard_router.get("/leaderboard/{realm_id}")
async def get_realm_leaderboard(realm: id):
    pass

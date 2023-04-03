from fastapi import APIRouter

from wow_api.external.blizz_api.auth import BlizzardApiAuth
from wow_api.external.blizz_api.game.connected_realm import (
    ConnectedRealmResponse, ConnectedRealmSearchResponse,
    get_connected_realm_by_id, get_connected_realm_search)

wow_router = APIRouter()

api_auth = BlizzardApiAuth()


@wow_router.get("/wow", tags=["wow"])
async def get_wow() -> str:
    return "hi"


@wow_router.get("/dungeons", tags=["leaderboard"])
async def get_dungeons() -> list[str]:
    return ["Ruby Life Pools", "Azure Vaults"]


@wow_router.get("/connected-realms", tags=["connected-realms"])
async def get_connected_realms() -> ConnectedRealmSearchResponse:
    return get_connected_realm_search(api_auth.get_token())


@wow_router.get("/connected-realms/{connected_realm_id}", tags=["connected-realms"])
async def get_connected_realm(
    connected_realm_id: int,
) -> ConnectedRealmResponse:
    return get_connected_realm_by_id(
        connected_realm_id=connected_realm_id, token=api_auth.get_token()
    )

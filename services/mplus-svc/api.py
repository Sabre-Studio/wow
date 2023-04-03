from typing import Annotated

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import Settings, get_settings
from mplus_svc.api.routers.leaderboards import leaderboard_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leaderboard_router)


@app.on_event("startup")
async def svc_start() -> None:
    print("mplus svc started")


@app.on_event("shutdown")
async def svc_shutdown() -> None:
    print("mplus svc shutdown")


@app.get("/")
async def root():
    return {"message": "Hello, World! I'm the Mplus svc"}


@app.get("/info")
async def get_info(
    settings: Annotated[Settings, Depends(get_settings)]
) -> dict[str, str]:
    return {"version": "v0.0.0", "build_env": settings.build_env}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)

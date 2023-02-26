from functools import lru_cache

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import Settings
from wow_api.api.routes.wow import wow_router

app = FastAPI()

app.include_router(wow_router)


@lru_cache()
def get_settings():
    return Settings()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Note: You can add multiple event handler functions and your app will wait
# until they are all done before it starts to receive requests
@app.on_event("startup")
async def startup_event():
    print("wow api start")


@app.on_event("shutdown")
async def shutdown_event():
    print("wow api shutdown")


@app.get("/")
async def hello():
    return {"message": "Hello from the wow api!"}


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "build_env": settings.build_env,
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)

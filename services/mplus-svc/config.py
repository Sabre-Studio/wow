from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    build_env: str
    db_cs: PostgresDsn
    blizz_client_id: str
    blizz_client_secret: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings.parse_obj({})

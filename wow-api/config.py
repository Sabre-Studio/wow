from pydantic import BaseSettings


class Settings(BaseSettings):
    build_env: str = "local"
    db_cs: str = "postgresql://postgres:pass@pg_db/wow"

    class Config:
        env_file = ".env"

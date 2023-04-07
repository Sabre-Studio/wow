from pydantic import BaseSettings


class Settings(BaseSettings):
    db_cs: str = "postgresql://postgres:pass@pg_db/wow"

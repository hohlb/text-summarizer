from pydantic import BaseSettings


class Settings(BaseSettings):
    database_file: str = "summaries.db"


settings = Settings()

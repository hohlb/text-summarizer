from pydantic import BaseSettings


class Settings(BaseSettings):
    database_file: str = "summaries.db"
    database_check_same_thread: bool = True


settings = Settings()

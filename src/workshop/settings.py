from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_post: int = 8000
    database_url: str = 'sqlite:///./database.sqlite'

settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "DDR Report Generator"


settings = Settings()
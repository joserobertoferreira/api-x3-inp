from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    DB: str
    DB_SERVER: str
    DB_PORT: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_SCHEMA: str
    DB_DRIVER: str

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    database_url: str = Field(
        "postgresql+asyncpg://postgres:postgres@db:5432/postgres_typo",
        validation_alias="DATABASE_URL",
    )
    log_level: str = Field(
        "INFO",
        validation_alias="LOG_LEVEL",
    )
    parse_schedule_minutes: int = Field(
        5,
        validation_alias="PARSE_SCHEDULE_MINUTES",
    )


settings = Settings()

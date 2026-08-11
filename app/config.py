from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", case_sensitive=False)

    app_name: str = "Qualificador de Leads API"
    secret_key: str = Field(
        default="troque-isso-em-producao-use-openssl-rand-hex-32",
        validation_alias="SECRET_KEY",
    )
    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(default=60, validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    database_url: str = Field(default="sqlite:///./leads.db", validation_alias="DATABASE_URL")


settings = Settings()

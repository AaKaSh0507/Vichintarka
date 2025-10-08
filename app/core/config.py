from typing import Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
    # Database Configuration
    DATABASE_URL: Union[str, None] = None

    # Redis Configuration
    REDIS_URL: str = "redis://localhost:6379/0"

    # Application Configuration
    SECRET_KEY: str = "Vichintarka"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ENVIRONMENT: str = "development"

    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Vichintarka"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "FastAPI application with PostgreSQL and Redis"

    # Database Configuration (for Docker)
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "vichintarka"
    POSTGRES_PORT: int = 5432

    # Redis Configuration (for Docker)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Union[str, None] = None

    # Application Settings
    DEBUG: bool = False
    TESTING: bool = False

    @property
    def database_url(self) -> str:
        """Build database URL from components if DATABASE_URL not provided."""
        if self.DATABASE_URL:
            # Convert postgresql+asyncpg:// to postgresql:// for asyncpg
            url = self.DATABASE_URL
            if url.startswith("postgresql+asyncpg://"):
                url = url.replace("postgresql+asyncpg://", "postgresql://")
            return url
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def redis_url(self) -> str:
        """Build Redis URL from components."""
        if self.REDIS_PASSWORD:
            return (
                f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:"
                f"{self.REDIS_PORT}/{self.REDIS_DB}"
            )
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"


settings = Settings()

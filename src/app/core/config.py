from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configurações do FastAPI
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    # Configurações do banco de dados
    DATABASE_URL: str
    TEST_DATABASE_URL: str | None = None  # Add this line
    # Configurações de Segunrança
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    
    class Config:
        env_file = ".env"
        case_sensitive = False  # Optional: makes field names case-insensitive
        extra = "ignore"  # Optional: ignores extra fields from .env

settings = Settings()
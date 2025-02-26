from pydantic import BaseSettings

class Settings(BaseSettings):
 # Configurações do FastAPI
    DEBUG: bool = True
    API_V1_STR: str = "/api/v10"
    SECRET_KEY: str
     # Configurações do banco de dados
    DATABASE_URL : str 

# Carrega variáveis de ambiente do arquivo .env
    class Config:
        env_file = ".env"

settings = Settings()
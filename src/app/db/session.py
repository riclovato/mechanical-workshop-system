from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from app.db.base import Base
from app.core.config import settings
#configuração do banco de dados
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

def get_db() -> Generator[Session, None, None]:
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()
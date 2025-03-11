# tests/conftest.py
import pytest
import os
import sys
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.db.base import Base

# Adiciona o diretório raiz ao PYTHONPATH
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir / "src"))
TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql://postgres:admin123@localhost:5432/workshop_test?client_encoding=utf8"
)

@pytest.fixture(scope="session")
def db_engine():
    """Fixture: Cria engine do PostgreSQL e gerencia o ciclo de vida das tabelas"""
    engine = create_engine(TEST_DATABASE_URL)
    
    try:
        # Cria todas as tabelas
        Base.metadata.create_all(bind=engine)
        yield engine
    finally:
        # Remove todas as tabelas após os testes
        Base.metadata.drop_all(bind=engine)
        engine.dispose()

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Fixture: Fornece uma sessão isolada para cada teste com rollback automático"""
    connection = db_engine.connect()
    transaction = connection.begin()
    
    try:
        # Configura a sessão
        Session = sessionmaker(bind=connection)
        session = Session()
        yield session
    except SQLAlchemyError as e:
        # Captura erros inesperados
        transaction.rollback()
        pytest.fail(f"Erro inesperado no banco de dados: {str(e)}")
    finally:
        # Limpeza garantida
        session.close()
        transaction.rollback()
        connection.close()
import sys
from pathlib import Path
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Adicione esta linha para garantir que o Python encontre seus módulos
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

# Importe a Base DEPOIS de ajustar o sys.path
from app.db.base import Base  # noqa

# Remova os imports diretos dos modelos. Eles devem ser importados através da Base
# Deixe o Alembic detectar automaticamente através dos metadados

# Configuração do Alembic
config = context.config

# Configure o logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,  # Adicione para detectar alterações de tipo de coluna
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Adicione para detectar alterações de tipo de coluna
            compare_server_default=True,  # Detecta mudanças em valores default
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
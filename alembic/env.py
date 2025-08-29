from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from src.core.config import settings
from src.core.database import Base

# 👇 importa tus modelos aquí
from src.users.models import User
from src.products.models import Product
from src.reviews.models import Review

# Configuración de logging
config = context.config
fileConfig(config.config_file_name)

# Metadata de los modelos
target_metadata = Base.metadata

def run_migrations_offline():
    """Ejecutar migraciones en modo offline (sin conexión directa a DB)."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecutar migraciones en modo online (con engine)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=settings.DATABASE_URL
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

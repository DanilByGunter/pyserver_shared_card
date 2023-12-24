from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import os
import sys

from src.config import DB_HOST, DB_PORT, DB_NAME, DB_PASS, DB_USER
from src.category.models import metadata as category_metadata
from src.shop.models import metadata as shop_metadata
from src.metric.models import metadata as metric_metadata
from src.currency.models import metadata as currency_metadata
from src.user.models import metadata as user_metadata
from src.product.models import metadata as product_metadata
from src.recipe.models import metadata as recipe_metadata
from src.recipe_product.models import metadata as recipe_product_metadata
from src.group.models import metadata as group_metadata
from src.check.models import metadata as check_metadata
from src.group_user.models import metadata as group_user_metadata
from src.target.models import metadata as target_metadata
from src.group_token.models import metadata as group_token_metadata
from src.user_account.models import metadata as user_account_metadata

sys.path.append(os.path.join(sys.path[0], 'src'))

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section = config.config_ini_section
config.set_section_option(section, "DB_HOST", DB_HOST)
config.set_section_option(section, "DB_PORT", DB_PORT)
config.set_section_option(section, "DB_USER", DB_USER)
config.set_section_option(section, "DB_NAME", DB_NAME)
config.set_section_option(section, "DB_PASS", DB_PASS)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = [category_metadata, shop_metadata, metric_metadata, 
                   currency_metadata, user_account_metadata, user_metadata, 
                   product_metadata, recipe_metadata, recipe_product_metadata, 
                   group_metadata, check_metadata, group_user_metadata, 
                   target_metadata, group_token_metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

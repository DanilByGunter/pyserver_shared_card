from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlalchemy import Table, Column, INTEGER, String, MetaData, ForeignKey, Boolean
import uuid
from datetime import datetime

from src.category.models import category
from src.user.models import user
from src.shop.models import shop
from src.currency.models import currency
from src.group.models import group

metadata = MetaData()

target = Table(
    "target",
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True),
    Column('id_category', ForeignKey(category.c.id), nullable=True),
    Column('id_shop', ForeignKey(shop.c.id), nullable=True),
    Column('id_currency', ForeignKey(currency.c.code), nullable=True),
    Column('id_group', ForeignKey(group.c.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False),
    Column('id_creator', ForeignKey(user.c.id), nullable=False),
    Column('id_buyer', ForeignKey(user.c.id), nullable=True),
    Column('date_create', TIMESTAMP, nullable=True, default=datetime.now),
    Column('date_close', TIMESTAMP, nullable=True),
    Column('description', String(128), nullable=True),
    Column('name', String(32), nullable=True),
    Column('price_first', INTEGER, nullable=True),
    Column('price_last', INTEGER, nullable=True),
    Column('status', Boolean, nullable=True, default=True)
)

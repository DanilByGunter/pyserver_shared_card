# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Table, Column, String, INTEGER, MetaData, ForeignKey
from src.user_account.models import user_account
# import uuid

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column('id',  ForeignKey(user_account.c.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False, unique=True, primary_key=True),
    Column('name',  String(32), nullable=False),
    Column('photo', String(256), nullable=True),
    Column('weight', INTEGER, nullable=True),
    Column('height', INTEGER, nullable=True),
    Column('age', INTEGER, nullable=True)
)

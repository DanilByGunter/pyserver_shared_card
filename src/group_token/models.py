from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import Table, Column, String, MetaData, ForeignKey

from datetime import datetime
import string
import random

from src.group.models import group

metadata = MetaData()

def generate_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 12))


group_token = Table(
    "group_token",
    metadata,
    Column('id', ForeignKey(group.c.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False, unique=True, primary_key=True),
    Column('token', String(12), nullable=True, default=generate_token),
    Column('date', TIMESTAMP, nullable=True, default=datetime.now)
)

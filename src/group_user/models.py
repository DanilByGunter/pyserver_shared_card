from sqlalchemy.dialects.postgresql import TIMESTAMP, ENUM
from sqlalchemy import Table, Column, MetaData, ForeignKey
from src.user.models import user
from src.group.models import group 
from datetime import datetime
from enum import Enum, unique
import uuid

metadata = MetaData()

@unique
class Role(Enum):
    CREATOR = "creator"
    ADMIN = "admin"
    USER = "user"
    
group_user_association = Table(
    "group_user_association",
    metadata,
    Column('id_user', ForeignKey(user.c.id, onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
    Column('id_group', ForeignKey(group.c.id, onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
    Column('status', ENUM(Role, name="user_status", create_type=True), default=Role.USER),
    Column('date_invite', TIMESTAMP, nullable=True, default=datetime.now)
)

from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, ENUM
from sqlalchemy import Table, Column, String, MetaData
from datetime import datetime
from enum import Enum, unique
import uuid

metadata = MetaData()

@unique
class Place(Enum):
    local = "local"
    globals = "globals"
    

group = Table(
    "group",
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True),
    Column('name', String(32), nullable=True, default=''),
    Column('photo', String(256), nullable=True),
    Column('creation_date', TIMESTAMP, nullable=True, default=datetime.now),
    Column('status', ENUM(Place, name="group_status", create_type=True), default=Place.local)
)

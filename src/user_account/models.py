from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, String, Boolean, MetaData
from src.database import Base
import uuid
from datetime import datetime

metadata = MetaData()

user_account = Table(
    'user_account',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True),
    Column('email', String(128), nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('hashed_password', String(1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)

class UserAccount(SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'user_account'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    email = Column(String(128), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password: Column(String(length=1024), nullable=False)
    is_active: Column(Boolean, default=True, nullable=False)
    is_superuser: Column(Boolean, default=False, nullable=False)
    is_verified: Column(Boolean, default=False, nullable=False)
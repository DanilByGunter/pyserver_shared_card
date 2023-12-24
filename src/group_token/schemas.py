from pydantic import BaseModel
from src.group_token.models import generate_token
from datetime import datetime
import uuid


class GroupTokenCreate(BaseModel):
    id_group: uuid.UUID | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class GroupTokenUpdate(BaseModel):
    token: str | None = generate_token()
    date: datetime | None = datetime.now()

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

from pydantic import BaseModel
from enum import Enum, unique
import uuid

@unique
class Role(Enum):
    CREATOR = "creator"
    ADMIN = "admin"
    USER = "user"

class GroupCreate(BaseModel):
    id_user: uuid.UUID
    id_group: uuid.UUID
    status: bool | None = Role.USER

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class GroupUpdate(BaseModel):
    id_user: uuid.UUID | None
    id_group: uuid.UUID | None
    status: bool | Role | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

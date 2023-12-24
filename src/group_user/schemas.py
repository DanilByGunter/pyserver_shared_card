from pydantic import BaseModel
from enum import Enum, unique
import uuid

@unique
class Role(Enum):
    CREATOR = "CREATOR"
    ADMIN = "ADMIN"
    USER = "USER"

class GroupCreate(BaseModel):
    id_user: uuid.UUID
    id_group: uuid.UUID

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class GroupUpdate(BaseModel):
    id_user: uuid.UUID
    status: Role | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

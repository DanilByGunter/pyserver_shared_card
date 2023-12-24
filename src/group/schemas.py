from pydantic import BaseModel
from src.group.models import Place

class GroupCreate(BaseModel):
    name: str | None = None
    photo: str | None = None
    status: Place | None = Place.local

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class GroupUpdate(BaseModel):
    name: str | None
    photo: str | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

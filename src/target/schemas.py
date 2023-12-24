from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class TargetCreate(BaseModel):
    id_category: int | None = None
    id_currency: str | None = None
    id_group: uuid.UUID
    id_creator: uuid.UUID
    name: str | None = Field(max_length=64, default=None, description="Max length of the name must be less than 64")
    description: str | None = Field(max_length=128, default=None, description="Max length of the description must be less than 128")
    price_first: int | None = Field(gt=0, default=None, description="The price must be greater than zero")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class TargetUpdate(BaseModel):
    id_shop: int | None
    id_currency: str | None
    id_buyer: uuid.UUID
    price_last: int | None = Field(gt=0, description="The price must be greater than zero")
    status: bool | None = False
    date_close: datetime | None = datetime.now()
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

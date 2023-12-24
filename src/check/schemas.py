from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class CheckCreate(BaseModel):
    id_product: int
    id_metric: int | None
    id_group: uuid.UUID
    id_creator: uuid.UUID
    description: str | None = Field(max_length=128, description="Max length of the description must be less than 128")
    count: int | None = Field(gt=0, description="The count must be greater than zero")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class CheckUpdate(BaseModel):
    id_shop: int | None
    id_currency: str | None
    id_buyer: uuid.UUID
    price: int | None = Field(gt=0, description="The price must be greater than zero")
    status: bool | None = Field(default=False)
    date_close: datetime | None = Field(default=datetime.now())
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

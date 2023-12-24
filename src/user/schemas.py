from pydantic import BaseModel, Field
import uuid

class UserCreate(BaseModel):
    id: uuid.UUID
    name: str
    photo: str | None = None
    weight: float | None = Field(gt=0, lt=600, default=None, description="The weight must be greater than zero")
    height: float | None = Field(gt=0, lt=300, default=None, description="The height must be greater than zero")
    age: int | None = Field(gt=0, lt=100, default=None, description="The age must be greater than zero")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class UserUpdate(BaseModel):
    name: str | None
    photo: str | None
    weight: float | None = Field(gt=0, lt=600, description="The weight must be greater than zero")
    height: float | None = Field(gt=0, lt=300, description="The height must be greater than zero")
    age: int | None = Field(gt=0, lt=100, description="The age must be greater than zero")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

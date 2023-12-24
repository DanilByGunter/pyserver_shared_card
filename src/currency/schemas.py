from pydantic import BaseModel, Field


class CurrencyCreate(BaseModel):
    code: str = Field(min_length=3, max_length=3)
    name: str
    name_en: str | None = None
    units: int | None = 1
    course: float | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class CurrencyUpdate(BaseModel):
    name: str | None
    name_en: str | None
    units: int | None
    course: float | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

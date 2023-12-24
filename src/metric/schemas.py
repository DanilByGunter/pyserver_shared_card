from pydantic import BaseModel


class MetricCreate(BaseModel):
    name: str
    name_en: str | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class MetricUpdate(BaseModel):
    name: str | None
    name_en: str | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

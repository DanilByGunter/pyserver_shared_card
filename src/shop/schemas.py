from pydantic import BaseModel


class ShopCreate(BaseModel):
    name: str
    name_en: str | None = None
    status: bool | None = True

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class ShopUpdate(BaseModel):
    name: str | None
    name_en: str | None
    status: bool | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

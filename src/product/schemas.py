from pydantic import BaseModel, Field
from src.recipe_product.models import recipe_product_association

class ProductCreate(BaseModel):
    name: str
    name_en: str | None = None
    id_category: int | None = 1
    fat: float | None = Field(gt=0, lt=100, default=None, description="The fat must be greater than zero")
    protein: float | None = Field(gt=0, lt=100, default=None, description="The protein must be greater than zero")
    carb: float | None = Field(gt=0, lt=100, default=None, description="The carb must be greater than zero")
    calorie: float | None = Field(gt=0, lt=3000, default=None, description="The calorie must be greater than zero")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class ProductUpdate(BaseModel):
    name: str | None
    name_en: str | None
    id_category: int | None
    fat: float | None = Field(gt=0, lt=100, description="The fat must be greater than zero")
    protein: float | None = Field(gt=0, lt=100, description="The protein must be greater than zero")
    carb: float | None = Field(gt=0, lt=100, description="The carb must be greater than zero")
    calorie: float | None = Field(gt=0, lt=3000, description="The calorie must be greater than zero")
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

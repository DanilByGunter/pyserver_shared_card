from pydantic import BaseModel
from typing import TYPE_CHECKING
from src.recipe_product.models import recipe_product_association
from sqlalchemy.orm import Mapped, relationship

if TYPE_CHECKING:
    from src.product.models import product

class RecipeCreate(BaseModel):
    name: str
    name_en: str | None = None
    description: str | None = None
    portion: int | None = None
    calories: float | None = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class RecipeUpdate(BaseModel):
    name: str | None
    name_en: str | None
    description: str | None
    portion: int | None
    calories: float | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

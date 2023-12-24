from pydantic import BaseModel, Field

class RecipeCreate(BaseModel):
    id_product: int
    id_recipe: int
    id_metric: int | None = None
    count: int | None = Field(gt=0, default=None, description="The count must be greater than zero")

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True


class RecipeUpdate(BaseModel):
    id_product: int | None
    id_recipe: int | None
    id_metric: int | None
    count: int | None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

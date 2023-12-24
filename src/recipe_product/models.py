from sqlalchemy import Table, Column, INTEGER, MetaData, INTEGER, ForeignKey
from src.product.models import product
from src.recipe.models import recipe
from src.metric.models import metric

metadata = MetaData()

recipe_product_association = Table(
    "recipe_product_association",
    metadata,
    Column('id_product', ForeignKey(product.c.id, onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
    Column('id_recipe', ForeignKey(recipe.c.id, onupdate="CASCADE", ondelete="CASCADE"), primary_key=True, nullable=False),
    Column('id_metric', ForeignKey(metric.c.id), nullable=True),
    Column('count', INTEGER, nullable=True)
)

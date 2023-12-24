from sqlalchemy import Table, Column, FLOAT, String, INTEGER, MetaData, ForeignKey
from src.category.models import category

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name', String(32), nullable=False),
    Column('name_en', String(32), nullable=True),
    Column('id_category', ForeignKey(category.c.id), nullable=True, default=1),
    Column('fat', FLOAT, nullable=True),
    Column('protein', FLOAT, nullable=True),
    Column('carb', FLOAT, nullable=True),
    Column('calorie', FLOAT, nullable=True)
)

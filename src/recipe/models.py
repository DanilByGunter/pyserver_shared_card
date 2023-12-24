from sqlalchemy import Table, Column, INTEGER, String, Float, MetaData

metadata = MetaData()

recipe = Table(
    "recipe",
    metadata,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name', String(32), nullable=False),
    Column('name_en', String(32), nullable=True),
    Column('description', String(128), nullable=True),
    Column('portion', INTEGER, nullable=True),
    Column('calories', Float, nullable=True)
)

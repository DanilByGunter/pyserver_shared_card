from sqlalchemy import Table, Column, INTEGER, String, MetaData

metadata = MetaData()

metric = Table(
    "metric",
    metadata,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name', String(32), unique=True, nullable=False),
    Column('name_en', String(32), nullable=True)
)

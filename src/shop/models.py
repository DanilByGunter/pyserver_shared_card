from sqlalchemy import Table, Column, INTEGER, String, BOOLEAN, MetaData

metadata = MetaData()

shop = Table(
    "shop",
    metadata,
    Column('id', INTEGER, primary_key=True, autoincrement=True),
    Column('name', String(32), nullable=False),
    Column('name_en', String(32), nullable=True),
    Column('status', BOOLEAN, nullable=True, default=True)
)

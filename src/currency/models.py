from sqlalchemy import Table, Column, String, MetaData, VARCHAR, INTEGER, FLOAT

metadata = MetaData()

currency = Table(
    "currency",
    metadata,
    Column('code', VARCHAR(3), primary_key=True),
    Column('name', String(32), unique=True, nullable=False),
    Column('code_en', String(3), nullable=True),
    Column('units', INTEGER, nullable=True),
    Column('course', FLOAT, nullable=True)
)

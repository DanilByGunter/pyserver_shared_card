"""upgrade many-to-many

Revision ID: de579845e518
Revises: 37b1b6236fa2
Create Date: 2023-12-24 16:47:18.290088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de579845e518'
down_revision: Union[str, None] = '37b1b6236fa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    op.drop_constraint('idx_group_user', 'group_user_association', type_='unique')
    op.drop_column('group_user_association', 'id')
    op.drop_constraint('idx_recipe_product', 'recipe_product_association', type_='unique')
    op.drop_column('recipe_product_association', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe_product_association', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.create_unique_constraint('idx_recipe_product', 'recipe_product_association', ['id_recipe', 'id_product'])
    op.add_column('group_user_association', sa.Column('id', sa.UUID(), autoincrement=False, nullable=False))
    op.create_unique_constraint('idx_group_user', 'group_user_association', ['id_user', 'id_group'])
    op.create_table('account',
    sa.Column('uid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('login', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('role', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('pwhash', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('real_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('home_phone', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('uid', name='account_pkey')
    )
    # ### end Alembic commands ###

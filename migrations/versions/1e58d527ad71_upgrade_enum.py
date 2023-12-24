"""upgrade enum

Revision ID: 1e58d527ad71
Revises: 15fe268f62e9
Create Date: 2023-12-24 15:35:20.860492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e58d527ad71'
down_revision: Union[str, None] = '15fe268f62e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    op.drop_index('index_check_id', table_name='check', postgresql_using='hash')
    op.create_foreign_key(None, 'check', 'user', ['id_creator'], ['id'])
    op.create_foreign_key(None, 'check', 'user', ['id_buyer'], ['id'])
    op.drop_constraint('group_user_association_id_user_fkey', 'group_user_association', type_='foreignkey')
    op.create_foreign_key(None, 'group_user_association', 'user', ['id_user'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_index('index_target_id', table_name='target', postgresql_using='hash')
    op.create_foreign_key(None, 'target', 'user', ['id_buyer'], ['id'])
    op.create_foreign_key(None, 'target', 'user', ['id_creator'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'target', type_='foreignkey')
    op.drop_constraint(None, 'target', type_='foreignkey')
    op.create_index('index_target_id', 'target', ['id_group'], unique=False, postgresql_using='hash')
    op.drop_constraint(None, 'group_user_association', type_='foreignkey')
    op.create_foreign_key('group_user_association_id_user_fkey', 'group_user_association', 'user', ['id_user'], ['id_user'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint(None, 'check', type_='foreignkey')
    op.drop_constraint(None, 'check', type_='foreignkey')
    op.create_index('index_check_id', 'check', ['id_group'], unique=False, postgresql_using='hash')
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

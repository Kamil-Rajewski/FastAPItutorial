"""add fkey to post table

Revision ID: 867c20a558c7
Revises: 792253c74664
Create Date: 2023-02-24 17:54:43.557508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '867c20a558c7'
down_revision = '792253c74664'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('posts_users_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')

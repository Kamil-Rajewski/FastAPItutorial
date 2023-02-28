"""add content column to post table

Revision ID: d1b702863b35
Revises: cf97db4dd980
Create Date: 2023-02-24 17:42:07.386545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1b702863b35'
down_revision = 'cf97db4dd980'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')

"""add user table

Revision ID: 792253c74664
Revises: d1b702863b35
Create Date: 2023-02-24 17:46:32.523492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '792253c74664'
down_revision = 'd1b702863b35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')

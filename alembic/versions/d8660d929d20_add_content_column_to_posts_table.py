"""add content column to posts table

Revision ID: d8660d929d20
Revises: 7ebf9c1ccb0f
Create Date: 2023-03-01 14:06:07.808094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8660d929d20'
down_revision = '7ebf9c1ccb0f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

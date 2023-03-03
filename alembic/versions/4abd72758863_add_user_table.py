"""add user table

Revision ID: 4abd72758863
Revises: d8660d929d20
Create Date: 2023-03-02 12:24:09.196535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4abd72758863'
down_revision = 'd8660d929d20'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass

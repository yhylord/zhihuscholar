"""create users table

Revision ID: 7f4b767fea17
Revises: 
Create Date: 2017-10-15 08:58:52.070443+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f4b767fea17'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('email', sa.String(128), nullable=False),
        sa.Column('password', sa.String(128), nullable=False)
    )


def downgrade():
    op.drop_table('users')

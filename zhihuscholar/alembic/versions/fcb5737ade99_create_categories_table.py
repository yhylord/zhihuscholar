"""create categories table

Revision ID: fcb5737ade99
Revises: a6f255b9c242
Create Date: 2017-10-22 02:31:40.203051+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcb5737ade99'
down_revision = '7f4b767fea17'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=True)
    )


def downgrade():
    op.drop_table('categories')

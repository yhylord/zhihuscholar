"""create columns table

Revision ID: b4dae29a2d3d
Revises: fcb5737ade99
Create Date: 2017-10-22 02:33:13.049443+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4dae29a2d3d'
down_revision = 'fcb5737ade99'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'columns',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'), nullable=False),
        sa.Column('name', sa.String(64), nullable=False)
    )


def downgrade():
    pass

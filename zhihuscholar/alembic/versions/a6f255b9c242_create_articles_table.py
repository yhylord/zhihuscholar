"""create articles table

Revision ID: a6f255b9c242
Revises: 7f4b767fea17
Create Date: 2017-10-22 01:56:04.785510+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f255b9c242'
down_revision = 'b4dae29a2d3d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('column_id', sa.Integer, sa.ForeignKey('columns.id'), nullable=False),
        sa.Column('title', sa.String(256), nullable=False),
        sa.Column('text', sa.Text, nullable=False),
        sa.Column('feature', sa.PickleType, nullable=False)
    )

def downgrade():
    op.drop_table('articles')

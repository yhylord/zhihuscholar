"""create feedback table

Revision ID: cb403ae39ea7
Revises: a6f255b9c242
Create Date: 2017-10-24 12:33:47.958105+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb403ae39ea7'
down_revision = 'a6f255b9c242'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'feedback',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True, nullable=False),
        sa.Column('article_id', sa.Integer, sa.ForeignKey('articles.id'), primary_key=True, nullable=False),
        sa.Column('opinion', sa.String, nullable=False)
    )

def downgrade():
    op.drop_table('feedback')

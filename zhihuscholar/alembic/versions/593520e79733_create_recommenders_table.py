"""create recommenders table

Revision ID: 593520e79733
Revises: cb403ae39ea7
Create Date: 2017-10-27 14:00:25.304239+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '593520e79733'
down_revision = 'cb403ae39ea7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'recommenders',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), primary_key=True, nullable=False),
        sa.Column('recommender', sa.PickleType)
    )


def downgrade():
    op.drop_table('recommenders')

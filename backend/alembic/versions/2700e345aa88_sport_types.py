"""Sport types

Revision ID: 2700e345aa88
Revises: defc1aa64f94
Create Date: 2023-07-16 17:25:57.369833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2700e345aa88'
down_revision = 'defc1aa64f94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    sport_table = op.create_table(
        'sport',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),

        sa.PrimaryKeyConstraint('id'),
    )

    op.bulk_insert(
        sport_table,
        [
            {"name": "Rugby League", "active": True},
            {"name": "Rugby Union", "active": True},
        ],
    )


def downgrade() -> None:
    op.drop_table('sport')


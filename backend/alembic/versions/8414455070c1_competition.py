"""Competition

Revision ID: 8414455070c1
Revises: 2e1584a40a08
Create Date: 2023-07-19 07:11:20.521110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8414455070c1'
down_revision = '2e1584a40a08'
branch_labels = None
depends_on = None


def upgrade() -> None:
    structure_table = op.create_table(
        'structure',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),

        sa.PrimaryKeyConstraint('id'),
    )

    competition_table = op.create_table(
        'competition',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('sport_id', sa.Integer, nullable=False),
        sa.Column('structure_id', sa.Integer, nullable=False),
        sa.Column('image', sa.String(80), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['sport_id'], ['sport.id']),
        sa.ForeignKeyConstraint(['structure_id'], ['structure.id']),
    )

    op.bulk_insert(
        structure_table,
        [
            {"name": "Elimination", "active": True},
            {"name": "Round Robin", "active": True},
        ],
    )


def downgrade() -> None:
    op.drop_table('competition')
    op.drop_table('structure')

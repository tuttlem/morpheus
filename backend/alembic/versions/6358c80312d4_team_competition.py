"""Team Competition

Revision ID: 6358c80312d4
Revises: 8414455070c1
Create Date: 2023-07-19 07:48:00.761681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6358c80312d4'
down_revision = '8414455070c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    competition_team_table = op.create_table(
        'competition_team',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('competition_id', sa.Integer, nullable=False),
        sa.Column('team_id', sa.Integer, nullable=False),
        sa.Column('points', sa.Integer, nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['competition_id'], ['competition.id']),
        sa.ForeignKeyConstraint(['team_id'], ['team.id']),
    )


def downgrade() -> None:
    op.drop_table('competition_team')

"""Player stat

Revision ID: 2d632bc697e4
Revises: 2705535ab6a9
Create Date: 2023-07-19 08:05:01.971707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d632bc697e4'
down_revision = '2705535ab6a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    statistic_table = op.create_table(
        'statistic',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False),

        sa.PrimaryKeyConstraint('id'),
    )

    op.bulk_insert(
        statistic_table,
        [
            {"name": "Stamina", "active": True},
            {"name": "Strength", "active": True},
            {"name": "Speed", "active": True},
            {"name": "Agility", "active": True},
            {"name": "Power", "active": True},
            {"name": "Balance", "active": True},
            {"name": "Endurance", "active": True},
            {"name": "Reflexes", "active": True},
            {"name": "Accuracy", "active": True},

            {"name": "Points", "active": True},
            {"name": "Run Metres", "active": True},
            {"name": "Tackles", "active": True},
            {"name": "Tackle Busts", "active": True},
            {"name": "Turnovers", "active": True},
            {"name": "Kicks", "active": True},
        ],
    )

    competition_team_player_statistic_table = op.create_table(
        'competition_team_player_statistic',
        sa.Column('id', sa.Integer),
        sa.Column('competition_team_player_id', sa.Integer, nullable=False),
        sa.Column('statistic_id', sa.Integer, nullable=False),
        sa.Column('value', sa.Integer, nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['competition_team_player_id'], ['competition_team_player.id']),
        sa.ForeignKeyConstraint(['statistic_id'], ['statistic.id']),
    )

def downgrade() -> None:
    op.drop_table('competition_team_player_statistic')
    op.drop_table('statistic')

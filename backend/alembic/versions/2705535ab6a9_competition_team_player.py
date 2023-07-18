"""Competition Team Player

Revision ID: 2705535ab6a9
Revises: 6358c80312d4
Create Date: 2023-07-19 07:57:13.560501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2705535ab6a9'
down_revision = '6358c80312d4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    competition_team_player_table = op.create_table(
        'competition_team_player',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('competition_team_id', sa.Integer, nullable=False),
        sa.Column('player_id', sa.Integer, nullable=False),
        sa.Column('position_id', sa.Integer, nullable=False),
        sa.Column('captain', sa.Boolean, nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['competition_team_id'], ['competition_team.id']),
        sa.ForeignKeyConstraint(['player_id'], ['player.id']),
        sa.ForeignKeyConstraint(['position_id'], ['position.id']),
    )


def downgrade() -> None:
    op.drop_table('competition_team_player')

"""Competition game

Revision ID: 12162450720a
Revises: 2d632bc697e4
Create Date: 2023-07-19 21:08:32.890978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12162450720a'
down_revision = '2d632bc697e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    stage_table = op.create_table(
        'stage',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),

        sa.PrimaryKeyConstraint('id'),
    )

    op.bulk_insert(
        stage_table,
        [
            {"name": "Round", "active": True},
            {"name": "Final", "active": True},
            {"name": "Quarter Final", "active": True},
            {"name": "Semi Final", "active": True},
            {"name": "Grand Final", "active": True}
        ]
    )
    competition_game_table = op.create_table(
        'competition_game',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('competition_id', sa.Integer, nullable=False),
        sa.Column('round', sa.Integer, nullable=False),
        sa.Column('game_number', sa.Integer, nullable=False),
        sa.Column('stage_id', sa.Integer, nullable=False),
        sa.Column('home_team_id', sa.Integer, nullable=False),
        sa.Column('home_score', sa.Integer, nullable=False),
        sa.Column('away_team_id', sa.Integer, nullable=False),
        sa.Column('away_score', sa.Integer, nullable=False),
        sa.Column('stadium_id', sa.Integer, nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['competition_id'], ['competition.id']),
        sa.ForeignKeyConstraint(['stage_id'], ['stage.id']),
        sa.ForeignKeyConstraint(['home_team_id'], ['team.id']),
        sa.ForeignKeyConstraint(['away_team_id'], ['team.id']),
        sa.ForeignKeyConstraint(['stadium_id'], ['team.id']),
    )


def downgrade() -> None:
    op.drop_table('competition_game')
    op.drop_table('stage')


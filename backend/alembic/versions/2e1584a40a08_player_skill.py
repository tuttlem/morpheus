"""Player skill

Revision ID: 2e1584a40a08
Revises: 4d1132b3fbd4
Create Date: 2023-07-19 06:42:25.487762

"""
import random

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '2e1584a40a08'
down_revision = '4d1132b3fbd4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    player_skill_table = op.create_table(
        'player_skill',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('player_id', sa.Integer, nullable=False),
        sa.Column('skill_id', sa.Integer, nullable=False),
        sa.Column('level', sa.Integer, nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['player_id'], ['player.id']),
        sa.ForeignKeyConstraint(['skill_id'], ['skill.id']),
    )

    conn = op.get_bind()
    players = list(conn.execute(text('SELECT id FROM player')))
    skills = list(conn.execute(text('SELECT id FROM skill')))

    data = []
    for player in players:
        for skill in skills:
            data.append({
                "player_id": player.id,
                "skill_id": skill.id,
                "level": 40 + random.randint(10, 55),
            })

    op.bulk_insert(
        player_skill_table,
        data,
    )


def downgrade() -> None:
    op.drop_table('player_skill')

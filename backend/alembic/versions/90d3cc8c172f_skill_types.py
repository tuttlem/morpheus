"""Skill types

Revision ID: 90d3cc8c172f
Revises: 703bddb56bfc
Create Date: 2023-07-18 07:55:10.505929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d3cc8c172f'
down_revision = '703bddb56bfc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    skill_type_table = op.create_table(
        'skill_type',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),

        sa.PrimaryKeyConstraint('id'),
    )

    op.bulk_insert(
        skill_type_table,
        [
            {"name": "Running", "active": True},
            {"name": "Passing", "active": True},
            {"name": "Tackling", "active": True},
            {"name": "Contact", "active": True},
            {"name": "General Kicking", "active": True},
            {"name": "Goal Kicking", "active": True},
        ],
    )


def downgrade() -> None:
    op.drop_table('skill_type')


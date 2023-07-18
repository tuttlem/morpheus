"""Position types

Revision ID: 703bddb56bfc
Revises: 2700e345aa88
Create Date: 2023-07-18 07:54:44.058224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '703bddb56bfc'
down_revision = '2700e345aa88'
branch_labels = None
depends_on = None


def upgrade() -> None:
    position_type_table = op.create_table(
        'position_type',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False, default=True),

        sa.PrimaryKeyConstraint('id'),
    )

    op.bulk_insert(
        position_type_table,
        [
            {"name": "Loose-head Prop", "active": True},
            {"name": "Front Row Forward", "active": True},
            {"name": "Hooker", "active": True},
            {"name": "Tight-head Prop", "active": True},
            {"name": "Lock", "active": True},
            {"name": "Second Row Forward", "active": True},
            {"name": "Blindside Flanker", "active": True},
            {"name": "Openside Flanker", "active": True},
            {"name": "Number 8", "active": True},
            {"name": "Lock Forward", "active": True},
            {"name": "Scrum Half", "active": True},
            {"name": "Half Back", "active": True},
            {"name": "Fly Half", "active": True},
            {"name": "Five Eighth", "active": True},
            {"name": "Left Wing", "active": True},
            {"name": "Inside Centre", "active": True},
            {"name": "Outside Centre", "active": True},
            {"name": "Right Wing", "active": True},
            {"name": "Full Back", "active": True},
        ],
    )


def downgrade() -> None:
    op.drop_table('position_type')


"""Create stadiums

Revision ID: defc1aa64f94
Revises: 
Create Date: 2023-07-15 13:32:43.361167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'defc1aa64f94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    stadium_table = op.create_table(
        'stadium',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('location', sa.String(80), nullable=False),
        sa.Column('image', sa.String(80), nullable=False),

        sa.PrimaryKeyConstraint('id'),
    )

    op.bulk_insert(
        stadium_table,
        [
            {"name": "The Roaring Lion's Den", "location": "Cape Town, South Africa", "image": "1.png"},
            {"name": "The Emerald Isle", "location": "Dublin, Ireland", "image": "2.png"},
            {"name": "The Silver Bullet", "location": "Sydney, Australia", "image": "3.png"},
            {"name": "The Red Dragon's Lair", "location": "Cardiff, Wales", "image": "4.png"},
            {"name": "The Maple Leaf Stadium", "location": "Toronto, Canada", "image": "5.png"},
            {"name": "The Rising Sun Stadium", "location": "Tokyo, Japan", "image": "6.png"},
            {"name": "The Golden Gate Stadium", "location": "San Francisco, USA", "image": "7.png"},
            {"name": "The Copacabana Stadium", "location": "Rio de Janeiro, Brazil", "image": "8.png"},
            {"name": "The Great Wall Stadium", "location": "Beijing, China", "image": "9.png"},
            {"name": "The Hallowed Ground", "location": "Edinburgh, Scotland", "image": "10.png"},
            {"name": "The House of Pain", "location": "Limerick, Ireland", "image": "11.png"},
            {"name": "The Fortress", "location": "Pretoria, South Africa", "image": "12.png"},
            {"name": "The Volcano", "location": "Auckland, New Zealand", "image": "13.png"},
            {"name": "The Temple of Thunder", "location": "Melbourne, Australia", "image": "14.png"},
            {"name": "The Maracanã", "location": "Rio de Janeiro, Brazil", "image": "15.png"},
            {"name": "The Colosseum", "location": "Rome, Italy", "image": "16.png"},
            {"name": "The Pyramids", "location": "Giza, Egypt", "image": "17.png"}
        ],
    )


def downgrade() -> None:
    op.drop_table('stadium')

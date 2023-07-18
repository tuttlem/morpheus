"""Teams

Revision ID: 0a8524eaaf80
Revises: 8fe6b610f356
Create Date: 2023-07-18 21:00:15.836222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8524eaaf80'
down_revision = '8fe6b610f356'
branch_labels = None
depends_on = None


def upgrade() -> None:
    team_table = op.create_table(
        'team',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String(80), nullable=False),
        sa.Column('home_stadium_id', sa.Integer, nullable=False),
        sa.Column('image', sa.String(80), nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['home_stadium_id'], ['stadium.id']),
    )

    op.bulk_insert(
        team_table,
        [
            {"name": "Maulers", "home_stadium_id": 1, "image": "1.png"},
            {"name": "Raging Bulls", "home_stadium_id": 2, "image": "2.png"},
            {"name": "Black Stallions", "home_stadium_id": 3, "image": "3.png"},
            {"name": "Blue Devils", "home_stadium_id": 4, "image": "4.png"},
            {"name": "Crimson Tide", "home_stadium_id": 5, "image": "5.png"},
            {"name": "Green Machine", "home_stadium_id": 6, "image": "6.png"},
            {"name": "Red Devils", "home_stadium_id": 7, "image": "7.png"},
            {"name": "White Sharks", "home_stadium_id": 8, "image": "8.png"},
            {"name": "Mighty Oaks", "home_stadium_id": 9, "image": "9.png"},
            {"name": "Raging Rhinos", "home_stadium_id": 10, "image": "10.png"},
            {"name": "Fighting Irish", "home_stadium_id": 11, "image": "11.png"},
            {"name": "Flying Eagles", "home_stadium_id": 12, "image": "12.png"},
            {"name": "Fighting Scots", "home_stadium_id": 13, "image": "13.png"},
            {"name": "Golden Bears", "home_stadium_id": 14, "image": "14.png"},
            {"name": "Purple Cobras", "home_stadium_id": 15, "image": "15.png"},
            {"name": "Silver Bullets", "home_stadium_id": 16, "image": "16.png"},
            {"name": "Thundering Herd", "home_stadium_id": 17, "image": "17.png"},
            {"name": "Wild Boars", "home_stadium_id": 1, "image": "18.png"},
            {"name": "Charging Buffaloes", "home_stadium_id": 2, "image": "19.png"},
            {"name": "Crushing Canines", "home_stadium_id": 3, "image": "20.png"},
            {"name": "Devastating Dragons", "home_stadium_id": 4, "image": "21.png"},
            {"name": "Ferocious Tigers", "home_stadium_id": 5, "image": "22.png"},
            {"name": "Relentless Rhinos", "home_stadium_id": 6, "image": "23.png"},
            {"name": "Savage Sharks", "home_stadium_id": 7, "image": "24.png"},
            {"name": "Tackling Titans", "home_stadium_id": 8, "image": "25.png"},
            {"name": "Unstoppable Wolverines", "home_stadium_id": 9, "image": "26.png"},
            {"name": "Winged Eagles", "home_stadium_id": 10, "image": "27.png"},
            {"name": "Blitzing Bulls", "home_stadium_id": 11, "image": "28.png"},
            {"name": "Crushing Crusaders", "home_stadium_id": 12, "image": "29.png"},
            {"name": "Dauntless Dragons", "home_stadium_id": 13, "image": "30.png"},
            {"name": "Fearless Falcons", "home_stadium_id": 14, "image": "31.png"},
            {"name": "Flying Foxes", "home_stadium_id": 15, "image": "32.png"},
            {"name": "Mighty Maulers", "home_stadium_id": 16, "image": "33.png"},
            {"name": "Relentless Rhinos", "home_stadium_id": 17, "image": "34.png"},
            {"name": "Savage Sharks", "home_stadium_id": 1, "image": "35.png"},
            {"name": "Tackling Titans", "home_stadium_id": 2, "image": "36.png"},
            {"name": "Unstoppable Wolverines", "home_stadium_id": 3, "image": "37.png"},
            {"name": "Winged Eagles", "home_stadium_id": 4, "image": "38.png"},
            {"name": "Charging Buffaloes", "home_stadium_id": 5, "image": "39.png"},
            {"name": "Crushing Canines", "home_stadium_id": 6, "image": "40.png"},
            {"name": "Devastating Dragons", "home_stadium_id": 7, "image": "41.png"},
            {"name": "Ferocious Tigers", "home_stadium_id": 8, "image": "42.png"},
        ],
    )


def downgrade() -> None:
    op.drop_table('team')

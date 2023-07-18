"""Players

Revision ID: 4d1132b3fbd4
Revises: 0a8524eaaf80
Create Date: 2023-07-18 21:43:40.204734

"""
import random

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4d1132b3fbd4'
down_revision = '0a8524eaaf80'
branch_labels = None
depends_on = None


def upgrade() -> None:
    player_table = op.create_table(
        'player',
        sa.Column('id', sa.Integer),
        sa.Column('first_name', sa.String(80), nullable=False),
        sa.Column('last_name', sa.String(80), nullable=False),
        sa.Column('location', sa.String(80), nullable=False),
        sa.Column('image', sa.String(80), nullable=False),

        sa.PrimaryKeyConstraint('id'),
    )

    data = []
    for i in range(50):
        first_name = random.choice([
            "Alexander", "Anthony", "Benjamin", "Christopher",
            "Daniel", "David", "Ethan", "Gabriel", "Henry", "Jacob",
            "James", "John", "Jonathan", "Joshua", "Matthew", "Michael",
            "Nathan", "Nicholas", "Noah", "Oliver", "Owen", "Peter", "Ryan",
            "Samuel", "Sean", "Thomas", "William"
        ])
        last_name = random.choice([
            "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Wilson",
            "Thompson", "Jackson", "White", "Garcia", "Martinez", "Rodriguez",
            "Lee", "Walker", "Hernandez", "Gonzalez", "Campbell", "Parker",
            "Evans", "Martin", "Thompson", "White", "Moore", "Green", "Harris",
            "Clark", "Robinson", "Lewis", "Scott", "Turner", "Morgan", "Bell"
        ])
        location = random.choice([
            "London, UK", "New York, USA", "Paris, France", "Tokyo, Japan", "Sydney, Australia",
            "Manchester, England", "Madrid, Spain", "Rome, Italy", "Berlin, Germany",
        ])
        image = f"{i + 1}.png"

        data.append({
            "first_name": first_name,
            "last_name": last_name,
            "location": location,
            "image": image,
        })

    op.bulk_insert(
        player_table,
        data,
    )


def downgrade() -> None:
    op.drop_table('player')

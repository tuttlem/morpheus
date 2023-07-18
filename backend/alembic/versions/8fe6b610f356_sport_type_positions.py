"""Sport type positions

Revision ID: 8fe6b610f356
Revises: 90d3cc8c172f
Create Date: 2023-07-18 08:10:22.400596

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Executable, text

# revision identifiers, used by Alembic.
revision = '8fe6b610f356'
down_revision = '90d3cc8c172f'
branch_labels = None
depends_on = None


def safe_get(list, key, default=None):
    """
    Get a value out of a list safely, using filter.

    Args:
        list: The list to search.
        key: The key to search for.
        default: The default value to return if the key is not found.

    Returns:
        The value associated with the key, or the default value if the key is not found.
    """

    return next(filter(lambda x: x.name == key, list), default).id

def upgrade() -> None:
    sport_types_position_type_table = op.create_table(
        'sport_type_position_type',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('sport_type_id', sa.Integer, nullable=False),
        sa.Column('position_type_id', sa.Integer, nullable=False),
        sa.Column('number', sa.Integer, nullable=False),

        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['sport_type_id'], ['sport_type.id']),
        sa.ForeignKeyConstraint(['position_type_id'], ['position_type.id']),
    )

    conn = op.get_bind()
    sport_types = list(conn.execute(text('SELECT id, name FROM sport_type')))
    position_types = list(conn.execute(text('SELECT id, name FROM position_type')))

    ru_id = safe_get(sport_types, 'Rugby Union')
    rl_id = safe_get(sport_types, 'Rugby League')

    lhp_id = safe_get(position_types, 'Loose-head Prop')
    frf_id = safe_get(position_types, 'Front Row Forward')
    hkr_id = safe_get(position_types, 'Hooker')
    thp_id = safe_get(position_types, 'Tight-head Prop')
    lck_id = safe_get(position_types, 'Lock')
    srf_id = safe_get(position_types, 'Second Row Forward')
    bsf_id = safe_get(position_types, 'Blindside Flanker')
    osf_id = safe_get(position_types, 'Openside Flanker')
    no8_id = safe_get(position_types, 'Number 8')
    lkf_id = safe_get(position_types, 'Lock Forward'),
    sch_id = safe_get(position_types, 'Scrum Half')
    hfb_id = safe_get(position_types, 'Half Back')
    fhf_id = safe_get(position_types, 'Fly Half')
    fet_id = safe_get(position_types, 'Five Eighth')
    lfw_id = safe_get(position_types, 'Left Wing')
    isc_id = safe_get(position_types, 'Inside Centre')
    oss_id = safe_get(position_types, 'Outside Centre')
    rtw_id = safe_get(position_types, 'Right Wing')
    fbk_id = safe_get(position_types, 'Full Back')

    op.bulk_insert(
        sport_types_position_type_table,
        [
            {"sport_type_id": ru_id, "position_type_id": lhp_id, "number": 1},
            {"sport_type_id": ru_id, "position_type_id": hkr_id, "number": 2},
            {"sport_type_id": ru_id, "position_type_id": thp_id, "number": 3},
            {"sport_type_id": ru_id, "position_type_id": lck_id, "number": 4},
            {"sport_type_id": ru_id, "position_type_id": lck_id, "number": 5},
            {"sport_type_id": ru_id, "position_type_id": bsf_id, "number": 6},
            {"sport_type_id": ru_id, "position_type_id": osf_id, "number": 7},
            {"sport_type_id": ru_id, "position_type_id": no8_id, "number": 8},
            {"sport_type_id": ru_id, "position_type_id": sch_id, "number": 9},
            {"sport_type_id": ru_id, "position_type_id": fhf_id, "number": 10},
            {"sport_type_id": ru_id, "position_type_id": lfw_id, "number": 11},
            {"sport_type_id": ru_id, "position_type_id": isc_id, "number": 12},
            {"sport_type_id": ru_id, "position_type_id": oss_id, "number": 13},
            {"sport_type_id": ru_id, "position_type_id": rtw_id, "number": 14},
            {"sport_type_id": ru_id, "position_type_id": fbk_id, "number": 15},

            {"sport_type_id": rl_id, "position_type_id": fbk_id, "number": 1},
            {"sport_type_id": rl_id, "position_type_id": rtw_id, "number": 2},
            {"sport_type_id": rl_id, "position_type_id": oss_id, "number": 3},
            {"sport_type_id": rl_id, "position_type_id": isc_id, "number": 4},
            {"sport_type_id": rl_id, "position_type_id": lfw_id, "number": 5},
            {"sport_type_id": rl_id, "position_type_id": fet_id, "number": 6},
            {"sport_type_id": rl_id, "position_type_id": hfb_id, "number": 7},
            {"sport_type_id": rl_id, "position_type_id": frf_id, "number": 8},
            {"sport_type_id": rl_id, "position_type_id": hkr_id, "number": 9},
            {"sport_type_id": rl_id, "position_type_id": frf_id, "number": 10},
            {"sport_type_id": rl_id, "position_type_id": srf_id, "number": 11},
            {"sport_type_id": rl_id, "position_type_id": srf_id, "number": 12},
            {"sport_type_id": rl_id, "position_type_id": lkf_id, "number": 13},
        ],
    )


def downgrade() -> None:
    op.drop_table('sport_type_position_type')
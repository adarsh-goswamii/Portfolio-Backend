"""add leetcode to platform enum

Revision ID: 2f5b332d387f
Revises: efeee8d296a1
Create Date: 2026-04-18 19:19:01.447000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '2f5b332d387f'
down_revision: Union[str, None] = 'efeee8d296a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TYPE platform ADD VALUE IF NOT EXISTS 'LEETCODE'")


def downgrade() -> None:
    pass

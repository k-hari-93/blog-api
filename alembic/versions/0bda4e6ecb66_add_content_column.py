"""add content column

Revision ID: 0bda4e6ecb66
Revises: 4f72ff1c15d3
Create Date: 2022-09-25 20:30:10.303806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bda4e6ecb66'
down_revision = '4f72ff1c15d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")

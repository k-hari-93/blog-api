"""create posts table

Revision ID: 4f72ff1c15d3
Revises: 
Create Date: 2022-09-25 20:16:43.221636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f72ff1c15d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.INTEGER, nullable=False, primary_key=True),
                    sa.Column("title", sa.String, nullable=False))


def downgrade() -> None:
    op.drop_table("posts")

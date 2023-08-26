"""add last columns to posts table

Revision ID: 2705ffc4fe0a
Revises: 4c56040ed9f4
Create Date: 2022-09-28 22:56:55.909614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2705ffc4fe0a'
down_revision = '4c56040ed9f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.BOOLEAN, 
                                     nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text("NOW()")))

def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")

"""add user table

Revision ID: 8eb7083fa98c
Revises: 0bda4e6ecb66
Create Date: 2022-09-25 20:36:28.203374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8eb7083fa98c'
down_revision = '0bda4e6ecb66'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.INTEGER, nullable=False),
                    sa.Column("email", sa.String, nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
    )

def downgrade() -> None:
    op.drop_table("users")

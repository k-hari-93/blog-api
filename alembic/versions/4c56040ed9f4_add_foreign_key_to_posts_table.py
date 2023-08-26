"""add foreign key to posts table

Revision ID: 4c56040ed9f4
Revises: 8eb7083fa98c
Create Date: 2022-09-28 22:49:16.475383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c56040ed9f4'
down_revision = '8eb7083fa98c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.INTEGER, nullable=False))
    op.create_foreign_key("posts_users_fkey", source_table="posts",
                          referent_table="users", local_cols=["owner_id"], 
                          remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fkey", "posts")
    op.drop_column("posts", "owner_id")

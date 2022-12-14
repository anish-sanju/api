"""Initial migration.

Revision ID: fa3e4dd3a613
Revises: 
Create Date: 2022-12-19 23:58:11.228819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa3e4dd3a613'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('admin_name', sa.String(length=30), nullable=False),
    sa.Column('admin_email', sa.String(length=30), nullable=False),
    sa.Column('admin_password', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('admin_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###

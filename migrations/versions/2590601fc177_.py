"""empty message

Revision ID: 2590601fc177
Revises: 413fbf026eca
Create Date: 2019-09-13 17:18:48.487469

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2590601fc177'
down_revision = '413fbf026eca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('events', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.alter_column('events', 'time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###

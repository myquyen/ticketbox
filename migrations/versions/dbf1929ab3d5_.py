"""empty message

Revision ID: dbf1929ab3d5
Revises: 2590601fc177
Create Date: 2019-09-13 18:24:18.279661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf1929ab3d5'
down_revision = '2590601fc177'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket__type')
    op.drop_column('events', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_table('ticket__type',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='ticket__type_event_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='ticket__type_pkey')
    )
    # ### end Alembic commands ###

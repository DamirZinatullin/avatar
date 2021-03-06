"""empty message

Revision ID: 435fceea3e0c
Revises: a6cd024e6680
Create Date: 2019-11-18 20:42:36.472656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '435fceea3e0c'
down_revision = 'a6cd024e6680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('fabric', sa.Column('color_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'fabric', 'color', ['color_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fabric', type_='foreignkey')
    op.drop_column('fabric', 'color_id')
    op.drop_table('color')
    # ### end Alembic commands ###

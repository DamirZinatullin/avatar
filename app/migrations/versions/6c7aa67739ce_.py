"""empty message

Revision ID: 6c7aa67739ce
Revises: 5f820bd3e77f
Create Date: 2019-12-02 22:20:30.364791

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6c7aa67739ce'
down_revision = '5f820bd3e77f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('shop', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'shop', 'city', ['city_id'], ['id'])
    op.drop_column('shop', 'city')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', mysql.VARCHAR(collation='utf8_unicode_ci', length=200), nullable=True))
    op.add_column('shop', sa.Column('city', mysql.VARCHAR(collation='utf8_unicode_ci', length=40), nullable=True))
    op.drop_constraint(None, 'shop', type_='foreignkey')
    op.drop_column('shop', 'city_id')
    op.drop_table('city')
    # ### end Alembic commands ###

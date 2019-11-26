"""empty message

Revision ID: 2bdbbc3443f4
Revises: 9c985af0eef9
Create Date: 2019-11-26 21:43:23.196753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bdbbc3443f4'
down_revision = '9c985af0eef9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=60), nullable=True))
    op.add_column('user', sa.Column('phone', sa.String(length=20), nullable=True))
    op.add_column('user', sa.Column('surname', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'surname')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###

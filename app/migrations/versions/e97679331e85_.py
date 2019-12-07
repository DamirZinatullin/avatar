"""empty message

Revision ID: e97679331e85
Revises: 6c7aa67739ce
Create Date: 2019-12-04 22:04:45.572764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e97679331e85'
down_revision = '6c7aa67739ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('suit', sa.Column('gender', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('suit', 'gender')
    # ### end Alembic commands ###

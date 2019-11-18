"""empty message

Revision ID: 7e133db55bd8
Revises: 64de7c70e313
Create Date: 2019-11-18 21:08:24.973948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e133db55bd8'
down_revision = '64de7c70e313'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tailor', sa.Column('role_id', sa.Integer(), nullable=True))
    op.add_column('tailor', sa.Column('status_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tailor', 'status', ['status_id'], ['id'])
    op.create_foreign_key(None, 'tailor', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tailor', type_='foreignkey')
    op.drop_constraint(None, 'tailor', type_='foreignkey')
    op.drop_column('tailor', 'status_id')
    op.drop_column('tailor', 'role_id')
    # ### end Alembic commands ###

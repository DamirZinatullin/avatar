"""empty message

Revision ID: 95135a8da541
Revises: 69c220294cb8
Create Date: 2019-11-18 21:34:43.201757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95135a8da541'
down_revision = '69c220294cb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('surname', sa.String(length=140), nullable=True),
    sa.Column('patronymic', sa.String(length=140), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=140), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['status.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('manager')
    # ### end Alembic commands ###

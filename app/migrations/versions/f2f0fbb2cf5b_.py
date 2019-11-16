"""empty message

Revision ID: f2f0fbb2cf5b
Revises: d26674e7317e
Create Date: 2019-11-16 15:03:41.330672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f0fbb2cf5b'
down_revision = 'd26674e7317e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('height', sa.DECIMAL(precision=9, scale=2), nullable=True),
    sa.Column('weight', sa.DECIMAL(precision=9, scale=2), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('data', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('suit', sa.Column('scan_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'suit', 'scan', ['scan_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'suit', type_='foreignkey')
    op.drop_column('suit', 'scan_id')
    op.drop_table('scan')
    # ### end Alembic commands ###
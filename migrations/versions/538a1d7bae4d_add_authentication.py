"""add authentication

Revision ID: 538a1d7bae4d
Revises: 7c81f0aea20d
Create Date: 2023-01-24 12:11:35.010393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '538a1d7bae4d'
down_revision = '7c81f0aea20d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=64), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.add_column(sa.Column('confirmed', sa.Boolean(), nullable=True))
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_email'))
        batch_op.drop_column('confirmed')
        batch_op.drop_column('password_hash')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
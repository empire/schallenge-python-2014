"""empty message

Revision ID: 28fed97b29ba
Revises: dcd4992a7ca
Create Date: 2014-08-12 12:43:17.695820

"""

# revision identifiers, used by Alembic.
revision = '28fed97b29ba'
down_revision = 'dcd4992a7ca'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('registered_at', sa.DateTime(), nullable=True))
    op.add_column('accounts', sa.Column('salt', sa.String(length=200), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'salt')
    op.drop_column('accounts', 'registered_at')
    ### end Alembic commands ###

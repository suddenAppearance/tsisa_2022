"""Add block table

Revision ID: be5bdfc4fed3
Revises: 
Create Date: 2022-09-26 19:32:19.006986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be5bdfc4fed3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block',
    sa.Column('index', sa.BigInteger(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('previous_hash', sa.String(), nullable=True),
    sa.Column('sign', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('index')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('block')
    # ### end Alembic commands ###

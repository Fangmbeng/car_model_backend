"""empty message

Revision ID: 744354fa639e
Revises: 7aeb3fd2f551
Create Date: 2023-05-30 09:33:02.425615

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '744354fa639e'
down_revision = '7aeb3fd2f551'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_token')
        batch_op.drop_column('token_expiration')
        batch_op.drop_column('token')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('token_expiration', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_token'), ['token'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_token'))
        batch_op.drop_column('token_expiration')
        batch_op.drop_column('token')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('token_expiration', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.create_index('ix_post_token', ['token'], unique=False)

    # ### end Alembic commands ###

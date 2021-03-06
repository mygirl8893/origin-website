"""empty message

Revision ID: 2627b59a3f8b
Revises: 80a54752ff01
Create Date: 2018-02-09 13:08:39.326285

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2627b59a3f8b'
down_revision = '75a6937030ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fullcontact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('fullcontact_response', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('github_handle', sa.String(length=255), nullable=True),
    sa.Column('angellist_handle', sa.String(length=255), nullable=True),
    sa.Column('twitter_handle', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fullcontact_email'), 'fullcontact', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fullcontact_email'), table_name='fullcontact')
    op.drop_table('fullcontact')
    # ### end Alembic commands ###

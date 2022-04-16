"""create-user-table

Revision ID: 0519f2769ca3
Revises: 
Create Date: 2022-04-16 15:21:05.200603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0519f2769ca3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('catchPhrase', sa.String(), nullable=True),
    sa.Column('bs', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_companies_id'), 'companies', ['id'], unique=False)
    op.create_table('geo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lat', sa.String(), nullable=True),
    sa.Column('lng', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_geo_id'), 'geo', ['id'], unique=False)
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('suite', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('zipcode', sa.String(), nullable=True),
    sa.Column('geo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['geo_id'], ['geo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_addresses_id'), 'addresses', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_addresses_id'), table_name='addresses')
    op.drop_table('addresses')
    op.drop_index(op.f('ix_geo_id'), table_name='geo')
    op.drop_table('geo')
    op.drop_index(op.f('ix_companies_id'), table_name='companies')
    op.drop_table('companies')
    # ### end Alembic commands ###

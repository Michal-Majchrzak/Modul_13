"""tables readers and inventory units

Revision ID: 6f71149add9a
Revises: 69da45f53d35
Create Date: 2021-03-11 09:14:21.527259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f71149add9a'
down_revision = '69da45f53d35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reader',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('lastname', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reader_lastname'), 'reader', ['lastname'], unique=False)
    op.create_index(op.f('ix_reader_name'), 'reader', ['name'], unique=False)
    op.create_table('inventory_unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('reader_id', sa.Integer(), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('last_borrow_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['reader_id'], ['reader.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_unit_last_borrow_date'), 'inventory_unit', ['last_borrow_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inventory_unit_last_borrow_date'), table_name='inventory_unit')
    op.drop_table('inventory_unit')
    op.drop_index(op.f('ix_reader_name'), table_name='reader')
    op.drop_index(op.f('ix_reader_lastname'), table_name='reader')
    op.drop_table('reader')
    # ### end Alembic commands ###

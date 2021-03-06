"""empty message

Revision ID: 30996f3c4a50
Revises: 44623edc0961
Create Date: 2021-03-13 21:53:51.170095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30996f3c4a50'
down_revision = '44623edc0961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_author',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], )
    )
    op.drop_table('book_details')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_details',
    sa.Column('book_id', sa.INTEGER(), nullable=False),
    sa.Column('author_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'author_id')
    )
    op.drop_table('book_author')
    # ### end Alembic commands ###

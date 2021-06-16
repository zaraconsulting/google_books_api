"""update

Revision ID: d204d19a5bc2
Revises: 9f99d1ededb1
Create Date: 2021-06-15 20:36:50.335221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd204d19a5bc2'
down_revision = '9f99d1ededb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('book', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'author', ['author_id'], ['id'])
    op.drop_column('book', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'author_id')
    op.drop_table('author')
    # ### end Alembic commands ###

"""make artist name unique

Revision ID: eca42a3e42c2
Revises: aba99ddc1146
Create Date: 2020-05-03 21:33:11.284731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca42a3e42c2'
down_revision = 'aba99ddc1146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###

"""Edited database

Revision ID: 88890d00582f
Revises: 507733729f23
Create Date: 2023-06-08 08:57:47.407918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88890d00582f'
down_revision = '507733729f23'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'destinations_new',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('image', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('visit_url', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Specify the column names in the SELECT statement
    op.execute("""
        INSERT INTO destinations_new (id, name, image, description, category, location, visit_url)
        SELECT id, name, image, description, category, location, visit_url FROM destinations
    """)

    op.drop_table('destinations')


def downgrade():
    op.create_table(
        'destinations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('image', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('visit_url', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.execute("""
        INSERT INTO destinations (id, name, image, description, category, location, visit_url)
        SELECT id, name, image, description, category, location, visit_url FROM destinations_new
    """)

    op.drop_table('destinations_new')
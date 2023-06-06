"""Added association object

Revision ID: 769167772583
Revises: 507733729f23
Create Date: 2023-06-06 15:10:53.539408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '769167772583'
down_revision = '507733729f23'
branch_labels = None
depends_on = None

def upgrade():
    # Drop the foreign key constraint
    with op.batch_alter_table('destinations') as batch_op:
        batch_op.drop_constraint('destination_id', type_='foreignkey')

    # Create a temporary table without the constraint
    op.create_table(
        'temp_destinations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('image', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('visit_url', sa.String(), nullable=True),
        sa.Column('interested', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the original table to the temporary table
    op.execute('INSERT INTO temp_destinations SELECT * FROM destinations')

    # Drop the original table
    op.drop_table('destinations')

    # Rename the temporary table to the original table name
    op.rename_table('temp_destinations', 'destinations')

    # Recreate the foreign key constraint
    with op.batch_alter_table('destinations') as batch_op:
        batch_op.create_foreign_key('destinatrion_id', 'destinations', 'users_destinations', ['destination_id'], ['id'])


def downgrade():
    # Drop the foreign key constraint
    with op.batch_alter_table('destinations') as batch_op:
        batch_op.drop_constraint('destination_id', type_='foreignkey')

    # Create a temporary table without the constraint
    op.create_table(
        'temp_destinations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('image', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('visit_url', sa.String(), nullable=True),
        sa.Column('interested', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Copy data from the original table to the temporary table
    op.execute('INSERT INTO temp_destinations SELECT * FROM destinations')

    # Drop the original table
    op.drop_table('destinations')

    # Rename the temporary table to the original table name
    op.rename_table('temp_destinations', 'destinations')

    # Recreate the foreign key constraint
    with op.batch_alter_table('destinations') as batch_op:
        batch_op.create_foreign_key('destination_id', 'destinations', 'users_destinations', ['destination_id'], ['id'])


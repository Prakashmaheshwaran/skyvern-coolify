"""add_engine_to_workflow_run_block

Revision ID: 2be3e0ba85ff
Revises: 2c6b27e8e961
Create Date: 2025-06-17 07:23:13.753617+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2be3e0ba85ff"
down_revision: Union[str, None] = "2c6b27e8e961"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("workflow_run_blocks", sa.Column("engine", sa.String(), nullable=True))
    op.create_index(op.f("ix_workflow_run_blocks_task_id"), "workflow_run_blocks", ["task_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_workflow_run_blocks_task_id"), table_name="workflow_run_blocks")
    op.drop_column("workflow_run_blocks", "engine")
    # ### end Alembic commands ###

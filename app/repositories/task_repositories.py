from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task_model import NewTask
from app.schemas.task_schema import TaskSchema, TaskUpdate
from sqlalchemy import select

async def get_tasks(db : AsyncSession):
    result = await db.execute(select(NewTask))
    return result.scalars().all()

async def get_task_by_id(db : AsyncSession, task_id : int):
    result = await db.execute(select(NewTask).where(NewTask.id == task_id))
    return result.scalar_one_or_none()

async def create_task(db: AsyncSession, task: TaskSchema):
    db_task = NewTask(
        user_id = task.user_id,
        description = task.description,
    )

    db.add(db_task)

    await db.commit()
    await db.refresh(db_task)
    return db_task

async def update_task(db : AsyncSession, Task_data : TaskUpdate):
    result = await db.execute(select(NewTask).where(NewTask.id == Task_data.id))
    task = result.scalar_one_or_none()

    task.description = Task_data.description
    task.user_id = Task_data.user_id

    await db.commit()
    await db.refresh(task)

    return task

async def delete_task(db : AsyncSession, task_id : int):
    result = await db.execute(select(NewTask).where(NewTask.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        return None
    
    await db.delete(task)
    await db.refresh()

    return task
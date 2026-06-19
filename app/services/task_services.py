from fastapi import HTTPException
from app.repositories.task_repositories import (
    get_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task,
)

async def get_all_tasks(db):
    result_from_db = await get_tasks(db)
    return result_from_db

async def get_one_task(db, task_id : int):
    result_from_db = await get_task_by_id(db, task_id)

    if not result_from_db:
        raise HTTPException(status_code=404, detail="Task not found!")

    return result_from_db

async def create_new_task(db, new_task):
    if not new_task.name.strip() or new_task.name == "string":
        raise HTTPException(status_code=400, detail="Name is required")
    
    result_from_db = await create_task(db, new_task)

    return result_from_db

async def change_task(db, task_id, task_data):
    if not task_data.name or not task_data.name.strip():
        raise HTTPException(status_code=400, detail="Name is required")
    
    result_from_db = await update_task(db, task_id, task_data)

    if not result_from_db:
        raise HTTPException(status_code=404, detail="Task not found!")
    
    return result_from_db

async def remove_task(db, task_id):
    result_from_db = await delete_task(db, task_id)

    if not result_from_db:
        raise HTTPException(status_code=404, detail="Task not found!")
    
    return result_from_db
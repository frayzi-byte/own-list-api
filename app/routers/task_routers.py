from fastapi import APIRouter, status, Depends
from app.schemas.task_schema import TaskSchema, TaskUpdate
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.task_services import (
    get_all_tasks,
    get_one_task,
    create_new_task,
    change_task,
    remove_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post("/", response_model=TaskSchema, status_code=status.HTTP_201_CREATED)
async def create(task : TaskSchema, db : AsyncSession = Depends(get_db)):
    return await create_new_task(db, task)

@router.get("/", response_model=list[TaskSchema], status_code=status.HTTP_200_OK)
async def get_all(db : AsyncSession = Depends(get_db)):
    return await get_all_tasks(db)

@router.get("/{task_id}", response_model=TaskSchema, status_code=status.HTTP_200_OK)
async def get_by_id(task_id : int, db : AsyncSession = Depends(get_db)):
   return await get_one_task(db, task_id) 

@router.put("/{task_id}", response_model=TaskSchema, status_code=status.HTTP_200_OK)
async def update(task_id : int, task_data : TaskUpdate, db : AsyncSession = Depends(get_db)):
    return await change_task(db, task_id, task_data)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(task_id : int, db : AsyncSession = Depends(get_db)):
    return await remove_task(db, task_id)

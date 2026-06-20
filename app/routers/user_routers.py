from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserUpdate, UserResponse, UserCreate
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.services.user_services import (
    get_all_users,
    get_one_user,
    create_new_user,
    change_user,
    remove_user,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create(user : UserCreate, db : AsyncSession = Depends(get_db)):
    return await create_new_user(db, user)

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_all(db : AsyncSession = Depends(get_db)):
    return await get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_by_id(user_id : UUID, db : AsyncSession = Depends(get_db)):
   return await get_one_user(db, user_id) 

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update(user_id : UUID, user_data : UserUpdate, db : AsyncSession = Depends(get_db)):
    return await change_user(db, user_id, user_data)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id : UUID, db : AsyncSession = Depends(get_db)):
    return await remove_user(db, user_id)
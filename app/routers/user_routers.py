from fastapi import APIRouter, status, Depends
from app.schemas.user_schema import UserUpdate, UserResponse, UserCreate
from app.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
<<<<<<< HEAD
from app.services.user_services import (
    get_all_users,
    get_one_user,
    create_new_user,
    change_user,
    remove_user,
=======
from app.repositories.user_repositories import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
>>>>>>> bd6d1a79a8de681b93ecb4914fce2b0fe4c7c6c4
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create(user : UserCreate, db : AsyncSession = Depends(get_db)):
<<<<<<< HEAD
    return await create_new_user(db, user)

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_all(db : AsyncSession = Depends(get_db)):
    return await get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_by_id(user_id : int, db : AsyncSession = Depends(get_db)):
   return await get_one_user(db, user_id) 

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update(user_id : int, user_data : UserUpdate, db : AsyncSession = Depends(get_db)):
    return await change_user(db, user_id, user_data)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id : int, db : AsyncSession = Depends(get_db)):
    return await remove_user(db, user_id)
=======
    return await create_user(db, user)

@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
async def get_all(db : AsyncSession = Depends(get_db)):
    return await get_users(db)

@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_by_id(user_id : int, db : AsyncSession = Depends(get_db)):
   return await get_user_by_id(db, user_id) 

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update(user_id : int, user_data : UserUpdate, db : AsyncSession = Depends(get_db)):
    return await update_user(db, user_id, user_data)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id : int, db : AsyncSession = Depends(get_db)):
    return await delete_user(db, user_id)
>>>>>>> bd6d1a79a8de681b93ecb4914fce2b0fe4c7c6c4

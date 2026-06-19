from fastapi import HTTPException
from app.repositories.user_repositories import (
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

async def get_all_users(db):
    result_from_db = await get_users(db)
    return result_from_db

async def get_one_user(db, user_id : int):
    result_from_db = await get_user_by_id(db, user_id)

    if not result_from_db:
        raise HTTPException(status_code=404, detail="User not found!")

    return result_from_db

async def create_new_user(db, new_user):
    if not new_user.username.strip() or new_user.username == "string":
        raise HTTPException(status_code=400, detail="Name is required")
    
    result_from_db = await create_user(db, new_user)

    return result_from_db

async def change_user(db, user_id, user_data):
    if not user_data.username or not user_data.usernamen.strip():
        raise HTTPException(status_code=400, detail="Name is required")
    
    result_from_db = await update_user(db, user_id, user_data)

    if not result_from_db:
        raise HTTPException(status_code=404, detail="User not found!")
    
    return result_from_db

async def remove_user(db, user_id):
    result_from_db = await delete_user(db, user_id)

    if not result_from_db:
        raise HTTPException(status_code=404, detail="User not found!")
    
    return result_from_db
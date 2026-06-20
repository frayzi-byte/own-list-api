from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import NewUser
from app.schemas.user_schema import UserUpdate, UserCreate
from sqlalchemy import select
from app.utils.security import hash_password
from uuid import UUID

async def get_users(db : AsyncSession):
    result = await db.execute(select(NewUser))
    return result.scalars().all()

async def get_user_by_id(db : AsyncSession, user_id : UUID):
    result = await db.execute(select(NewUser).where(NewUser.id == user_id))
    return result.scalar_one_or_none()

async def create_user(db : AsyncSession, User : UserCreate):
    password_hash = hash_password(
        User.password
    )

    db_user = NewUser(
        username = User.username,
        email = User.email,
        password_hash=password_hash
    )

    db.add(db_user)

    await db.commit()
    await db.refresh(db_user)

    return db_user

async def update_user(db : AsyncSession, User_data : UserUpdate):
    result = await db.execute(select(NewUser).where(NewUser.id == User_data.id))
    user = result.scalar_one_or_none()
    if not user:
        return None

    user.username = User_data.username
    user.email = User_data.email

    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(db : AsyncSession, user_id : UUID):
    result = await db.execute(select(NewUser).where(NewUser.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        return None
    
    await db.delete(user)
    await db.commit()

    return user
from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

<<<<<<< HEAD
class UserCreate(BaseModel):
=======
class CreateUserRequest(BaseModel):
>>>>>>> bd6d1a79a8de681b93ecb4914fce2b0fe4c7c6c4
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: str
    email: EmailStr

    password_hash: str
    
class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

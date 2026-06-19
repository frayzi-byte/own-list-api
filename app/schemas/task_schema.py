from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TaskSchema(BaseModel):
    id: UUID
    user_id: UUID

    description: str

    start_date: datetime | None
    end_date: datetime | None

    completed: bool

    created_at: datetime
    updated_at: datetime

class TaskUpdate(BaseModel):
    user_id: UUID

    description: str
    completed: bool
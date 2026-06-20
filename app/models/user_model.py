from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy import UUID as SQLAlchemyUUID
from sqlalchemy.sql import func
import uuid

from app.db import Base

class NewUser(Base):
    __tablename__ = "users"
    
    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
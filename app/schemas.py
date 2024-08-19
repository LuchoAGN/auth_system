from pydantic import BaseModel
from datetime import datetime
from typing import Optional 
from app.models import UserRole

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_active: bool
    role: UserRole
    created_at: datetime
    updated_at: Optional[datetime] 

    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserInDB(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.now)
    total_urls: int = 0
    daily_usage: int = 0
    is_subscribed: bool = False

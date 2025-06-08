from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import time

class UserInDB(BaseModel):
    email: EmailStr
    password: str
    # created_at: datetime = Field(default_factory=datetime.now)
    created_at: int = Field(default_factory=lambda: int(time.time()))
    total_urls: int = 0
    daily_usage: int = 0
    is_subscribed: bool = False

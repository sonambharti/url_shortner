from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import time

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UpdateUserRequest(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    # created_at: datetime = Field(default_factory=int(time.time()))
    created_at: int = Field(default_factory=lambda: int(time.time()))
    is_subscribed: Optional[bool] = False
    daily_usage: Optional[int] = 0
    total_urls: Optional[int] = 0
from fastapi import APIRouter, HTTPException
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import register_user, login_user
from app.core.security import hash_password
from app.db.mongodb import users_collection

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(data: RegisterRequest):
    try:
        user_data = {
            "email": data.email,
            "password": hash_password(data.password),
            "is_subscribed": False,
            "daily_usage": 0,
            "total_urls": 0
        }
        users_collection.insert_one(user_data)
        return register_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    try:
        return login_user(data)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

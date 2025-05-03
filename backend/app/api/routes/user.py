from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/me")
def read_current_user(user: dict = Depends(get_current_user)):
    return {
        "email": user["email"],
        "is_subscribed": user.get("is_subscribed", False),
        "daily_usage": user.get("daily_usage", 0),
        "total_urls": user.get("total_urls", 0)
    }

from fastapi import APIRouter, Depends, HTTPException
from app.models.user import UserInDB
from app.api.deps import get_current_user
from app.helpers.utilities import URLDataStore
from app.schemas.auth import UpdateUserRequest
from app.services.user_service import updateUser

router = APIRouter(prefix="/user", tags=["user"])

#   get a user
@router.get("/me")
async def read_current_user(user: dict = Depends(get_current_user)):
    return {
        "email": user["email"],
        "is_subscribed": user.get("is_subscribed", False),
        "daily_usage": user.get("daily_usage", 0),
        "total_urls": user.get("total_urls", 0)
    }


#   update a user
@router.put("/update-me")
async def update_user(update: UpdateUserRequest, user: dict = Depends(get_current_user)):
    try:
        return await updateUser(update, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


#   delete the user
@router.delete("/delete-me")
async def delete_user(user: dict = Depends(get_current_user)):
    db = URLDataStore().mongoDb
    users_collection = db["users"]
    result = await users_collection.delete_one({"email": user["email"]})
    if result.deleted_count == 0:
        raise HTTPException(status_code=400, detail="User deletion failed")
    return {"msg": "User deleted successfully"}

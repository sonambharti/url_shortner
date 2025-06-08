# from app.db.mongodb import users_collection
from app.helpers.utilities import URLDataStore
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException
from datetime import timedelta, datetime


async def updateUser(update, user):
    update_data = update.model_dump(exclude_unset=True)
    # Hash password if present
    if "password" in update_data:
        # update_data["password"] = hash_password(update_data.pop("password"))
        update_data["password"] = hash_password(update_data["password"])

    # ✅ Always update created_at or better: updated_at
    update_data["created_at"] = datetime.now()

    db = URLDataStore().mongoDb
    users_collection = db["users"]
    result = await users_collection.update_one(
        {"email": user["email"]},
        {"$set": update_data}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Update failed or nothing changed")

    # Create fresh token after update
    token = create_access_token({"sub": str(user["_id"])}, timedelta(minutes=60))
    return {
        "access_token": token,
        "token_type": "bearer",
        "msg": "User updated successfully"
    }
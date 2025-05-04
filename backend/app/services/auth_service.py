from app.db.mongodb import users_collection
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.auth import RegisterRequest, LoginRequest
from app.models.user import UserInDB
from datetime import timedelta

def register_user(data: RegisterRequest):
    if users_collection.find_one({"email": data.email}):
        raise ValueError("Email already registered")

    hashed_pw = hash_password(data.password)
    user_data = {
        "email": data.email,
        "password": hashed_pw,
        # "is_subscribed": False,
        # "daily_usage": 0,
        # "total_urls": 0
    }
    user = UserInDB(user_data).model_dump()
    users_collection.insert_one(user)
    return {"msg": "User registered successfully"}

def login_user(data: LoginRequest):
    user_doc = users_collection.find_one({"email": data.email})
    # print("user document: \n", user_doc)
    if not user_doc or not verify_password(data.password, user_doc["password"]):
        raise ValueError("Invalid credentials")

    token = create_access_token({"sub": str(user_doc["_id"])}, timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}

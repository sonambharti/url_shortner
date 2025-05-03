from app.db.mongodb import users_collection
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.auth import RegisterRequest, LoginRequest
from app.models.user import UserInDB
from datetime import timedelta

def register_user(data: RegisterRequest):
    if users_collection.find_one({"email": data.email}):
        raise ValueError("Email already registered")

    hashed_pw = hash_password(data.password)
    user = UserInDB(email=data.email, hashed_password=hashed_pw).dict()
    users_collection.insert_one(user)
    return {"msg": "User registered successfully"}

def login_user(data: LoginRequest):
    user_doc = users_collection.find_one({"email": data.email})
    if not user_doc or not verify_password(data.password, user_doc["hashed_password"]):
        raise ValueError("Invalid credentials")

    token = create_access_token({"sub": str(user_doc["_id"])}, timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}

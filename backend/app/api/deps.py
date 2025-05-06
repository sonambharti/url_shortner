from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from app.core.security import decode_access_token
# from app.db.mongodb import users_collection
from bson import ObjectId
from app.helpers.utilities import URLDataStore

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        if payload is None:
            raise credentials_exception

        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        db = URLDataStore().mongoDb
        users_collection = db["users"]
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise credentials_exception

        return user  # You can return a Pydantic User schema if needed
    except InvalidTokenError:
        raise credentials_exception

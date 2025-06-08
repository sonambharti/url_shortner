from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from app.core.security import decode_access_token
# from app.db.mongodb import users_collection
from bson import ObjectId
from app.helpers.utilities import URLDataStore
import time

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
        token_iat = payload.get("iat")
        
        if user_id is None or token_iat is None:
            raise credentials_exception
        
        db = URLDataStore().mongoDb
        users_collection = db["users"]
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        
        if user is None:
            raise credentials_exception

        user_created_at = user.get("created_at")
        if not user_created_at:
            raise credentials_exception

        # ✅ Convert timestamps to same format
        # if isinstance(user_created_at, str):
        #     user_created_at = datetime.fromisoformat(user_created_at)
        # elif isinstance(user_created_at, datetime):
        #     pass
        # else:
        #     raise credentials_exception

        # token_issued_time = datetime.utcfromtimestamp(token_iat)

        # ✅ Compare issue time and created_at
        # if token_issued_time < user_created_at:
        if token_iat < user_created_at:
            raise HTTPException(status_code=401, detail="Token issued before user was created/updated")
        print(f'In try, User: {user}')
        return user
    except InvalidTokenError:
        print(f'In except, User: {credentials_exception}')
        raise credentials_exception
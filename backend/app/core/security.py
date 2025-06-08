# app/core/security.py
import jwt, time
from datetime import datetime, timedelta
import bcrypt
import os
from app.core.config import JWT_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

# print(f"JWT: {JWT_SECRET_KEY}")
# print(f"Algorithm: {ALGORITHM}")
# print(f"Access Token Expire minutes: {ACCESS_TOKEN_EXPIRE_MINUTES}")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    now = int(time.time())
    expire = now + ACCESS_TOKEN_EXPIRE_MINUTES * 60 # (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({
        "exp": expire,
        "iat": now  # ✅ add issued-at timestamp
    })
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM,]) # options={"verify_signature": False}
        return payload
    except ExpiredSignatureError as e:
        raise e
    except InvalidTokenError as e:
        raise e
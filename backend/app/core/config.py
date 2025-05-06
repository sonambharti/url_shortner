import os
from dotenv import load_dotenv

# Load variables from .env file (if you're using one)
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
# Secret key for JWT
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")  # Change this in production

# Algorithm for encoding JWTs
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Token expiration in minutes (optional)
ACCESS_TOKEN_EXPIRE_MINUTES = 60

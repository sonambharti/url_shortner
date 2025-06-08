import logging
# from pymongo import MongoClient
from pymongo import errors
import motor.motor_asyncio
from app.core.config import MONGO_URI, DB_NAME
import os


# Set up logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if not MONGO_URI:
    logger.error("MONGO_URI environment variable is not set")
    raise EnvironmentError("MONGO_URI environment variable is not set")

async def mongoConnection():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]  # Replace "your_database_name" with your database name
        logger.info("Successfully connected to MongoDB")
    except errors.ConnectionFailure as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        raise ConnectionError(f"Failed to connect to MongoDB: {e}")
        
    return db


# try:
#     client = MongoClient(MONGO_URI)
#     db = client.url_shortener_db
#     users_collection = db.users
#     logger.info("Successfully connected to MongoDB")
# except errors.ConnectionFailure as e:
#     logger.error(f"Failed to connect to MongoDB: {e}")
#     raise ConnectionError(f"Failed to connect to MongoDB: {e}")

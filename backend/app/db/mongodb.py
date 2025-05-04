import logging
from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()

# Set up logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    logger.error("MONGO_URI environment variable is not set")
    raise EnvironmentError("MONGO_URI environment variable is not set")

try:
    client = MongoClient(MONGO_URI)
    db = client.url_shortener_db
    users_collection = db.users
    logger.info("Successfully connected to MongoDB")
except errors.ConnectionFailure as e:
    logger.error(f"Failed to connect to MongoDB: {e}")
    raise ConnectionError(f"Failed to connect to MongoDB: {e}")

from dotenv import dotenv_values
import os
from pymongo import MongoClient
from dotenv import load_dotenv 
load_dotenv()
import motor.motor_asyncio
import time
from helpers.utilities import EpiDataStore

config = dotenv_values(".env")

def connection():
    print("Triggered Database Connection")
    mongodb_client = MongoClient(os.environ.get("ATLAS_URI"))
    database = mongodb_client[os.environ.get("DB_NAME")]
    return database

async def mongo_connection_obj():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("ATLAS_URI"))
    db = client[os.environ.get("DB_NAME")]  # Replace "your_database_name" with your database name
    return db


async def get_data_from_db(tableName,query):
    in_time = time.time()
    cursor = EpiDataStore().mongoDb[f"{tableName}"].find(query)

    documents = []
    async for document in cursor:
        documents.append(document)
    print(f"Time Taken by get_response_from_db data count {len(documents)} {str(time.time() - in_time)}")
    return documents

async def upsert_data_into_db(tableName,query,value):
    in_time = time.time()
    cursor = EpiDataStore().mongoDb[f"{tableName}"].update_one(query,value,upsert=True)
    print(f"Time Taken by upsert_data_into_db  {str(time.time() - in_time)}")
    return cursor

async def insert_one_into_db(tableName,value):
    in_time = time.time()
    cursor = EpiDataStore().mongoDb[f"{tableName}"].insert_one(value)
    print(f"Time Taken by insert_one_into_db  {str(time.time() - in_time)}")
    return cursor


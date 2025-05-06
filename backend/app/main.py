from fastapi import FastAPI
from app.api.routes import auth, user
import uvicorn
import asyncio
from app.db.mongodb import mongoConnection
from app.helpers.utilities import URLDataStore

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to the URL Shortener"}



# if __name__ == "__main__":
#     # uvicorn.run(app, host="0.0.0.0", port=8000)
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

async def startup_event():
    URLDataStore().mongoDb = await mongoConnection()

asyncio.get_event_loop().create_task(startup_event())

"""
from app.core.log_config import listener

@app.on_event("shutdown")
def shutdown_event():
    listener.stop()

"""